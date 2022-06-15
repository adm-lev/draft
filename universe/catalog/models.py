from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """
    Description
    """
    #  Fields

    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Description
    """
    #  Fields

    title = models.CharField(max_length=200, help_text='Enter a book name')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description')
    isbn = models.CharField('ISBN', max_length=13, help_text='13character')
    genre = models.ManyToManyField(Genre, help_text='Select a genre')

    #  Metadata
    # class Meta:
    #     ordering = ['-field_name']

    # Methods

    def get_absolute_url(self):
        """
        Returns url
        """
        return reverse('books-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Description
    """
    #  Fields

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_to_birth = models.DateField(null=True, blank=True)
    date_to_death = models.DateField('Died', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    #  Metadata
    # class Meta:
    #     ordering = ['-field_name']

    # Methods

    def get_absolute_url(self):
        """
        Returns url
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'







