from django.db import models
from ckeditor.fields import RichTextField


class New(models.Model):
    name = models.CharField(max_length=250)
    text = RichTextField()
    principal_image = models.ImageField(upload_to='images')
    author = models.ForeignKey('volunteers.Volunteer')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

    @property
    def rating(self):
        rate = 0
        try:
            votes = Vote.objects.filter(new=self)
            for vote in votes:
                rate += vote.vote
            rate /= len(votes)
            return rate
        except:
            return rate

    def __str__(self):
        return self.name


class Vote(models.Model):

    VOTES_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    vote = models.IntegerField(choices=VOTES_CHOICES)
    new = models.ForeignKey('neewsfeed.New')
    volunteer = models.OneToOneField('volunteers.Volunteer')

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"


class Comment(models.Model):

    volunteer = models.OneToOneField('volunteers.Volunteer')
    new = models.OneToOneField('neewsfeed.New')
    text = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        pass 


class NewPhoto(models.Model):

    image = models.ImageField(upload_to='images')
    new = models.ForeignKey('neewsfeed.New')

    class Meta:
        verbose_name = "NewPhoto"
        verbose_name_plural = "NewPhotos"
