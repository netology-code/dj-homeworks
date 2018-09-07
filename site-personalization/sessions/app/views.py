import random

from django.shortcuts import render

from app.models import Game, Player, PlayerGameInfo


def show_home(request):
    if request.method == "POST":
        number = int(request.POST['number'])
        player_game_info = get_game_info_for_current_user(request)

        message = ''

        if player_game_info.game.number is number:
            player = Player.objects.filter(id=request.session.get('player_id')).first()
            player_game_info.game.is_finish = True
            player_game_info.game.winner = player
            player_game_info.game.save()
            message = 'Вы угадали число!'
        elif player_game_info.game.number < number:
            message = 'Загаданное число меньше числа %s' % number
        elif player_game_info.game.number > number:
            message = 'Загаданное число больше числа %s' % number

        return render(
            request,
            'home.html',
            {
                'message': message,
            }
        )
    else:
        message = get_message_to_owner(request)
        game = get_game(request)
        is_owner = current_player_is_owner(request, game)

        return render(
            request,
            'home.html',
            {
                'is_owner': is_owner,
                'number': game.number,
                'message': message,
            }
        )


def get_message_to_owner(request):
    game_id = request.session.get('game_id')
    player_id = request.session.get('player_id')
    games = Game.objects.filter(id=game_id, owner=player_id)
    if games:
        game = games.first()
        if game.is_finish:
            return 'Ваше число угадали с %s попытки!' % game.try_count
    return ''


def current_player_is_owner(request, game):
    player_id = get_player_id(request)
    player = Player.objects.filter(id=player_id)
    if player is not None:
        player = player.first()
    return player.__eq__(game.owner)


def create_new_game(request):
    number = random.randint(1, 10)
    player_id = get_player_id(request)

    current_players = Player.objects.filter(id=player_id)

    game = Game()
    game.number = number
    game.owner = current_players.first()
    game.save()
    return game


def get_game(request):
    games = Game.objects.filter(is_finish=False)
    if games:
        game = games.first()
    else:
        game = create_new_game(request)
    request.session['game_id'] = game.id
    return game


def get_player_id(request):
    player_id = request.session.get('player_id')
    if player_id is None:
        player = Player()
        player.save()
        player_id = player.id
        request.session['player_id'] = player_id
    return player_id


def get_game_info_for_current_user(request):
    player = Player.objects.filter(id=request.session.get('player_id')).first()
    game = Game.objects.filter(id=request.session.get('game_id')).first()
    game_infos = PlayerGameInfo.objects.filter(player=player, game=game, game__is_finish=False)
    if game_infos:
        game_info = game_infos.first()
        game_info.try_count += 1
        game_info.save()
    else:
        if not game or game.is_finish:
            game = get_game(request)
        game_info = PlayerGameInfo()
        game_info.player = player
        game_info.game = game
        game_info.save()
    return game_info
