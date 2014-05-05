__author__ = '12'
# -*- coding: utf-8 -*-
from django import forms
from BaseApp.models import CustomUser, Tutor, Additional_information, ListCity
import json



CHOICES = ((1, '-------'), (2, 'Репетитор'), (3, 'Ученик'))

class Registration(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Логин'}), label='',
                                help_text="Введите 30 символов или менее. Буквы, цифры и знаки из набора @/./+/-/_")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'type': 'password'}),
                                help_text="цифры 0-9,латиница,буквы верхнего и нижнего регистра", label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля', 'type': 'password'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}), label='')
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Город', 'type': 'text'}), label='',
                                help_text="введите название своего города или выберете из списка")
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Адрес'}), label='',required=True)
    category = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'ng-model': 'checked'}),
                                help_text="выберете категорию из списка", label='', required=True)

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        self.city = json.dumps([
            city.Cities for city in ListCity.objects.all()
        ])

        self.widget = forms.TextInput(attrs={
            'class': 'text',
            'placeholder': 'City',
            'autocomplete': 'off',
            'data-provide': 'typeahead',
            'data-source': self.city})

        self.fields['city'] = forms.CharField(
            label='',
            required=True,
            widget=self.widget)

class Log_in(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), max_length=30, min_length=8)

class Review_form(forms.Form):
    review = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Коментарий'}))

class Custom_user_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'patronymic',)

class Tutor_settings_form(forms.ModelForm):
    experience = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Стаж', 'type': 'number'}), required=True)
    education = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Образование', 'type': 'text'}), required=True)
    work = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Работа', 'type': 'text'}), required=True)
    venue_of = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Место проведения', 'type': 'text'}), required=True)
    avatar = forms.ImageField(label='', required=False)
    class Meta:
        model = Tutor
        exclude = ('username', 'rating',)

class Additional_inf_settings_form(forms.ModelForm):
    subject_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Предмет', 'type': 'text'}), label='', required=True)
    section = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Раздел', 'type': 'text'}), label='', required=False)
    additions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Дополнение', 'type': 'text'}), label='', required=False)
    pupil_category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Категория ученика', 'type': 'text'}), label='', required=True)
    price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Цена', 'type': 'number'}), label='', required=True)
    class Meta:
        model = Additional_information
        exclude = ('tutor',)

class Additions_form(forms.Form):
    subject_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Предмет', 'type': 'text'}), label='', required=True)
    section = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Раздел', 'type': 'text'}), label='', required=False)
    additions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Дополнение', 'type': 'text'}), label='', required=False)
    pupil_category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Категория ученика', 'type': 'text'}), label='', required=True)
    price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Цена', 'type': 'number'}), label='', required=True)

CHOICES_for_contact_form = (('студент', 'студент'), ('школьник', 'школьник'), ('работающий', 'работающий'))

class Contact_form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'имя', 'type': 'text'}), label='', required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'фамилие', 'type': 'text'}), label='', required=True)
    category = forms.CharField(widget=forms.Select(choices=CHOICES_for_contact_form), label='', help_text="выберете категорию из списка", required=True)
    number_telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'номер телефона', 'type': 'number'}), label='', required=True)
