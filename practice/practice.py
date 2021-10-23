#01 add all items
def sumitems(items):
    total = 0
    for x in items:
        total = x + total
        x = x + 1
    print("Sum is ", total)

#02 multiply all items
def multitems(items):
    total = 1
    for x in items:
        total = x * total
        x = x + 1
    print("Product is ", total)

#03 get largest number
def maxnum(items):
    x = max(items)
    print("Max is ", x)

#04 get smallest number
def minnum(items):
    x = min(items)
    print("Min is ", x)

#05 count the number of strings where the string length is 2 
# or more and the first and last character are same from 
# a given list of strings.

#TODO

#06 get a list, sorted in increasing order by the last 
# element in each tuple from a given list of non-empty tuples.
#TODO

#07 remove duplicates from list
def remdups(items):
    items.sort()
    uniqitems = []
    for i in items:
        if i not in uniqitems:
            uniqitems.append(i)
        else: i = i + 1
    print("Original entries: ", items)
    print("Unique entries: ", uniqitems)

#08 check is list empty
def listempty(items):
    print("List is empty? ", items == [])

#find list of words that are longer than n
def listnlong(words, n):
    longlist = []
    for i in words:
        if len(i) > n:
            longlist.append(i)
    print(longlist)
        
#09  clone or copy a list
def clone(list):
    list_clone = list
    print("This is the original list: ", list)
    print("This is a clone of the list: ", list_clone)

#10 find the list of words that are longer 
# than n from a given list of words

def longerthann(words, n):
    nlongwords = []
    for i in words:
        if i > n:
            nlongwords.append(i)
    print(f"These are the words longer than {n} characters: ", longerthann)

#11 takes two lists and returns True if they have at least one common member / TODO
def commonmem(lista, listb):
    biglist = lista + listb
    #print(biglist)
    bigdictlist = dict(biglist)
    return bigdictlist < biglist

#12 print a specified list after removing the 0th, 4th and 5th elements
def rem045(words):
    del words[5]
    del words[4]
    del words[0]
    print(words)

#14 print the numbers of a specified list after removing even numbers from it
def remevens(list):
    oddlist = []
    for i in list:
        if i % 2 != 0:
            oddlist.append(i)
    print(oddlist)

#15 shuffle and print a specified list TODO

