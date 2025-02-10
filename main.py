from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
from tkinter import font
#functionality
fontSize = 12
fontStyle = 'arial'
def font_style(event):
  global fontStyle
  fontStyle = font_family_variable.get()
  text_edit.config(font = (fontStyle, fontSize))

def font_size(event):
  global fontSize
  fontSize = size_variable.get()
  text_edit.config(font=(fontStyle,fontSize))

def Bold():
  pass

def open_file(window, text_edit):
  filepath  = askopenfilename(filetypes= [('Text Files', "*.txt")])
  if not filepath:
    return
  text_edit.delete(1.0,END)
  with open(filepath, "r") as f:
    content = f.read()
    text_edit.insert(END, content)
  window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
  filepath = asksaveasfilename(filetypes= [('Text Files', "*.txt")])

  if not filepath:
    return 
  with open(filepath, "w") as f:
    content = text_edit.get(1.0, END)
    f.write(content)
  window.title(f"Open File: {filepath}")



def toggle_bold():
    """Toggles bold styling for the selected text."""
    try:
        current_tags = text_edit.tag_names("sel.first")  # Get current tags
        if "bold" in current_tags:
            text_edit.tag_remove("bold", "sel.first", "sel.last")  # Remove bold
        else:
            text_edit.tag_add("bold", "sel.first", "sel.last")  # Add bold
            text_edit.tag_config("bold", font=bold_font)  # Define bold tag
    except TclError:
        pass  # If no text is selected, do nothing


window = Tk()
window.title("Text Editor")

# # initial number specifies the row/column 
window.rowconfigure(1, weight= 1)
window.columnconfigure(0, weight = 1)



# #Creating a frame - a vertical column
# frame = Frame(window, relief= RAISED, border= 2)
# save_button = Button(frame, text="Save", command= lambda: save_file(window, text_edit))
# open_button = Button(frame, text="Open", command= lambda: open_file(window, text_edit))

# save_button.grid(row = 0, column= 0, padx =5, pady = 5, sticky="ew" )
# open_button.grid(row = 1, column = 0, padx =5, sticky="ew")
# frame.grid(row = 0, column= 0, sticky = "ns") 

# Create a menu bar
menu_bar = Menu(window)
window.config(menu = menu_bar)
  
# Add Sub-menus to the menu bar
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label = "New", accelerator = "Ctrl+N")
file_menu.add_command(label = "Open", accelerator = "Ctrl+O")
file_menu.add_command(label = "Save", accelerator = "Ctrl+S")
file_menu.add_command(label = "Save as", accelerator = "Ctrl+Alt+S")
file_menu.add_separator()
file_menu.add_command(label = "Exit", accelerator = "Ctrl+Q")





edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label = "Cut", accelerator = "Ctrl+X")
edit_menu.add_command(label = "Paste", accelerator = "Ctrl+V")
edit_menu.add_command(label = "Copy", accelerator = "Ctrl+C")
edit_menu.add_command(label = "Clear", accelerator = "Ctrl+Alt+X")
edit_menu.add_command(label = "Find", accelerator = "Ctrl+F")


show_toolbar = BooleanVar()
show_statusbar = BooleanVar()
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_checkbutton(label = "Tool Bar", variable = show_toolbar, onvalue=True, offvalue= False)
view_menu.add_checkbutton(label = "Status Bar", variable = show_statusbar, onvalue=True, offvalue= False)


color_scheme_menu = Menu(menu_bar, tearoff=0)
lightImage = PhotoImage(file = "Images/light_default.png")
darkImage = PhotoImage(file = "Images/dark.png")
nightBlueImage = PhotoImage(file = "Images/night_blue.png")
monokaiImage = PhotoImage(file = "Images/monokai.png")
redImage = PhotoImage(file = "Images/red.png")

theme_choice = StringVar()
menu_bar.add_cascade(label="Color Scheme", menu=color_scheme_menu) 
color_scheme_menu.add_radiobutton(label ="Light", variable=theme_choice,compound=LEFT,image= lightImage )
color_scheme_menu.add_radiobutton(label ="Dark", variable=theme_choice,compound=LEFT,image= darkImage)
color_scheme_menu.add_radiobutton(label ="Night Blue", variable=theme_choice,compound=LEFT,image= nightBlueImage )
color_scheme_menu.add_radiobutton(label ="Monokai", variable=theme_choice,compound=LEFT,image= monokaiImage )
color_scheme_menu.add_radiobutton(label ="Red", variable=theme_choice,compound=LEFT,image= redImage )

#toolbar scetion

tool_bar = Label(window)
tool_bar.grid(row= 0, column= 0, sticky= "ns")
font_families =font.families()
font_family_variable = StringVar()

fontfamily_combobox = Combobox(tool_bar, width= 30, values= font_families, state="readonly", textvariable= font_family_variable)
fontfamily_combobox.current(0)
fontfamily_combobox.grid(row=0, column=0, padx= 5)
fontfamily_combobox.bind('<<ComboboxSelected>>', font_style)

size_variable = IntVar()
fontsize_combobox = Combobox(tool_bar, width= 14, values= tuple(range(3,80)), state="readonly", textvariable= size_variable)
fontsize_combobox.current(4)
fontsize_combobox.grid(row=0, column=1, padx= 5)

fontsize_combobox.bind('<<ComboboxSelected>>', font_size)

# button  section - toolbar
boldImage = PhotoImage(file="Images/bold.png")
italicImage = PhotoImage(file="Images/italic.png")
underlineImage = PhotoImage(file="Images/underline.png")
fontColorImage = PhotoImage(file="Images/font_color.png")
rightImage = PhotoImage(file="Images/right.png")
leftImage = PhotoImage(file= "Images/left.png")
centerImage = PhotoImage(file= "Images/center.png")

bold_button = Button(tool_bar, image = boldImage, command=toggle_bold )
bold_button.grid(row=0, column=2,padx= 5)

italic_button = Button(tool_bar, image = italicImage)
italic_button.grid(row=0, column=3,padx= 5)

underline_button = Button(tool_bar, image = underlineImage)
underline_button.grid(row=0, column=4,padx= 5)

font_color_button = Button(tool_bar, image = fontColorImage)
font_color_button.grid(row=0, column=5,padx= 5)

right_button = Button(tool_bar, image = rightImage)
right_button.grid(row=0, column=8,padx= 5)

left_button = Button(tool_bar, image = leftImage)
left_button.grid(row=0, column=6,padx= 5)

center_button = Button(tool_bar, image = centerImage)
center_button.grid(row=0, column=7,padx= 5)



#"""Creating the text editor components. Specifying the window and 
# the default fonts"""
text_edit = Text(window, font="Helvetica 18", wrap = "word")

#placing the text_edit component 
text_edit.grid(row = 1, column = 0, sticky="nsew")

# Create a bold font style
bold_font = font.Font(text_edit, text_edit.cget("font"))
bold_font.configure(weight="bold")

#Scroll Bar
scrollbar = Scrollbar(window, command= text_edit.yview)
scrollbar.grid(row = 1, column=1,sticky="ns")
#Linking the scrollbar to the text widget
text_edit.config(yscrollcommand=scrollbar.set)

status_bar = Label(window, text="Status Bar")
status_bar.grid(row=2, column=0, sticky="ew")

#Adding shortcuts
window.bind("<Control-s>", lambda x: save_file(window, text_edit))
window.bind("<Control-o>", lambda x: open_file(window, text_edit))
window.mainloop()


