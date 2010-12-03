#!/usr/bin/python

import os

def fabcheck():

    fab_printers = [ "fab5517bw1",
                     "fab5517bw2",
                     "fab6001bw1",
                     "fab6019bw1",
                     "fab8201bw1",  # ^ lpr printers
                     "fab160bw2",
                     "fab160bw1",
                     "fab5517clr1",
                     "fab8202bw1",
                   ]
    # lpq check - all FAB printers
    for printer in fab_printers:
        print("lpq -P " + printer)
        #os.system("lpq -P " + printer)

    # lpr
    for printer in fab_printers[:5]:
        print("lpr pacman -P " + printer)
        #os.system("lpr pacman -P " + printer)

def ebcheck():

    eb_printers = [ "eb325bw1",
                    "eb325bw2",
                    "eb423bw1",     # ^ lpr printers
                    "eb325clr1",
                    "eb423clr1",
                  ]

    # lpq check
    for printer in eb_printers:
        print("lpq -P " + printer)
        #os.system("lpq -P " + printer)

    # lpr
    for printer in eb_printers[:3]:
        print("lpr pacman -P " + printer)
        #os.system("lpr pacman -P " + printer)

def main():

    fabcheck()
    ebcheck()

if __name__=="__main__":
    main()
