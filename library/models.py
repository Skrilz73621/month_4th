from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Horror', 'Ужасы'),
        ('Comedy', 'Комедия'),
        ('Fantasy', 'Фэнтези')
    )
    image = models.ImageField(verbose_name='Загрузите изображение', upload_to='books/')
    title = models.CharField(max_length=100, verbose_name='Введите название книги')
    description = models.TextField(verbose_name='Введите описание книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='Введите цену', default=120)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name='Выберите жанр')
    email = models.CharField(max_length=120, verbose_name='Введите адрес электронной почты')
    director = models.CharField(max_length=100, verbose_name='Введите имя режиссера', default='Исманкулов Нурсултан')
    trailer = models.URLField(verbose_name='Вставьте ссылку на трейлер')


class Meta:
    verbose_name = 'книга'
    verbose_name_plural = 'книги'
    
    def __str__(self):
        return f'{self.title}:{self.price}'