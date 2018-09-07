from django.contrib import admin

from app.models import Player, Game, PlayerGameInfo


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', )


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'winner', 'try_count', 'is_finish', )


class PlayerGameInfoAdmin(admin.ModelAdmin):
    list_display = ('try_count', )


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerGameInfo, PlayerGameInfoAdmin)