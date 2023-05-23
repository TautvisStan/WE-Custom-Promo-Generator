import dataContainers
import features
import re
import tkinter as tk
import ctypes
import webbrowser

ctypes.windll.shcore.SetProcessDpiAwareness(True)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Wrestling Empire Custom Promo Generator")
root.geometry("600x500")
canvas = tk.Canvas(root, borderwidth=0)
frame = tk.Frame(canvas)
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

def donothing():
    pass

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=lambda:[features.cleanUp(basePromoData, pages, idFrame, canvas)])
filemenu.add_command(label="Open", command=lambda:[features.loadPromo(basePromoData, pages, idFrame, frame, canvas)])
filemenu.add_command(label="Save", command=lambda:[features.formatPromo(basePromoData,pages)])
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

def openWebsite():
    webbrowser.open("https://thunderstore.io/c/wrestling-empire/p/GeeEm/PromoGenerator/",new=1)
    
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=openWebsite)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

titleFrame = tk.Frame(frame)
versionLabel = tk.Label(frame,text="Version: 1.2.0")
versionLabel.grid()
titleLabel = tk.Label(titleFrame,text="Please enter the promo title:")
titleLabel.grid()
titleEntry = tk.Entry(titleFrame)
titleEntry.grid()
titleFrame.grid()

descFrame = tk.Frame(frame)
descLabel = tk.Label(descFrame,text="Please enter the promo description: (You can use '[P1]' and '[P2]' to name wrestlers)")
descLabel.grid()
descEntry = tk.Entry(descFrame,width=50)
descEntry.grid()
descFrame.grid()

wrestlersFrame = tk.Frame(frame)
wrestlersLabel = tk.Label(wrestlersFrame,text="How many speakers are there? Min 0, max 3, not counting the ref or team partners:")
wrestlersLabel.grid()
wrestlersEntry = tk.Entry(wrestlersFrame)
wrestlersEntry.grid()
wrestlersFrame.grid()

team1Var = tk.IntVar()
team2Var = tk.IntVar()
refVar = tk.IntVar()
team1Check = tk.Checkbutton(frame,text="Is the wrestler 1 team partner included in the promo?", variable=team1Var, onvalue=1, offvalue=0)
team1Check.grid()
team2Check = tk.Checkbutton(frame,text="Is the wrestler 2 team partner included in the promo?", variable=team2Var, onvalue=1, offvalue=0)
team2Check.grid()
refCheck = tk.Checkbutton(frame,text="Is the ref included in the promo?", variable=refVar, onvalue=1, offvalue=0)
refCheck.grid()

basePromoData = dataContainers.basePromoData(titleEntry, descEntry, wrestlersEntry, team1Var, team2Var, refVar)
pages = []

idFrame = tk.Frame(frame)
nextStep = tk.Button(frame, text="Update id list", command=lambda:[features.updateID(idFrame, basePromoData)])
nextStep.grid()

idFrame.grid()
tk.Label(idFrame,text="No wrestlers").grid()
newPageButton = tk.Button(frame, text="Create new page", command=lambda:[features.newPage(frame, pages)])
createPromoButton = tk.Button(frame, text="Create .promo file", command=lambda:[features.formatPromo(basePromoData,pages)])
newPageButton.grid()
createPromoButton.grid()
separatorLabel = tk.Label(frame, text="--------------------------------------------------------------------------------------")
separatorLabel.grid()

root.mainloop()