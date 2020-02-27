import sqlite3
import getpass
MASTER_PASSWORD = "123456"

senha = input("Insira uma senha master: ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("****GERENCIADOR DE SENHAS*****")
    print("******************************")
    print("* i : inserir nova senha     *")
    print("* l : listar serviços salvos *")
    print("* r : recuperar uma senha    *")
    print("* s : sair                   *")
    print("******************************")

def get_pasword(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use '1' para verificar os serviços)")
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
''')
    conn.commit()

def show_passwords():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("O que deseja fazer?\n ")
    if op not in ['l', 'i', 'r', 's']:
        print("Opção Inválida")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input("Informe o nome do serviço:\n ")
        username = input("Informe o nome de usuário para o serviço: " + service + "\n")
        password = input("Digite a senha do usuário: " + username + "\n")
        insert_password(service, username, password)

    if op == 'l':
        show_passwords()

    if op == 'r':
        service = input("Qual o serviço para o qual quer a senha? ")
        get_pasword(service)

conn.close()

