
# from audioop import add
# from cgi import print_arguments
# from operator import ge
# from re import sub
from tkinter import *
import sqlite3
from tkinter import messagebox

from mysqlx import Column
root = Tk()
root.title("Facebook")
dataBAse = sqlite3.connect("Database.db")# creating database
c = dataBAse.cursor()#to execute the code
# to create new Table:
# c.execute("""CREATE TABLE Facebook(
#     first_name text,
#     last_name text,
#     age text,
#     address text,
#     city text,
#     zipcode text,
#     password text,
#     gender text
#     ) """)

def submit():
    dataBAse = sqlite3.connect("Database.db")
    c = dataBAse.cursor()
    c.execute("INSERT INTO Facebook VALUES(:first_name, :last_name,:age, :address, :city, :zipcode, :password, :gender)",{
        'first_name' : first_name.get(),
        'last_name' : last_name.get(),
        'age' : age.get(),
        'address' : address.get(),
        'city' : city.get(),
        'zipcode' : zipcode.get(),
        'password' : password.get(),
        'gender' : gender.get()
        
    })
    messagebox.showinfo("Address","Inserted Successfully")
    dataBAse.commit()
    dataBAse.close()
    #clear the text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)
    password.delete(0, END)
    gender.delete(0, END)
  
def query():
    dataBAse = sqlite3.connect("Database.db")
    c = dataBAse.cursor()
    c.execute("SELECT *, OID FROM Facebook")
    records = c.fetchall()
    
    print_record =''
    for record in records:
        print_record+=str(record[0])+' '+str(record[1])+' '+str(record[2])+' '+str(record[3])+' '+str(record[4])+' '+str(record[5])+' '+str(record[6])+' '+str(record[7])+'\t'+ str(record[8]) +"\n" # careful while putting indexing
    query_label = Label(root, text=print_record)
    query_label.grid(row=9, column=0, columnspan=2)
 
    
def delete():
    dataBAse = sqlite3.connect("Database.db")
    c = dataBAse.cursor()
    c.execute("DELETE FROM Facebook WHERE oid= "+ delete_box.get())
    print("Delete Successfully")
    delete_box.delete(0, END)
    dataBAse.commit()
    dataBAse.close()

def edit():
    global editor
    editor=Toplevel()# use to create a new window
    editor.title("Update Data")
    editor.geometry('300x400')
    dataBAse = sqlite3.connect("Database.db")
    c = dataBAse.cursor()
    record_id = update_box.get()
    c.execute("SELECT * FROM Facebook WHERE oid= "+ record_id)
    records = c.fetchall()
    
    global f_name_edit
    global l_name_edit
    global address_text_edit
    global age_edit
    global city_edit
    global zipcode_edit
    global password_edit
    global gender_edit
    
    f_name_edit = Entry(editor, width=30)
    f_name_edit.grid(row=0, column=1, padx=20,pady=(10,0))

    l_name_edit = Entry(editor, width=30)
    l_name_edit.grid(row=1, column=1)

    address_text_edit = Entry(editor, width=30)
    address_text_edit.grid(row=2, column=1)

    age_edit = Entry(editor, width=30)
    age_edit.grid(row=3, column=1)

    city_edit = Entry(editor, width=30)
    city_edit.grid(row=4, column=1)
    
    zipcode_edit = Entry(editor, width=30)
    zipcode_edit.grid(row=5, column=1)

    password_edit = Entry(editor, width =30)
    password_edit.grid(row=6, column =1, padx=20)

    gender_edit = Entry(editor, width=30)
    gender_edit.grid(row=7, column=1, padx=20)

    
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    
    age_label = Label(editor,text ="Age")
    age_label.grid(row=2,column= 0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=3, column=0)
    
    city_label = Label(editor, text="City")
    city_label.grid(row=4, column=0)
    
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    
    password_label = Label(editor, text="Password")
    password_label.grid(row=6, column=0)
    
    gender_label = Label(editor, text="Gender")
    gender_label.grid(row=7, column=0)


    
    
    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_text_edit.insert(0, record[2])
        age_edit.insert(0, record[3])
        city_edit.insert(0, record[4])
        zipcode_edit.insert(0, record[5])
        password_edit.insert(0, record[6])
        gender_edit.insert(0, record[7])    
        
        
    edit_btn = Button(editor,text="Save",command = update)
    edit_btn.grid(row=8, column=0,columnspan=2,pady=10)

def update():
    dataBAse = sqlite3.connect("Database.db")
    c = dataBAse.cursor()
    record_id = update_box.get()
    c.execute("""UPDATE Facebook SET 
              first_name = :first_name, 
              last_name = :last_name, 
              address = :address, 
              age = :age, 
              city = :city, 
              zipcode = :zipcode, 
              password = :password, 
              gender = :gender 
              WHERE oid =:oid""",{
            'first_name': f_name_edit.get(),
          'last_name': l_name_edit.get(),
          'age': age_edit.get(),
          'address': address_text_edit.get(),
          'city': city_edit.get(),
          'zipcode': zipcode_edit.get(),
          'password': password_edit.get(),
          'gender': gender_edit.get(),
          'oid': record_id})
    print ("Data has been updated")
    dataBAse.commit()
    dataBAse.close()
    editor.destroy()
    
    
    

    
    
    
    
    


first_name = Entry(root,width=30)
first_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

password = Entry(root, width =30)
password.grid(row=6, column =1, padx=20)

gender = Entry(root, width=30)
gender.grid(row=7, column=1, padx=20)

update_box = Entry(root, width=30)
update_box.grid(row=13, column=1, padx = 20)



#LABEL

first_name_label = Label(root, text = "First Name")
first_name_label.grid(row=0, column=0, padx=20)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0, padx=20)

age_label = Label(root, text="Age")
age_label.grid(row=2, column=0, padx=20)

address_label = Label(root, text="Address")
address_label.grid(row=3, column=0, padx=20)

city_label = Label(root, text="City")
city_label.grid(row=4, column=0, padx=20)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0, padx=20)

password_label = Label(root, text="Password")
password_label.grid(row=6, column=0, padx=20)

gender_label = Label(root, text="Gender")
gender_label.grid(row=7, column=0, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=11, column=1, padx=20)

delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=12,column=1, padx=20, columnspan=2, pady=10, ipadx=70)

submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=8, column=1, padx=20, columnspan=2, pady=10, ipadx=70) 

query_btn = Button(root, text="Query", command=query)
query_btn.grid(row=10, column=1, padx=20, columnspan=2, pady=10, ipadx=70)

update_box_label = Label(root, text="Update")
update_box_label.grid(row=13, column=0)

edit_btn = Button(root, text="Update", command=edit)
edit_btn.grid(row=14, column=1, padx=20, columnspan=2, pady=10, ipadx=70)



dataBAse.commit()
dataBAse.close()
root.mainloop()


