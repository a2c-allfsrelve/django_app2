from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Friend(models.Model):
    name = models.CharField(max_length=10)
    mail = models.EmailField(max_length=100, validators=[
        RegexValidator(r'^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$')]) #バリデーションルールに正規表現を用いる
    gender = models.BooleanField()
    age = models.IntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(150)]) #モデルで最初からバリデーションを設定
    birthday = models.DateField()

    #カラムをテキストの値に変換したもの
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + \
            self.name + '(' + str(self.age) + ')>'
