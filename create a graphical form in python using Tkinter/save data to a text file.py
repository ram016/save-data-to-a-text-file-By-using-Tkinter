from tkinter import*

def save_data():
    firstname_info=firstname.get()
    lastname_info=lastname.get()
    age_info=age.get()
    age_info=str(age_info)
    print(firstname_info,lastname_info,age_info)

    file=open("user.txt",'a+')
    file.write(firstname_info)
    file.write('\n')
    file.write(lastname_info)
    file.write('\n')
    file.write(age_info)
    file.write('\n')
    file.write('\n')

    file.close()
    print("user",firstname,"has been register successfully")
screen=Tk()
screen.geometry('500x500')
screen.title("Python Form")
heading=Label(text="Saving Data in text File",bg="grey",fg="Black",font=('arial',18,'bold'),height='2',width='500').pack()

firstname_text=Label(text="First Name *",font=('arial',15,'bold'))
firstname_text.place(x=10,y=80)

lastname_text=Label(text="LastName *",font=('arial',15,'bold'))
lastname_text.place(x=10,y=140)

age_text=Label(text='Age *',font=('arial',15,'bold'))
age_text.place(x=10,y=190)
#-----------Variable Declaratoin-------------------
firstname= StringVar()
lastname= StringVar()
age=IntVar()

#------------Creating Entry---------
firstname_entry=Entry(textvariable=firstname,width='30')
firstname_entry.place(x=10,y=110)
lastname_entry=Entry(textvariable=lastname,width='30')
lastname_entry.place(x=10,y=170)
age_entry=Entry(textvariable=age,width='30')
age_entry.place(x=10,y=220)
#-----------------Button--------
register=Button(screen,text="Register",width='30',command=save_data,bg='orange')
register.place(x=120,y=260)



screen.mainloop()

