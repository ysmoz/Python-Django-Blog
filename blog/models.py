from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS=(
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    title=models.CharField(max_length=100)
    keyword=models.CharField(blank=True,max_length=255)
    description=models.CharField(blank=True,max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    parent=TreeForeignKey('self',blank=True,null=True,related_name='chidren',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append( k.title )
            k= k.parent
        return  '->'.join (full_path[::-1])

    def image_tag(self):
      return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Blog(models.Model):
    STATUS=(
        ('True','Evet'),
        ('False','Hayır'),
    )

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    keyword=models.CharField(blank=True,max_length=255)
    description=models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    detail=RichTextUploadingField()
    file=models.FileField(null=True,blank=True)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    slug = models.SlugField(blank=True,max_length=150)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
      return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def catimg_tag(self):
        return mark_safe((Category.status))

class Images (models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    title=models.CharField(max_length=150,blank=True)
    image=models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'














