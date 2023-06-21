

class Note(object):
    
    
    # Поля
    
    id_Note = ""
    title_Note = ""
    text_Note = ""
    date_Note = ""
    
    # Инициализация
    
    def __init__(self, id_Note, title_Note, text_Note, date_Note):
        self.__id_Note = id_Note
        self.__title_Note = title_Note
        self.__text_Note = text_Note
        self.__date_Note = date_Note
    
    # Геттеры
    
    def get_Id(self):
        return self.__id_Note
    
    def get_Title(self):
        return self.__title_Note
    
    def get_Text(self):
        return self.__text_Note
    
    def get_Date(self):
        return self.__date_Note 
    
    # Сеттеры
    
    def set_id(self, new_Id):
        self.__id_Note = new_Id
    
    def set_id(self, new_Title):
        self.__title_Note = new_Title
    
    def set_id(self, new_Text):
        self.__text_Note = new_Text
    
    def set_id(self, new_Date):
        self.__date_Note = new_Date
        
    
    
    # def __str__(self):
    #     print_Note = f" Note №{self.__id_Note}\n{self.__title_Note}\n{self.__text_Note}\n Date of change: {self.__date_Note}"
    #     return print_Note
    
    

    