Problem:
INPUT is a text file.
* The file consists of a number of lines, separated by line breaks.
* Each line contains "words" made up of lower case alphabetical characters separated by white space.
* You can assume that the file is small enough to fit in working memory.
   
OUTPUT is a text file containing an index to the input:
* For each word w in the input, there is an entry of the form w
            num1 num2 ... <carriage_return>
            such that num1, num2,... are the line numbers in the input on which
            w occurs. If w occurs more than once on a given line, the line number
            should only occur once.
* The entries appear in alphabetical order.
   
For example, if the input is:
  
the quick brown fox jumps over
the lazy
lazy lazy
dog
 
then the output will be: 

brown 1
dog 4
fox 1
jumps 1
lazy 2 3
over 1
quick 1
the 1 2


***Some Test Scenarios:

1. if file empty : returns empty file
2. normal file: returns map (key, values)
3. if input file does not open/does not exist : returns error message


***Running program:

Run file as: 'python FileParsing.py <inputFilename> <OutputFilename>'

***Program Flow:

File is opened and read line by line. Every line is split with space which gives us list of words on that line.
Every word is put in dictionary with line number against it.
So, in dict, key = word value = line number. For value, set is used, since we do not need to repeat the line numbers. Set does keeps it unique.
Once file reading is completed, the map is sorted with keys and written into output file.
