import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import os


class StockGui:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Stock Bot")
        self.window.geometry('500x500')

        self.label = tk.Label(self.window, text="Stock Ticker here", font=("Bold", 20))
        self.label.pack(padx=20, pady=10)

        self.textbox = tk.Text(self.window, height=1, width=10, font=("Bold", 20))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.window, height=2, width=5, text="Click", font=("Bold", 8),
                                command=lambda: [textbox_retrieve(), stock_price(self.label1), delete()])
        self.button.pack(padx=20, pady=20)

        self.label1 = tk.Label(self.window, text="Waiting on stock Lookup", font=("Bold", 20))
        self.label1.pack(padx=50, pady=50)

        def stock_price(label):
            with open("stock_data.txt", "r") as f:
                stock = yf.Ticker(f.readline()).info
                price = stock['regularMarketPrice']
                if price is None:
                    messagebox.showerror(title="Invalid Stock", message="Enter a Valid Stock")
                else:
                    label["text"] = str(price)

        def textbox_retrieve():
            textbox_value = str(self.textbox.get("1.0", "end-1c")).upper()
            if len(textbox_value) == 0:
                messagebox.showerror(title="Error", message="Nothing inputted")
            else:
                with open("stock_data.txt", "w+") as f:
                    f.write(textbox_value)
                    f.close()

        def delete():
            self.textbox.delete("1.0", "end")

        self.window.mainloop()


if __name__ == "__main__":
    file_path = os.getcwd()
    if os.path.exists(f'{file_path}/stock_data.txt'):
        os.remove(f"{file_path}/stock_data.txt")
        file = open(f'{file_path}/stock_data.txt', "+w")
        file.close()
    else:
        file = open(f'{file_path}/stock_data.txt', "+w")
        file.close()
    StockGui()
