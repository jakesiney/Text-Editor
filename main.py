import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400, weight=1)
    window.columnconfigure(0, minsize=500, weight=1)

    text_edit = tk.Text(window, font=("Helvetica", 18))
    text_edit.grid(row=0, column=0)

    window.mainloop()


main()
