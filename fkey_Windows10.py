from os import system
Sys_ver=input("1- Home\n2- Home N\n3- Home Single Language\n4- Home Country Specific\n5- Professional\n6- Professional N\n7- Education\n8- Education N\n9- Entreprise\n10- Entreprise N\n\n[1-10]:")
if Sys_ver == 1:
    Sys_key = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
if Sys_ver == 2:
    Sys_key = "3KHY7-WNT83-DGQKR-F7HPR-844BM"
if Sys_ver == 3:
    Sys_key = "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
if Sys_ver == 4:
    Sys_key = "PVMJN-6DFY6–9CCP6–7BKTT-D3WVR"
if Sys_ver == 5:
    Sys_key = "W269N-WFGWX-YVC9B-4J6C9-T83GX"
if Sys_ver == 6:
    Sys_key = "MH37W-N47XK-V7XM9-C7227-GCQG9"
if Sys_ver == 7:
    Sys_key = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
if Sys_ver == 8:
    Sys_key = "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"
if Sys_ver == 9:
    Sys_key = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
if Sys_ver == 10:
    Sys_key = "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
system("slmgr /ipk "+Sys_key)
system("slmgr /skms kms8.msguides.com")
system("slmgr /ato")
print("By Psyquoquack") 