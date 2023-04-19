import tkinter as tk
import traceback

title = ""
description = ""
wrestlers = -1
total = -1
team1 = -1
team2 = -1
ref = -1
baseInfo = []
pages = []

def formatPromo(button1, button2):
    try:
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
        for x in pages:
            for i in range(6):
                x[i].config(state="disabled")
        button1.grid_forget()
        button2.grid_forget()
        wd = tk.Tk()
        wd.title("Wrestling Empire Custom Promo Generator")
        label = tk.Label(wd, text=".promo file was successfully generated! You can now close this tool")
        label.pack()
    except:
        traceback.print_exc()
        wd = tk.Tk()
        wd.title("Wrestling Empire Custom Promo Generator")
        label = tk.Label(wd, text="An error has occured, check if everything is correct and try again!")
        label.pack()

def newPage(frame):
    pageInfo = []
    newPagecanvas = tk.Canvas(frame)
    line1Label = tk.Label(newPagecanvas, text="Enter the first line of the speaker:")
    line1Label.grid()
    line1Entry = tk.Entry(newPagecanvas, width=100)
    line1Entry.grid()
    pageInfo.append(line1Entry)
    
    line2Label = tk.Label(newPagecanvas, text="Enter the second line of the speaker:")
    line2Label.grid()
    line2Entry = tk.Entry(newPagecanvas, width=100)
    line2Entry.grid()
    pageInfo.append(line2Entry)
    
    speakerLabel = tk.Label(newPagecanvas, text="Enter the speaker id:")
    speakerLabel.grid()
    speakerEntry = tk.Entry(newPagecanvas)
    speakerEntry.grid()
    pageInfo.append(speakerEntry)
    
    receiverLabel = tk.Label(newPagecanvas, text="Enter the receiver id:")
    receiverLabel.grid()
    receiverEntry = tk.Entry(newPagecanvas)
    receiverEntry.grid()
    pageInfo.append(receiverEntry)
    
    tauntLabel = tk.Label(newPagecanvas, text="Enter the taunt number (0 for none):")
    tauntLabel.grid()
    tauntEntry = tk.Entry(newPagecanvas)
    tauntEntry.grid()
    pageInfo.append(tauntEntry)
    
    demeanorLabel = tk.Label(newPagecanvas, text="Is the speaker happy (H) or angry (A)? (enter 0 for none): ")
    demeanorLabel.grid()
    demeanorEntry = tk.Entry(newPagecanvas)
    demeanorEntry.grid()
    pageInfo.append(demeanorEntry)
    pages.append(pageInfo)
    
    separatorLabel = tk.Label(newPagecanvas, text="--------------------------------------------------------------------------------------------------")
    separatorLabel.grid()
    newPagecanvas.grid()


def nextStepClicked(nextStep,frame,errorLabel,baseInfo):
    errorLabel.grid_forget()
    try:
        global title
        title = baseInfo[0].get()
        if title == "":
            raise Exception("No title")
        global description
        description = baseInfo[1].get()
        if description == "":
            raise Exception("No description")
        if baseInfo[2].get() == "":
            raise Exception("No wrestlers")
        global wrestlers
        wrestlers = int(baseInfo[2].get())
        global team1
        team1 = baseInfo[3].get()
        global team2
        team2 = baseInfo[4].get()
        global ref
        ref = baseInfo[5].get()
        global total
        total = wrestlers + team1 + team2 + ref
        
        for i in range(wrestlers):
            tk.Label(master=frame,text=f"Wrestler {i+1} id: {i+1}").grid()
        if team1 == 1:
            tk.Label(master=frame,text=f"Wrestler 1 team member id: {wrestlers + team1}").grid()
        if team2 == 1:
            tk.Label(master=frame,text=f"Wrestler 2 team member id: {wrestlers + team1 + team2}").grid()
        if ref == 1:
            tk.Label(master=frame,text=f"Ref id: {wrestlers + team1 + team2 + ref}").grid()
        baseInfo[0].config(state="disabled")
        baseInfo[1].config(state="disabled")
        baseInfo[2].config(state="disabled")
        baseInfo[6].config(state="disabled")
        baseInfo[7].config(state="disabled")
        baseInfo[8].config(state="disabled")
        newPageButton = tk.Button(frame, text="Create new page", command=lambda:[newPage(frame)])
        newPageButton.grid()
        createPromoButton = tk.Button(frame, text="Create .promo file", command=lambda:[formatPromo(newPageButton,createPromoButton)])
        createPromoButton.grid()
        nextStep.grid_forget()
    except:
        traceback.print_exc()
        errorLabel.grid()



def main(frame): 
        
    titleLabel = tk.Label(frame,text="Please enter the promo title:")
    titleLabel.grid()
    titleEntry = tk.Entry(frame)
    titleEntry.grid()
    baseInfo.append(titleEntry)
    descLabel = tk.Label(frame,text="Please enter the promo description: (You can use '[P1]' and '[P2]' to name wrestlers)")
    descLabel.grid()
    descEntry = tk.Entry(frame,width=100)
    descEntry.grid()
    baseInfo.append(descEntry)
    wrestlersLabel = tk.Label(frame,text="How many speakers are there? Min 0, max 3, not counting the ref or team partners:")
    wrestlersLabel.grid()
    wrestlersEntry = tk.Entry(master=frame)
    wrestlersEntry.grid()
    baseInfo.append(wrestlersEntry)

    team1Var = tk.IntVar()
    team2Var = tk.IntVar()
    refVar = tk.IntVar()
    team1Check = tk.Checkbutton(frame,text="Is the wrestler 1 team partner included in the promo?", variable=team1Var, onvalue=1, offvalue=0)
    team1Check.grid()
    baseInfo.append(team1Var)
    team2Check = tk.Checkbutton(frame,text="Is the wrestler 2 team partner included in the promo?", variable=team2Var, onvalue=1, offvalue=0)
    team2Check.grid()
    baseInfo.append(team2Var)
    refCheck = tk.Checkbutton(frame,text="Is the ref included in the promo?", variable=refVar, onvalue=1, offvalue=0)
    refCheck.grid()
    baseInfo.append(refVar)
    baseInfo.append(team1Check)
    baseInfo.append(team2Check)
    baseInfo.append(refCheck)

    errorLabel = tk.Label(frame,text="An error has occured, check if everything is correct and try again!")
    nextStep = tk.Button(frame, text="Next step", command=lambda:[nextStepClicked(nextStep,frame,errorLabel,baseInfo)])
    nextStep.grid()
    

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Wrestling Empire Custom Promo Generator")
root.geometry("800x800")
canvas = tk.Canvas(root, borderwidth=0)
frame = tk.Frame(canvas)
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

main(frame)

root.mainloop()