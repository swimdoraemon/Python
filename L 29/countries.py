class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of india")
    
    def type(self):
        print("India is a devoloping country")



class Japan():
    def capital(self):
        print("Tokyo is the capital of Japan.")

    def language(self):
        print("Japanese is the most widely spoken language of Japan")
    
    def type(self):
        print("Japan is a devoloped country")


obj_ind = India()
obj_jp = Japan()

for country in (obj_ind, obj_jp):
    country.capital()
    country.language()
    country.type()

    

