from app import app
from engine import Chess
from flask import request

game = Chess()


@app.route('/')
@app.route('/index')
def start():
    game.reset()
    return f'<html><body><center>{game.get_image()}<form action="/move" method="post"><input type="text" name="move"> </input><input type="submit" value="Move"></input></form></center></body></html>'


@app.route('/move', methods=['POST'])
def move():
    move = request.form['move']
    # print(f'The move is {move}')
    if game.is_legal(move):
        game.move(move)
        if not game.game_over():
            return f'<html><body><center>{game.get_image()}<form action="/move" method="post"><input type="text" name="move"> </input><input type="submit" value="Move"></input></form></center></body></html>'
        else:
            if game.get_result() != 'Draw':
                winner = 'White' if game.get_turn() == 'Black' else 'White'
                return f'<html><body><center>{game.get_image()}<form action="/move" method="post"><input type="text" name="move"> </input><input type="submit" value="Move"></input></form><p>Checkmate {winner}</p></center></body></html>'
            else:
                return f'<html><body><center>{game.get_image()}<form action="/move" method="post"><input type="text" name="move"> </input><input type="submit" value="Move"></input></form><p>Stalemate - Draw</p></center></body></html>'

    else:
        return f'<html><body><center>{game.get_image()}<form action="/move" method="post"><input type="text" name="move"> </input><input type="submit" value="Move"></input></form><p>Illegal Move</p></center></body></html>'
