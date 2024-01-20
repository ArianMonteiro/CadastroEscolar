from random import randint

sal_min = 1412.00
mensal = [250, 350, 500, 650, 800]
basico = []
dados1 = []
dados2 = []

def renda():
    #verifica a renda per capita
    recebimentos = float(dados1[4]) + float(dados2[4])
    percapita = recebimentos / int(outros)
    return percapita

def bolsa():
    #verifica possibilidade de bolsa de acordo com a renda per capita
    valor = renda()
    pgto = valor_mensalidade()
    if 0 < valor <= sal_min:
        mensalidade = 0
    elif sal_min < valor <= sal_min * 2:
        mensalidade = pgto * 0.5
    elif sal_min * 2 < valor <= sal_min * 3:
        mensalidade = pgto * 0.3
    else:
        mensalidade = pgto
    return mensalidade

def serie():
    #Verifica série solicitada e mensalidade do setor
    match escolaridade:
        case 1:
            total = str(f'Pré escola: R$ {mensal[0]:.2f}')
        case 2:
            total = str(f'Maternal: R$ {mensal[1]:.2f}')
        case 3:
            total = str(f'Fundamental I: R$ {mensal[2]:.2f}')
        case 4:
            total = str(f'Fundamental II: R$ {mensal[3]:.2f}')
        case 5:
            total = str(f'Ensino Médio: R$ {mensal[4]:.2f}')
    return total

def valor_mensalidade():
    match escolaridade:
        case 1:
            total = mensal[0]
        case 2:
            total = mensal[1]
        case 3:
            total = mensal[2]
        case 4:
            total = mensal[3]
        case 5:
            total = mensal[4]
    return total    

def ver_alfabet():
    #Verifica progresso escolar com base na idade
    idade = int(basico[1])
    if 0 < idade <= 3 and escolaridade == 1:
        tempo = str('Certo')
    elif 3 < idade <= 6 and escolaridade == 2:
        tempo = str('Certo')
    elif 6 < idade <= 10 and escolaridade == 3:
        tempo = str('Certo')
    elif 10 < idade <= 15 and escolaridade == 4:
        tempo = str('Certo')
    elif 15 < idade <= 18 and escolaridade == 5:
        tempo = str('Certo')
    else:
        tempo = str('Atenção a idade!')
    return tempo

#entrada de dados
inicio = input('Dados iniciais:\nNome completo, Idade, CPF, data de nascimento, e-mail.\nDados: ').split(',')
resp1 = input('Responsável 1:\nNome, idade, CPF, Profissão, Renda.\nDados: ').split(',')
resp2 = input('Responsável 2:\nNome, idade, CPF, Profissão, Renda.\nDados: ').split(',')
outros = input('Dados Adicionais:\nTotal de moradores na casa: ')
escolaridade = int(input('Escolaridade:\n1- Pré-Escola\n2- Maternal\n3- Fundamental I\n4- Fundamental II\n5- Ensino médio\nResposta: '))
matricula = randint(0, 1500)

#insere os dados na em suas respectivas listas
for c in range(0,5): 
    basico.append(inicio[c])
    dados1.append(resp1[c])
    dados2.append(resp2[c])

print(f'Aluno: {basico[0]}\nIdade: {basico[1]}\nProgresso escolar: {ver_alfabet()}\nRenda per capita: {renda():.2f}\nMensalidade padrão: {serie()}\nMensalidade com bolsa: {bolsa()}\nMatrícula: {matricula}')