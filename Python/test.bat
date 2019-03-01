SET src=c:\users\Aaron\Desktop\test
SET dest=c:\users\Aaron\Desktop\test2

REM robocopy %src% %dest%

FOR /F "delims=" %%i IN ('DIR /b %src%') DO MOVE "%src%\%%i" "%dest%\%%i"