from django.db import models

# class Location(models.Model):
#     city = models.CharField(maxlength=50)
#     state = models.CharField(maxlength=50, null=True, blank=True)
#     country = models.CharField(maxlength=50)
#
#     def __str__(self):
#         if self.state:
#             return "%s, %s, %s" % (self.city, self.state, self.country)
#         else:
#             return "%s, %s" % (self.city, self.country)

class Job(models.Model):
    bid = models.CharField(max_length=50, blank=True, default=0)
    bcount = models.IntegerField()


from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块 
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())     # 列出所有配色风格


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)