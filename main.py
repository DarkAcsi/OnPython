import random

emojis = "😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😌😍😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁😣😖😫😢😩😭😤😠" \
         "😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀" \
         "👽👾🤖🎃😺😸😹😻😼😽🙀😿😾"


def update():
    r = random.choice(emojis)
    print(r, r.encode('ascii', 'namereplace').decode()[3:-1])


while input() != 'exit':
    update()
