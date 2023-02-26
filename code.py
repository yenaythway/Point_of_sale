from tkinter import *
import random,os
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tempfile

dtl = []
class Pos:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("POS System")

        # self.category_list={'title':['Select Option','Laptop','Phone'],
        #                     'Laptop':{'name':['Acer','Lenovo','Dell','MSC','Mac book'],'price':[4000,7000,5000,6000,7000]},
        #                     'Phone':{'name':['Samsung','Huawei','I phone','Mi','Redmi','Xiomi','Mi'],'price':[4000,7000,5000,6000,7000]}}
        # self.one={}
        # self.two={}
        # double=[self.category_list,self.one,self.two]
        # title=['Select Option','Laptop','Phone']
        # cate=[['Select Option','Laptop','Phone'],['Acer','Lenovo','Dell','MSC','Mac book'],[4000,7000,5000,6000,7000],['Samsung','Huawei','I phone','Mi','Redmi','Xiomi','Mi'],[4000,7000,5000,6000,7000]]

        self.c_name=StringVar()
        self.c_phno=StringVar()
        self.c_address=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.txt_input=StringVar()
        self.total=StringVar()

        self.categorytxt = ['Select Option', 'Laptop', 'Phone']
        self.subcatlap = ['Acer', 'Lenovo', 'Dell', 'Mac book']
        self.acer_price = 50000
        self.lenovo_price = 60000
        self.dell_price = 70000
        self.mac_price = 80000
        self.subcatph = ['Samsung', 'Huawei', 'I phone', 'Redmi']
        self.sam_price = 50000
        self.huawei_price = 60000
        self.i_price = 70000
        self.red_price = 80000
        self.color=['white','black','silver']

        # mainframe
        mainframe = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        mainframe.place(x=0, y=175, width=1530, height=620)
        #image
        wood = Image.open("C:\\Users\\Acer Swift 3\\Downloads\\wood.png")
        wood = wood.resize((1908,170), Image.LANCZOS)
        self.wood = ImageTk.PhotoImage(wood)
        wood_lbl=Label(self.root,image=self.wood)
        wood_lbl.place(x=0,y=0,)
        b = Image.open("C:\\Users\\Acer Swift 3\\Downloads\\wood.png")
        b = b.resize((997, 330), Image.LANCZOS)
        self.b = ImageTk.PhotoImage(b)
        b_lbl = Label(self.root, image=self.b)
        b_lbl.place(x=3, y=328, )
        # customer_detail_frame
        customerframe = LabelFrame(mainframe, text="Customer detail", font=("times new roman", 12, "bold"), bg="white",fg="grey")
        customerframe.place(x=10, y=5, width=350, height=140)
        cu_detail = ["Name", "Address", "Phone Number"]
        vlist=[self.c_name,self.c_address,self.c_phno]

        for j in range(0, 3):
            self.cu_detil = Label(customerframe, text=cu_detail[j], font=("times new roman", 12, "bold"), bg="white")
            self.cu_detil.grid(row=j, column=0, sticky=W, pady=2)
            self.entry = ttk.Entry(customerframe,textvariable=vlist[j], font=("times new roman", 12, "bold"), width=24)
            # dtl.append(self.entry.get())
            self.entry.grid(row=j, column=1)

        # product detail frame
        productframe = LabelFrame(mainframe, text="Product Detail", font=("times new roman", 12, "bold"), bg="white",fg="grey")
        productframe.place(x=370, y=5, width=620, height=140)

        #category
        self.category = Label(productframe, font=('arial', 12, 'bold'), bg='white', text='Select Categories', bd=4)
        self.category.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.combo_category = ttk.Combobox(productframe, values=self.categorytxt, font=('arial', 10, 'bold'), width=24,state='readonly')
        self.combo_category.current(0)
        self.combo_category.grid(row=0, column=1)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)
        #subcategory
        self.subcategory = Label(productframe, font=('arial', 12, 'bold'), bg='white', text='Sub category', bd=4)
        self.subcategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.combo_subcategory = ttk.Combobox(productframe,textvariable=self.product, values=[''], font=('arial', 10, 'bold'), width=24,state='readonly')
        self.combo_subcategory.current(0)
        self.combo_subcategory.grid(row=1, column=1)
        self.combo_subcategory.bind("<<ComboboxSelected>>", self.Price)
        #color
        self.category2 = Label(productframe, font=('arial', 12, 'bold'), bg='white', text="Color", bd=4)
        self.category2.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.combo_category2 = ttk.Combobox(productframe, values=self.color, font=('arial', 10, 'bold'), width=24,state='readonly')
        self.combo_category2.current(0)
        self.combo_category2.grid(row=2, column=1)
        #price
        self.price_lbl = Label(productframe, font=('arial', 12, 'bold'), bg='white', text="Price", bd=4)
        self.price_lbl.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        self.combo_price = ttk.Combobox(productframe,textvariable=self.prices, font=('arial', 10, 'bold'), width=24, state='readonly')
        self.combo_price.grid(row=1, column=3)
        #qty
        self.qty_lbl = Label(productframe, font=('arial', 12, 'bold'), bg='white', text="Qty", bd=4)
        self.qty_lbl.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        self.combo_qty = ttk.Combobox(productframe,textvariable=self.qty, font=('arial', 10, 'bold'), width=24, state='readonly')
        self.combo_qty.grid(row=2, column=3)

        # bill frame
        billframe = LabelFrame(mainframe, text="Billing area", font=("times new roman", 12, "bold"), bg="white",
                               fg="grey")
        billframe.place(x=1000, y=45, width=480, height=440)
        scroll = Scrollbar(billframe, orient=VERTICAL)
        self.textarea = Text(billframe, yscrollcommand=scroll.set, bg="white", font=("times new roman", 12, "bold"))
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # bill counter frame
        billcounterframe = LabelFrame(mainframe, text="Bill counter", font=("times new roman", 12, "bold"), bg="white",
                                      fg="grey")
        billcounterframe.place(x=0, y=485, width=1520, height=120)
        bill = ["Sub Total", "Government Tax", "Total"]
        textvr=[self.sub_total,self.txt_input,self.total]
        for j in range(0, 3):
            self.cu_detil = Label(billcounterframe, text=bill[j], font=("times new roman", 12, "bold"), bg="white")
            self.cu_detil.grid(row=j, column=0, sticky=W, pady=2)
            self.entry = ttk.Entry(billcounterframe,textvariable=textvr[j], font=("times new roman", 12, "bold"), width=24)
            self.entry.grid(row=j, column=1)

        # buttonFrame
        buttonframe = Frame(billcounterframe, bd=2, )
        buttonframe.place(x=420, y=10)
        btlist = ['Add to cart','Generate Bill', 'Save', 'Clear']#,'Print'
        com_list=[self.AddItem,self.gen_bill,self.save_bill,self.clear]#,self.iprint()
        for i in range(0, 4):
            self.cart_b = Button(buttonframe,command=com_list[i], height=2, width=20, cursor="hand2", text=btlist[i],
                                 font=('arial', 15, 'bold'), bg="black", fg="white")
            self.cart_b.grid(row=0, column=i)

        # search
        searchframe = Frame(mainframe, bd=2, bg="white")
        searchframe.place(x=1020, y=5, width=500, height=40)

        self.billnumber = Label(searchframe, font=('arial', 10, 'bold'), fg='black', bg='grey', text="Bill Number", )
        self.billnumber.grid(row=0, column=0, sticky=W, padx=1)

        self.searchentry = ttk.Entry(searchframe,textvariable=self.search_bill, font=('arial', 10, 'bold'), width=30)
        self.searchentry.grid(row=0, column=1)

        self.searchbt = Button(searchframe, height=1, cursor="hand2", text="Search", font=('arial', 10, 'bold'),
                               bg="black", fg="white",command=self.find_bill, )
        self.searchbt.grid(row=0, column=2, padx=2)
        self.l = []
        self.welcome()

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"

        if found=='no':
            messagebox.showerror("Error","Invalid BIill No")


    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the product name")
        else:
            self.textarea.insert(END,f"\n\t{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            #self.txt_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.txt_input.set(str('Rs.%.2f' % ((sum(self.l)*0.05))))
            self.total.set(str('Rs.%.2f' % (((sum(self.l) +(sum(self.l) * 0.05))))))
            # self.total.set(str('Rs.%.2f'%(((sum(self.l)+((((sum(self.l))-(self.prices.get()))*Tax)/100))))))

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do u want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open(str("C:\\Users\\Acer Swift 3\\PycharmProjects\\posimage\\venv\\bills\\"+self.bill_no.get()+'.txt'),"w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()
    def iprint(self):
         pass
        # q=self.textarea.get(1.0,"end-1c")
        # filename=tempfile.mktemp('.txt')
        # open(filename,"w").write(q)
        # os.startfile(filename,"print")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phno.set("")
        self.c_address.set("")
        self.product.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.l=[0]
        self.search_bill.set("")
        self.prices.set("")
        self.qty.set("")
        self.total.set("")
        self.sub_total.set("")
        self.txt_input.set("")
        self.welcome()
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\n\t\t Welcome Royal Pos System")
        self.textarea.insert(END, f"\n\n\tBill Number\t\t: {self.bill_no.get()}")
        self.textarea.insert(END, f"\n \tCustomer Name\t\t: {self.c_name.get()}")
        self.textarea.insert(END, f"\n \tPhone NUmber\t\t: {self.c_phno.get()}")#
        self.textarea.insert(END, f"\n \tAddress\t\t: {self.c_address.get()}")#
        self.textarea.insert(END,"\n \t=======================================")
        self.textarea.insert(END, "\n\tProduct Name \t\tQTY\t\tPrice")
        self.textarea.insert(END, "\n\t=======================================")

    def gen_bill(self):
        if self.product.get()=="" :
            messagebox.showerror("Error","Please select the product name")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n \t=======================================")
            self.textarea.insert(END, f"\n \tSub Amount:\t\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n \tTax Amount:\t\t\t\t{self.txt_input.get()}")
            self.textarea.insert(END, f"\n \tTotal Amount:\t\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n \t=======================================")

    def Categories(self,event=""):
        if self.combo_category.get()=='Laptop':
            self.combo_subcategory.config(values=self.subcatlap)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=='Phone':
            self.combo_subcategory.config(values=self.subcatph)
            self.combo_subcategory.current(0)


    def Price(self,event=""):
        #laptop
        if self.combo_subcategory.get()=="Acer":
            self.combo_price.config(values=self.acer_price)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_subcategory.get()=="Lenovo":
            self.combo_price.config(values=self.lenovo_price)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_subcategory.get()=="Dell":
            self.combo_price.config(values=self.dell_price)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_subcategory.get()=="Mac book":
            self.combo_price.config(values=self.mac_price)
            self.combo_price.current(0)
            self.qty.set(1)
        #phone
        if self.combo_subcategory.get()=="Samsung":
            self.combo_price.config(values=self.sam_price)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_subcategory.get()=="Huawei":
            self.combo_price.config(values=self.huawei_price)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_subcategory.get()=="I phone":
            self.combo_price.config(values=self.i_price)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_subcategory.get()=="Redmi":
            self.combo_price.config(values=self.red_price)
            self.combo_price.current(0)
            self.qty.set(1)
        # save = Image.open("C:\\Users\\Acer Swift 3\\Downloads\\save.png")
        # clear = Image.open("C:\\Users\\Acer Swift 3\\Downloads\\clear.png")
        # cart = Image.open("C:\\Users\\Acer Swift 3\\Downloads\\cart.png")
        # save = save.resize((80, 80), Image.LANCZOS)
        # clear = clear.resize((80, 80), Image.LANCZOS)
        # self.cart = cart.resize((10, 10), Image.LANCZOS)
        # save = ImageTk.PhotoImage(save)
        # clear = ImageTk.PhotoImage(clear)
        # self.cart = ImageTk.PhotoImage(cart)
        # self.cart_b = Button(mainframe, image=self.cart, height=80, width=80, ).place(x=100,y=300,)
        # clear_b = Button(mainframe, image=clear, height=280, width=190, ).grid(row=1, column=1, padx=5, pady=5)
        # save_b = Button(mainframe, image=save, height=280, width=190, ).grid(row=1, column=1, padx=5, pady=5)


# cart/save bill/clear/


if __name__ == '__main__':
    root = Tk()
    obj = Pos(root)
    root.mainloop()
