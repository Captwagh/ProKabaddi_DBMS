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
Label(root,text="PLAYER", font="comicsanms 13 bold",pady=15).grid(row=0,column=3)
Name = Label(root,text="Name :").grid(row=2,column=2)
Age = Label(root,text="Age :").grid(row=3,column=2)
Team_name = Label(root,text="Team_name :").grid(row=4,column=2)
Type = Label(root,text="Type :").grid(row=5,column=2)


Namevalue = StringVar()
Agevalue = StringVar()
Team_namevalue = StringVar()
Typevalue = StringVar()


Nameentry =Entry(root,textvariable=Namevalue).grid(row=2,column=3)
Ageentry =Entry(root,textvariable=Agevalue).grid(row=3,column=3)
Team_nameentry =Entry(root,textvariable=Team_namevalue).grid(row=4,column=3)
Typeentry =Entry(root,textvariable=Typevalue).grid(row=5,column=3)

updateID = 0

def getplayer():
    mycursor.execute("select * from players")
    playerList = mycursor.fetchall()
    Label(root,text='ID').grid(row=9, column=2)
    Label(root,text='Name').grid(row=9, column=3)
    Label(root,text='Age').grid(row=9, column=4)
    Label(root,text='Team').grid(row=9, column=5)
    Label(root,text='Type').grid(row=9, column=6)
    for i in range((len(playerList))):
        for j in range((len(playerList[i]))):
            Label(root,text=playerList[i][j]).grid(row=10+i, column=j+2)
        Button(root, text=f"Delete" , padx=20,pady=5, fg="black",bg="white" , command=partial(deletePlayer, playerList[i][0])).grid(row=10+i , column=8)
        Button(root, text=" Edit" , padx=20,pady=5, fg="black",bg="white" , command=partial(editPlayer, playerList[i][0])).grid(row=10+i , column=10)

def editPlayer(id):
    mycursor.execute(f'SELECT * FROM players WHERE id={id}')
    player = mycursor.fetchone()
    Namevalue.set(player[1])
    Agevalue.set(player[2])
    Team_namevalue.set(player[3])
    Typevalue.set(player[4])
    global updateID
    updateID = id

def refresh():
    for widget in root.winfo_children():
        widget.destroy()
    Label(root,text="PLAYERS", font="comicsanms 13 bold",pady=15).grid(row=0,column=3)
    
    Name = Label(root,text="Name :").grid(row=2,column=2)
    Age = Label(root,text="Age :").grid(row=3,column=2)
    Team_name = Label(root,text="Team_name :").grid(row=4,column=2)
    Type = Label(root,text="Type :").grid(row=5,column=2)
    
    Nameentry =Entry(root,textvariable=Namevalue).grid(row=2,column=3)
    Ageentry =Entry(root,textvariable=Agevalue).grid(row=3,column=3)
    Team_nameentry =Entry(root,textvariable=Team_namevalue).grid(row=4,column=3)
    Typeentry =Entry(root,textvariable=Typevalue).grid(row=5,column=3)
    mybutton1 = Button(root, text="Submit" , padx=20,pady=5, fg="black",bg="white" , command= addPlayer).grid(row=7 , column=3)
    mybutton2 = Button(root, text="Update" , padx=20,pady=5, fg="black",bg="white" , command= updatePlayer).grid(row=7 , column=4)
    mybutton3 = Button(root, text="back" , padx=20,pady=5, fg="black",bg="white" , command= CallBack).grid(row=0, column=0)


def deletePlayer(id):
    mycursor.execute(f'delete from players where id={id}')
    mydb.commit()
    refresh()
    getplayer()

def updatePlayer():
    mycursor.execute("update players set name=%s, age=%s, team=%s, type=%s WHERE id=%s",(Namevalue.get(),Agevalue.get(),Team_namevalue.get(),Typevalue.get(), updateID))
    Namevalue.set('')
    Agevalue.set('')
    Team_namevalue.set('')
    Typevalue.set('')
    mydb.commit()
    getplayer()

def addPlayer():
    mycursor.execute("insert into players(name, age, team, type) values (%s,%s,%s,%s)",(Namevalue.get(),Agevalue.get(),Team_namevalue.get(),Typevalue.get()))
    Namevalue.set('')
    Agevalue.set('')
    Team_namevalue.set('')
    Typevalue.set('')
    mydb.commit()
    getplayer()


mybutton1 = Button(root, text="Submit" , padx=20,pady=5, fg="black",bg="white" , command= addPlayer).grid(row=7 , column=3)
mybutton2 = Button(root, text="Update" , padx=20,pady=5, fg="black",bg="white" , command= updatePlayer).grid(row=7 , column=4)

def CallBack():
    filename = 'index.py'
    os.system(filename)
    os.system('notepad'+filename)
mybutton3 = Button(root, text="back" , padx=20,pady=5, fg="black",bg="white" , command= CallBack).grid(row=0, column=0)

getplayer()
root.mainloop()
