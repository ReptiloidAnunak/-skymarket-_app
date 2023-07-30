from rest_framework import serializers
from phonenumber_field import serializerfields
from ads.models import Ad, Comment



class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_image = serializers.ImageField(source="author.image", read_only=True)

    # author_image = serializers.ReadOnlyField(source="author.image")

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at", "author_first_name",
                  "author_last_name", "ad_id", "author_image"]
        #


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description",
                  "author_first_name", "author_last_name", "author_id"]

