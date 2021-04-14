from django.urls import reverse, resolve

from test_plus.test import TestCase


class TestGenreURLs(TestCase):
    """Test URL patterns for inventory app."""

    def test_genre_list_reverse(self):
        """genre-list should reverse to /api/inventory/genre/."""
        self.assertEqual(reverse('genre-list'), '/api/inventory/genre/')

    def test_genre_list_resolve(self):
        """/api/inventory/genre/ should resolve to genre-list."""
        self.assertEqual(resolve('/api/inventory/genre/').view_name, 'genre-list')

    def test_genre_detail_reverse(self):
        """genre-detail should reverse to /api/inventory/genre/2/."""
        self.assertEqual(reverse('genre-detail', args={2}), '/api/inventory/genre/2/')

    def test_genre_detail_resolve(self):
        """/api/inventory/genre/2/ should resolve to genre-detail."""
        self.assertEqual(resolve('/api/inventory/genre/2/').view_name, 'genre-detail')


class TestBookURLs(TestCase):
    """Test URL patterns for inventory app."""

    def test_book_list_reverse(self):
        """book-list should reverse to /api/inventory/books/."""
        self.assertEqual(reverse('book-list'), '/api/inventory/books/')

    def test_book_list_resolve(self):
        """/api/inventory/books/ should resolve to book-list."""
        self.assertEqual(resolve('/api/inventory/books/').view_name, 'book-list')

    def test_book_detail_reverse(self):
        """book-detail should reverse to /api/inventory/books/2/."""
        self.assertEqual(reverse('book-detail', args={2}), '/api/inventory/books/2/')

    def test_book_detail_resolve(self):
        """/api/inventory/books/2/ should resolve to book-detail."""
        self.assertEqual(resolve('/api/inventory/books/2/').view_name, 'book-detail')


class TestAuthorURLs(TestCase):
    """Test URL patterns for inventory app."""

    def test_author_list_reverse(self):
        """author-list should reverse to /api/inventory/authors/."""
        self.assertEqual(reverse('author-list'), '/api/inventory/authors/')

    def test_author_list_resolve(self):
        """/api/inventory/authors/ should resolve to author-list."""
        self.assertEqual(resolve('/api/inventory/authors/').view_name, 'author-list')

    def test_author_detail_reverse(self):
        """author-detail should reverse to /api/inventory/authors/2/."""
        self.assertEqual(reverse('author-detail', args={2}), '/api/inventory/authors/2/')

    def test_author_detail_resolve(self):
        """/api/inventory/authors/2/ should resolve to author-detail."""
        self.assertEqual(resolve('/api/inventory/authors/2/').view_name, 'author-detail')


class TestPublisherURLs(TestCase):
    """Test URL patterns for inventory app."""

    def test_publisher_list_reverse(self):
        """publisher-list should reverse to /api/inventory/publishers/."""
        self.assertEqual(reverse('publisher-list'), '/api/inventory/publishers/')

    def test_publisher_list_resolve(self):
        """/api/inventory/publishers/ should resolve to publisher-list."""
        self.assertEqual(resolve('/api/inventory/publishers/').view_name, 'publisher-list')

    def test_publisher_detail_reverse(self):
        """publisher-detail should reverse to /api/inventory/publishers/2/."""
        self.assertEqual(reverse('publisher-detail', args={2}), '/api/inventory/publishers/2/')

    def test_publisher_detail_resolve(self):
        """/api/inventory/publishers/2/ should resolve to publisher-detail."""
        self.assertEqual(resolve('/api/inventory/publishers/2/').view_name, 'publisher-detail')
