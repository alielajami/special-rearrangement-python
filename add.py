'''Special Rearrangement of Integers in a list'''

list_size = int(input("Enter the size of the list: "))
integer_list = []

for i in range(list_size):
    integer_list.append(int(input("Enter the integer " + str(i+1) + ": ")))

print("Original List: ", integer_list)