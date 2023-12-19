from django.contrib import admin

from .models import User, Book, Author


@admin.register(User)
class BookAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_release', 'genre', 'category', 'publisher',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'date_birth',)
