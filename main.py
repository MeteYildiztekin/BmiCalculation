import tkinter
import webbrowser
from tkinter import *

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Lütfen bir değer giriniz!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Doğru bir değer giriniz!")

def openlink():
    webbrowser.open("https://www.medicalpark.com.tr/vucut-kitle-indeksi/hg-2345")

linkbutton = Button(window, text="OBEZİTE HAKKINDA BİLGİ İÇİN TIKLAYIN", command=openlink)


weight_input_label = tkinter.Label(text="KG")
weight_input_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()
height_input_label = tkinter.Label(text="CM")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()
calculate_button = tkinter.Button(text="HESAPLA", command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"{round(bmi, 2)}."
    if bmi <= 18.5:
        result_string += "Zayıf!"
    elif 18.5 < bmi <= 24.9:
        result_string += "Normal Ağırlık!"
    elif 25 < bmi <= 29.9:
        result_string += "Kilolu"
    elif 30 < bmi <= 34.9:
        result_string += "1.Derece Obezite"
    elif 35 < bmi <= 39.9:
        result_string += "2.Derece Obezite"
    else:
        result_string += "3.Derece Obez"
    return result_string


linkbutton.pack()
window.mainloop()
