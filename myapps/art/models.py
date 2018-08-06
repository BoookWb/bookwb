from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='分类名')
    add_time = models.DateTimeField(verbose_name='添加时间',
                                    auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table ='t_cate'#对应的表名
        verbose_name ='分类表'
        verbose_name_plural=verbose_name#去除复数s


class Art(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    summary = models.CharField(max_length=200,
                               verbose_name='简介')
    #content = models.TextField(verbose_name='内容',
     #                          null=True)

    content = UEditorField(verbose_name='内容',#给你的模型类起一个更可读的名字
                           width=600,height=480,
                           imagePath='art/ueditor_images',#图片路径
                           filePath='art/ueditor_files',# 文件路径
                           toolbars='full',#配置你想显示的工具栏
                           blank=True)#工具栏可以为空
    author = models.CharField(max_length=50,
                              verbose_name='作者')
    publish_time = models.DateTimeField(verbose_name='发布时间',
                                        auto_now_add=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='分类')
    # upoad_to 指定图片存储路径是相当于MEDIA_ROOT
    cover = models.ImageField(verbose_name='封面',
                              upload_to='art/images/',
                              null=True,
                              blank=True)
    def __str__(self):
        return self.title



    class Meta:
        db_table = 't_art'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name
