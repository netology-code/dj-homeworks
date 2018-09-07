from django.db import models
from django.db.models import CASCADE


class Player(models.Model):
    pass


class Game(models.Model):
    number = models.IntegerField(u'Угадываемое число')
    is_finish = models.BooleanField(u'Игра завершена', default=False)
    winner = models.ForeignKey(to=Player, related_name='winner', on_delete=CASCADE, blank=True, null=True)
    owner = models.ForeignKey(to=Player, related_name='owner', on_delete=CASCADE)
    try_count = models.IntegerField(u'Количество попыток', default=0)

    # Если игра окончилась, получаем количество попыток угадать число всеми игроками
    def save(self, *args, **kwargs):
        if self.is_finish:
            game_info_for_all_players = PlayerGameInfo.objects.filter(game=self.id)
            try_count = 0
            for info in game_info_for_all_players:
                try_count += info.try_count
            self.try_count = try_count
        super(Game, self).save(*args, **kwargs)


class PlayerGameInfo(models.Model):
    game = models.ForeignKey(to=Game, related_name='game', on_delete=CASCADE)
    player = models.ForeignKey(to=Player, related_name='player', on_delete=CASCADE)
    try_count = models.IntegerField(u'Количество попыток', default=1)