@echo off
setlocal EnableDelayedExpansion

set GITHUB_USERNAME=YourUsername REM 替换成你的GitHub用户名
set GITHUB_REPO=YourRepository REM 替换成你的GitHub仓库名

REM 创建mods文件夹
if not exist mods mkdir mods

REM 检查mod统计列表是否存在，若不存在则从GitHub下载
if not exist "mods\mod-list.json" (
  powershell -Command "& {Invoke-WebRequest 'https://raw.githubusercontent.com/%GITHUB_USERNAME%/%GITHUB_REPO%/main/mod-list.json' -OutFile 'mods\mod-list.json'}"
)

REM 比较mod统计列表和本地mods文件夹中的mod文件，并删除旧版本的mod文件
for /f "tokens=1,2,3 delims=," %%i in ('type "mods\mod-list.json" ^| jq -r ".[] | [.name, .version, .download_url] | @csv"') do (
  set "mod_name=%%~i"
  set "mod_version=%%~j"
  set "mod_download_url=%%~k"

  REM 下载最新的mod文件
  powershell -Command "& {Invoke-WebRequest '%mod_download_url%' -OutFile 'mods\%mod_name%-%mod_version%.jar'}"

  REM 删除低版本的mod文件
  for %%f in ("mods\%mod_name%-*.jar") do (
    for /f "delims=-" %%a in ("%%~nf") do (
      if "!mod_version!" LSS "%%a" (
        del "%%~f"
      )
    )
  )
)
