from django import forms


class ArticleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.sections = kwargs.pop('sections')
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = 'Название'
        self.fields['title'].widget = forms.TextInput(
                                            attrs={
                                                'class': 'form-control'
                                            }
        )

        self.fields['text'].label = 'Текст'
        self.fields['text'].widget = forms.Textarea(
                                            attrs={
                                                'class': 'form-control'
                                            }
        )

        self.fields['pub_date'].label = 'Дата публикации'
        self.fields['pub_date'].widget = forms.SelectDateWidget(
                                                attrs={
                                                    'class': 'form-control'
                                                }
        )

        self.fields['main_section'].label = 'Основной раздел'
        self.fields['main_section'].widget = forms.CheckboxSelectMultiple()
        self.fields['main_section'].choices = tuple([(sec.pk, sec) for sec in self.sections])

        self.fields['additional_sections'].label = 'Дополнительные разделы'
        self.fields['additional_sections'].widget = forms.CheckboxSelectMultiple()
        self.fields['additional_sections'].choices = tuple([(sec.pk, sec) for sec in self.sections])
        self.fields['additional_sections'].required = False

        self.fields['image'].label = 'Изображение'
        self.fields['image'].widget = forms.FileInput(
                                            attrs={
                                                'class': 'form-control'
                                            }
        )


    title = forms.CharField()
    text = forms.CharField()
    pub_date = forms.DateField()
    main_section = forms.MultipleChoiceField()
    additional_sections = forms.MultipleChoiceField()
    image = forms.ImageField()


class SectionMemberForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.sections = kwargs.pop('sections')
        self.articles = kwargs.pop('articles')
        super(SectionMemberForm, self).__init__(*args, **kwargs)

        self.fields['section'].label = 'Раздел'
        self.fields['section'].widget = forms.Select(
                                                attrs={
                                                    'class': 'form-control'
                                                }
        )
        self.fields['section'].choices = tuple([(sec.pk, sec) for sec in self.sections])

        self.fields['main'].label = 'Основной'
        self.fields['main'].widget = forms.CheckboxInput(
                                            attrs={
                                                'class': 'form-control'
                                            }
        )
        self.fields['main'].required = False

        self.fields['article'].label = 'Статья'
        self.fields['article'].widget = forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
        self.fields['article'].choices = tuple([(art.pk, art) for art in self.articles])

    section = forms.ChoiceField()
    main = forms.BooleanField()
    article = forms.ChoiceField()