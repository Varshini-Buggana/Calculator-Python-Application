import tkinter as tk
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
entry = tk.Entry(root, font = "Arial 20", borderwidth=4, relief=tk.RIDGE) 
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['C','0','=','+']
]       
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True,fill="both")
    for btn in row:
        button = tk.Button(frame,text = btn, font="Arial 18",relief=tk.GROOVE, border=0)
        button.pack(side=tk.LEFT,expand=True, fill="both",padx=2,pady=2)
        button.bind("<Button-1>",click)
root.mainloop()