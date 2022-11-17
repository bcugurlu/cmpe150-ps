# PS-3 Questions

**Q1) Factorial**

Write a program that takes an integer x and prints the result of "x!".

Input | Output
--- | ---
5 | 120
8 | 40320

**Q2) Largest number**

Write a program that takes five integers and decides which is the largest number.

**Q3) Hooping numbers**

Write a program that reads 3 integers A, B and T from the user. Then prints numbers from A to B with increment of T. Assume that B > A.

Input | Output
--- | ---
7 <br> 16 <br> 3| 7 10 13 16
2 <br> 30 <br> 6| 2 8 14 20 26

**Q4) Logistics**

You are responsible for the logistics various types of cargo. Depending on the weight of each cargo, you need a different vehicle, and this will cost a different price per ton:

* Up to 3 tons – a minibus (200 USD per ton).
* From over 3 and up to 11 tons – truck (175 USD per ton).
* Over 11 tons – train (120 USD per ton).

Your task is to calculate the average price per ton of the cargo, and also what percentage of the cargo is transported in each vehicle.

From the console we must read a sequence of numbers, each on a separate line:

* First line: count of cargo for transportation – integer in the range of [1 … 1000].
* On the next lines we pass the tonnage of the current cargo – integer in the range of [1 … 1000].

Print on the console 4 lines, as follows:

* Line #1 – the average price per ton of the cargo (rounded up to the second digit after the decimal point).
* Line #2 – percentage of the cargo, carried by minibus (between 0.00 and 100.00, rounded up to the second digit after the decimal point).
* Line #3 – percentage of the cargo, carried by truck (between 0.00 and 100.00).
* Line #4 – percentage of the cargo, carried by train (between 0.00 and 100.00).

Input | Output
--- | ---
5 <br> 2 <br> 10 <br> 20 <br> 1 <br> 7 | 149.38 <br> 7.50 <br> 42.50 <br> 50.00
4 <br> 53 <br> 7 <br> 56 <br> 999 | 120.35 <br> 0.00 <br> 0.63 <br> 99.37

**Q5) Multiplication table**

Write a program that prints a 9x9 multiplication table of the integers from 1 to 9.

**Q6) Rectangles**

**a)** Write a program that takes two integers as the number of rows and columns 
of a rectangle, then prints it.

Input | Output
--- | ---
5 <br> 3 | ooo <br> ooo <br> ooo <br> ooo <br> ooo
3 <br> 2 | oo <br> oo <br> oo

**b)** Write a program that takes two integers as the number of rows and columns of a rectangle, 
then prints it with "o" on the borders and "_" inside.

Input | Output
--- | ---
5 <br> 3 | ooo <br> o_o <br> o_o <br> o_o <br> ooo
3 <br> 2 | oo <br> oo <br> oo

**Q7) Powers**

Write a program that takes two integers as base number and exponent, then
prints the results as given below.

Input | Output
--- | ---
4 <br> 3 | 4 <br> 4 16 <br> 4 16 64
5 <br> 4 | 5 <br> 5 25 <br> 5 25 125 <br> 5 25 125 625