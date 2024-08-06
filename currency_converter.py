from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.geometry("470x490")
root.title("CURRENCY CONVERTER")


icon_image = Image.open("C:\\Users\\Admin\\Pictures\\Screenshots\\icon.jpg")
icon_image = icon_image.resize((30,30))
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True,icon_photo)


def convert():

    try:
       
       selected_currency = currency_combobox.get().strip()

       value = float(usd_currency.get().strip())

       if selected_currency == "INR":

         exchange_rate = 83.0
         converted_value = value*exchange_rate
         other_currency.set(converted_value)
         display_result.set(f"{value} U.S.D = {converted_value} INR")

       elif selected_currency == "EUR":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")

       elif selected_currency == "GBP":
        
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")

       elif selected_currency == "JPY":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")
          

       elif selected_currency == "CAD":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")
      


       elif selected_currency == "AUD":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")



       elif selected_currency == "CHF":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")
        
  


       elif selected_currency == "CNY":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")



       elif selected_currency == "MXN":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")
 

       elif selected_currency == "SGD":
          
          exchange_rate = 0.93
          converted_value = value*exchange_rate
          other_currency.set(converted_value)
          display_result.set(f"{int(value)} U.S.D = {int(converted_value)} INR")

       else:

          display_result.set("PLEASE SELECT CURRENCY")  

    except ValueError:
       
       display_result.set("PLEASE ENTER VALID AMOUNT")     



def reset():
    
    usd_currency.set("") 
    other_currency.set("")
    usd_combobox.set("")
    currency_combobox.set("")
    display_result.set("")
    


label = Label(root, text="CONVERTS U.S.D TO SELECTED COUNTRY CURRENCY", font= "timesnewroman 12 bold")
label.pack(pady=10)

f1 = Frame(root)
f1.pack(pady=10)

usd_currency = StringVar()
usd_currency.set("")


Entry(f1, textvariable=usd_currency,font= "timesnewroman 10 ").pack(side=LEFT,padx=10,ipady=5)

my_image = Image.open("C:\\Users\\Admin\\Pictures\\Screenshots\\currency.png")

resize_image = my_image.resize((60,60))

currency_pic = ImageTk.PhotoImage(resize_image)
label = Label(f1,image=currency_pic,padx=10)
label.pack(side=LEFT)

usd_combobox = ttk.Combobox(f1, values=["U.S.D"])
usd_combobox.pack(side=LEFT,padx=10,ipady=5)


f2 = Frame(root)
f2.pack(pady=10)

other_currency = StringVar()
other_currency.set("")

Entry(f2, textvariable=other_currency,font= "timesnewroman 10 ").pack(side=LEFT,padx=45,ipady=5)

currency_combobox = ttk.Combobox(f2, values=[ "INR ", "EUR" , "GBP" , "JPY" , "CAD" , "AUD" , "CHF" , "CNY" , "MXN" , "SGD" ])
currency_combobox.pack(side=LEFT,padx=45,ipady=5)

f3 = Frame(root)
f3.pack(pady=10)

b = Button(f3,text="CONVERT" , command=convert , bg="yellow",borderwidth=5 , font= "timesnewroman  10 bold")
b.pack(padx=70,pady=40,ipady=2)

b = Button(f3,text="RESET" ,command=reset , bg="red")
b.pack(padx=70,ipady=2)



f4 = Frame(root)
f4.pack(pady=10)

display_result = StringVar()
display_result.set("")

Entry(f4, textvariable= display_result, font= "timesnewroman 12 ").pack(padx=20,pady=10,ipadx=60,ipady=20)


root.mainloop()