## LIBRARIES
import customtkinter as ctk
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading
import sys
import keyboard

## USER-DEFINED FUNCTIONS

# 1.To create icon image in system tray
def create_image():
    img = Image.new("RGB", (64, 64), "yellow")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 64, 64), fill="orange")
    return img

# 2. To Exit the Progeam
def on_exit(icon, item=None):
    icon.stop()
    root.after(0, root.destroy)
    sys.exit()

# 3. To Show App
def show():
    root.deiconify()
    root.state("normal") 
    root.lift()
    root.focus_force()

# 4. After shown , not on top
def not_top():
    root.attributes("-topmost",False)

# 5. WIN+D Shortcut not Work on our APP
def on_hotkey():
    print("WIN+D PRESSED")
    root.after(100, show)
    root.attributes("-topmost", True)
    root.after(100,not_top)

# 6. ADD ELEMENTS 

# "X". Main Function
def main():
    ## GLOBAL VARIABLE DEFINED
    global root, icon

    ## CTK BASICS
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    ## CTK WINDOW CONFIG
    root = ctk.CTk()
    root.geometry("300x300+1050+20")
    root.overrideredirect(True)
    root.attributes("-topmost", False)
    root.wm_attributes("-toolwindow", True)


    ## TRAY ICON
    menu = Menu(MenuItem("Exit", on_exit))
    icon = Icon("sticky_note", create_image(), "Sticky Note", menu)
    threading.Thread(target=icon.run).start()

    ## HOTKEY FOR WIN+D
    keyboard.add_hotkey("win+d", on_hotkey)

    ## ELEMENTS

    # 1.MAIN FRAME
    main_frame = ctk.CTkScrollableFrame(root)
    task_entry = ctk.CTkEntry(main_frame,placeholder_text="Enter New Task")


    ## ELEMENT CONFIGURE
    main_frame.grid_columnconfigure(0, weight=1)



    ## ELEMENTS PACK / PLACE
    main_frame.pack(fill="both", expand=True,padx=5,pady=5)
    task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")




    ## RUN APP
    root.mainloop()


## RUN MAIN FUNCTION
main()
