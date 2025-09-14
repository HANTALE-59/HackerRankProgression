#from soc


sorted_list1 = [1,3,5,6,7,9,10,20,30]
sorted_list2 = [1,3,7,9,10,20,30]
sorted_list3 = [1,3,5,6,7,9,10,20,30,50]

def find_match(sorted_list:list,element:int) -> bool:
    mid = int(len(sorted_list)/2)
    lenght = len(sorted_list)
    high = lenght - 1
    low = 0
    while True:
        mid = int((high + low) / 2)
        if sorted_list[mid] == element:
            return True
        elif sorted_list[mid] > element:
            # mid = int(mid-mid/2) 
            high = mid
        else:
            # mid = min(int(mid + mid/2), lenght - 1)
            low = mid

        #print(f'low: {low}, high: {high}')
        #print(mid)
        if low == high or low == high - 1:
            return False

        


print(find_match(sorted_list=sorted_list1,element=5))
print(find_match(sorted_list=sorted_list2,element=8))
print(find_match(sorted_list=sorted_list3,element=31))