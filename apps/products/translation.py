from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Images, Comment, Slider


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description', 'title', 'keywords')

@register(Images)
class ImagesTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('name', 'email', 'comment')

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title',)



