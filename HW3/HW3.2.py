#lst=[12, 3, 4, 10] #=> [10, 12, 3, 4]
#lst=[1] #=> [1]
#lst = []  #=> []
lst=[12, 3, 4, 10, 8] #=> [8, 12, 3, 4, 10]

if [] not in lst:
    print(lst)
else:
    lst = [0]
    lst1 = [lst[-1]]
    lst.pop()
    lst1 += lst
    print(lst1)

