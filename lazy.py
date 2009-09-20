
from comcenter.product.models import Product
from glob import glob

files = []

misses = 0
for p in Product.objects.all():
    if p


text = 'An easy-to-read translation especially for students! The Good News Translation used to be called Today\'s English Version. Its reading level is about 7th grade. Clear medium-size type in two-column format with large headings on quality off-white newsprint paper. Includes book introductions and outlines, six-page Extreme Faith youth introduction, Bible chart, Bible helps, famous passages list,  reading checklist, glossary, chronology, 14 maps, The Deuterocanon/Apocrypha is placed between the Old and New Testaments. <i>Imprimatur. </i>Four-color paper cover, 5.25 x 8.25 x 1.5.<br><br>Order one or many (24 fit in a box).<br><br><a href="index.cfm?fuseaction=customer.category&amp;category_code=L000074">For a complete list of Good News Translations available, click here.<br><br><a href="http:'


class Lazy(object):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self._cache = None
    def __get__(self, instance, owner):
        if not self._cache:
            self._cache = self.func(*self.args, **self.kwargs)
        return self._cache
    def __set__(self, instance, value):
        raise AttributeError

class Test(object):
    def sum(self, n):
        result = 0
        for i in range(n * 100000):
            result += i
        return result
    sum5 = Lazy(Test.sum, 5)


short_text = 
words = text.split(' ')
