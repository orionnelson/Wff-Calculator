# Wff-Calculator
````Turns a Properly constructed regex equation into a WFF Constuction Sequence

*****************************************************************
                    REQUIRES PYTHON 3 
*****************************************************************


Note the following is not being considered a WFF
(pνqΛp) 
The script does not know if you mean ((pνq)Λp) or (pν(qΛp)) and will probably just do both if exceptions are disabled or throw an exception as it is not in propper bracket notation WFF. 
Note Some textbooks use these types of functions and assume left to right progression. May add this as a default but am busy and will take some planning.

Possible Updates:
* Adding a truth value table and method to tell if the entry is well formed before computing the construction sequence.
^^ Did That ;)

Notes:

Examples of WFF:
*(((pΛ((¬p)νq))Λ(s→r))Λ((¬s)→s))
*((pνq)Λp)
*((a4b)2((1a)4b))  ** Inputed in the num conversion formula. 
*(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))) try this


How Do I Know You Did not HardCode Those Examples? Try any combination of WFFs by replacing variables of a wff with other wff's  My Favorite is: 

(((1((((pΛ((¬p)νq))Λ((((1(a3b))2((1c)2b))4((c4d)2((1a)4d)))→r))Λ((¬(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))))→(((1(a3b))2((1c)2b))4((c4d)2((1a)4d)))))3((pνq)Λp)))2((1c)2((pνq)Λp)))4((c4d)2((1(((pΛ((¬p)νq))Λ((((1(a3b))2((1c)2b))4((c4d)2((1a)4d)))→r))Λ((¬(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))))→(((1(a3b))2((1c)2b))4((c4d)2((1a)4d))))))4d)))

Note At This Point the size of the equation is larger then the cmd or python shell window so it may look glitchy.



Future
May add (¬¬p) since most people count it as well formed 
````

