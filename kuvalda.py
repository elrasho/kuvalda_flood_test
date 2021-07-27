import threading, sys, os, requests, argparse
from fake_useragent import UserAgent
from clr import splv
from msgs import Messages

parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, default=None, help="Website URL")
parser.add_argument("--req", type=int, default=50, help="How many requests to do")
parser.add_argument("--output", type=int, default=1, help="Show output? (0,1)")
args = parser.parse_args()
msg = Messages

def logo():
    print("""
  _                     _     _       
 | |                   | |   | |      
 | | ___   ___   ____ _| | __| | __ _ 
 | |/ / | | \ \ / / _` | |/ _` |/ _` |
 |   <| |_| |\ V / (_| | | (_| | (_| |
 |_|\_\\__,_| \_/ \__,_|_|\__,_|\__,_|
                                      
                                      
          """)

if args.url is None:
    sys.exit(f"[ERROR] {splv.CYELLOW2}You need to add {splv.CEND} {splv.CYELLOW2}--url{splv.CEND}")

s = requests.Session()

thrds = 500
thread_list = []
status_codes = []

def req():
    global sucess_request
    global status_codes
    ua = UserAgent()
    agt = ua.random
    hdrs = {
    "User-Agent": agt,
    "Connection": "keep-alive",
    }
    try:
        r = s.get(f"{args.url}", headers=hdrs)
        status_codes.append(r.status_code)
        if args.output == 1:
            if r.status_code == 200:
                print(f"{splv.CGREEN} [*] 200 | {r.url} {splv.CEND}")
            elif r.status_code == 403:
                print(f"{splv.CRED} [*] 403 | {r.url} {splv.CEND}")
            elif r.status_code == 500:
                print(f"{splv.CRED} [*] 500 | {r.url} {splv.CEND}")
            elif r.status_code == 503:
                print(f"{splv.CRED} [*] 503 | {r.url} {splv.CEND}")
            elif r.status_code == 520:
                print(f"{splv.CRED} [*] 520 | {r.url} {splv.CEND}")
            else:
                print(f"{splv.CRED} [*] {r.status_code} | {r.url} {splv.CEND}")
        else:
            msg.att(f"Got response {r.status_code}")
    except requests.exceptions.RequestException:
        status_codes.append(0)


for thr in range(args.req):
    thread = threading.Thread(target=req)
    thread_list.append(thread)
    thread_list[thr].start()

for thread in thread_list:
    thread.join()

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        countas = list1.count(x)
        print(f"[*] Status code: {x} ({countas})")

if __name__ == "__main__":
    try:
        os.system("cls")
    except:
        os.system("clear")
    logo()
    print("-------------------------------------------------")
    msg.success("Done!")
    print("-------------------------------------------------")
    print(f"More about status codes you can find at: {splv.CGREEN}https://developer.mozilla.org/en-US/docs/Web/HTTP/Status{splv.CEND}")
    print(f"""
Status code {splv.CRED2}0{splv.CEND} - Thats there was an {splv.CRED2}error{splv.CEND}.
          """)
    print("-------------------------------------------------")
    print(f"[*] URL: {splv.CGREEN}{args.url}{splv.CEND}")
    print(f"[*] Requests: {splv.CGREEN}{args.req}{splv.CEND}")
    print("-------------------------------------------------")
    print("[*] Status codes:")
    unique(status_codes)
    print("-------------------------------------------------")