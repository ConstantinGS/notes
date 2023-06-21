import csv
import pandas
import datetime


class Repository(object):
    
    def __init__(self, path):
        self.__path = path


# Вывод всех заметок в файле
    def print_data(self):
        print_text = ""
        try:
            with open(self.__path, encoding='utf-8') as r_file:
                reader_object = csv.reader(r_file, delimiter =";")
                for row in reader_object:
                    print_text+= f"\n {row[0]} \n {row[1]} \n {row[2]} \n {row[3]} \n"

            return print_text    
        except FileNotFoundError:
            print ("Файл не найден")
# Вывод заметки по номеру ID                              
    def find_note(self, id_note):
        ret_note = ""
        try:
            with open(self.__path, encoding='utf-8') as r_file:
                reader_object = csv.reader(r_file, delimiter =";")
                for i in reader_object:
                    if i[0]==id_note:
                        return f"\n {i[0]} \n {i[1]} \n {i[2]} \n {i[3]} \n"
        except FileNotFoundError:
            print ("Файл не найден")
            
# Запись заметки в файл
    def write_data(self, note):
            
        new_note = note
        id = 0
        count_id = 1
        id_s = []
        try:
            with open(self.__path, encoding='utf-8') as r_file:
                reader_object = csv.reader(r_file, delimiter =";")
                for i in reader_object:
                    id_s.append(int(i[0]))
                
                while(id==0):
                    
                    if (count_id in id_s):
                        count_id+=1
                    else:
                        id = count_id
        except FileNotFoundError:
            print ("Файл не найден")            
                
        new_note.insert(0, str(id))
        
        try:
            with open(self.__path,mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
                file_writer.writerow(new_note)
        except FileNotFoundError:
            print ("Файл не найден")
 
# Удаление заметки       
    def delete_data(self, id_note):
        new_file = []
        try:
            with open(self.__path, encoding='utf-8') as r_file:
                reader_object = csv.reader(r_file, delimiter =";")
                for i in reader_object:
                    if i[0]!=id_note:
                        new_file.append(i)
      
            with open(self.__path,mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
                for i in new_file:
                    file_writer.writerow(i)
        except FileNotFoundError:
            print ("Файл не найден")
             
 

   
   
# Редактировать заметку                            
    def change_note(self, id_note, ch_note, new_date):
        
        new_file = []
        try:
            with open(self.__path, encoding='utf-8') as r_file:
                reader_object = csv.reader(r_file, delimiter =";")
                for i in reader_object:
                    if i[0]!=id_note:
                        new_file.append(i)
                    else:
                        new_file.append([i[0],i[1],ch_note, new_date])                 
    
          
            with open(self.__path,mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
                for i in new_file:
                    file_writer.writerow(i)
                    
            print("Заметка обновлена \n")
            
        except FileNotFoundError:
            print ("Файл не найден")


#Выборка заметок по дате                                   
    def choice_date_notes(self, date1, date2):
        
        print_text = ""
        dict_notes = {"ID":[], "Title":[], "Text":[], "Dates":[]}
        try:
            with open(self.__path, encoding='utf-8') as r_file:
                reader_object = csv.reader(r_file, delimiter =";")
                for row in reader_object:
                    dict_notes.get("ID").append(row[0])
                    dict_notes.get("Title").append(row[1])
                    dict_notes.get("Text").append(row[2])
                    dict_notes.get("Dates").append(row[3])
                
                df = pandas.DataFrame({"ID":dict_notes.get("ID"),
                "Titles": dict_notes.get("Title"),
                "Text":dict_notes.get("Text")}, index = dict_notes.get("Dates") )        

                df_sort = df.sort_index().loc[date1:date2]
                for i in range (len(df_sort["Titles"])):
                    print_text+="№ "+ df_sort["ID"][i]+"\n"
                    print_text+=df_sort["Titles"][i]+"\n"
                    print_text+=df_sort["Text"][i]+"\n"
                    print_text+=df_sort.index[i]+"\n"
                    print_text+="\n"

            return print_text
        except FileNotFoundError:
            print ("Файл не найден")

