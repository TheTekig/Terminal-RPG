import os
import json
import random
import time

#region SAVE/LOAD

def save(nomeArquivo,lista):
  with open (nomeArquivo, "w") as arquivo:
    json.dump(lista, arquivo,indent=5)

def load(nomeArquivo):
  if os.path.exists(nomeArquivo):
    with open(nomeArquivo, "r") as arquivo:
      return json.load(arquivo)
  else:
    print("Arquivo nao encontrado")
    return {}

#endregion


def Combate(nome,vJogadores,vInimigos):
  print("\n\t-=-Combate Iniciado-=-")
  jogador = vJogadores[nome]                                              #Declaracao de jogador e inimigo para encurtar chave para chamada de atributos
  inimigo = gerador_inimigos(vInimigos)
  print("\n\tSeu Inimigo é: ", inimigo['nome'])

  while jogador['Atributos']['vida'] > 0 and inimigo['vida'] > 0:
                                                                          #Status do Inimigo e do Jogador
    print(f"\n\t-=-{jogador['Nome']}-=-")
    print("\n\tVida: ",jogador['Atributos']['vida'])
    print("\tAtaque: ",jogador['Atributos']['ataque'])
    print(f"\n\t-=-Inimigo {inimigo['nome']}-=-")
    print("\n\tVida: ",inimigo['vida'])
    print("\tAtaque: ",inimigo['ataque'])

    time.sleep(0.5)

    Inicio = random.randint(0,1)                                           #Numero Random para decidir quem sera o atacante

    time.sleep(0.5)

    if Inicio == 0:
      print("\n\t-=-Sua Vez-=-")
      print("-" * 50)
      print(f"//O Ataque do jogador vai escalionar com a Skill")
      print("-" * 50)
      print("\tA - ATTACK / I - ITENS")
      print("-" * 50)
      
      op = input("--->")
      while op.upper() not in ["I","A"]:
        op = input("Valor Invalido \n---> ")
        
      if op.upper() == "A":
        print("Escolha o seu Ataque:")
        print(f"{jogador['Skills']}")

        op = input("Skill: ")
        while op not in jogador['Skills']:
          op = input("Skills Inesistentes\nSkill: ")

        #region Aleatoridade/DanoJogador
  
        ataque = jogador['Atributos']['ataque'] * jogador['Skills'][op]         #Escalabilidade do ataque
        missChance = random.randint(0,100)                                      #Gera o numero que sera usado de parametro para definir acertividade do ataque
        time.sleep(0.5)
        if missChance < 5:
          inimigo['vida'] -= ataque * 1.5
          print("Dano :" , ataque * 1.5)
          print(f"\t!DANO CRITICO!\nVida Atual do Inimigo - {inimigo['vida']}")
        elif missChance < 30:
          inimigo['vida'] -= ataque
          print("Dano :" , ataque)
          print(f"\t!DANO EM CHEIO!\nVida Atual do Inimigo - {inimigo['vida']}")
        elif missChance < 50:
          inimigo['vida'] -= ataque / 2
          print("Dano :" , ataque / 2)
          print(f"\t!DANO RASPAO!\nVida Atual do Inimigo - {inimigo['vida']}")
        elif missChance < 70:
          inimigo['vida'] -= ataque / 4
          print("Dano :", ataque / 4)
          print(f"\t!DANO MEDIOCRE!\nVida Atual do Inimigo - {inimigo['vida']}")
        else:
          inimigo['vida'] -= 0
          print(f"\t!INIMIGO DESVIOU!\nVida Atual do Inimigo - {inimigo['vida']}")
          
          
          #endregion
      else:
        print("-" * 50)
        print(f"{jogador['Itens']}")
        print("Escolha seu Item (ou digite 0 para cancelar):")

        item_nome = input("---> ")

        if item_nome == "0":
            acao = Game_Inputs()
        else:
            item_encontrado = None
            for i in jogador['Itens']:
                if i['nome'] == item_nome:
                    item_encontrado = i
                    break

            if item_encontrado:
                if 'Cura' in item_encontrado:
                    jogador['Atributos']['vida'] += item_encontrado['Cura']
                    print(f"Você recuperou {item_encontrado['Cura']} de vida!")
                
                elif 'Ataque' in item_encontrado:
                    jogador['Atributos']['ataque'] *= item_encontrado['Ataque']
                    print(f"Ataque multiplicado por {item_encontrado['Ataque']}!")
                
                # Pode adicionar mais efeitos aqui se necessário

                jogador['Itens'].remove(item_encontrado)
                print("Item consumido!")
            else:
                print("Item não encontrado.")
    else:
      print("\n\t-=-Inimigo Vez-=-")

      print("-" * 50)

      #region Aleatoridade/DanoInimigo
      ataque = inimigo['ataque']
      missChance = random.randint(0,100)


      if missChance < 5:
        jogador['Atributos']['vida'] -= ataque * 1.5
        print("Dano :" , ataque * 1.5)
        print(f"\t!DANO CRITICO!\nVida Atual do Jogador - {jogador['vida']}")
      elif missChance < 30:
        jogador['Atributos']['vida'] -= ataque
        print("Dano :" , ataque)
        print(f"\t!DANO EM CHEIO!\nVida Atual do Jogador - {jogador['Atributos']['vida']}")
      elif missChance < 50:
        jogador['Atributos']['vida'] -= ataque / 2
        print("Dano :" , ataque / 2)
        print(f"\t!DANO RASPAO!\nVida Atual do Jogador - {jogador['Atributos']['vida']}")
      elif missChance < 70:
        jogador['Atributos']['vida'] -= ataque / 4
        print("Dano :", ataque / 4)
        print(f"\t!DANO MEDIOCRE!\nVida Atual do Jogador - {jogador['Atributos']['vida']}")
      else:
        jogador['Atributos']['vida'] -= 0
        print(f"\t!JOGADOR DESVIOU!\nVida Atual do Jogador - {jogador['Atributos']['vida']}")

      #endregion

      print("-" * 50)
    
  if jogador['Atributos']['vida'] <= 0:                                 #Morte do Jogador Caso sua vida seja meno igual a 0
    print("\n\t!VOCE MORREU!")
    
  else:

    print("INIMIGO DERROTADO")

#################Recompensas########################
    jogador['xp'] += inimigo['xp']
    jogador['Inimigos'] += 1
    goldmonster = random.randint(0,inimigo['gold'])
    jogador['Gold'] += goldmonster
###################################################

    print(f"Jogador Adquiriu {inimigo['xp']}")
    print(f"Jogador Adquiriu {goldmonster}")
    print(f"XP Atual: {jogador['xp']}")
    print(f"Gold Atual: {jogador['Gold']}")

    Level_up(vJogadores,nome)

  save("jogadores.json",vJogadores)

  print("\n\t-=-Combate Finalizado-=-")

def Level_up(vJogadores,nome):                                           #Sistema de LevelUp

  jogador = vJogadores[nome]
  XPnextLevel = jogador['lvl'] * 10
  if jogador['xp'] >= XPnextLevel:
    jogador['lvl'] += 1
    jogador['Atributos']['vida'] *= 1.2                                    #Multiplicador de atributos do jogador por nivel subido (obs: Provavelmente vou alterar para que o nivel de xp necessario escale com o nvl subido)
    jogador['Atributos']['ataque'] *= 1.2
    print("-" * 50)
    print(f"Jogador{jogador['Nome']} subiu para o nivel{jogador['lvl']}")
    print(f"Novos atributos = Vida:{jogador['Atributos']['vida']} / Ataque:{jogador['Atributos']['ataque']}")
    print("-" * 50)
  save("jogadores.json",vJogadores)


def Game_Inputs():                                                       #Em geral alguns inputs

  print("-" * 50)
  print("\tM - MOVE / S - STATUS / I - ITENS")
  print("-" * 50)
  op = input("--->")
  while op.upper() not in ["M","S","I","0"]:
    op = input("Invalido\n--->")
  
  return op.upper() 

def exploracao():
  
  Ambiente = ["Dangeon", "Floresta", "Campos Escuros", "Casa Abandonada"]                               #Sistema Futuro//

  Situacoes = ["Acho Inimigo!" , "Nada Aconteceu" , "Achou um Item", "Caiu em uma Armadilha"]           #Todas as possiveis situacoes que o jogador pode acabar entrando
  resultado = random.choice(Situacoes)                                                                  #Escolhe uma situacao da lista de situacoes elaborada acima
  
  return resultado

def controlador(vJogadores,nome,arm,vItens,vInimigos):                   #Controlador chama todas as funcoes de acoes dependendo da escolha do jogador
  acao = Game_Inputs()

  while acao != "0":

    if acao == "M":
      situacao = exploracao()

      if situacao == "Acho Inimigo!":                                       #Inicia a funcao de combate do jogador
        print("INIMIGO AVISTADO!")
        Combate(nome,vJogadores,vInimigos)
        acao = Game_Inputs()

      elif situacao == "Nada Aconteceu":
        print("NADA OCORREU!")
        acao = Game_Inputs()

      elif situacao == "Caiu em uma Armadilha":
        print("Voce caiu em uma armadilha mas escapou!")
        arm += 1                            

        if arm == random.randint(3,10):                                     #Impede que toda vez que o jogador caia em uma armadilha ele se machuque
          print("Voce caiu em uma armadilha e se machucou!")
          vJogadores[nome]['Atributos']['vida'] -= random.randint(1,10)     #Aleatoridade do dano que o jogador ira tomar caso caia na armadilha
          arm = 0
        acao = Game_Inputs()

      else:
        item = gerador_itens(vItens)                                        #Adicao de itens a um "Inventario" do jogador
        vJogadores[nome]['Itens'].append(item)
        print(f"Voce achou um - {item}")
        save("jogadores.json",vJogadores)
        acao = Game_Inputs()
        
    if acao == "S":                                                        #Mostra o Status do jogador
      print("\n\t-=-STATUS-=-")
      ficha_jogador(vJogadores,nome)
      acao = Game_Inputs()

    if acao == "I":
      jogador = vJogadores[nome]
      print("-" * 50)
      print(f"{jogador['Itens']}")
      print("Escolha seu Item (ou digite 0 para cancelar):")

      item_nome = input("---> ")

      if item_nome == "0":
          acao = Game_Inputs()
      else:
          item_encontrado = None
          for i in jogador['Itens']:
              if i['nome'] == item_nome:
                  item_encontrado = i
                  break

          if item_encontrado:
              if 'Cura' in item_encontrado:
                  jogador['Atributos']['vida'] += item_encontrado['Cura']
                  print(f"Você recuperou {item_encontrado['Cura']} de vida!")
              
              elif 'Ataque' in item_encontrado:
                  jogador['Atributos']['ataque'] *= item_encontrado['Ataque']
                  print(f"Ataque multiplicado por {item_encontrado['Ataque']}!")
              
              # Pode adicionar mais efeitos aqui se necessário

              jogador['Itens'].remove(item_encontrado)
              print("Item consumido!")
          else:
              print("Item não encontrado.")

    save("jogadores.json",vJogadores)    
  print("Saindo...")

def gerador_inimigos(vInimigos):                                          #Escolhe um Inimigo do Dicionario de Inimigos
  num = random.randint(1,len(vInimigos))        
  return vInimigos[str(num)].copy()                 #faz uma copia do inimigo para nao alterar a variavel principal do inimigo

def gerador_itens(vItens):                                                #Escolhe um Item da lista de Itens do jogo
  num = random.randint(1,len(vItens))
  return vItens[str(num)]

def Listas_Dicionarios():                                                 #Listas de Dicionarios com os principais elementos 
    vInimigos = {
      
      "1" : {"nome" : "Zumbi",        "vida" : 10 , "ataque" : 5, "xp" : 10, "gold" : 4},
      "2" : {"nome" : "Esqueleto",    "vida" : 15 , "ataque" : 10,"xp" : 10, "gold" : 6},
      "3" : {"nome" : "Mago Sombrio", "vida" : 20 , "ataque" : 15,"xp" : 10, "gold" : 2},
      "4" : {"nome" : "Bandido",      "vida" : 25 , "ataque" : 20,"xp" : 10, "gold" : 8},
      "5" : {"nome" : "Louco",        "vida" : 30 , "ataque" : 25,"xp" : 10, "gold" : 10}
    }

    vItens = {
      "1" : {"nome" : "Pocao de Cura"   , "Cura"   : 20},
      "2" : {"nome" : "Pocao de Forca"  , "Ataque" : 1.5},
      "3" : {"nome" : "Pocao de Negacao de Dano"},
      "4" : {"nome" : "Bomba"           , "Ataque" : 25},
      "5" : {"nome" : "Arco"            ,  "Ataque": 1.1},
      "6" : {"nome" : "Espada"          , "Ataque" : 1.2},
      "7" : {"nome" : "Escudo"          , "Defesa" : 1.2}
    }

    vSkills = {
      
      "Guerreiro" : {"Slash" : 1.5 , "Porrada" : 1.1 , "Aumentar Defesa" : 1.2},
      "Mago"      : {"Bola de Fogo" : 1.5 , "Cajadada" : 0.9 , "Enfraquecimento" : 5},
      "Assassino"  : {"Corte Profundo" : 1.4  , "Ataque Escondido" : 1.2 , "Ataque baixo" : 1.7},
      "Arqueiro"  : {"Flecha Comum" : 1.1 , "Flecha com efeito" : 1.3, "Flecha Explosiva" : 1.5}    
                     
    }

    vClasse = {
      
      "Guerreiro" : {"vida" : 20 , "ataque" : 5 },
      "Mago"      : {"vida" : 10 , "ataque" : 15},
      "Assassino"  : {"vida" : 5  , "ataque" : 20},
      "Arqueiro"  : {"vida" : 15 , "ataque" : 10}

    }
    
    save("classe.json",vClasse)
    save("inimigos.json",vInimigos)
    save("itens.json",vItens)
    save("skills.json",vSkills)

#region CADASTRO/FUNCOES DE MENU

def ficha_jogador(vJogadores,nome):                                       #Ficha Simples com todos os Status

  print("-" * 40)
  print("\tNome: "  ,vJogadores[nome]["Nome"])
  print("\tIdade: " ,vJogadores[nome]["Idade"])
  print("\tGold: "  ,vJogadores[nome]["Gold"])
  print("\txp: "    ,vJogadores[nome]["xp"])
  print("\tLevel: " ,vJogadores[nome]["lvl"])
  print("\tClasse: ",vJogadores[nome]["Classe"])
  print("\tVida: "  ,vJogadores[nome]["Atributos"]["vida"])
  print("\tAtaque: ",vJogadores[nome]["Atributos"]["ataque"])
  print("-" * 40)

def porcurar_jogador(vJogadores):                                         #Funcao de Procurar Jogador (obs: Posso implementar isso melhor para reutilizar em outros locais)
  nome = input("Nome do Jogador: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido\nNome do Jogador: ")
  if nome in vJogadores:
    ficha_jogador(vJogadores,nome)
  else:
    print("\n\t-=- Jogador Não Encontrado -=-\n")

def listar_jogadores(vJogadores):                                         #Listagem com nome/idade/clasee de cada jogador
  print("\n\t-=-Lista de Jogadores-=-\n ")
  print("-" * 20)
  for nome,dado in vJogadores.items():
    print(f"Nome:  {dado['Nome']}")
    print(f"Idade: {dado['Idade']}")
    print(f"Classe: {dado['Classe']}")
    print("-" * 20)

def opcoesdeclasse():
  print("\n\tClasse do Jogador: ")
  print("\t1. Guerreiro")
  print("\t2. Mago")
  print("\t3. Assassino")
  print("\t4. Arqueiro")

def cad_player(vJogadores,vClasse,vSkills):                               #Cadastro Player
  #region Nome/Idade

  nome = input("Nome do Jogador: ")
  while nome.isalpha() != True or len(nome) == 0:
    nome = input("Valor Inválido\nNome do Jogador:")
  
  idade = input("Idade do Jogador: ")
  while idade.isdigit() != True:
    idade = input("Valor Inválido\nIdade do Jogador: ")

  #endregion
          
  while True:       #Mostra cada tipo de Classe
     
      opcoesdeclasse()
      op = op_()

      if op == 1:
          classe = "Guerreiro"
          descricao = "-Possui Mais Vida\n-Ataque Equilibrado"
      elif op == 2:
          classe = "Mago"
          descricao = "-Vida Mediana\n-Aprende magias\n-Dano um pouco maior"
      elif op == 3:
          classe = "Assassino"
          descricao = "-Vida Baixa\n-Ataque Muito Alto"
      elif op == 4:
          classe = "Arqueiro"
          descricao = "-Vida e Ataque Equilibrados"

      print(f"\n\t{classe}\n{descricao}")
      confirmacao = input("Deseja Escolher essa classe? (S/N): ").upper()
      while confirmacao not in ["S", "N"]:
          confirmacao = input("Valor Inválido\nDeseja Escolher essa classe? (S/N): ").upper()

      if confirmacao == "S":
          break

################################################      
            #Dicionario Principal#
################################################
  
  vJogadores[nome] = {
        "Nome" : nome,
        "Idade" : idade,
        "Gold"  : 0,
        "xp"    : 0,
        "lvl"   : 1,
        "Classe" : classe,
        "Skills" : vSkills[classe].copy(),                    #Faz uma copia das listas de dicionario de vSkills para nao alterar os valores para outros jogadores
        "Atributos" : vClasse[classe].copy(),                 #Faz uma copia das listas de dicionario de vClasse para nao alterar os valores para outros jogadores  
        "Inimigos" : 0,
        "Itens" : []
  }
#################################################
  save("jogadores.json",vJogadores)
  save("classe.json",vClasse)
  save("skills.json",vSkills)

  print("\n\t-=- Jogador Cadastrado -=-\n")

#endregion

#region MENU/INPUTs

def menu():
  print("\n\t-=- Menu -=-")
  print("\t1. Jogar")
  print("\t2. Cadastrar Jogador")
  print("\t3. Listar Jogadores")
  print("\t4. Procurar Jogador")
  print("\t5. Encerrar o Programa")

def op_():
  op = int(input("Digito: "))
  while op not in [1,2,3,4,5]:
    op = int(input("Valor Inválido\nDigito: "))
  return op

#endregion

def main():
  #region Variaveis Iniciais/Loads
  
  arm = 0
  Listas_Dicionarios()                     #Executa as Listas de Dicionarios para serem salvas e poderem ser usadas pelos jogadores
  vJogadores = load("jogadores.json")
  vClasse = load("classe.json")
  vInimigos = load("inimigos.json")
  vItens = load("itens.json")
  vAmbiente = load("ambiente.json")         #Sistema Futuro
  vSkills = load("skills.json")

 #endregion

  print("\n\t-=-SISTEMA DE RPG-=-")   
  menu()
  op = op_()
  while op != 5:

    if op == 1:
###############################################################################
      print("\n\t-=- Jogar -=-\n")                                            
      nome = input("Nome do Jogador: ")
      while nome.isalpha() != True or len(nome) < 0 or nome not in vJogadores:
        if nome not in vJogadores:
          print("\n\t-=- Jogador Não Encontrado -=-\n")
          nome = input("Nome do Jogador: ")
        else:
          nome = input("Valor Inválido\nNome do Jogador: ")
      controlador(vJogadores,nome,arm,vItens,vInimigos)
      menu()
      op = op_()
###############################################################################
    if op == 2:
      cad_player(vJogadores,vClasse,vSkills)
      menu()
      op = op_()

    if op == 3:
      listar_jogadores(vJogadores)
      menu()
      op = op_()

    if op == 4:
      print("\n\t-=-Ficha do Jogador-=-")
      porcurar_jogador(vJogadores)
      menu()
      op = op_()

  print("Saindo...")

main()
