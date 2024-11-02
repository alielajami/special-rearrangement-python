'''Special Rearrangement of Integers in a list'''

list_size = int(input("Enter the size of the list: ")) # Size of the list
integer_list = [] # List to store the integers
rearranged_list = [] # List to store the rearranged integers

for i in range(list_size):
    integer_list.append(int(input("Enter the integer " + str(i+1) + ": "))) # Appending the integers to the list

def special_rearrangement(integer_list):
    '''Function to rearrange the integers in a list
     such that all even integers are placed before the odd integers'''

    for j in range(len(integer_list)): # Loop to append the even integers first
        if integer_list[j] % 2 == 0: # Checking if the integer is even
            rearranged_list.append(integer_list[j])

    for k in range(len(integer_list)): # Loop to append the odd integers next
        if integer_list[k] % 2 != 0: # Checking if the integer is odd
            rearranged_list.append(integer_list[k])

    return rearranged_list

print("The rearranged list is : ", special_rearrangement(integer_list)) # Printing the rearranged list