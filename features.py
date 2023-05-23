import tkinter as tk
import traceback
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter import filedialog as fd
import dataContainers
import re
import os
def updateID(idFrame, basePromoData):
    try:
        wrestlers = int(basePromoData.wrestlersEntry.get())
        team1 = basePromoData.team1Var.get()
        team2 = basePromoData.team2Var.get()
        ref = basePromoData.refVar.get()
        for widgets in idFrame.winfo_children():
            widgets.destroy()
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

def newPage(frame, pages):
    newPageframe = tk.Frame(frame)
    line1Label = tk.Label(newPageframe, text="Enter the first line of the speaker:")
    line1Label.grid(row=1)
    line1Entry = tk.Entry(newPageframe, width=50)
    line1Entry.grid(row=2)
    
    line2Label = tk.Label(newPageframe, text="Enter the second line of the speaker:")
    line2Label.grid(row=3)
    line2Entry = tk.Entry(newPageframe, width=50)
    line2Entry.grid(row=4)
    
    speakerLabel = tk.Label(newPageframe, text="Enter the speaker id:")
    speakerLabel.grid(row=5)
    speakerEntry = tk.Entry(newPageframe)
    speakerEntry.grid(row=6)
    
    receiverLabel = tk.Label(newPageframe, text="Enter the receiver id:")
    receiverLabel.grid(row=7)
    receiverEntry = tk.Entry(newPageframe)
    receiverEntry.grid(row=8)
    
    tauntLabel = tk.Label(newPageframe, text="Enter the taunt name or number (0 for none):")
    tauntLabel.grid(row=9)
    tauntEntry = tk.Entry(newPageframe)
    tauntEntry.grid(row=10)
    
    demeanorLabel = tk.Label(newPageframe, text="Is the speaker happy (H) or angry (A)? (enter 0 for none): ")
    demeanorLabel.grid(row=11)
    demeanorEntry = tk.Entry(newPageframe)
    demeanorEntry.grid(row=12)
    featureData = []
    pageInfo = dataContainers.singlePageData(line1Entry, line2Entry, speakerEntry, receiverEntry, tauntEntry, demeanorEntry, featureData)
    pages.append(pageInfo)
    
    
    addNewFeatureButton = tk.Button(newPageframe, text="Add new feature", command=lambda:[newFeature(newPageframe, pageInfo.featureData)])
    addNewFeatureButton.grid(row=13)
    
    FrameFooter = tk.Frame(newPageframe)
    newPageframe.grid()
    deletePageButton = tk.Button(FrameFooter, text="Delete this page", command=lambda:[pages.remove(pageInfo),newPageframe.destroy(), FrameFooter.destroy()])
    deletePageButton.grid()
    separatorLabel = tk.Label(FrameFooter, text="--------------------------------------------------------------------------------------")
    separatorLabel.grid()

    FrameFooter.grid(row=100)
    
    return newPageframe, featureData

def newFeature(frame, features):
    newFeatureframe = tk.Frame(frame)
    featureLabel = tk.Label(newFeatureframe, text="Enter the promo feature")
    featureLabel.grid()
    featureEntry = tk.Entry(newFeatureframe, width=50)
    featureEntry.grid()
    featureInfo = dataContainers.singleFeatureData(featureEntry)
    features.append(featureInfo)
    deleteFeatureButton = tk.Button(newFeatureframe, text="Delete this feature", command=lambda:[lambda: features.remove(featureInfo),newFeatureframe.destroy()])
    deleteFeatureButton.grid()
    newFeatureframe.grid(row=len(features)+13)
def formatPromo(basePromoData, pages):
    try:
        title = basePromoData.titleEntry.get()
        if title == "":
            raise Exception("No title")
        description = basePromoData.descEntry.get()
        if description == "":
            raise Exception("No description")
        if basePromoData.wrestlersEntry.get() == "":
            raise Exception("No wrestlers")
        wrestlers = int(basePromoData.wrestlersEntry.get())
        team1 = basePromoData.team1Var.get()
        team2 = basePromoData.team2Var.get()
        ref = basePromoData.refVar.get()
        total = wrestlers + team1 + team2 + ref
        if len(pages) == 0:
            raise Exception("No pages")
        for x in pages:
            if (x.speakerEntry.get() == "" or x.receiverEntry.get() == ""):
                raise Exception("No speaker/target")
        filetypes = [('.promo files', '*.promo'),
                    ('All files', '*.*')]
        filename = fd.asksaveasfilename(
            title='Save a file',
            initialdir=basePromoData.fileDirectory,
            filetypes=filetypes,
            initialfile=title + ".promo")
        basePromoData.fileDirectory = os.path.split(filename)[0]
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
            strline = '"' + x.line1Entry.get() + '","' + x.line2Entry.get() + '",' + x.speakerEntry.get() + ',' + x.receiverEntry.get() + ',' + x.tauntEntry.get() + ','
            d = 0
            if (x.demeanorEntry.get() == "H"):
                d = 50
            if (x.demeanorEntry.get() == "A"):
                d = -50
            if (x.demeanorEntry.get() == "0"):
                d = 0
            strline += str(d)
            f.write(strline)
            if x.featureData:
                f.write(',')
                feature = ""
                for y in x.featureData:
                    feature += y.featureEntry.get() + ';'
                feature = feature.strip(';')    
                f.write(feature)
            f.write("\n")
        f.close()
        showinfo(title='Wrestling Empire Custom Promo Generator', message=".promo file was successfully generated! You can now close this tool")
    except:
        traceback.print_exc()
        showerror(title='Wrestling Empire Custom Promo Generator', message="An error has occured, check if everything is correct and try again!")

def cleanUp(basePromoData, pages, idFrame, canvas):
    canvas.yview_moveto(0)
    basePromoData.titleEntry.delete(0, tk.END)
    basePromoData.descEntry.delete(0, tk.END)
    basePromoData.wrestlersEntry.delete(0, tk.END)
    basePromoData.team1Var.set(0)
    basePromoData.team2Var.set(0)
    basePromoData.refVar.set(0)
    for widgets in idFrame.winfo_children():
        widgets.destroy()
    tk.Label(idFrame,text="No wrestlers").grid()
    for x in pages:
        x.line1Entry.master.destroy()
    pages[:] = []

def loadPromo(basePromoData, pages, idFrame, frame, canvas):
    filetypes = (
        ('.promo files', '*.promo'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=basePromoData.fileDirectory,
        filetypes=filetypes)
    try:
        cleanUp(basePromoData, pages, idFrame, canvas)
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        basePromoData.fileDirectory = os.path.split(filename)[0]
        basePromoData.titleEntry.insert(-1, lines[0][7:].strip())
        basePromoData.descEntry.insert(-1, lines[1][13:].strip())
        wrestlersLine = lines[2][12:].strip().split(',')
        wrestlers = 0
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
        basePromoData.wrestlersEntry.insert(-1, str(wrestlers))
        basePromoData.team1Var.set(team1)
        basePromoData.team2Var.set(team2)
        basePromoData.refVar.set(ref)
        updateID(idFrame, basePromoData)

        for i, x in enumerate(lines[3:]):
            newPageFrame, featureData = newPage(frame, pages)
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
                demeanor = pageLine[5].strip()
                d = int(demeanor)
                if(d > 0):
                    demeanor = "H"
                if(d < 0):
                    demeanor = "A"
            pages[i].line1Entry.insert(-1, line1)
            pages[i].line2Entry.insert(-1, line2)
            pages[i].speakerEntry.insert(-1, speaker)
            pages[i].receiverEntry.insert(-1, target)
            pages[i].tauntEntry.insert(-1, taunt)
            pages[i].demeanorEntry.insert(-1, demeanor)
            if(len(pageLine) > 6):
                featureLine = pageLine[6].split(';')
                for j, y in enumerate(featureLine):
                    newFeature(newPageFrame, pages[i].featureData)
                    pages[i].featureData[j].featureEntry.insert(-1, featureLine[j].strip())
                    
    except:
        traceback.print_exc()
        showerror(title='Wrestling Empire Custom Promo Generator', message="Failed to load the file.")
