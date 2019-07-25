'''
Title: Create a text file called Todo.txt using the following data, one line per row: Clean House,low Pay Bills,
high When the program starts, load each row of data from the ToDo.txt text file into a Python list. After you load the
data into a list, loop through the list and add each item as a "key,value" pair a new dictionary. After you have added
existing data to the dictionary, use the menu structure included in the template to allow the user to Add or Remove
tasks from the dictionary using numbered choices and then Save the data from the table into the Todo.txt file when
the program exits.
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
Date: 7/24/2019
Dev: Kiran Varaganti
Dependencies: python 3x
'''

infile = "ToDo.txt"

# read in ToDo.txt here
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
# create empty dictionary to store data as we loop
task_dict = {}

# Run loop to put the store it in a dictionary.
for line in lines:
   task = line.split(',')[0]
   priority = line.split(',')[1]
   task_dict[task] = priority

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Choice 1 -Show the current items in the table
    if (strChoice.strip() == '1'):
        # loop through the dictionary here and print items
        for task in task_dict:
            priority = task_dict[task]
            print("Task:{}, Priority:{}\n".format(task,priority))

# Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
       task = input("Enter the task:")
       if task not in task_dict:
            priority = input("Enter the priority of the task entered:")
            # add a new key, value pair to the dictionary
            task_dict[task] = priority
       else: print("Task not added, it is already exists.")

#Choice 3 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        # locate key and delete it using del function
        if remove_key in task_dict:
           del task_dict[remove_key]
        else:print("The entered task doesn't exist")

# Choice 4 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        with open("Todo.txt", "w") as infile:  # open a file handle
            for task in task_dict:  # loop through key, value and write to file
                task_dict[task] = priority
                infile.write("{}, {}\n".format(task, priority))
# Choice 5- end the program
    elif (strChoice.strip() == '5'):
        print("Good-bye.")
        break  # and Exit the program
