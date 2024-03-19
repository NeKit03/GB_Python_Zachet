import datetime
import csv
note = dict()

class Note:
    ID = 0  # Статическая переменная для индикатора заметки

    def __init__(self, heading, text):
        self.ID = Note.ID  # Присваиваем текущее значение индикатора заметки
        Note.ID += 1  # Увеличиваем индикатор для следующей заметки
        self.heading = heading
        self.text = text
        self.date_time = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")  

    def __str__(self):
        return f"{self.ID}) {self.date_time} {self.heading}\n{self.text}\n"

    def printNote(self):
        print(self.ID+')', self.date_time, self.heading)
        print(self.text)

class NoteManager:
    
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, "r") as file:
            A = file.readlines()
            for i in A:
                key = i.split(';')
                if key[0][:10] not in note:
                    note[key[0][:10]] = [Note(key[1], key[2])]
                    note[key[0][:10]][0].date_time=key[0] 

                else:
                    arr = note[key[0][:10]]  
                    arr.append(Note(key[1], key[2]))
                    arr[len(arr)-1].date_time=key[0]  
                    note[key[0][:10]] = arr
                    
                
    

    def add_note(self, new_note):
        if new_note.date_time[:10] not in note: 
            note[new_note.date_time[:10]] = [new_note]  
        else:
            arr = note[new_note.date_time[:10]]  
            arr.append(new_note)  
            note[new_note.date_time[:10]] = arr

    def delete_note_by_date_time(self, date_time):
        if date_time[:10] in note:
            for i in range(len(note[date_time[:10]])):
                print(i + 1, ')', note[date_time[:10]][i]) 
            index = int(input('Выберите индекс заметки для удаления: '))
            if index > 0 and index <= len(note[date_time[:10]]):
                print("Была удалена заметка:")
                print(note[date_time[:10]].pop(index - 1))
            else:
                print('Неверный индекс!')
                return    

    def edit_note_by_date_time(self, date_time):
        if date_time[:10] in note:
            for i in range(len(note[date_time[:10]])):
                print(i + 1, ')', note[date_time[:10]][i]) 
            index = int(input('Выберите индекс заметки для редактирования: '))
            if index > 0 and index <= len(note[date_time[:10]]):
                a = int(input("Что редактируем:\n1) Заголовок\n2) Текст\n"))
                print(a)
                if a == 1:
                    note1=note[date_time[:10]].pop(index-1)
                    note1.heading = input("Введите новый заголовок: ").replace("\n", "")
                    note1.date_time=datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S") 
                    note[note1.date_time[:10]]=[note1]
                    print(note1.text)
                elif a == 2:
                    note1=note[date_time[:10]].pop(index-1)
                    note1.text = input("Введите новый текст: ").replace("\n", "")
                    note1.date_time=datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S") 
                    note[note1.date_time[:10]]=[note1]
                else:
                    print("Введен неверный индекс")
                    return   

    def find_notes_by_date_time(self, date_time):
        if date_time[:10] in note:
            for i in range(len(note[date_time[:10]])):
                print(i + 1, ')', note[date_time[:10]][i])

    def save_note(self, file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            for key, value in note.items():
                for i in value:
                    print(i.ID,i.heading,i.text.replace("\n", ""),i.date_time)
                    writer.writerow([i.ID,i.heading,i.text.replace("\n", ""),i.date_time])


    def full_notes(self):   
        for i,value in note.items():
            if not value==[]:
                for j in value:
                    print(j)        
if __name__ == "__main__":
    note_manager = NoteManager("C:\codes\pyth\GB_Zametki\zametki.csv")

    while True:
        print("\nМеню:")
        print("1. Вывести все заметки")
        print("2. Редактировать заметку по дате ")
        print("3. Удалить заметку по дате ")
        print("4. Найти заметку по дате ")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            note_manager.full_notes()
        elif choice == "2":
            date_time = input("Введите дату  заметки для редактирования (гггг.мм.дд): ")
            note_manager.edit_note_by_date_time(date_time)
        elif choice == "3":
            date_time = input("Введите дату  заметки для удаления (гггг.мм.дд): ")
            note_manager.delete_note_by_date_time(date_time)
        elif choice == "4":
            date_time = input("Введите дату заметки для поиска (гггг.мм.дд): ")
            note_manager.find_notes_by_date_time(date_time)
        elif choice == "5":
            note_manager.save_note("C:\codes\pyth\GB_Zametki\zametki.csv")
            break
        else:
            print("Неверный индекс. Попробуйте снова!")
