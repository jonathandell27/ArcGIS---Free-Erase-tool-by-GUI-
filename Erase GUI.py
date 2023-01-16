import arcpy
import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


root = Tk()

Inputlist = []

Eraselist = []

savenamelist = []

inputfiledslist = []


def Inputfun():
    root.directory = filedialog.askopenfilename()
    InputLayer = root.directory
    Input= r'{}'.format(InputLayer) #Select from a folder
    if len(Inputlist) < 1 :
        Inputlist.append(Input)
    else:
        Inputlist.remove(Inputlist[0])
        Inputlist.append(Input)
    path1.config(text="{}".format(Inputlist[0]))


def Erasefun():
    root.directory = filedialog.askopenfilename()
    EraseLayer = root.directory
    Erase = r'{}'.format(EraseLayer)  # Select from a folder
    if len(Eraselist) < 1 :
        Eraselist.append(Erase)
    else:
        Eraselist.remove(Eraselist[0])
        Eraselist.append(Erase)
    path2.config(text="{}".format(Eraselist[0]))

def savefile():
    savepath = filedialog.askdirectory()
    savename = savepath
    if len(savenamelist) < 1 :
        savenamelist.append(savename)
    else:
        Eraselist.remove(savenamelist[0])
        Eraselist.append(savename)
    path3.config(text="{}".format(savenamelist[0]))

def run ():
    inputfileds =  arcpy.ListFields(Inputlist[0])
    for i in inputfileds:
        f = i.baseName
        inputfiledslist.append(f)
    name = text.get()
    arcpy.analysis.Union((Eraselist[0],Inputlist[0]), r"{}\f{}.shp".format(savenamelist[0],name), "ALL", None, "GAPS") #Select from a folder
    output1 =  r"{}\f{}.shp".format(savenamelist[0],name)
    Fieldnames = arcpy.ListFields(output1)
    FIDEarse = Fieldnames[2]
    FID= FIDEarse.baseName
    arcpy.analysis.Select(output1, r"{}\{}.shp".format(savenamelist[0],name), "{} = -1".format(FID))
    finallayer = r"{}\{}.shp".format(savenamelist[0],name)
    arcpy.management.Delete(output1)
    Fieldnames = arcpy.ListFields(finallayer)
    for i in Fieldnames[:len(inputfileds) + 2]:
        if i.baseName != "ObjectID" and i.baseName != "FID" and i.baseName != "Shape" and i.baseName != "OBJECTID":  #and i.baseName != "Shape_Length" and i.baseName != "Shape_Area":
            arcpy.management.DeleteField(finallayer, i.baseName)
    endtxt.config(text="The process was completed successfully!")


root.title("Erase Free")
root.geometry('600x600')
button1 = Button(root, text="Input Feature",bg='#0052cc', fg='#ffffff',height = 2, width = 20, padx = 80 , font = ('Sans','10','bold'), command  =Inputfun)
path1 = Label(root, text="")
button2 = Button(root, text="Erase Feature",bg='#0052cc', fg='#ffffff',height = 2, width = 20,padx = 80, font = ('Sans','10','bold'), command  =Erasefun)
path2 = Label(root, text="")
button3 = Button(root, text="Output Folder Location",bg='#0052cc', fg='#ffffff',height = 2, width = 20,font = ('Sans','10','bold'),padx = 80, command  =savefile)
path3 = Label(root, text="")
button4 = Button(root, text="Run",bg='#0052cc', fg='#ffffff',height = 2, width = 20,padx = 80,font = ('Sans','10','bold'), command  =run)
filename = StringVar()
text = Entry(root, textvariable = filename)
textlable = Label(root,text="File Name:",height = 2, width = 20,padx = 80,font = ('Sans','10','bold'))
button1.place(x=150, y=50)
path1.place(x=50, y=100,height = 20, width = 500)
button2.place(x=150, y=150)
path2.place(x=50, y=200,height = 20, width = 500)
button3.place(x=150, y=250)
path3.place(x=50, y=300,height = 20, width = 500)
textlable.place(x=150, y=350)
text.place(x=230, y=400, height = 20, width = 150)
button4.place(x=150, y=450)
endtxt = Label(root, text="",height = 2, width = 20,padx = 80,font = ('Sans','10','bold'))
endtxt.place(x=100, y=500)

root.mainloop()

#======================================================================================================
