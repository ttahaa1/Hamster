try:
 import requests,os
 import time
 from cfonts import render, say
 from colorama import init, Fore, Style
 from datetime import datetime
 from itertools import cycle
 import json
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install colorama')
 os.system('pip install cfonts')
 os.system('pip install itertools')
 os.system('clear')
b='\033[31m' #red
g='\033[32m' #green
y='\033[33m' #yellow
p='\033[34m' #blue
m='\033[35m' #magenta
c='\033[36m' #cyan
w='\033[37m' #white
def JOK(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)
output = render('JOKER', colors=['white', 'blue'], align='center')
print (output)
JOK(m+f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : JOKER ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: @X1_H9 \n                            ᴄʜᴀɴɴᴇʟ : @TEAM_JO  』", 0.07, True)
JOK(c+f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 0.07, True)
bot = '6362717551:AAG5yExgcHkJns-4DsJZuCGZG3sXncQJ-Z4'
acc = '5957072350'
def load_tokens(filename):
  with open(filename, 'r') as file:
      return [line.strip() for line in file]
def get_token(init_data_raw):
  url = 'https://api.hamsterkombat.io/auth/auth-by-telegram-webapp'
  headers = {
      'Accept-Language': 'en-US,en;q=0.9',
      'Connection': 'keep-alive',
      'Origin': 'https://hamsterkombat.io',
      'Referer': 'https://hamsterkombat.io/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
      'accept': 'application/json',
      'content-type': 'application/json'
  }
  data = json.dumps({"initDataRaw": init_data_raw})
  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
      return response.json()['authToken']
  else:
      error_data = response.json()
      if "invalid" in error_data.get("error_code", "").lower():
          print(Fore.RED + Style.BRIGHT + "\rFailed Get Token. Invalid init data", flush=True)
      else:
          print(Fore.RED + Style.BRIGHT + f"\rFailed Get Token. {error_data}", flush=True)
      return None
cek_task_dict = {}
def main():
    global cek_task_dict
    print(Fore.GREEN + Style.BRIGHT + "Starting Hamster Kombat....\n\n")
    init_data = load_tokens('JOKER.txt')
    token_cycle = cycle(init_data)

    token_dict = {}
    while True:
        init_data_raw = next(token_cycle)
        token = token_dict.get(init_data_raw)

        if token:
            print(Fore.GREEN + Style.BRIGHT + f"\rBY JOKER•••", end="", flush=True)
        else:
            print(Fore.GREEN + Style.BRIGHT + f"\rGet Token•••", end="", flush=True)

            token = get_token(init_data_raw)
            if token:
                token_dict[init_data_raw] = token
                print(Fore.GREEN + Style.BRIGHT + f"\rThe token was obtained successfully ",token, flush=True)
            else:
                print(Fore.RED + Style.BRIGHT + f"\rSwitch to the next account \n\n", flush=True)
                continue        
        headers = {
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://hamsterkombat.io',
    'Referer': 'https://hamsterkombat.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

        json_data = {
    'count': 50,
    'availableTaps': 3500,
    'timestamp': int(time.time()),
}

        response = requests.post('https://api.hamsterkombat.io/clicker/tap', headers=headers, json=json_data)
        if response.status_code == 200:
        	coin = response.json()["clickerUser"]["balanceCoins"]
        	print(g+f' ➜ Done Add 200 coin✅ | {coin} BY: @X1_H9')
        	tlg = f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={acc}&text=•  ➜ Done Add 200 coin✅ | {coin} BY: @X1_H9"
        	tlg_params = {"parse_mode": "HTML"}
        	i = requests.post(tlg, params=tlg_params)
        else:
        	print(b+f' ➜ ERROR ADD COIN')
        	tlg = f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={acc}&text=•  ➜ ERROR ADD COIN | {coin} BY:@X1_H9"
        	tlg_params = {"parse_mode": "HTML"}
        	i = requests.post(tlg, params=tlg_params)
        time.sleep(25)
if __name__ == "__main__":
  main()
