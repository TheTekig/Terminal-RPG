import os
import json
import random 

def save(nomeArquivo,lista):
  with open (nomeArquivo, "w") as arquivo:
    json.dump(lista, arquivo)

def load(nomeArquivo):
  if os.path.exists(nomeArquivo):
    with open(nomeArquivo, "r") as arquivo:
      return json.load(arquivo)
  else:
    return {}

def op_():
  op = int(input("Digito: "))
  while op not in [1,2,3,4,5]:
    op = input("Valor Inválido\nDigito: ")
  return op

def Combate(nome,vJogadores,vInimigos):
  print("\n\t-=-Combate Iniciado-=-")
  jogador = vJogadores[nome]
  inimigo = strgerador_inimigos()
  print("\n\tSeu Inimigo é: ", inimigo['nome'])

  while jogador['Atributos']['vida'] > 0 and inimigo['vida'].copy() > 0:
    print(f"\n\t-=-{jogador['Nome']}-=-")
    print("\n\tVida: ",jogador['Atributos']['vida'])
    print("\tAtaque: ",jogador['Atributos']['ataque'])
    print(f"\n\t-=-Inimigo {inimigo['nome']}-=-")
    print("\n\tVida: ",inimigo['vida'])
    print("\tAtaque: ",inimigo['ataque'])

    Inicio = random.randint(0,1)
    if Inicio == 0:
      print("\n\t-=-Sua Vez-=-")
      print(f"{jogador['Atributos']['vida']}")
      print(f"//O Ataque do jogador vai escalionar com a Skill")
      print("Escolha o seu Ataque:")
      print(f"{jogador['Atributos']['ataque']}")
      print(f"{jogador['Skills']}")
      op = input("Skill: ")
      while op not in jogador['Skills']:
        op = input("Skills Inesistentes\nSkill: ")
      ataque = jogador['Atributos']['ataque'] * jogador['Skills'][op]

      missChance = random.randint(0,100)
      if missChance < 5:
        inimigo['vida'].copy -= ataque * 1.5
        print("Dano :" , ataque * 1.5)
        print(f"\t!DANO CRITICO!\nVida Atual do Inimigo - {inimigo['vida']}")
      elif missChance < 30:
        inimigo['vida'].copy -= ataque
        print("Dano :" , ataque)
        print(f"\t!DANO EM CHEIO!\nVida Atual do Inimigo - {inimigo['vida']}")
      elif missChance < 50:
        inimigo['vida'].copy -= ataque / 2
        print("Dano :" , ataque / 2)
        print(f"\t!DANO RASPAO!\nVida Atual do Inimigo - {inimigo['vida']}")
      elif missChance < 70:
        inimigo['vida'].copy -= ataque / 4
        print("Dano :", ataque / 4)
        print(f"\t!DANO MEDIOCRE!\nVida Atual do Inimigo - {inimigo['vida']}")
      else:
        inimigo['vida'].copy -= 0
        print(f"\t!INIMIGO DESVIOU!\nVida Atual do Inimigo - {inimigo['vida']}")

      

    else:
      print("\n\t-=-Inimigo Vez-=-")
      ataque = inimigo['ataque']
      missChance = random.randint(0,100)
      if missChance < 5:
        jogador['vida'].copy -= ataque * 1.5
        print("Dano :" , ataque * 1.5)
        print(f"\t!DANO CRITICO!\nVida Atual do Inimigo - {jogador['vida']}")
      elif missChance < 30:
        jogador['vida'].copy -= ataque
        print("Dano :" , ataque)
        print(f"\t!DANO EM CHEIO!\nVida Atual do Inimigo - {jogador['vida']}")
      elif missChance < 50:
        jogador['vida'].copy -= ataque / 2
        print("Dano :" , ataque / 2)
        print(f"\t!DANO RASPAO!\nVida Atual do Inimigo - {jogador['vida']}")
      elif missChance < 70:
        jogador['vida'].copy -= ataque / 4
        print("Dano :", ataque / 4)
        print(f"\t!DANO MEDIOCRE!\nVida Atual do Inimigo - {jogador['vida']}")
      else:
        jogador['vida'].copy -= 0
        print(f"\t!INIMIGO DESVIOU!\nVida Atual do Inimigo - {jogador['vida']}")
    
    if jogador['vida'].copy <= 0:
      print("\n\t!VOCE MORREU!")
    
    else:

      print("INIMIGO DERROTADO")
      print(f"Jogador Adquiriu {inimigo['xp']}")
      jogador['xp'] += inimigo['xp']
      jogador['Inimigos'] += 1
      goldmonster = random.randint(0,inimigo['gold'])
      print(f"Jogador Adquiriu {goldmonster}")
      jogador['Gold'] += goldmonster
      print(f"XP Atual: {jogador['xp']}")
      print(f"Gold Atual: {jogador['Gold']}")

    salvar("jogadores.json",vJogadores)
  print("\n\t-=-Combate Finalizado-=-")

def exploracao():
  
  Ambiente = ["Dangeon", "Floresta", "Campos Escuros", "Casa Abandonada"]

  Situacoes = ["Acho Inimigo!" , "Nada Aconteceu" , "Achou um Item", "Caiu em uma Armadilha"]
  resultado = random.choide(Situacoes)
  
  return resultado
def gerador_inimigos(vInimigos):
  num = random.radint(0,len(vInimigos))
  vInimigos[str(num)]:{
      
                  "1" : {"nome" : "Zumbi",        "vida" : 10 , "ataque" : 5, "xp" : 10, "gold" : 0},
                  "2" : {"nome" : "Esqueleto",    "vida" : 15 , "ataque" : 10,"xp" : 10, "gold" : 0},
                  "3" : {"nome" : "Mago Sombrio", "vida" : 20 , "ataque" : 15,"xp" : 10, "gold" : 0},
                  "4" : {"nome" : "Bandido",      "vida" : 25 , "ataque" : 20,"xp" : 10, "gold" : 0},
                  "5" : {"nome" : "Louco",        "vida" : 30 , "ataque" : 25,"xp" : 10, "gold" : 0}

  }
  return vInimigos[str(num)].copy()
def itens():
  vItens = {
      "1" : {"nome" : "Pocao de Cura"   , "Cura"   : 20},
      "2" : {"nome" : "Pocao de Forca"  , "Ataque" : 1.5},
      "3" : {"nome" : "Pocao de Negacao de Dano"},
      "4" : {"nome" : "Bomba"           , "Ataque" : 25},
      "5" : {"nome" : "Arco"            ,  "Ataque": 1.1},
      "6" : {"nome" : "Espada"          , "Ataque" : 1.2},
      "7" : {"nome" : "Escudo"          , "Defesa" : 1.2}
  }
  return vItens
  

def ficha_jogador(vJogadores,nome):
  print("\n\tFicha do Jogador: ")
  print("\tNome: "  ,vJogadores[nome]["Nome"])
  print("\tIdade: " ,vJogadores[nome]["Idade"])
  print("\tGold: "  ,vJogadores[nome]["Gold"])
  print("\txp: "    ,vJogadores[nome]["xp"])
  print("\tLevel: " ,vJogadores[nome]["lvl"])
  print("\tClasse: ",vJogadores[nome]["Classe"])
  print("\tVida: "  ,vJogadores[nome]["Atributos"]["vida"])
  print("\tAtaque: ",vJogadores[nome]["Atributos"]["ataque"])
def porcurar_jogador(vJogadores):
  nome = input("Nome do Jogador: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido\nNome do Jogador: ")
  if nome in vJogadores:
    ficha_jogador(vJogadores,nome)
  else:
    print("\n\t-=- Jogador Não Encontrado -=-\n")
def listar_jogadores():
  print("\n\tLista de Jogadores: ")
  i = 0
  while i < len(vJogadores):
    print(vJogadores[i]["Nome"])
    print(vJogadores[i]["Idade"])
    print(vJogadores[i]["Classe"])
    i = i + 1
def opcoesdeclasse():
  print("\n\tClasse do Jogador: ")
  print("\t1. Guerreiro")
  print("\t2. Mago")
  print("\t3. Assasino")
  print("\t4. Arqueiro")
def cad_player(vJogadores,vClasses,vSkills):
  nome = input("Nome do Jogador: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido\nNome do Jogador:")
  
  idade = input("Idade do Jogador: ")
  while idade.isdigit() != True:
    idade = input("Valor Inválido\nIdade do Jogador: ")

  opcoesdeclasse()
  op = op_()

  if op == 1:

    print("\n\tGuerreiro\n-Possui Mais Vida\n-Ataque mais Equilibrado")
    print("Deseja Escolher essa classe? (S/N)")
    op = input("Digito: ")
    while op.upper() != "S" and op.upper() != "N":
      op = input("Valor Inválido\nDigito: ")
    if op.upper() == "S":
      classe = "Guerreiro"
    else:
      opcoesdeclasse()
      op = op_()

  elif op == 2:
    print("\n\tMago\n-Possui Vida Mediana\n-Aprende mais magias\n-Dano um pouco maior")
    print("Deseja Escolher essa classe? (S/N)")
    op = input("Digito: ")
    while op.upper() != "S" and op.upper() != "N":
      op = input("Valor Inválido\nDigito: ")
    if op.upper() == "S":
      classe = "Mago"
    else:
      opcoesdeclasse()
      op = op_()

  elif op == 3:
    print("\n\tAssasino\n-Vida Baixa\n-Ataque absurdo de alto")
    print("Deseja Escolher essa classe? (S/N)")
    op = input("Digito: ")
    while op.upper() != "S" and op.upper() != "N":
      op = input("Valor Inválido\nDigito: ")
    if op.upper() == "S":
      classe = "Assasino"
    else:
      opcoesdeclasse()
      op = op_()

  else:
    print("\n\tArqueiro\n-Vida Equilibrada\n-Ataque Equilibrado")
    print("Deseja Escolher essa classe? (S/N)")
    op = input("Digito: ")
    while op.upper() != "S" and op.upper() != "N":
      op = input("Valor Inválido\nDigito: ")
    if op.upper() == "S":
      classe = "Arqueiro"
    else:
      opcoesdeclasse()
      op = op_()

  vSkills[classe] = {
      
      "Guerreiro" : {"Slash" : 1.5 , "Porrada" : 1.1 , "Aumentar Defesa" : 1.2},
      "Mago"      : {"Bola de Fogo" : 1.5 , "Cajadada" : 0.9 , "Enfraquecimento" : 5},
      "Assasino"  : {"Corte Profundo" : 1.4  , "Ataque Escondido" : 1.2 , "Ataque baixo" : 1.7},
      "Arqueiro"  : {"Flecha Comum" : 1.1 , "Flecha com efeito" : 1.3, "Flecha Explosiva" : 1.5}    
                     
  }

  vClasse[classe] = {
      
      "Guerreiro" : {"vida" : 20 , "ataque" : 5 },
      "Mago"      : {"vida" : 10 , "ataque" : 15},
      "Assasino"  : {"vida" : 5  , "ataque" : 20},
      "Arqueiro"  : {"vida" : 15 , "ataque" : 10}

  }

  vJogadores[nome] = {
        "Nome" : nome,
        "Idade" : idade,
        "Gold"  : 0,
        "xp"    : 0,
        "lvl"   : 1,
        "Classe" : classe,
        "Skills" : vSkills[classe].copy(),
        "Atributos" : vClasse[classe].copy(),
        "Inimigos" : 0,
        "Itens" : []
  }

  salvar("jogadores.json",vJogadores)
  salvar("classe.json",vClasse)
  salvar("skills.json",vSkills)

  print("\n\t-=- Jogador Cadastrado -=-\n")


def menu():
  print("\n\t-=- Menu -=-")
  print("\t1. Jogar")
  print("\t2. Cadastrar Jogador")
  print("\t3. Listar Jogadores")
  print("\t4. Procurar Jogador")
  print("\t5. Encerrar o Programa")

def main():
  vJogadores = load("jogadores.json")
  vClasse = load("classe.json")
  vInimigos = load("inimigos.json")
  vItens = load("itens.json")
  vAmbiente = load("ambiente.json")
  vSkills = load("skills.json")

  print("\n\t-=-SISTEMA DE RPG-=-")
  menu()
  op = op_()
  while op != 5:

    if op == 1:
      print("\n\t-=- Jogar -=-\n")
      nome = input("Nome do Jogador: ")
      while nome.isalpha() != True or len(nome) < 0 on nome not in vJogadores:
        if nome not in vJogadores:
          print("\n\t-=- Jogador Não Encontrado -=-\n")
          nome = input("Nome do Jogador: ")
        else:
          nome = input("Valor Inválido\nNome do Jogador: ")


    
    if op == 2:
      cad_player()

    if op == 3:
      listar_jogadores()

    if op == 4:
      porcurar_jogador()

    menu()
    op = op_()


main()
