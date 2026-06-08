import customtkinter

APP_TITLE = "Android Pattern LockScreen Bruteforce - Visualizer"
APP_GEOMETRY = "1200x600"

app = customtkinter.CTk()
app.title(APP_TITLE)
app.geometry(APP_GEOMETRY)
app.columnconfigure(0, weight=1)


def button_callback():
    print("Button Pressed")

button = customtkinter.CTkButton(app, text="Click Me!", command= button_callback)
button.grid(row=0,column=0,padx=10,pady=10, sticky="ew")

app.mainloop()
