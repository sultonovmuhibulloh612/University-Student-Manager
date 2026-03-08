# Внешние библиотеки
from flask import render_template, request, redirect, url_for

# Локальные модули
from .storage import DBStorage
from .flask_io import FlaskInputOutput

class Students:
    def __init__(self):
        self.io = FlaskInputOutput(request)
        self.storage = DBStorage(self)

    def ShowForm(self, id, role):
        return self.storage.GetItem(id, role).ShowForm(self.io)

    def ShowBook(self, message=None):
        return render_template('list.tpl', items=self.storage.GetItems(), m=message)

    def Add(self, role):
        
        item_id = self.io.Input('id')
        item = self.storage.GetItem(int(item_id), role)
        item.EditFormData(self.io)
        self.storage.Add(item)
        return redirect(url_for('university.index'))
        
        

    def Delete(self, id):
        self.storage.Delete(id)
        return redirect(url_for('university.index'))
   
