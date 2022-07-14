from tkinter import *

root = Tk()
root.title('Mortgage Calculator')
root.geometry("500x400")


def payment():
  if amount_entry.get() and interest_entry.get() and term_entry.get() and down_entry.get():
    #convert entry boxes to numbers
    years = int(term_entry.get())
    months = years * 12 
    down_payment = (float(down_entry.get())/100) * float(interest_entry.get())
    rate = float(interest_entry.get()) - down_payment
    loan = int(amount_entry.get())
    #calculate the loan
    monthly_rate = rate / 100/12
    #get payment
    payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months)))* loan 
    #format
    payment = f"{payment:,.2f}"
    #output payment
    payment_label.config(text=f"Monthly Payment: ${payment}")
    
    
  else:
    payment_label.config(text="You forgot something")


  

my_label_frame = LabelFrame(root, text = "Mortgage Calculator")
my_label_frame.pack(pady = 30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady = 10, padx=20)

# Define label and entry boxes
amount_label = Label(my_frame, text ="Loan amount")
amount_entry = Entry(my_frame, font =("Helvetica", 18))

interest_label =Label(my_frame, text ="Interest Rate")
interest_entry = Entry(my_frame, font =("Helvetica", 18))

term_label =Label(my_frame, text ="Term (years)")
term_entry = Entry(my_frame, font =("Helvetica", 18))

down_label =Label(my_frame, text ="Down Payment")
down_entry = Entry(my_frame, font =("Helvetica", 18))

#put labels and entry boxes on screen
amount_label.grid(row = 0, column = 0)
amount_entry.grid(row = 0, column = 1)

interest_label.grid(row = 1, column = 0)
interest_entry.grid(row = 1, column = 1, pady = 10)

term_label.grid(row = 2, column = 0)
term_entry.grid(row = 2, column = 1,pady = 10)

down_label.grid(row = 3, column = 0)
down_entry.grid(row = 3, column = 1)


#Buttton
my_button = Button(my_label_frame, text ="Calculate Payment", command=payment)
my_button.pack(pady=20)

#Output Label
payment_label = Label(my_label_frame, text = "", font= ("Helvetica, 18"))
payment_label.pack(pady =0)



root.mainloop()
