
import random

mobsHP = {
    # hostis
    'Slime' : 20,
    'Esqueleto' : 10,
    'Zombie' : 20,
    'Lobo' : 15,
    'Morcego' : 3,
    'Urso' : 35,
    'Urso Polar' : 35,
    'Dragão' : 150,
    'Rato' : 3,
    'Ogre' : 40,
    'Goblin' : 15,
    'Aranha' : 10,
    'Aranha Gigante' : 30,
    'Minotauro' : 80,
    'Cobra' : 5,
    'Vampiro' : 30,
    'Demónio' : 50,
    'Escorpião' : 10,
    'Escorpião Gigante' : 40,
    'Fantasma' : 5,
    'Bruxa' : 20,
    'Múmia' : 15,
    'Lobisomem' : 40,
    'Bandido' : 15,
    'Orca' : 60,
    'Gato Selvagem' : 25,
    # neutros
    'Gnomo': 5,
    'Aldeão' : 20,
    'Golem' : 100,
    'Cão' : 15,
    'Gorila' : 80,
    'Lhama' : 25,
    'Baleia' : 70,
    'Bode' : 20,
    # passivos
    'Vaca' : 15,
    'Porco' : 10,
    'Galinha' : 5,
    'Ovelha' : 10,
    'Gato' : 10,
    'Veado' : 25,
    'Pássaro' : 5,
    'Borboleta' : 3,
    'Camelo' : 35,
    'Pinguim' : 10,
    'Foca' : 15,
    'Peixe' : 3,
    # bosses
    'Finn' : 200,
    'Jake' : 250,
    'Rei do Gelo': 280,
    'Leviathan' : 350
}

mobsATK = {
    # hostil
    'Slime' : 2,
    'Esqueleto' : 5,
    'Zombie' : 5,
    'Lobo' : 4,
    'Morcego' : 0.5,
    'Urso' : 25,
    'Urso Polar' : 25,
    'Dragão' : 50,
    'Rato' : 0.5,
    'Ogre' : 15,
    'Goblin' : 3,
    'Aranha' : 2,
    'Aranha Gigante' : 6,
    'Minotauro' : 30,
    'Cobra' : 2,
    'Vampiro' : 15,
    'Demónio' : 25,
    'Escorpião' : 4,
    'Escorpião Gigante' : 12,
    'Fantasma' : 2,
    'Bruxa' : 10,
    'Múmia' : 5,
    'Lobisomem' : 20,
    'Bandido' : 7,
    'Orca' : 25,
    'Gato Selvagem' : 10,
    # neutro
    'Gnomo': 1.5,
    'Aldeão' : 7,
    'Golem' : 35,
    'Cão' : 4,
    'Gorila' : 30,
    'Lhama' : 0.1,
    'Baleia' : 30,
    'Bode' : 7,
    # bosses
    'Finn' : 60,
    'Jake' : 100,
    'Rei do Gelo': 115,
    'Leviathan' : 150
}

biomas = [
    'Floresta',
    'Oceano',
    'Ruinas',
    'Cemitério',
    'Planície',
    'Deserto',
    'Glaciar',
    'Floresta Assombrada',
    'Caverna',
    'Masmorra',
    'Montanha',
    'Submundo',
    'Pântano',
    'Selva',
    'Savana',
]

biomasMobs = [
    ( # floresta
        'Lobo',
        'Urso',
        'Cobra',
        'Rato',
        'Vaca',
        'Borboleta',
        'Veado',
        'Porco',
        'Ovelha',
        'Cão',
        'Gato',
        'Gato Selvagem',
        'Galinha',
        'Bandido',
        'Minotauro',
        'Ogre',
        'Aranha',
        'Gnomo',
        'Lobisomem',
        'Pássaro',
        'Goblin',
        'Gorila'
    ),
    ( # oceano
        'Orca',
        'Baleia',
        'Peixe'
    ),
    ( # ruinas
        'Esqueleto',
        'Slime',
        'Zombie',
        'Morcego',
        'Rato',
        'Aranha',
        'Aranha Gigante',
        'Fantasma',
        'Bandido'
    ),
    ( # cemiterio
        'Esqueleto',
        'Morcego',
        'Vampiro',
        'Fantasma',
        'Aranha',
        'Múmia',
        'Rato',
        'Bruxa',
        'Lobisomem',
    ),
    ( # planicie
        'Vaca',
        'Porco',
        'Galinha',
        'Ovelha',
        'Gato',
        'Veado',
        'Pássaro',
        'Borboleta',
        'Cão',
        'Gato Selvagem',
        'Aldeão',
        'Golem',
        'Bandido',
        'Goblin'
    ),
    ( # deserto
        'Lhama',
        'Camelo',
        'Esqueleto',
        'Cobra',
        'Escorpião',
        'Escorpião Gigante',
        'Aranha',
        'Aranha Gigante',
        'Múmia'
    ),
    ( # glaciar
        'Orca',
        'Foca',
        'Pinguim',
        'Lobo'
    ),
    ( # floresta assombrada
        'Fantasma',
        'Vampiro',
        'Rato',
        'Morcego',
        'Esqueleto',
        'Zombie',
        'Lobo',
        'Minotauro',
        'Cobra',
        'Lobisomem',
        'Demónio',
        'Aranha',
        'Aranha Gigante',
        'Ogre',
        'Bruxa'
    ),
    ( # caverna
        'Esqueleto',
        'Zombie',
        'Morcego',
        'Rato',
        'Goblin',
        'Aranha',
        'Fantasma'
    ),
    ( # masmorra
        'Rato',
        'Morcego',
        'Vampiro',
        'Fantasma',
        'Aranha',
        'Bruxa'
    ),
    ( # montanha
        'Bode',
        'Lobo',
        'Veado',
        'Urso',
    ),
    ( # submundo
        'Esqueleto',
        'Zombie',
        'Morcego',
        'Dragão',
        'Aranha Gigante',
        'Vampiro',
        'Demónio',
        'Escorpião Gigante',
        'Fantasma',
        'Múmia'
    ),
    ( # pantano
        'Slime',
        'Morcego',
        'Rato',
        'Ogre',
        'Bruxa',
        'Gato',
        'Peixe',
        'Pássaro',
        'Cobras',
        'Gato Selvagem'
    ),
    ( # selva
        'Cobra',
        'Gorila',
        'Pássaro',
        'Minotauro',
        'Aranha',
        'Aranha Gigante',
        'Goblin',
        'Gnomo',
        'Lobo',
        'Urso',
        'Gato Selvagem',
        'Borboleta',
        'Pássaro',
        'Bruxa',
        'Porco'
    ),
    ( # savana
        'Cobra',
        'Porco',
        'Gato Selvagem',
        'Pássaro',
        'Borboleta',
        'Minotauro',
        'Bruxa',
        'Aranha',
        'Aranha Gigante',
        'Goblin',
    )
]

armas = {
    'Espada de Madeira' : 2,
    'Espada de Pedra' : 5,
    'Espada de Ferro' : 7,
    'Espada de Diamante' : 9,
    'Escudo' : 1,
    'Arco' : 5,
    'Machado de Madeira' : 4,
    'Machado de Pedra' : 10,
    'Machado de Ferro' : 14,
    'Machado de Diamante' : 18,
    'Espada do Finn' : 50,
    'Cajado do Rei do Gelo' : 75,
    'LIFE TAKER' : 1000
    # magia talvez
}

armaduras = {
    'Armadura de Ferro' : 10,
    'Armadura de Aço' : 20,
    'Armadura de Diamante' : 30,
    'Armadura do Jake' : 75,
    'ARMADURA INQUEBRÁVEL' : 1000
}

items = [
    'Madeira', # golem, goblin
    'Pedra', # golem, goblin
    'Ferro', # bandido, goblin, golem
    'Diamante', # bandido, goblin, golem
    'Aço', # bandido, goblin, golem
    'Fio', # aranha, goblin
    'Bife Cru', # vaca
    'Costeleta Crua', # porco
    'Frango Cru', # galinha, passaro
    'Carneiro Cru', # ovelha
    'Cervo Cru', # veado
    'Cogumelo' # bruxa, gnomo, ganhar item aleatorio, construir
    'Poção de Vida', # bruxa, goblin, gnomo, construir
    'Poção de Vida Máxima', # bruxa, goblin, gnomo, construir
    'Poção de Força', # bruxa, goblin, gnomo, construir
    'Poção de Resistência', # bruxa, goblin, gnomo, construir
    'Arco', # esqueleto
    'Flecha', # esqueleto
    'Bife Assado', # cozinhar
    'Costeleta Assada', # cozinhar
    'Frango Assado', # cozinhar
    'Carneiro Assado', # cozinhar
    'Cervo Assado', # cozinhar
    'Frasco' # bruxa
]

itemsCraftaveis = [
    'Espada de Madeira', # 1
    'Espada de Pedra', # 2
    'Espada de Ferro', # 3
    'Espada de Diamante', # 4
    'Arco', # 5
    'Flecha', # 6
    'Machado de Madeira', # 7
    'Machado de Pedra', # 8
    'Machado de Ferro', # 9
    'Machado de Diamante', # 10
    'Poção de Vida', # 11
    'Poção de Vida Máxima', # 12
    'Poção de Força', # 13
    'Poção de Resistência' # 14
]

status = {
    'HP' : 40,
    'ATK' : 3,
    'DEF' : 2,
    'BIOMA' : random.choice(biomas),
    'GOLD' : 10,
    'ARMA': 'Desarmado'
}

inv = {}
