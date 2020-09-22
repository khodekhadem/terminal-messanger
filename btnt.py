import requests
import platform
info = platform.uname()
texttosend = ""
base = ""
while texttosend != "base" :
    url = "https://api.telegram.org/bot1345704085:AAE_RxB8n_NJfXtdO10hat4i6FLanMwh424/SendMessage?chat_id=297024443&text=<yor text>"
    texttosend = input("che befrestam ?    \n")
    if texttosend == "info-bede":
        url = url + str(info)
    else:
        url = url + texttosend
    payload = {"UrlBox": url,
               "AgentList" : "Mozilla Firefox",
               "VersionList":"HTTP/1.1",
                "MethodList": "POST",

               }

    r = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
#print(r.text)
