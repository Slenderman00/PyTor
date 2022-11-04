# PyTor 🔥
PyTor is a simple framework that enables the automatic creation of new Tor sessions.
PyTor is created with asynchronous opperations in mind.

PyTor supports as many sessions as you have available ports
 
## Usage 🤌
~~~python 

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
~~~


## TODO 📝
- Implement a session manager that can keep track of all the sessions.

- Clean up temp files.

- Specify allowed ports.


---
## Badges  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  
