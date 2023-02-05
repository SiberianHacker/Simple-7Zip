import os
print("7Zip archives cracker by SiberianHacker...")
passwfile = open("passwords.txt", "r")
print("\n\n\n\n[ru] Файл должен находиться в папке со скриптом!\n\n[en] the file must be in the folder with the script! \n\n")
path = input("7z file: ")
for pas in passwfile.readlines():
    pas = pas.strip()
    print("Checking password " + pas)
    try:
        os.system('7zG.exe e test.7z -y -bd -ohacked_archive -p' + pas)
    except:
        pass