from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'buying_type', 'address',
                  'comments']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['phone'].label = 'Контактный телефон'
        self.fields['phone'].help_text = '*Пожалуйста, указывайте реальный номер телефона, по которому с Вами можно связаться'
        self.fields['email'].label = 'Почтовый ящик'
        self.fields['email'].required = False
        self.fields['buying_type'].label = 'Способ получения'
        self.fields['address'].label = 'Адрес доставки'
        self.fields['address'].help_text = '*Обязательно указывайте город!'
        self.fields['address'].required = False
        self.fields['comments'].label = 'Комментарии к заказу'
        self.fields['comments'].required = False