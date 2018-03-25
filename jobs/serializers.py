from rest_framework import serializers
from jobs.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from jobs.models import Job
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('bid', 'bcount')