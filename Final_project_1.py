"""Overall function docstring"""
import tkinter as tk
import sqlite3
"""
Create and connect to the sql database
"""
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cq = '''CREATE TABLE contacts(
        name TEXT, number TEXT, address TEXT
        )'''
cursor.execute(cq)


        
class ContactWindow:
    def __init__(self, name, number, address):
        self.name = name
        print(self.name)
        
        

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

def delete_contact(name,contact):
    """Delete contact with same name and number"""
    dq='''DELETE
            FROM contacts
            WHERE name=name AND number=number'''
    cursor.execute(dq)
    
def main():
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 400, height = 100,  relief = 'raised')
    canvas1.pack()
    
    def save_response(name, number, address):
        """this function takes the entered name, number, and address,
        stores it in a person class, informs the user that it has been saved,
        and passes it off to the save_contact function"""
        #newPerson = People(name, number, address)
        newPerson = (name,number,address)
        label5 = tk.Label(root, text='Contact has been saved')
        label5.config(font=('helvetica', 10))
        canvas1.create_window(200, 100, window=label5)
        label5.pack()
        save_contact(newPerson)
        
    def display_contacts():
        contacts = get_contacts()
        contact_display_string = ""
        for i in range(len(contacts)):
            name = contacts[i][0]
            number = contacts[i][1]
            address = contacts[i][2]
            intermediate_display_string = "Name: " + str(name) + "\nNumber: " + str(number) + "\nAddress: " + str(address) + "\n\n"
            contact_display_string = contact_display_string + intermediate_display_string
            b=[0 for x in range(len(contacts))]
            b[i] = tk.Button(root, text = name, command=lambda : get_contacts())
            b[i].pack()
        label6["text"] = contact_display_string
        
        """b = [0 for x in range(5)]
        for i in range(5):
            b[i] = tk.Button(root, command=lambda : get_contacts())
            b[i].pack()"""
        
            

        #should iterate through contacts and make a button for each name
        #still working on that
        
    
    label1 = tk.Label(root, text='Contacts')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    label1.pack()
   
    label2 = tk.Label(root, text='Enter contact name:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)
    label2.pack()

    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry1)
    entry1.pack()

    label3 = tk.Label(root, text='Enter contact number:')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label3)
    label3.pack()

    entry2 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry2)
    entry2.pack()

    label4 = tk.Label(root, text='Enter contact address:')
    label4.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label4)
    label4.pack()

    entry3 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry3)
    entry3.pack()
    
    label6 = tk.Label(root, text="")
    label6.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label6)
    label6.pack()
    
    button1 = tk.Button(text='save contact', command=lambda:save_response(entry1.get(), entry2.get(), entry3.get()), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)
    button1.pack()

    button2 = tk.Button(text='display contacts', command=display_contacts, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button2)
    button2.pack()

    

    root.mainloop()
    
main()
