import Final_project_1 as f


def test_window():
    """
    Test the window
    """
    m = f.MainWindow()
    #Display contacts should be a empty list
    assert m.get_contacts() == []
    #Delete with no object in the list
    m.delete_contact('Ming',123)
    assert m.get_contacts() == []
    #Add with nothing
    person = ('','','')
    m.save_contact(person)
    assert m.get_contacts() == [('','','')]
    #Save with only name
    person = ('Ming','','')
    m.save_contact(person)
    assert m.get_contacts() == [('','',''),('Ming','','')]
    #Save duplicate contact
    m.save_contact(person)
    assert m.get_contacts() == [('','',''),('Ming','','')]
    
    

test_window()
    