#!/usr/bin/env python3
# Split a large text file (log) into smaller pieces.
# Written by Michiel Tiller (https://github.com/mchlt)
import sys, os

numargs = len(sys.argv)

if numargs>=3:
    try:
        numsplits=int(sys.argv[2])
        if not 2 <= numsplits <= 1024:
            raise ValueError('Split argument outside range.')
        filename=sys.argv[1]
    except ValueError:
        numargs=2
        
if numargs<=2:
    inputOK=False
    while not inputOK:
        try:
            answer = input("How many files to split to: ")
            numsplits = int(answer)
            if not 2 <= numsplits <= 1024:
                raise ValueError('Number outside range.')
            inputOK=True
        except ValueError:
            print ("Invalid input. Enter a number between 2 and 1024")
            inputOK=False
    if numargs==2:
        filename=sys.argv[1]
           
if numargs==1:
    filename = raw_input("Enter source filename: ")
    
try:
    infile = open(filename,'rb')
except:
    print ("Could not open file '{}' !".format(filename))
    quit(1)
    
print("Splitting file {} into {} files...".format(filename,numsplits))
fsize=os.path.getsize(filename)
print("Source file size is: {}".format(fsize))

bufsize=int(fsize/numsplits)
bytesread=0

for x in range(1, numsplits+1):
    outfilename="{}.{}".format(filename,x)
    print("Writing {}".format(outfilename))
    try:
        outfile = open(outfilename,'wb')
    except:
        print ("Could not open file '{}' !".format(filename))
        quit(1)
    if x==numsplits:
        bufsize=bufsize*2
    buf=infile.read(bufsize)
    bytesread+=len(buf)
    outfile.write(buf)
    outfile.flush()
    print("  {} bytes written".format(len(buf)))
    outfile.close()
    
infile.close()
print("Done.")

quit(0)
    
    

            
            