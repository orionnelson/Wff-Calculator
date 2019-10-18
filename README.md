# Wff-Calculator
````Turns a Properly constructed regex equation into a WFF Constuction Sequence


Note the following is not being considered a WFF
(pνqΛp) 
The script does not know if you mean ((pνq)Λp) or (pν(qΛp)) and will probably throw an exception

Possible Updates:
* Adding a truth value table and method to tell if the entry is well formed before computing the construction sequence.

Notes:
Why does the output contain ¬12  in the index number of called operations?
    * If the number is greater then four digits the negation is carried over to save space say you were to write this out by hand. 
 
Why does the program keep crashing?
The program Is made for wff and if your entry was not a wff I did not include a Try Catch block. 

Examples of WFF:
*(((pΛ((¬p)νq))Λ(s→r))Λ((¬s)→s))
*((pνq)Λp)
*((a4b)2((1a)4b))  ** Inputed in the num conversion formula. 

````

