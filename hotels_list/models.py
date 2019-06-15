from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Hotel(models.Model):
    """Класс отелей
    """
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    hotel = models.TextField("Название отеля")
    address = models.TextField("Адрес")
    description = models.TextField("Описание")
    capacity = models.TextField("Вместимость")
    type = models.TextField("Тип номера")
    facilities = models.TextField("Удобства")
    owner = models.TextField("Владелец отеля")

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"

    def __str__(self):
        return self.hotel


class Comments(models.Model):
    """Класс комментариев к отелям
    """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    hotel = models.ForeignKey(
        Hotel,
        verbose_name="Отель",
        on_delete=models.CASCADE)
    # hotel = models.CharField("Название отеля", max_length=15)
    typ_comment = models.CharField("Тема комментария", max_length=50, default="")
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)
