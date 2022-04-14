from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    child = models.ForeignKey('self', related_name='children',
                              on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        if self.child:
            return f'{self.name} --> {self.child}'
        return self.name
