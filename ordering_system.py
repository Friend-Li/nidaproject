##downloading imports/libraries/packages###
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
####Framing the website title/page####
root . Tk()
root.geometry ("1350x650+0+0")
root.title ("Online Ordering System")
root.configure (background.'pink')


root.mainloop()
###ExitFunction###
def Exit():
    qExit . messagebox.askyesno("Ordering System", "Do you want to exit this system?")
    if exit > 0:
        root.destroy()
        return

##ListOfVariables##
def Reset ():
##ListOfVariables##
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofNecklace.set("")
    CostofBracelet.set("")
    CostofEarrings.set("")
    CostofOtherJewlery.set("")
    #CostofBestFriendDeal2Necklaces.set("")
    #CostofBestFriendDealNecklaceandEarringSet.set("")
    #CostofBestFriendDeal2Bracelets.set("")
    #CostofBestFriendDeal2Earrings.set("")
    CostofDelivery.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    TimeofOrder.set("")
    DateofOrder.set("")
    Discount.set("")
    Tip.set("")
    CostofBestFriendDeal2Necklaces.set("")
    CostofBestFriendDealNecklaceandEarringSet.set("")
    CostofBestFriendDeal2Bracelets.set("")
    CostofBestFriendDeal2Earrings.set("")
    UnitPriceOtherJewlery.set("")
    UnitPriceNecklce.set("")
    UnitPriceBracelet.set("")
    UnitPriceEarrings.set("")
    QtyOtherJewlery.set("")
    QtyNecklace.set("")
    QtyBracelet.set("")
    QtyEarrings.set("")
    Discount.set("")

 ##Framing the whole table####   
Tops.Frame (root, width.1350, height.50, bd.16, relief."raise")
Tops.pack(side.TOP)
LF.Frame(root, width.700, height.650, bd.16, relief."raise")
LF.pack(side.LEFT)
RF.Frame(root,width.600, height.650,bd.16, relief."raise")
RF.pack(side.RIGHT) 

Tops.configure(background.'black')
LF.configure(background.'black')
RF.configure(background.'black')

LeftInsideLF.Frame(LF, width.700, height.100, bd.8, relief."raise")
LeftInsideLF.pack(side.TOP)
LeftInsideLFLF.Frame(LF, width.700, height.400, bd.8, relief."raise")
LeftInsideLFLF.pack(side.LEFT)

RightInsideLF.Frame(RF, width.604, height.200, bd.8, relief."raise")
RightInsideLF.pack(side.TOP)
RightInsideLFLF.Frame(RF, width.700, height.400, bd.8, relief."raise")
RightInsideLFLF.pack(side.LEFT)
RightInsideRFRF.Frame(RF, width.300, height.400, bd.8, relief."raise")
RightInsideRFRF.pack(side.RIGHT)

lblInfo . Label(Tops, font.('Playfair Display', 50, 'bold'), texts. "Online Ordering Systems", bd.20, anchor.'w')
lblInfo.grid(row.0, column.0)

####Top Left Frame###
lblCustomerName . Label (LeftInsideLF, font.('Liberata',14,'bold'),text.'Customer Name', fg.'black', bd.20, anchor.'w')
lblCustomerName.grid(row.0, column.0)
txtCustomerName . Entry(RightInsideLFLF, font.('Liberata', 14, 'bold'),bd.20, width.43, bg.'white', justify.'left', textvariable.CustomerName)
txtCustomerName.grid(row.0,column.1)
lblCustomerPhone . Label (LeftInsideLF, font.('Liberata',14,'bold'),text.'Customer Phone', fg.'black', bd.20, anchor.'w')
lblCustomerPhone.grid(row.1, column.0)
txtCustomerPhone . Entry(RightInsideLFLF, font.('Liberata', 14, 'bold'),bd.20, width.43, bg.'white', justify.'left', textvariable.CustomerPhone)
txtCustomerPhone.grid(row.1,column.1)
lblCustomerEmail . Label (LeftInsideLF, font.('Liberata',14,'bold'),text.'Customer Email', fg.'black', bd.20, anchor.'w')
lblCustomerEmail.grid(row.2, column.0)
txtCustomerEmail . Entry(RightInsideLFLF, font.('Liberata', 14, 'bold'),bd.20, width.43, bg.'white', justify.'left', textvariable.CustomerEmail)
txtCustomerName.grid(row.2,column.1)


####Top Right Frame###
lblDateofOrder.Label(RightInsideLF,font.('Liberata', 12, 'bold'), text.'DateofOrder',  fg . 'red', bd.10, anchor.'w')
lblDateofOrder.grid(row.0,column.0)
txtDateofOrder . Entry(RightInsideLFLF, font.('Liberata', 12, 'bold'),bd.20, width.43, bg.'white', justify.'left', textvariable.DateofOrder)
txtDateofOrder.grid(row.0,column.1)
lblTimeofOrder.Label(RightInsideLFLF, font.('Liberata', 12, 'bold'),text.'Time of Order', bd.10, bg.'white', justify.'left', textvariable.DateofOrder)#width.43, bg.'white', justify.'left', textvariable.DateofOrder)
lblTimeofOrder.grid(row.1,column.0)
txtTimeofOrder.Entry(RightInsideLF,font.('Liberata',12,'bold'), bd.20,width.43, bg.'white',justify.'left', textvariable.TimeofOrder)
txtTimeofOrder.grid(row.1,column.1)
lblCustomerRef.Label(RightInsideLFLF, font.('Liberata', 12, 'bold'), text.'Customer Ref', fg.'black', bd.10, anchor.'w')
lblCustomerRef.grid(row.2,column.0)
txtCustomerRef . Entry(RightInsideLF, font.('Liberata',12,'bold'), bd.20, width.43, bg.'white', justify.'left', textvariable.CustomerRef)
txtCustomerRef.grid(row.3,column.1)


#####Right Frame(Names of widgets)#####
lblMethodOfPayment. Label(RightInsideLFLF, font.('Liberata', 12, 'bold'), text.' Method of Payment',
                          fg . 'red', bd.16, anchor.'w')
lblMethodOfPayment.grid(row.0, column.0)
cmdMethodofPayment.ttk.Combobox(RightInsideLFLF,font.('Liberta', 10,'bold'))
cmdMethodofPayment['value']. ('','Debit Card','Visa Card', 'MasterCard','Cash App','Apple Pay','Venmo')
cmdMethodofPayment.grid(row.0, column.1)
lblDiscount . Label(RightInsideLFLF,font.('Liberata', 12, 'bold'), text.'Discount',fg.'black', bd.16, anchor.'w')
lblDiscount.grid(row.1,column.0)
txtDiscount . Entry(RightInsideLF, font.('Liberata', 12, 'bold'),bd.16, width.18, bg.'white', justify.'left', textvariable.Discount)
txtDiscount.grid(row.1,column.1)
lblTax . Label (RightInsideLF, font.('Liberata', 12, 'bold'), text.'Tax', fg.'black', bd.16, anchor.'w')
lblTax.grid(row.2,column.0)
txtTax . Entry(RightInsideLFLF,font.('Liberata',12, 'bold'), bd.16, width.18, bg.'white', justify.'left',textvariable.Tax)
txtTax.grid(row.2,column.1)
lblSubTotal . Label(RightInsideLFLF,font.('Liberata',12,'bold'),text.'Sub Total', fg.'black', bd.16, anchor.'w')
lblSubTotal.grid(row.3,column.0)
txtSubtotal . Entry(RightInsideLFLF, font.('Liberata', 12, 'bold'), bd.16, width.18, bg.'white', justify.'left',textvariable.SubTotal)
txtSubtotal.grid(row.3,column.1)
lblTotalCost . Label(RightInsideLFLF, font.('Liberata',12,'bold'), text. 'Total Cost', fg.'black',bd.16, anchor.'w')
lblTotalCost.grid(row.4,column.0)
txtTotalCost. Entry(RightInsideLFLF,font.('Liberata',12,'bold'), bd.16, width.18, bg.'white', justify.'left',textvariable.TotalCost)
txtTotalCost.grid(row.4,column.1)
#####Bottom Left Frame#####
#####Right Buttons Frame#####
btnTotalCost.Button(RightInsideRFRF, pady.8, bd.8, fg.'black', font.('Liberata', 16, 'bold'), width.11,
                    text.'Total Cost', bg.'white').grid(row.0,column.0)
btnReset.Button(RightInsideRFRF, pady.8, bd.8, fg.'black', font.('Liberata', 16, 'bold'), width.11,
                    text.'Reset', bg.'white').grid(row.1,column.0)
btnTip.Button(RightInsideRFRF, pady.8, bd.8, fg.'black', font.('Liberata', 16, 'bold'), width.11,
                    text.'Tip', bg.'white').grid(row.2,column.0)
btnOrderRef.Button(RightInsideRFRF, pady.8, bd.8, fg.'black', font.('Liberata', 16, 'bold'), width.11,
                    text.'Order Refrence', bg.'white').grid(row.3,column.0)
btnExit.Button(RightInsideRFRF, pady.8, bd.8, fg.'black', font.('Liberata', 16, 'bold'), width.11,
                    text.'Exit', bg.'white', command.Exit).grid(row.4,column.0)
root.mainloop()

                                                   

