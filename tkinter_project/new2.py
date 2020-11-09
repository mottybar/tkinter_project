from tkinter import *
import pyodbc

conn = pyodbc.connect(
 'Driver={SQL Server};'
 'Server=MOTTYBAR20-PC\SQLEXPRESS;'
 'Database=ACDB;'
 'Trusted_Connection=yes;')

def Clean():
    frame1.place_forget()
    frame2.place_forget()
    frame3.place_forget()
    frame4.place_forget()
    frame5.place_forget()
    frame6.place_forget()



def Read_Customers(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.customers')
    for row in cursor:
        print(f'row = {row}')
    print()

def Read_Packages(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.packages')
    for row in cursor:
        print(f'row = {row}')
    print()

def create_customter():
    inserted = Label(frame1, text="****Record inserted successfully**", fg="black", bg="green")
    exception = Label(frame1, text="****Failed to insert the record*****", fg="black", bg="red")
    output = Text(frame1, width=100, height=1, wrap=WORD, background="white")
    try:
        customer_idget=customer_id.get()
        first_nameget=first_name.get()
        last_nameget=last_name.get()
        birth_dateget=birth_date.get()
        join_dateget=join_date.get()
        cityget=city.get()
        stateget=state.get()
        streetget=street.get()
        main_phone_numget=main_phone_num.get()
        secondary_phone_numget=secondary_phone_num.get()
        faxget=fax.get()
        monthly_discountget=monthly_discount.get()
        customer_pack_idget=customer_pack_id.get()
        cursor = conn.cursor()
        cursor.execute('SET IDENTITY_INSERT customers ON')
        cursor.execute('insert into dbo.customers(customer_id,first_name,last_name,birth_date,join_date,city,state,street,main_phone_num,secondary_phone_num,fax,monthly_discount,pack_id) values(?,?,?,?,?,?,?,?,?,?,?,?,?);',
        (customer_idget, first_nameget, last_nameget, birth_dateget, join_dateget,cityget,stateget,streetget,main_phone_numget,secondary_phone_numget,faxget,monthly_discountget,customer_pack_idget))
        conn.commit()
        output.place(x=0, y=340)
        cursor.execute('SELECT * FROM dbo.customers where customer_id=?;',
                       (customer_idget))
        for row in cursor:
            output.insert(END, str(row) + "\n")
        inserted.place(x=20, y=300)
    except:
        exception.place(x=20,y=300)
    customer_id.delete(0,END)
    first_name.delete(0,END)
    last_name.delete(0,END)
    birth_date.delete(0,END)
    join_date.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    street.delete(0,END)
    main_phone_num.delete(0,END)
    secondary_phone_num.delete(0,END)
    fax.delete(0,END)
    monthly_discount.delete(0,END)
    customer_pack_id.delete(0,END)





    
def create_package():
    inserted = Label(frame2, text = "****Record inserted successfully**", fg="black", bg="green")
    exception = Label(frame2, text ="****Failed to insert the record*****", fg="black", bg="red")
    output = Text(frame2, width=35, height=1, wrap=WORD, background="white")
    try:
        packages_pack_idget=packages_pack_id.get()
        speedget=speed.get()
        strt_dateget=strt_date.get()
        monthly_paymentget=monthly_payment.get()
        packages_sector_idget=packages_sector_id.get()
        cursor = conn.cursor()
        cursor.execute('SET IDENTITY_INSERT packages ON')
        cursor.execute('insert into dbo.packages(pack_id,speed,strt_date,monthly_payment,sector_id) values(?,?,?,?,?);',
               (packages_pack_idget, speedget, strt_dateget, monthly_paymentget,  packages_sector_idget)
               )
        conn.commit()
        output.place(x=0,y=150)
        cursor.execute('SELECT * FROM dbo.packages where pack_id=?;',
                            (packages_pack_idget))
        for row in cursor:
            output.insert(END,str(row) + "\n")
        inserted.place(x=20, y=180)
    except:
        exception.place(x=20,y=180)
    packages_pack_id.delete(0,END)
    speed.delete(0,END)
    strt_date.delete(0,END)
    monthly_payment.delete(0,END)
    packages_sector_id.delete(0,END)
    
def Update_package():
    updated = Label(frame3, text = "****Record updated successfully*", fg="black", bg="green")
    exception = Label(frame3, text ="****Failed to update the record***", fg="black", bg="red")
    output = Text(frame3, width=200, height=1, wrap=WORD, background="white")
    try:
        customer_idframe3get=customer_idframe3.get()
        customer_pack_idframe3get=customer_pack_idframe3.get()
        cursor = conn.cursor()
        cursor.execute('update dbo.customers set pack_id = ? where customer_id = ?;',
                   (customer_pack_idframe3get,customer_idframe3get)
                   )
        conn.commit()
        Read_Customers(conn)
        updated.place(x=20, y=180)
    except:
        exception.place(x=20,y=180)
    customer_idframe3.delete(0,END)
    customer_pack_idframe3.delete(0,END)

def delete():
    deleted = Label(frame4, text="***Record deleted successfully**", fg="black", bg="green")
    exception = Label(frame4, text="****Failed to delete the record**", fg="black", bg="red")
    try:
        customer_idframe4get=customer_idframe4.get()
        cursor = conn.cursor()
        cursor.execute('delete from dbo.customers where customer_id = ?;',
                   (customer_idframe4get))
        conn.commit()
        Read_Customers(conn)
        deleted.place(x=20, y=180)
    except:
        exception.place(x=20,y=180)
    customer_idframe4.delete(0, END)



def add_a_customer():
    Clean()
    frame1.place(x=0,y=200,height=1000,width=1000)
    customer_id_label.place(x=0,y=0)
    customer_id.place(x=110,y=0)
    first_name_label.place(x=0,y=20)
    first_name.place(x=110,y=20)
    last_name_label.place(x=0,y=40)
    last_name.place(x=110, y=40)
    birth_date_label.place(x=0, y=60)
    birth_date.place(x=110, y=60)
    join_date_label.place(x=0,y=80)
    join_date.place(x=110, y=80)
    city_label.place(x=0, y=100)
    city.place(x=110, y=100)
    state_label.place(x=0, y=120)
    state.place(x=110, y=120)
    street_label.place(x=0, y=140)
    street.place(x=110, y=140)
    main_phone_num_label.place(x=0, y=160)
    main_phone_num.place(x=110, y=160)
    secondary_phone_num_label.place(x=0, y=180)
    secondary_phone_num.place(x=110, y=180)
    fax_label.place(x=0, y=200)
    fax.place(x=110, y=200)
    monthly_discount_label.place(x=0, y=220)
    monthly_discount.place(x=110, y=220)
    customer_pack_id_label.place(x=0, y=240)
    customer_pack_id.place(x=110, y=240)
    
    button6 = Button(frame1, text="submit", bg="blue", fg="white", width=30,command=create_customter).place(x=20, y=270)

    

def add_a_package():
    Clean()
    frame2.place(x=0,y=200,height=1000,width=1000)
    packages_pack_id_label.place(x=0, y=0)
    packages_pack_id.place(x=110, y=0)
    speed_label.place(x=0, y=20)
    speed.place(x=110, y=20)
    strt_date_label.place(x=0, y=40)
    strt_date.place(x=110, y=40)
    monthly_payment_label.place(x=0, y=60)
    monthly_payment.place(x=110, y=60)
    packages_sector_id_label.place(x=0, y=80)
    packages_sector_id.place(x=110, y=80)

    button6 = Button(frame2, text="submit", bg="blue", fg="white", width=30,command=create_package ).place(x=20, y=220)

def change_a_package():
    Clean()
    frame3.place(x=0, y=200, height=2000, width=2000)
    customer_id_labelframe3.place(x=0, y=0)
    customer_idframe3.place(x=110, y=0)
    customer_pack_id_labelframe3.place(x=0, y=20)
    customer_pack_idframe3.place(x=110, y=20)
    
    button6 = Button(frame3, text="submit", bg="blue", fg="white", width=30,command=Update_package).place(x=20, y=220)

def delete_a_customer():
    Clean()
    frame4.place(x=0, y=200, height=1000, width=1000)
    customer_id_labelframe4.place(x=0, y=0)
    customer_idframe4.place(x=110, y=0)

    button6 = Button(frame4, text="submit", bg="blue", fg="white", width=30, command=delete).place(x=20, y=220)

def query1():
    Clean()
    frame5.place(x=0, y=200, height=1000, width=1000)
    xscrollbar = Scrollbar(window,orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    yscrollbar = Scrollbar(window,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)
    output = Text(frame5, width=75, height=25, wrap=WORD, background="white",xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
    xscrollbar.config(command=output.xview)
    yscrollbar.config(command=output.yview)
    output.place(x=0,y=0)
    cursor = conn.cursor()
    cursor.execute('select customers.First_Name,monthly_discount,pack_id,main_phone_num,secondary_phone_num from customers where customers.pack_id in (select packages.pack_id from packages where sector_id=2 )')
    for row in cursor:
        output.insert(END,str(row) + "\n" )

def get_query2():
    blanklable= Label(frame6,text="                              ", fg="black", bg="white")
    exception = Label(frame6, text="***wrong input**", fg="black", bg="red")
    output = Text(frame6, width=50, height=20, wrap=WORD, background="white")
    try:
        blanklable.place(x=250, y=0)
        exception.place_forget()
        customer_idframe6get=customer_idframe6.get()
        cursor = conn.cursor()
        cursor.execute('select customers.First_Name,Last_name,join_date from customers where MONTH(customers.Join_Date) = (select MONTH(customers.Join_Date) from customers where customers.Customer_Id=?) and YEAR(customers.Join_Date) = (select YEAR(customers.Join_Date) from customers where customers.Customer_Id=?);',
                   (customer_idframe6get,customer_idframe6get))
        output.place(x=0, y=60)
        for row in cursor:
            output.insert(END,str(row) + "\n" )
    except:
        exception.place(x=250,y=0)
    customer_idframe6.delete(0, END)



def query2():
    Clean()
    frame6.place(x=0, y=200, height=1000, width=1000)
    customer_id_labelframe6.place(x=0, y=0)
    customer_idframe6.place(x=130, y=0)
    Button(frame6, text="submit",bg="blue",fg="white", width=30,command=get_query2) .place(x=0, y=20)


window=Tk()
window.geometry("800x600")
window.configure(background="orange")
window.title("Kirya_Comunication_LTD")





Label(window, text="Kirya_Comunication_LTD ", fg="green", font="none 20 bold") .place(x=180, y=0)
frame1=Frame(window,bg="white")
frame2=Frame(window,bg="white")
frame3=Frame(window,bg="white")
frame4=Frame(window,bg="white")
frame5=Frame(window,bg="white")
frame6=Frame(window,bg="white")


customer_id = Entry(frame1, width=20, bg="white")
customer_idframe3 = Entry(frame3, width=20, bg="white")
customer_idframe4 = Entry(frame4, width=20, bg="white")
customer_idframe6 = Entry(frame6, width=20, bg="white")
first_name = Entry(frame1, width=20, bg="white")
last_name = Entry(frame1, width=20, bg="white")
birth_date = Entry(frame1, width=20, bg="white")
join_date = Entry(frame1, width=20, bg="white")
city = Entry(frame1, width=20, bg="white")
state = Entry(frame1, width=20, bg="white")
street = Entry(frame1, width=20, bg="white")
main_phone_num = Entry(frame1, width=20, bg="white")
secondary_phone_num = Entry(frame1, width=20, bg="white")
fax = Entry(frame1, width=20, bg="white")
monthly_discount = Entry(frame1, width=20, bg="white")
customer_pack_id = Entry(frame1, width=20, bg="white")
customer_pack_idframe3 = Entry(frame3, width=20, bg="white")
customer_id_label = Label(frame1, text="customer_id",bg="white")
customer_id_labelframe3 = Label(frame3, text="customer_id",bg="white")
customer_id_labelframe4 = Label(frame4, text="customer_id",bg="white")
customer_id_labelframe6 = Label(frame6, text="customer_id",bg="white")
first_name_label=Label(frame1, text="first_name",bg="white")
last_name_label=Label(frame1, text="last_name",bg="white")
birth_date_label=Label(frame1, text="birth_date",bg="white")
join_date_label=Label(frame1, text="join_date",bg="white")
city_label=Label(frame1, text="city",bg="white")
state_label=Label(frame1, text="state",bg="white")
street_label=Label(frame1, text="street",bg="white")
main_phone_num_label=Label(frame1, text="main_phone",bg="white")
secondary_phone_num_label=Label(frame1, text="secondary_phone",bg="white")
fax_label=Label(frame1, text="fax",bg="white")
monthly_discount_label=Label(frame1, text="monthly_discount",bg="white")
customer_pack_id_label=Label(frame1, text="pack_id",bg="white")
customer_pack_id_labelframe3=Label(frame3, text="pack_id",bg="white")
packages_pack_id = Entry(frame2, width=20, bg="white")
speed = Entry(frame2, width=20, bg="white")
strt_date = Entry(frame2, width=20, bg="white")
monthly_payment = Entry(frame2, width=20, bg="white")
packages_sector_id = Entry(frame2, width=20, bg="white")
packages_pack_id_label=Label(frame2, text="pack_id",bg="white")
speed_label=Label(frame2, text="speed",bg="white")
strt_date_label=Label(frame2, text="strt_date",bg="white")
monthly_payment_label=Label(frame2, text="monthly_payment",bg="white")
packages_sector_id_label=Label(frame2, text="sector_id",bg="white")


button1=Button(window, text="add a customer", bg="blue",width=30,fg="white", command=add_a_customer) .place(x=0, y=50)

button2=Button(window, text="add a package",bg="blue", width=30,fg="white", command=add_a_package) .place(x=0, y=80)

button3=Button(window, text="update a package",bg="blue",fg="white", width=30,command=change_a_package) .place(x=0, y=110)

button4=Button(window, text="delete a customer",bg="blue",fg="white", width=30,command=delete_a_customer) .place(x=0, y=140)

button5=Button(window, text="Query1",bg="blue",fg="white", width=30,command=query1) .place(x=230, y=50)

button6=Button(window, text="Query2",bg="blue",fg="white", width=30,command=query2) .place(x=230, y=80)

button7=Button(window, text="Query3",bg="blue",fg="white", width=30) .place(x=230, y=110)

button8=Button(window, text="Query4",bg="blue",fg="white", width=30) .place(x=230, y=140)















window.mainloop()