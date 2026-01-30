# Matchings
Name: Luis Goicoechea - UFID:3500-9213
Name: Robert Miller - UFID:6705-1188

## Instructions to compile/build code 
Code was written using Python 3.12

## Instructions to run the matcher and the verifier
If using an IDE you only need to click Run on the Matcher.py and Verifier.py files to make them run.
If using a console you can navigate to the /src folder where the files are and use the command "python3 Matcher.py" or "python3 Verifier.py" depending on which would like to run.

To make changes as to which files you want to use on each file, the only change needed is in the first two lines of code with variables path_in and path_out and you can change them using the format "../data/xxxxx where xxxxx is the name of the file you would like to use and is in the /data folder.

## Assumptions
The input files will have a single positive integer in the first line and will have the same amount of lines for hospital and students as the integer in the first line. The preference on each line will be in order from most preferred to least preferred and each entry will be separated by a blank space " ".

The output file will have the same amount of lines as the n integer declared in the first line of the input file and will only have two integers per line (first one to represent the hospital, and the second one to represent the student) separated by a blank space " ".

## Task C
By analyzing the graphs we can see that for small quantities the time it takes to execute the matching as well as verification takes a similar amount of time once it is using higher entries we can see that the time time it takes to execute increases exponentially as the n increases by multiplying by 2 on each trial but the time it takes increases more than that. We can also see that while the Verifier initially has a higher execution time when n is small (n < 64) likely due to the fact that it is performing several checks sequentially, once n grows to 128 and above the time it takes to execute the matcher increases more rapidly due to the amount of permutation needed to perform the algorithm.

### Graph of Matcher
<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/a6363f98-b2d6-457f-a5e2-9100d4e7ded8" />

### Graph of Verifier
<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/fa76bde3-d0d5-4b8c-b500-6edcb5983a17" />

