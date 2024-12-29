'''
Author: Aayan Ahmad Khan

Date: 23/12/2024

Infos: #######'''

#Location: C:\Users\amna_\OneDrive\Dokumente\Codes,program\Python files

from tkinter import *
import tkinter as tk
import requests

root = tk.Tk()
root.geometry("300x300")
root.title("Currency Converter")
root.config(bg="Black")

cur_label = Label(root, text="", fg="Green", bg="black", font=("Arial", 16))
cur_label.pack()


label_1 = Label(root, text="Enter Euros:", fg="white", bg="black", font=("Arial", 16))
label_1.pack()

entry1 = Entry(root, width=20, font=("Arial", 16))
entry1.pack()

answer_label = Label(root, text="Dollars:", fg="white", bg="black", font=("Arial", 16))
answer_label.pack()


url = "https://v6.exchangerate-api.com/v6/14dd33f0ea2c74d9f0b1e45a/latest/EUR"

response = requests.get(url)

def calculate():
    try:
        data = response.json()
        euro_to_usd_rate = data['conversion_rates']['USD']

        currency = entry1.get()
        euros = float(currency)  

        dollars = euros * euro_to_usd_rate

        cur_label.config(text=f'{euros:.2f} euros is equivalent to {dollars:.2f} dollars.')
    except ValueError:
        cur_label.config(text="Please enter a valid number.")
    except Exception as e:
        cur_label.config(text=f"Error: {e}")

button1 = Button(root, text="Convert", command=calculate, font=("Arial", 16))
button1.pack()

root.mainloop()