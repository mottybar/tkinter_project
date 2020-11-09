from tkinter import *
import pyodbc


def Create(conn,customer_id,first_name):
 #   try:
        cursor = conn.cursor()
        cursor.execute('insert into dbo.customers(customer_id,first_name) values(?,?);',
                (customer_id, first_name))


        conn.commit()
       # print("Record inserted successfully into Laptop table")
  #  except :
  #          print("Failed to insert into MySQL table {}")


def add_a_customer():
    frame2.place_forget()
    frame1.place(x=220,y=200,height=500,width=250)
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
    button5 = Button(frame1, text="submit", bg="blue", fg="white", width=30,command=Create(conn,customer_id,first_name)).place(x=0, y=260)



def add_a_package():
    frame1.place_forget()
    frame2.place(x=220,y=200,height=500,width=250)
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
    button5 = Button(frame2, text="submit", bg="blue", fg="white", width=30).place(x=0, y=260)



window=Tk()
window.geometry("700x500")
window.configure(background="white")

conn = pyodbc.connect(
 'Driver={SQL Server};'
 'Server=MOTTYBAR20-PC\SQLEXPRESS;'
 'Database=sqlexercise01;'
 'Trusted_Connection=yes;')



Label(window, text="Kirya_Comunication_LTD ", fg="green", font="none 20 bold") .place(x=180, y=0)
frame1=Frame(window,bg="white")
frame2=Frame(window,bg="white")
customer_id = Entry(frame1, width=20, bg="white")
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
customer_id_label = Label(frame1, text="customer_id",bg="white")
first_name_label=Label(frame1, text="first_name",bg="white")
last_name_label=Label(frame1, text="last_name",bg="white")
birth_date_label=Label(frame1, text="birth_date",bg="white")
join_date_label=Label(frame1, text="join_date",bg="white")
city_label=Label(frame1, text="city",bg="white")
state_label=Label(frame1, text="state",bg="white")
street_label=Label(frame1, text="street",bg="white")
main_phone_num_label=Label(frame1, text="main_phone")
secondary_phone_num_label=Label(frame1, text="secondary_phone",bg="white")
fax_label=Label(frame1, text="fax",bg="white")
monthly_discount_label=Label(frame1, text="monthly_discount",bg="white")
customer_pack_id_label=Label(frame1, text="pack_id",bg="white")
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


button1=Button(window, text="add a customer", bg="blue",width=30,fg="white", command=add_a_customer) .place(x=220, y=50)

button2=Button(window, text="add a package",bg="blue", width=30,fg="white", command=add_a_package) .place(x=220, y=80)

button3=Button(window, text="update a package",bg="blue",fg="white", width=30) .place(x=220, y=110)

button4=Button(window, text="delete a customer",bg="blue",fg="white", width=30) .place(x=220, y=140)


















window.mainloop()