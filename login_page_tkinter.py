from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root= Tk()
root.title("My App")        # Name of the APP
root.geometry("1100x650")   # Window Size
root.configure(bg="white")  # Window Configuration
root.resizable(False,False) # Ability to change window size (x axis, y axis)
   
   
    ## Main Page ##
imag = Image.open("Bora Bora.jpg") # BG IMAGE
img = ImageTk.PhotoImage(imag)

Label(root,border=0,image= img, bg="black").place(x=0,y=0)  # APPLY BG IMAGE
frame = Frame(root,width=400,height=550,bg="white")         # SIGN IN WINDOW
frame.place(x= 625, y=50)                                   # SIGN IN WINDOW PLACE


heading = Label(frame,text="Sign In", fg ="#2f5eb8",bg= "white",font=("Microsoft Corbel",30)) # SIGN IN TITLE
heading.place(x=135,y=50) # SIGN IN TITLE PLACE

def Main():
        ## Main Page ##
    imag = Image.open("Bora Bora.jpg") # BG IMAGE
    img = ImageTk.PhotoImage(imag)

    Label(root,border=0,image= img, bg="black").place(x=0,y=0) # APPLY BG IMAGE
    frame = Frame(root,width=400,height=550,bg="white")        # SIGN IN WINDOW
    frame.place(x= 625, y=50)                                  # SIGN IN WINDOW PLACE


    heading = Label(frame,text="Sign In", fg ="#2f5eb8",bg= "white",font=("Microsoft Corbel",30)) # SIGN IN TITLE
    heading.place(x=135,y=50) # SIGN IN TITLE PLACE

        # username
    def on_enter(i): # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
        name = user.get()
        if name == "Username":
            user.delete(0,"end")
    def on_leave(i):
        name= user.get()
        if name== "":
            user.insert(2,"Username")
                
                
    user = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18)) # USERNAME ENTRY BLOCK
    user.place(x=40,y=150)           # PLACE OF THE USERNAME ENTRY BLOCK
    user.insert(2,"Username")        # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    user.bind("<FocusIn>",on_enter)  # GO 27
    user.bind("<FocusOut>",on_leave) # GO 27

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=178) # FEATURES OF THE ENTRY BLOCK AND PLACE
        #----------------------


        # password
    def on_enter(i):    # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "PASSWORD" WILL DISAPPEAR
        word = password.get()
        if word == "Password":
            password.delete(0,"end")
    def on_leave(i):
        word= password.get()
        if word== "":
            password.insert(2,"Password")
                
    password = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18)) # PASSWORD ENTRY BLOCK
    password.place(x=40,y=200)           # PLACE OF THE PASSWORD ENTRY BLOCK
    password.insert(2,"Password")        # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    password.bind("<FocusIn>",on_enter)  # GO 48
    password.bind("<FocusOut>",on_leave) # GO 48

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=228) # FEATURES OF THE ENTRY BLOCK AND PLACE

    # Main Page Buttons
    Button(frame,width=23,text= "Sign In",bg = "#2f5eb8",fg = "white",border=0, font=("Microsoft Corbel",18),command=signin).place(x=38, y=275)           # FEATURES OF THE SIGN IN BUTTON
    Label(frame,text="Don't have an account?",bg="white",fg="black",border=0,font=("Microsoft Corbel",11)).place(x=125,y=325)                             # DON'T HAVE ACCOUNT TEXT
    Button(frame,width=23,text= "Sign Up",bg = "#ff5a6c",fg = "white",border=0, font=("Microsoft Corbel",18),command=signup).place(x=38, y=350)           # FEATURES OF THE SIGN UP BUTTON
    root.mainloop()

    #----------------------

    # username
def on_enter(i): # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
    name = user.get()
    if name == "Username":
        user.delete(0,"end")
def on_leave(i):
    name= user.get()
    if name== "":
        user.insert(2,"Username")
            
            
user = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18)) # USERNAME ENTRY BLOCK
user.place(x=40,y=150)           # PLACE OF THE USERNAME ENTRY BLOCK
user.insert(2,"Username")        # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
user.bind("<FocusIn>",on_enter)  # GO 27
user.bind("<FocusOut>",on_leave) # GO 27

Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=178) # FEATURES OF THE ENTRY BLOCK AND PLACE
    #----------------------


    # password
def on_enter(i):    # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "PASSWORD" WILL DISAPPEAR
    word = password.get()
    if word == "Password":
        password.delete(0,"end")
def on_leave(i):
    word= password.get()
    if word== "":
        password.insert(2,"Password")
            
password = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18)) # PASSWORD ENTRY BLOCK
password.place(x=40,y=200)           # PLACE OF THE PASSWORD ENTRY BLOCK
password.insert(2,"Password")        # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
password.bind("<FocusIn>",on_enter)  # GO 48
password.bind("<FocusOut>",on_leave) # GO 48

Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=228) # FEATURES OF THE ENTRY BLOCK AND PLACE
    #----------------------


### When You Press Sign In Button ###
def signin():
    username = user.get()     # READ USERNAME
    passkey = password.get()  # READ PASSWORD

    # If you enter correct ADMIN information
    if username == "admin" and passkey == "1234": 

        Label(root,image=img, border=0).place(x=0,y=0) # BG IMAGE
        Label(root,text="Hello Admin!!!",fg="black",font=("Microsoft Corbel",30)).place(x=450,y=275) # WELCOME MESSAGE AND PLACE
        Button(root,width=18,text= "Back",bg ="#ff5a6c",fg = "white",border=0, font=("Microsoft Corbel",18),command=Main).place(x=450, y=428) # BACK BUTTON AND PLACE
        root.mainloop()
    # If you do not enter correct account information
    else:
        messagebox.showerror("Oops","Invalid Username or Password!!") # ERROR MESSAGE FOR INVALID USERNAME OR PASSWORD

### When You Press Sign Up Button ###
def signup():
    Label(root,border=0,image= img, bg="black").place(x=0,y=0) # BG IMAGE

    frame = Frame(root,width=400,height=550,bg="white") # SIGN UP WINDOW
    frame.place(x= 625, y=50) # SIGN UP WINDOW PLACE

    heading1 = Label(frame,text="Sign Up", fg ="#2f5eb8",bg= "white",font=("Microsoft Corbel",30)) # SIGN UP TITLE
    heading1.place(x=135,y=50) # SIGN UP TITLE PLACE

  
    # Username  
    def on_enter(i):                 # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
        name1 = user1.get()
        if name1 == "Username":
            user1.delete(0,"end")
    def on_leave(i):
        name1= user1.get()
        if name1== "":
            user1.insert(2,"Username")
    

    user1 = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18)) # USERNAME ENTRY BLOCK
    user1.place(x=40,y=150)           # PLACE OF THE USERNAME ENTRY BLOCK
    user1.insert(2,"Username")        # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    user1.bind("<FocusIn>",on_enter)  # GO 152
    user1.bind("<FocusOut>",on_leave) # GO 152

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=178) # FEATURES OF THE ENTRY BLOCK AND PLACE

    # e-mail   
    def on_enter(i):        # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
        email = mail.get()
        if email == "e-mail":
            mail.delete(0,"end")
    def on_leave(i):
        email= mail.get()
        if email== "":
            mail.insert(2,"e-mail")


    mail = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18))    # MAIL ENTRY BLOCK
    mail.place(x=40,y=200)           # PLACE OF THE MAIL ENTRY BLOCK
    mail.insert(2,"e-mail")          # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    mail.bind("<FocusIn>",on_enter)  # GO 171
    mail.bind("<FocusOut>",on_leave) # GO 171

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=228) # FEATURES OF THE ENTRY BLOCK AND PLACE

    # Phone Number
    def on_enter(i):       # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
        number = phoneNo.get()
        if number == "Phone Number":
            phoneNo.delete(0,"end")
    def on_leave(i):
        number= phoneNo.get()
        if number == "":
            phoneNo.insert(2,"Phone Number")
    

    phoneNo = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18)) # Phone Number ENTRY BLOCK
    phoneNo.place(x=40,y=250)              # PLACE OF THE Phone Number ENTRY BLOCK
    phoneNo.insert(2,"Phone Number")       # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    phoneNo.bind("<FocusIn>",on_enter)     # GO 190
    phoneNo.bind("<FocusOut>",on_leave)    # GO 190

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=278) # FEATURES OF THE ENTRY BLOCK AND PLACE
        
        # password1
    def on_enter(i):        # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
        word1 = password1.get()
        if word1 == "Password":
            password1.delete(0,"end")
    def on_leave(i):
        word1= password1.get()
        if word1== "":
            password1.insert(2,"Password")
                
    password1 = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18))   # PASSWORD ENTRY BLOCK
    password1.place(x=40,y=300)            # PLACE OF THE PASSWORD ENTRY BLOCK
    password1.insert(2,"Password")         # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    password1.bind("<FocusIn>",on_enter)   # GO 209
    password1.bind("<FocusOut>",on_leave)  # GO 209

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=328) # FEATURES OF THE ENTRY BLOCK AND PLACE

            # password2
    def on_enter(i):        # THIS PART OF THE CODE WORKS FOR, WHEN YOU CLICK ON THE TEXT "USERNAME" WILL DISAPPEAR
        word2 = password2.get()
        if word2 == "Password Again":          
            password2.delete(0,"end")
    def on_leave(i):
        word2= password2.get()
        if word2== "":
            password2.insert(2,"Password Again")
                
    password2 = Entry(frame,width=25,fg="black", border=0,bg="white",font=("Microsoft Corbel",18))   # PASSWORD ENTRY BLOCK
    password2.place(x=40,y=350)               # PLACE OF THE PASSWORD ENTRY BLOCK
    password2.insert(2,"Password Again")      # WHAT WE WANT TO WRITE INTO THE ENTRY BLOCK
    password2.bind("<FocusIn>",on_enter)      # GO 227
    password2.bind("<FocusOut>",on_leave)     # GO 227

    Frame(frame,width=328,height=2,bg="#2f5eb8").place(x=38,y=378) # FEATURES OF THE ENTRY BLOCK AND PLACE
    
    # Sign Up Page Buttons
    Button(frame,width=23,text= "Sign Up",bg =  "#ff5a6c",fg = "white",border=0, font=("Microsoft Corbel",18),command=signup).place(x=38, y=428)      # FEATURES OF THE SIGN UP BUTTON
    Button(frame,width=23,text= "Back",bg =  "#2f5eb8",fg = "white",border=0, font=("Microsoft Corbel",18),command=Main).place(x=38, y=478)           # FEATURES OF THE BACK BUTTON




# Main Page Buttons
Button(frame,width=23,text= "Sign In",bg = "#2f5eb8",fg = "white",border=0, font=("Microsoft Corbel",18),command=signin).place(x=38, y=275)           # FEATURES OF THE SIGN IN BUTTON
label= Label(frame,text="Don't have an account?",bg="white",fg="black",border=0,font=("Microsoft Corbel",11)).place(x=125,y=325)                      # DON'T HAVE ACCOUNT TEXT
sign_up= Button(frame,width=23,text= "Sign Up",bg = "#ff5a6c",fg = "white",border=0, font=("Microsoft Corbel",18),command=signup).place(x=38, y=350)  # FEATURES OF THE SIGN UP BUTTON
root.mainloop()

