#!/usr/bin/env python

import CScanner

#
#Scan for everything( Names, IPs', Ports )
#Scan for Names and IPs
#Search for Name in the network (Show IP)
#Search for IP in the network (Show Name)
#
def menu():
    answer = ""

    print "1. Scan for everything ( Names, IPs, Ports )"
    print "2. Scan for Names and IPs"
    print "3. Search for Name in the network"
    print "4. Search for IP in the network"
    print "0. Exit"

    while 1:
        answer = raw_input("Enter your option: ")

        if not answer.isdigit() or int(answer) > 4 or int(answer) < 0:
            print "Not a valid option. Valid options are 0-4"
        else:
            break

    return answer

def process(menuChoice):
    print menuChoice
    network = CScanner.Scanner()
    print str(network.ourIP)

process(menu())