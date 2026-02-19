from django import forms
from apps.shops_app.models import Product, Shop, Order






class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'description', 'bot_token', 'chat_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'bot_token': forms.TextInput(attrs={'class': 'form-control'}),
            'chat_id': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
        }


class ProductForm(forms.ModelForm):
    shop = forms.ModelChoiceField(
        queryset=Shop.objects.none(),
        label='Shops',
        widget=forms.Select(attrs={'class': 'cyber-input'})
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'shop', 'description', 'image', 'stock', 'unity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'unity': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['shop'].queryset = Shop.objects.filter(owner=user)



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'phone_number', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }