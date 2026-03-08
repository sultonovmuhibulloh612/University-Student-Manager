from flask import g, request, Blueprint, redirect, url_for

from .students import Students

bp = Blueprint('university', __name__, url_prefix='')

def get_students_manager():
    if 'students_manager' not in g:
        g.students_manager = Students()
    return g.students_manager

@bp.route("/")
def index():
    return get_students_manager().ShowBook()

@bp.route("/form/<int:id>", methods=['GET'])
def show_form(id):
    role = request.args.get('role', 'student')
    return get_students_manager().ShowForm(id, role)

@bp.route("/delete/<int:id>", methods=['POST'])
def delete(id):
    return get_students_manager().Delete(id) 

@bp.route("/add", methods=['POST'])
def add():
    role = request.form.get('role', 'student')
    return get_students_manager().Add(role)

@bp.teardown_app_request
def close_db(error):
   
  
    manager = g.pop('students_manager', None)
    
    
    if manager is not None:
        try:
            manager.storage.close()
            print(f"Соединение с БД закрыто. Ошибка: {error}")
        except Exception as e:
            print(f"Ошибка при закрытии соединения с БД: {e}")