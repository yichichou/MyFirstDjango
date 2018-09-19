from django.db import models
from django.db.models import CharField,DateField,ForeignKey,IntegerField
from django.contrib.auth.models import User
# Create your models here.
#Django 預設會為每一個 Model 加上 id 欄位，並將這個欄位設成 primary key（主鍵）。
#model相關參數參考網址：https://docs.djangoproject.com/en/1.8/ref/models/fields/
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	
	def __str__ (self):
		return self.title
	


BALANCE_TYPE=((u'收入',u'收入'),(u'支出',u'支出'))  #(key,value)
class Category(models.Model):
	user = models.ForeignKey(User,null=True)
	category = CharField(max_length=20)
	
	def __str__(self):
		return self.category #表示用catrgory直接來顯示名稱

#foreignKey中on_delete的參數可以有哪些：
#models.CASCADE:若原生的某一筆資料的值被刪除，而屬於forign的那個關聯資料表的有出現那個值的資料全部都會被刪除
#models.PROTECT:不允許某個值被刪除
#models.SET_NULL:要搭配null=True:關聯資料表的某個值若被刪除，則值只會變成null(null在python中是none)
#models.SET_DEFAULT:要搭配DEFAULT:跟上面類似，會將null值變成自己要設定的值
#models.SET():要傳入function
class Record(models.Model):
	user = models.ForeignKey(User,null=True)
	date=DateField()
	description=CharField(max_length=300)
	category = ForeignKey(Category,on_delete=models.SET_NULL,null=True)
	cash = IntegerField()
	balance_type = CharField(max_length=2,choices=BALANCE_TYPE)

	def __str__(self):
		return self.description