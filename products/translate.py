from modeltranslation.translator import translator, TranslationOptions
from .models import Product,Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title')

translator.register(News, NewsTranslationOptions)