from tkinter import *
from PIL import ImageTk, Image
from engine import load_obj
from fetch import fetch_column
from Heap import Heap
from tfidf import tf_idf, querySimilarity
from normalizer import normalize_query
import os

def onclick():
   pass


class SearchEngine:
    def __init__(self, tType, address):
        self.tokenize_type = tType
        self.address = address

        print("RUNNING ENGINE ...")
        self.inverted_index = load_obj("INVERTED INDEX " + self.tokenize_type + "_" + self.address)
        self.tfidfs = load_obj("CHAMPIONS " + self.tokenize_type + "_" + self.address)
        self.titles = fetch_column(self.address, 'title')

        self.gui = Tk(className='فونل')
        self.gui.geometry("1000x640")
        self.gui.configure(bg='white')

        self.scrollbar = Scrollbar(self.gui)
        self.scrollbar.pack( side = RIGHT, fill = Y )


        img = ImageTk.PhotoImage(Image.open("Logo.png"))
        self.panel = Label(self.gui, image = img, bg = "white")
        self.panel.pack()

        self.text = Text(self.gui, width = 40, height = 1, pady = 10, font = "IRANSans", bg = "#a3a3a3")
        self.text.tag_configure('tag-right', justify = "right")
        self.text.pack(side = "top")

        self.b = Button(self.gui, text='جستجو کن', command = self.callback, width = 10, height = 1, pady = 10, bg = "#a3a3a3").pack(side = "top")
        


        
        self.mylist = Listbox(self.gui, yscrollcommand = self.scrollbar.set, justify = "right", font = ("IranSans", 14), width = 70)
        for line in range(10):
            self.mylist.insert(END, "")

        

        self.mylist.pack( side = TOP)
        self.scrollbar.config( command = self.mylist.yview )

        self.gui.mainloop()


    def callback(self):
        print("GOT TOKEN ", self.text.get("1.0",END))
        queryToken = self.text.get("1.0",END).replace("\n", "").split(" ")
        queryToken = normalize_query(queryToken)
        print(queryToken)
        queryw = tf_idf(queryToken, self.inverted_index, False)

        h = Heap()    

        for i in range(len(self.tfidfs)):
            if bool(set(queryToken) & set(self.tfidfs[i].keys())):
                sim = querySimilarity(queryw, self.tfidfs[i])
                if sim != 0:
                    h.addnSort([i, sim])

        k = 10
        result = h.getFirstK(k)
        k = min(len(result), k)
        print(k)
        for i in range(k):
            print(self.titles[result[i][0]])
            self.mylist.delete(i)
            self.mylist.insert(i, self.titles[result[i][0]])

        
        

s = SearchEngine("simple", "ir-news-0-2.csv")

