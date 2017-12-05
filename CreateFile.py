from tkinter import *
import os

root = Tk()
root.title("CreateWebFile")

def GetUserFilename():
    return userEntryFilename.get()

def GetUserFilePath():
    return userEntryFilepath.get()

def createFile():
    fileExtension = [".html", ".css", ".js"]
    for index in range(len(fileExtension)):
        if (GetUserFilePath() == ""):
            #if no user input, use default path
            userDirectory = "C:/Users/Ai Li/Desktop/MyWeb"
        else:
            #user must change all the \ to / in the path
            userDirectory = '\"' + GetUserFilePath() + '\"'

        whereToCreate = os.path.join(userDirectory, GetUserFilename() + fileExtension[index])
        f = open(whereToCreate, "w+")
        f.close()

    displayStatus()

def clearFilename():
    userEntryFilename.delete(0, END)
    userEntryFilename.insert(0,"")

def clearPath():
    userEntryFilepath.delete(0, END)
    userEntryFilepath.insert(0,"")

def displayStatus():
    status = Label(root, text = 'Done! :)')
    status.grid(row = 3, column = 2)

#GUI layout
filename = Label(root, text = "File Name: ")
filename.grid(row = 0, column = 0, padx = 10, pady = 10)
userEntryFilename = Entry(root)
userEntryFilename.grid(row = 0, column = 1, padx = 10, pady = 10)

clearFile = Button(root, text = "Clear", command = clearFilename)
clearFile.grid(row = 0, column = 2, padx = 10)

clearPath = Button(root, text = "Clear", command = clearPath)
clearPath.grid(row = 1, column = 2, padx = 10)

destPath = Label(root, text = "Path: ")
destPath.grid(row = 1, column = 0, padx = 10, pady = 10)
userEntryFilepath = Entry(root)
userEntryFilepath.grid(row = 1, column = 1, padx = 10, pady = 10)

my_button = Button(root, text = "Create", command = createFile)
my_button.grid(row = 3, column = 1, padx = 10, pady = 10)

# future development
# var = StringVar()
# htmlOption = Radiobutton(root, text = "HTML", variable = var, value = ".html", command = sel)
# htmlOption.grid(row = 3, column = 0)
#
# cssOption = Radiobutton(root, text = "CSS", variable = var, value = ".css", command = sel)
# cssOption.grid(row = 4, column = 0)
#
# jsOption = Radiobutton(root, text = "JS", variable = var, value = ".js", command = sel)
# jsOption.grid(row = 5, column = 0)

root.mainloop()