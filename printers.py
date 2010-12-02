#!/usr/bin/python

import os

def fabcheck():

    fab_printers = [ "fab5517bw1",
                     "fab5517bw2",
                     "fab6001bw1",
                     "fab6019bw1",
                     "fab8201bw1", # ^ lpr printers
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


def main():

    fabcheck()

# eb check

# lpq
# eb325clr1
# eb423clr1

# lpr
#> eb325bw1
#> eb325bw2
#> eb423bw1

if __name__=="__main__":
    main()
