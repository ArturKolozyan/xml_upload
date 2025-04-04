# XML Upload Application

## Описание

Этот проект представляет собой простое веб-приложение на Django, которое позволяет загружать XML-файлы через
веб-интерфейс. Приложение проверяет загруженные объявления на дубликаты по ссылке и сохраняет уникальные объявления в
базе данных.

## Установка

### Шаги установки

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/xml-upload.git
   cd xml-upload


2. Создайте виртуальное окружение и активируйте его:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции базы данных:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```


