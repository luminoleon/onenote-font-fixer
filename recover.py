import os
import shutil

import onenote_font_fixer

def main():
    onmain_dll_dir = onenote_font_fixer.get_onmain_dll_dir()
    if onmain_dll_dir == None:
        onenote_font_fixer.log("没有找到{}。".format(onenote_font_fixer.DLL_NAME), "error")
        exit(1)
    onmain_dll_path = onmain_dll_dir.rstrip("\\") + "\\" + onenote_font_fixer.DLL_NAME
    onmain_dll_bak_path = onmain_dll_dir.rstrip("\\") + "\\" + onenote_font_fixer.DLL_BAK_NAME
    onenote_font_fixer.log("已找到{}位置：{}。".format(onenote_font_fixer.DLL_NAME, onmain_dll_path))
    if os.path.exists(onmain_dll_bak_path):
        try:
            shutil.move(onmain_dll_bak_path, onmain_dll_path)
        except PermissionError as e:
            onenote_font_fixer.log("权限错误：请关闭OneNote并以管理员身份运行。".format(e), "error")
        except Exception as e:
            onenote_font_fixer.log("未知错误：{}。".format(e), "error")
        else:
            onenote_font_fixer.log("恢复成功。")
    else:
        onenote_font_fixer.log("没有找到{}。可能已经恢复。".format(onenote_font_fixer.DLL_BAK_NAME), "error")
    os.system("powershell pause")

if __name__ == "__main__":
    main()
