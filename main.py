import random
import PySimpleGUI as pg

emoji = "😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😌😍😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁😣😖😫😢😩😭😤😠" \
        "😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀" \
        "👽👾🤖🎃😺😸😹😻😼😽🙀😿😾"


def update():
    r = random.choice(emoji)
    text_elem = window['result']
    text_elem.update("Результат: {}".format(r))
    print(r)


layout = [[pg.Button('Новый смайлик', enable_events=True, key='func', font='Helvetica 16')],
          [pg.Text('Результат:', size=(25, 1), key='result', font='Helvetica 16')]]

window = pg.Window('Генератор случайнго смайлика', layout, size=(350, 100))

while True:
    event, values = window.read()
    if event in (pg.WIN_CLOSED, 'Exit'):
        break
    if event == 'func':
        update()

window.close()
