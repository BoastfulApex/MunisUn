from django.db import models


class Scroll(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(null=True)
    cost = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=500, null=True, blank=True)
    info = models.TextField(max_length=1000, null=True, blank=True)
    xit = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Hamkorlar(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class FAQ(models.Model):
    question = models.CharField(max_length=500, null=True, blank=True)
    answer = models.CharField(max_length=500, null=True, blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)


class About(models.Model):
    link = models.CharField(max_length=500, null=True, blank=True)


class Blog(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogPicture(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.blog.name
