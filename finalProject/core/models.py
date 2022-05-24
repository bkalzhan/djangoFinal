from django.db import models

from utils.constants import journal_type


# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField("Name", max_length=20)
    price = models.IntegerField("Price")
    description = models.TextField("Description")
    created_at = models.DateField("Created at")

    class Meta:
        abstract = True

    def __str__(self):
        return '%s, %s' % (self.id, self.name)


class Book(BookJournalBase):
    num_pages = models.IntegerField("Num pages")
    genre = models.CharField("genre", max_length=20)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    type = models.CharField("Type", choices=journal_type, max_length=20)
    publisher = models.CharField("Publisher", max_length=20)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'





