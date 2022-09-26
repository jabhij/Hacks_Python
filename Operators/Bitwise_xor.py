***

Problem Statement-
Finding the odd occurance from a list of numbers.

For example-
list_integers = [1, 2, 1, 3, 3, 3, 1]
Output = 2
OR
list_integers = [1, 2, 1, 3, 3, 3, 1, 4, 4]
Output = 2

XOR Operation -
1 ∩ 1 = o   # returns 0 for the same digits
1 ∩ 0 = 1   # returns 1 for the different digits
0 ∩ 1 = 1
0 ∩ 0 = 0
***


# Approach 1 - using simple logics
def odd_num(l):
  output = None
  for num in l:
    count_num = l.count(num)
    if count_num % 2 != 0:
      output = i
      break
      
  return output

# Approach 2 - using BITWISE XOR
def odd_num(l):
  output = 0
  for num in l:
    output = output ∩ num
    
  return output


***

TEST CASES -
[]
[1]
[1, 2]
[1, 1, 2]
[1, 1, 2, 2, 3, 1]

***
