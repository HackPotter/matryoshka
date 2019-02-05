#!/usr/bin/python3

import sys, getopt, tarfile, os, magic

debug = None

def main(argv):
    global debug
    debug = False #By default not in debug mode
    infile=""
    outfile=""
    archive = None

    #Right off the bat, an important safety feature
    if(not os.getuid()): #Panic if running as root
        print("Hey, you just tried to run matryoshka as root.")
        print("I appreciate that you're so confident in my code. I really do.")
        print("But the fact is, this is an unfinished mess. *I* don't even run it as root.")
        print("There is a very real chance that this code will try to overwrite something incredibly important.")
        print("So try again, but not as root.")
        sys.exit(1337)

    try: #Get all arguments, raise exception if malformed
        opts, args = getopt.getopt(argv, "i:o:dh",["infile=", "outfile=", "debug"])
    except: 
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h': #Help Flag
            help()
            sys.exit(0)
        elif opt in ("-d", "--debug"): #Debugging mode
            debug = True
        elif opt in ("-i", "--infile"): #Infile option
            infile = arg
            if debug: print("DEBUG INFO: Input file name is " + infile)
    
    if infile == "": # Exit if no infile is specified
        help()
        sys.exit(1)
    
    #THIS TAR STUFF IS JUST HERE FOR TESTING RIGHT NOW
    #TODO: MOVE TO SEPERATE CLASS
    checkType(infile)
    try:
        if debug: print ("Attempting to open {0} as tarfile".format(infile))
        TarArchive = tarfile.open(name=infile, mode='r')
    except Exception as e:
        print(e)
        print ("Error: {0} is not a tarfile. Exiting.".format(infile)) 


def checkType(archiveName): # Uses libmagic to determine filetype via path to file
    archiveType = magic.from_file(archiveName, mime=True)
    if debug: print ("File {0} found to be type {1}".format(archiveName, archiveType))
    

    
#TODO: More in depth help page
def help():
    print("Useage: matryoshka -i <Archive file in>")

if __name__ == "__main__":
   main(sys.argv[1:])
