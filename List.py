# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:45:15 2018

@author: abusithik
"""
#LIST - It is the mmost basic data structure we will use frequently in python,you can do various operations with list which are given below


#CREATING LIST
#List can be simply created with a variable name and assign it with comma seperated values within square backets.
my_list = [1,3,6,12,16,28]

# List can also be created with different data types
list1 = ['physics', 'chemistry', 1997, 2000];

#ACCESSING LIST
#Individual element of the list  can be accessed using index value in square brackets []. Indexing starts from 0.
my_list[0]
#It return the 1st element

#Range of elements can also be accessed using start and end index numbers
my_list[2:5]
#It slices the value from index 2 to 4 (excluding end index) Eg: 6,12,16

#Negative indexing retrives data from last
my_list[-2]
#It returns last but 2nd value

#UPDATING LIST
list1 = ['physics', 'chemistry', 1997, 2000];
list1[2]=1998

#DELETE LIST
list1 = ['physics', 'chemistry', 1997, 2000];
del list1[2];
#It removes 1997 from the list

#COmmon Functions of List

cmp(list1, my_list)
#Compares elements of both lists.

len(list1)
#Gives the total length of the list.

max(list1)
#Returns item from the list with max value.

min(list1)
#Returns item from the list with min value.

list1.append(obj)
#Appends object obj to list

list1.count(obj)
#Returns count of how many times obj occurs in list

list1.extend(seq)
#Appends the contents of seq to list

list1.index(obj)
#Returns the lowest index in list that obj appears

list1.insert(index, obj)
#Inserts object obj into list at offset index

list1.pop(obj=list[-1])
#Removes and returns last object or obj from list

list1.remove(obj)
#Removes object obj from list

list1.reverse()
#Reverses objects of list in place

list1.sort([func])
#Sorts objects of list, use compare func if given

