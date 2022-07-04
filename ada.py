import tkinter as tk
from tkinter import ttk
from tkinter import *
from ctypes import windll
from tkinter.messagebox import askyesno
import mysql.connector
from tkinter.font import Font
from tkinter.messagebox import showinfo
import webbrowser
import smtplib
# import numpy as np
# import matplotlib.pyplot as plt

# plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="companyx"
)
myCursor = mydb.cursor()

windll.shcore.SetProcessDpiAwareness(1)


class Graph:
    def __init__(self, vertex: object):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:", u, v, end=" ")
            print("-", weight)

        return result


g = Graph(5)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)
g.kruskal()


def callback(url):
    webbrowser.open_new(url)

class readArticle(tk.Toplevel):
    def __init__(self,parent):
        super(). __init__(parent)

        self.title ("Articles")
        self.geometry("2500x2500")
        self.config (bg ="black")

        self.myfont = Font(
            family="corbel",
            size=10,
            weight="bold"
        )

        self.bg = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\nightn.png")

        Label (self, image=self.bg).place(x=0,y=0)
        self.frame = LabelFrame(self, text='HELPFUL ARTICLES',
                                font=self.myfont, padx=20, pady=20, bg="black",
                                fg="red")

        self.frame.place(x=100, y=100)

        link1 = Label(self.frame, text="Graphs in Data Structure: Overview, Types and More ...",
                      fg="#f0dc06", cursor="hand2", font=("Arial",12),bg="black")
        link1.grid (column=0, row = 0, sticky=W,pady = 5)
        link1.bind("<Button-1>", lambda e: callback("https://www.simplilearn.com/tutorials/data-structure-tutorial/graphs-in-data-structure"))
        link1 = Label(self.frame, text="Graphs in data structures are non-linear data structures made up of a finite number of nodes or vertices and the edges that connect them. Graphs in data structures are used to address real-world problems\n"
                                       "in which it represents the problem area as a network like telephone networks, circuit networks, and social networks.                                                                                                                                 ",
                      fg="white", cursor="hand2", font=("Arial", 10), bg="black")
        link1.grid(column=0, row=1, sticky=W, pady=10)

        link2 = Label(self.frame, text="Graph in Data Structure | Learn the Terminologies and...",
                      fg="#f0dc06", cursor="hand2", font=("Arial",12),bg="black")
        link2.grid(column=0,row=10,sticky=W,pady = 5)
        link2.bind("<Button-1>", lambda e: callback("https://www.educba.com/graph-in-data-structure/"))
        link1 = Label(self.frame,
                      text="Conclusion - Graph in Data Structure. Graphs are a beneficial concept in data structures. It has practical implementations in almost every field. Therefore, it is essential to understand the basics of graph theory to\n"
                           "understand the graph structure's algorithms. This article was merely an introduction to graphs. It is just a stepping stone.                                                                                                                                   "
                      ,fg="white", cursor="hand2", font=("Arial", 10), bg="black")
        link1.grid(column=0, row=11, sticky=W, pady=10)

        link1 = Label(self.frame, text="What is a Minimum Spanning Tree? - OpenGenus IQ: Computing",
                      fg="#f0dc06", cursor="hand2", font=("Arial",12),bg="black")
        link1.grid (column=0, row = 20, sticky=W,pady =5)
        link1.bind("<Button-1>", lambda e: callback("https://iq.opengenus.org/what-is-a-minimum-spanning-tree/"))
        link1 = Label(self.frame,
                      text="A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted directed or undirected graph that connects all the vertices together, without any cycles and with the\n"
                           "minimum possible total edge weight. It is a spanning tree whose sum of edge weights is as small as possible. More generally, any edge-weighted undirected graph (not necessarily                                                                "
                      , fg="white", cursor="hand2", font=("Arial", 10), bg="black")
        link1.grid(column=0, row=21, sticky=W, pady=10)

        link1 = Label(self.frame, text="Properties of Minimum Spanning Tree (MST) - GeeksforGeeks",
                      fg="#f0dc06", cursor="hand2", font=("Arial", 12), bg="black")
        link1.grid(column=0, row=30, sticky=W, pady=5)
        link1.bind("<Button-1>", lambda e: callback("https://www.geeksforgeeks.org/properties-of-minimum-spanning-tree-mst/"))
        link1 = Label(self.frame,
                      text="For a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. A single graph can have multiple spanning trees. A Minimum Spanning Tree(MST) or \n"
                           "minimum weight spanning tree for a weighted, connected, undirected graph is a spanning tree having a weight less than or equal to the weight of every other possible spanning tree.                                                             ",
                      fg="white", cursor="hand2", font=("Arial", 10), bg="black")
        link1.grid(column=0, row=31, sticky=W, pady=10)

        link1 = Label(self.frame, text="Minimum Spanning Tree Tutorials & Notes | Algorithms",
                      fg="#f0dc06", cursor="hand2", font=("Arial", 12), bg="black")
        link1.grid(column=0, row=40, sticky=W, pady=5)
        link1.bind("<Button-1>", lambda e: callback("https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/"))
        link1 = Label(self.frame,
                      text="Minimum spanning tree is the spanning tree where the cost is minimum among all the spanning trees. There also can be many minimum spanning trees. Minimum spanning tree has direct application in the design of networks. \n"
                           "It is used in algorithms approximating the travelling salesman problem, multi-terminal minimum cut problem and minimum-cost                                                                                                                                                   "
                      , fg="white", cursor="hand2", font=("Arial", 10), bg="black")
        link1.grid(column=0, row=41, sticky=W, pady=10)

class watchVideo(tk.Toplevel):
    def __init__(self,parent):
        super(). __init__(parent)

        self.title("Articles")
        self.geometry("500x500")
        self.config(bg="black")

        self.myfont = Font(
            family="corbel",
            size=10,
            weight="bold"
        )

        self.bg = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\nightn.png")
        Label(self, image=self.bg).place(x=0, y=0)
        self.frame = LabelFrame(self, text='HELPFUL ARTICLES',
                                font=self.myfont, padx=20, pady=20, bg="black",
                                fg="red")

        self.frame.place(x=100, y=100)

        link1 = Label(self.frame, text="Watch video on: -Introduction to graphs",
                      fg="#f0dc06", cursor="hand2", font=("Arial", 12), bg="black")
        link1.grid(column=0, row=0, sticky=W, pady=5)
        link1.bind("<Button-1>", lambda e: callback(
            "https://www.youtube.com/watch?v=TwdjOQMTaQ4"))

        link2 = Label(self.frame, text=" Watch video on: -Kruskal Algo",
                      fg="#f0dc06", cursor="hand2", font=("Arial", 12), bg="black")
        link2.grid(column=0, row=1, sticky=W, pady=5)
        link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=huQojf2tevI"))

        link1 = Label(self.frame, text=" Watch video on: -Prims's Algo",
                      fg="#f0dc06", cursor="hand2", font=("Arial", 12), bg="black")
        link1.grid(column=0, row=2, sticky=W, pady=5)
        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/results?search_query=prims+algo"))




class MainWindow(tk.Toplevel):

    def open_article_window(self):
        window = readArticle(self)
        window.grab_set()

    def open_watch_video(self):
        window = watchVideo(self)
        window.grab_set()



    def CostRep(self):
        self.frame6= LabelFrame(self.frame, text="COST COMPARISON", font=self.myfont,
                                  bg="black", fg="red")
        self.frame6.grid (column = 40, row = 0, sticky = N, padx = 50, pady = 7)

        label1= Label (self.frame6, text = "COST BEFORE:", font = self.myfont
                       ,bg = "black", fg = "#f0dc06")
        label1.grid (column = 0, row = 0, sticky=W)

        label2 = Label (self.frame6, text = "COST AFTER:", font = self.myfont,
                        bg ="black", fg = "#f0dc06")
        label2.grid (column = 0, row = 1, sticky=W)


        label3 = Label(self.frame6, text=self.cost_before, font=self.buttonFont,
                       bg="black", fg="#f0dc06")
        label3.grid(column=1, row=0)

        label4 = Label(self.frame6, text=self.cost_after, font=self.buttonFont,
                       bg="black", fg="#f0dc06")
        label4.grid(column=1, row=1)

        label5 = Label(self.frame6, text="PERCENTAGE DECREASE:", font=self.myfont,
                       bg="black", fg="red")
        label5.grid(column=0, row=2, sticky=W)

        a = self.cost_before
        b = self.cost_after

        num = round(((a-b)/a)*100,2)

        label5 = Label(self.frame6, text=str(num)+"%", font=self.buttonFont,
                       bg="black", fg="red")
        label5.grid(column=1, row=2, sticky=W)


    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))

    def giveResult(self):
        nodes = int(self.vertices.get())
        print(type(nodes))
        self.g = Graph(nodes)

        for i in self.edges:
            self.g.add_edge(i[0],i[1],i[2])
            print (self.cost_after,i[2])


        r = self.g.kruskal()

        for i in r:
            self.cost_after=self.cost_after+i[2]

        print(r)
        print (self.cost_after)

        self.CostRep()

        self.frame3 = LabelFrame(self.frame, text="EFFECTIVE CONNECTIONS", font=self.myfont,
                                 padx=20, pady=20, bg="black", fg="red")
        self.frame3.grid(column=20, row=10, columnspan=5,sticky=tk.W)
        columns = ('FROM HOUSE', 'TO HOUSE', 'LENGTH')

        self.tree = ttk.Treeview(self.frame3, columns=columns, show='headings')

        # define headings
        # tree.heading('first_name', text='First Name')
        # tree.heading('last_name', text='Last Name')
        # tree.heading('email', text='Email')

        for i in columns:
            self.tree.heading(i, text=i)


        for row in r:
            self.tree.insert('', tk.END, values=row)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.grid(row=230, column=1000, sticky='nsew', rowspan=400, columnspan=100)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.frame3, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=230, column=2001, sticky='ns')

    def insertEdge(self):
        a = int(self.text1.get())
        b = int(self.text2.get())
        w = int(self.text3.get())

        self.cost_before = self.cost_before+w

        row = [a,b,w]
        self.tree2.insert('', tk.END, values=row)

        self.edges.append(row)


    def generateGraph(self):

        self.frame4 = LabelFrame(self.frame, text="GRAPH EDGES", font=self.myfont,
                                 padx=30, pady=10, bg="black", fg="red")

        # for i in range(10):
        #     label = Label(self.frame, text="", bg="black", fg="black")
        #     label.grid(column=i, row=0)

        self.frame4.grid(column=20, row=0, columnspan=10,
                         rowspan=10, sticky=W)
        columns = ('FROM HOUSE', 'TO HOUSE', 'LENGTH')

        self.tree2 = ttk.Treeview(self.frame4, columns=columns, show='headings')


        # define headings
        # tree.heading('first_name', text='First Name')
        # tree.heading('last_name', text='Last Name')
        # tree.heading('email', text='Email')

        for i in columns:
            self.tree2.heading(i, text=i)


        self.tree2.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree2.grid(row=230, column=1000, sticky='nsew', rowspan=400, columnspan=100)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.frame4, orient=tk.VERTICAL, command=self.tree2.yview)
        self.tree2.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=230, column=2002, sticky='ns')

        # for i in range(3):
        #     label = Label(self.frame, text="", bg="black", fg="black")
        #     label.grid(column=0, row=1+i)

        self.frame2 = LabelFrame (self.frame, text = "HOME CONNECTION", font = self.myfont,
                                  pady = 20,bg = "black", fg = "red")
        self.frame2.grid (column = 0, row = 10,sticky=W)

        for i in range(int(self.num_of_edges.get())):
            # label3 = Label(self.frame2, image=self.edges_img, bg="black", padx=10, pady=10)
            # label3.grid(column=0, row=5)
            label4 = Label(self.frame2, text="FROM", bg="black", font=self.myfont,fg="#f0dc06",padx = 10, pady = 10)
            label4.grid(column=0, row=6)

            self.text1 = tk.StringVar()
            from_entry = Entry(self.frame2, textvariable=self.text1,font=self.buttonFont)
            from_entry.grid(column=1, row=6)

            label4 = Label(self.frame2, text="TO", bg="black",font =self.myfont, fg="#f0dc06", padx=10, pady=10)
            label4.grid(column=0, row=7)

            self.text2 = tk.StringVar()
            to_entry = Entry(self.frame2, textvariable=self.text2,font=self.buttonFont)
            to_entry.grid(column=1, row=7)

            label5 = Label(self.frame2, text="LENGTH", bg="black",font=self.myfont, fg="#f0dc06", padx=10, pady=10)
            label5.grid(column=0, row=8)

            self.text3 = tk.StringVar()
            weight_entry = Entry(self.frame2, textvariable=self.text3, font= self.buttonFont)
            weight_entry.grid(column=1, row=8)

            label3 = Label(self.frame, text="", bg="black")
            label3.grid(column=1, row=9, padx=40)

            self.button1 = Button(self.frame2, text="INSERT EDGE INTO GRAPH", font=self.buttonFont, bg="#66FCf1",
                                  height=1,
                                  width=25)
            self.button1.config(command=self.insertEdge)
            self.button1.grid(column=1, row=10, padx=40, pady=20)






        button1 = Button(self.frame2, text="RESULT", font=self.buttonFont, bg="red", height=1,
                         width=25, fg = "white")
        button1.config(command=self.giveResult)
        button1.grid(column=1, row=12, padx=40)


    def __init__(self, parent):
        super().__init__(parent)

        self.frame6 = None
        self.button1 = None
        self.text1 = None
        self.g = None
        self.text2 = None
        self.text3 = None
        self.edges = []
        self.cost_before = 0
        self.cost_after = 0

        self.title("Main window")
        self.geometry("2000x2000")
        self.config(bg="black")

        self.myfont = Font(
            family="corbel",
            size=10,
            weight="bold"
        )

        self.linkfont = Font(
            family="corbel",
            size=12,
            weight="bold"
        )

        self.buttonFont = Font(
            family="Arial",
            size=9,
            weight="bold"
        )

        self.logo = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\ada logo.png")
        logo_frame = Frame (self,width=10, height=10, borderwidth=0, bg = "black")
        # ogo_frame['padding']=(5,20,5,20)
        logo_frame.grid (column=0,row=0)

        label =Label(logo_frame,image=self.logo,bg = "black")
        label.grid (column = 0, row=0, padx = 10, pady = 10)

        link1 = Button (logo_frame,text="READ\nARTICLES", bg = "black", fg = "#66FCf1",
                        font =self.linkfont, command=self.open_article_window)
        link1.grid (column = 0, row = 1, padx = 10, pady = 20)

        link1 = Button(logo_frame, text="WATCH\nVIDEOS", bg="black", fg="#66FCf1",
                       font=self.linkfont, command=self.open_watch_video)
        link1.grid(column=0, row=2, padx=10, pady=20)

        link1 = Button(logo_frame, text="PROJECT\nREPORT", bg="black", fg="#66FCf1",
                       font=self.linkfont)
        link1.grid(column=0, row=3, padx=10, pady=20)



        self.bg = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\new.png")

        label1 = Label(self, image=self.bg, bg="black")
        label1.image = self.bg
        label1.place (x = 0, y = 500)


        self.frame = LabelFrame(self, text='ELECTRIC GRID DESIGN',
                                font=self.myfont, padx=20, pady=20, bg="black",
                                fg="white")

        self.frame.place (x = 250, y = 100)

        self.new_frame = LabelFrame(self.frame, text="AREA DETAILS", font=self.myfont,
                                 padx=20, pady=20, bg="black", fg="red")
        self.new_frame.grid (column =0, row = 0)


        self.user_img = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\home.png")
        self.pass_img = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\line.png")
        self.edges_img = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\edges.png")

        label1 = Label(self.new_frame, image=self.user_img, bg="black", padx=10, pady=10)
        label1.grid(column=0, row=0)
        label2 = Label(self.new_frame, image=self.pass_img, bg="black", padx=10, pady=10)
        label2.grid(column=0, row=1)

        self.vertices = tk.StringVar()
        self.num_of_edges = tk.StringVar()

        vertices_entry = ttk.Entry(self.new_frame, textvariable=self.vertices, font=self.buttonFont)
        vertices_entry.focus()
        vertices_entry.grid(column=1, row=0, padx=40, pady=10)

        num_of_edges_entry = ttk.Entry(self.new_frame, textvariable=self.num_of_edges, font=self.buttonFont)
        num_of_edges_entry.grid(column=1, row=1, padx=40, pady=10)

        # label3 = Label(self.new_frame, text="", bg="black")
        # label3.grid(column=1, row=2)

        button1 = Button(self.new_frame, text="GENERATE GRAPH", font=self.buttonFont, bg="#66FCf1", height=1, width=30)
        button1.config(command=self.generateGraph)
        button1.grid(column=1, row=3, padx=40, pady = 20)

        # label3 = Label(self.new_frame, text="", bg="black")
        # label3.grid(column=1, row=4, padx=40)
        # label3 = Label(self.new_frame, text="", bg="black")
        # label3.grid(column=1, row=5, padx=40)







class LoginPage(tk.Toplevel):
    def LoginPressed(self):
        print(self.username.get(), self.password.get())
        window = MainWindow(self)
        window.grab_set()

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Login")
        self.geometry("800x533")

        myfont = Font(
            family="corbel",
            size=10,
            weight="bold"
        )
        buttonFont = Font(
            family="Arial",
            size=9,
            weight="bold"
        )
        # self.bg = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\nightn.png")
        self.bg = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\electric background.png")

        self.my_canvas = Canvas(self, width=1500, height=1500, background="black")
        self.my_canvas.pack(fill="both", expand=True)

        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.logo = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\ada logo.png")
        self.user_img = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\username.png")
        self.pass_img = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\password.png")

        self.frame = LabelFrame(self.my_canvas, text='LOGIN DETAILS',
                                font=myfont, padx=20, pady=20, bg="black",
                                fg="white")

        label1 = Label(self.frame, image=self.user_img, bg="black", padx=10, pady=10)
        label1.grid(column=0, row=0)
        label2 = Label(self.frame, image=self.pass_img, bg="black", padx=10, pady=10)
        label2.grid(column=0, row=1)
        # self.my_canvas.create_image(300, 400, image=self.logo)
        # self.my_canvas.create_text(300,500, text="ELECTRIFY", font = login_font, fill = "#66FCf1")
        # label = Label (self.frame,text ="hi")
        # label.grid(column = 0, row = 0)
        self.my_canvas.create_window(360, 255, window=self.frame)

        # self.my_canvas.create_text(300,300, text = "Username", font = myfont,fill = "#f0dc06")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        username_entry = ttk.Entry(self.frame, textvariable=self.username, font=buttonFont)
        username_entry.focus()
        username_entry.grid(column=1, row=0, padx=40, pady=10)
        # self.my_canvas.create_window(305,300,window = username_entry)
        # # password
        # self.my_canvas.create_text(300,305, text="Password:", font=("Arial", 12))
        #
        password_entry = ttk.Entry(self.frame, textvariable=self.password, show="*", font=buttonFont)
        password_entry.grid(column=1, row=1, padx=40, pady=10)
        # self.my_canvas.create_window(305,305,window = password_entry)
        # # login button
        # login_button = ttk.Button(self, text="Login", command=self.returnKeyPressed)
        # # login_button.bind ('<Return>', returnKeyPressed)
        # self.my_canvas.create_window(310,310,window=login_button)
        label3 = Label(self.frame, text="", bg="black")
        label3.grid(column=1, row=2, padx=40)

        button1 = Button(self.frame, text="LOGIN", font=buttonFont, bg="#66FCf1", height=1, width=8)
        button1.config(command=self.LoginPressed)
        button1.grid(column=1, row=3, padx=40)


class App(tk.Tk):
    def send_message(self):
        address_info = self.address.get()

        # email_body_info = email_body.get()

        # print(address_info, email_body_info)

        sender_email = "devil2001bc@gmail.com"

        sender_password = "passwordisme1602."

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender_email, sender_password)

        print("Login successful")
        email_body_info = "Thank you for choosing us!"
        server.sendmail(sender_email, address_info, email_body_info)

        print("Message sent")

        address_entry.delete(0, END)
        email_body_entry.delete(0, END)

    def buttonClicked(self):
        window = LoginPage(self)
        window.grab_set()

    def __init__(self):
        super().__init__()
        self.title("Electric grid generator")
        self.geometry("1600x1500")
        self.config(bg="black")
        # self. resizable(0,0)

        loginFont = Font(
            family="Franklin Gothic Heavy",
            size=50,
        )

        buttonFont = Font(
            family="Arial",
            size=10,
            weight="bold"
        )

        self.bg = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\ada login 1600.png")
        self.logo = PhotoImage(file=r"C:\Users\piyush chauhan\Pictures\ada logo.png")

        self.my_canvas = Canvas(self, width=1500, height=1500, background="black")
        self.my_canvas.pack(fill="both", expand=True)

        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.my_canvas.create_image(30, 40, image=self.logo)
        self.my_canvas.create_text(190, 300, text="Let's",
                                   font=loginFont, fill="white")
        self.my_canvas.create_text(490, 300, text="Enlighten",
                                   font=loginFont, fill="#f0dc06")
        self.my_canvas.create_text(473, 320, text="\nIndian Households!",
                                   font=loginFont, fill="white")
        self.my_canvas.create_text(210, 420, text="\nAN INDIAN GOVT. INITIATIVE",
                                   font=("Arial", 10), fill="white")

        pixel = tk.PhotoImage(width=1, height=1)
        self.my_canvas.create_text(200,500,text="ENTER YOUR EMAIL ID:",fill="yellow",font=("corbel",12,"bold"))
        self.my_canvas.create_text(500, 535, text="OR", fill="yellow", font=("corbel", 9, "bold"))

        self.address = tk.StringVar()

        entry = Entry(self,textvariable=self.address, font=("arial",12,"bold"))
        self.my_canvas.create_window(205,535,window=entry)
        button1 = Button(self, text="REGISTER", font=buttonFont, bg="#66FCf1", height=1, width=10)
        button1.config(command=self.send_message)

        # button1 = Button(self,text = "login", command = self.buttonClicked)
        button_window = self.my_canvas.create_window(400, 535, window=button1)

        self.my_canvas.create_window(205, 535, window=entry)
        button1 = Button(self, text="LOGIN", font=buttonFont, bg="red",fg="white", height=1, width=10)
        button1.config(command=self.buttonClicked)
        button_window = self.my_canvas.create_window(540, 535, window=button1)


if __name__ == "__main__":
    app = App()
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    app.mainloop()





def send_message():
    address_info = address.get()

    email_body_info = email_body.get()

    print(address_info, email_body_info)

    sender_email = "mayankcool890@gmail.com"

    sender_password = "mayanklife0&M"

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, sender_password)

    print("Login successful")

    server.sendmail(sender_email, address_info, email_body_info)

    print("Message sent")

    address_entry.delete(0, END)
    email_body_entry.delete(0, END)


app = Tk()

app.geometry("500x500")

app.title("Python Mail Send App")

heading = Label(text="Python Email Sending App", bg="yellow", fg="black", font="10", width="500", height="3")

heading.pack()

address_field = Label(text="Recipient Address :")
email_body_field = Label(text="Message :")

address_field.place(x=15, y=70)
email_body_field.place(x=15, y=140)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address, width="30")
email_body_entry = Entry(textvariable=email_body, width="30")

address_entry.place(x=15, y=100)
email_body_entry.place(x=15, y=180)

button = Button(app, text="Send Message", command=send_message, width="30", height="2", bg="grey")

button.place(x=15, y=220)
