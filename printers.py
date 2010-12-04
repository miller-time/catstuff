#!/usr/bin/python

import os, sys, time, re
from subprocess import Popen, PIPE

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
    # lpq the non-lpr printers
    for printer in fab_printers[5:]:
        do_lpq(printer)

    # lpr printers that are "ready"
    for printer in fab_printers[:5]:
        do_lpr(printer)

def ebcheck():

    eb_printers = [ "eb325bw1",
                    "eb325bw2",
                    "eb423bw1",     # ^ lpr printers
                    "eb325clr1",
                    "eb423clr1",
                  ]

    # lpq the non-lpr printers
    for printer in eb_printers[3:]:
        do_lpq(printer)

    # lpr printers that are "ready"
    for printer in eb_printers[:3]:
        do_lpr(printer)

def do_lpq(printer):
        lpq_cmd = "lpq -P " + printer
        lpq = Popen(lpq_cmd, shell=True, stdout=PIPE)
        lpq_out = lpq.stdout.read()
        match = re.search(r'ready',lpq_out)
        # tell me what's up if they're not ready
        if not match:
            print(lpq_out)
        #print("lpq_cmd)     # debug print

def do_lpr(printer):
        lpq_cmd = "lpq -P " + printer
        lpq = Popen(lpq_cmd, shell=True, stdout=PIPE)
        lpq_out = lpq.stdout.read()
        match = re.search(r'ready',lpq_out)
        if match:
            # check if printer is duplex
            sides = 1
            opts_cmd = "lpoptions -p " + printer
            opts = Popen(opts_cmd, shell=True, stdout=PIPE)
            opts_out = opts.stdout.read()
            match = re.search(r'sides=two-sided',opts_out)
            if match:
                sides = 2
            generate_image(printer, sides)
            os.system("lpr pacman.tmp -P " + printer)
            #print("lpr pacman.tmp -P " + printer)   #debug print
            delete_image()
        else:
            print(lpq_out)

def fab_or_eb():
    result = raw_input("EB or FAB? ")
    return result.lower()

def getarg():
    if len(sys.argv) > 1:
        return sys.argv[1].lower()

def generate_image(printer, sides):
    f = open('pacman.tmp', 'w')
    f.write("Russell Miller thatguy@cat.pdx.edu " +
            time.ctime() + " " + printer + "\n")
    f.close()
    os.system("cat pacman >> pacman.tmp")
    if sides == 2:
        os.system("cat death >> pacman.tmp")

def delete_image():
    if os.path.exists("pacman.tmp"):
        os.system("rm pacman.tmp")

def test():
    printer = "fabc8802bw1"
    do_lpr(printer)

def main():
   
    if len(sys.argv) == 1:
        which = fab_or_eb()
    else:
        which = getarg()
    if which == "fab":
        fabcheck()
    elif which == "eb":
        ebcheck()
    elif which == "test":
        test()
    else:
        sys.exit(0)
    print("done.")

if __name__=="__main__":
    main()
