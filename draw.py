from tkinter import *
from tkinter import colorchooser
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import filedialog
import pyautogui



window = Tk()
window.geometry("1000x600")
window.title("Draw app")

canvas = Canvas(window,background="black")
canvas.pack(fill="both",expand=True)


line_width = 3
pencolor = "yellow"
loaded_image = ""


def add_image(event=None):
    global loaded_image
    file = filedialog.askopenfilename(filetypes=[("Image files",("*.png", "*.jpg","*.JPG","*.JPEG","*.ico"))])
    if file:
        loaded_image = file 
        print(loaded_image)
        image = Image.open(loaded_image)
        image = image.resize((500,500),Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        canvas.create_image(20,20,image=image,anchor="nw")

    
    else:
        pass
   



def save_canvas(event=None):
    file_path = filedialog.asksaveasfile(filetypes=[("Postscript",("*.eps"),"Image",("*.png"))])
    screen_shot = pyautogui.screenshot()

    if file_path:
        file_name = f"{file_path.name}"#{str(datetime.now())[:19]
        canvas.postscript(file=file_name + ".eps")
        screen_shot.save(file_name+".png")
        # try:
        #     img = Image.open(file_name+".eps")
        #     img.save(file_name+".png","png")
        #     print("done")
        # except Exception as e:
        #     print(e)
        #     pass
    else:
        pass


def increase_line_width(event):
    global line_width
    line_width += 1
    print(line_width)

def decrease_line_width(event):
    global line_width
    if line_width == 0:
        line_width = 0
    else:
        line_width -= 1
    print(line_width)


def get_x_y_posn(event):
    global posx,posy 
    posx,posy = event.x,event.y
    
def draw_oncanvas(event):
    global line_width
    global posx,posy 
    canvas.create_line((posx,posy,event.x,event.y),fill=pencolor,width=line_width)
    posx,posy = event.x,event.y

def change_pen_color(event=None):
    global pencolor
    color = colorchooser.askcolor()
    hex_color = color[1]
    pencolor = hex_color
    window.title(str(pencolor))


def clear_canvas(event=None):
    canvas.delete('all')

def light_bg(event=None):
    color = "white"
    canvas.config(bg=color)

def dark_bg(event=None):
    color = "black"
    canvas.config(bg=color)


main_menu = Menu(window,relief="raised")
window.config(menu=main_menu)


file_menu = Menu(main_menu,tearoff=0)
preferences_menu = Menu(main_menu,tearoff=0)
help_menu = Menu(main_menu,tearoff=0)
about_menu = Menu(main_menu,tearoff=0)


open_icon = PhotoImage(file="./file.png")
save_icon = PhotoImage(file="./save.png")
edit_icon = PhotoImage(file="./edit.png")
pallete_icon = PhotoImage(file="./pallete.png")

dark_bg_icon = PhotoImage(file="./dark.png")
light_bg_icon = PhotoImage(file="./mixed.png")


main_menu.add_cascade(label="files",menu=file_menu)
main_menu.add_cascade(label="Preferences",menu=preferences_menu)
main_menu.add_cascade(label="Help",menu=help_menu)
main_menu.add_cascade(label="About",menu=about_menu)


file_menu.add_command(label="New file  ctrl+O",command=lambda:None,image=open_icon,compound="left")
file_menu.add_command(label="Save   ctrl+S",command=lambda:save_canvas(),image=save_icon,compound="left")
file_menu.add_command(label="Clear canvas    ctrl+w",command=lambda:clear_canvas(),image=pallete_icon,compound="left")


preferences_menu.add_command(label="Pen color   ctrl+p",command=lambda:change_pen_color(),image=pallete_icon,compound="left")
preferences_menu.add_command(label="Light background    ctrl+l",command=lambda:light_bg(),image=light_bg_icon,compound="left")
preferences_menu.add_command(label="Dark background     ctrl+d",command=lambda:dark_bg(),image=dark_bg_icon,compound="left")
preferences_menu.add_command(label="Place Image     ctrl+alt+i",command=lambda:add_image())

help_menu.add_command(label="help",command=lambda:None)


canvas.bind("<Button-1>",get_x_y_posn)
canvas.bind("<B1-Motion>",draw_oncanvas)
canvas.bind("<Button-3>",decrease_line_width)
window.bind("<Control-t>",increase_line_width)
window.bind("<Control-p>",change_pen_color)
window.bind("<Control-l>",light_bg)
window.bind("<Control-d>",dark_bg)
window.bind("<Control-w>",clear_canvas)


if __name__ == "__main__":
    window.mainloop()