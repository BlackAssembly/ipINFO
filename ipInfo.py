import os
import requests
import socket
import sys
from datetime import datetime

def portS():



    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    try:

        # will scan ports between 1 to 65,535
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()



def ipinfo():

    ip = (target)

    def ipinnfo():

        print("")
        url = f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'demo.ip-api.com',
            'Origin': 'https://ip-api.com',
            'Referer': 'https://ip-api.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        req = requests.post(url, headers=headers)
        print(f'\033[31m[+]  status :  \033[32m' + req.json()['status'])
        print(f'\033[31m[+]  continent :  \033[32m' + req.json()['continent'])
        print(f'\033[31m[+]  continentCode : \033[32m' + req.json()['continentCode'])
        print(f'\033[31m[+]  country : \033[32m' + req.json()['country'])
        print(f'\033[31m[+]  countryCode : \033[32m' + req.json()['countryCode'])
        print(f'\033[31m[+]  region :  \033[32m' + req.json()['region'])
        print(f'\033[31m[+]  regionName : \033[32m' + req.json()['regionName'])
        print(f'\033[31m[+]  city : \033[32m' + req.json()['city'])
        print(f'\033[31m[+]  district : \033[32m' + req.json()['district'])
        print(f'\033[31m[+]  zip : \033[32m' + req.json()['zip'])
        print(f'\033[31m[+]  timezone : \033[32m' + req.json()['timezone'])
        print(f'\033[31m[+]  currency : \033[32m' + req.json()['currency'])
        print(f'\033[31m[+]  isp : \033[32m' + req.json()['isp'])
        print(f'\033[31m[+]  as : \033[32m' + req.json()['as'])
        print(f'\033[31m[+]  asname : \033[32m' + req.json()['asname'])
        print(f'\033[31m[+]  query : \033[32m' + req.json()['query'])
        print(f'\033[31m[+]  lat : \033[32m' + str(req.json()['lat']))
        print(f'\033[31m[+]  lon : \033[32m' + str(req.json()['lon']))
        print(f'\033[31m[+]  offset : \033[32m' + str(req.json()['offset']))
        print(f'\033[31m[+]  mobile : \033[32m' + str(req.json()['mobile']))
        print(f'\033[31m[+]  proxy : \033[32m' + str(req.json()['proxy']))
        print(f'\033[31m[+]  hosting : \033[32m' + str(req.json()['hosting']))

        req3 = requests.get(f'https://ipapi.co/{ip}/json/')
        print(f'\033[31m[+]  version :  \033[32m' + str(req3.json()['version']))
        print(f'\033[31m[+]  asn :  \033[32m' + str(req3.json()['asn']))
        print(f'\033[31m[+]  Location : \033[32m' + str(req.json()['lat']) + ',' + str(req.json()['lon']))

    ipinnfo()
target = input("enter ip : ")
print("""
[1] ip info

[2] port scanner

[3] ip info and then port scanner
""")
choose = input("what do you need : ")
if choose == "1":
    ipinfo()
elif choose == '2':
    portS()
elif choose == '3':
    ipinfo()
    portS()