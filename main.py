from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from student import Student


class face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # #first image x= 0 , 500,1000
        # #eh ni sahi lgri mnu
        # img = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\facerecognition.jfif")
        # img = img.resize((500,130), Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width = 500,height = 130)

        #bg image
        img1 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\th.jfif")
        img1 = img1.resize((1530,790), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width = 1530,height = 790)

        title_lbl = Label(bg_img,text="FACE RECOGNITION AND ATTENDANCE SYSTEM",font = ("times new roman",35,"bold"),bg="white",fg="RED")
        title_lbl.place(x=0,y=0,width=1530, height=45)


        #student button1
        img2 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\s.d.jfif")
        # img2 = img2.resize((1530,790), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1= Button(bg_img,image=self.photoimg2,command = self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width =220,height = 220)

        b1_1= Button(bg_img,text = "Student Details",command = self.student_details,cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width =220,height = 40)


        #Detect Face button2
        img3 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\facerecognition.jfif")
        # img2 = img2.resize((1530,790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3) 
         
        b2= Button(bg_img,image=self.photoimg3,cursor="hand2")
        b2.place(x=500,y=100,width =220,height = 220)

        b2_1= Button(bg_img,text = "Face Detector",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width =220,height = 40)


        #Attendance button2
        img4 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\attend1.jfif")
        # img4 = img4.resize((1530,790), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4) 
         
        b3= Button(bg_img,image=self.photoimg4,cursor="hand2")
        b3.place(x=800,y=100,width =220,height = 220)

        b3_1= Button(bg_img,text = "Attendance",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width =220,height = 40)


        #chatbot button2
        img5 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\chatbot3.jfif")
        # img5 = img5.resize((1530,790), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5) 
         
        b4= Button(bg_img,image=self.photoimg5,cursor="hand2")
        b4.place(x=1100,y=100,width =220,height = 220)

        b4_1= Button(bg_img,text = "Help Desk",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width =220,height = 40)


        #Train Data button2
        img6 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\train.jfif")
        # img6 = img6.resize((1530,790), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6) 
         
        b5= Button(bg_img,image=self.photoimg6,cursor="hand2")
        b5.place(x=200,y=380,width =220,height = 220)

        b5_1= Button(bg_img,text = "Train Data",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width =220,height = 40)


        #photos button
        img7 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\th (10).jfif")
        # img7 = img6.resize((1530,790), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7) 
         
        b6= Button(bg_img,image=self.photoimg7,cursor="hand2")
        b6.place(x=500,y=380,width =220,height = 220)

        b6_1= Button(bg_img,text = "Photos",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width =220,height = 40)


        #Developer button
        img9 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\developer.jfif")
        # img9 = img9.resize((1530,790), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9) 
         
        b8= Button(bg_img,image=self.photoimg9,cursor="hand2")
        b8.place(x=800,y=380,width =220,height = 220)

        b8_1= Button(bg_img,text = "Developer",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=800,y=580,width =220,height = 40)


        #Exit button
        img8 = Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\exit.jfif")
        # img8 = img8.resize((1530,790), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8) 
         
        b7= Button(bg_img,image=self.photoimg8,cursor="hand2")
        b7.place(x=1100,y=380,width =220,height = 220)

        b7_1= Button(bg_img,text = "Exit",cursor="hand2",font = ("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=1100,y=580,width =220,height = 40)


        # ===========================function button 3rd vid============
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Student(self.new_window)

        









if __name__ == "__main__":
    root=Tk()
    obj= face_recognition_system(root)
    root.mainloop()
