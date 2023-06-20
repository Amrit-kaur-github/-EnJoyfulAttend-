from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
# pip install mysql-connector-python
import mysql.connector
#pip install opencv-python
import cv2



class Student:
    # 2nd video images add krn lee dekhli dubara
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")

        # ================variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # first image
        # second image
        # third image
        #bg image
        img1 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\th (2).jfif")
        # img1 = img1.resize((1530,790), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width = 1530,height =800)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font = ("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530, height=45)
        
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10,y=60,width=1502,height=710)

        # left label Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("time new roman",20))
        Left_frame.place(x=10,y=20,width=670,height=650)

        img_left = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\student.jfif")
        img_left= img_left.resize((500,130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left,bg="white")
        f_lbl.place(x=5,y=0,width =650,height = 130)
        
        # current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course's Information",font=("time new roman",17))
        current_course_frame.place(x=10,y=135,width=650,height=130)
        
        #Department
        dep_label = Label(current_course_frame,text="Department:",font=("time new roman",13),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky = W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",13),state="readonly")
        dep_combo["values"]=("Select Department","IT","Civil","Mechnical","Medical and Bioscience")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2,pady=10,sticky =W)

        #course
        course_label = Label(current_course_frame,text="Course:",font=("time new roman",13),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky = W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",13),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2,pady=10,sticky =W)

        #year
        year_label = Label(current_course_frame,text="Year:",font=("time new roman",13),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky = W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",13),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2,pady=10,sticky =W)

        #Semester
        Semester_label = Label(current_course_frame,text="Semester:",font=("time new roman",13),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky = W)

        Semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",13),state="readonly")
        Semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3, padx=2,pady=10,sticky =W)

        # class's student information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class's Student information",font=("time new roman",17))
        class_student_frame.place(x=10,y=270,width=650,height=300)  #y = 135 upr

        #student id
        StudentId_label = Label(class_student_frame,text="Student Id",font=("time new roman",13),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky = W)
        StudentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width = 15,font=("time new roman",13))
        StudentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky = W)


        #STUDENT name
        StudentName_label = Label(class_student_frame,text="Student Name:",font=("time new roman",13),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky = W)
        StudentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width = 15,font=("time new roman",13))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky = W)

        #class division
        class_div_label = Label(class_student_frame ,text="Class Division:",font=("time new roman",13),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky = W)
        # class_div_label_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width = 15,font=("time new roman",13))
        # class_div_label_entry.grid(row=1,column=1,padx=10,pady=5,sticky = W)
        class_div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("time new roman",13),state="readonly",width=15)
        class_div_combo["values"]=("Select","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1, padx=2,pady=5,sticky =W)

        #Roll No.
        roll_no_label = Label(class_student_frame ,text="Roll No.:",font=("time new roman",13),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky = W)
        roll_no_label_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width = 15,font=("time new roman",13))
        roll_no_label_entry.grid(row=1,column=3,padx=10,pady=5,sticky = W)

        #Gender
        gender_label = Label(class_student_frame ,text="Gender:",font=("time new roman",13),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky = W)
        # gender_label_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender,width = 15,font=("time new roman",13))
        # gender_label_entry.grid(row=2,column=1,padx=10,pady=5,sticky = W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("time new roman",13),state="readonly",width=15)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1, padx=2,pady=5,sticky =W)

        #Date Of Birth
        dob_label = Label(class_student_frame ,text="DOB:",font=("time new roman",13),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky = W)
        dob_label_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width = 15,font=("time new roman",13))
        dob_label_entry.grid(row=2,column=3,padx=10,pady=5,sticky = W)

        #Email
        email_label = Label(class_student_frame ,text="Email:",font=("time new roman",13),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky = W)
        email_label_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width = 15,font=("time new roman",13))
        email_label_entry.grid(row=3,column=1,padx=10,pady=5,sticky = W)

        #Phone No.
        phone_label = Label(class_student_frame ,text="Phone No:",font=("time new roman",13),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky = W)
        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width = 15,font=("time new roman",13))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky = W)

        #Address
        address_label = Label(class_student_frame ,text="Address:",font=("time new roman",13),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky = W)
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width = 15,font=("time new roman",13))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky = W)

        #teacer 
        teacher_label = Label(class_student_frame ,text="Teacher Name:",font=("time new roman",13),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky = W)
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width = 15,font=("time new roman",13))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky = W)
        #radio Buttons
        self.var_radio1=StringVar()
        Radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text = "Take Photo Sample", value="Yes")
        Radiobtn1.grid(row=6,column=0)

        Radiobtn2= ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text = "No Photo Sample", value="No")
        Radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame =Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height =70)

        save_btn= Button(btn_frame,text="Save",command=self.add_data,width = 15,font=("times new roman",13),bg ="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5)

        update_btn= Button(btn_frame,text="Update",command=self.update_data,width = 15,font=("times new roman",13),bg ="blue",fg="white")
        update_btn.grid(row=0,column=1,padx = 5)


        delete_btn= Button(btn_frame,text="Delete",command=self.delete_data,width = 15,font=("times new roman",13),bg ="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx = 5)

        reset_btn= Button(btn_frame,text="Reset",command=self.reset_data,width = 15,font=("times new roman",13),bg ="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx = 5)

        btn_frame1 =Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height =35)

        take_photo_btn= Button(btn_frame1,text="Take Photo Sample",width = 33,font = ("times new roman",13),bg ="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx= 5,pady=1)

        update_photo_btn= Button(btn_frame1,text="Update Photo Sample",width =33,font = ("times new roman",13),bg ="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=5,pady=1)

        # right label Frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",20,"bold"))
        Right_frame.place(x=690,y=20,width=800,height=650)
        
        img_right = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\s.d.jfif")
        img_right= img_right.resize((720,130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame, image = self.photoimg_right,bg="white")
        f_lbl.place(x=5,y=0,width=720,height =130)

        # =======Search system=========
        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font = ("times new roman",13),bg="white")
        Search_frame.place(x=5,y=138,width=750,height=70)

        Search_label = Label(Search_frame,text="Search by =",font = ("times new roman",13),bg ="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo = ttk.Combobox(Search_frame,font=("time new roman",13),state="readonly",width = 15)
        Search_combo["values"]=("Select","Roll_no","Phone_no")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1, padx=2,pady=10,sticky =W)

        search_entry = ttk.Entry(Search_frame,width = 15,font=("time new roman",13))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky = W)

        search_btn = Button(Search_frame,text="Search",width = 14,font = ("times new roman",13),bg ="blue",fg="white")
        search_btn.grid(row=0,column=3,padx= 5,pady=5)

        showall_btn= Button(Search_frame,text="Show all",width = 14,font = ("times new roman",13),bg ="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx= 5,pady=5)

        # =========table frame=============
        table_frame =Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=213,width=780,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text ="Department")
        self.student_table.heading("course",text ="Course")
        self.student_table.heading("year",text ="Year")
        self.student_table.heading("sem",text ="Semester")
        self.student_table.heading("id",text ="StudentId")
        self.student_table.heading("name",text ="Name")
        self.student_table.heading("div",text ="Division")
        self.student_table.heading("roll",text ="Roll no")
        self.student_table.heading("gender",text ="Gender")
        self.student_table.heading("dob",text ="DOB")
        self.student_table.heading("email",text ="Email")
        self.student_table.heading("phone",text ="Phone")
        self.student_table.heading("address",text ="Address")
        self.student_table.heading("teacher",text ="Teacher")
        self.student_table.heading("photo",text ="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # -=====================function deeclaration==========
    def add_data(self):
           print("entered in addd function")
           if (self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==""):
                messagebox.showerror("Error","All fields are required",parent = self.root)
           else:
                try:#messagebox.showinfo("Sucess","Welcome to CodewithAmrit")
                    conn=mysql.connector.connect(host="localhost",user="root",password="mysqlworkbench123",database="face_recognizer")
                    my_cursor = conn.cursor()
                    print("login ho gea mysqlworkbench ch")
                    my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (  
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(), # eh cut dena address mai ...pwd,category
                            self.var_teacher.get(),
                            self.var_radio1.get()
                    ))
                    print("data add ho rea")                    
                    conn.commit()
                    print("data commit ho gea")
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","student details has been added Successfully",parent = self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent =self.root)
        # =======fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mysqlworkbench123",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =========get cursor=============
    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()
        content =self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update_function
    def update_data(self):
        print("Update button clicked")
        if(self.var_dep.get()=="Select Deparment" or self.var_std_name.get()=="" or self.var_std_id.get()==""):
                messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
             try:
                Update = messagebox.askyesno("Update","Do you want to update this student's details")
                if Update>0:
                    print("LOCAL HOST TE GEA")
                    conn=mysql.connector.connect(host ="localhost",username="root",password="mysqlworkbench123",database="face_recognizer")
                    print("login ho gea mysqlworkbench ch")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Name=%s, `RollNo`=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSampleStatus=%s WHERE StudentId=%s", 
                         (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                                                                                                
                else:
                     if not Update:
                          return
                messagebox.showerror("Success","Students detail succesfully updated completed",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
             except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        ##############   Delete Function #######################33

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Permission Required","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root" , password="mysqlworkbench123", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                    
                
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Details successfully deleted",parent=self.root)
                
            
            except Exception as es:
                messagebox.showerror("Error","Student Id required",parent=self.root)
    ################  Reset Function  #####################
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select")
        self.var_rollNo.set("")
        self.var_gender.set("Select Gender")        
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("Select")
        self.var_radio1.set("")
           
                   


        





            

          
             




if __name__ == "__main__":
            root=Tk()
            obj= Student(root)
            root.mainloop()