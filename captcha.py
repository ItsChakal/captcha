# Dev by Chakal
from PIL import Image, ImageDraw, ImageFont
import string
import random
from os import system
import os
from time import sleep
from colorama import Fore

system("cls")
string.ascii_letters = ("abdefghinpqrtuzABDEFGHINPQRTUZ0123456789")
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


captcha = random_char(8)
font = ImageFont.truetype("./marola.ttf", 45)
img = Image.new('RGB', (400, 100), color='white')
draw = ImageDraw.Draw(img)
draw.text((100, 30), captcha, (0, 0, 0), font=font)
img.save("captcha.png")
texte2 = """
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body {
 background-color: #232331;
 font-family: 'Roboto', sans-serif;
}
#captchaHeading {
    color: white;
   }
#captcha {
 height: 80%;
 width: 80%;
 font-size: 30px;
 letter-spacing: 3px;
 margin: auto;
 display: block;
 top: 0;
 bottom: 0;
 left: 0;
 right: 0;
}
.center {
 display: flex;
 flex-direction: column;
 align-items: center;
}
#textBox {
 height: 25px;
}

"""
texte = """<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

<body>
    <div class="center">
        <h1 id="captchaHeading">Veuillez ecrire les lettres suivante dans la console :</h1>
        <img src="captcha.png">
        <div id="captchaBackground">
        </div>
    </div>
</body>

</html>
"""
x = open('main.html', 'w')
x.write(texte)
x.close()
x = open('styles.css', 'w')
x.write(texte2)
x.close()
system("main.html")
sleep(0.5)
verif = input(Fore.CYAN + "Code :  ")
if verif == captcha:
    os.remove("main.html")
    os.remove("styles.css")
    os.remove("captcha.png")
    input(Fore.GREEN + "Correcte !")
else:
    os.remove("main.html")
    os.remove("styles.css")
    os.remove("captcha.png")
    input(Fore.RED + "Incorrecte !")
# Dev by Chakal
