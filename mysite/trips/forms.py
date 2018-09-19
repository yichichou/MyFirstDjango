#ModelForm:跟某一個table作連動
from django.forms import ModelForm, TextInput

#datetime
from datetime import date
from .models import Record, Category

class RecordForm(ModelForm):

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args, **kwargs)
        by_user = Category.objects.filter(user=user) | Category.objects.filter(pk=39)
        self.fields['category'].queryset = by_user
        
    class Meta:
        model = Record  #用record物件來跟他作連動
        fields = ['date','description','category','cash','balance_type'] #要跟record連動的欄位 
        #用widgets進行客製化內容(這裡是用在date的小日曆)
        widgets = {
            #'資料表的欄位(也就是fields的值)':'選用的欄位格式'
            'date':TextInput(
                attrs={
                    'id':'datepicker1',
                    'value':date.today().strftime('%Y-%m-%d') #date.today()表示顯示今日日期，strftime表示顯示的方式
                }
            )
        }
        
