from django.contrib import admin
# import models from models in this app
from .models import Cat, Feeding, Toy

# Register the models here.

# register the Cat model
admin.site.register(Cat)
# register the Feeding model
admin.site.register(Feeding)
# register the Toy model
admin.site.register(Toy)