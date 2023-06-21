import sys


sys.path.insert(0, 'C:/Users/Admin/Desktop/py/notes')
import file_repository


class Controller(object):
    
   
    
    
    
    def __init__(self, repository):
        self.__new_repository = repository
    
    def read_note(self, id_note):
        try:
            return self.__new_repository.find_note(id_note)
        except ValueError:
            print ("Неверный ввод ID")
    
    def change_note(self, id_note, ch_note, red_date):
        self.__new_repository.change_note(id_note, ch_note, red_date)
    
    def choice_date_notes(self, date1, date2):
        return self.__new_repository.choice_date_notes(date1, date2)
    
    def write_note(self, new_note):
        self.__new_repository.write_data(new_note)
    
    def read_all_notes(self):
        return self.__new_repository.print_data()
    
    def delete_note(self, id_note):
        self.__new_repository.delete_data(id_note)
    
    
