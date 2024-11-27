import customtkinter as ctk
from tkinter import StringVar

def convert_temperature():
    choice = selected_value.get()
    if (choice == "C"):
        convert_to_celsius()
    else:
        convert_to_fahrenheit()

def convert_to_celsius():
    fahrenheit = float(temp_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    celsius_text = f"{celsius:.2f}°C"
    label_result.configure(text=celsius_text,text_color="green", font=ctk.CTkFont(size=20,weight="bold"))

def convert_to_fahrenheit():
    celsius = float(temp_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    fahrenheit_text = f"{fahrenheit:.2f}°F"
    label_result.configure(text=fahrenheit_text,text_color="green", font=ctk.CTkFont(size=20,weight="bold"))


window = ctk.CTk()
ctk.set_appearance_mode("white")
window.geometry("600x400")
window.title("Temperature Converter")

title_label = ctk.CTkLabel(window, text="Temperature Converter", font=ctk.CTkFont(size=30, weight='bold'))
title_label.pack(padx=10, pady=(30, 20))

radio_Frame = ctk.CTkFrame(window)
radio_Frame.pack(fill='x', padx=50)

selected_value = StringVar(value='C')

radio_FtoC = ctk.CTkRadioButton(radio_Frame, text="Fahrenheit to Celsius", variable=selected_value, value="C")
radio_FtoC.pack(side="left", padx=(80, 10), pady=10)

radio_CtoF = ctk.CTkRadioButton(radio_Frame, text="Celsius to Fahrenheit", variable=selected_value, value="F")
radio_CtoF.pack(side="left", padx="10", pady="10")

input_Frame = ctk.CTkFrame(window)
input_Frame.pack(fill="x", padx="50", pady="30")

temp_entry = ctk.CTkEntry(input_Frame, placeholder_text="enter temperature...")
temp_entry.pack(side="left", padx=(80,10), pady=20)

convert_button = ctk.CTkButton(input_Frame, text="Convert" , command=convert_temperature)
convert_button.pack(side='left',padx=10,pady=20)

result_Frame = ctk.CTkFrame(window)
result_Frame.pack(fill="x", padx=50)

label_result = ctk.CTkLabel(result_Frame, text="")
label_result.pack()

window.mainloop()