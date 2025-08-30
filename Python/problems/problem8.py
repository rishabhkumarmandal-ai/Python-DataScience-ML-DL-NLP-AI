letter = '''
Dear <|NAME|>,
you are selected!
Date: <|DATE|>'''
print(letter.replace("<|NAME|>","Rishabh").replace("<|DATE|>", "30/08/2025"))



# learn replace function
letter2 ='''
Dear Name,
Your are Selcetd!
Date: Date'''
print(letter2.replace("Name", "Rishabh").replace("Date", "30/08/2025"))


name ="rishabh   mandal"
print(name.find("   "))
