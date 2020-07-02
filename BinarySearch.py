def BinearySearch(lists, start, end, value):
    mid = 0
    mid = int((start + end )/2)
    if lists[mid] == value:
        return lists[mid]

    if lists[mid] > value:
        return BinearySearch(lists,start,mid-1,value)
    elif lists[mid] < value:
        return BinearySearch(lists,mid+1,end,value)
    else:
        return -1

a = [1,2,3,4,5,6,7,8,9,10]
print(BinearySearch(a,0,len(a),4))

