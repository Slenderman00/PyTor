import PyTor
import requests

#start a new pytor session
pytor = PyTor.Session()
pytor.start()

#get public ip using pytor proxy
res = requests.get("https://api.ipify.org", proxies={"http": pytor.getProxy(), "https": pytor.getProxy()})
print(res.text)

#request a new public ip
pytor.newIP()

res = requests.get("https://api.ipify.org", proxies={"http": pytor.getProxy(), "https": pytor.getProxy()})
print(res.text)