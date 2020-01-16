# Wff-Calculator

This script evaluates well formed formulas and provides feedback issuing an error providing feedback to the user. 
Upon reciving a properly structured well formed formula. The script will then compute the construction sequence.
The three rules that the formula tests are as follows.

#### Well Formed Formula Rules

'1. Every well formed formula is atomic (that is, an element of the core set) or starts with the left bracket symbol ‘(’.'
'2. Equivelent number of left and right brackets in the formula.'
'3. In every proper initial segment of a well formed formula, the number of left brackets ‘(’ is larger then right brackets '


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
To understand how this program works consider the example : (pνqΛp). 

The script does not know if you mean ((pνq)Λp) or (pν(qΛp)) 
and will probably just do both if exceptions are disabled or 
throw an exception as it is not in propper bracket notation WFF. 

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
*(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))) 
**You may also replace any primitive variable with another well formed formula.
````
Here is a large one
(((1((((pΛ((¬p)νq))Λ((((1(a3b))2((1c)2b))4((c4d)2((1a)4d)))→r))Λ((¬(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))))→(((1(a3b))2((1c)2b))4((c4d)2((1a)4d)))))3((pνq)Λp)))2((1c)2((pνq)Λp)))4((c4d)2((1(((pΛ((¬p)νq))Λ((((1(a3b))2((1c)2b))4((c4d)2((1a)4d)))→r))Λ((¬(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))))→(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))))))4d)))

Note At This Point the size of the equation is larger then the cmd or python shell window so it may look glitchy. 


