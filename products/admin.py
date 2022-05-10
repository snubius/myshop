from django.contrib import admin
from django.contrib import admin
from .models import Movie, Genre, Actor,Category,MovieShots,Rating,RatingStar,Reviews


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Rating)