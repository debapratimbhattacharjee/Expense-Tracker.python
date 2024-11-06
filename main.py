from tkinter import *
from tkinter import ttk
import datetime as dt
from mydb import *
from tkinter import messagebox

class DailyExpensesApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Daily Expenses')
        self.root.geometry('900x600')
        
        # Database object
        self.data = Database(db='test.db')
        
        # Global variables
        self.count = 0
        self.selected_rowid = 0
        
        # Variables
        self.f = ('Times new roman', 14)
        self.namevar = StringVar()
        self.amtvar = IntVar()
        self.dopvar = StringVar()
        
        # Set up the UI
        self.create_widgets()
        self.fetch_records()
        
    def create_widgets(self):
        # Frame for input fields
        f1 = Frame(self.root, padx=10, pady=10, bg='#2B2B2B')
        f1.pack(expand=True, fill=BOTH)

        # Labels
        Label(f1, text='ITEM NAME', font=self.f, bg='#2B2B2B', fg='#FFFFFF').grid(row=0, column=0, sticky=W)
        Label(f1, text='ITEM PRICE', font=self.f, bg='#2B2B2B', fg='#FFFFFF').grid(row=1, column=0, sticky=W)
        Label(f1, text='PURCHASE DATE', font=self.f, bg='#2B2B2B', fg='#FFFFFF').grid(row=2, column=0, sticky=W)

        # Entry widgets
        self.item_name = Entry(f1, font=self.f, textvariable=self.namevar, bg='#333333', fg='#FFFFFF', relief='flat')
        self.item_amt = Entry(f1, font=self.f, textvariable=self.amtvar, bg='#333333', fg='#FFFFFF', relief='flat')
        self.transaction_date = Entry(f1, font=self.f, textvariable=self.dopvar, bg='#333333', fg='#FFFFFF', relief='flat')
        self.item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
        self.item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
        self.transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))

        # Action buttons with color scheme
        btn_style = {'bg': '#007BFF', 'fg': 'white', 'font': self.f, 'relief': 'flat'}
        Button(f1, text='Current Date', command=self.set_date, **btn_style).grid(row=3, column=1, sticky=EW, padx=(10, 0))
        Button(f1, text='Save Record', command=self.save_record, **btn_style).grid(row=0, column=2, sticky=EW, padx=(10, 0))
        Button(f1, text='Clear Entry', command=self.clear_entries, **btn_style).grid(row=1, column=2, sticky=EW, padx=(10, 0))
        Button(f1, text='Exit', command=self.root.destroy, bg='#DC3545', fg='white', font=self.f, relief='flat').grid(row=2, column=2, sticky=EW, padx=(10, 0))
        Button(f1, text='Total Balance', command=self.total_balance, **btn_style).grid(row=0, column=3, sticky=EW, padx=(10, 0))
        Button(f1, text='Update', command=self.update_record, bg='#FFC107', fg='black', font=self.f, relief='flat').grid(row=1, column=3, sticky=EW, padx=(10, 0))
        Button(f1, text='Delete', command=self.delete_row, bg='#DC3545', fg='white', font=self.f, relief='flat').grid(row=2, column=3, sticky=EW, padx=(10, 0))

        # Frame for Treeview widget
        f2 = Frame(self.root)
        f2.pack()

        # Treeview widget
        self.tv = ttk.Treeview(f2, columns=(1, 2, 3, 4), show='headings', height=8)
        self.tv.pack(side="left")
        self.tv.column(1, anchor=CENTER, stretch=NO, width=70)
        self.tv.column(2, anchor=CENTER)
        self.tv.column(3, anchor=CENTER)
        self.tv.column(4, anchor=CENTER)
        self.tv.heading(1, text="Serial no")
        self.tv.heading(2, text="Item Name")
        self.tv.heading(3, text="Item Price")
        self.tv.heading(4, text="Purchase Date")
        self.tv.bind("<ButtonRelease-1>", self.select_record)

        # Style for Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'))
        style.configure("Treeview", background="#333333", foreground="white", rowheight=25, fieldbackground="#333333")
        style.map("Treeview", background=[('selected', '#007BFF')], foreground=[('selected', 'white')])

        # Scrollbar
        scrollbar = Scrollbar(f2, orient='vertical')
        scrollbar.configure(command=self.tv.yview)
        scrollbar.pack(side="right", fill="y")
        self.tv.config(yscrollcommand=scrollbar.set)

    def save_record(self):
        self.data.insertRecord(item_name=self.item_name.get(), item_price=self.item_amt.get(), purchase_date=self.transaction_date.get())
        self.refresh_data()

    def set_date(self):
        date = dt.datetime.now()
        self.dopvar.set(f'{date:%d %B %Y}')

    def clear_entries(self):
        self.item_name.delete(0, 'end')
        self.item_amt.delete(0, 'end')
        self.transaction_date.delete(0, 'end')

    def fetch_records(self):
        records = self.data.fetchRecord('select rowid, * from expense_record')
        for rec in records:
            self.tv.insert(parent='', index='0', iid=self.count, values=(rec[0], rec[1], rec[2], rec[3]))
            self.count += 1
        self.tv.after(400, self.refresh_data)

    def select_record(self, event):
        selected = self.tv.focus()
        val = self.tv.item(selected, 'values')
        if val:
            self.selected_rowid = val[0]
            self.namevar.set(val[1])
            self.amtvar.set(val[2])
            self.dopvar.set(str(val[3]))

    def update_record(self):
        try:
            self.data.updateRecord(self.namevar.get(), self.amtvar.get(), self.dopvar.get(), self.selected_rowid)
            self.refresh_data()
        except Exception as ep:
            messagebox.showerror('Error', ep)
        self.clear_entries()

    def total_balance(self):
        total = self.data.fetchRecord(query="Select sum(item_price) from expense_record")
        for i in total:
            for j in i:
                messagebox.showinfo('Current Balance:', f"Total Expense: {j} \nBalance Remaining: {5000 - j}")

    def refresh_data(self):
        for item in self.tv.get_children():
            self.tv.delete(item)
        self.fetch_records()

    def delete_row(self):
        self.data.removeRecord(self.selected_rowid)
        self.refresh_data()

if __name__ == "__main__":
    root = Tk()
    app = DailyExpensesApp(root)
    root.mainloop()
