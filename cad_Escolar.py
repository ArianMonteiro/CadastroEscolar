import mysql.connector
from random import randint

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="base_escolar")
mycursor = mydb.cursor()

sal_min = 1412.00
mensal = [250, 350, 500, 650, 800]
basico = []
dados1 = []
dados2 = []
mais = []
base_alunos = []

def renda():
    # verifica a renda per capita
    qtd = int(mais[0])
    recebimentos = float(dados1[4]) + float(dados2[4])
    percapita = recebimentos / int(qtd)
    return percapita

def bolsa():
    # verifica possibilidade de bolsa de acordo com a renda per capita
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
    # Verifica série solicitada e mensalidade do setor
    match mais[1]:
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
    match mais[1]:
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
    # Verifica progresso escolar com base na idade
    idade = int(basico[1])
    esc = int(mais[1])
    if 0 < idade <= 3 and esc == 1:
        tempo = str('Certo')
    elif 3 < idade <= 6 and esc == 2:
        tempo = str('Certo')
    elif 6 < idade <= 10 and esc == 3:
        tempo = str('Certo')
    elif 10 < idade <= 15 and esc == 4:
        tempo = str('Certo')
    elif 15 < idade <= 18 and esc == 5:
        tempo = str('Certo')
    else:
        tempo = str('Atenção a idade!')
    return tempo

# entrada de dados
def cadastro():
    inicio = input('Dados iniciais:\nNome completo, Idade, CPF, data de nascimento, e-mail.\nDados: ').split(',')
    resp1 = input('Responsável 1:\nNome, idade, CPF, Profissão, Renda.\nDados: ').split(',')
    resp2 = input('Responsável 2:\nNome, idade, CPF, Profissão, Renda.\nDados: ').split(',')
    outros = input('Dados Adicionais:\nTotal de moradores na casa: ')
    escolaridade = int(input(
        'Escolaridade:\n1- Pré-Escola\n2- Maternal\n3- Fundamental I\n4- Fundamental II\n5- Ensino médio\nResposta: '))
    matricula = randint(0, 1500)

    # insere os dados na em suas respectivas listas
    base_alunos.append(matricula)
    base_alunos.append(escolaridade)
    for c in range(0, 5):
        basico.append(inicio[c])
        dados1.append(resp1[c])
        dados2.append(resp2[c])
        base_alunos.append(inicio[c])
        base_alunos.append(resp1[c])
        base_alunos.append(resp2[c])

    mais.append(outros)
    mais.append(escolaridade)
    mais.append(matricula)
    base_alunos.append(outros)
    base_alunos.append(renda())
    base_alunos.append((bolsa()))

def novo():
    cad_aluno = int(input('Deseja matricular um novo aluno?\n1- Sim\n2- Não\nResposta: '))
    return cad_aluno

while novo() == 1:
    cadastro()
    sql = f"INSERT INTO alunos(matricula, nome, idade, email, renda_familiar, cpf, escolaridade, renda_capta, mensalidade, resp1, resp2) VALUES ({base_alunos[0]},'{base_alunos[2]}',{base_alunos[5]},'{base_alunos[14]}',{base_alunos[18]},'{base_alunos[8]}', '{base_alunos[1]}', {base_alunos[18]}, {base_alunos[19]}, '{base_alunos[3]}','{base_alunos[4]}')"
    mycursor.execute(sql)
    mydb.commit()

print(base_alunos)

