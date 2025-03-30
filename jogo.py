import conteudo
import random

nome = str(input('Por favor insere o nome do teu aventureiro: '))

def menu():
    if conteudo.status['HP'] <= 0:
        print(f'O teu aventureiro morreu.\nFoi uma boa jornada, {nome}, boa sorte na próxima!')
    else:
        print('\n------ BEM VINDO À AVENTURA ÉPICA ------')
        print(f'\nOlá, {nome}! Como desejas prosseguir na tua aventura?')
        escolha = str(input(
            '0. Sair\n'
            '1. Mostrar Status\n'
            '2. Mostrar Inventário\n'
            '3. Recolher Materiais\n'
            '4. Mudar de Bioma\n'
            '5. Explorar\n'
            '6. Construir\n'
            '7. Cozinhar\n'
            '8. Desafiar o chefe do bioma\n'
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
                bioma()
            case '5':
                explorar()
            case '6':
                construir()
            case '7':
                cozinhar()
            case '8':
                boss()

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
        escolha = str(input('Queres usar algum item? [1/2]\n.: '))
        if escolha == '1':
            item = str(input('Que item queres utilizar? [nome]\n.: '))
            if item in conteudo.inv:
                conteudo.inv[item] -= 1
                match item:
                    case 'Poção de Vida':
                        conteudo.status['HP'] += 15
                        # se a vida curada exceder a vida máxima, é retirada a vida a mais
                        if conteudo.status['HP'] > 40:
                            conteudo.status['HP'] = 40
                    case 'Poção de Vida Máxima':
                        conteudo.status['HP'] += 20
                    case 'Poção de Força':
                        conteudo.status['ATK'] += 5
                    case 'Poção de Resistência':
                        conteudo.status['DEF'] += 0.5
                    case 'Bife Assado':
                        conteudo.status['HP'] += 5
                        if conteudo.status['HP'] > 40:
                            conteudo.status['HP'] = 40
                    case 'Costeleta Assada':
                        conteudo.status['HP'] += 5
                        if conteudo.status['HP'] > 40:
                            conteudo.status['HP'] = 40
                    case 'Frango Assado':
                        conteudo.status['HP'] += 5
                        if conteudo.status['HP'] > 40:
                            conteudo.status['HP'] = 40
                    case 'Carneiro Assado':
                        conteudo.status['HP'] += 5
                        if conteudo.status['HP'] > 40:
                            conteudo.status['HP'] = 40
                    case 'Cervo Assado':
                        conteudo.status['HP'] += 5
                        if conteudo.status['HP'] > 40:
                            conteudo.status['HP'] = 40
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
    item = random.choice(['Madeira', 'Pedra'])
    quant = random.randint(2, 6)
    if rng <= 7:
        print('Materiais Encontrados!')
        escolha = str(input(f'Encontraste {quant} de {item}, desejas guardar no teu inventário? [1/2]\n.: ')).lower()
        if escolha == '1':
            if item in conteudo.inv:
                conteudo.inv[item] += quant
            else:
                conteudo.inv.setdefault(item, quant)
            print('Materiais Guardados.')
        else:
            print('Materiais Mandados Fora.')
    else:
        print('Enquanto andavas, encontraste um inimigo!')
        escolha = str(input('Desejas fugir ou lutar? [1/2]\n.: '))
        if escolha == '1':
            print('Escolheste ficar e enfrentar o inimigo, boa sorte!')
            combate()
        else:
            print('Fugiste da batalha com sucesso!')
    print()
    menu()

def bioma():
    print()
    escolha = str(input(
        'Para que bioma desejas ir?\n'
        '1. Floresta\n'
        '2. Oceano\n'
        '3. Ruinas\n'
        '4. Cemitério\n'
        '5. Planície\n'
        '6. Deserto\n'
        '7. Glaciar\n'
        '8. Floresta Assombrada\n'
        '9. Caverna\n'
        '10. Masmorra\n'
        '11. Montanha\n'
        '12. Submundo\n'
        '13. Pântano\n'
        '14. Selva\n'
        '15. Savana\n[nome] .: '
    ))
    if conteudo.status['BIOMA'] == escolha:
        print('Já estás no bioma introduzido!')
    else:
        conteudo.status['BIOMA'] = escolha
        print(f'Estás agora no bioma {escolha}.')
    print()
    menu()

def explorar():
    print()
    print('Saiste da safe zone para explorar o mundo...')
    rng = random.randint(1, 10)
    item = random.choice(['Ferro', 'Diamante', 'Aço', 'Cogumelo', 'Espada de Madeira', 'Espada de Pedra', 'Arco e Flecha', 'Machado de Madeira', 'Armadura de Ferro', 'Pedra', 'Fio'])
    if rng <= 3:
        escolha = str(input(f'Enquanto andavas, encontraste um {item} no chão, desejas guardar no teu inventário? [1/2]\n.: ')).lower()
        if escolha == '1':
            if item in conteudo.inv: # feito desta maneira pois apenas com o conteudo.inv[item] += 1 nao estava a adicionar ao inv
                conteudo.inv[item] += 1
            else:
                conteudo.inv.setdefault(item, 1)
            print('Item Guardado.')
        else:
            print('Item Mandado Fora.')
    else:
        print('Enquanto andavas, encontraste um inimigo!')
        escolha = str(input('Desejas fugir ou lutar? [1/2]\n.: '))
        if escolha == '1':
            print('Escolheste ficar e enfrentar o inimigo, boa sorte!')
            combate()
        else:
            print('Fugiste da batalha com sucesso!')
    print()
    menu()

def construir():
    escolha = str(input(
        'Que item queres construir?\n'
        '1. Espada de Madeira [3 Madeiras]\n'
        '2. Espada de Pedra [2 Pedras ; 1 Madeira]\n'
        '3. Espada de Ferro [2 Ferros ; 1 Madeira]\n'
        '4. Espada de Diamante [2 Diamantes ; 1 Madeira]\n'
        '5. Arco [2 Fios ; 3 Madeiras]\n'
        '6. Flecha [1 Pedra ; 1 Madeira]\n'
        '7. Machado de Madeira [4 Madeiras]\n'
        '8. Machado de Pedra [3 Pedras ; 1 Madeira]\n'
        '9. Machado de Ferro [3 Ferros ; 1 Madeira]\n'
        '10. Machado de Diamante [3 Diamantes ; 1 Madeira]\n'
    ))
    # usar mesmo esquema do cozinhar(), meter poçoes e armadura tambem

def cozinhar():
    print()
    escolha = str(input(
        'Qual carne queres cozinhar?\n'
        '1. Bife Cru\n'
        '2. Costeleta Crua\n'
        '3. Frango Cru\n'
        '4. Carneiro Cru\n'
        '5. Cervo cru\n[nome] .: '
    ))
    if escolha in conteudo.inv:
        if 'Madeira' in conteudo.inv:
            conteudo.inv['Madeira'] -= 1
            conteudo.inv[escolha] -= 1
            match escolha:
                case 'Bife Cru':
                    conteudo.inv['Bife Assado'] += 1
                case 'Costeleta Crua':
                    conteudo.inv['Costeleta Assada'] += 1
                case 'Frango Cru':
                    conteudo.inv['Frango Assado'] += 1
                case 'Carneiro Cru':
                    conteudo.inv['Carneiro Assado'] += 1
                case 'Cervo Cru':
                    conteudo.inv['Cervo Assado'] += 1
        else:
            print('Não tens madeira para cozinhar a carne.')
    else:
        print('Não tens essa carne no teu inventário.')
    print()
    menu()

def boss():
    bioma = conteudo.status.get('BIOMA')
    match bioma:
        case 'Floresta':
            boss = 'Finn'
            print(f'O boss do bioma {bioma} é o {boss}!')
        case 'Selva':
            boss = 'Jake'
            print(f'O boss do bioma {bioma} é o {boss}!')
        case 'Glaciar':
            boss = 'Rei do Gelo'
            print(f'O boss do bioma {bioma} é o {boss}!')
        case 'Oceano':
            boss = 'Leviathan'
            print(f'O boss do bioma {bioma} é o {boss}!')

    if boss is None:
        print(f'Não existe um boss no bioma em que te encontras! [{bioma}]')
    else:
        bossHP = conteudo.mobsHP.get(boss)
        bossATK = conteudo.mobsATK.get(boss)
        playerHP = conteudo.status.get('HP')
        playerATK =  conteudo.status.get('ATK')
        playerDEF = conteudo.status.get('DEF') * 0.04
        while bossHP > 0:
            dmg = bossATK - bossATK * playerDEF
            playerHP -= dmg
            bossHP -= playerATK
            print(f'Deste {playerATK} de dano ao {boss}!\n'
                f'O {boss} deu-te {dmg:.2f} de dano!'
            )
            conteudo.status['HP'] = round(playerHP, 2) # atualizar hp
            if bossHP < 0 or playerHP < 0:
                break
            escolha = str(input(f'O {boss} encontra-se agora com {bossHP:.2f} de HP e tu com {playerHP:.2f}, continuar ou fugir? [1/2]\n.: ')).lower()
            if escolha == '1':
                continue
            else:
                print('Fugiste da batalha com sucesso.')
                menu()

        if bossHP <= 0:
            print(f'Parabéns, mataste o boss {boss}! Ficaste com {playerHP} de HP.')
            item = drops(boss)
            escolha = str(input(f'Encontraste 1 {item}, desejas guardar no teu inventário? [1/2]\n.: ')).lower()
            if escolha == '1':
                if item in conteudo.inv:
                    conteudo.inv[item] += 1
                else:
                    conteudo.inv.setdefault(item, 1)
                print('Item Guardado.')
            else:
                print('Item Mandado Fora.')
    menu()
    print()


def combate():
    print()
    bioma = conteudo.status.get('BIOMA')
    indiceBioma = conteudo.biomas.index(bioma)
    listaMobs = conteudo.biomasMobs[indiceBioma]
    mob = random.choice(listaMobs)
    mobHP = conteudo.mobsHP.get(mob)
    mobATK = conteudo.mobsATK.get(mob)
    playerHP = conteudo.status.get('HP')
    playerATK =  conteudo.status.get('ATK')
    playerDEF = conteudo.status.get('DEF') * 0.04

    while mobHP > 0:
        if mobATK is None:
            mobHP -= playerATK
            print(f'Deste {playerATK} de dano ao {mob}!')
        else:
            dmg = mobATK - mobATK * playerDEF
            playerHP -= dmg
            mobHP -= playerATK
            print(f'Deste {playerATK} de dano ao {mob}!\n'
                f'O {mob} deu-te {dmg:.2f} de dano!'
            )
        conteudo.status['HP'] = round(playerHP, 2) # atualizar hp
        if mobHP < 0 or playerHP < 0:
            break
        escolha = str(input(f'O {mob} encontra-se agora com {mobHP:.2f} de HP e tu com {playerHP:.2f}, continuar ou fugir? [1/2]\n.: ')).lower()
        if escolha == '1':
            continue
        else:
            print('Fugiste da batalha com sucesso.')
            menu()

    print(f'O {mob} morreu! Ficaste com {playerHP} de HP.')
    if mobHP <= 0:
        quant = random.randint(2, 6)
        item = drops(mob)
        if item != None:
            escolha = str(input(f'Encontraste {quant} de {item}, desejas guardar no teu inventário? [1/2]\n.: ')).lower()
            if escolha == '1':
                if item in conteudo.inv:
                    conteudo.inv[item] += quant
                else:
                    conteudo.inv.setdefault(item, quant)
                print('Item Guardado.')
            else:
                print('Item Mandado Fora.')
    menu()
    print()

def drops(mob):
    match mob:
        case 'Golem':
            drop = random.choice(['Madeira', 'Pedra', 'Ferro', 'Diamante', 'Aço'])
            return drop
        case 'Goblin':
            drop = random.choice(['Madeira', 'Pedra', 'Ferro', 'Diamante', 'Aço', 'Fio', 'Poção de Vida', 'Poção de Vida Máxima', 'Poção de Força', 'Poção de Resistência'])
            return drop
        case 'Bandido':
            drop = random.choice(['Ferro', 'Diamante', 'Aço'])
            return drop
        case 'Aranha':
            drop = 'Fio'
            return drop
        case 'Vaca':
            drop = 'Bife Cru'
            return drop
        case 'Porco':
            drop = 'Costeleta Crua'
            return drop
        case 'Galinha':
            drop = 'Frango Cru'
            return drop
        case 'Pássaro':
            drop = 'Frango Cru'
            return drop
        case 'Ovelha':
            drop = 'Carneiro Cru'
            return drop
        case 'Veado':
            drop = 'Cervo Cru'
            return drop
        case 'Bruxa':
            drop = random.choice(['Cogumelo', 'Poção de Vida', 'Poção de Vida Máxima', 'Poção de Força', 'Poção de Resistência'])
            return drop
        case 'Gnomo':
            drop = random.choice(['Cogumelo', 'Poção de Vida', 'Poção de Vida Máxima', 'Poção de Força', 'Poção de Resistência'])
            return drop
        case 'Esqueleto':
            drop = random.choice(['Arco', 'Flecha'])
            return drop
        case 'Finn':
            drop = 'Espada do Finn'
            return drop
        case 'Jake':
            drop = 'Armadura do Jake'
            return drop
        case 'Rei do Gelo':
            drop = 'Cajado do Rei do Gelo'
            return drop
        case 'Leviathan':
            drop = random.choice(['LIFE TAKER', 'ARMADURA INQUEBRÁVEL'])
            return drop

menu()
