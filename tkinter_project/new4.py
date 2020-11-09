from tkinter import *
import pyodbc
from tkinter import ttk






conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=MOTTYBAR20-PC\SQLEXPRESS;'
    'Database=ACDB;'
    'Trusted_Connection=yes;')


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


def create_customter(window1, customer_id, first_name, last_name, birth_date, join_date, city, state, street,
                     main_phone_num, secondary_phone_num, fax, monthly_discount, customer_pack_id):
    inserted = Label(window1, text="Record inserted successfully", fg="black", bg="green")
    exception = Label(window1, text="Failed to insert the record", fg="black", bg="red", padx=8)
    output = Text(window1, width=100, height=3, wrap=WORD, font="Times 15 bold", background="white")
    output.tag_config('warning', background="red", foreground="yellow")
    output.tag_config('created', background="green", foreground="yellow")
    output.place(x=0, y=400)
    try:
        customer_idget = customer_id.get()
        first_nameget = first_name.get()
        last_nameget = last_name.get()
        birth_dateget = birth_date.get()
        join_dateget = join_date.get()
        cityget = city.get()
        stateget = state.get()
        streetget = street.get()
        main_phone_numget = main_phone_num.get()
        secondary_phone_numget = secondary_phone_num.get()
        faxget = fax.get()
        monthly_discountget = monthly_discount.get()
        customer_pack_idget = customer_pack_id.get()
        cursor = conn.cursor()
        cursor.execute('SET IDENTITY_INSERT customers ON')
        cursor.execute(
            'insert into dbo.customers(customer_id,first_name,last_name,birth_date,join_date,city,state,street,main_phone_num,secondary_phone_num,fax,monthly_discount,pack_id) values(?,?,?,?,?,?,?,?,?,?,?,?,?);',
            (customer_idget, first_nameget, last_nameget, birth_dateget, join_dateget, cityget, stateget, streetget,
             main_phone_numget, secondary_phone_numget, faxget, monthly_discountget, customer_pack_idget))
        conn.commit()

        cursor.execute('SELECT customer_id,first_name,last_name,birth_date,join_date,city,state,street,main_phone_num,secondary_phone_num,fax,monthly_discount,pack_id FROM dbo.customers where customer_id=?;',
                       (customer_idget))
        output.insert(END, "Record inserted successfully", 'created')
        for row in cursor:
            output.insert(END, "\n" + str(row) + "\n")

    except:
        output.insert(END, "********Failed to insert the record******", 'warning')


def create_package(window2, packages_pack_id, speed, strt_date, monthly_payment, packages_sector_id):
    inserted = Label(window2, text="Record inserted successfully", fg="black", bg="green")
    exception = Label(window2, text="Failed to insert the record", fg="black", bg="red", padx=8)
    output = Text(window2, width=100, height=3, wrap=WORD, font="Times 20 bold", background="white")
    output.tag_config('warning', background="red", foreground="yellow")
    output.tag_config('created', background="green", foreground="yellow")
    output.place(x=0, y=300)
    try:
        packages_pack_idget = packages_pack_id.get()
        speedget = speed.get()
        strt_dateget = strt_date.get()
        monthly_paymentget = monthly_payment.get()
        packages_sector_idget = packages_sector_id.get()
        cursor = conn.cursor()
        cursor.execute('SET IDENTITY_INSERT packages ON')
        cursor.execute('insert into dbo.packages(pack_id,speed,strt_date,monthly_payment,sector_id) values(?,?,?,?,?);',
                       (packages_pack_idget, speedget, strt_dateget, monthly_paymentget, packages_sector_idget)
                       )
        conn.commit()

        cursor.execute('SELECT * FROM dbo.packages where pack_id=?;',
                       (packages_pack_idget))
        output.insert(END, "Record inserted successfully", 'created')
        for row in cursor:
            output.insert(END, "\n" + str(row) + "\n")

    except:
        output.insert(END, "*************Failed to insert the record**********************", 'warning')


def Update_package(window3, customer_id, customer_pack_id):
    updated = Label(window3, text="Record updated successfully", fg="black", bg="green")
    exception = Label(window3, text="Failed to update the record", fg="black", bg="red", padx=5)
    output = Text(window3, width=90, height=3, wrap=WORD, font="Times 20 bold", background="white")
    output.tag_config('warning', background="red", foreground="yellow")
    output.tag_config('updated', background="green", foreground="yellow")
    output.place(x=0, y=150)
    try:
        customer_idget = customer_id.get()
        customer_pack_idget = customer_pack_id.get()
        cursor = conn.cursor()
        cursor.execute('update dbo.customers set pack_id = ? where customer_id = ?;',
                       (customer_pack_idget, customer_idget)
                       )
        conn.commit()
        cursor.execute('SELECT customer_id,first_name,last_name,birth_date,join_date,city,state,street,main_phone_num,secondary_phone_num,fax,monthly_discount,pack_id FROM dbo.customers where customer_id=?;',
                       (customer_idget))
        output.insert(END, "Record updated successfully", 'updated')
        for row in cursor:
            output.insert(END, "\n" + str(row) + "\n")

    except:
        output.insert(END, "*************failed to update the record**********************", 'warning')


def delete(window4, customer_id):
    deleted = Label(window4, text="Record deleted successfully", fg="black", bg="green")
    exception = Label(window4, text="Failed to delete the record", fg="black", bg="red", padx=5)
    output = Text(window4, width=100, height=3, wrap=WORD, font="Times 20 bold", background="white")
    output.place(x=0, y=150)
    output.tag_config('warning', background="red", foreground="yellow")
    output.tag_config('deleted', background="green", foreground="yellow")
    try:
        customer_idget = customer_id.get()
        cursor = conn.cursor()
        cursor.execute('delete from dbo.customers where customer_id = ?;',
                       (customer_idget))
        conn.commit()
        output.insert(END, "*********Record deleted successfully*******", 'deleted')
    except:
        output.insert(END, "*****Failed to delete the record********", 'warning')


def query1():
    i = 1
    window5 = Tk()
    window5.geometry("800x600")
    window5.title("Kirya_Comunication_LTD")
    window5.configure(bg="white")
    tree = ttk.Treeview(window5, height=20)
    tree["columns"] = ("one", "two", "three","four","five")
    tree.column("#0", anchor="w", width='50')
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three", width=100)
    tree.column("four", width=100)
    tree.column("five", width=100)

    tree.heading("#0")
    tree.heading("one", text="First_Name")
    tree.heading("two", text="monthly_discount")
    tree.heading("three", text="pack_id")
    tree.heading("four", text="main_phone_num")
    tree.heading("five", text="secondary_phone_num")


    xscrollbar = Scrollbar(window5, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    yscrollbar = Scrollbar(window5, orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)
    xscrollbar.config(command=tree.xview)
    yscrollbar.config(command=tree.yview)
    tree.place(x=0, y=0)
    cursor = conn.cursor()
    cursor.execute(
        'select customers.First_Name,monthly_discount,pack_id,main_phone_num,secondary_phone_num from customers where customers.pack_id in (select packages.pack_id from packages where sector_id=2 )')
    for row in cursor:
        tree.insert('', 'end', text=str(i), values=(row[0],row[1],row[2],row[3],row[4]))
        i += 1
    button2 = Button(window5, text="Exit", bg="red", fg="white", width=10, command=window5.destroy).place(x=300,y=450)


def get_query2(window6, customer_id):
    i = 1
    tree = ttk.Treeview(window6,height=50)
    tree["columns"] = ("one", "two", "three")
    tree.column("#0", anchor="w", width='50')
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three", width=250)
    tree.heading("#0")
    tree.heading("one", text="First_Name")
    tree.heading("two", text="Last_Name")
    tree.heading("three", text="join_date")

    output = Text(window6,width=50,height=20, wrap=WORD, font="Times 30 bold", background="white")
    output.tag_config('warning', background="red", foreground="yellow", font="Times 12 bold")

    try:
        customer_idget = customer_id.get()
        cursor = conn.cursor()
        cursor.execute(
            'select customers.First_Name,Last_name,join_date from customers where MONTH(customers.Join_Date) = (select MONTH(customers.Join_Date) from customers where customers.Customer_Id=?) and YEAR(customers.Join_Date) = (select YEAR(customers.Join_Date) from customers where customers.Customer_Id=?);',
            (customer_idget, customer_idget))
        tree.place(x=300,y=0)
        for row in cursor:
            tree.insert('', 'end', text=str(i), values=(row[0],row[1],row[2]))
            i += 1

    except:
        output.place(x=300,y=0)
        output.insert(END, "****************************Wrong input************************", 'warning')


def query2():
    window6 = Tk()
    window6.geometry("800x600")
    window6.configure(bg="white")
    window6.title("Kirya_Comunication_LTD")
    customer_id = Entry(window6, width=20, font="none 10 bold", bg="white")
    customer_id_label = Label(window6, text="customer_id", font="none 10 bold")
    customer_id_label.place(x=0, y=0)
    customer_id.place(x=130, y=0)
    entry_list = [customer_id]
    Button(window6, text="submit", bg="green", fg="white", width=10,
           command=lambda: get_query2(window6, customer_id)).place(x=10, y=30)
    Button(window6, text="Exit", bg="red", fg="white", width=10, command=window6.destroy).place(x=100, y=30)
    Button(window6, text="Clear", bg="purple", fg="white", width=10, command=lambda: clear(entry_list)).place(x=200,y=30)


def query3():
    i = 1
    window7 = Tk()
    window7.geometry("800x600")
    window7.title("Kirya_Comunication_LTD")
    window7.configure(bg="white")
    tree = ttk.Treeview(window7,height=20)
    xscrollbar = Scrollbar(window7, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    yscrollbar = Scrollbar(window7, orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)
    xscrollbar.config(command=tree.xview)
    yscrollbar.config(command=tree.yview)
    tree["columns"] = ("one", "two", "three","four","five")
    tree.column("#0", anchor="w", width='50')
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three", width=100)
    tree.column("four", width=150)
    tree.column("five", width=100)

    tree.heading("#0")
    tree.heading("one", text="First_Name")
    tree.heading("two", text="Last_Name")
    tree.heading("three", text="City")
    tree.heading("four", text="State")
    tree.heading("five", text="pack_id")



    tree.pack()


    cursor = conn.cursor()
    cursor.execute(
        "select customers.First_Name,Last_Name,City,State,pack_id from customers where customers.pack_id in (select packages.pack_id from packages where speed='5Mbps')")

    for row in cursor:
        tree.insert('', 'end', text=str(i), values=(row[0],row[1],row[2],row[3],row[4]))
        i += 1
    Button(window7, text="Exit", bg="red", fg="white", width=10, command=window7.destroy).place(x=110, y=450)


def query4():
    cpt = 1
    window8 = Tk()
    window8.geometry("800x600")
    window8.title("Kirya_Comunication_LTD")
    window8.configure(bg="white")
    tree = ttk.Treeview(window8,height=20)
    xscrollbar = Scrollbar(window8, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    yscrollbar = Scrollbar(window8, orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)
    xscrollbar.config(command=tree.xview)
    yscrollbar.config(command=tree.yview)
    tree["columns"] = ("one", "two", "three")
    tree.column("#0", anchor="w",width='50')
    tree.column("one", width=100)
    tree.column("two", width=110)
    tree.column("three", width=100)
    tree.heading("#0")
    tree.heading("one", text="First_Name")
    tree.heading("two", text="monthly_discount")
    tree.heading("three", text="pack_id")
    tree.pack()
    cursor = conn.cursor()
    cursor.execute(
        ' select customers.First_Name,monthly_discount,pack_id from customers where customers.pack_id in (select packages.pack_id from packages where packages.monthly_payment > (select AVG(packages.monthly_payment) AVERAGE from packages))')

    for row in cursor:
        tree.insert('', 'end',text=str(cpt), values=(row[0], row[1], row[2]))
        cpt += 1


    Button(window8, text="Exit", bg="red", fg="white", width=10, command=window8.destroy).place(x=350, y=450)

def update_packages_abroad(window9,customer_id,partners_pack_id):
    output = Text(window9, width=90, height=3, wrap=WORD, font="Times 20 bold", background="white")
    output.tag_config('warning', background="red", foreground="yellow")
    output.tag_config('updated', background="green", foreground="yellow")
    output.place(x=0, y=150)
    try:
        customer_idget = customer_id.get()
        partners_pack_idget = partners_pack_id.get()
        cursor = conn.cursor()
        cursor.execute('update dbo.customers set partners_pack_id = ? where customer_id = ?;',
                       (partners_pack_idget, customer_idget)
                       )
        conn.commit()
        cursor.execute(
            'SELECT * FROM dbo.customers where customer_id=?;',
            (customer_idget))
        output.insert(END, "Record updated successfully", 'updated')
        for row in cursor:
            output.insert(END, "\n" + str(row) + "\n")

    except:
        output.insert(END, "*************failed to update the record**********************", 'warning')



def packages_abroad():
    window9 = Tk()
    window9.geometry("800x1000")
    window9.title("Kirya_Comunication_LTD")
    show_image(window9, "project2.gif")
    customer_id = Entry(window9, width=20, font="none 10 bold", bg="white")
    partners_pack_id = Entry(window9, width=20, font="none 10 bold", bg="white")
    customer_id_label = Label(window9, text="customer_id", font="none 10 bold", bg="white")
    partners_pack_id_label = Label(window9, text="partners_pack_id", font="none 10 bold", bg="white")
    customer_id_label.place(x=0, y=30)
    customer_id.place(x=120, y=30)
    partners_pack_id_label.place(x=0, y=50)
    partners_pack_id.place(x=120, y=50)
    entry_list = [customer_id, partners_pack_id]

    Button(window9, text="submit", bg="green", fg="white", width=10,command=lambda: update_packages_abroad(window9,customer_id,partners_pack_id)).place(x=20, y=100)
    Button(window9, text="Exit", bg="red", fg="white", width=10, command=window9.destroy).place(x=110, y=100)
    Button(window9, text="Clear", bg="purple", fg="white", width=10, command=lambda: clear(entry_list)).place(x=200,y=100)


def clear(entry_list):
    for entry in entry_list:
        entry.delete(0, END)


def add_a_customer():
    window1 = Tk()
    window1.geometry("800x600")
    window1.title("Kirya_Comunication_LTD")
    show_image(window1, "project3.gif")
    customer_id = Entry(window1, width=20, font="none 10 bold", bg="white")
    first_name = Entry(window1, width=20, font="none 10 bold", bg="white")
    last_name = Entry(window1, width=20, font="none 10 bold", bg="white")
    birth_date = Entry(window1, width=20, font="none 10 bold", bg="white")
    join_date = Entry(window1, width=20, font="none 10 bold", bg="white")
    city = Entry(window1, width=20, font="none 10 bold", bg="white")
    state = Entry(window1, width=20, font="none 10 bold", bg="white")
    street = Entry(window1, width=20, font="none 10 bold", bg="white")
    main_phone_num = Entry(window1, width=20, font="none 10 bold", bg="white")
    secondary_phone_num = Entry(window1, width=20, font="none 10 bold", bg="white")
    fax = Entry(window1, width=20, font="none 10 bold", bg="white")
    monthly_discount = Entry(window1, width=20, font="none 10 bold", bg="white")
    customer_pack_id = Entry(window1, width=20, font="none 10 bold", bg="white")
    customer_id_label = Label(window1, text="customer_id", font="none 10 bold",bg="white")
    first_name_label = Label(window1, text="first_name", font="none 10 bold",bg="white")
    last_name_label = Label(window1, text="last_name", font="none 10 bold",bg="white")
    birth_date_label = Label(window1, text="birth_date", font="none 10 bold",bg="white")
    join_date_label = Label(window1, text="join_date", font="none 10 bold",bg="white")
    city_label = Label(window1, text="city", font="none 10 bold",bg="white")
    state_label = Label(window1, text="state", font="none 10 bold",bg="white")
    street_label = Label(window1, text="street", font="none 10 bold",bg="white")
    main_phone_num_label = Label(window1, text="main_phone", font="none 10 bold",bg="white")
    secondary_phone_num_label = Label(window1, text="secondary_phone", font="none 10 bold",bg="white")
    fax_label = Label(window1, text="fax", font="none 10 bold",bg="white")
    monthly_discount_label = Label(window1, text="monthly_discount", font="none 10 bold",bg="white")
    customer_pack_id_label = Label(window1, text="pack_id", font="none 10 bold",bg="white")
    customer_id_label.place(x=0, y=30)
    customer_id.place(x=120, y=30)
    first_name_label.place(x=0, y=50)
    first_name.place(x=120, y=50)
    last_name_label.place(x=0, y=70)
    last_name.place(x=120, y=70)
    birth_date_label.place(x=0, y=90)
    birth_date.place(x=120, y=90)
    join_date_label.place(x=0, y=110)
    join_date.place(x=120, y=110)
    city_label.place(x=0, y=130)
    city.place(x=120, y=130)
    state_label.place(x=0, y=150)
    state.place(x=120, y=150)
    street_label.place(x=0, y=170)
    street.place(x=120, y=170)
    main_phone_num_label.place(x=0, y=190)
    main_phone_num.place(x=120, y=190)
    secondary_phone_num_label.place(x=0, y=210)
    secondary_phone_num.place(x=120, y=210)
    fax_label.place(x=0, y=230)
    fax.place(x=120, y=230)
    monthly_discount_label.place(x=0, y=250)
    monthly_discount.place(x=120, y=250)
    customer_pack_id_label.place(x=0, y=270)
    customer_pack_id.place(x=120, y=270)
    entry_list = [customer_id, first_name, last_name, birth_date, join_date, city, state, street, main_phone_num,
                  secondary_phone_num, fax, monthly_discount, customer_pack_id]

    Button(window1, text="Submit", bg="green", fg="white", width=10,
           command=lambda: create_customter(window1, customer_id, first_name, last_name, birth_date, join_date, city,
                                            state, street, main_phone_num, secondary_phone_num, fax, monthly_discount,
                                            customer_pack_id)).place(x=20, y=350)
    Button(window1, text="Exit", bg="red", fg="white", width=10, command=window1.destroy).place(x=110, y=350)
    Button(window1, text="Clear", bg="purple", fg="white", width=10, command=lambda: clear(entry_list)).place(x=200,y=350)


def add_a_package():
    window2 = Tk()
    window2.geometry("800x600")
    window2.title("Kirya_Comunication_LTD")
    show_image(window2, "project4.gif")
    packages_pack_id = Entry(window2, width=20)
    speed = Entry(window2, width=20, bg="white")
    strt_date = Entry(window2, width=20, bg="white")
    monthly_payment = Entry(window2, width=20, bg="white")
    packages_sector_id = Entry(window2, width=20,bg="white")
    packages_pack_id_label = Label(window2, text="pack_id", font="none 10 bold")
    speed_label = Label(window2, text="speed", font="none 10 bold")
    strt_date_label = Label(window2, text="strt_date", font="none 10 bold")
    monthly_payment_label = Label(window2, text="monthly_payment", font="none 10 bold")
    packages_sector_id_label = Label(window2, text="sector_id", font="none 10 bold")
    packages_pack_id_label.place(x=0, y=30)
    packages_pack_id.place(x=120, y=30)
    speed_label.place(x=0, y=50)
    speed.place(x=120, y=50)
    strt_date_label.place(x=0, y=70)
    strt_date.place(x=120, y=70)
    monthly_payment_label.place(x=0, y=90)
    monthly_payment.place(x=120, y=90)
    packages_sector_id_label.place(x=0, y=110)
    packages_sector_id.place(x=120, y=110)
    entry_list = [packages_pack_id, speed, strt_date, monthly_payment, packages_sector_id]

    Button(window2, text="submit", bg="green", fg="white", width=10,
           command=lambda: create_package(window2, packages_pack_id, speed, strt_date, monthly_payment,
                                          packages_sector_id)).place(x=20, y=200)
    Button(window2, text="Exit", bg="red", fg="white", width=10, command=window2.destroy).place(x=110, y=200)
    Button(window2, text="Clear", bg="purple", fg="white", width=10, command=lambda: clear(entry_list)).place(x=200,y=200)


def change_a_package():
    window3 = Tk()
    window3.geometry("800x600")
    window3.title("Kirya_Comunication_LTD")
    show_image(window3, "project5.gif")
    customer_id = Entry(window3, width=20, font="none 10 bold", bg="white")
    customer_pack_id = Entry(window3, width=20, font="none 10 bold", bg="white")
    customer_id_label = Label(window3, text="customer_id", font="none 10 bold",bg="white")
    customer_pack_id_label = Label(window3, text="pack_id", font="none 10 bold",bg="white")
    customer_id_label.place(x=0, y=30)
    customer_id.place(x=120, y=30)
    customer_pack_id_label.place(x=0, y=50)
    customer_pack_id.place(x=120, y=50)
    entry_list = [customer_id, customer_pack_id]

    Button(window3, text="submit", bg="green", fg="white", width=10,
           command=lambda: Update_package(window3, customer_id, customer_pack_id)).place(x=20, y=100)
    Button(window3, text="Exit", bg="red", fg="white", width=10, command=window3.destroy).place(x=110, y=100)
    Button(window3, text="Clear", bg="purple", fg="white", width=10, command=lambda: clear(entry_list)).place(x=200,y=100)


def delete_a_customer():

    window4 = Tk()
    window4.geometry("800x600")
    window4.title("Kirya_Comunication_LTD")
    show_image(window4, "project6.gif")
    customer_id = Entry(window4, width=20, font="none 10 bold", bg="white")
    customer_id_label = Label(window4, text="customer_id", font="none 10 bold",bg="white")
    customer_id_label.place(x=0, y=30)
    customer_id.place(x=110, y=30)
    entry_list = [customer_id]
    Button(window4, text="submit", bg="green", fg="white", width=10,
           command=lambda: delete(window4, customer_id)).place(x=20, y=80)
    Button(window4, text="Exit", bg="red", fg="white", width=10, command=window4.destroy).place(x=110, y=80)
    Button(window4, text="Clear", bg="purple", fg="white", width=10, command=lambda: clear(entry_list)).place(x=200,y=80)


def new_window():
    master.destroy()
    window = Tk()
    window.geometry("800x600")
    window.configure(bg="light blue")
    window.title("Kirya_Comunication_LTD")
    show_image(window,"project11.gif")
    Button(window, text="add a customer", bg="grey", width=30, font="none 12 bold", fg="white",command=add_a_customer).place(x=250, y=50)
    Button(window, text="add a package", bg="grey", width=30, font="none 12 bold", fg="white",command=add_a_package).place(x=250, y=90)
    Button(window, text="update a package", bg="grey", font="none 12 bold", fg="white", width=30,command=change_a_package).place(x=250, y=130)
    Button(window, text="delete a customer", bg="grey", font="none 12 bold", fg="white", width=30,command=delete_a_customer).place(x=250, y=170)
    Button(window, text="Query1", bg="grey", fg="white", font="none 12 bold", width=30, command=query1).place(x=250, y=210)
    Button(window, text="Query2", bg="grey", fg="white", font="none 12 bold", width=30, command=query2).place(x=250, y=250)
    Button(window, text="Query3", bg="grey", fg="white", font="none 12 bold", width=30, command=query3).place(x=250, y=290)
    Button(window, text="Query4", bg="grey", fg="white", font="none 12 bold", width=30, command=query4).place(x=250, y=330)
    Button(window, text="update a package abroad", bg="grey", fg="white", font="none 12 bold", width=30, command=packages_abroad).place(x=250, y=370)

def show_image(root,image_name):
    canvas = Canvas(root, width=500, height=500)
    img_label = Label(canvas)
    img_label.image = PhotoImage(master=root,file=image_name)
    img_label['image'] = img_label.image
    canvas.create_image(0, 0, anchor=NW, image=img_label.image)
    canvas.pack(side=TOP,expand='yes',fill='both')

master = Tk()
master.geometry("1000x600")
master.title("Kirya_Comunication_LTD")
show_image(master,"project1.gif")
button1 = Button(master, text="login", bg="light sky blue", width=10, fg="black", font="none 16 bold", command=new_window)
button1.place(x=440, y=140)
label1 = Label(master, text="Kirya_Comunication_LTD ", fg="black", bg="light sky blue", font="none 30 bold").place(x=0, y=0)


master.mainloop()