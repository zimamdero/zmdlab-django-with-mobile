from django.db import models

PARENT_TYPE = (
    ('none', 'none'),
    ('card_v1', 'card_v1'),
    ('img_info', 'img_info'),
    ('comment', 'comment'),
)


class CardV1(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.PositiveIntegerField(default=0)
    parent_type = models.CharField(max_length=50, choices=PARENT_TYPE, default='none')
    level = models.PositiveIntegerField(default=1)
    m_level = models.PositiveIntegerField(default=1)
    writer = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=100, blank=True)
    contents = models.TextField(blank=True)
    like_up = models.PositiveIntegerField(default=0)
    like_down = models.PositiveIntegerField(default=0)
    report_count = models.PositiveIntegerField(default=0)


class ImgInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.PositiveIntegerField(default=0)
    parent_type = models.CharField(max_length=50, choices=PARENT_TYPE, default='none')
    m_level = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=100, blank=True)
    contents = models.TextField(blank=True)
    like_up = models.PositiveIntegerField(default=0)
    like_down = models.PositiveIntegerField(default=0)
    report_count = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='card_v1_imgs', height_field='img_height', width_field='img_width')
    img_height = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.PositiveIntegerField(default=0)
    parent_type = models.CharField(max_length=50, choices=PARENT_TYPE, default='none')
    m_level = models.PositiveIntegerField(default=1)
    like_up = models.PositiveIntegerField(default=0)
    like_down = models.PositiveIntegerField(default=0)
    report_count = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True)


class ReportInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target_id = models.PositiveIntegerField(default=0)
    target_type = models.CharField(max_length=50, choices=PARENT_TYPE, default='none')
    title = models.CharField(max_length=100, blank=True)
    contents = models.TextField(blank=True)
    writer = models.PositiveIntegerField(default=0)
    state = models.PositiveIntegerField(default=0)


class ReadInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.PositiveIntegerField(default=0)
    target_id = models.PositiveIntegerField(default=0)
    target_type = models.CharField(max_length=50, choices=PARENT_TYPE, default='none')
