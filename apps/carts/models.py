from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Название категории')
    keywords = models.CharField(max_length=255, verbose_name='Ключевые слова')
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS, default=True)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'
    
class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    keywords = models.CharField(max_length=255, verbose_name='Ключевые слова')
    image = models.ImageField(blank=False, upload_to='images/')
    descriptions = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.ImageField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'продукт'