from django.contrib import admin

from .models import Categories, Comment, Review, Title, User

admin.site.register(User)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Categories)
