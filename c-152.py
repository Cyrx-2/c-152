
from tkinter import*

root = Tk()

root.title("Profit")
root.geometry("500x500")
root.configure(background="blue")

LabelMonth = Label(root)
LabelProfit = Label(root)
LabelMaxProfit = Label(root)
LabelMinProfit = Label(root)

month = ("January","Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November","December")
profits = (2000, 45000, 78000, 97000, 12000, 45600,65000,54000, 62000, 48000, 30000, 120000, 90000, 71000, 82000)
LabelMonth["text"] = "month: " + str(month)
LabelProfit["text"] = "Profit: " + str(profits)

def maxProfit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)

    max_profit_month = month[max_profit_index]
    print("The max profit of " + str(max_profit) + "was recorded in the month of " + str(max_profit_month))
    LabelMaxProfit["text"] = "The max profit of " + str(max_profit) + "was recorded in the month of " + str(max_profit_month)

def minProfit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)

    min_profit_month = month[min_profit_index]
    print("The min profit of " + str(min_profit) + "was recorded in the month of " + str(min_profit_month))
    LabelMinProfit["text"] = "The min profit of " + str(min_profit) + "was recorded in the month of " + str(min_profit_month)
    
LabelMonth.place(relx = 0.5, rely = 0.2 , anchor = CENTER)
LabelProfit.place(relx = 0.5, rely = 0.3 , anchor = CENTER)

btnmax = Button(root, text = "Most Profitable Month", command = maxProfit, bg = "tan" ,fg = "white")
btnmin = Button(root, text = "Least Profitable Month", command = minProfit, bg = "tan" ,fg = "white")
                
btnmax.place(relx = 0.5, rely = 0.4, anchor=CENTER)

LabelMaxProfit.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btnmin.place(relx = 0.5, rely = 0.6, anchor=CENTER)

LabelMinProfit.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()




