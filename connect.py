import requests 
import json
import re
import credentials
from bs4 import BeautifulSoup 

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Connection": "keep-alive"
}

def let_login(payload:dict['str','str']):
    response= requests.post('http://wifi.sochcollege.edu.np/login',data=payload,headers=headers)
    if "Welcome" in response.text:
        print("You are Sucessfully Logged In")
    else:
        print("\x1b[31m Failed to login \x1b[0m",response.status_code)
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
        # print(_)
        if "document.sendin.username.value" in str(object=_):
            _need:str=str(object=_).replace('\n','')
            regx_pattern=r"(hex[^;]+)"
            pattern_match=re.search(regx_pattern,_need)
            if not pattern_match:
                print("\x1b[31m Regex Pattern couldn't be matched \x1b[0m")
                exit(code=1)
            need_pattern=pattern_match.group(0).replace('document.login.password.value',f"{credentials.password.__repr__()}")
            passcode=requests.post(url='http://localhost:8000/process_post',data=json.dumps(obj={"password_eval":need_pattern}),headers=headers)
            login_payload={'username':credentials.username,'password':passcode.json()['password']}
            let_login(payload=login_payload)
        else:
            print("\x1b[31mUnknown Response from Server ErrCode 2 \x1b[0m")
            exit(code=1)

if __name__=="__main__":
    main()

    