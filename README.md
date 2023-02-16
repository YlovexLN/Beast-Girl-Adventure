### generate-mod-list.bat
该脚本通过CurseForge API获取指定的mod信息，包括mod名称、版本号、下载地址，并将这些信息组成json格式的mod统计列表文件。
文件名为mod-list.json，并存储在指定的本地文件夹（在此脚本中为./temp）中。
具体步骤如下：
    设置mod ID列表以及CurseForge API URL
    遍历mod ID列表，发送HTTP请求获取mod信息，提取名称、版本号、下载地址等信息，存入一个对象数组中
    将对象数组转换为json字符串，写入mod-list.json文件中
### update-mods.bat
该脚本用于检查mod文件夹中的mod文件是否需要更新，并自动更新。
具体步骤如下：
    检查mods文件夹是否存在，不存在则创建
    检查mod-list.json文件是否存在，不存在则从指定的github仓库中下载
    读取mod-list.json文件中的mod信息，遍历mod列表
    对于每个mod，检查本地mods文件夹中是否存在该mod的jar文件
    如果存在，比较版本号，如果需要更新则从下载地址下载最新版本的jar文件并替换旧文件
    如果不存在，从下载地址下载最新版本的jar文件，并放入mods文件夹中

---
代码中使用中文注释和echo语句，以提高代码可读性和可维护性。同时，由于bat脚本本身是Windows系统自带的脚本语言，因此使用PowerShell的Invoke-WebRequest进行下载操作，以保证兼容性。
