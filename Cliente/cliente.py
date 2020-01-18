# coding=utf-8

import requests
import json
import sys

header = {
    'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
    'Content-type': 'application/json'
}


def Main():
    while True:
        print("")
        print("Digite 'Control + C' para sair do programa")
        print("")
        PrintMenu()
        escolha = input("Escolha: ")
        if escolha == "1":
            getItems()
        elif escolha == "2":
            nome_item = input("Nome do item a recuperar: ")
            getItem(nome_item)
        elif escolha == "3":
            nome_item = input("Nome do item a enviar: ")
            preco_item = input("Preco do item a enviar: ")
            postItem(nome_item, preco_item)
        elif escolha == "4":
            nome_item = input("Nome do item a deletar: ")
            deleteItem(nome_item)
        elif escolha == "5":
            nome_item = input("Nome do item a alterar/criar: ")
            putItem(nome_item)
        else:
            print("Escolha inválida")
            print("-"*50)


def PrintMenu():
    print("1 - Para obter todos os items")
    print("2 - Para obter um item")
    print("3 - Para cadastrar um item")
    print("4 - Para deletar um item")
    print("6 - Para Atualizar ou cria um item (se nao existir)")


def getItems():
    # print("-"*50)
    print("[+] Para obtendo todos os items...")
    url = 'http://127.0.0.1:5000/items'
    try:
        requisicao = requests.get(url, headers=header)
    except Exception as err:
        print('[-] Erro Na Requisição: ', err)

    requisicao_json = json.dumps(json.loads(requisicao.text), indent=4)
    print("")
    print(requisicao_json)


def getItem(nome_item):
    print("[+] Obtendo item...")
    url = 'http://127.0.0.1:5000/item/'+nome_item
    try:
        requisicao = requests.get(url, headers=header)
    except Exception as err:
        print('[-] Erro Na Requisição: ', err)

    requisicao_json = json.dumps(json.loads(requisicao.text), indent=4)
    print("")
    print(requisicao_json)


def postItem(nome_item, preco_item):
    print("[+] Enviando item...")
    url = 'http://127.0.0.1:5000/item/'+nome_item
    if preco_item:
        data ={"preco" : float(preco_item)}
    else:
        data ={"preco" : 00.00}
    try:
        requisicao = requests.post(url, data=json.dumps(data), headers=header)
    except Exception as err:
        print('[-] Erro Na Requisição: ', err)

    requisicao_json = json.dumps(json.loads(requisicao.text), indent=4)
    print("")
    print(requisicao_json)


def deleteItem(self):
    print("")
    print("[+] Deletando item...")
    pass


def putItem(self):
    print("")
    print("[+] Alterando/criando item...")
    pass


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print('\n[!] Error: Cliente Interrompeu o Programa!')
        sys.exit(1)
