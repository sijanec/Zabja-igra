def naredi_polje(n, k, zamik_n=1, zamik_k=1):
    polje = []
    for i in range(zamik_n, n + 1):
        for j in range(zamik_k, k + 1):
            polje.append([i, j])
    return polje


def zmanjsaj_polje(polje, list):
    for i in polje:
        if i in list:
            i.append(False)
    return polje


def zakleni_polja(polje, vrata):
    for i in polje:
        if i in vrata:
            i.append("zaklenjeno")
    return polje


def odkleni_polja(polje, vrata):
    for i in polje:
        if "zaklenjeno" in i:
            i.remove("zaklenjeno")


def lovska_poteza(polje, frog_position):
    mozno = []

    for i in [1, -1]:
        for j in [1, -1]:
            x = 1
            while True:
                if [frog_position[0] + x * i, frog_position[1] + x * j] in polje:
                    mozno.append([frog_position[0] + x * i, frog_position[1] + x * j])
                    x += 1
                else:
                    break
    return mozno


def trdnjavska_poteza(polje, frog_position):
    mozno = []

    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x = 1
        while True:
            if [frog_position[0] + i[0] * x, frog_position[1] + i[1] * x] in polje:
                mozno.append([frog_position[0] + i[0] * x, frog_position[1] + i[1] * x])
                x += 1
            else:
                break
    return mozno


def damina_poteza(polje, frog_position):
    return trdnjavska_poteza(polje, frog_position) + lovska_poteza(polje, frog_position)


def konjska_poteza(polje, frog_position):
    mozno = []

    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [1, 2]:
                if [frog_position[0] + i * k, frog_position[1] + j * (3 - k)] in polje:
                    mozno.append(
                        [frog_position[0] + i * k, frog_position[1] + j * (3 - k)]
                    )
    return mozno


def kraljeva_poteza(polje, frog_position):
    mozno = []

    for i in naredi_polje(
        frog_position[0] + 1,
        frog_position[1] + 1,
        frog_position[0] - 1,
        frog_position[1] - 1,
    ):
        if i in polje and i != frog_position:
            mozno.append(i)
    return mozno


def trdnjavska_pot(start, finish):
    if start[0] < finish[0] or start[1] < finish[1]:
        return naredi_polje(finish[0], finish[1], start[0], start[1])
    else:
        return naredi_polje(start[0], start[1], finish[0], finish[1])


def lovska_pot(start, finish):
    pot = []

    if finish[0] > start[0]:
        a = 1
    else:
        a = -1
    if finish[1] > start[1]:
        b = 1
    else:
        b = -1
    for i in range(0, abs(finish[0] - start[0]) + 1):
        pot.append([start[0] + i * a, start[1] + i * b])
    return pot


def damina_pot(start, finish):
    if finish[0] == start[0] or finish[1] == start[1]:
        return trdnjavska_pot(start, finish)
    else:
        return lovska_pot(start, finish)


def konjska_pot(start, finish):
    return [start, finish]


def kraljevska_pot(start, finish):
    return [start, finish]


def pojej_muhe(pot, muhe):
    for i in pot:
        if i in muhe:
            muhe.remove(i)
    return muhe


def poberi_kljuce(pot, kljuc):
    if kljuc in pot:
        kljuc = []
    return kljuc


def shrani_game_state(game_state, muhe, poteze, frog_position, varnost):
    return game_state.append([muhe, poteze, frog_position, varnost])


def povrni_game_state(game_state):
    if len(game_state) != 1:
        game_state.remove(game_state[-1])
    return game_state


def povrni_muhe(game_state):
    return game_state[-1][0]


def povrni_poteze(game_state):
    return game_state[-1][1]


def povrni_frog_position(game_state):
    return game_state[-1][2]


def povrni_kljuc(game_state):
    return game_state[-1][3][0]


def povrni_vrata(game_state):
    return game_state[-1][3][1]


def povrni_odprto(game_state):
    return game_state[-1][3][2]


def znakec(eno_polje, muhe, frog_position, kljuc, vrata, mozne_poteze=[False]):
    if False in eno_polje:
        return " "
    if eno_polje == frog_position:
        return "𓆏"
    if eno_polje == kljuc:
        return "🗝️"
    if eno_polje in muhe:
        return "M"
    if "zaklenjeno" in eno_polje:
        return "🔒"
    if eno_polje in mozne_poteze:
        return "▣"
    else:
        return "▢"


def visualize(polje, game_state, mozne_poteze=[False]):
    muhe = povrni_muhe(game_state)
    frog_position = povrni_frog_position(game_state)
    poteze = povrni_poteze(game_state)
    kljuc = povrni_kljuc(game_state)
    vrata = povrni_vrata(game_state)
    n = polje[-1][1] - polje[0][0] + 1
    vrstica = "1 "
    x = 0
    for i in polje:
        vrstica = (
            vrstica + znakec(i, muhe, frog_position, kljuc, vrata, mozne_poteze) + " "
        )
        x += 1
        if x % n == 0:
            print(vrstica)
            vrstica = str(x // n + 1) + " "
    vrstica = "  "
    for j in range(1, x // n + 1):
        vrstica = vrstica + str(j) + " "
    print(vrstica)
    print("")
    print(poteze)


slovar_funkcij_potez = {
    "konj": konjska_poteza,
    "trdnjava": trdnjavska_poteza,
    "dama": damina_poteza,
    "kralj": kraljeva_poteza,
    "lovec": lovska_poteza,
}
slovar_funkcij_poti = {
    "konj": konjska_pot,
    "trdnjava": trdnjavska_pot,
    "dama": damina_pot,
    "kralj": kraljevska_pot,
    "lovec": lovska_pot,
}

# Tukaj je potek igre


def igra(level):
    global slovar_funkcij_potez, slovar_funkcij_poti
    polje = level[0]
    prepovedano = level[1]
    game_state = level[2]

    polje = zmanjsaj_polje(polje, prepovedano)
    vrata = povrni_vrata(game_state)
    polje = zakleni_polja(polje, vrata)

    odklenjeno = povrni_odprto(game_state)
    poteze = povrni_poteze(game_state)
    frog_position = povrni_frog_position(game_state)
    muhe = povrni_muhe(game_state)
    odprto = povrni_odprto(game_state)
    kljuc = povrni_kljuc(game_state)
    pazitelj_premikov = []
    konec = False

    while konec == False:
        visualize(polje, game_state)
        poteza = str(input("Izberi potezo: ")).lower()
        if poteza == "nazaj":
            game_state = povrni_game_state(game_state)
            frog_position = povrni_frog_position(game_state)
            muhe = povrni_muhe(game_state)
            odprto = povrni_odprto(game_state)
            if pazitelj_premikov != []:
                poteze[pazitelj_premikov[-1]] += 1
                pazitelj_premikov.remove(pazitelj_premikov[-1])
            if odprto == False:
                zakleni_polja(polje, vrata)
            visualize(polje, game_state)
        elif poteze.get(poteza, 0) == 0:
            print("Ne moreš tega narediti!")
        else:
            mozne_poteze = slovar_funkcij_potez[poteza](polje, frog_position)
            visualize(polje, game_state, mozne_poteze)
            print(mozne_poteze)
            premik = (
                input("Izberi na katero polje se želiš premakniti: ")
                .replace("[", "")
                .replace("]", "")
                .split(",")
            )
            if premik[0].isnumeric() and premik[-1].isnumeric():
                premik = [int(premik[0]), int(premik[-1])]
            if premik in mozne_poteze:
                poteze[poteza] -= 1
                pazitelj_premikov.append(poteza)
                pot = slovar_funkcij_poti[poteza](frog_position, premik)
                frog_position = premik
                muhe = pojej_muhe(pot, muhe)
                kljuc = poberi_kljuce(pot, kljuc)
                if kljuc == []:
                    odprto = True
                    odkleni_polja(polje, vrata)
                if len(muhe) == 0:
                    konec = True
                varnost = [kljuc, vrata, odklenjeno]
                shrani_game_state(game_state, muhe, poteze, frog_position, varnost)
            else:
                print(mozne_poteze)
                print("Tega ne moreš narediti!")
    visualize(polje, game_state)
    print("Bravo, zmagal si!")


polje_1 = naredi_polje(8, 8)
prepovedano_1 = naredi_polje(4, 4)
polje_1 = zmanjsaj_polje(polje_1, prepovedano_1)
frog_position_1 = [6, 3]
kljuc_1 = [8, 1]
muhe_1 = naredi_polje(3, 7, 1, 6)
vrata_1 = naredi_polje(8, 5, 1, 5)
poteze_1 = {"konj": 3, "kralj": 2, "dama": 3, "lovec": 3, "trdnjava": 4}
odklenjeno_1 = False
varnost_1 = [kljuc_1, vrata_1, odklenjeno_1]
game_state_1 = [[muhe_1, poteze_1, frog_position_1, varnost_1]]

level_1 = [polje_1, prepovedano_1, game_state_1]

igra(level_1)
