echo f | xcopy /f /y Data.wz Data.wz.bak
"..\Harepacker-resurrected\HaRepackerCLI\HarepackerCLI\bin\Debug\net8.0-windows7.0\HarepackerCLI.exe" "42e3fbee-cbe9-4366-ae4e-c38d651d7dc2" ".\\" "Data.wz" "packignore.txt"
cd ..\rsvp-server
SignDataFile.bat
cd ..\rsvp-data
