
import sys
import datetime
sys.path.insert(0, 'C:/Users/Admin/Desktop/py/notes')
import note_controller
from cgi import print_arguments


class View(object):
    
    __controller = note_controller.Controller(object)
    
    def __init__(self, controller):
        self.__controller = controller
        
    def create_note(self):
        new_note = []
        new_note.append(input ("Введите название \n" )) 
        new_note.append(input ("Введите текст \n" )) 
        new_note.append(datetime.datetime.today().strftime("%Y-%d-%m"))
        return new_note   
        

    def run(self):

        print("Используйте следующие команды: \n") 
        note_commands = ["none","commands","read","create","sort", "update","list","delete","exit"]
        print("\n") 
        
        for i in note_commands:
            print(i)
        
        print("\n")
        command = "none"
        
        while (command!='exit'):
            command = input ("Введите команду: \n" )
            
            if command in note_commands:
                match command:
                    case "none":
                        pass
                    
                    case "commands":
                        print("\n")
                        for i in note_commands:
                            print(i)
                    
                    case "read":
                        r_note = input ("Введите номер заметки: ")
                        print(self.__controller.read_note(r_note))
                        
                    case "create":
                        new_note = self.create_note()
                        self.__controller.write_note(new_note)
                        print("Заметка сохранена")
                        
                    case "update":
                        up_note = input ("Введите номер заметки: ")
                        red_note = input ("Новый текст редактируемой заметки: ")
                        new_date = datetime.datetime.today().strftime("%d-%m-%Y")
                        self.__controller.change_note(up_note, red_note, new_date)
                        
                    case "sort":
                        print("Введите даты в формате гггг-дд-мм")
                        
                        try:
                            date1 = input ("От  " )
                            date2 = input ("До  " )                         
                            if ex_r_format(date1) and ex_r_format(date2):
                                print(self.__controller.choice_date_notes(date1, date2))
                        except FormatDateError as e:
                            print(f"Ошибка ввода: {e}.")       
                            
                            
                        print("\n \n")
                        
                    case "list":
                        print(self.__controller.read_all_notes())
                    
                    case "delete":
                        del_note = input("Введите ID удаляемой заметки: \n")
                        self.__controller.delete_note(del_note)
                        
                    case "exit":
                        pass
                    
            else:
                print("Command error") 
                
                
                
    def r_format(str_date):
        mas = ["1","2","3","4","5","6","7","8","9","0","-"]
        count = 0
        if str_date[4]!="-" or str_date[7]!="-":
            return False
        while count < len(str_date):
            if str_date[count] not in mas:
                return False
        return True
    
    
    
class FormatDateError(Exception):
    pass
    
def ex_r_format(str_date):
    mas = ["1","2","3","4","5","6","7","8","9","0","-"]
    count = 0
    if str_date[4]=="-" and str_date[7]=="-":
        while count < len(str_date):
            if str_date[count] in mas:
                count=count+1
        if count == len(str_date):
            return True
            
    raise FormatDateError(" Неверный формат ввода даты")
                    