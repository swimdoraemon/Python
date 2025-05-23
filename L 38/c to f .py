import tkinter as tk

def fahrenheit_to_celcius():
    """Convert the value for Fahrenheit to Celsius and insert the result into lbl_result"""

    fahrenheit = ent_temperature.get()
    celcius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


window = tk.Tk()
window.title("Tempurature Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.label(master=frm_entry, text="\N{DEGREE FARENHEIT}")


ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master=window,
    text="-->",
    command=fahrenheit_to_celcius
)
lbl_result = tk.label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, pady=10)