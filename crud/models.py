from django.db import models


class Todo(models.Model):
    content = models.TextField(verbose_name="İçerik", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False, verbose_name=("Tamamlama"))

    class Meta:

        verbose_name = "TodoList"
        verbose_name_plural = "TodoList"
        default_permissions = ()
        permissions = (
            (("liste"), ("Listeleme Yetkisi")),
            (("sil"), ("Silme Yetkisi")),
            (("ekle"), ("Ekleme Yetkisi")),
            (("guncelle"), ("Güncelleme Yetkisi")),
        )
