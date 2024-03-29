'''
Title: create a script to read ToDo list from a text file and do following tasks: Show current data, Add a new item,
       Remove an existing item, Save Data to File and Exit Program(hw5.py)
Date: 7/24/2019
Dev: Kiran Varaganti
Dependencies: python 3x
'''

infile = "ToDo.txt"#store path of ToDo.txt file as a variable so that it can be accessed later in the program

# read in ToDo.txt here
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
# create empty dictionary to store data as we loop
task_dict = {}

# Run loop to put the store it in a dictionary.
for line in lines:
   task = line.split(',')[0].strip()
   priority = line.split(',')[1].strip()
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
            print("Task:{}, Priority:{}".format(task,task_dict[task]))

# Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
       NewTask = input("Enter the task:")
       if NewTask not in task_dict: #checking so that we don't enter a duplicate task
            NewPriority = input("Enter the priority of the task entered:")
            # add a new key, value pair to the dictionary
            task_dict.update({NewTask:NewPriority})
            print("\nTask is added to the list")
       else: print("\nEntered task not added, it already exists in the list.")

#Choice 3 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        # locate key and delete it using del function
        if remove_key in task_dict:
           del task_dict[remove_key]
           print("\nTask is deleted from the list")
        else:print("\nEntered task not deleted, it doesn't exist in the list")

# Choice 4 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        with open("Todo.txt", "w") as infile:  # open a file handle
            for task in task_dict:  # loop through key, value and write to file
                infile.write("{}, {}\n".format(task,task_dict[task]))
            print("\nData saved to the file")
# Choice 5- end the program
    elif (strChoice.strip() == '5'):
        print("\nGood-bye.")
        break  # and Exit the program