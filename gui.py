from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from generate import run_generator

def callback(url):
    webbrowser.open_new(url)

def startprocess():
    Language = Language_Combobox.get().strip()
    API_KEY = APIKey_Entry.get().strip()

    if Language not in ["Malay", "English"]:
        messagebox.showerror("Error", "A language has not been selected")
        return

    if API_KEY == "":
        messagebox.showerror("Error", "Please enter your API key.")
        return

    # Save API key locally
    with open("apikey.txt", "w") as f:
        f.write(API_KEY)

    if not messagebox.askyesno("Confirm", f"Proceed with language *{Language}*?"):
        return
    
    try:
        run_generator(Language, API_KEY)
        messagebox.showinfo("Done", "Generation completed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))



root = Tk()
root.geometry("400x400")

App_Title = root.title("Ains HyperGen v0.0.1alpha(groq)")

App_Label = Label(root, text="AINS HyperGen", font = ("Arial", 14, "bold"))
App_Label.pack(anchor = N)

Lines = Label(root, text = "_____________________________________________________________", font = ("Arial" , 15))
Lines.pack(anchor = N)

Language_Label = Label(root, text = "Language used:", font = ("Arial", 11, "bold"))
Language_Label.pack(anchor = N, pady = (20,0))

language_values = ["Malay", "English"]
Language_Combobox = ttk.Combobox(root, values = language_values)
Language_Combobox.pack(anchor= N)

APIKey_Label = Label(text = "API Key:", font=("Arial", 11, "bold"))
APIKey_Label.pack(anchor = N, pady = (30,0))

APIKey_Entry = Entry(width = 50)
APIKey_Entry.pack(anchor = N)

try:
    with open("apikey.txt", "r") as f:
        saved_key = f.read().strip()
        APIKey_Entry.insert(0, saved_key)
except FileNotFoundError:
    pass

getAPIKey_hyperlink = Label(text = "Get API key...", font = ("Arial", 8, "bold"), fg = "#1100FF")
getAPIKey_hyperlink.pack(anchor = N)
getAPIKey_hyperlink.bind("<Button-1>", lambda e: callback("https://platform.openai.com/api-keys"))


Run_Button = Button(text="Run", background ="#15FA65" , width = 25, command = startprocess)
Run_Button.pack(anchor= S, pady = (50,0))


root.mainloop()