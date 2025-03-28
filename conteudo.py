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
    'Dragão' : 200,
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
    'Finn' : 500,
    'Jake' : 1000,
    'Leviathan' : 6000
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
    'Minotauro' : 40,
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
        'Leviathan',
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
        'Leviathan',
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
# usar o index para navegar pelos indices

armas = {
    'Espada de Madeira' : 2,
    'Espada de Pedra' : 5,
    'Espada de Ferro' : 7,
    'Espada de Diamante' : 9,
    'Escudo' : 1,
    'Arco e Flecha' : 5,
    'Machado de Madeira' : 4,
    'Machado de Pedra' : 10,
    'Machado de Ferro' : 14,
    'Machado de Diamante' : 18,
    'LIFE TAKER' : 10000
    # magia talvez no futuro
}

armaduras = {
    'Armadura de Ferro' : 10,
    'Armadura de Aço' : 20,
    'Armadura de Diamante' : 30,
    'ARMADURA INQUEBRÁVEL' : 10000
}

items = [
    'Madeira', # golem, goblin
    'Pedra', # golem, goblin
    'Ferro', # bandido, goblin
    'Diamante', # bandido, goblin
    'Aço', # bandido, goblin
    'Fio', # aranha, goblin
    'Bife cru', # vaca
    'Costeleta crua', # porco
    'Frango cru', # galinha, passaro
    'Carneiro cru', # ovelha
    'Cervo cru', # veado
    'Cogumelo' # ITEM ALEATORIO bruxa, gnomo
    'Poção de Vida', # bruxa, goblin, gnomo
    'Poção de Vida Máxima', # bruxa, goblin, gnomo
    'Poção de Força', # bruxa, goblin, gnomo
    'Poção de Resistência', # bruxa, goblin, gnomo
    'Arco' # esqueleto
    'Flecha' # esqueleto
]

status = {
    'HP' : 40,
    'ATK' : 3,
    'DEF' : 0.3, # (em %)
    'BIOMA' : random.choice(biomas),
    'GOLD' : 10,
    'ARMA': 'Desarmado'
}

inv = {}
