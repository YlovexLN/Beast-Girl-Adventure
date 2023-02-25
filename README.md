<h1 align="center">Mod-UpdateScript</h1>

### generate-mod-list.bat

通过 CurseForge API 获取指定的 mod 信息，包括 mod 名称、版本号、下载地址，

并将这些信息组成 json 格式的 mod-list

最后再将 mod-list 上传到 GitHub 方便于本地的 mod-list 对比。

### update-mods.bat

检测远程仓库的 mod-list 与本地 mod-list 是否不一样

从而找到对应的 mod 实现 mod 更新。

---

这只是一个测试
目前还在写，不知道什么时候能写好。我知道你很急，但你先别急。

#### 已知问题：

**[机械动力]**Create
**Forge**版 **mod_id:** 328085
目前只会返回两个版本的Mod详细信息
**1.14.4**和**1.19.2**

如下：

~~~json
"id": 328085,
        "gameId": 432,
        "name": "Create",
        "links": "https://www.curseforge.com/minecraft/mc-mods/create",
        "latestFiles": [
            {
                "id": 2952509,
                "modid": 328085,
                "displayName": "Create 1.14.4 v0.2.3",
                "fileName": "create-mc1.14.4_v0.2.3.jar",
                "fileDate": "2020-05-09T17:25:03.4Z",
                "downloadUrl": "https://edge.forgecdn.net/files/2952/509/create-mc1.14.4_v0.2.3.jar",
                "gameVersions": [
                    "1.14.4",
                    "Forge"
                ]
            },
            {
                "id": 4371809,
                "modid": 328085,
                "displayName": "Create 1.19.2 v0.5.0i",
                "fileName": "create-1.19.2-0.5.0.i.jar",
                "fileDate": "2023-01-29T23:43:02.557Z",
                "downloadUrl": "https://edge.forgecdn.net/files/4371/809/create-1.19.2-0.5.0.i.jar",
                "gameVersions": [
                    "1.19.2",
                    "Forge"
                ]
            }
        ]
~~~

我这里已经是筛选掉没有用的信息之后的结果，如果你需要这两个版本之外的版本
请自行去[CurseForge](https://www.curseforge.com/minecraft/mc-mods/create)下载  （👈点击超链接直接跳转至Mod页面）
