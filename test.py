from functools import reduce
strings =["John","had" ,"a", "big","lunch"]
print(reduce(lambda x,y: x +" "+y,strings))