@echo off
setlocal EnableDelayedExpansion

set CF_PROJECT_ID=12345  REM 替换成你的CurseForge项目ID
set GITHUB_USERNAME=YourUsername REM 替换成你的GitHub用户名
set GITHUB_REPO=YourRepository REM 替换成你的GitHub仓库名

REM 通过CurseForge API获取mod信息
powershell -Command "& {Invoke-WebRequest 'https://addons-ecs.forgesvc.net/api/v2/addon/%CF_PROJECT_ID%' -OutFile mod_info.json}"
set /p mod_name=< mod_info.json | jq -r '.name'
set /p mod_version=< mod_info.json | jq -r '.latestFiles[0].displayName'
set /p mod_download_url=< mod_info.json | jq -r '.latestFiles[0].downloadUrl'

REM 生成mod统计列表
echo [{>"mod-list.json"
echo     "name":"%mod_name%",>>"mod-list.json"
echo     "version":"%mod_version%",>>"mod-list.json"
echo     "download_url":"%mod_download_url%" >>"mod-list.json"
echo }]>>"mod-list.json"

REM 上传到GitHub
git add mod-list.json
git commit -m "Update mod list"
git push origin main
