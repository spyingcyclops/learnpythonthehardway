nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def remevens(list):
    oddlist = []
    for i in list:
        if i % 2 != 0:
            oddlist.append(i)
    print(oddlist)

remevens(nums)