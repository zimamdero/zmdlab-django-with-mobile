from rest_framework import serializers
from card_v1.models import *
from django.contrib.auth.models import User


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CardV1Serializer(serializers.ModelSerializer):
    imgs = serializers.SerializerMethodField()
    writer_info = serializers.SerializerMethodField()

    def get_imgs(self, obj):
        try:
            imgInfos = ImgInfo.objects.filter(parent_type='card_v1').filter(parent_id=obj.id)
            result = [ImgInfoSerializer(info).data for info in imgInfos]
            return result
        except Exception as e:
            return {
                "exception": e.args
            }

    def get_writer_info(self, obj):
        try:
            print(obj)
            user = User.objects.get(pk=obj.writer)
            return WriterSerializer(user).data
        except Exception as e:
            return {
                "exception": e.args
            }

    class Meta:
        model = CardV1
        fields = ['id', 'parent_id', 'parent_type', 'level', 'm_level',
                  'writer', 'title', 'contents', 'like_up', 'like_down',
                  'report_count', 'created_at', 'updated_at', 'writer_info', 'imgs']
        extra_kwargs = {
            'writer': {'required': True},
            'title': {'required': True},
            'contents': {'required': True}
        }

    #def update(self, instance, validated_data):
    #    changed = False
    #    if hasattr(validated_data, 'title'):
    #        instance.set_title(validated_data['title'])
    #        changed = True
    #
    #    if hasattr(validated_data, 'contents'):
    #        instance.set_contents(validated_data['contents'])
    #        changed = True
    #
    #    if changed:
    #        instance.save()
    #
    #    return instance


class ImgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgInfo
        fields = ['id', 'parent_id', 'parent_type', 'img', 'img_width', 'img_height',
                  'title', 'contents', 'created_at', 'updated_at', 'm_level',
                  'like_up', 'like_down', 'report_count']
