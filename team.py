from tkinter import *
import mysql.connector
from functools import partial
import sys
import os
mydb = mysql.connector.connect(
    host="localhost",
    user="dbms",
    password="dbms",
    database="project"
)

mycursor = mydb.cursor()
root =Tk()
root.minsize(height=400,width=300)
Label(root,text="TEAMS", font="comicsanms 13 bold",pady=15).grid(row=0,column=3)

tname = Label(root,text="Team name :").grid(row=2,column=2)
hcity= Label(root,text="Homecity :").grid(row=3,column=2)
win= Label(root,text="Win :").grid(row=4,column=2)
total_matches = Label(root,text="Total matches:").grid(row=5,column=2)


tnamevalue = StringVar()
hcityvalue = StringVar()
winvalue = StringVar()
total_matchesvalue = StringVar()


tnameentry =Entry(root,textvariable=tnamevalue).grid(row=2,column=3)
hcityentry =Entry(root,textvariable=hcityvalue).grid(row=3,column=3)
winentry =Entry(root,textvariable=winvalue).grid(row=4,column=3)
total_matchesentry =Entry(root,textvariable=total_matchesvalue).grid(row=5,column=3)

updateID = 0

def getteam():
    mycursor.execute("select * from teams")
    playerList = mycursor.fetchall()
    
    Label(root,text='Team Name').grid(row=9, column=3)
    Label(root,text='Homecity').grid(row=9, column=4)
    Label(root,text='Win').grid(row=9, column=5)
    Label(root,text='Total matches').grid(row=9, column=6)
    for i in range((len(playerList))):
        for j in range((len(playerList[i]))):
            Label(root,text=playerList[i][j]).grid(row=10+i, column=j+2)
        Button(root, text=f"Delete" , padx=20,pady=5, fg="black",bg="white" , command=partial(deleteteam, playerList[i][0])).grid(row=10+i , column=8)
        Button(root, text=" Edit" , padx=20,pady=5, fg="black",bg="white" , command=partial(editteam, playerList[i][0])).grid(row=10+i , column=10)

def editteam(id):
    mycursor.execute(f'SELECT * FROM teams WHERE id={id}')
    team = mycursor.fetchone()
    
    tnamevalue.set(team[1])
    hcityvalue.set(team[2])
    winvalue.set(team[3])
    total_matchesvalue.set(team[4])
    global updateID
    updateID = id

def refresh():
    for widget in root.winfo_children():
        widget.destroy()
    Label(root,text="TEAMS", font="comicsanms 13 bold",pady=15).grid(row=0,column=3)
    
    tname = Label(root,text="Team name :").grid(row=2,column=2)
    hcity = Label(root,text="Homecity :").grid(row=3,column=2)
    win = Label(root,text="Win:").grid(row=4,column=2)
    teammatch= Label(root,text="Team match :").grid(row=5,column=2)

    
    tnameentry =Entry(root,textvariable=tnamevalue).grid(row=2,column=3)
    hcityentry =Entry(root,textvariable=hcityvalue).grid(row=3,column=3)
    winentry =Entry(root,textvariable=winvalue).grid(row=4,column=3)
    teammatchentry =Entry(root,textvariable=total_matchesvalue).grid(row=5,column=3)
    mybutton1 = Button(root, text="Submit" , padx=20,pady=5, fg="black",bg="white" , command= addteam).grid(row=7 , column=3)
    mybutton2 = Button(root, text="Update" , padx=20,pady=5, fg="black",bg="white" , command= updateteam).grid(row=7 , column=4)
    mybutton3 = Button(root, text="back" , padx=20,pady=5, fg="black",bg="white" , command= CallBack).grid(row=0, column=0)


def deleteteam(id):
    mycursor.execute(f'delete from teams where id={id}')
    mydb.commit()
    refresh()
    getteam()

def updateteam():
    mycursor.execute("update teams set tname=%s, hcity=%s, win=%s,total_matches=%s WHERE id=%s",(tnamevalue.get(),hcityvalue.get(),winvalue.get(),total_matchesvalue.get(), updateID))
    
    tnamevalue.set('')
    hcityvalue.set('')
    winvalue.set('')
    total_matchesvalue.set('')
    mydb.commit()
    getteam()

def addteam():
    mycursor.execute("insert into teams(tname,hcity,win,total_matches) values (%s,%s,%s,%s)",(tnamevalue.get(),hcityvalue.get(),winvalue.get(),total_matchesvalue.get()))
    
    tnamevalue.set('')
    hcityvalue.set('')
    winvalue.set('')
    total_matchesvalue.set('')
    mydb.commit()
    getteam()


mybutton1 = Button(root, text="Submit" , padx=20,pady=5, fg="black",bg="white" , command= addteam).grid(row=7 , column=3)
mybutton2 = Button(root, text="Update" , padx=20,pady=5, fg="black",bg="white" , command= updateteam).grid(row=7 , column=4)


def CallBack():
    filename = 'index.py'
    os.system(filename)
    os.system('notepad'+filename)
mybutton3 = Button(root, text="back" , padx=20,pady=5, fg="black",bg="white" , command= CallBack).grid(row=0, column=0)

getteam()






root.mainloop()