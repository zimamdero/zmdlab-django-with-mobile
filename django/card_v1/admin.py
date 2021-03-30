from django.contrib import admin
from card_v1.models import CardV1, ImgInfo, Comment, ReportInfo, ReadInfo


class CardV1Admin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(CardV1, CardV1Admin)


class ImgInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(ImgInfo, ImgInfoAdmin)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Comment)


class ReportInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(ReportInfo,ReportInfoAdmin)


class ReadInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(ReadInfo, ReadInfoAdmin)
