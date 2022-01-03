
import mysql.connector
import datetime
import re
 
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import tkinter
from tkinter import *
import string
import random
import pyperclip

try :
    mydb = mysql.connector.connect(
    host="bytqsqoh5rsdu8rmkjb4-mysql.services.clever-cloud.com",
    user="unvemyeiilliuqzt",
    database="bytqsqoh5rsdu8rmkjb4", 
    passwd="FWLmxwvQQavzqXNN6nEt"
    )
except:
        messagebox.showinfo("Connection failure... ","Please check your internet connection")
        

mycursor = mydb.cursor()

window=tkinter.Tk()
window.title("PASSWORD MANAGER APP")
img = PhotoImage(file="lock2.png")
label = Label(
    window,
    image=img
)
label.place(x=0,y=0)
tp=tkinter.Frame(window).pack(side="top")
bt=tkinter.Frame(window).pack(side="bottom")


def password_generator():
    label_title = Label(text="* PASSWORD GENERATOR BY PASSWORD MANAGER APP *",
                    bg="#383e56",
                    fg="#c5d7bd",
                    font=("Arial", 13, "bold"))
    label_title.place(x=1000,y=50)

 
    char_input = Entry(bg="#fb743e")
    char_input.place(x=1000, y=100)
    char_input.insert(0, "12")
    char_input.focus()

    generate_password_button = Button(text="Generate Password & Copy to Clipboard",
                                  bg="#fb743e",
                                  height=2,
                                  width=38,
                                  command=password_generator)
    generate_password_button.place(x=1000, y=150)

    password_field = Entry(bg="#383e56",
                       font=("Arial", 15, "bold"), width=25)
    password_field.place(x=1000, y=200)
    global password_chars
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password_field.delete(0, END)
    length = int(char_input.get())
    password = "".join([random.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)
    pyperclip.copy(password)
    



def addpass():
            ld=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your user id of PASSWORD MANAGER APP agin to verify that is you")
            mycursor.execute("SELECT * FROM userlogin where userid=%s " ,(ld,) )
            da=mycursor.fetchall()
            if da and ld :
                appname=simpledialog.askstring(title="PASSWORD MANAGER APP",prompt="Enter the application name")
                appid=simpledialog.askstring(title="insert userid " ,prompt="Enter the application user id")
                apppsd=simpledialog.askstring(title="Add new apps password", prompt="Enter the application user password")
                current_time = datetime.datetime.now() 
                sql="INSERT INTO alluserappinfo(appname,apploginid,apppswd,doj,ID) values (%s,%s,%s,%s,%s)"
                val1=(appname,appid,apppsd,current_time,ld,) 
                mycursor.execute(sql,val1)
                mydb.commit()
                messagebox.showinfo("PASSWORD MANAGER APP","password entered succesfully");
            else:
                 messagebox.showinfo("PASSWORD MANAGER APP","incoorect userid");
         

def delpass():
     ld=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your user id of PASSWORD MANAGER APP agin to verify that is you")
     mycursor.execute("SELECT * FROM userlogin where userid=%s " ,(ld,) )
     da=mycursor.fetchall()
     if da and ld :
         Appname=simpledialog.askstring(title="Passcode saver app",prompt="Enter the application name")
         mycursor.execute("select * from alluserappinfo where appname=%s and ID=%s ",(Appname,ld,))
         ki=mycursor.fetchall()
         if ki and Appname:
            sql="DELETE FROM `alluserappinfo` WHERE appname=%s and ID=%s"
            val3=(Appname,ld)
            mycursor.execute(sql,val3)
            mydb.commit()
            messagebox.showinfo("Passcode saver app","Application password delete sucessfully");
         else :
            messagebox.showinfo("Passcode saver app","Invalid application");
     else:
         messagebox.showinfo("Passcode saver app","incoorect userid or application");
        
def showpass():
      
      apname=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your application name")
      mycursor.execute("SELECT * FROM alluserappinfo where appname=%s AND ID=%s " ,(apname,ld,))
      data=mycursor.fetchall()
      if data and apname: 
          for row in data:
               apnav=row[0]
               apid=row[1]
               ss=row[2]
               qq=row[3]
               
               messagebox.showinfo(qq,"your password is "+ss)        
      else:
         messagebox.showinfo("PASSWORD MANAGER APP"," No such app found ")
         
def changepass():
    appname=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter the application name")
    mycursor.execute("SELECT * FROM alluserappinfo where appname=%s AND ID=%s " ,(appname,ld,))
    data2=mycursor.fetchall()
    if data2 and appname:
       newpas=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter new password of this application")
       sql = "UPDATE alluserappinfo SET apppswd =%s WHERE appname =%s"
       val3=(newpas,appname)
       mycursor.execute(sql,val3)
       mydb.commit()
       messagebox.showinfo("PASSWORD MANAGER APP","Password reset sucessfully")
    else:
         messagebox.showinfo("PASSWORD MANAGER APP","App doesnt exists in ")
         


def checkpass():
    appname=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter the application name")
    mycursor.execute("SELECT apppswd FROM alluserappinfo where appname=%s AND ID=%s " ,(appname,ld,))
    data2=mycursor.fetchone()
    if data2 and appname:
       if len(data2) > 12:
          messagebox.showinfo("STRONG PASSWORD"," Crack time : 2-3 months")
       elif len(data2) <= 12 and len(data2) >=8:
          messagebox.showinfo("Good PASSWORD"," Crack time : 5-6 Week")
       elif len(data2) <8:
          messagebox.showwarning("WEEK PASSWORD ", "Crack Time : 1-2 hours [Suggesion :Change your password with the length of > 12 Characters]")
    else:
        messagebox.showerror("No such app found", "Please enter the correct application name")
    
def abinfo():
    message ='''
                     **About Us**
    _____________________________________________________
    Dear User,
    We’re client focused application designers
    Our master group of application designers utilize more
    intelligent and friendlier user interface and
    Protected Data-base for our customers to Manage
    their Password with an Authenticate way and making
    remarkable client.Working inside test-driven
    conditions implies . we can guarantee well-performing
    all through improvement and stable forms.
    Thanks & Regards,
    Devloper and Designer Team of
    PASSWORD MANAGER APP '''
    text_box = Text(
    window,
    height=17,
    width=58
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(background="grey",foreground="white",state='disabled')

def needhelp():
    message ='''
                              HELP
______________________________________________________________
    *) How Register on this app,
    step1 : Click on the Register button
    step2 : Enter Your Emailid
    step3 : Create your userid
    step3 : Create your password
    [password policy: password length must be 8
    and must contain one digit , special character,
    uppercase letter,]
    step4 : Enter your Mobile number
    After the Sucessfull Registration you will be able to use this application

    *) How to login
    A very simple :Enter your Login id and Password
    If you forgot your password then you can Reset it.

    
    Thanks & Regards,
    Team Save Your Password APP '''
    text_box = Text(
    window,
    height=20,
    width=62
    )
    text_box.place(x=19,y=290)
    text_box.insert('end', message)
    text_box.config(background="purple",foreground="white",state='disabled')

             
def delac():
    ld=simpledialog.askstring(title=" 🔒🔒 Passcode saver app 🔑🔑 ",prompt="Enter your user id of passcode saver app")
    psd=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your password of passcode saver app")
    mycursor.execute("SELECT * FROM userlogin where userid=%s AND passcode=%s " ,(ld,psd,) )
    da=mycursor.fetchall()
    if da and psd :
       mycursor.execute('DELETE  FROM  userlogin WHERE userid=%s and passcode=%s',(ld,psd,))
       mycursor.execute('DELETE  FROM  newaccount WHERE userid=%s and password=%s',(ld,psd,))
       mycursor.execute('DELETE  FROM  alluserappinfo WHERE ID=%s',(ld,))
       mydb.commit()
       messagebox.showinfo("Thank You for using this APP","You are account deleted sucessfully")
    else:
        messagebox.showerror("Invalid Userid id", "No such Userid Found ")
       

def history():
    ld=simpledialog.askstring(title=" 🔒🔒 Passcode saver app 🔑🔑 ",prompt="Enter your user id of passcode saver app")
    mycursor.execute("SELECT * FROM userlogin where userid=%s " ,(ld,) )
    dat=mycursor.fetchall()
    if dat and ld:
       apnav=simpledialog.askstring(title="Password Manager APP",prompt="Enter Application name")
       mycursor.execute("SELECT * from alluserappinfo where appname=%s",(apnav,))
       dat2=mycursor.fetchall()
       if dat2 and apnav:
           mycursor.execute("SELECT doj from alluserappinfo where appname=%s",(apnav,))
           info=mycursor.fetchall()
           messagebox.showinfo("Last changed",info)
       else:
           messagebox.showerror("Invalid app app","No such app found")
    else:
        messagebox.showerror("Invalid user name","Please enter the correct user name")
    

class login:
   
     img = PhotoImage(file="idpass.png")
     label = Label(
            window,
            image=img
             )
     label.place(x=0,y=0)
  
              
     def logininto(self):
        
        global ld
        
        ld=simpledialog.askstring(title=" 🔒🔒 Passcode saver app 🔑🔑 ",prompt="Enter your user id of passcode saver app")
        psd=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your password of passcode saver app")
        mycursor.execute("SELECT * FROM userlogin where userid=%s AND passcode=%s " ,(ld,psd,) )
        da=mycursor.fetchall()
        if da and psd :
           master = Tk()
           master.geometry("500x500")
           newWindow = Toplevel(master)
           newWindow.title("New Window (Profile)")
           newWindow.geometry("1000x1000")
   
           
           messagebox.showinfo("Profile 👥",  ld) 
           messagebox.showwarning("PASSWORD MANAGER APP", "your Profile is opened in the next window ")
           
           
           txt3 = "Profile 👤 : {}".format(ld)
            
           profile=tk.Button(newWindow,text=txt3,fg='purple',activebackground='green',width=70, height=5).place(x=0,y=0)
           btn1=tkinter.Button(newWindow,text="Add Password +",fg="red",bg='white',activebackground='green',width=20, height=3,command=addpass).place(x=655,y=100)
           btn2=tkinter.Button(newWindow,text="FIND PASSWORD ",fg="white",bg='blue',activebackground='blue',width=20, height=3,command=showpass).place(x=655,y=200)
           btn3=tkinter.Button(newWindow,text="CHANGE PASSWORD ",fg="red",bg='yellow',activebackground='red',width=20, height=3,command=changepass).place(x=655,y=300)
           btn4=tkinter.Button(newWindow,text="Check the scurity of your password ✔️",fg="red",bg='white',activebackground='red',width=30, height=3 , command=checkpass).place(x=655,y=400)
           tbn6=tkinter.Button(newWindow,text="DELETE PASSWORD -",fg="white",bg='red',activebackground='red',width=30, height=3 , command=delpass).place(x=655,y=500)        
           btn7=tkinter.Button(newWindow,text="CHECK PASSWORD HISTORY",fg="black",bg='pink',activebackground='purple',width=23, height=3,command=history).place(x=655,y=600)
           btn8=tkinter.Button(newWindow,text="EXIT ",fg="black",bg='#54FA9B',activebackground='purple',width=10, height=3,command=exit).place(x=655,y=700)
           
           
        else:
           messagebox.showwarning("please enter a correct userid and password") 
           pointer=simpledialog.askinteger(title="PASSWORD MANAGER APP", prompt="if you Forgot the Password then press 1 to reset it")
           if(pointer==1):
                      fg=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="enter your userid")
                      mycursor.execute("SELECT * FROM userlogin where userid=%s  " ,(fg,) )
                      dada=mycursor.fetchall()
                
                      if dada and fg:
                          messagebox.showinfo("Enter your new password","[password policy: password length must be  8 and mustcontain   one digit , special character,uppercase letter,]")
                          pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
                          passwordnew=simpledialog.askstring(title="SAVE MY PASSWORD APP ",prompt="Enter your password ")
                          if(re.search(pattern,passwordnew)):
                               passcode=passwordnew
                               sql = "UPDATE userlogin SET passcode =%s WHERE userid=%s"
                               newdat=(passcode,fg)
                               mycursor.execute(sql,newdat)
                               mydb.commit();
                               
                               messagebox.showinfo("PASSWORD MANAGER APP","!!! Password reset sucessfully !!!")
                          else:
                             
                             messagebox.showinfo("PASSWORD MANAGER APP","Invalid password!! please follow the password policy")
                       
                                                       
                     
                     
                     
                      else:
                        messagebox.showinfo("PASSWORD MANAGER APP","sorry please enter the correct user id  ")
                         
           else:
            messagebox.showinfo("PASSWORD MANAGER APP","Please enter the 1 ")
               
      
                
        
               



def createaccount():
          
          email=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your email id")
          regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
          if(re.search(regex,email)):
              emailid=email
          else:
              messagebox.showinfo("PASSWORD MANAGER APP","Invalid Email please provide the correct email")
              exit()
          UserId=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Create Your userid")
          mycursor.execute("SELECT * FROM userlogin where userid=%s " ,(UserId,))
          if mycursor.fetchall():
              messagebox.showinfo("PASSWORD MANAGER APP","user id allready exits")
          else:    
             pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
             messagebox.showinfo("Enter your password ","[password policy: password length must be  8 and mustcontain   one digit , special character,uppercase letter,]")
             password=simpledialog.askstring(title="SAVE MY PASSWORD APP", prompt="Create a strong password")
          
             if(re.search(pattern,password)):
               passcode=password
             else:
               messagebox.showinfo("PASSWORD MANAGER APP","Invalid password!! please follow the password policy")
               exit()
             mobile=simpledialog.askstring(title="PASSWORD MANAGER APP", prompt="Enter your mobile number") 
             sql="INSERT INTO newaccount (emailid,userid,password,phno) VALUES (%s,%s,%s,%s)"
             val=(emailid,UserId,passcode,mobile)
             mycursor.execute(sql,val)
             mycursor.execute("INSERT INTO userlogin(userid,passcode) VALUES(%s,%s) ",(UserId,passcode,))
             mydb.commit()
             messagebox.showinfo("Congratulation"+UserId,"You are sucessfully register at passcode manager")


 
u=login()



    
root= tk.Tk()
root.withdraw()
click_btn= PhotoImage(file='login1.png')
img_label= Label(image=click_btn)
register_btn=PhotoImage(file='register1.png')
reg_label=Label(image=register_btn)
exit_img=PhotoImage(file='exit1.png')
ex_label=Label(image=exit_img)
aboutus=tk.Button(text='About us',fg='red', width=7, height=2, command=abinfo).place(x=0,y=0)
Needhelp=tk.Button(text='Help',fg='red', width=7, height=2, command=needhelp).place(x=0,y=80)

btn5=tkinter.Button(text="Suggest a Strong Password ",fg="Purple",bg='#54FA9B',activebackground='orange',width=20, height=3,command=password_generator).place(x=455,y=100)
#login =tkinter.Button(tp,text="login 👥",fg="green",command=u.logininto).pack()
login=tk.Button( text='Log in', width=200, height=50, fg="blue" ,image=click_btn,borderwidth=0,command=u.logininto).pack()
#register=tkinter.Button(bt,text="sign out📴",fg="grey",command=createaccount).pack()
register=tk.Button( text='singn out',width=200, height=50, fg="green",image=register_btn,borderwidth=0,command=createaccount).place(x=665,y=100)

out=tk.Button(text="Exit" ,fg="black",width=200, height=50, image=exit_img, borderwidth=0, bg="red",command=root.destroy).place(x=665,y=200)
btn9=tkinter.Button(text="DELETE MY ACCOUNT ",fg="black",bg='white',activebackground='purple',width=20, height=3,command=delac).place(x=20,y=710)                  
root.mainloop()


 

      
      
         




#mycursor.execute("CREATE TABLE userlogin(userid VARCHAR(255), passcode VARCHAR(255))")
#data=mycursor.execute("SELECT * FROM `userlogin`")

#insert records 
#sql="INSERT INTO userlogin (userid,passcode) VALUES (%s,%s)"
#userid=str(input("Enter your name"))
#passcode=str(input("enter your passcode"))        
#val=(userid,passcode)
#mycursor.execute(sql,val)
#mydb.commit()

#Egt paascode
     
