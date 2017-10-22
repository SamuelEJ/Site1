from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Tags(models.Model):
    Tag_text = models.CharField(max_length=200)

    def __str__(self):
        return self.Tag_text
      #  return u'%s %s' % (self.Tag_text)


class Author1(models.Model):
    Author1_name = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Author1_name

class Author2(models.Model):
    Author2_name = models.CharField(max_length=200)

    def __str__(self):
      """
      String for representing the Model object.
      """
      return self.Author2_name

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=450)
    Opening_Para = models.CharField(max_length=4000)
    Post_text = RichTextUploadingField(null=True, blank=True)
    Tags = models.ManyToManyField(Tags)
    Author1 = models.ForeignKey(Author1, on_delete=models.CASCADE)
    Author2 = models.ForeignKey(Author2, on_delete=models.CASCADE)
    Image = models.ImageField(max_length=255, null=True, upload_to="")

    createdDate = models.DateTimeField(default=timezone.now)

    year = models.IntegerField(blank=True,null=True)
    month = models.CharField(max_length=25,null=True)
    monthNumber = models.IntegerField(blank=True,null=True)
    dayNumber = models.IntegerField(blank=True,null=True)



    class Meta:
       ordering = ['-createdDate']

    def image_tag(self):
        return ('<img src="%s" width="150" height="150" />' % (self.Image))


        #def image_tag(self):
     #   return u'<img src="%s" />' % self.Image.url

    def get_tags(self):
        return ",".join([str(p) for p in self.Tags.all()])




# Create your models here.
class PostView(models.Model):
    id = models.BigIntegerField(primary_key=True)
    Title = models.CharField(max_length=450)
    Opening_Para = models.CharField(max_length=4000)
    Post_text = models.TextField()
    Tags = models.ManyToManyField(Tags)
    Author1 = models.ForeignKey(Author1, on_delete=models.DO_NOTHING)
    Author2 = models.ForeignKey(Author2, on_delete=models.DO_NOTHING)
    Image = models.ImageField(max_length=255, null=True, upload_to="")
    createdDate = models.DateTimeField()

    Title_Opening_Combined = models.TextField()
    year = models.IntegerField()
    month = models.IntegerField(2)


    class Meta:
        managed = False
        db_table = 'post_view'
        ordering = ['-createdDate']

    def image_tag(self):
        return ('<img src="%s" width="150" height="150" />' % (self.Image))


        #def image_tag(self):
     #   return u'<img src="%s" />' % self.Image.url

    def get_tags(self):
        return ",".join([str(p) for p in self.Tags.all()])





