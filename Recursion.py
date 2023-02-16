#Move items to the end of a list


def move_to_end(lst, val): 
  result = []
  if len(lst) == 0: 
    return []
  if val == lst[0]:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else: 
    result.append(lst[0])
    result += move_to_end(lst[1:], val) 
  return result

#Delete i-th node from a linked list


def remove_node(head, i): 
  if i < 0: 
    return head
  if head == None: 
    return None
  if i == 0: 
    return head.next_node
  head.next_node = remove_node(head.next_node, i-1) 
  return head

#Prepend and append to a string


def wrap_string(str, n): 
  result = ''
  if n <= 0:
    return str
  result += '<'
  result += wrap_string(str, n-1)
  result +='>'
  return result
