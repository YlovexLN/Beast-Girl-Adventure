# <center>Mod-UpdateScript<center>

### generate-mod-list.bat

该脚本通过 CurseForge API 获取指定的 mod 信息，包括 mod 名称、版本号、下载地址，并将这些信息组成 json 格式的 mod 统计列表文件。
文件名为 mod-list.json，并存储在指定的本地文件夹（在此脚本中为./temp）中。
具体步骤如下：
设置 mod ID 列表以及 CurseForge API URL
遍历 mod ID 列表，发送 HTTP 请求获取 mod 信息，提取名称、版本号、下载地址等信息，存入一个对象数组中
将对象数组转换为 json 字符串，写入 mod-list.json 文件中

### update-mods.bat

该脚本用于检查 mod 文件夹中的 mod 文件是否需要更新，并自动更新。
具体步骤如下：
检查 mods 文件夹是否存在，不存在则创建
检查 mod-list.json 文件是否存在，不存在则从指定的 github 仓库中下载
读取 mod-list.json 文件中的 mod 信息，遍历 mod 列表
对于每个 mod，检查本地 mods 文件夹中是否存在该 mod 的 jar 文件
如果存在，比较版本号，如果需要更新则从下载地址下载最新版本的 jar 文件并替换旧文件
如果不存在，从下载地址下载最新版本的 jar 文件，并放入 mods 文件夹中

---

这只是一个测试
目前还在写，不知道什么时候能写好。我知道你很急，但你先别急。
