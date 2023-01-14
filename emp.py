from tkinter import *
from tkinter import ttk
import pymysql
from requests import delete



class Employee:

        def __init__(self, root):

                self.root = root
                self.root.title("Employee Management System")
                self.root.geometry("1350x700+0+0")   # w - 1350 h - 700

                title = Label(self.root, text = 'Employee Management System', bd = 3, relief= GROOVE,  font= ("aharoni", 40, 'bold'), bg = "dark blue", fg= "white")
                title.pack(side = TOP, fill=X)

                ###variables#######

                self.emp_id = StringVar()
                self.fn = StringVar()
                self.ln = StringVar()
                self.gen = StringVar()
                #self.add = StringVar()
                self.sal = IntVar()         #to perform calc.
                self.dep_id = StringVar()

                CRUD_FRAME = Frame(self.root, bd = 2, relief= RIDGE)  #CAN ADD BG 
                CRUD_FRAME.place(x = 3, y = 73, width= 330 , height= 765)
                crud_title = Label(CRUD_FRAME, text = 'Manage Employees', font= ("aharoni", 23, 'bold'), fg= "dark blue")
                crud_title.grid(row=0, columnspan= 2, pady=3)

                #emp_id

                emp_id = Label(CRUD_FRAME, text = 'Employee ID:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                emp_id.grid(row=1, columnspan= 2, pady = 5, sticky="w")

                #emp_id_text box

                txt_emp_id = Entry(CRUD_FRAME, textvariable=self.emp_id , font= ("aharoni",14))
                txt_emp_id.grid(row=2, columnspan= 2, pady = 5)

                #firstname

                first_name = Label(CRUD_FRAME, text = 'Firstname:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                first_name.grid(row=3, columnspan= 2, pady = 5, sticky="w")

                txt_fn = Entry(CRUD_FRAME, textvariable= self.fn , font= ("aharoni",14))
                txt_fn.grid(row=4, columnspan= 2, pady = 5)

                #lastname

                ln = Label(CRUD_FRAME, text = 'Lastname:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                ln.grid(row=5, columnspan= 2, pady = 5, sticky="w")

                txt_ln = Entry(CRUD_FRAME, textvariable= self.ln,font= ("aharoni",14))
                txt_ln.grid(row=6, columnspan= 2, pady = 5)

                #Gender

                gen = Label(CRUD_FRAME, text = 'Gender:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                gen.grid(row=7, column= 0, pady = 5, sticky="w")

                #combo_box

                comb_gen = ttk.Combobox(CRUD_FRAME, textvariable= self.gen, font= ("aharoni",14), state='readonly')
                comb_gen['values'] = ("Male", "Female", "Other")
                comb_gen.grid(row = 8, columnspan= 2, pady = 5 )

                #address

                add = Label(CRUD_FRAME, text = 'Address:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                add.grid(row=9, columnspan= 2, pady = 5, sticky="w")

                self.txt_add = Text(CRUD_FRAME, width=22, height=3, font= ("aharoni",14))
                self.txt_add.grid(row=10, columnspan= 2, pady =5)

                #Salary

                sal = Label(CRUD_FRAME, text = 'Salary:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                sal.grid(row=11, columnspan= 2, pady = 5, sticky="w")  #sticky w to stick towards left

                txt_sal= Entry(CRUD_FRAME, textvariable= self.sal,font= ("aharoni",14))
                txt_sal.grid(row=12, columnspan= 2, pady = 5)

                #Department ID

                dep_id = Label(CRUD_FRAME, text = 'Department ID:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                dep_id.grid(row=13, columnspan= 2, pady = 10, sticky="w")

                txt_dep_id= Entry(CRUD_FRAME, textvariable= self.dep_id, font= ("aharoni",14))
                txt_dep_id.grid(row=14, columnspan= 2, pady = 5)

                #buttons

                Q_FRAME = Frame(CRUD_FRAME, bd = 2, relief = RIDGE)
                Q_FRAME.place(x = 3, y = 655, width= 320 , height=75)

                add_b = Button(Q_FRAME, text = 'Add', width = 8, command =  self.add_data ,height=3).grid(row = 0, column=0, pady =7, padx =7)
                up_b = Button(Q_FRAME, text = 'Update', width = 8, command = self.update_data, height=3).grid(row = 0, column=1, pady =7, padx =5)
                del_b = Button(Q_FRAME, text = 'Delete', width = 8, command = self.delete_data, height=3).grid(row = 0, column=2, pady =7, padx =5)
                clear_b = Button(Q_FRAME, text = 'Clear', width = 8, command = self.clear, height=3).grid(row = 0, column=3, pady =7, padx =7)





                INFO_FRAME = Frame(self.root, bd = 2, relief= RIDGE)
                INFO_FRAME.place(x = 335, y = 73, width= 1120 , height=765)

                info_title = Label(INFO_FRAME, text = 'Search By:', font= ("aharoni", 13, 'bold'), fg= "dark blue")
                info_title.grid(row=2, column= 0, pady=5, padx = 5 )

                comb_sb = ttk.Combobox(INFO_FRAME, font= ("aharoni",13), state='readonly')
                comb_sb['values'] = ("Employee ID", "Department ID", "Salary")
                comb_sb.grid(row = 2, column= 1, pady = 5, padx = 5 )

                txt_search= Entry(INFO_FRAME, font= ("aharoni",14))
                txt_search.grid(row=2, column= 2, pady = 5, padx = 5 )

                search_b = Button(INFO_FRAME, text = 'Search', width = 13, height=1).grid(row = 2, column=3, pady =5, padx =5)
                showall_b = Button(INFO_FRAME, text = 'Show All', width = 13, height=1).grid(row = 2, column=4, pady =5, padx =5)
                
                #TABLE DESIGN

                TABLE_FRAME = Frame(self.root, bd = 2, relief= RIDGE)
                TABLE_FRAME.place(x = 345, y = 120, width= 1100 , height=707)

                #SCROLL BAR

                scroll_x = Scrollbar(TABLE_FRAME, orient= HORIZONTAL)
                scroll_y = Scrollbar(TABLE_FRAME, orient= VERTICAL)


                #DESIGNING TABLE

                self.employee_table = ttk.Treeview(TABLE_FRAME, columns=("Employee ID","Firstname", "Lastname", "Gender", "Address", "Salary" ,"Department ID"), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set)
                scroll_x.pack(side=BOTTOM, fill= X)
                scroll_y.pack(side=RIGHT, fill= Y)

                #CONFIGURE

                scroll_x.config( command= self.employee_table.xview)
                scroll_y.config( command= self.employee_table.yview)

                #headings

                self.employee_table.heading("Employee ID", text = "Employee ID")
                self.employee_table.heading("Firstname", text = "Firstname")
                self.employee_table.heading("Lastname", text = "Lastname")
                self.employee_table.heading("Gender", text = "Gender")
                self.employee_table.heading("Address", text = "Address")
                self.employee_table.heading("Salary", text = "Salary")
                self.employee_table.heading("Department ID", text = "Department ID")

                #set h and width of columns

                self.employee_table.column("Employee ID", width=158)
                self.employee_table.column("Firstname", width=158)
                self.employee_table.column("Lastname", width=158)
                self.employee_table.column("Gender", width=158)
                self.employee_table.column("Address", width=158)
                self.employee_table.column("Salary", width=158)
                self.employee_table.column("Department ID", width=158)

                #remove the first empty column
                self.employee_table['show'] = 'headings'
                self.employee_table.pack(fill = BOTH, expand=1)

                #binding with the table- event handling

                self.employee_table.bind("<ButtonRelease-1>", self.fetch_data)

                #display previous data when we start the program

                self.display_data()
        
        def add_data(self):

                con = pymysql.connect(host = "localhost", user= "root", password="GwUgtD@123", database = "employee")
                cur = con.cursor()
                cur.execute("INSERT INTO employees values (%s,%s,%s,%s,%s,%s,%s)", 
                
                (
                        self.emp_id.get(),
                        self.fn.get(),
                        self.ln.get(),
                        self.gen.get(),
                        self.txt_add.get('1.0', END),  #FROM LINE 1 TO END
                        self.sal.get(),
                        self.dep_id.get()
                ))

                con.commit()
                self.display_data()
                self.clear()
                con.close()
        
        def display_data(self):    #display data on the table

                con = pymysql.connect(host = "localhost", user= "root", password="GwUgtD@123", database = "employee")
                cur = con.cursor()
                cur.execute("SELECT * FROM employees")
                rows_data = cur.fetchall()

                if len(rows_data) > 0:   #if entry is not empty

                        self.employee_table.delete(*self.employee_table.get_children())   #deleting all data

                        for row in rows_data:

                                self.employee_table.insert('', END, values = row)

                        con.commit()
                con.close()
        
        def clear(self):

                self.emp_id.set("")
                self.fn.set("")
                self.ln.set("")
                self.gen.set("")
                self.txt_add.delete("1.0", END)
                self.sal.set("")
                self.dep_id.set("")


        def fetch_data(self, ev):           #have to be binded with the employees table- event handling

                                                #for an event another argument has to b e provided, eve1 in this case

                cursor_row = self.employee_table.focus()    #to fetch data by placing a cursor on a row in a table
                fetched_data = self.employee_table.item(cursor_row)   #fetched data

                row = fetched_data['values']    #data fetched and stored in row variable


                self.emp_id.set(row[0])
                self.fn.set(row[1])
                self.ln.set(row[2])
                self.gen.set(row[3])
                self.txt_add.delete('1.0', END)
                self.txt_add.insert(END, row[4])
                self.sal.set(row[5])
                self.dep_id.set(row[6])

        def update_data(self):

                con = pymysql.connect(host = "localhost", user= "root", password="GwUgtD@123", database = "employee")
                cur = con.cursor()
                cur.execute("UPDATE employees set Firstname = %s,Lastame = %s, Gender = %s, Address = %s, Salary = %s, Department_ID = %s where Employee_ID = %s",( 
                
                        self.fn.get(),
                        self.ln.get(),
                        self.gen.get(),
                        self.txt_add.get('1.0', END),  #FROM LINE 1 TO END
                        self.sal.get(),
                        self.dep_id.get(),
                        self.emp_id.get()
                ))

                con.commit()
                self.display_data()
                self.clear()
                con.close()

        def delete_data(self):

                con = pymysql.connect(host = "localhost", user= "root", password="GwUgtD@123", database = "employee")
                cur = con.cursor()
                cur.execute("DELETE FROM employees WHERE Employee_ID = %s", self.emp_id.get())
                con.commit()
                con.close()
                self.display_data()
                self.clear()
                








if __name__=='__main__':

    root = Tk()    #Tkinter window is given as an input to the class as root
    object = Employee(root)
    root.mainloop()