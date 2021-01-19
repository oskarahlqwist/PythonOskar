#!/bin/python3
a,b,c=3,1,2
if (a == b):
    if (a == c):
        answer = 'all are equal'
    else:
        answer = 'a and b are equal'
else:
    if (a == c):
        answer = 'a and c are equal'
    else:
        if (b == c):
            answer = 'b and c are equal'
        else:
            answer = 'all are different'
print(answer)
