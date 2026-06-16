import tkinter as tk

root = tk.Tk()
root.title("My first gUI app")
root.geometry('300x300')

label = tk.Label(root, text = "Hello!", font=('Arial', 16))

def say_hello():
    label.config(text="Button clicked!")
button = tk.Button(root, text = "Click me", command = say_hello)

entry = tk.Entry(root)
def entry_change():
    user_text = entry.get()
    label.config(text = user_text)
button2 = tk.Button(root, text = "Entry change", command = entry_change)

label.grid(row = 0, column = 1)
button.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
entry.grid(row = 0, column = 0)

label.config(fg = 'blue')
button2.config(bg = 'yellow')
root.config(bg = 'lightgrey')

def key_press(event):
    label.config(text = f"You pressed: {event.char}")

root.bind('<key>', key_press)


root.mainloop()

