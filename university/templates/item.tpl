<h2>Student Information</h2>
<div class="info">
    <p>PASSPORT NUMBER: <strong>{{ it.passport_number }}</strong></p>
    <p>NAME: <strong>{{ it.name }}</strong></p>
    <p>SURNAME: <strong>{{ it.surname }}</strong></p>
    <p>GROUP: <strong>{{ it.group_name }}</strong></p>
    <p>AGE: <strong>{{ it.age }}</strong></p>
    <p>Time: <strong>{{ it.time }}</strong></p>
    <p>Status: <strong>{{ it.status_in_group }}</strong></p>

    {% if it.start_date %}
    <p>Date of appointment: <strong>{{ it.start_date }}</strong></p>
    <p>Contact Number: <strong>{{ it.contact_number }}</strong></p>
    {% endif %}

    {% if it.the_number_of_organized_collected %}
    <p>Number of Organized Collected: <strong>{{ it.the_number_of_organized_collected }}</strong></p>
    <p>Performance Assessment: <strong>{{ it.performance_assessment }}</strong></p>
    {% endif %}

    <div class="button-container">
        <!-- Форма для редактирования (GET запрос) -->
        <form class="edit-form" action="{{ url_for('university.show_form', id=it.id) }}" method="get">
            <input type="hidden" name="role" value="{{ it.status_in_group }}">
            <button type="submit" class="action-button">Edit</button>
        </form>

        <!-- Форма для удаления (POST запрос с CSRF) -->
        <form class="delete-form" action="{{ url_for('university.delete', id=it.id) }}" method="post">
            <!-- CSRF токен для защиты -->
            <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
            <button type="submit" class="action-button" 
                    onclick="return confirm('Are you sure you want to delete this student?')">Delete</button>
        </form>
    </div>
</div>