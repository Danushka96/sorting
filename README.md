# sorting
Sorting Methods using Python

##Selection Sort

#Psudo code
SelectionSort(int[] t, int n)
1: begin
2: int i,j,min,q
3: for i = 1 to n-1 do
4: min = i
5: for j = i+1 TO n do
6: if t[j] < t[min] then
7: min = j
8: end if
9: end for
10: q = t[min]
11: t[min]= t[i]
12: t[i] = q
13: end for
