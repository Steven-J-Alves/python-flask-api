# coding=utf-8

import requests
import json
import sys

url = 'http://127.0.0.1:5000/item/porta'
header = {
    'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
    'Content-type': 'application/json'
}

try:
    requisicao = requests.get(url, headers=header)
except Exception as err:
    print('requisicao deu erro: ', err)

requisicao_json = json.dumps(json.loads(requisicao.text), indent=4)
print(requisicao_json)


def Main():
    while True:
        print("Digite 'Control + C' para sair do programa")
        PrintMenu()
        escolha = input("Escolha: ")
        if escolha == "1":
            getItems()
            break
        elif escolha == "2":
            getItem()
            break
        elif escolha == "3":
            postItem()
            break
        elif escolha == "4":
            deleteItem()
            break
        elif escolha == "5":
            putItem()
            break
        else:
            print("Escolha inválida")


def PrintMenu():
    print("1 - Para obter todos os items")
    print("2 - Para obter um item")
    print("3 - Para cadastrar um item")
    print("4 - Para deletar um item")
    print("6 - Para Atualizar ou cria um item (se nao existir)")


def requisicao():
    pass


def getItems():
    pass


def getItem():
    pass


def postItem():
    pass


def deleteItem():
    pass


def putItem():
    pass


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print('\n[!] Error: Cliente Interrompeu o Programa!')
        sys.exit(1)
