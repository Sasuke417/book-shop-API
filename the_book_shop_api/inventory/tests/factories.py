import factory
from factory import fuzzy
from the_book_shop_api.inventory.models import Genre, Publisher, Author, Book


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    tag = fuzzy.FuzzyChoice([
        Genre.GRAPHIC_NOVEL,
        Genre.FICTION,
    ])
    description = fuzzy.FuzzyText(length=30)


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher
    name = factory.Sequence(lambda n: 'Publisher {}'.format(n))
    website = factory.Sequence(lambda n: 'https://www.publisher{}-site.com/'.format(n))


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    @factory.post_generation
    def genre(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genre.add(genre)


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    book_format = fuzzy.FuzzyChoice([
        Book.HARD_BOUND,
        Book.PAPER_BACK,
    ])
    edition = factory.Sequence(lambda n: "{} Edition".format(n))
    publisher = factory.SubFactory(PublisherFactory)
    price = fuzzy.FuzzyFloat(low=5.0)

    @factory.post_generation
    def genre(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genre.add(genre)

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.autho.add(author)
