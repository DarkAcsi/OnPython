import random
import emoji
import keyboard

emoji = "😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😌😍😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁😣😖😫😢😩😭😤😠" \
        "😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀" \
        "👽👾🤖🎃😺😸😹😻😼😽🙀😿😾"


def update():
    r = random.choice(emoji)
    print(r, r.encode('ascii', 'namereplace').decode()[3:-1])


def on_press(key):
    print(f'Press {key.name}')

def on_release(key):
    print(f'Release {key.name}')

while input() != 'exit':
    update()

