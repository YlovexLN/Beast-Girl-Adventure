@echo off
chcp 65001
set modid=531749 240908
set gameversion=1.16.5

echo 测试是否能正常访问CurseForge...
powershell -Command "Invoke-WebRequest -Uri 'https://minecraft.curseforge.com' -UseBasicParsing -TimeoutSec 5"
if %errorlevel% neq 0 (
    echo 访问CurseForge失败 请选择操作
    echo 1. 直接通过gitee仓库链接下载mod压缩包
    echo 2. 手动设置代理服务器 http://127.0.0.1:7890/
    set /p choice=请选择：
    if %choice% equ 1 (
        echo 开始下载mod...
        powershell -Command "Invoke-WebRequest -Uri 'https://gitee.com/example/repo-name/raw/branch-name/mods/my-mod-id-1.0.0.jar' -OutFile 'my-mod-id-1.0.0.jar'"
        if %errorlevel% equ 0 (
            echo 下载完成。
            echo ^{^"name^": ^"My Mod Name^", ^"version^": ^"1.0.0^", ^"download^": ^"./my-mod-id-1.0.0.jar^"^} > mod-list.json
            echo mod信息已输出到mod-list.json文件。
        ) else (
            echo 下载失败 请检查modid和gitee仓库链接是否正确。
        )
    ) else (
        set /p proxy=请输入代理服务器地址格式如 http://127.0.0.1:7890/
        echo 测试代理服务器是否可用...
        powershell -Command "Invoke-WebRequest -Uri 'https://minecraft.curseforge.com' -UseBasicParsing -TimeoutSec 5 -Proxy %proxy%"
        if %errorlevel% neq 0 (
            echo 代理服务器不可用，请检查地址是否正确。
        ) else (
            echo 访问CurseForge的代理服务器已设置。
            goto get_mod_info
        )
    )
) else (
    echo 可以正常访问CurseForge。
    goto get_mod_info
)

:get_mod_info
echo 获取mod信息...
powershell -Command "$json = Invoke-WebRequest -Uri 'https://addons-ecs.forgesvc.net/api/v2/addon/%modid%/file/%gameversion%' -UseBasicParsing | ConvertFrom-Json; $mod_name = $json.gameVersionLatestFiles.projectFile.displayName; $mod_version = $json.gameVersionLatestFiles.projectFile.version; $mod_download = $json.gameVersionLatestFiles.projectFile.downloadUrl; $output = @{'name'=$mod_name;'version'=$mod_version;'download'=$mod_download} | ConvertTo-Json; echo $output > mod-list.json"
echo mod信息已输出到mod-list.json文件。
pause