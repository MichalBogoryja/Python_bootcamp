import pymsgbox

name = pymsgbox.prompt('Jak masz na imię?')
pymsgbox.alert(f"Specjalne pozdrowienia dla {name.capitalize()}")
