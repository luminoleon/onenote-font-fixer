# OneNote Font Fixer

解决Win32版OneNote中英文字体不同的问题。对UWP版OneNote无效。

通过注册表定位OneNote的安装位置，直接修改对应dll文件的内容来修复字体问题。

## 使用方法

### 可执行文件

注意：由于存在修改dll文件的行为，可执行文件可能会被杀毒软件拦截。

1. [下载](https://github.com/luminoleon/onenote-font-fixer/releases)
2. 以管理员身份运行`onenote_font_fixer.exe`。

### Python脚本

1. [下载](https://github.com/luminoleon/onenote-font-fixer/releases)
2. 以管理员身份运行命令`python onenote_font_fixer.py`。

## 如何恢复

以管理员身份运行`recover.exe`或者命令`python recover.py`。

## 注意事项

* OneNote更新会覆盖原来的dll文件使修改失效，需要重新运行此程序来恢复更改。
* 此程序对有些版本的OneNote可能无效。
* 如果运行此程序后问题没有得到修复，请恢复更改以避免引起其他问题。

## 参考

* [接力治愈强迫症，onenote 2016字体防切换！ - rec0rd - 博客园](https://www.cnblogs.com/rec0rd/p/14761148.html)
* [OneFont for OneNote防止字体切换工具 – LXF's X Factory](https://lxf.me/116?unapproved=815&moderation-hash=cf6f75f95c7e998e75cbc001a0c905f9)
