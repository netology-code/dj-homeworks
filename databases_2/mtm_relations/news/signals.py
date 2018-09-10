from django.db.models.signals import pre_save, post_save, pre_delete
from .models import SectionMember, Article, Section
from django.db.models import Q, ProtectedError


def pre_save_section_member(sender, instance, **kwargs):
    relations = sender.objects.filter(article=instance.article)

    # New object
    if sender.objects.filter(Q(pk=instance.pk)).count() == 0:
        if relations.filter(~Q(pk=instance.pk) & Q(section=instance.section)).count() > 0:
            raise Exception("Такое соотношение уже имеется")
    # Old one
    else:
        if not instance.main and relations.count() == 1:
            raise ProtectedError('Изменить статус основного раздела можно только сделав другой раздел основным',
                                 instance)


def post_save_section_member(sender, instance, **kwargs):
    relations = sender.objects.filter(Q(article=instance.article) & ~Q(pk=instance.pk))
    if instance.main:
        for rel in relations.filter(~Q(pk=instance.pk)):
            rel.main = False
            rel.save()

    relations = sender.objects.filter(Q(article=instance.article) & Q(main=True))

    if relations.count() == 0:
        default_section_member_qs = sender.objects.filter(Q(article=instance.article) & Q(section_id=1))

        if default_section_member_qs.count() == 1:
            default_section_member = default_section_member_qs.get()
            default_section_member.main = True
            default_section_member.save()
        else:
            create_default_section_member(instance.article)


def create_default_section_member(article):
    rel = SectionMember()
    rel.article = article
    rel.section = Section.objects.get(pk=1)
    rel.main = True
    rel.save()


def post_save_article(sender, instance, **kwargs):
    relations = SectionMember.objects.filter(Q(article=instance) & Q(main=True))

    if relations.count() == 0:
        create_default_section_member(instance)


def protect_last_section_member(sender, instance, **kwargs):
    relations = sender.objects.filter(article=instance.article)
    default_section = Section.objects.get(pk=1)

    if relations.count() == 1:
        raise ProtectedError('Нельзя удалить единственный раздел', instance)
    elif instance.main and instance.section != default_section:
        try:
            default_section_member = sender.objects.get(section=default_section)
            default_section_member.main = True
        except:
            create_default_section_member(instance.article)
    elif instance.main and instance.section == default_section:
        raise Exception('Нельзя удалить раздел который идет основным по дефолту, '
                        'для этого сначала нужно сделать основным другой раздел')


pre_save.connect(pre_save_section_member, sender=SectionMember)
post_save.connect(post_save_section_member, sender=SectionMember)
pre_delete.connect(protect_last_section_member, sender=SectionMember)
post_save.connect(post_save_article, sender=Article)

