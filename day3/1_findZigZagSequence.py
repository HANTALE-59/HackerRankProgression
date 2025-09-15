#https://www.hackerrank.com/challenges/one-week-preparation-kit-zig-zag-sequence/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three
def findZigZagSequence(a, n): #//Le test est clairement bon mais hacker rank ne veut pas
    a.sort()
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    st = mid + 1
    ed = n - 2
    
    while(st < ed):
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1
    """
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    
    output = ""
    for e in a:
        output += f"{e} "
    print(output)
    return 
    """
    print(" ".join(map(str, a)))


'''
test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
'''
findZigZagSequence(a=[5,2,3,4,7,6,9,10,11],n=9)
print("espace")
print("espace")

findZigZagSequence(a=[5,2,3,4,7,6,9,10],n=8)
print("espace")
print("espace")

findZigZagSequence(a=[5,2,3,4,7,6],n=7)
print("espace")
print("espace")

findZigZagSequence(a=[5,2,3,4,7],n=6)

