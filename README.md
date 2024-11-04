# LibraryofCongress
1. Library of Congress - Description
Read all Instructions carefully. Not following instructions will result in you not getting the credit you want for this assignment.
Learning Outcomes
Read structured input from text files
Write structured output to text files
Process structured strings
Use data structures such as list, tuple, dict in programs
Sort data
Rearrange data to make processing easier
Compute basic statistics or metadata from data
Structure
File
library.py
Input
a text file such as TTC.txt
one input file for each book
Output
text file such asTTC_book.txt
one output file for each book
Problem
You’re an intern at the Library of Congress. You are given a collection of text files where each file corresponds to a book. Each file is named with a three-letter code for the book it contains. Examples are like TTC.txt, WOO.txt, TTL.txt and other names too. There could be many such input files and we may not know how many.
Each line in the file looks like this: one line from the book and the line number, separated by a '|’. For example: "It was the best of times, it was the worst of times,"|1
You discover though, that the content of each file is scrambled so that the lines are not in order.
Your task is to write a program that reads each of these book files and does a few things:
Find the longest line from the book along with its line number.
Calculate the average length of the lines in the book.
Unscramble the lines of text in order of line number.
Once your program has done that, it needs to save this information in a new file called '<three_letter_code>_book.txt’. The format would be:
first line is the three-letter code
second line is the longest line with line number and content as shown
third line is the average length
lines 4 to end are the contents of the book in line order
Example Run
As an example, for this input
python3 library.py TTL.txt
Your code will generate a file named as TTL_book.txt and the first few lines of that output file would look like this:
TTL
Longest line (14153): Ecclesiastes—“Who can fathom the soundless depths?”—two men out of all
Average length: 58
Twenty Thousand Leagues Under the Seas
An Underwater Tour of the World
JULES VERNE
[......]
If there are multiple lines with the same length as the longest, use the line number to decide: the line that appears later is considered as "longest". Round the average to the closest integer.
And that’s it! You’ve gathered useful information, unscrambled the text, and written the information to a new file.
Key Requirements and Grading
While you might observe that certain rubrics are being automatically graded, please note that these scores will not be transferred to Canvas until your instructor or TA comprehensively reviews the entire project and manually assigns grades after the deadline ends.
Automatically-graded scoring (90 points)
(40) The program produces an output file for each book file given (Input is given through one command line parameter).
(40) The program produces the correct text for another book file you are not given (While it checking through autograder).
(10) The program contains a main function with conditional execution.
Manually graded scoring (10 points)
(5) All variable names and the code follows Python snake case or camelcase.
(5) There is no global code.
Submit library.py in your workspace.
