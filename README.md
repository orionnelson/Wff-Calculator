# Wff-Calculator

This script evaluates well formed formulas and provides feedback issuing an error providing feedback to the user. 
Upon reciving a properly structured well formed formula. The script will then compute the construction sequence.
The three rules that the formula tests are as follows.

#### Well Formed Formula Rules
````
`1. Every well formed formula is atomic (that is, an element of the core set)
or starts with the left bracket symbol ‘(’.`

`2. Equivalent number of left and right brackets in the formula.`

`3. In every proper initial segment of a well formed formula, 
the number of left brackets ‘(’ is larger then right brackets `
````

## Program 
#### Info
Turns a Properly constructed regex equation into a WFF Constuction Sequence and Truth Table. 
````
*****************************************************************
                    REQUIRES PYTHON 3 
*****************************************************************
````
The symbols used in this program will only work with Python 3 
and above, you can download Python from  
[Python Download Page](https://www.python.org/downloads/)
````
To understand how this program works consider the example : (p→qΛp). 

The script does not know if you mean ((p→q)Λp) or (p→(qΛp))
As we know these have completly diffrent truth tables denoted 1 and 2.
This problem stresses the importance of brackets.

                    | 1 | 2 |
                    | T | T |
                    | F | F |
                    | T | F |
                    | T | F | 

Note: Some textbooks use these types of functions and assume 
left to right progression for the same symbols most commonly (¬¬a).
At this point in time this method is unsupported but may include in the future. 
Instead please resort to (¬(¬a)).
 ````
## Usage of the  Program
The following symbols are used in the program to denote the functions of the adequate set (¬,Λ,ν, →)
The formula will accept either the number or these symbols themselves.
````
` 1 =  ¬ ` negation.
 `2 = Λ ` and.
 `3 = ν ` or.
 `4 = → ` implies.
 ````
## Examples of formulas to try.
````
Examples of WFF:
*(((pΛ((¬p)νq))Λ(s→r))Λ((¬s)→s))
*((pνq)Λp)
*((a4b)2((1a)4b))  ** Inputed in the num conversion formula. 
These Last two would most likely take a person a bit of time to do manually.
*((((¬(aνb))Λ((¬c)Λb))→((c→d)Λ((¬a)→d))) This is a tautology
*(((pΛ((¬p)νq))Λ((¬((¬((¬(¬((¬a)Λ(¬b))))νc))ν(¬a)))→r))Λ((¬(¬((¬((¬(¬((¬a)Λ(¬b))))νc))ν(¬a))))→(¬((¬((¬(¬((¬a)Λ(¬b))))νc))ν(¬a))))) is satisfiable.
**You may also replace any primitive variable with another well formed formula try using notepad for this
````


