from django.db import models


class Genre(models.Model):
    # TAG Choices
    FICTION = 'F'
    GRAPHIC_NOVEL = 'GN'
    # add more tag options if required
    TAGS = (
        (FICTION, 'Fiction'),
        (GRAPHIC_NOVEL, 'Graphic Novel'),
    )
    tag = models.CharField(max_length=1, null=False, choices=TAGS)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.tag


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    author_bio = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.first_name


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    # Book formatOrder choices
    PAPER_BACK = 'P'
    HARD_BOUND = 'H'
    # add more format if required
    FORMAT = (
        (PAPER_BACK, 'Paper Back'),
        (HARD_BOUND, 'Hard Bound'),
    )

    title = models.CharField(max_length=1, null=False, choices=FORMAT)
    author = models.ManyToManyField(Author)
    description = models.CharField(max_length=250)
    book_format = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    edition = models.CharField(max_length=20)
    price = models.FloatField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
