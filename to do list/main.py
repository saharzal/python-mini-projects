import tkinter as tk
root = tk.Tk()

# Calculate X of window
def cal_x_center(x_window):
    screen_width = root.winfo_screenwidth()
    x_normal = (screen_width / 2) - (x_window / 2)
    return x_normal

# Calculate Y of window
def cal_y_center(y_window):
    screen_height = root.winfo_screenheight()
    y_normal = (screen_height / 2) - (y_window / 2)
    return y_normal

geometry = f'400x300+{int(cal_x_center(400))}+{int(cal_y_center(400))}'
root.title('To-Do List')
root.geometry(geometry)
root.resizable(0, 0)
root.config(bg="#a29bfe")
# Heading Label
tk.Label(root, text='My TODO List', bg='#a29bfe',font=("Comic Sans MS", 15), wraplength=300 , justify='center').place(x=132, y=0)

# Show window
root.update()
root.mainloop()



