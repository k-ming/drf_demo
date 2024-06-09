# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User


class Flower(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    product_name = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    bust = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)
    habit = models.CharField(max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)
    value = models.CharField(max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)

    # 新增2个字段到flower模型中
    # owner = models.ForeignKey('auth.User', related_name='flower',on_delete=models.CASCADE, null=True, default=None)
    owner = models.ForeignKey(User, related_name='flower',on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        managed = True
        db_table = 'flower'


    # 新增save方法
    def save(self, *args, **kwargs):
        """
        使用`pygments`库创建一个高亮显示的HTML表示代码段。
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title':self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos\
                                ,full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Flower, self).save(*args, **kwargs)


