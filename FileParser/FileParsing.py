#!/usr/bin/env python
import sys
import re


#def main(argv):program name inputfile outputfile
# 3 arguments :
if len(sys.argv) < 3:
    print(" .\program input_file_name output_file_name")
else:
    input_file = sys.argv[1]
    out_file = sys.argv[2]
    #dictionary to store word against linenumber
    mapp = {}
    #variable to keep track of line number
    lineNumber = 0
    try:
        with open(input_file) as inFile:
            for line in inFile:
                lineNumber +=1
                #strip for any extra spaces and split with space.
                #this returns list of words on particular line
                lst = re.sub(r'\s+',' ',line).strip().split(' ')
                for word in lst:
                    if word in mapp:
                        mapp.get(word).add(lineNumber)
                    else:
                        mapp[word] = set()
                        mapp[word].add(lineNumber)
        #open file to write output
        f = open(out_file, "a+")
        for key in sorted(mapp.keys()):
            f.write(key+' ')
            for val in mapp[key]:
                f.write(str(val)+' ')
            f.write('\n')
        f.close()
    except:
        print("File Opening error : Fail to open")