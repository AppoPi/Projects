@echo off

set text=
for /f "delims=" %%a in ('ver') do @set os=%%a
if "%os%" == "Microsoft Windows [Version 6.3.9600]" (set text=Windows 8.1)
if "%os%" == "Microsoft Windows [Version 6.2.9200]" (set text=Windows 8)
if "%os%" == "Microsoft Windows [Version 6.1.7601]" (set text=Windows 7 SP1)
if "%os%" == "Microsoft Windows [Version 6.1.7600]" (set text=Windows 7)
if "%os%" == "Microsoft Windows [Version 6.0.6002]" (set text=Windows Vista SP2)
if "%os%" == "Microsoft Windows [Version 6.0.6000]" (set text=Windows Vista)
if "%os%" == "Microsoft Windows XP [Version 5.1.2600]" (set text=Windows XP)

set architecture=
if exist "%ProgramFiles(x86)%" (
	set architecture=x64
)
if not exist "%ProgramFiles(x86)%" (
	set architecture=x86
)

echo %text% %architecture%
