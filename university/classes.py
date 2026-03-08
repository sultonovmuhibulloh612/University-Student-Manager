
import datetime, pickle
from dataclasses import dataclass



form_path = 'form.tpl'


@dataclass
class Student:
    id: int = 0
    passport_number: str = ""
    name: str = ""
    surname: str = ""
    age: int = 21
    group_name: str = ""
    time: str = ""
    status_in_group: str = "Студент"

    def __post_init__(self):
        self.time = str(datetime.datetime.now())
     


    def Show(self):
        return "complete the form"

    def EditFormData(self, io):
        self.id = int(io.Input('id'))
        self.passport_number = io.Input('passport_number')
        self.name = io.Input('name')
        self.surname = io.Input('surname')
        self.age = int(io.Input('age'))
        self.group_name = io.Input('group_name')


    def ShowForm(self, io):
        return io.Output(form_path, self)

    def DBLoad(self, r):
        self.id = r['id']
        self.passport_number = r['passport_number']
        self.name = r['name']
        self.surname = r['surname']
        self.age = r['age']
        self.group_name = r['group_name']
        self.time = r['time']
        self.status_in_group = r['status_in_group']

    def DBStore(self, db):
        print(f"DBStore вызван для {self.__class__.__name__} с id={self.id}")
        
        if not self.id or int(self.id) == 0:
            print("Выполняется INSERT операция")
            db.execute("""
                INSERT INTO book (
                    passport_number, name, surname, age, group_name, time, status_in_group, additional_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (self.passport_number, self.name, self.surname, self.age, self.group_name, self.time,
                        self.status_in_group, None))
            print("INSERT выполнен успешно")
        else:
            print("Выполняется UPDATE операция")
            db.execute("""
                UPDATE book
                SET passport_number=?, name=?, surname=?, age=?, group_name=?, time=?, status_in_group=?
                WHERE id=?""",
                    (self.passport_number, self.name, self.surname, self.age, self.group_name, self.time,
                        self.status_in_group, self.id))
            print("UPDATE выполнен успешно")
        
        return True  # Можно вернуть что-то для проверки

    
@dataclass
class Starosta(Student):
    start_date: str = ""
    contact_number: int = 0
    status_in_group: str = "Староста"

    def __post_init__(self):
        super().__post_init__()  # Вызов базового метода
        self.time = str(datetime.datetime.now())




    def EditFormData(self, io):
        super().EditFormData(io)
        self.start_date = io.Input('start_date')
        self.contact_number = io.Input('contact_number')

    def ShowForm(self, io):
        return io.Output(form_path, self)

    def DBLoad(self, r):
        super().DBLoad(r)
        additional_data = pickle.loads(r['additional_data']) if r['additional_data'] else {}
        self.start_date = additional_data.get('start_date', "")
        self.contact_number = additional_data.get('contact_number', 0)

    def DBStore(self, db):
        additional_data = pickle.dumps({
            "start_date": self.start_date,
            "contact_number": self.contact_number,
        })
        if not self.id or int(self.id) == 0:
            db.execute("""
                INSERT INTO book (
                    passport_number, name, surname, age, group_name, time, status_in_group, additional_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                       (self.passport_number, self.name, self.surname, self.age, self.group_name, self.time,
                        self.status_in_group, additional_data))
        else:
            db.execute("""
                UPDATE book
                SET passport_number=?, name=?, surname=?, age=?, group_name=?, time=?, status_in_group=?, additional_data=?
                WHERE id=?""",
                       (self.passport_number, self.name, self.surname, self.age, self.group_name, self.time,
                        self.status_in_group, additional_data, self.id))


@dataclass
class Proforg(Student):
    the_number_of_organized_collected: int = 0
    performance_assessment: int = 0
    status_in_group: str = "Профорг"

    def __post_init__(self):
        super().__post_init__()  # Вызов базового метода
        self.time = str(datetime.datetime.now())
        

    def EditFormData(self, io):
        super().EditFormData(io)
        self.the_number_of_organized_collected = io.Input('the_number_of_organized_collected')
        self.performance_assessment = io.Input('performance_assessment')

    def ShowForm(self, io):
        return io.Output(form_path, self)

    def DBLoad(self, r):
        super().DBLoad(r)
        additional_data = pickle.loads(r['additional_data']) if r['additional_data'] else {}
        self.the_number_of_organized_collected = additional_data.get('the_number_of_organized_collected', 0)
        self.performance_assessment = additional_data.get('performance_assessment', 0)

    def DBStore(self, db):
        additional_data = pickle.dumps({
            "the_number_of_organized_collected": self.the_number_of_organized_collected,
            "performance_assessment": self.performance_assessment,
        })
        if not self.id or int(self.id) == 0:
            db.execute("""
                INSERT INTO book (
                    passport_number, name, surname, age, group_name, time, status_in_group, additional_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                       (self.passport_number, self.name, self.surname, self.age, self.group_name, self.time,
                        self.status_in_group, additional_data))
        else:
            db.execute("""
                UPDATE book
                SET passport_number=?, name=?, surname=?, age=?, group_name=?, time=?, status_in_group=?, additional_data=?
                WHERE id=?""",
                       (self.passport_number, self.name, self.surname, self.age, self.group_name, self.time,
                        self.status_in_group, additional_data, self.id))
