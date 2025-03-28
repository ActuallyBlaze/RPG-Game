import conteudo
import random

nome = str(input('Por favor insere o nome do teu aventureiro: '))
def menu():
    print('------ BEM VINDO À AVENTURA ÉPICA ------')
    print(f'\nOlá, {nome}! Como desejas prosseguir na tua aventura?')
    escolha = str(input(
        '0. Sair\n'
        '1. Mostrar Status\n'
        '2. Mostrar Inventário\n'
        '3. Recolher Materiais\n'
        '4. Mudar de Bioma\n'
        '5. Explorar\n'
        '6. Craftar'
        '7. Desafiar o chefe do bioma\n'
        '.: '
    ))
    match escolha:
        case '1':
            status()
        case '2':
            inventario()
        case '3':
            materiais()
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            combate()

def status():
    print()
    print(f'Aqui estão os teus status atuais, {nome}!')
    for item in conteudo.status:
        print(item, ':', conteudo.status[item])
    print()
    menu()

def inventario():
    print()
    print(f'Aqui está o teu inventário, {nome}!')
    if len(conteudo.inv) == 0:
        print('Parece que ainda não tens nada no inventário!')
    else:
        for item in conteudo.inv:
            print(item, ':', conteudo.inv[item])
    escolha = str(input('Queres usar algum item? [s/n]\n.: '))
    if escolha == 's':
        item = str(input('Que item queres utilizar? [nome]\n.: '))
        if item in conteudo.inv:
            match item:
                case 'Poção de Vida':
                    conteudo.inv[item] -= 1
                    conteudo.status['HP'] += 15
                    # se a vida curada exceder a vida máxima, é retirada a vida a mais
                    if conteudo.status['HP'] > 40:
                        conteudo.status['HP'] == 40
                case 'Poção de Vida Máxima':
                    conteudo.inv[item] -= 1
                    conteudo.status['HP'] += 20
                case 'Poção de Força':
                    conteudo.inv[item] -= 1
                    conteudo.status['ATK'] += 5
                case 'Poção de Resistência':
                    print()
                case _:
                    print('Item introduzido não pode ser utilizado.')
        else:
            print('Item não encontrado.')
    print()
    menu()

def materiais():
    print()
    print('Saiste da safe zone à procura de materiais...')
    rng = random.randint(1, 10)
    item = random.choice(['Madeiras', 'Pedras'])
    quant = random.randint(2, 6)
    if rng <= 7:
        print('Materiais Encontrados!')
        escolha = str(input(f'Encontraste {quant} {item}, desejas guardar no teu inventário? [s/n]\n.: ')).lower()
        if escolha == 's':
            if item in conteudo.inv:
                conteudo.inv[item] += quant
            else:
                conteudo.inv.setdefault(item, quant)
            print('Materiais Guardados.')
        elif escolha == 'n':
            print('Materiais Mandados Fora.')
        else:
            print('Escolha Inválida.')
    else:
        print('Enquanto andavas, encontraste um inimigo!')
        escolha = str(input('Desejas fugir ou lutar? [1/2]\n.: '))
        if escolha == '1':
            print('Escolheste ficar e enfrentar o inimigo, boa sorte!')
            combate()
        elif escolha == '2':
            print('Fugiste da batalha com sucesso!')
        else:
            print('Escolha Inválida.')
    print()
    menu()

def combate():
    bioma = conteudo.status.get('BIOMA')
    indiceBioma = conteudo.biomas.index(bioma)
    listaMobs = conteudo.biomasMobs[indiceBioma]
    mob = random.choice(listaMobs)
    mobHP = conteudo.mobsHP.get(mob)
    mobATK = conteudo.mobsATK.get(mob)
    playerHP = conteudo.status.get('HP')
    playerATK =  conteudo.status.get('ATK')
    playerDEF = conteudo.status.get('DEF')
    if playerHP <= 0:
        print(f'O teu aventureiro morreu.\nFoi uma boa jornada, {nome}, boa sorte na próxima!')
    else:
        while mobHP > 0:
            if mobATK is None:
                mobHP -= playerATK
            else:
                playerHP -= mobATK - mobATK * playerDEF
                mobHP -= playerATK
            escolha = str(input(
                f'Deste {playerATK} de dano ao {mob}!\n'
                f'O {mob} deu-te {mobATK - mobATK * playerDEF} de dano!\n'
                f'O {mob} encontra-se agora com {mobHP:.2f} de HP e tu com {playerHP:.2f}, continuar ou fugir? [1/2]\n.: '
            )).lower()
            if escolha == '1':
                continue
            else:
                break
        conteudo.status['HP'] = playerHP
        print('Mob morto! Recebeste um monte de nada.')
        menu()

def drops():
    pass

menu()
