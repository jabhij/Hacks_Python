***

Problem Statement-
Reversing a given list.

For example-
list_integers = [1, 2, 4, 3]
Output = [3, 4, 2, 1]
OR
list_integers = [1, 2, 1, 3, 3, 3]
Output = [3, 3, 3, 1, 2, 1]

***


# Approach 1 - using reverse function
list_name.reverse()  # no new list is created

# Approach 2 - 
new_list = list(reverse(list_name))  # new list is created

# Approach 3 - using list slicing
new_list = my_list[ : : -1]  # new list is created


***
TEST CASES -



***
