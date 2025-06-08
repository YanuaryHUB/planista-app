from flask import Flask, render_template
import random

app = Flask(__name__)

wulgaryzmy = [
    "Znowu ci handlowcy coś namieszali!",
    "Jak mam to zaplanować, skoro brief wygląda jakby pisał go pies?",
    "Czy oni serio myślą, że czas się rozciąga?",
    "Jakbym miał drukarkę czasu, to bym może zdążył.",
    "Niech mi ktoś powie, jak to ma zejść z maszyny w 2 godziny.",
    "Kto im powiedział, że kolory same się dopasują?",
    "Ciekawe czy handlowiec w ogóle widział tę maszynę na oczy.",
    "Dajcie mi dzień bez cudów i magii w plikach.",
    "Znów chcą zadruk na złotym podłożu bez dodatkowych kosztów.",
    "Niech ktoś im powie, że lakier to nie Photoshop.",
    "Jak mam zaplanować coś, czego fizycznie nie da się wydrukować?",
    "Brief ma 3 linijki, a oczekują cuda na kiju.",
    "Handlowcy myślą, że czas produkcji to fikcja literacka.",
    "Siedzę tu znowu i ratuję projekt zrobiony w Paintcie.",
    "Ciekawe kiedy handlowcy odkryją istnienie specyfikacji technicznych.",
    "Ile razy mam mówić, że nie robimy cudów bez materiałów?",
    "Znowu plik bez spadów. Ciekawe jak im to wychodzi.",
    "Ktoś chyba myśli, że pantone to styl życia, nie kolor.",
    "Dzięki handlowcom znowu siedzę po godzinach.",
    "Planista to nie wróżbita, ale coraz częściej się nim czuję."
]

@app.route("/")
def index():
    tekst = random.choice(wulgaryzmy)
    return render_template("index.html", tekst=tekst)
