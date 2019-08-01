'''
Title: create a script which uses functions to read ToDo list from a "ToDo.txt" text file and do following tasks:
Show current data, Add a new item, Remove an existing item, Save Data to File and Exit Program(hw6.py)
Date: 7/30/2019
Dev: Kiran Varaganti
Dependencies: python 3x
'''

infile = "ToDo.txt" #store path of ToDo.txt file as a variable so that it can be accessed later in the program

# Choice 1 - Function to show the current items in the table
def Show_Tasks(Input_dict):
    """Show current Todo list tasks along with its priority"""
    for task in Input_dict: # loop through the dictionary here and print items
        print("Task:{}, Priority:{}".format(task, Input_dict[task]))

# Choice 2 - Function to add a new item to the list/Table
def Add_Task(Input_dict):
    """Add user entered tasks and its priority"""
    NewTask = input("Enter the task:")
    if NewTask not in Input_dict: #checking so that we don't enter a duplicate task
        NewPriority = input("Enter the priority of the task entered:")
        # add a new key, value pair to the dictionary
        Input_dict.update({NewTask:NewPriority})
        print("\nTask is added to the list")
    else: print("\nEntered task not added, it already exists in the list.")
    return Input_dict

#Choice 3 - Function to remove a new item to the list/Table
def Remove_Task(Input_dict):
    """Delete user entered tasks and its priority"""
    remove_key = input("Enter the task name to remove: ")
    # locate key and delete it using del function
    if remove_key in Input_dict:
        del Input_dict[remove_key]
        print("\nTask is deleted from the list")
    else:print("\nEntered task not deleted, it doesn't exist in the list")
    return Input_dict

# Choice 4 - Function to Save added/deleted tasks to the ToDo.txt file
def Save_Data(Input_dict, Input_file):
    """Write new ToDo list to the text file"""
    with open(Input_file, "w") as file:  # open a file handle
        for task in Input_dict:  # loop through key, value and write to file
            file.write("{}, {}\n".format(task, Input_dict[task]))
        print("\nData saved to the file")
# Choice 5- Function to end the program
def exit():
    """Exit the program"""
    print("\nGood-bye!")

def main():# Created a main function to encapulsate the main code.
    # read in ToDo.txt here
    with open(infile, 'r') as todo_file:
        lines = todo_file.readlines()
    task_dict = {}  # create an empty dictionary to store data as we loop

    # Run loop to put the store it in a dictionary.
    for line in lines:
        task = line.split(',')[0].strip()
        priority = line.split(',')[1].strip()
        task_dict[task] = priority

    while(True):
        print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
        strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
        print()#adding a new line
        if (strChoice.strip() == '1'):
            Show_Tasks(task_dict)
        elif(strChoice.strip() == '2'):
            Add_Task(task_dict)
        elif(strChoice.strip() == '3'):
            Remove_Task(task_dict)
        elif(strChoice.strip() == '4'):
            Save_Data(task_dict, infile)
        elif(strChoice.strip() == '5'):
            exit()
            break

# start the program
if __name__=="__main__":
    main()