import math
import pathlib
import subprocess
import random
import socket
import tempfile

class Session():
    def __init__(self):
        self.path = pathlib.Path(__file__).parent.resolve()
        self.id = math.floor(random.random()*9999)
        self.port0 = math.floor(random.random()*64510) + 1024
        self.port1 = self.port0 + 1
        self.port2 = self.port0 + 2

        self.tmp = tempfile.TemporaryDirectory(dir=self.path)

        self.path = pathlib.Path.joinpath(self.path, self.tmp.name)

        self.createTorrc(self.id, self.port0, self.port1, self.port2)

    def createTorrc(self, id, port0, port1, port2):
        print(f"Creating Tor{id}")
        f = open(pathlib.Path.joinpath(self.path, f'torrc.{id}'), "w")
        f.write(f"HTTPTunnelPort {port0}\nSocksPort {port1}\nControlPort {port2}\nDataDirectory {self.path}/tor{id}")

    def startTorrc(self, id):
        print(f"Starting Tor{id}")
        file = pathlib.Path.joinpath(self.path, f'torrc.{id}')
        output = subprocess.Popen(["tor", "-f", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        run = True
        while run:
            line = output.stdout.readline()
            if line != b'':
                if(b"Bootstrapped 100% (done): Done\n" in line):
                    print(f"Tor{id} started")
                    run = False
            else:
                break

    def start(self):
        self.startTorrc(self.id)

    def getProxy(self):
        return f"http://127.0.0.1:{self.port0}"

    def newIP(self):
        #send signal to tor to change ip
        sock = socket.socket()
        sock.connect(('127.0.0.1', self.port2))
        sock.send("AUTHENTICATE \"\"\r\nSIGNAL NEWNYM\r\n".encode())
        #loop over response
        run = True
        while run:
            line = sock.recv(1024)
            if line != b'':
                if(b"250 OK" in line):
                    print(f"Tor{self.id} New IP")
                    run = False
            else:
                break
        sock.close()



