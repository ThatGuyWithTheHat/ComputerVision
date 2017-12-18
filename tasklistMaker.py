# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:43:23 2017

@author: mattd
"""
import os.path

def addToList():
    taskList = []
    while(1):
        x = input("Name of Task(or q to quit):")
        if(x == "q"):
            break
        x = [x,0]
        #print(x)
        taskList.append(x)
    return taskList

def printList(taskList):
    count = 0
    isChecked = ["unchecked", "Checked"]
    for item in taskList:
        taskName = item[0]
        index = item[1]
        check = isChecked[index]
        print(str(count) + " " + taskName + " " + check)
        count = count + 1
    return count

def checkItem(taskList):
    count = 0

    while(1):
        count = printList(taskList)
        inp = input("Which one would you like to check?(q to quit)")
        if(inp == 'q'):
            break
        if(int(inp) <= count and int(inp) >= 0):
            x = taskList[int(inp)] 
            x[1] = 1
            taskList[int(inp)] = x

    return taskList
            
def saveList(taskList):
    file = open("taskList.txt",'w')
    for item in taskList:
        file.write(item[0] + " ;,; " + str(item[1]) + "\n")
    file.close()


taskList = []
if(os.path.isfile("taskList.txt")):
    f = open("taskList.txt",'r')
    x = []
    for line in f:
        x.append(line)
    
    for item in x:
        y = item.split(" ;,; ")
        y[1] = int(y[1])
        taskList.append(y)
    f.close()
while(1):
    print("What would you like to do?")
    inp = input("[S]Save [Q]Quit [A]Add [C]Check Item Off [R] Review \n")
    inp = inp.lower()
    if(inp == 'q'):
        break
    if(inp == 'a'):
        newTasks = addToList()
        for item in newTasks:
            taskList.append(item)
        for item in taskList:
            print(item)
    if(inp == 'c'):
        taskList = checkItem(taskList)
    if(inp == 'r'):
        printList(taskList)
    if(inp == 's'):
        saveList(taskList)

code = []
code = "<fieldset>\n\t<legend>Task List</legend>\n"
for item in taskList:
    if(item[1] == 1):
        code= code + '\t<div>\n\t\t\t<input type="checkbox" checked>\n \t\t <label>\n'
    else:
        code = code + '\t<div>\n\t\t<input type="checkbox">\n\t\t<label>\n'
    code = code + "\t\t\t" +item[0] + '\n'
    code = code + '\t\t</label>\n\t</div>\n'
    
code = code + '</fieldset>'

print(code)



