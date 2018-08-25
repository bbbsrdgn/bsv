from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
	tag = models.CharField(max_length=50, unique=True, verbose_name="Etiketler")
	created = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.tag

class User(models.Model):
	username = models.CharField(max_length = 50, verbose_name="Kullanıcı Adı")
	email = models.EmailField()
	password = models.CharField(max_length = 20, verbose_name="Şifre")

	def __str__(self):
		return self.username

class Post(models.Model):
	title = models.CharField(max_length=100, verbose_name="Başlık")
	post = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Gönderen")
	tags = models.ManyToManyField(Tag, blank=True, verbose_name="Etiketler")
	pub_date = models.DateTimeField(default=timezone.now, verbose_name="Yayınlanma Tarihi")

	def __str__(self):
		return self.title

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)	


class Comment(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, verbose_name="Gönderen")
    text = models.TextField(verbose_name="Yorum")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

