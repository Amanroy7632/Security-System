from tkinter import *
import random
from tkinter import messagebox as tmsg
import Security
# import Library_project
# import mysql.connector
class Login(Tk):
    def __init__(self):
          def padder(): 
            pass
          super().__init__()
          
          # self=root
          self.geometry("1920x1080")
          self.title("Login")
          self.photox=PhotoImage(file="C:\\Users\\yadav\\Documents\\project\\library_login.png")
          Label(image=self.photox).pack()
          self.photo_icon=PhotoImage(file="C:\\Users\\yadav\\Documents\\project\\group.png")
          self.iconphoto(True,self.photo_icon)
          self.UserId=StringVar(self)
          self.Password=StringVar(self)
          # =============frame for userid or password=============

          self.login_frame=Frame(self,borderwidth=7,relief=SUNKEN,padx=281,bg="grey5").place(x=430,y=300,width=600,height=300)
          button=Button(self.login_frame,command=lambda:self.destroy(),text="🔙 Exit",font=("times new roman",12,"bold"),bg="grey5",fg="white smoke").place(x=430,y=300,width=100)
          user_id=Label(self.login_frame,text="Enter user ID:",background="grey5",fg="white smoke",font=("ariel",14,"bold"),pady=20).place(x=540,y=308,width=380)
          user_id_entry=Entry(self.login_frame,width=25,font=("ariel",12,"bold"),textvariable=self.UserId).place(x=490,y=360,width=500)
          user_password=Label(self.login_frame,text="Password:",background="grey5",fg="white smoke",pady=10,font=("ariel",14,"bold")).place(x=440,y=400,width=580)
          entery1=Entry(self.login_frame,show="*",width=25,textvariable=self.Password,font=("ariel",12,"bold"))
          entery1.place(x=490,y=445,width=500)

          # ==================Checking of Button=================

          def check_button(*args):
            if (len(self.Password.get())>6) and (len(self.UserId.get())>0):
              submit_button.config(state=NORMAL)
            else:
              submit_button.config(state=DISABLED)
          self.UserId.trace('w',check_button)
          self.Password.trace('w',check_button)
          def forgrt_password():
            self.withdraw()
            self.forgot_window=Toplevel(self)
            self.forgot_window.geometry("500x500+430+150")
            self.title("Forgot Password")
            self.f1=Frame(self.forgot_window,borderwidth=7,relief=SUNKEN,bg="#262626").place(x=0,y=0,width=500,height=500)
            def back():
              self.forgot_window.destroy()
              self.deiconify()
            Label(self.forgot_window,text="Enter Email Id:",fg="white",bg="#262626",font=("times new roman",18,"bold")).place(x=150,y=12,width=200,height=50)
            self.email_entry=StringVar()
            Button(self.forgot_window,text="🔙 Back",command=back,fg="white",bg="#204634").place(x=0,y=0,width=100)
            Entry(self.forgot_window,textvariable=self.email_entry,font=("times new roman",16,"bold")).place(x=100,y=65,width=300,height=40)
            Label(self.forgot_window,text="Phone No:",fg="white",bg="#262626",font=("times new roman",18,"bold")).place(x=150,y=105,width=200,height=50)
            self.phone_entry=StringVar()
            self.otp_entry=StringVar()
            self.new_password=StringVar()
            Entry(self.forgot_window,textvariable=self.phone_entry,font=("times new roman",16,"bold")).place(x=100,y=165,width=300,height=40)
            self.otp=0
            # ===========================For Otp Sending =========================================
            def send_otp():
              if not (self.email_entry.get() and self.phone_entry.get()):
                  tmsg.showerror("Error","Please enter proper data")
              elif not '@' in self.email_entry.get():
                  tmsg.showerror("Error","Invalid email id")
              elif not (self.phone_entry.get().isnumeric() and len(self.phone_entry.get())==10):
                  tmsg.showerror("Error","Please enter proper Phone number")
              else:
                   otp=123
                   conn=mysql.connector.connect(host="localhost",password="aman7632@$",username="root",database="library")
                   my_cursor2=conn.cursor()
                   my_cursor2.execute("select * from Admin_staff where Email=%s and Phone=%s",(self.email_entry.get(),self.phone_entry.get()))
                   row2=my_cursor2.fetchone()
                   conn.commit()
                   conn.close()
                   if row2:
                      self.otp=random.randint(1000, 9999)
                      tmsg.showinfo("OTP",f"Your OTP is {self.otp}")
                      Label(self.forgot_window,text="New Password:",fg="white",bg="#262626",font=("times new roman",18,"bold")).place(x=150,y=245,width=200,height=30)
                      Entry(self.forgot_window,textvariable=self.new_password,font=("times new roman",16,"bold")).place(x=100,y=280,width=300,height=30)
                   else:
                      tmsg.showerror("Error","No User record found")
                   def info():
                      if self.otp_entry.get()==str(self.otp):
                        if len(self.new_password.get())>6: 
                         conn=mysql.connector.connect(host="localhost",password="aman7632@$",username="root",database="library")
                         my_cursor3=conn.cursor()
                         my_cursor3.execute("update Admin_staff set password=%s where Email=%s",(self.new_password.get(),self.email_entry.get()))
                         conn.commit()
                         conn.close()
                         tmsg.showinfo("Success","Your Password changed Successfully")
                         self.forgot_window.destroy()
                         self.deiconify()
                        else:
                          tmsg.showerror("Error","Password must be greater than 6-digit")
                      else:
                        tmsg.showerror("Error","Wrong OTP")
                   def check_button(*args):
                    if (len(self.new_password.get())>6):
                       b1.config(state=NORMAL)
                    else:
                      b1.config(state=DISABLED)
                   self.new_password.trace('w',check_button)

                   b1=Button(self.forgot_window,text="Submit",command=info,state=DISABLED,bg="blue",fg="white",font=("times new roman",16,"bold"))
                   b1.place(x=100,y=315,width=300,height=40)
            Button(self.forgot_window,text="Send OTP:",command=send_otp,fg="white",bg="blue",font=("times new roman",16,"bold")).place(x=80,y=210,width=200,height=30)
            Entry(self.forgot_window,textvariable=self.otp_entry,font=("times new roman",16,"bold")).place(x=300,y=210,width=100,height=30)
          def lib():
            if self.UserId.get()=="Aman" and self.Password.get()=="aman7632":
              # self.withdraw()
              obj=Security.HouseGUI()
              obj.mainloop()

            # conn=mysql.connector.connect(host="localhost",password="aman7632@$",user="root",database="library")
            # my_cursor4=conn.cursor()
            # my_cursor4.execute("select Name,Email,password from Admin_staff where Email=%s and password=%s",(self.UserId.get(),self.Password.get()))
            # row=my_cursor4.fetchone()
            # if row:
            #   tmsg.showinfo("Success",f"Welcome 😊\n{row[0]}")
            #   self.destroy()
            #   y=Library_project.Library()
            #   y.data_1st_frame()
            #   y.data_3rd_frame()
            #   y.Menu_bar()
            #   y.Welcome_notification()
            # else:
            #   tmsg.showerror("Error","Please enter proper Id or password")
            #   Button(self.login_frame,text="Forget Password",command=forgrt_password,padx=20,pady=5,bg="grey5",fg="white smoke",font=("times new roman",12,"bold")).place(x=780,y=500)
          # ==================Hiding of Password==================  
          def Hide_password():
           if entery1.cget('show')=='*':
            entery1.config(show='')
           else:
            entery1.config(show='*') 
          #======================================================= 
          check=Checkbutton(self.login_frame,bg="grey5",fg="blue",text="Show Password",font=("times new roman",12,"bold"),pady=5,command=Hide_password)
          check.place(x=850,y=470)
          submit_button=Button(self.login_frame,text="Submit",bg="blue",state=DISABLED,fg="white",padx=20,pady=5,font=("times new roman",12,"bold"),command=lib)
          submit_button.place(x=680,y=500)
          def register_id(self):
            self.withdraw()
            self.register_window=Toplevel(self)
            self.register_window.geometry("600x600+430+150")
            self.register_window.resizable(False,False)
            self.register_window.title("🏡Create Account")
            self.register_window.config(bg="springgreen")
            Label(self.register_window,text="Enter your details:",font=("times new roman",18,"bold"),padx=10,pady=10,bg="black",fg="white").place(x=0,y=0,width=600,height=50)
            Label(self.register_window,text="Full Name:",font=("times new roman",14,"bold"),bg="black",fg="white").place(x=0,y=50,width=100,height=50)
            self.name=StringVar()
            self.email=StringVar()
            self.phone=StringVar()
            self.user_password=StringVar()
            def check_data():
              temp_data=(self.name.get(),self.phone.get(),self.email.get())
              conn=mysql.connector.connect(host="localhost",password="aman7632@$",username="root",database="library")
              my_cursor1=conn.cursor()
              my_cursor1.execute("select * from Admin_staff where Name=%s and Phone=%s and Email=%s",temp_data)
              rows=my_cursor1.fetchone()
              conn.commit()
              conn.close()
              return rows
            def check_for_Email():
              conn=mysql.connector.connect(host="localhost",password="aman7632@$",username="root",database="library")
              my_cursor1=conn.cursor()
              my_cursor1.execute("select * from Admin_staff where Email=%s",(self.email.get(),))
              rows=my_cursor1.fetchone()
              conn.commit()
              conn.close()
              return rows
            def check_for_phone():
              conn=mysql.connector.connect(host="localhost",password="aman7632@$",username="root",database="library")
              my_cursor1=conn.cursor()
              my_cursor1.execute("select * from Admin_staff where Phone=%s",(self.phone.get(),))
              rows=my_cursor1.fetchone()
              conn.commit()
              conn.close()
              return rows
            def add_account():
               if not (self.name.get() and self.email.get() and self.phone.get() and self.user_password.get()):
                tmsg.showerror("Error","Fill Proper data")
               elif not(self.name.get().isalpha()):
                tmsg.showerror("Error","Name must be Alphabetical")
               elif not '@' in (self.email.get()):
                tmsg.showerror("Error","invalid email id")
               elif not (self.phone.get().isnumeric()) and (len(self.phone.get())==10):
                tmsg.showerror("Error","Invalid phone number")
               elif not len(self.user_password.get())>6:
                tmsg.showerror("Error","Password must be greater than 6-digits")
               elif check_data():
                   tmsg.showerror( "Error","Account already exists")
               elif check_for_phone():
                tmsg.showerror( "Error","Phone number already connected with account")
               elif check_for_Email():
                tmsg.showerror( "Error","Email already connected with account")
               else:
                 conn=mysql.connector.connect(host="localhost",password="aman7632@$",username="root",database="library")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into Admin_staff values(%s,%s,%s,%s)",(self.name.get(),self.phone.get(),self.email.get(),self.user_password.get()))
                 conn.commit()
                 conn.close()
                 tmsg.showinfo("Thank you","Account created successfully")
                 self.register_window.destroy()
                 self.deiconify()
            def back():
              self.register_window.destroy()
              self.deiconify()
            name_entry=Entry(self.register_window,textvariable=self.name,font=("times new roman",12,"bold")).place(x=101,y=60,width=250,height=30)
            Label(self.register_window,text="Email📧:",font=("times new roman",14,"bold"),bg="black",fg="white").place(x=0,y=100,width=100,height=50)
            email_entry=Entry(self.register_window,textvariable=self.email,font=("times new roman",12,"bold")).place(x=101,y=110,width=250,height=30)
            Label(self.register_window,text="Phone no📲:",font=("times new roman",14,"bold"),bg="black",fg="white").place(x=0,y=150,width=100,height=50)
            phone_entry=Entry(self.register_window,textvariable=self.phone,font=("times new roman",12,"bold")).place(x=101,y=160,width=250,height=30)
            Label(self.register_window,text="Password:",font=("times new roman",14,"bold"),bg="black",fg="white").place(x=0,y=200,width=100,height=50)
            phone_entry=Entry(self.register_window,textvariable=self.user_password,font=("times new roman",12,"bold")).place(x=101,y=210,width=250,height=30)
            Button(self.register_window,text="Submit",command=add_account,font=("times new roman",12,"bold"),bg="blue",fg="white").place(x=0,y=250,width=100,height=30)
            Label(self.register_window,text="Already having an Account ,for login:",font=("times new roman",12,"bold"),bg="black",fg="white").place(x=0,y=300,width=250,height=30) 
            Button(self.register_window,text="Click Here",font=("times new roman",12,"bold"),command=back,bg="light yellow").place(x=250,y=300,width=100,height=30) 
          # reg_button=Button(self.login_frame,bg="grey5",fg="white smoke",command=lambda:register_id(self),text="Create Account",font=("times new roman",12,"bold"))
          # reg_button.place(x=430,y=565)
    def back():
      x=Login()
      x.mainloop() 
if __name__ =='__main__':
 x=Login()
 x.mainloop()

