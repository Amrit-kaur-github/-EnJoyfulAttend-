from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2



class Train:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET", font=("times new roman",35,"bold"),bg="white",fg="Red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\sMVYi.jpg")
        img_top=img_top.resize((1530,525),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        img_bottom=Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\1_3WCnoIgwKpdGR_CqbyDAVQ.jpg")
        img_bottom=img_bottom.resize((765,525),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        b_lbl=Label(self.root,image=self.photoimg_bottom)
        b_lbl.place(x=0,y=440,width=765,height=325)

        img_bottomr=Image.open(r"C:\Users\lenovo\OneDrive\Pictures\Saved Pictures\Screenshot 2023-06-22 122349.jpg")
        img_bottomr=img_bottomr.resize((765,525),Image.LANCZOS)
        self.photoimg_bottomr=ImageTk.PhotoImage(img_bottomr)

        br_lbl=Label(self.root,image=self.photoimg_bottomr)
        br_lbl.place(x=765,y=440,width=765,height=325)

        train_btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("rockwell",36,"bold"),bg="dark blue",fg="white")
        train_btn.place(x=0,y=340,width=1530,height=100)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('_')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training',imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)
        # ======================Train the classifier and save==========
        
        # clf=cv2.face.LBPHFaceRecognizer_create()
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
