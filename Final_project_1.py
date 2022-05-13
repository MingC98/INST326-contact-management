"""Overall function docstring"""
import tkinter as tk
import sqlite3
"""
Create and connect to the sql database, must be global
"""
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cq = '''CREATE TABLE contacts(
        name TEXT, number TEXT, address TEXT
        )'''
cursor.execute(cq)


        
class ContactWindow:
    
    def __init__(self, name, number, address):
        self.branch2= tk.Tk()
        self.canvas2 = tk.Canvas(self.branch2, width = 400, height = 100,  relief = 'raised')
        self.canvas2.pack()
        self.name = name
        self.number = number
        self.address = address
        display_string = "Name: " + str(self.name) + "\nNumber: " + str(self.number) + "\nAddress: " + str(self.address) + "\n\n"
        labelz = tk.Label(self.branch2, text=display_string)
        labelz.config(font=('helvetica', 14))
        self.canvas2.create_window(200, 25, window=labelz)
        labelz.pack()

        

def save_contact(person):
    """this function stores a new contact person in a database
    Parameter: person: a tuple contains name,number,address
    """
    imq = '''INSERT INTO contacts VALUES(?,?,?)'''
    cursor.execute(imq,person)
    print('saved')
    pass

def get_contacts():
    """this function retrieves the contacts from the database 
    and returns them as a list of tuples"""
    #test_return = [("bob", "123", "Cherry lane"), ("alice", "456","pond road")]
    #print(test_return)
    #return test_return
    sq = '''SELECT * FROM contacts'''
    m_contacts = cursor.execute(sq).fetchall()
    print(m_contacts)
    return m_contacts
    
class MainWindow:
    def __init__(self):
        
        self.root= tk.Tk()
        self.canvas1 = tk.Canvas(self.root, width = 400, height = 100,  relief = 'raised')
        self.canvas1.pack()
        self.contact_button_list = []
        self.contact_window_button_list = []

        label1 = tk.Label(self.root, text='Contacts')
        label1.config(font=('helvetica', 14))
        self.canvas1.create_window(200, 25, window=label1)
        label1.pack()
   
        label2 = tk.Label(self.root, text='Enter contact name:')
        label2.config(font=('helvetica', 10))
        self.canvas1.create_window(200, 100, window=label2)
        label2.pack()

        entry1 = tk.Entry (self.root) 
        self.canvas1.create_window(200, 140, window=entry1)
        entry1.pack()

        label3 = tk.Label(self.root, text='Enter contact number:')
        label3.config(font=('helvetica', 10))
        self.canvas1.create_window(200, 100, window=label3)
        label3.pack()

        entry2 = tk.Entry (self.root) 
        self.canvas1.create_window(200, 140, window=entry2)
        entry2.pack()

        label4 = tk.Label(self.root, text='Enter contact address:')
        label4.config(font=('helvetica', 10))
        self.canvas1.create_window(200, 100, window=label4)
        label4.pack()

        entry3 = tk.Entry (self.root) 
        self.canvas1.create_window(200, 140, window=entry3)
        entry3.pack()
    
        label6 = tk.Label(self.root, text="")
        label6.config(font=('helvetica', 10))
        self.canvas1.create_window(200, 100, window=label6)
        label6.pack()
    
        button1 = tk.Button(text='save contact', command=lambda:self.save_response(entry1.get(), entry2.get(), entry3.get()), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(200, 180, window=button1)
        button1.pack()

        button3 = tk.Button(text='delete contact', command=lambda:self.delete_contact(entry1.get(), entry2.get()), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(200, 180, window=button3)
        button3.pack()

        self.root.mainloop()
    
    def save_response(self,name, number, address):
        """this function takes the entered name, number, and address,
        stores it in a person class, informs the user that it has been saved,
        and passes it off to the save_contact function"""
        #newPerson = People(name, number, address)
        newPerson = (name,number,address)
        label5 = tk.Label(self.root, text='Contact has been saved')
        label5.config(font=('helvetica', 10))
        self.canvas1.create_window(200, 100, window=label5)
        label5.pack()
        save_contact(newPerson)
        self.display_contacts()
        
    def display_contacts(self):
        contacts = get_contacts()
        for j in self.contact_button_list:
            j.destroy()
        for i in range(len(contacts)):
            name = contacts[i][0]
            b=[0 for x in range(len(contacts))]
            button_test = tk.Button(self.root, text = name, command=lambda i=i: self.new_window(contacts[i][0], contacts[i][1], contacts[i][2]))
            self.contact_button_list.append(button_test)
            b[i] = button_test
            b[i].pack()
            
    def new_window(self, name, number, address):
        wind = ContactWindow(name, number, address)
            

    def delete_contact(self, m_name,m_number):
        """Delete contact with same name and number"""
        dq=f'''DELETE FROM contacts
            WHERE name = '{m_name}' AND number = '{m_number}' '''
        cursor.execute(dq)
        self.display_contacts()

def main():
    MainWindow()

if __name__ == "__main__":
    main()
        
    
