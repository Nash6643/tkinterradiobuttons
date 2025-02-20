import tkinter as tk



root = tk.Tk()



root.geometry('300x300')
root.title("My window")

book1 = tk.Label(root, text="First Name").grid(row=0)
book2 = tk.Label(root, text="Last Name").grid(row=1)

def myfunc():
    print("First name: %s\n Last Name: %s" % (b1.get(), b2.get()))
    b1.delete(0, tk.END)
    b2.delete(0, tk.END)
b1 = tk.Entry(root)
b2 = tk.Entry(root)
b1.grid(row=0, column=1)
b2.grid(row=1, column=1)

what = tk.Button(root, text="Quit", command=root.quit).grid(row=3, column=0)
whapa = tk.Button(root, text="Show", command=myfunc).grid(row=3, column=1)

root.mainloop()
