l1 = [1,3,4,5,6,8,9,100]
#             ^        
l2 = [2, 100]
#           ^

pointerA = 0
pointerB = 0
res = []


while pointerA < len(l1) and pointerB < len(l2):
    e1 = l1[pointerA]
    e2 = l2[pointerB]
    if e1 > e2:
        pointerB +=1
    elif e1 < e2:
        pointerA +=1
    else:
        res.append(e1)
        pointerA += 1 
        pointerB += 1 
print(res)

