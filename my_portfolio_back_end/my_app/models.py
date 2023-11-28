from django.db import models


class Project(models.Model):
    CHOICES_LANGUAGE = (
        ("py", "Python"),
        ("ru", "Rust"),
    )

    name = models.CharField(max_length=30, unique=True)
    language = models.CharField(choices=CHOICES_LANGUAGE)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
