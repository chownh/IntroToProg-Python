# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Nahien Chowdhury, 11.01.2019
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None   # An object that represents a file
strData = 'ToDoList.txt'  # A row of text data from the file
dicRow = {'Tasks': 'What do you need to do?', 'Priority': 'How Important is this Task?' }    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.

objFile = open(strData, "w")

def strMenu():
    print(" \n Menu of Options \n 1) Show Current Data \n 2) Add a New Item \n 3) Remove an Existing Item \n 4) Save to File \n 5) Exit Program \n")
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    strMenu()
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your current Data is: \n")
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while (True):
            objFile = open(strData, "a")
            print("Type in your tasks and priority (Low, Med, High); Type exit to quit. \n")
            Task = input("Enter Tasks: ")
            if (Task.lower() == "exit"):
                break
            else:objFile.write(Task + ", ")
            print('How Important? Type Low, Med or High \n')
            Priority = input("Low, Med, or High: ")
            if (Priority.lower() == "exit"):
                break
            else:objFile.write(Priority + '\n')
            lstTable=[Task, Priority]
            #objFile.write(lstTable[0] + ', ' + lstTable[1] + '\n')
            objFile.close()
                #objFile.write(dicRow)
             #   objFile.close()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        removedTask = lstTable.pop()
        removedPriority = lstTable.pop()
        print("Removed these items from the list: \n")
        print(removedTask)
        print(removedPriority)
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile.close()
        print("Data saved to file!")
        print()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("End of Script. Thanks for using. Press Enter to Exit")
        break  # and Exit the program
