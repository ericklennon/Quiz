while True:

    from os import system, name
    from time import sleep


    def clear():


        if name == 'nt':
            _ = system('cls')

    print(f''' ______       __    __   __   ________     .___  ___.      ___      .__   __.  __       _______ .___________.
     /  __  \     |  |  |  | |  | |       /     |   \/   |     /   \     |  \ |  | |  |     |   ____||           |
    |  |  |  |    |  |  |  | |  | `---/  /      |  \  /  |    /  ^  \    |   \|  | |  |     |  |__   `---|  |----`
    |  |  |  |    |  |  |  | |  |    /  /       |  |\/|  |   /  /_\  \   |  . `  | |  |     |   __|      |  |     
    |  `--'  '--. |  `--'  | |  |   /  /----.   |  |  |  |  /  _____  \  |  |\   | |  `----.|  |____     |  |     
     \_____\_____\ \______/  |__|  /________|   |__|  |__| /__/     \__\ |__| \__| |_______||_______|    |__|     ''')

    print()
    print('Não se esqueça de responder as perguntas com: "a", "b", "c" ou "d"')
    perguntas = {
        'Pergunta 1': {
             'pergunta': 'Quanto é 2 + 2? ',
             'respostas': {'a': '0', 'b': '4', 'c': '5', 'd': '7'},
             'resposta_certa': 'b',
        },
        'Pergunta 2': {
            'pergunta': 'Qual é a capital da Suíça? ',
            'respostas': {'a': 'Zurich', 'b': 'Amsterdã', 'c': 'Berna', 'd': 'Roma'},
            'resposta_certa': 'c',
        },
        'Pergunta 3': {
            'pergunta': 'De onde é a invenção do chuveiro elétrico? ',
            'respostas': {'a': 'França', 'b': 'Inglaterra', 'c': 'Brasil', 'd': 'Itália'},
            'resposta_certa': 'c',
        },
        'Pergunta 4': {
            'pergunta': 'Qual é o menor e o maior país do mundo? ',
            'respostas': {'a': 'Vaticano e Rússia', 'b': 'Nauru e China', 'c': 'Mônaco e Canadá', 'd': 'Malta e Estados Unidos'},
            'resposta_certa': 'a',
        },
        'Pergunta 5': {
            'pergunta': 'Qual o nome do presidente do Brasil que ficou conhecido como Jango? ',
            'respostas': {'a': 'Jânio Quadros', 'b': 'Getúlio Vargas', 'c': 'João Goulart',
                          'd': 'João Figueiredo'},
            'resposta_certa': 'c',
        },
        'Pergunta 6': {
            'pergunta': 'Qual o livro mais vendido no mundo a seguir à Bíblia? ',
            'respostas': {'a': 'O Senhor dos Anéis', 'b': 'Dom Quixote', 'c': 'O Pequeno Príncipe',
                          'd': 'Ela, a Feiticeira'},
            'resposta_certa': 'b',
        },
        'Pergunta 7': {
            'pergunta': 'Quantas casas decimais tem o número pi? ',
            'respostas': {'a': 'Duas', 'b': 'Centenas', 'c': 'Milhares',
                          'd': 'Infinitas'},
            'resposta_certa': 'd',
        },
        'Pergunta 8': {
            'pergunta': 'Atualmente, quantos elementos químicos a tabela periódica possui? ',
            'respostas': {'a': '118', 'b': '113', 'c': '108',
                          'd': '92'},
            'resposta_certa': 'a',
        },
        'Pergunta 9': {
            'pergunta': 'Quais os países que têm a maior e a menor expectativa de vida do mundo? ',
            'respostas': {'a': 'Itália e Chade', 'b': 'Japão e Serra Leoa', 'c': ' Brasil e Congo',
                          'd': 'Estados Unidos e Angola'},
            'resposta_certa': 'b',
        },
        'Pergunta 10': {
            'pergunta': 'Quanto tempo a luz do Sol demora para chegar à Terra? ',
            'respostas': {'a': '12 minutos', 'b': ' 8 minutos', 'c': '12 horas',
                          'd': '1 dia'},
            'resposta_certa': 'b',
        },

    }
    print()

    respostas_certas = 0

    for pk, pv in perguntas.items():
        print(f'{pk}: {pv["pergunta"]}')
        print()

        print('Opções: ')
        for rk, rv in pv['respostas'].items():
            print(f'[{rk}]: {rv}')

        respostas_usuario = input('Qual a alternativa certa? ')

        if respostas_usuario != 'a' and respostas_usuario != 'b' and respostas_usuario != 'c' and respostas_usuario != 'd':
            print('Resposta inválida! Utilize as alternativas corretas (a, b, c ou d).')
            resposta_invalida = input('Insira uma alternativa válida: ')






        resposta_invalida = ''
        if respostas_usuario == pv['resposta_certa'] or resposta_invalida == pv['resposta_certa']:
            print('Resposta CERTA!!!')
            respostas_certas += 1
        else:
            print('Respostas ERRADA!!! =( ')


        print()

    quantidade_p = len(perguntas)
    assertividade = respostas_certas / quantidade_p * 100

    if assertividade == 100:
        print(f'Você acertou {assertividade}%. Você é um verdadeiro GÊNIO MANLET!!!')

    elif assertividade < 100 and assertividade >= 80:
        print(f'Você acertou {assertividade}%. Você foi muito bem!! Já está no caminho para se tornar um incrível MANLET!!')

    elif assertividade < 80 and assertividade >= 60:
        print(f'Você acertou {assertividade}%. Nada mal, mas ainda está longe de se tornar um MANLET!')

    elif assertividade < 60 and assertividade >= 40:
        print(f'Você acertou {assertividade}%. Você foi muito mal, assim nunca vai ser um GÊNIO MANLET!')

    elif assertividade == 0:
        print('Você foi tão mal que não teve nem porcentagem de acerto.')

    reiniciar = input('Deseja iniciar novamente o Quiz Manlet? [s]im ou [n]ão: ')

    if reiniciar == reiniciar == 's' or reiniciar == 'S' or reiniciar == 'sim' or reiniciar == 'Sim' or reiniciar == 'SIM':
        continue
    else:
        print('''.______   ____    ____        __  ___  __    __  .______      .___________. ________  
|   _  \  \   \  /   /  _    |  |/  / |  |  |  | |   _  \     |           ||       /  
|  |_)  |  \   \/   /  (_)   |  '  /  |  |  |  | |  |_)  |    `---|  |----``---/  /   
|   _  <    \_    _/         |    <   |  |  |  | |      /         |  |        /  /    
|  |_)  |     |  |      _    |  .  \  |  `--'  | |  |\  \----.    |  |       /  /----.
|______/      |__|     (_)   |__|\__\  \______/  | _| `._____|    |__|      /________|''')
        sleep(2)
        clear()
        break








