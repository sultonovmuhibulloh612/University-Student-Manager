{% extends "base.tpl" %}

{% block content %}
<div class="form-container"> <!-- Добавьте этот div -->
    <h2>{{ it.Show() }}</h2>

    <form action="{{ url_for('university.add') }}" method="POST">
        <!-- CSRF ЗАЩИТА -->
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
        
        <!-- СКРЫТОЕ ПОЛЕ С РОЛЬЮ (в теле формы) -->
        <input type="hidden" name="role" value="{{ it.status_in_group }}">
        
        <input type="hidden" name="id" value="{{ it.id }}">

        <label>PASSPORT NUMBER:</label>
        <input type="text" name="passport_number" value="{{ it.passport_number }}"
               pattern="^\d{5}$" title="Введите 5-значное число" required maxlength="5">

        <label>NAME:</label>
        <input type="text" name="name" value="{{ it.name }}"
               pattern="^[A-Za-zА-Яа-яЁё]+$" title="Имя должно состоять только из букв" required>

        <label>SURNAME:</label>
        <input type="text" name="surname" value="{{ it.surname }}"
               pattern="^[A-Za-zА-Яа-яЁё]+$" title="Фамилия должна состоять только из букв" required>

        <label>GROUP:</label>
        <input type="text" name="group_name" value="{{ it.group_name }}">

        <label>AGE:</label>
        <input type="number" name="age" value="{{ it.age }}" min="15" max="36" required
               oninvalid="this.setCustomValidity('Возраст должен быть от 15 до 36')"
               oninput="this.setCustomValidity('')">

        {% if it.status_in_group == 'Староста' %}
        <label>START DATE:</label>
        <input type="text" name="start_date" value="{{ it.start_date }}"
               pattern="^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
               title="Введите дату в формате ДД/ММ/ГГГГ (например, 26/10/2024)" required>

        <label>CONTACT NUMBER:</label>
        <input type="tel" name="contact_number" value="{{ it.contact_number }}"
               pattern="^\+?[0-9]{10,15}$"
               title="Введите номер телефона в формате +1234567890 или 1234567890 (от 10 до 15 цифр)" required>
        {% endif %}

        {% if it.status_in_group == 'Профорг' %}
        <label>PERFORMANCE ASSESSMENT:</label>
        <input type="number" name="performance_assessment" value="{{ it.performance_assessment }}"
               min="1" max="10" required
               oninvalid="this.setCustomValidity('Оценка должна быть от 1 до 10')"
               oninput="this.setCustomValidity('')">

        <label>THE NUMBER OF ORGANIZED COLLECTED:</label>
        <input type="number" name="the_number_of_organized_collected" value="{{ it.the_number_of_organized_collected }}"
               required title="Введите число" step="1">
        {% endif %}

        <input type="submit" value="Ok">
    </form>
</div>
{% endblock %}