from tkinter import *
from tkinter import filedialog

import qrcode
from PIL import Image , ImageTk
from resizeimage import resizeimage
class Qr__genrator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("Qr Generator")
        self.root.resizable(False,False)
        title=Label(self.root,text="  QR Generator",font=("sans-serif",30),bg="pink",fg="black").place(x=0,y=0,relwidth=1)
        #employee details================
        self.var_emp_code=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_department=StringVar()
        self.var_emp_designation=StringVar()


        emp_frame=Frame(self.root,bd=2 , relief=RAISED ,bg="white")
        emp_frame.place(x=50,y=100 , width=500, height=380)
        emp_title=Label(emp_frame,text=" Employee Details",font=("goudy old style",20),bg="blue", fg="white")
        emp_title.place(x=0,y=0, relwidth=1 )
        #lables of emp frame

        lbl_emp_code=Label(emp_frame,text="Employee ID ",font=("times new roman",15,"bold"),bg="white").place(x=20,y= 60)
        lbl_emp_name=Label(emp_frame,text="Name ",font=("times new roman",15,"bold"),bg="white").place(x=20,y=100)
        lbl_emp_department=Label(emp_frame,text="Department ",font=("times new roman",15,"bold"),bg="white").place(x=20,y=140)
        lbl_emp_designation=Label(emp_frame,text="Designation ",font=("times new roman",15,"bold"),bg="white").place(x=20,y=180)

        #ENTry field of emp frame

        txt_emp_code=Entry(emp_frame,text="Employee ID ",font=("times new roman",15),textvariable=self.var_emp_code,bg="yellow").place(x=200,y= 60)
        txt_emp_name=Entry(emp_frame,text="Name ",font=("times new roman",15),textvariable=self.var_emp_name,bg="yellow").place(x=200,y=100)
        txt_emp_department=Entry(emp_frame,text="Department ",font=("times new roman",15),textvariable=self.var_emp_department,bg="yellow").place(x=200,y=140)
        txt_emp_designation=Entry(emp_frame,text="Designation ",font=("times new roman",15 ),textvariable=self.var_emp_designation,bg="yellow").place(x=200,y=180)

        #buttons
        btn_genterator=Button(emp_frame,text="QR Generate",command=self.generate, font=("times new roman",16,"bold",),bg="lightblue").place(x=80,y=250,width=200,height=25)
        btn_clear=Button(emp_frame,text="Clear",command=self.clear, font=("times new roman",16,"bold",),bg="lightblue").place(x=300,y=250,width=150,height=25)
        btn_save_qr = Button(emp_frame, text="Save QR Code", command=self.save_qr, font=("times new roman", 16, "bold",),
                             bg="lightblue").place(x=80, y=290, width=200, height=20)
        self.msg=''
        self.lbl_msg=Label(emp_frame,text=self.msg,font=("times new roman",18),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #qr details
        qr_frame=Frame(self.root,bd=2,relief=RAISED ,bg="white")
        qr_frame.place(x=560,y=100,width=300, height=380)
        qr_label=Label(qr_frame,text="Employee QR Code",font=("goudy old style",20),bg="blue",fg="white").place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_frame,text="No QR\n Available",font=("times new roman",15),bg="darkblue",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=50,y=80,width=180,height=180)

    #  this function save the generated qr code
    def save_qr(self):
        if self.var_emp_code.get() == '':
            self.msg = "Generate QR first!!!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if filename:
                self.im.save(filename)
                self.msg = "QR Code saved successfully!"
                self.lbl_msg.config(text=self.msg, fg="green")
   
    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')
        self.msg='Nothing to Clear'
        self.lbl_msg.config(text=self.msg,fg="red")
        self.im=Label(text="No QR\n Available",font=("times new roman",15),bg="darkblue",fg="white",bd=1,relief=RIDGE)
        self.im.place(x=610, y=183, width=180, height=180)
        self.im.config(text=self.im)


         
    def generate(self):
        if self.var_emp_code.get()=='' or self.var_emp_name.get()=='' or self.var_emp_department.get()=='' or self.var_emp_designation.get()=='' :
             self.msg="All fields are required!!!"
             self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Employee ID :{self.var_emp_code.get()}\nEmployee Name:{self.var_emp_name.get()}\nDepartment :{self.var_emp_department.get()}\nDesignation :{self.var_emp_designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180 ])
            qr_code.save("Employee QR/Emp_"+str(self.var_emp_code.get())+'.png')
            #Qr code image----------------------
            self.im=ImageTk.PhotoImage(file="Employee QR/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
           # #updating notification
            self.msg = "QR Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg, fg="green")

root=Tk()


obj=Qr__genrator(root)
root.wm_iconbitmap("accessories_text_editor.ico")

root.mainloop()
