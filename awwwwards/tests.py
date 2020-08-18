from django.test import TestCase
from .models import Profile,Countries,Post,Technologies,Rating
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.username = User(id=1, username='cindy', password='hyte4vvd4')
        self.username.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.username, User))

    def test_save_user(self):
        self.username.save()

    def test_delete_user(self):
        self.username.delete()


class TestPost(TestCase):
    def setUp(self):
        self.username = User.objects.create(id=1, username='cindy')
        self.post = Post.objects.create(id=1, title='test post', photo='great.jpeg', description='desc',username=self.username, link='http://url.com')
                                        

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_post('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_post('test')
        self.assertTrue(len(post) < 1)


class TestCountry(TestCase):
    def setUp(self):
        self.countries = Countries(countries = 'kenya')
        self.countries.save

    def test_save_country(self):
        self.countries.save()

    def test_delete_country(self):
        self.countries.delete()


    
