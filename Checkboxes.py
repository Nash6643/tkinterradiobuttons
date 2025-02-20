import tkinter as tk
root = tk.Tk()



root.geometry("300x300")

root.title("My window")

def myfunc():
    print(v1.get(),v2.get())

v1 = tk.IntVar()
v2 = tk.IntVar()

lab = tk.Label(root, text="Your sex??")
lab.pack()

Book1 = tk.Checkbutton(root, text="Man", variable=v1)
Book1.pack()
Book2 = tk.Checkbutton(root, text="Female", variable=v2)
Book2.pack()

Book3 = tk.Button(root, text="Quit", command=root.destroy)
Book3.pack()

Book4 = tk.Button(root, text="Show", command=myfunc)
Book4.pack()

root.mainloop()
