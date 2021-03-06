from django.db import models


class Social(models.Model):
    title = models.CharField(verbose_name="Заголовок", blank=True, null=True, max_length=255)
    link = models.CharField(verbose_name="Ссылка на соц.сеть", blank=True, null=True, max_length=255)
    image_icon = models.ImageField(
        verbose_name="Фото иконка соц.сети", 
        upload_to="social/", 
        blank=True, null=True,
        help_text="можно взять из сайта  https://www.flaticon.com/"
    )
    
    def __str__(self):
        return f"{self.title} -- {self.link}"
    
    class Meta:
        verbose_name_plural = "Соц.сети"
    