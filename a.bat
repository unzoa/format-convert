@echo off
setlocal enabledelayedexpansion

rem 设置源文件扩展名和目标文件扩展名
set "source_ext=jpg"
set "target_ext=webp"

rem 循环遍历当前目录中所有源扩展名的文件
for %%f in (*.%source_ext%) do (
    rem 获取文件名（不包括扩展名）
    set "filename=%%~nf"
    rem 重命名文件扩展名
    ren "%%f" "!filename!.%target_ext%"
)

echo 完成所有 %source_ext% 文件重命名为 %target_ext% 文件。
endlocal
pause
