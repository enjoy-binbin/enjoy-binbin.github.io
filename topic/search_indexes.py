from haystack import indexes

from .models import Topic


class TopicIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Topic
        fields = ['title', 'markdown_content']
