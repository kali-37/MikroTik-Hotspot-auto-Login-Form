import requests 
import re
import credentials
from bs4 import BeautifulSoup 

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://wifi.sochcollege.edu.np',
    'Referer': 'http://wifi.sochcollege.edu.np/login',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

def let_login(payload:dict['str','str']):
    url="http://wifi.sochcollege.edu.np/login"
    print(f"SENDING REQUESt TO {url}")
    response= requests.post(url=url,json=payload,headers=headers)
    if "Welcome" in response.text:
        print("You are Sucessfully Logged In")
    else:
        print("\x1b[31m Failed to login \x1b[0m",response.status_code,response.text)
        with open("temp.html",'w') as fp:
            fp.write(response.text)
        exit(code=1)


def main()->None:
    url="http://wifi.sochcollege.edu.np/login"
    try:
        response=requests.get(url=url)
    except requests.exceptions.ConnectionError as e:
        print(f"\x1b[31m Connection ERR: \x1b[0 \x1b[32m Are you connected to SOCHCOLLEGE WIFI ?\x1b[0m")
        exit(1)
    except:
        print(f"\x1b[31m Unknown ERR connecting {url}\x1b[0m")
        exit(1)
    if response is None: 
        print("response seems to be NULL")
        exit(1)
    data=response.text

    '''
    #  Debug 0
    # with open('resp.html', 'w') as f:
        # f.write(response.text)
    # data=None
    
    #Debug  1

    # with open('resp.html','r')as f:
        # data=f.read()
    '''
        
    read_=BeautifulSoup(
        data,'html.parser')

    scrpit_tag=read_.find_all(name='script')
    if scrpit_tag ==[]:
        print("\x1b[31m ERR OCCURED Unknown Response from the Server ERR code 1 \x1b[0m")
        exit(1)
    for _ in scrpit_tag:
        if "document.sendin.username.value" in str(object=_):
            _need:str=str(object=_).replace('\n','')
            regx_pattern=r"(hex[^;]+)"
            pattern_match=re.search(regx_pattern,_need)
            if not pattern_match:
                print("\x1b[31m Regex Pattern couldn't be matched \x1b[0m")
                exit(code=1)
            need_pattern=pattern_match.group(0).replace('document.login.password.value',f"{credentials.password.__repr__()}")
            # print(need_pattern)
            passcode: requests.Response=requests.post(url='http://localhost:8000/process_post',json={"password_eval":need_pattern})
            login_payload={'username':credentials.username,'password':passcode.json()['password'],'dst': 'http%3A%2F%2Fdetectportal.brave-http-only.com%2F','popup':False}
            let_login(payload=login_payload)

if __name__=="__main__":
    main()

    
