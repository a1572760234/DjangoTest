from django.db import models
# Create your models here.

# 1.模型类,需要继承自models.Model
# 2.系统会自动为该类添加主键(属性)----id
# 3.定义name字段(属性)  字段名 = modle.类型(选项)
# 字段名其实就是数据表的字段名,不要使用Python/Mysql的关键字
class Book(models.Model):
    #id已自动创建

    #name,varchar(选项)===>varchar(10)
    name = models.CharField(max_length=10)