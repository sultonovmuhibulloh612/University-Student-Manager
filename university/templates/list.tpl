{% if m %}
    <div id="message-box" class="message">
        {{ m }}
    </div>
{% endif %}

{% extends "base.tpl" %}

{% block content %}
    {% for it in items %}
        {% include "item.tpl" ignore missing %}
    {% else %}
        <div class="no-data">No data</div>
    {% endfor %}

    <div class="button-container">
        <form action="{{ url_for('university.show_form', id=0) }}" method="get" style="display: inline;">
            <input type="hidden" name="role" value="Студент">
            <button type="submit" class="action-button">Add Student</button>
        </form>
        
        <form action="{{ url_for('university.show_form', id=0) }}" method="get" style="display: inline;">
            <input type="hidden" name="role" value="Профорг">
            <button type="submit" class="action-button">Add Proforg</button>
        </form>
        
        <form action="{{ url_for('university.show_form', id=0) }}" method="get" style="display: inline;">
            <input type="hidden" name="role" value="Староста">
            <button type="submit" class="action-button">Add Starosta</button>
        </form>
    </div>
{% endblock %}