#factorial

#recursion
def factorial(n):  
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

#itteration
def factorial(n):
  result = 1 
  for num in range(1, n+1): 
    result *= num 
  return result

#fibonacci

#recursion
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

#itteration
def fibonacci(n): 
  prevprev = 0
  prev = 1
  count = 0
  if n == 0: 
    return 0 
  if n == 1: 
    return 1
  else:
    while count < n-1:
      curr = prevprev
      prevprev = prev
      prev = curr + prev
      count+=1
  return prev

#sum digits

#recursion
def sum_digits(n): 
  if n < 10: 
    return n
  else: 
    return n%10 + sum_digits(n//10)

#itteration
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n != 0:
    result += n % 10
    n = n // 10
  return result + n

#minimum value

#recursion
def find_min(my_list, min=None): 
  if len(my_list) == 0: 
    return min
  else: 
    if min == None or min > my_list[0]:
      min = my_list[0]
  return find_min(my_list[1:], min)

#itteration
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

#palindromes

#recursion
def is_palindrome(my_string): 
  if len(my_string) < 2: 
    return True
  else: 
    if my_string[0] != my_string[-1]:
      return False
  return is_palindrome(my_string[1:-1])

#itteration
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True

#multiplication

#recursion
def multiplication(num_1, num_2): 
  if num_2 == 1: 
    return num_1
  else: 
    num_1 += multiplication(num_1, num_2-1)
  return num_1


#itteration
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

#tree depth

#recursion
def depth(tree_node): 
  if tree_node == None: 
    return 0 
  left_depth = depth(tree_node['left_child'])
  right_depth = depth(tree_node['right_child'])
  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1


#itteration
def depth(tree):
  result = 0
  queue = [tree]
  while queue:
    level_count = len(queue)
    for child_count in range(0, level_count):
      child = queue.pop(0)
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    result += 1
  return result
