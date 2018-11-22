@echo off
SETLOCAL EnableExtensions
set device_one = "Speakers"
set device_two = "Digital Audio (S/PDIF)"
set EXE=GameBarPresenceWriter.exe
:start
FOR /F %%x IN ('tasklist /NH /FI "IMAGENAME eq %EXE%"') DO IF %%x == %EXE% goto FOUND
echo Not running
nircmd.exe setdefaultsounddevice %device_two%

goto FIN
:FOUND
echo Running
nircmd.exe setdefaultsounddevice %device_one%

:FIN
ENDLOCAL