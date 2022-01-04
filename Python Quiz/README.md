There is a popular puzzle where you try to guess the combination to a lock given some clues. For our purposes, the lock has exactly three wheels, each with values 0 through 9.

![1](https://user-images.githubusercontent.com/22623056/148006255-8b3ed3db-2a56-468b-993d-bdffef858c47.jpg)

You must provide the clues on the command line and they must be of the form XYZ-R-W where:
XYZ = a possible combination of 3 digits, each 0-9
R = count of wheels that are the right digit in the right place (0-3)
W = count of wheels that are the right digit but in the wrong place (0-3)
The expectation is that you will use a brute form technique to solve this puzzle. Iterate through all 1,000 possible combinations and see which one(s) pass all the clues. Do NOT try to solve this puzzle the way a human would, using logic.
Additional rules:
1.	The number of clues can vary. If no clues are given you must print an error message.
2.	You must use a regular expression to validate the XYZ-R-W syntax. 
3.	You do not need to do any additional validation of the XYZ, R, W parameters.
4.	You must print the list of clues given, all on one line.
5.	You must count the number of solutions found and print that count.
6.	If no solutions are found, you must print a message to that effect.
