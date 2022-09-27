from rest_framework import generics, permissions, viewsets
from apps.blog.models import Article
from apps.api.blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()

        if self.request.query_params.get('user'):
            queryset = queryset.filter(user=self.request.query_params['user'])

        if self.request.query_params.get('category'):
            queryset = queryset.filter(category=self.request.query_params['category'])

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
