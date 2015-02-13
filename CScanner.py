#!/usr/bin/env python

import nmap

class Scanner(object):

	def __init__(self):
		self.nm = nmap.PortScanner()
		self.ourIP = '127.0.0.1' #Need a consistent solution to get our 192.168.x.x ip, using sockets is not an option