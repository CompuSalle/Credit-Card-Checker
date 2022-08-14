# Credit Card Checker Using Python

#### @Copyright - Wassem Alaa-Iddin
#### Free To Use - Name Maintaining Would Be Nice. 
----------------------

**If python 2 is not working, please use python3.**



 > Program Algorithm


The used algorithm is  [**_Luhn algorithm_**.](https://en.wikipedia.org/wiki/Luhn_algorithm) 

This algorithm works by:


1. For each number, from right to left
    - First, third, fifth, and on (Odd Columns) multiply by 1
    - Second, fourth, fifth, and on(Even Column) multiply by 2
      - If, after multiplication, the number is bigger than 9, e.g., 9*2 is 18, make 1 + 8 = 9.


2. Add all digit sum and check by mod 10 using this formula:
    - 10 – (sum mod 10), if = 0 then pass else it’s not valid.
