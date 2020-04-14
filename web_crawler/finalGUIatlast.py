import tkinter as tk
from ttkthemes import ThemedTk
import csv
import webbrowser
import threading
import merged_code
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

MAX = 10
#
# def loop_function():
#
#     k = 0
#     while k <= MAX:
#     ### some work to be done
#         progress_var.set(k)
#         k += 1
#         time.sleep(0.01)
#         window.update()
#     window.after(10, loop_function)


class GUI:
    e1 = ''
    e2 = ''
    e3 = ''
    thread_list = []

    def __init__(self):
        self.window = ThemedTk(theme="arc")  # arc breeze
        self.window.title("Web Scraping")
        self.window.configure(background="white")
        self.setInputs()
        self.setButtons()
        self.name = ''
        self.min1 = ''
        self.max1 = ''
        self.ans = []

    def start(self):
        self.window.mainloop()

    def setInputs(self):
        Label(self.window, text="Enter Category ", font=("Arial", 15), background="white", foreground="black").grid(row=2)
        Label(self.window, text="Enter Min Price ", font=("Arial", 15), background="white", foreground="black").grid(row=4)
        Label(self.window, text="Enter Max Price ", font=("Arial", 15), background="white", foreground="black").grid(row=6)
        Label(self.window, text="", font=("Arial", 15), background="white", foreground="black").grid(row=0)

        self.e1 = tk.Entry(self.window)
        self.e1.grid(row=2, column=1)
        self.e2 = tk.Entry(self.window)
        self.e2.grid(row=4, column=1)
        self.e3 = tk.Entry(self.window)
        self.e3.grid(row=6, column=1)

    def setButtons(self):
        tk.Button(self.window, text=' Search ', bg="#e0e0d1", command=self.running).grid(row=8, column=1, sticky=tk.W, pady=6)
        tk.Button(self.window, text=' Exit ', bg="#e0e0d1", command=quit).grid(row=8, column=2, sticky=tk.W, pady=6)
        # running()

    @staticmethod
    def callback(url):
        print(url)
        webbrowser.open_new(url)

    def on_change(self, e):
        print(e.widget.get())

    @staticmethod
    def readAnsFromCSV(name_of_file):
        data0 = []
        with open(name_of_file, 'r')as f:
            data1 = csv.reader(f)
            for row in data1:
                data0.append(row)
        return data0[1:]

    def do(self):
        obj = merged_code.result(self.name.strip(), self.min1, self.max1)
        self.ansfile = obj.getResult()
        print("answer file " + self.ansfile)
        self.ans = self.readAnsFromCSV(self.ansfile)
        print('result ' + str(len(self.ans)))
        print(self.ans)
        self.loading.quit()

    def loading(self):
        self.loading = ThemedTk(theme="arc")  # arc breeze
        self.loading.title("loading")
        self.loading.configure(background="white")
        self.loading.geometry("300x200")
        self.loading_label = Label(self.loading, text="Loading Please Wait ", font=("Arial", 15), background="blue",foreground="black").grid(row=2, column=2)
        self.loading.mainloop()
        print('loading')
        print('-----------------------------------------------------')

    class Splash(tk.Toplevel):
        def __init__(self, parent):
            tk.Toplevel.__init__(self, parent)
            self.title("Splash")

    def running(self):
        self.name = self.e1.get()
        self.min1 = float(self.e2.get())
        self.max1 = float(self.e3.get())

        thread = threading.Thread(target=self.do)
        thread1 = threading.Thread(target=self.loading)

        thread.start()
        thread1.start()

        self.thread_list.append(thread)
        self.thread_list.append(thread1)

        for th in self.thread_list:
            th.join()
        self.show_entry_fields()

    def show_entry_fields(self):
        print(self.ans)
        self.flag = 0
        for i in range(len(self.ans)):
            if self.flag == 0:
                Label(self.window, text="Model", font=("Arial", 15), background="white", foreground="#000099").grid(row=10 + i, column=0, padx=25, pady=10)
                Label(self.window, text="Original Price", font=("Arial", 15), background="white", foreground="#000099").grid(row=10 + i, column=1, padx=25, pady=10)
                Label(self.window, text="Flipkart Price", font=("Arial", 15), background="white", foreground="#000099").grid(row=10 + i, column=2, padx=25, pady=10)
                Label(self.window, text="Rating", font=("Arial", 15), background="white", foreground="#000099").grid(row=10 + i, column=3, padx=25, pady=10)
                Label(self.window, text="Number of Reviews", font=("Arial", 15), background="white",foreground="#000099").grid(row=10 + i, column=4, padx=25, pady=10)
                Label(self.window, text="Link", font=("Arial", 15), background="white", foreground="#000099").grid(row=10 + i, column=5, padx=25, pady=10)
                self.flag = 111

            if len(self.ans[i][0]) > 40:
                titletemp = self.ans[i][0][:40] + '...'
            else:
                titletemp = self.ans[i][0]

            b1 = Label(self.window, text=titletemp, font=("Arial", 12), background="white", foreground="black")  # assign price 1
            b1.grid(row=12 + i, column=0, padx=25, pady=10)
            b2 = Label(self.window, text=self.ans[i][1], font=("Arial", 12), background="white", foreground="black")  # assign price 1
            b2.grid(row=12 + i, column=1, padx=25, pady=10)
            b3 = Label(self.window, text=self.ans[i][2], font=("Arial", 12), background="white", foreground="black")  # assign price 2
            b3.grid(row=12 + i, column=2, padx=25, pady=10)
            b4 = ttk.Label(self.window, text=self.ans[i][3], font=("Arial", 12), background="white", foreground="black")  # assign ratings
            b4.grid(row=12 + i, column=3, padx=25, pady=10)
            b5 = ttk.Label(self.window, text=self.ans[i][4], font=("Arial", 12), background="white", foreground="black")  # assign reviews
            b5.grid(row=12 + i, column=4, padx=25, pady=10)
            b6 = tk.Button(self.window, text="Click Here to know more", bg="white", fg="blue", command=lambda aurl=self.ans[i][5]: self.callback(aurl))
            b6.grid(row=12 + i, column=5, padx=25, pady=10)


obj = GUI()
obj.start()