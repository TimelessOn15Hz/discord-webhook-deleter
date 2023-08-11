# IMPORTS
import os
try:
    from colorama import Fore, init
except:
    os.system("python.exe -m pip install colorama")
    from colorama import Fore, init
try:
    import requests
except:
    os.system("python.exe -m pip install requests")
    import requests

from banner import banner

init()
os.system("title WEBHOOK DELETER")
banner = (Fore.RED + banner)

def main():
    print(banner)
    webhook = input(" [INPUT] ENTER WEBHOOK URL : ")

    test = requests.get(webhook)
    if test.status_code == 404:
        print("\n [OUTPUT] THE WEBHOOK IS INVALID")
        print("\n PRESS ANY KEY TO EXIT")
        os.system("pause >nul")
    elif test.status_code == 200:
        print("\n [OUTPUT] WEBHOOK IS VALID -- DELETING WEBHOOK")
        delete()

    def delete():
        requests.delete(webhook)
        check = requests.get(webhook)
        status = check.status_code
        if status == 404:
            print("\n [OUTPUT] WEBHOOK SUCCESFULLY DELETED")
            print("\n PRESS ANY KEY TO EXIT")
            os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
        elif status == 200:
            print(f"\n [OUTPUT] FAILED TO DELETE WEBHOOK -- STATUS CODE {status}")
            print("\n PRESS ANY KEY TO EXIT")
            os.system("pause >nul")

if __name__ == '__main__':
    main()