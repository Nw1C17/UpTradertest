from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True,
                               related_name='children',
                               null=True)
    url = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.name


