from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post
# from .urls import urlpatterns
# Create your tests here.

class testPost(TestCase):

    # prepare our data..
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='swedani',
            email='swedani@gmail.com',
            password='swedani'
        )
        self.post = Post.objects.create(
            title='new test post',
            author=self.user,
            body='this is test for posting..'
        )




    # test all posts page..
    def test_posts_status(self):
        urls = reverse('posts')
        response = self.client.get(urls)
        self.assertEquals(response.status_code, 200)

    def test_posts_contain(self):
        urls = reverse('posts')
        response = self.client.get(urls)
        self.assertContains(response, 'new test post')

    
    # test post details..
    def test_details_post_status(self):
        urls = reverse('details_post',args='1')
        response = self.client.get(urls)
        self.assertEquals(response.status_code, 200)

    def test_details_post_contain(self):
        urls = reverse('details_post',args='1')
        response = self.client.get(urls)
        self.assertContains(response, 'new test post')
        self.assertContains(response, 'swedani')
        self.assertContains(response, 'this is test for posting..')


    # test create post..
    def test_create_post_status(self):
        urls = reverse('create_post')
        response = self.client.get(urls)
        self.assertEquals(response.status_code, 200)

    # test post update..
    def test_update_post_status(self):
        urls = reverse('update_post',args='1')
        response = self.client.get(urls)
        self.assertEquals(response.status_code, 200)
    
    def test_update_post_contain(self):
        urls = reverse('update_post',args='1')
        response = self.client.post(urls, {
            'title': 'edit test'
        })
        self.assertContains(response, 'edit test')


    # test delete post..    
    def test_delete_post_status(self):
        post_response = self.client.post(reverse('delete_post', args='1'), follow=True)
        self.assertRedirects(post_response, reverse('posts'), status_code=302)

    def test_post_after_delete_status(self):
        self.client.post(reverse('delete_post', args='1'), follow=True)
        urls = reverse('delete_post',args='1')
        response = self.client.get(urls)
        self.assertEquals(response.status_code, 404)

