from django.test import TestCase
from .models import Article
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your tests here.

User = get_user_model()

class TestArticle(TestCase):
    article_title = 'a title '
    article_body = 'a body'
    user_username='username'
    user_email='use@email.com'
    user_password='pass'
    @classmethod 
    def setUpTestData(cls):
        user = User(email=cls.user_email,username=cls.user_username)
        user.set_password(cls.user_password)
        user.save()
        #creating the article
        article = Article(body=cls.article_body,title=cls.article_title,author=user)
        article.save()
    #start testing 
    def testUserCount(self):
        self.assertTrue(User.objects.count()==1)
    def testArticleCount(self):
        self.assertTrue(Article.objects.count()==1)
    def testUser(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username,self.user_username)
        self.assertEqual(user.email,self.user_email)
    def testArticleTitle(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.title,self.article_title)
    def testArticleBody(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.body,self.article_body)
    def testArticleAuthor(self):
        article = Article.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(article.author,user)
    def testArticleSlug(self):
        sluggedTitle = slugify(self.article_title)
        article  = Article.objects.get(id=1)
        self.assertEqual(article.slug,sluggedTitle)
    def testArticlePublish(self):
        article  = Article.objects.get(id=1)
        self.assertTrue(article.publish)
