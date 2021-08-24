from django.db.models import QuerySet
from random import randint

class CustomQuerySet(QuerySet):

    #Funciones para filtrar los productos dentro del template.
    def on_slider(self):
        return self.filter(preview='slider')

    def on_preorder(self):
        return self.filter(preview='preorder')

    def get_accesories(self):
        return self.filter(category='accesory')

    def get_hoodies(self):
        return self.filter(category='hoodie')

    def get_bottoms(self):
        return self.filter(category='bottom')

    def get_sneakers(self):
        return self.filter(category='sneaker')

    def get_outerwears(self):
        return self.filter(category='outerwear')

    def get_tshirts(self):
        return self.filter(category='t-shirt')


    #Esta funcion devuelve un producto aleatorio de la lista de productos del queryset
    def random(self):
        random = self
        if len(random) > 0:
            return random[randint(0, len(random) - 1)]

        #Hacer esto me tomo una noche entera y una lata de speed
