#!/usr/bin/env python

import nmap

class Scanner(object):

    def __init__(self):
        self.nm = nmap.PortScanner()
        self.ourIP = '127.0.0.1' #Need a consistent solution to get our 192.168.x.x ip, using sockets is not an option

    def scanAll(self):
        print self.nm.scan(hosts='192.168.0.0/24', arguments='-n -sP -PE -PA21,23,80,3389')#Wont retrieve hostname for each scanned ip
        for host in self.nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, self.nm[host].hostname()))