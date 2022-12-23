# PS-8 Questions

### **Q1) Border crossing**

You are given a CSV file which contains border crossing/entry data for US-Mexico and US-Canada borders.

**Input:** Year, border and border crossing method

**Output:** Total number of people (value) who have crossed the border in the given year using the given method

**CSV file format:** `Port Name,State,Port Code,Border,Year,Method,Value,Latitude,Longitude,Point`

To obtain satisfactory outputs, write a program that includes nested dictionary and list structures. Suggested dictionary format is given below.

```py
dict = {"year1": {"border1": {"method1": [value1, value2, value3],
                              "method2": [value4, value5, value6]}}}
```

### **Q2) Grade analysis**

You are given a text file which contains students' grades in different subjects.

**Text file format:** `class,subject1,grade1,grade2,grade3,subject2,grade1,grade2,grade3`

Write a program that calculates the average/median of students' grades in a given subject and a given class.

Input | Output
--- | ---
11b chem average | 83.0
11b math median | 78

### **Q3) Pant style pattern**

Write a program that takes an even integer (N) and prints a pant style pattern of stars with N/2 rows.

An example for N=10 is given below.
```
**********
****  ****
***    ***
**      **
*        *
```