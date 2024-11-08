# LibraryofCongress
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
