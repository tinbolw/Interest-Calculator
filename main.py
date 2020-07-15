import tkinter as tk

money = 0
rate = 0
answer = 0

root = tk.Tk()

root.title("Interest")
root.geometry("250x150")

moneyEntry = tk.Entry(root)
moneyEntry.grid(column=1, row=0)

rateEntry = tk.Entry(root)
rateEntry.grid(column=1, row=1)

answerEntry = tk.Entry(root)
answerEntry.grid(column=1, row=2)

moneyLabel = tk.Label(root, text = "Starting Amount")
moneyLabel.grid(row=0)

interestLabel = tk.Label(root, text = "Interest Amount")
interestLabel.grid(row=1)

answerLabel = tk.Label(root, text = "After Interest")
answerLabel.grid(row=2)

def calculate():
	global money
	global rate
	global answer
	money = moneyEntry.get()
	rate = rateEntry.get()
	answerEntry.delete(0, tk.END)
	moneyEntry.delete(0, tk.END)
	rateEntry.delete(0, tk.END)
	money = float(money)
	rate = float(rate)
	addToMoney = money * rate
	answer = money + addToMoney
	answerEntry.insert(0, answer)


calculateButton = tk.Button(root, height=3, width=10, text = "Calculate", command = calculate)
calculateButton.grid(column=1, row=3)


root.mainloop()