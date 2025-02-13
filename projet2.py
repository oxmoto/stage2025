import tkinter as tk
from tkinter import messagebox

def msgCallBack():
     messagebox.showinfo ("App", "Le bouton est cliqué")
def msgCallBack2():
    messagebox.showwarning("App", "se si est la droite")
def msgCallBack3():
    messagebox.showerror("App", "c'est se que tu mas demander")
def msgCallBack4():
    messagebox.askquestion("App", "j'ai juste oui ou non")

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
