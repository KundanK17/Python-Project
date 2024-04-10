from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime

root=Tk()
root.geometry("1350x850")
root.title("Online Trip Booking System")
root.configure(background="dark blue")

def Exit():
    qExit=messagebox.askyesno("Trip Bokking System","Do you want to Exit the System")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    TicketNum.set('')
    Tax.set('')
    SubTotal.set('')
    TotalCost.set('')
    CustomerName.set('')
    CustomerMob.set('')
    CustomerEmail.set('')
    TimeofOrder.set('')
    DateofOrder.set('')
    CostofAdult.set(0)
    CostofChild.set(0)
    CostofSenior.set(0)
    CostofConcession.set(0)
    UnitPriceAdult.set(0)
    UnitPriceChild.set(0)
    UnitPriceSenior.set(0)
    UnitPriceConcession.set(0)
    QtyAdult.set(0)
    QtyChild.set(0)
    QtySenior.set(0)
    QtyConcession.set(0)
    CardNum.set('')
    CardValidity.set('')
    Discount.set(0)
    cmdMethodofPayment.set('Other')

def TicketRef():
    Refpay = random.randint(10300,709467)
    Refpaid = ('ORD' + str(Refpay))
    TicketNum.set(Refpaid)

def CostofOrder():
    Qty1=float(QtyAdult.get())
    Qty2=float(QtyChild.get())
    Qty3=float(QtySenior.get())
    Qty4=float(QtyConcession.get())

    UnitPrice1=float(UnitPriceAdult.get())
    UnitPrice2=float(UnitPriceChild.get())
    UnitPrice3=float(UnitPriceSenior.get())
    UnitPrice4=float(UnitPriceConcession.get())

    CostofCategory1='$ '+str('%2f'%(Qty1*UnitPrice1))
    CostofCategory2='$ '+str('%2f'%(Qty2*UnitPrice2))
    CostofCategory3='$ '+str('%2f'%(Qty3*UnitPrice3))
    CostofCategory4='$ '+str('%2f'%(Qty4*UnitPrice4))

    CostofAdult.set(CostofCategory1)
    CostofChild.set(CostofCategory2)
    CostofSenior.set(CostofCategory3)
    CostofConcession.set(CostofCategory4)

    AllItemCost=((Qty1*UnitPrice1)+(Qty2*UnitPrice2)+(Qty3*UnitPrice3)+(Qty4*UnitPrice4))
    AppliedDiscount=float(Discount.get())
    DiscountonAllItem=(AllItemCost*(AppliedDiscount/100))
    CostAfterDiscount=AllItemCost-DiscountonAllItem

    TaxonAllItem = '$ ' + str('%.2f'%((CostAfterDiscount)*0.05))
    Tax.set(TaxonAllItem)

    SubTotalp = '$ ' + str('%.2f'%(AllItemCost))
    SubTotal.set(SubTotalp)

    TotalCostp = '$ ' + str('%.2f'%(CostAfterDiscount+((CostAfterDiscount)* 0.05)))
    TotalCost.set(TotalCostp)

    TicketRef()
    return

def TicketReceipt():
    root1 = Tk()
    root1.geometry("500x390")
    root1.title("Trip Ticket Receipt")
    root1.configure(background="light blue")

    txtTicketDetail = Text(root1,font=('arial',10,'bold'),fg='dark blue',bg='light yellow')
    txtTicketDetail.grid(row=0,column=0)

    #txtTicketDetail.insert(END,''+'\n')
    txtTicketDetail.insert(END,'Customer Name : ' + CustomerName.get() + '\t\t\t\t' + 'Mob : ' + CustomerMob.get() + '\t\t' + 'Email:' + CustomerEmail.get() + '\n')
    txtTicketDetail.insert(END,'Ticket No:' + TicketNum.get() + '\t\t\t\t'+'Time:'+ TimeofOrder.get()+'\t\t'+'Date:'+DateofOrder.get()+'\n')
    txtTicketDetail.insert(END,'=============================================================================='+'\n')

    txtTicketDetail.insert(END,'Ticket Category:\t\t\t'+'Qty:\t\t\t'+'Unit Price:\t\t\t'+'\n')
    txtTicketDetail.insert(END,'Adult:\t\t\t'+QtyAdult.get()+'\t\t\t'+UnitPriceAdult.get()+'\t\t\t'+'\n')
    txtTicketDetail.insert(END,'==============================================================='+'\n')
    txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price:\t'+CostofAdult.get()+'\n')

    txtTicketDetail.insert(END,'Child:\t\t\t'+QtyChild.get()+'\t\t\t'+UnitPriceChild.get()+'\t\t\t'+'\n')
    txtTicketDetail.insert(END,'==============================================================='+'\n')
    txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price:\t'+CostofChild.get()+'\n')

    txtTicketDetail.insert(END,'Senior:\t\t\t'+QtySenior.get()+'\t\t\t'+UnitPriceSenior.get()+'\t\t\t'+'\n')
    txtTicketDetail.insert(END,'==============================================================='+'\n')
    txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price:\t'+CostofSenior.get()+'\n'+'\n')

    txtTicketDetail.insert(END,'Prime:\t\t\t'+QtyConcession.get()+'\t\t\t'+UnitPriceConcession.get()+'\t\t\t'+'\n')
    txtTicketDetail.insert(END,'==============================================================='+'\n')
    txtTicketDetail.insert(END,'\t\t\t\t'+'Total Price:\t'+CostofConcession.get()+'\n'+'\n')

    txtTicketDetail.insert(END,'\t\t'+'SubTotal($): \t\t\t'+SubTotal.get()+'\n')
    txtTicketDetail.insert(END,'\t\t'+'Discount(in %): \t\t\t'+Discount.get()+'%'+'\n')
    txtTicketDetail.insert(END,'\t\t'+'Tax: \t\t\t'+Tax.get()+'\n')
    txtTicketDetail.insert(END,'\t\t'+'==============================================================='+'\n')
    txtTicketDetail.insert(END,'\t\t'+'Total Payable Price($): \t'+TotalCost.get()+'\n')

#=============================Define Variables====================================
TicketNum=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofAdult=StringVar()
CostofChild=StringVar()
CostofSenior=StringVar()
CostofConcession=StringVar()
CustomerName=StringVar()
CustomerMob=StringVar()
CustomerEmail=StringVar()
TimeofOrder=StringVar()
DateofOrder=StringVar()
Discount=StringVar()
UnitPriceAdult=StringVar()
UnitPriceChild=StringVar()
UnitPriceSenior=StringVar()
UnitPriceConcession=StringVar()
QtyAdult=StringVar()
QtyChild=StringVar()
QtySenior=StringVar()
QtyConcession=StringVar()
CardNum=StringVar()
CardValidity=StringVar()
Discount=StringVar()
                               
                            
#===========================Set Default Value of Component=========================
CostofAdult.set(0)
CostofChild.set(0)
CostofSenior.set(0)
CostofConcession.set(0)
UnitPriceAdult.set(0)
UnitPriceChild.set(0)
UnitPriceSenior.set(0)
UnitPriceConcession.set(0)
QtyAdult.set(0)
QtyChild.set(0)
QtySenior.set(0)
QtyConcession.set(0)
Discount.set(0)

#=========================Set Default Value of Date and Time Component===============
TimeofOrder.set(time.strftime('%H:%M:%S'))
DateofOrder.set(time.strftime('%d/%m/%Y'))

#=========================Frame Design=============================================
Tops=Frame(root, width=1350, height=50, bd=16, relief='raise')
Tops.pack(side=TOP)

LF=Frame(root, width=700, height=650, bd=16, relief='raise')
LF.pack(side=LEFT)

RF=Frame(root, width=600, height=650, bd=16, relief='raise')
RF.pack(side=RIGHT)

Tops.configure(background="dark blue")
LF.configure(background="dark blue")
RF.configure(background="dark blue")
#--------------------------------------------
LeftInsideLF=Frame(LF, width=700, height=100, bd=8, relief='raise', bg='yellow')
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=700, height=400, bd=8, relief='raise',bg='light blue')
LeftInsideLFLF.pack(side=LEFT)
#-----------------------------------------------
RightInsideLF=Frame(RF, width=604, height=300, bd=8, relief='raise', bg='light blue')
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=306, height=400, bd=8, relief='raise',bg='yellow')
RightInsideLFLF.pack(side=LEFT)            
RightInsideRFRF=Frame(RF, width=300, height=800, bd=8, relief='raise',bg='blue')
RightInsideRFRF.pack(side=RIGHT)

#============================Define Title===================
lblInfo=Label(Tops,font=('Century Schoolbook',50,'bold'),text="       Country Trip Booking System    ",
              fg='dark blue',bg='orange',bd=10,anchor='w')
lblInfo.grid(row=0,column=1)

#========================Top Left Frame=====================
lblCustomerName=Label(LeftInsideLF, font=('arial',14,'bold'),text='Client Name',
                      bg='yellow',fg='blue',bd=10,anchor='w')
lblCustomerName.grid(row=0,column=0)

txtCustomerName=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                      bg='white',justify='left',textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lblCustomerMob=Label(LeftInsideLF,font=('arial',14,'bold'),text='Contact',bg='yellow',fg='blue',bd=10,anchor='w')
lblCustomerMob.grid(row=1,column=0)

txtCustomerMob=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                      bg='white',justify='left',textvariable=CustomerMob)
txtCustomerMob.grid(row=1,column=1)

lblCustomerEmail=Label(LeftInsideLF,font=('arial',14,'bold'),text='Email',bg='yellow',fg='blue',bd=10,anchor='w')
lblCustomerEmail.grid(row=2,column=0)

txtCustomerEmail=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                      bg='white',justify='left',textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)

#=====================Top Right Frame==========================
lblDateofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text='Date',bg='light blue',fg='blue',bd=10,anchor='w')
lblDateofOrder.grid(row=0,column=0)

txtDateofOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                      bg='white',justify='left',textvariable=DateofOrder)
txtDateofOrder.grid(row=0,column=1)

lblTimeofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text='Time',bg='light blue',fg='blue',bd=10,anchor='w')
lblTimeofOrder.grid(row=1,column=0)

txtTimeofOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                      bg='white',justify='left',textvariable=DateofOrder)
txtTimeofOrder.grid(row=1,column=1)

lblTicketNumber=Label(RightInsideLF,font=('arial',12,'bold'),text='Ticket Receipt No.',bg='light blue',fg='blue',bd=10,anchor='w')
lblTicketNumber.grid(row=2,column=0)

txtTicketNumber=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                      bg='white',justify='left',textvariable=DateofOrder)
txtTicketNumber.grid(row=2,column=1)

#======================Bottom Right Frame============================
lblSubTotal=Label(RightInsideLFLF,font=('arial',12,'bold'),text='SubTotal($)',bg='yellow',fg='blue',bd=16,anchor='w')
lblSubTotal.grid(row=0,column=0)

txtSubTotal=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                      bg='white',justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=0,column=1)

lblDiscount=Label(RightInsideLF,font=('arial',12,'bold'),text='-Discount(%)',bg='yellow',fg='blue',bd=16,anchor='w')
lblDiscount.grid(row=1,column=0)

txtDiscount=Entry(RightInsideLF,font=('arial',12,'bold'),bd=16,width=18,
                      bg='white',justify='left',textvariable=Discount)
txtDiscount.grid(row=1,column=1)

lblTax=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Tax(5% value)',bg='yellow',fg='blue',bd=16,anchor='w')
lblTax.grid(row=2,column=0)

txtTax=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                      bg='white',justify='left',textvariable=Tax)
txtTax.grid(row=2,column=1)

lblTotalCost=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Total Cost($)',bg='yellow',fg='blue',bd=16,anchor='w')
lblTotalCost.grid(row=3,column=0)

txtTotalCost=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                      bg='white',justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=3,column=1)

lblMethodofPayment=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Mode of Payment',bg='yellow',fg='blue',bd=16,anchor='w')
lblMethodofPayment.grid(row=4,column=0)
cmdMethodofPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodofPayment['value']=('Other','Cash on Delivery','Debit Card','Visa Card','Master Card')
cmdMethodofPayment.grid(row=4,column=1)
cmdMethodofPayment.set('Other')

lblCardNum=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Card Ref.(14 digit)',bg='yellow',fg='blue',bd=16,anchor='w')
lblCardNum.grid(row=5,column=0)

txtCardNum=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,bg='white',justify='left',textvariable=CardNum)
txtCardNum.grid(row=5,column=1)

lblCardValidity=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Card Validity(MM/YYYY)',bg='yellow',fg='blue',bd=16,anchor='w')
lblCardValidity.grid(row=6,column=0)

txtCardValidity=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                      bg='white',justify='left',textvariable=CardValidity)
txtCardValidity.grid(row=6,column=1)

#========================Bottom Left Frame==========================
lblTicket=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Ticket',bg='light blue',fg='blue',bd=20)
lblTicket.grid(row=0,column=0)

lblQty=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Quantity',bg='light blue',fg='blue',bd=10)
lblQty.grid(row=0,column=1)

lblUnitPrice=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Unit Cost($)',bg='light blue',fg='blue',bd=20)
lblUnitPrice.grid(row=0,column=2)

lblCostofTicket=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Total Cost($)',bg='light blue',fg='blue',bd=20)
lblCostofTicket.grid(row=0,column=3)

#========================
lblAdult=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Adult',bg='light blue',fg='blue',bd=20)
lblAdult.grid(row=1,column=0)

lblChild=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Child',bg='light blue',fg='blue',bd=20)
lblChild.grid(row=2,column=0)

lblSenior=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Senior',bg='light blue',fg='blue',bd=20)
lblSenior.grid(row=3,column=0)

lblConcession=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Concession',bg='light blue',fg='blue',bd=20)
lblConcession.grid(row=4,column=0)

#===========================
txtQtyAdult=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtyAdult)
txtQtyAdult.grid(row=1,column=1)

txtQtyChild=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtyChild)
txtQtyChild.grid(row=2,column=1)

txtQtySenior=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtySenior)
txtQtySenior.grid(row=3,column=1)

txtQtyConcession=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=QtyConcession)
txtQtyConcession.grid(row=4,column=1)

#================================
txtUnitPriceAdult=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceAdult)
txtUnitPriceAdult.grid(row=1,column=2)

txtUnitPriceChild=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceChild)
txtUnitPriceChild.grid(row=2,column=2)

txtUnitPriceSenior=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceSenior)
txtUnitPriceSenior.grid(row=3,column=2)

txtUnitPriceConcession=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=UnitPriceConcession)
txtUnitPriceConcession.grid(row=4,column=2)
#===========================
txtCostofAdult=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostofAdult)
txtCostofAdult.grid(row=1,column=3)

txtCostofChild=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostofChild)
txtCostofChild.grid(row=2,column=3)

txtCostofSenior=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostofSenior)
txtCostofSenior.grid(row=3,column=3)

txtCostofConcession=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,bg='white',justify='left',textvariable=CostofConcession)
txtCostofConcession.grid(row=4,column=3)

#=====================Bottom Right frame==========================
btnTotalCost=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Total Cost',bg='light blue',command=CostofOrder).grid(row=0,column=0)
btnReset=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Reset',bg='light blue',command=Reset).grid(row=1,column=0)
btnTicketReceipt=Button(RightInsideRFRF,pady=10,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Receipt',bg='light blue',command=TicketReceipt).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=5,bd=5,fg='blue',font=('arial',16,'bold'),width=11,text='Exit',bg='light blue',command=Exit).grid(row=3,column=0)

root.mainloop()

