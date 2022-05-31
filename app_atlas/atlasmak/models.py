from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Новости сайта')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateField(auto_now_add=True, verbose_name='Добавить')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновить')
    # delete_at = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Удалить')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
