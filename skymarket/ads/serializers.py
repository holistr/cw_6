from rest_framework import serializers


from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__ad__"


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name")

    # def get_author_first_name(self, obj):
    #     return obj.author.first_name

    class Meta:
        model = Ad
        fields = "__all__"
