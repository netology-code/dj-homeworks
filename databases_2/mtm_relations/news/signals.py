from django.db.models.signals import pre_save, post_save, pre_delete
from .models import SectionMember, Article


def pre_save_section_member(sender, instance, **kwargs):
    """
        Данная функция вызывается перед тем как произойдет сохранение SectionMember
    """
    pass


def post_save_section_member(sender, instance, **kwargs):
    """
        Данная функция вызывается после того как произойдет сохранение SectionMember
    """
    pass


def post_save_article(sender, instance, **kwargs):
    """
        Данная функция вызывается после того как произойдет сохранение Article
    """
    pass


def protect_last_section_member(sender, instance, **kwargs):
    """
        Данная функция вызывается перед удалением SectionMember
    """
    pass


pre_save.connect(pre_save_section_member, sender=SectionMember)
post_save.connect(post_save_section_member, sender=SectionMember)
pre_delete.connect(protect_last_section_member, sender=SectionMember)
post_save.connect(post_save_article, sender=Article)

