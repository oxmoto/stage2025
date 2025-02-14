import tkinter as tk
from tkinter import messagebox

def msgCallBack():
     messagebox.showinfo ("App", "et sa c'est l'extreme gauche")
def msgCallBack2():
    messagebox.showwarning("App", "se si est l'extreme droite")
def msgCallBack3():
    messagebox.showerror("App", "et sa c'est le haut")
def msgCallBack4():
    messagebox.askquestion("App", "sa c'est le bas")

gui = tk.Tk()
btn1 = tk.Button(gui, text="gauche", command=msgCallBack, activeforeground="green", activebackground="yellow", padx=8, pady=5)
btn2 = tk.Button(gui, text="droite", command=msgCallBack2, activeforeground="blue", activebackground="yellow", padx=8, pady=5)
btn3 = tk.Button(gui, text="haut", command=msgCallBack3, activeforeground="red", activebackground="yellow", padx=8, pady=5)
btn4 = tk.Button(gui, text="bas", command=msgCallBack4, activeforeground="black", activebackground="yellow", padx=8, pady=5)

btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.RIGHT)
btn3.pack(side=tk.TOP)
btn4.pack(side=tk.BOTTOM)

gui.mainloop()
