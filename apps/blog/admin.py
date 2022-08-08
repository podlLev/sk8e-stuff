from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'article_list_link']
    list_display_links = ['id', 'name']

    def article_list_link(self, obj):
        count = Article.objects.filter(tags__in=[obj.id]).count()
        url = (
            reverse('admin:blog_article_changelist')
            + '?'
            + urlencode({'tags__id': obj.id, 'tags__id__exact': obj.id})
        )
        return format_html(f"<a href='{url}'>Статьи(ей): {count}</a>")

    article_list_link.short_description = 'Статьи'


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_list_link']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']

    def article_list_link(self, obj):
        count = Article.objects.filter(category=obj).count()
        url = (
            reverse('admin:blog_article_changelist')
            + '?'
            + urlencode({'category__id': obj.id, 'category__id__exact': obj.id})
        )
        return format_html(f"<a href='{url}'>Статьи(ей): {count}</a>")

    article_list_link.short_description = 'Статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag_thumbnail', 'user_link', 'category_link', 'tag_links', 'created_at']
    list_display_links = ['id', 'title', 'image_tag_thumbnail']
    fields = ['category', 'image_tag', 'image', 'tags', 'user', 'title', 'text_preview', 'text']
    readonly_fields = ['image_tag']
    list_filter = ['category', 'tags']

    def category_link(self, obj):
        if obj.category:
            url = reverse('admin:blog_blogcategory_change', args=[obj.category.id])
            return format_html(f"<a href='{url}'>{obj.category.name}</a>")

    category_link.short_description = 'Категория'

    def user_link(self, obj):
        if obj.user:
            url = reverse('admin:user_user_change', args=[obj.user.id])
            return format_html(f"<a href='{url}'>{obj.user.username}</a>")

    user_link.short_description = 'Автор'

    def tag_links(self, obj):
        format_string = []
        for tag in obj.tags.all():
            url = reverse('admin:blog_tag_change', args=[tag.id])
            format_string.append(f"<a href='{url}'>#{tag.name}</a>")
        return format_html(', '.join(format_string))

    tag_links.short_description = 'Теги'
