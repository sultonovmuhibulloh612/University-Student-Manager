from flask import render_template
from flask import request


class FlaskInputOutput:
    def __init__(self, request):
        self.request = request

    def Input(self, field, default=None):
        """Получить значение из формы."""
        return self.request.form.get(field, default)  # Для работы с данными формы



    def Output(self, formpath, item):
        """Рендеринг шаблона с передачей данных."""
        try:
            return render_template(formpath, it=item)
        except Exception as e:
            raise RuntimeError(f"Ошибка при рендеринге шаблона '{formpath}': {e}")

