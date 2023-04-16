This problem can be best solved using dynamic programming. As we would have to repeat a lot of computations if we do not use dynamic programming. The result of each computations can be stored in a 2D table. 
So first we create a table to store the result of computatioins. 
As this problem involves substrings to be repeated we have the if (testString[i-1]==testString[j-1]) condition. As there is one more constraint given in the problem that the index of both charcaters should not be the same, we have this additional constraint, (and (i!=j)).
If any of the conditions is not satisfied, it will just take the value from the upper row 
and the left column, whichever is greater.
If there is an element that corresponds to the nth row and nth column, we will have a repeating subsequence. If not, it means that through all the iterations, the code could not find any string order which matches itself where the index positions of the repeating characters cant be the same. 


