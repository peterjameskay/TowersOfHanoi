from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Stacks Area:
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack =  Stack('Right')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Game Setup:
num_disks = 0

while num_disks < 3:
  num_disks = int(input('\nHow many disks do you want to play with?\n'))
  if num_disks < 3:
    print('Enter a number greater than or equal to 3\n')
    continue
for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optimal_moves = 2 ** num_disks - 1

print('\nThe fastest you can solve this game is in ' + str(num_optimal_moves) + ' moves')

# User Input:
def get_input():
  choices = [letter.get_name()[0] for letter in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter " + letter + " for " + name + ".")
    user_input = input('')
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]  
        
# Play Setup:
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
print("\n\nYou completed the game in {U} moves, and the optimal number of moves is {O}".format(U = num_user_moves, O = num_optimal_moves))

# The End!
