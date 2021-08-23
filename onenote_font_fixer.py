import os
import shutil
from typing import Optional
import winreg

BYTES_OLD = "680203"
BYTES_NEW = "680003"
BYTES64_OLD = "B90203"
BYTES64_NEW = "B90003"
DLL_NAME = "onmain.DLL"
DLL_BAK_NAME = "onmain.DLL.bak"

def get_reg_value(key: int, sub_key: str, value_name: str) -> str:
    try:
        key = winreg.OpenKey(key, sub_key)
        value = winreg.QueryValueEx(key, value_name)[0]
        return value
    except:
        return None

def find_reg_key(key: int, sub_key: str, key_name_partial: str) -> str:
    key = winreg.OpenKey(key, sub_key)
    i = 0
    while True:
        try:
            package_name = winreg.EnumKey(key, i)
        except:
            return None
        if key_name_partial in package_name:
            key_full = sub_key.rstrip("\\") + "\\" + package_name
            return key_full
        i += 1

def dll_replace(path: str, backup_path: str, old: str, new: str) -> bool:
    dll = open(path, "rb+")
    dll_bytes = dll.read()
    if dll_bytes.find(bytes.fromhex(old)) >= 0:
        shutil.copy(path, backup_path)
        dll_bytes_replaced = dll_bytes.replace(bytes.fromhex(old), bytes.fromhex(new), 1)
        dll.seek(0)
        dll.write(dll_bytes_replaced)
        dll.close()
        return True
    else:
        return False

def log(text: str, level: str = "info") -> None:
    if level == "info":
        print("{}".format(text))
    elif level == "warning":
        print("警告：{}".format(text))
    elif level == "error":
        print("错误：{}".format(text))

def machine_type(path: str) -> Optional[str]:
    dll = open(path, "rb")
    dll_bytes = dll.read()
    dll.close()
    pe_index = dll_bytes.find(bytes.fromhex("50450000"))
    machine_types = dll_bytes[pe_index + 4 : pe_index + 6]
    if machine_types == bytes.fromhex("6486"):
        return "x64"
    elif machine_types == bytes.fromhex("4C01"):
        return "x86"

def get_onmain_dll_dir() -> str:
    onmain_dll_dir = get_reg_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\OneNote.exe", "Path")
    return onmain_dll_dir

def main() -> None:
    onmain_dll_dir = get_onmain_dll_dir()
    if onmain_dll_dir == None:
        log("没有找到{}。".format(DLL_NAME), "error")
        exit(1)
    onmain_dll_path = onmain_dll_dir.rstrip("\\") + "\\" + DLL_NAME
    nomain_dll_bak_path = onmain_dll_dir.rstrip("\\") + "\\" + DLL_BAK_NAME
    log("已找到{}位置：{}。".format(DLL_NAME, onmain_dll_path))
    dll_machine_type = machine_type(onmain_dll_path)
    if dll_machine_type == None:
        log("无法识别dll类型。", "error")
        exit(1)
    log("{}版本：{}。".format(DLL_NAME, dll_machine_type))
    try:
        successed = False
        if dll_machine_type == "x64":
            successed = dll_replace(onmain_dll_path, nomain_dll_bak_path, BYTES64_OLD, BYTES64_NEW)
        elif dll_machine_type == "x86":
            successed = dll_replace(onmain_dll_path, nomain_dll_bak_path, BYTES_OLD, BYTES_NEW)
    except PermissionError as e:
        log("权限错误：请关闭OneNote并以管理员身份运行。".format(e), "error")
    except Exception as e:
        log("未知错误：{}。".format(e), "error")
    else:
        if successed:
            log("替换成功。")
        else:
            log("已替换或dll版本不匹配。")
    os.system("powershell pause")

if __name__ == "__main__":
    main()
