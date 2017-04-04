"""Managers for models."""

# from models import NewsPost
import django.db.models as models


class MainManager(models.Manager):

    def get_news_by_slug(self, slug):
        result = super(MainManager, self).get_queryset()\
            .filter(slug=slug) \
            .first()
            # .select_related('picturefornews') \

        return result


class CommentManager(models.Manager):

    def get_comments_for_news(self, news):
        result = super(CommentManager, self).get_queryset()\
            .filter(news=news)\
            .select_related('user_nickname')\
            .all()

        return result
