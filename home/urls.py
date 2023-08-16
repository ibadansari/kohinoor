from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Kohinoor Catters"
admin.site.site_title = "Kohinoor Catters Admin Portal"
admin.site.index_title = "Welcome to Kohinoor Catters"


urlpatterns = [
    path("", views.index, name='About'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
path("nonveg", views.nonveg, name='nonveg'),
path("veg", views.veg, name='veg'),
path("starters", views.starters, name='starters'),
path("desserts", views.desserts, name='desserts'),
path("bevrages", views.bevrages, name='bevrages'),
path("chinese", views.chinese, name='chinese'),
path("chicken", views.chicken, name='chicken'),
path("beaf", views.beaf, name='beaf'),
path("mutton", views.mutton, name='mutton'),
path("paneer", views.paneer, name='paneer'),
path("veggies", views.veggies, name='veggies'),
path("others", views.others, name='others'),
path("icecream", views.icecream, name='icecream'),
path("halwa", views.halwa, name='halwa'),
path("special", views.special, name='special'),
]