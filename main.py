import random

emojis = "😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😌😍😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁😣😖😫😢😩😭😤😠" \
         "😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀" \
         "👽👾🤖🎃😺😸😹😻😼😽🙀😿😾"


def update():
    r = random.choice(emojis)
    print(r, r.encode('ascii', 'namereplace').decode()[3:-1])

try:
    while input() != 'exit':
        update()
except EOFError:
    print("Ошибка во время исполнения")
