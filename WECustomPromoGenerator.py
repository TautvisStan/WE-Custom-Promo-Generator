import tkinter as tk
import re
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
import traceback

pages = []

def loadPromo():
    filetypes = (
        ('.promo files', '*.promo'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        titleEntry.delete(0, tk.END)
        titleEntry.insert(-1, lines[0][7:].strip())
        descEntry.delete(0, tk.END)
        descEntry.insert(-1, lines[1][13:].strip())
        wrestlersLine = lines[2][12:].strip().split(',')
        wrestlers = 0
        total = 0
        team1 = 0
        team2 = 0
        ref = 0
        if(len(wrestlersLine) == 1):
            if(wrestlersLine == "-1"):
                ref = 1
            else:
                wrestlers = wrestlersLine[0]
        else:
            for x in wrestlersLine:
                if (x == "1" or x == "2" or x == "3"):
                    wrestlers += 1
                if (x == "11"):
                    team1 = 1
                if (x == "22"):
                    team2 = 1
                if (x == "-1"):
                    ref = 1
        wrestlersEntry.delete(0, tk.END)
        wrestlersEntry.insert(-1, str(wrestlers))
        team1Var.set(team1)
        team2Var.set(team2)
        refVar.set(ref)
        updateID()
        for x in pages:
            x[0].master.destroy()
        pages[:] = []
        i = 0
        for x in lines[3:]:
            newPage()
            pageLine = re.split(r',(?=(?:[^"]|"[^"\\]*(?:\\\\.[^"\\]*)*")*$)', x) #regex source: chatgpt
            line1 = pageLine[0][1:-1]
            line2 = pageLine[1][1:-1]
            speaker = pageLine[2]
            target = pageLine[3]
            taunt = "0"
            if(len(pageLine) > 4):
                taunt = pageLine[4]
            demeanor = "0"
            if(len(pageLine) > 5):
                demeanor = pageLine[5]
                d = int(demeanor)
                if(d > 0):
                    demeanor = "H"
                if(d < 0):
                    demeanor = "A"
            pages[i][0].insert(-1, line1)
            pages[i][1].insert(-1, line2)
            pages[i][2].insert(-1, speaker)
            pages[i][3].insert(-1, target)
            pages[i][4].insert(-1, taunt)
            pages[i][5].insert(-1, demeanor)
            i+=1
    except:
        traceback.print_exc()
        showerror(title='Wrestling Empire Custom Promo Generator', message="Failed to load the file.")

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Wrestling Empire Custom Promo Generator")
root.geometry("600x500")  #Window size is messed up after compiling, dunno why
canvas = tk.Canvas(root, borderwidth=0)
frame = tk.Frame(canvas)
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

versionLabel = tk.Label(frame,text="Version: 1.1.0")
versionLabel.grid()
loadPromoButton = tk.Button(frame, text="Load .promo file", command=loadPromo)
loadPromoButton.grid()
titleLabel = tk.Label(frame,text="Please enter the promo title:")
titleLabel.grid()
titleEntry = tk.Entry(frame)
titleEntry.grid()
descLabel = tk.Label(frame,text="Please enter the promo description: (You can use '[P1]' and '[P2]' to name wrestlers)")
descLabel.grid()
descEntry = tk.Entry(frame,width=100)
descEntry.grid()
wrestlersLabel = tk.Label(frame,text="How many speakers are there? Min 0, max 3, not counting the ref or team partners:")
wrestlersLabel.grid()
wrestlersEntry = tk.Entry(master=frame)
wrestlersEntry.grid()

team1Var = tk.IntVar()
team2Var = tk.IntVar()
refVar = tk.IntVar()
team1Check = tk.Checkbutton(frame,text="Is the wrestler 1 team partner included in the promo?", variable=team1Var, onvalue=1, offvalue=0)
team1Check.grid()
team2Check = tk.Checkbutton(frame,text="Is the wrestler 2 team partner included in the promo?", variable=team2Var, onvalue=1, offvalue=0)
team2Check.grid()
refCheck = tk.Checkbutton(frame,text="Is the ref included in the promo?", variable=refVar, onvalue=1, offvalue=0)
refCheck.grid()

nextStep = tk.Button(frame, text="Update id list", command=lambda:[updateID()])
nextStep.grid()
idFrame = tk.Frame(frame)
idFrame.grid()
newPageButton = tk.Button(frame, text="Create new page", command=lambda:[newPage()])
createPromoButton = tk.Button(frame, text="Create .promo file", command=lambda:[formatPromo()])
newPageButton.grid()
createPromoButton.grid()

def updateID():
    for widgets in idFrame.winfo_children():
      widgets.destroy()
    try:
        wrestlers = int(wrestlersEntry.get())
        team1 = team1Var.get()
        team2 = team2Var.get()
        ref = refVar.get()
        
        for i in range(wrestlers):
            tk.Label(idFrame,text=f"Wrestler {i+1} id: {i+1}").grid()
        if team1 == 1:
            tk.Label(idFrame,text=f"Wrestler 1 team member id: {wrestlers + team1}").grid()
        if team2 == 1:
            tk.Label(idFrame,text=f"Wrestler 2 team member id: {wrestlers + team1 + team2}").grid()
        if ref == 1:
            tk.Label(idFrame,text=f"Ref id: {wrestlers + team1 + team2 + ref}").grid()
        
    except:
        traceback.print_exc()
        showerror(title='Wrestling Empire Custom Promo Generator', message="An error has occured, check if everything is correct and try again!")

def newPage():
    pageInfo = []
    newPageframe = tk.Frame(frame)
    line1Label = tk.Label(newPageframe, text="Enter the first line of the speaker:")
    line1Label.grid()
    line1Entry = tk.Entry(newPageframe, width=100)
    line1Entry.grid()
    pageInfo.append(line1Entry)
    
    line2Label = tk.Label(newPageframe, text="Enter the second line of the speaker:")
    line2Label.grid()
    line2Entry = tk.Entry(newPageframe, width=100)
    line2Entry.grid()
    pageInfo.append(line2Entry)
    
    speakerLabel = tk.Label(newPageframe, text="Enter the speaker id:")
    speakerLabel.grid()
    speakerEntry = tk.Entry(newPageframe)
    speakerEntry.grid()
    pageInfo.append(speakerEntry)
    
    receiverLabel = tk.Label(newPageframe, text="Enter the receiver id:")
    receiverLabel.grid()
    receiverEntry = tk.Entry(newPageframe)
    receiverEntry.grid()
    pageInfo.append(receiverEntry)
    
    tauntLabel = tk.Label(newPageframe, text="Enter the taunt number (0 for none):")
    tauntLabel.grid()
    tauntEntry = tk.Entry(newPageframe)
    tauntEntry.grid()
    pageInfo.append(tauntEntry)
    
    demeanorLabel = tk.Label(newPageframe, text="Is the speaker happy (H) or angry (A)? (enter 0 for none): ")
    demeanorLabel.grid()
    demeanorEntry = tk.Entry(newPageframe)
    demeanorEntry.grid()
    pageInfo.append(demeanorEntry)
    pages.append(pageInfo)
    
    deletePageButton = tk.Button(newPageframe, text="Delete this page", command=lambda:[pages.remove(pageInfo),newPageframe.destroy()])
    deletePageButton.grid()
    separatorLabel = tk.Label(newPageframe, text="--------------------------------------------------------------------------------------------------")
    separatorLabel.grid()

    newPageframe.grid()

def formatPromo():
    try:
        title = titleEntry.get()
        if title == "":
            raise Exception("No title")
        description = descEntry.get()
        if description == "":
            raise Exception("No description")
        if wrestlersEntry.get() == "":
            raise Exception("No wrestlers")
        wrestlers = int(wrestlersEntry.get())
        team1 = team1Var.get()
        team2 = team2Var.get()
        ref = refVar.get()
        total = wrestlers + team1 + team2 + ref
        if len(pages) == 0:
            raise Exception("No pages")
        for x in pages:
            if (x[2].get() == "" or x[3].get() == ""):
                raise Exception("No speaker/target")
        filename = title + ".promo"
        f = open(filename, "w")
        f.write("title: " + title + "\n")
        f.write("description: " + description + "\n")
        f.write("characters: ")
        for i in range(wrestlers):
            if (i != 0):
                f.write(",")
            f.write(str(i+1))
        if (team1 == 1):
                f.write(",11")
        if (team2 == 1):
                f.write(",22")
        if(wrestlers != 0 and ref == 1):
            f.write(",")
        if (ref == 1):
            f.write("-1")
        f.write("\n")
        for x in pages:
            strline = '"' + x[0].get() + '","' + x[1].get() + '",' + x[2].get() + ',' + x[3].get() + ',' + x[4].get() + ','
            if (x[5].get() == "H"):
                d = 50
            if (x[5].get() == "A"):
                d = -50
            if (x[5].get() == "0"):
                d = 0
            strline += str(d)
            f.write(strline + "\n")
        f.close()
        showinfo(title='Wrestling Empire Custom Promo Generator', message=".promo file was successfully generated! You can now close this tool")
    except:
        traceback.print_exc()
        showerror(title='Wrestling Empire Custom Promo Generator', message="An error has occured, check if everything is correct and try again!")


root.mainloop()
