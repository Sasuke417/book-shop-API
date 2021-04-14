from test_plus.test import TestCase
from the_book_shop_api.inventory.models import Author, Publisher, Book, Genre
from . import factories


class TestModels(TestCase):
    """test to check if all the required fields are declared in each model"""

    def test_create_genre(self):
        genre = Genre.objects.create(tag=Genre.FICTION, description="Test description.")
        self.assertIsNotNone(genre)

    def test_create_publisher(self):
        name = "Acme Co."
        website = "www.acme.com"
        publisher = Publisher.objects.create(name=name, website=website)
        self.assertIsNotNone(publisher)

    def test_create_author(self):
        first_name = 'Fresco'
        last_name = 'Play'
        author_bio = 'Gamified learning platform.'
        genre = factories.GenreFactory()
        author = Author.objects.create(first_name=first_name, last_name=last_name, author_bio=author_bio)
        author.genre.add(genre)
        self.assertIsNotNone(author)

    def test_create_book(self):
        genre = factories.GenreFactory()
        author = factories.AuthorFactory.create(genre=[genre])
        publisher = factories.PublisherFactory()
        title = "Book"
        description = "Some description"
        book_format = Book.HARD_BOUND
        edition = "1st Edition"
        price = "500.0"
        book = Book.objects.create(title=title, description=description, book_format=book_format,
                                   publisher=publisher, edition=edition, price=price)
        book.author.add(author)
        book.genre.add(genre)
        self.assertIsNotNone(book)
        self.assertIn(author, book.author.all())
        self.assertIn(genre, book.genre.all())
