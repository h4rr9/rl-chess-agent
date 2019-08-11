from app import app
from engine import Chess
from flask import request, render_template, Markup

game = Chess()


@app.route('/')
@app.route('/index')
def start():
    game.reset()
    return render_template('board.html', image=Markup(game.get_image()), message='', moves=[])


@app.route('/setup', methods=['POST'])
def start_pos():
    print(request.get_data())
    fen_string = request.form['fen']
    game = Chess(fen_string=fen_string)
    return render_template('board.html', image=Markup(game.get_image()), message='', moves=[])


@app.route('/move', methods=['POST'])
def move():
    move = request.form['move']
    # print(f'The move is {move}')
    if game.is_legal(move):

        game.move(move)

        pair_moves = []

        for move_pair in map(tuple, zip(game.moves[::2], game.moves[1::2])):
            pair_moves.append(move_pair)

        if len(game.moves) % 2 == 1:
            pair_moves.append((game.moves[-1],))

        print(game.moves)

        if not game.game_over():
            return render_template('board.html', image=Markup(game.get_image()), message='', moves=pair_moves)
        else:
            if game.get_result() != 'Draw':
                winner = 'White' if game.get_turn() == 'Black' else 'Black'
                return render_template('board.html', image=Markup(game.get_image()), message=f'Checkmate - {winner} wins', moves=pair_moves)
            else:
                return render_template('board.html', image=Markup(game.get_image()), message='Stalemate - Draw', moves=pair_moves)

    else:
        return render_template('board.html', image=Markup(game.get_image()), message='Illegal Move', moves=pair_moves)
