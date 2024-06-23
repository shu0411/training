from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField('タイトル', max_length=50)
    content = models.TextField('本文')
    photo1 = models.ImageField('写真1', blank=True, null=True)
    photo2 = models.ImageField('写真2', blank=True, null=True)
    photo3 = models.ImageField('写真3', blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'diary'

    def __str__(self):
        return self.title