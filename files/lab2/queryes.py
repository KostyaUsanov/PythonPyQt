import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    obj = Entry.objects.filter(author__name__contains='author')
    print(obj)

    from django.db.models import Max, Min

    # Вычислить максимальную и минимальную оценку
    calc_rating = Entry.objects.aggregate(
        max_rating=Max('rating'), min_rating=Min('rating')
    )
    print(calc_rating)  # {'max_rating': 5.0, 'min_rating': 0.0}



    # Обычный запрос
    print(Blog.objects.filter(name__startswith='Фитнес'))
    # <QuerySet [<Blog: Фитнес и здоровый образ жизни>]>

    # Запрос раскрывающий значения
    print(Blog.objects.filter(name__startswith='Фитнес').values())
    """
    QuerySet [{'id': 3, 'name': 'Фитнес и здоровый образ жизни', 
    'tagline': 'Позаботьтесь о своем здоровье, достигните физической формы и ощутите преимущества активного образа жизни!'}]>
    """

    # Вывод всех строк с их раскрытием
    print(Blog.objects.values())
    """
    <QuerySet [
    {'id': 1, 'name': 'Путешествия по миру', 'tagline': 'Откройте новые горизонты и погрузитесь в удивительные приключения вместе с нами!'}, 
    {'id': 2, 'name': 'Кулинарные искушения', 'tagline': 'Раскройте вкусовые грани и наслаждайтесь миром кулинарии вместе с нами!'}, 
    {'id': 3, 'name': 'Фитнес и здоровый образ жизни', 'tagline': 'Позаботьтесь о своем здоровье, достигните физической формы и ощутите преимущества активного образа жизни!'}, 
    {'id': 4, 'name': 'ИТ-новости и технологии', 'tagline': 'Будьте в курсе последних новостей, трендов и инноваций в мире информационных технологий!'}, 
    {'id': 5, 'name': 'Мода и стиль', 'tagline': 'Выражайте свою индивидуальность, следите за модными тенденциями и создавайте неповторимые образы вместе с нами!'}
    ]>
    """
    # Вывод всех строк с сохранением в запросе только необходимых столбцов
    print(Blog.objects.values('id', 'name'))  # Обратите внимание, что данные отсортированы по полю name
    """
    <QuerySet [
    {'id': 4, 'name': 'ИТ-новости и технологии'}, 
    {'id': 2, 'name': 'Кулинарные искушения'}, 
    {'id': 5, 'name': 'Мода и стиль'}, 
    {'id': 1, 'name': 'Путешествия по миру'}, 
    {'id': 3, 'name': 'Фитнес и здоровый образ жизни'}]>
    """











