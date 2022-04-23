from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.Title.name, filename)


class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)


class Chapters(models.Model):
    name = models.CharField(max_length=120,)
    images = models.ForeignKey(Images, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=120,)
    descriptions = models.TextField()
    poster = models.ImageField(upload_to="{{Titles.name}}/arts/")
    genre = models.CharField(max_length=120,)
    author = models.CharField(max_length=120,)
    publisher = models.CharField(max_length=120,)
    translator = models.CharField(max_length=120,)
    slug = models.SlugField(max_length=120, unique=True, )

    def __str__(self):
        return self.name

