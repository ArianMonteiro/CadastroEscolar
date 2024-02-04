import mysql.connector
from random import randint
import datetime

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="base_escolar")
mycursor = mydb.cursor()

mensal = [500, 750, 1000, 1250, 1500]
dados_alunos = []

def renda():
    # verifica a renda per capita
    qtd = int(dados_alunos[18])
    recebimentos = float(dados_alunos[16]) + float(dados_alunos[17])
    percapita = recebimentos / int(qtd)
    return percapita

def bolsa():
    # verifica possibilidade de bolsa de acordo com a renda per capita
    valor = renda()
    pgto = valor_mensalidade()
    if 0 < valor <= 1000:
        mensalidade = pgto * 0.8
    elif 1000 < valor <= 2000:
        mensalidade = pgto * 0.5
    elif 2000 < valor <= 3000 * 3:
        mensalidade = pgto * 0.3
    else:
        mensalidade = pgto
    return mensalidade

def serie():
    # Verifica série solicitada e mensalidade do setor
    match dados_alunos[1]:
        case 1:
            total = str(f'Pré escola')
        case 2:
            total = str(f'Maternal')
        case 3:
            total = str(f'Fundamental I')
        case 4:
            total = str(f'Fundamental II')
        case 5:
            total = str(f'Ensino Médio')
    return total

def valor_mensalidade():
    match dados_alunos[1]:
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
    dados_alunos.append(matricula)
    dados_alunos.append(escolaridade)
    dados_alunos.append(serie())
    for c in range(0, 5):
        dados_alunos.append(inicio[c])
        dados_alunos.append(resp1[c])
        dados_alunos.append(resp2[c])

    dados_alunos.append(outros)
    dados_alunos.append(renda())
    dados_alunos.append((bolsa()))
    dados_alunos.append(datetime.date.today())

    sql = f"INSERT INTO alunos(matricula, nome, idade, email, cpf_aluno, cod_escol, escolaridade, renda_capta, mensalidade, resp1, cpf_resp1, resp2, cpf_resp2, data_matricula) VALUES ({dados_alunos[0]},'{dados_alunos[3]}',{dados_alunos[6]},'{dados_alunos[15]}',{dados_alunos[9]},'{dados_alunos[1]}', '{dados_alunos[2]}', {dados_alunos[19]}, {dados_alunos[20]}, '{dados_alunos[4]}','{dados_alunos[10]}','{dados_alunos[5]}','{dados_alunos[11]}','{dados_alunos[21]}')"
    mycursor.execute(sql)
    mydb.commit()
    dados_alunos.clear()

def novo():
    sist = str.upper(input('Deseja iniciar o arquivo?\nS- Sim\nN- Não\nResposta: '))
    return sist


def altera_dados():
    nun_matricula = input('Insira a matrícula do aluno: ')
    campo_alterado = input('Qual campo será atualizado? ')
    novoValor = input('Insira a nova informação: ')

    sql = f"UPDATE alunos SET {campo_alterado} = '{novoValor}' WHERE matricula = '{nun_matricula}'"
    mycursor.execute(sql)
    mydb.commit()

def pesquisa_dados():
    opcao = input('O que deseja pesquisar?\n1- Todos os alunos\n2- Alunos matriculados por data\n3- Buscar aluno específico\n Opção: ')
    match opcao:
        case '1':
            sql = "SELECT * FROM alunos"
        case '2':
            data_filtro = input('Insira a data a ser filtrada: ')
            sql = f"SELECT * FROM alunos WHERE data_matricula LIKE '%{data_filtro}%'"
        case '3':
            nun_matricula = input('Insira a matrícula do aluno: ')
            sql = f"SELECT * FROM alunos WHERE matricula LIKE {nun_matricula}"
        case _:
            print("Selecione uma das opções acima!")

    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    for x in resultado:
        print(x)

def deleta_alunos():
    num_matricula = input('Insira a matrícula do aluno: ')
    sql = f"DELETE FROM alunos WHERE matricula LIKE '%{num_matricula}%'"
    mycursor.execute(sql)
    mydb.commit()

while novo() == "S":
    menu = input('Bem-vindo! O que deseja fazer?\n1- Matricular aluno\n2- Atualizar dados cadastrais\n3- Pesquisar dados\n4- Deletar registro\n5- Sair do programa\nOpção: ')
    match menu:
        case '1':
            cadastro()
        case '2':
            altera_dados()
        case '3':
            pesquisa_dados()
        case '4':
            deleta_alunos()
        case '5':
            print('Até a próxima!')
        case _:
            print('Selecione uma das opções acima!')