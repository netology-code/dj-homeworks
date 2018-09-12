from django import forms
# from .models import Section, Article


class ArticleForm(forms.Form):
    title = forms.CharField(label='Название', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    text = forms.CharField(label='Текст', widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    pub_date = forms.DateField(label='Дата публикации', widget=forms.SelectDateWidget(
        attrs={
            'class': 'form-control'
        }
    ))
    # main_section = forms.MultipleChoiceField(
    #                                  label='Основной раздел',
    #                                  choices=tuple([(sec.pk, sec) for ind, sec in enumerate(Section.objects.all()) if sec.pk != 1]),
    #                                  widget=forms.CheckboxSelectMultiple()
    #)
    # additional_sections = forms.MultipleChoiceField(
    #                                  label='Дополнительные разделы',
    #                                  choices=tuple([(sec.pk, sec) for ind, sec in enumerate(Section.objects.all()) if sec.pk != 1]),
    #                                  widget=forms.CheckboxSelectMultiple(),
    #                                  required=False
    #)
    # image = forms.ImageField(
    #               label='Изображение',
    #               widget=forms.FileInput(
    #                            attrs={
    #                               'class': 'form-control'
    #                           }
    #               )
    #)


class SectionMemberForm(forms.Form):
    # section = forms.ChoiceField(
    #                   label='Раздел',
    #                   choices=tuple([(sec.pk, sec) for sec in Section.objects.exclude(pk=1)]),
    #                   widget=forms.Select(
    #                                 attrs={
    #                                     'class': 'form-control'
    #                                 }
    #                   )
    # )
    main = forms.BooleanField(
                    label='Основной',
                    required=False,
                    widget=forms.CheckboxInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                    )
    )
    # article = forms.ChoiceField(
    #                   label='Статья',
    #                   choices=tuple([(sec.pk, sec) for sec in Article.objects.all()]),
    #                   widget=forms.Select(
    #                                   attrs={
    #                                       'class': 'form-control'
    #                                   }
    #                   )
    # )