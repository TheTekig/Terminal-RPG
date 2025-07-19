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


def Combate(nome,vJogadores,vInimigos,vItens,vSkills):
  
  jogador = vJogadores[nome]                                              #Declaracao de jogador e inimigo para encurtar chave para chamada de atributos
  inimigo = gerador_inimigos(vInimigos)
  print("\n\t-=-Combate Iniciado-=-")
  time.sleep(1)
  print("\n\tSeu Inimigo é: ", inimigo['nome'])

  while jogador['Atributos']['vida'] > 0 and inimigo['vida'] > 0:
                                                                          #Status do Inimigo e do Jogador
    print(f"\n\t-=-{jogador['Nome']}-=-")
    time.sleep(0.5)
    print("\n\tVida: ",jogador['Atributos']['vida'])
    time.sleep(0.5)
    print("\tAtaque: ",jogador['Atributos']['ataque'])
    time.sleep(0.5)
    print("\tDefesa: ",jogador['Atributos']['defesa'])
    time.sleep(0.5)
    print(f"\n\t-=-Inimigo {inimigo['nome']}-=-")
    time.sleep(0.5)
    print("\n\tVida: ",inimigo['vida'])
    time.sleep(0.5)
    print("\tAtaque: ",inimigo['ataque'])

    print("\n-=-Analisando Iniciativa-=-")
    time.sleep(3)

    Inicio = random.randint(0,1)                                           #Numero Random para decidir quem sera o atacante

    time.sleep(0.5)

    if Inicio == 0:
      print("\n-=-Jogador Saiu Na Frente-=-")
      time.sleep(0.5)
      print("\n\t-=-Sua Vez-=-")
      time.sleep(0.5)
      print("-" * 50)
      time.sleep(0.5)
      print(f"//O Ataque do jogador vai escalionar com a Skill")
      print("=" * 50)
      time.sleep(0.5)
      print("\tA - ATTACK / I - ITENS")
      time.sleep(0.5)
      print("=" * 50)
      
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
        print("Jogador esta preparando o ataque...")
        time.sleep(random.randint(1,3))
        print(f"Jogador utilizou : {op}")

        if op == "Aumentar Defesa":

          jogador['Atributos']['defesa'] *= jogador['Skills'][op]
          print(f"\t!DEFESA AUMENTADA!\nDefesa Atual do Jogador - {jogador['Atributos']['defesa']}")
          time.sleep(0.5)
          print("-" * 50)
        else:

          ataque = jogador['Atributos']['ataque'] * jogador['Skills'][op]

          #Escalabilidade do ataque
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
        print("=" * 50)
        time.sleep(0.5)
        print(f"{jogador['Itens']}")
        time.sleep(0.5)
        print("Escolha seu Item (ou digite 0 para cancelar):")
        time.sleep(0.5)
        print("=" * 50)
        time.sleep(0.5)
        item_nome = input("---> ")
        time.sleep(0.5)
        print("-" * 50)
        time.sleep(0.5)
        if item_nome == "0":
            print("Jogador não escolhe nenhum item e o jogo avança")
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
      totem_encontrado = False
      for i in jogador['Itens']:
        
        if i['nome'] == "Totem de Negacao de Dano":
          totem_encontrado = True
          time.sleep(0.5)
          print("\n-=-Inimigo saiu na Frente-=-")
          time.sleep(random.randint(1,3))
          print("Um Totem Salta de seu bolso!")
          time.sleep(0.5)
          print("\n\t-=-TOTEM DEFENDIDO-=-")
          time.sleep(0.5)
          print("-" * 50)
          time.sleep(0.5)
          jogador['Itens'].remove(i)
          print('-=- Item - Totem de Negacao de Dano foi Utilizado -=-')
          time.sleep(0.5)
          break

      if not totem_encontrado:
          time.sleep(0.5)
          print("\n-=-Inimigo saiu na Frente-=-")
          time.sleep(0.5)
          print("\n\t-=-Inimigo Vez-=-")

          print("-" * 50)

          #region Aleatoridade/DanoInimigo
          print("Inimigo esta pensando no ataque...")
          time.sleep(random.randint(1,5))
          ataque = inimigo['ataque']
          missChance = random.randint(0,100)


          if missChance < 5:

            print("\t!DANO CRITICO!")
            time.sleep(0.5)
            print("Dano :" , ataque * 1.5)
            time.sleep(0.5)

            if jogador['Atributos']['defesa'] <= 0:

              jogador['Atributos']['vida'] -= ataque * 1.5
              time.sleep(0.5)
              print(f"Vida Atual do Jogador - {jogador['Atributos']['vida']}")

            else:
              jogador['Atributos']['defesa'] -= ataque * 1.5

              if jogador['Atributos']['defesa'] <= 0:
                jogador['Atributos']['defesa'] = 0
                print("\n\t!Defesa Destruida!")

              else:
                print("\n\tDefesa Aguentou Ataque!")
                time.sleep(0.5)
                print(f"Defesa Atual do Jogador - {jogador['Atributos']['defesa']}")

          elif missChance < 30:

            print("\t!DANO CHEIO!")
            time.sleep(0.5)
            print("Dano :" , ataque )
            time.sleep(0.5)
            if jogador['Atributos']['defesa'] <= 0:

              jogador['Atributos']['vida'] -= ataque 
              time.sleep(0.5)
              print(f"Vida Atual do Jogador - {jogador['Atributos']['vida']}")
            else:
              jogador['Atributos']['defesa'] -= ataque 
              if jogador['Atributos']['defesa'] <= 0:
                jogador['Atributos']['defesa'] = 0
                print("\n\t!Defesa Destruida!")

              else:
                print("\n\tDefesa Aguentou Ataque!")
                time.sleep(0.5)
                print(f"Defesa Atual do Jogador - {jogador['Atributos']['defesa']}")

          elif missChance < 50:

            print("\t!DANO MEDIOCRE!")
            time.sleep(0.5)
            print("Dano :" , ataque / 2)
            time.sleep(0.5)
            if jogador['Atributos']['defesa'] <= 0:

              jogador['Atributos']['vida'] -= ataque / 2
              time.sleep(0.5)
              print(f"Vida Atual do Jogador - {jogador['Atributos']['vida']}")
            else:
              jogador['Atributos']['defesa'] -= ataque / 2
              if jogador['Atributos']['defesa'] <= 0:
                jogador['Atributos']['defesa'] = 0
                print("\n\t!Defesa Destruida!")

              else:
                print("\n\tDefesa Aguentou Ataque!")
                time.sleep(0.5)
                print(f"Defesa Atual do Jogador - {jogador['Atributos']['defesa']}")

          elif missChance < 70:

            print("\t!DANO RASPAO!")
            time.sleep(0.5)
            print("Dano :" , ataque / 4)
            time.sleep(0.5)
            if jogador['Atributos']['defesa'] <= 0:

              jogador['Atributos']['vida'] -= ataque / 4
              time.sleep(0.5)
              print(f"Vida Atual do Jogador - {jogador['Atributos']['vida']}")
            else:
              jogador['Atributos']['defesa'] -= ataque / 4
              if jogador['Atributos']['defesa'] <= 0:
                jogador['Atributos']['defesa'] = 0
                print("\n\t!Defesa Destruida!")

              else:
                print("\n\tDefesa Aguentou Ataque!")
                time.sleep(0.5)
                print(f"Defesa Atual do Jogador - {jogador['Atributos']['defesa']}")

          else:
            time.sleep(1)
            print("\t!JOGADOR DESVIOU!")
            time.sleep(0.5)
            jogador['Atributos']['vida'] -= 0
            time.sleep(0.5)
            print(f"Vida Atual do Jogador - {jogador['Atributos']['vida']}")

        #endregion

      print("-" * 50)
      time.sleep(0.5)
  if jogador['Atributos']['vida'] <= 0:                                 #Morte do Jogador Caso sua vida seja meno igual a 0
    time.sleep(1)
    print("\n\t!VOCE ESTA INCAPACITADO!")
    
  else:
    time.sleep(0.5)
    print("\n","-=" * 10,"INIMIGO DERROTADO","=-" * 10,"\n")
    time.sleep(2)
    ###############Recompensas########################
    jogador['xp'] += inimigo['xp']
    jogador['Inimigos'] += 1
    goldmonster = random.randint(0,inimigo['gold'])
    jogador['Gold'] += goldmonster
    #################################################

    print(f"Jogador Adquiriu {inimigo['xp']}XP")
    time.sleep(1)
    print(f"Jogador Adquiriu {goldmonster} Gold")
    time.sleep(1)

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
    time.sleep(0.5)
    print(f"Jogador{jogador['Nome']} subiu para o nivel {jogador['lvl']}")
    time.sleep(0.5)
    print(f"Novos atributos = Vida:{jogador['Atributos']['vida']} / Ataque:{jogador['Atributos']['ataque']}")
    time.sleep(0.5)
    print("-" * 50)
    jogador['xp']  -= XPnextLevel

  save("jogadores.json",vJogadores)


def Game_Inputs():                                                       #Em geral alguns inputs

  time.sleep(0.5)
  print("=" * 50)
  time.sleep(0.5)
  print("\tM - MOVE / S - STATUS / I - ITENS")
  time.sleep(0.5)
  print("=" * 50)
  time.sleep(0.5)
  op = input("--->")
  while op.upper() not in ["M","S","I","0"]:
    op = input("Invalido\n--->")
  
  return op.upper() 

def exploracao(vAmbiente,vJogadores,nome):

  vJogadores[nome]['ambiente'] += 1

  if vJogadores[nome]['ambiente'] == (random.randint(3,10)):
    
    ambiente = vAmbiente[str(random.randint(1,4))]['nome']
    print(f"Voce esta adentrando a ... {ambiente}")

    vJogadores[nome]['ambiente'] = 0

  Situacoes = ["Acho Inimigo!" , "Nada Aconteceu" , "Achou um Item", "Caiu em uma Armadilha", "Achou NPC" , "Achou Comerciante"]           #Todas as possiveis situacoes que o jogador pode acabar entrando
  resultado = random.choice(Situacoes)                                                                  #Escolhe uma situacao da lista de situacoes elaborada acima
  
  return resultado

def controlador(vJogadores,nome,arm,vItens,vInimigos,vNPC,vComerciantes,vSkills,vAmbiente):                   #Controlador chama todas as funcoes de acoes dependendo da escolha do jogador
  acao = Game_Inputs()

  while acao != "0":

    if acao == "M":
      print("\nExplorando...")
      time.sleep(random.randint(1,4))
      situacao = exploracao(vAmbiente,vJogadores,nome)

      if situacao == "Acho Inimigo!":                                       #Inicia a funcao de combate do jogador
        print("Voce sente uma presença se aproximando...")
        time.sleep(random.randint(1,4))
        Combate(nome,vJogadores,vInimigos,vItens,vSkills)
        acao = Game_Inputs()

      elif situacao == "Nada Aconteceu":
        print("NADA OCORREU!\n")
        acao = Game_Inputs()

      elif situacao == "Caiu em uma Armadilha":
        print("Voce sente que esta em uma enrascada...")
        time.sleep(2)
        print("Voce caiu em uma armadilha mas escapou!\n")
        time.sleep(0.5)
        arm += 1                            

        if arm == random.randint(3,10):
          print("Voce sente que esta em uma enrascada...")
          time.sleep(2)                                     #Impede que toda vez que o jogador caia em uma armadilha ele se machuque
          print("Voce caiu em uma armadilha e se machucou!")
          time.sleep(0.5)
          vJogadores[nome]['Atributos']['vida'] -= random.randint(1,10)     #Aleatoridade do dano que o jogador ira tomar caso caia na armadilha
          print(f"Vida: {vJogadores[nome]['Atributos']['vida']}\n")
          time.sleep(0.5)
          arm = 0

        acao = Game_Inputs()

      elif situacao == "Achou NPC":

        print("Voce sente uma presença se aproximando...")

        time.sleep(random.randint(1,4))
        NPC = gerador_npc(vNPC)

        print(f"Voce achou um NPC - {NPC['nome']}")
        time.sleep(0.5)
        print("Eu preciso te dizer uma coisa...")
        time.sleep(2.5)
        print(f"\n\t{NPC['nome']}\n")
        time.sleep(0.5)
        print(f"{NPC['Fala-1']}\n")
        time.sleep(0.5)
        print("-" * 50)
        time.sleep(0.5)
        acao = Game_Inputs()

      elif situacao == "Achou Comerciante":

        print("Voce sente uma presença se aproximando...")
        time.sleep(random.randint(1,4))
        Comerciante = gerador_comerciante(vComerciantes)

        if Comerciante['nome'] == "Jhonny o UPGRADE":
    
          print(f"Voce achou um Comerciante - {Comerciante['nome']}")
          time.sleep(0.5)
          print("-" * 50)
          time.sleep(0.5)
          print(f"\n\t{Comerciante['nome']}\n")
          time.sleep(0.5)
          print("AE CUMPADE!!! VOU TE DAR UMA MORAL!!!")
          time.sleep(0.5)
          print("PELOS PODERES DE OJHONNYYY!!!")
          time.sleep(0.5)

          if 0 == random.randint(0,1):
            print("EU TE DOU A FORÇA!!!")
            vJogadores[nome]['Atributos']['ataque'] += 2
            save("jogadores.json",vJogadores)
          else:
            print("EU TE DOA A CURA!!!")
            vJogadores[nome]['Atributos']['vida'] += 5
            save("jogadores.json",vJogadores)

          print("-" * 50)
          time.sleep(0.5)
          acao = Game_Inputs()

        else:
          print(f"Voce achou um Comerciante - {Comerciante['nome']}")

          time.sleep(0.5)
          print("-" * 50)
          time.sleep(0.5)

          print(f"\n\t{Comerciante['nome']}\n")

          time.sleep(0.5)

          print(f"{Comerciante['item - 1']} Valor : 2")

          time.sleep(0.5)

          print(f"{Comerciante['item - 2']} Valor : 3\n")

          time.sleep(0.5)
          print("-" * 50)
          time.sleep(0.5)

          print("Escolha seu Item (ou digite 0 para cancelar):")
          time.sleep(0.5)
          print(f"Gold : {vJogadores[nome]['Gold']}")
          time.sleep(0.5)
          print("=" * 50)
          time.sleep(0.5)

          item_nome = input("---> ")
          time.sleep(0.5)

          print("-" * 50)
          time.sleep(0.5)

          if item_nome == "0":
              acao = Game_Inputs()

          else:
              if item_nome == Comerciante['item - 1']:
                if vJogadores[nome]['Gold'] >= 2:                 
                  item = Comerciante['item - 1']
                  vJogadores[nome]['Gold'] -= 2
                  vJogadores[nome]['Itens'].append(item)
                  save("jogadores.json",vJogadores)
                  acao = Game_Inputs()

                else:
                  print("Voce nao possui dinheiro suficiente...")
                  time.sleep(0.5)
                  print("Não Tenho tempo para quem nao tem dinheiro!")
                  time.sleep(0.5)
                  acao = Game_Inputs()
                  
                

              elif item_nome == Comerciante['item - 2']:
                if vJogadores[nome]['Gold'] >= 3:
                  item = Comerciante['item - 2']
                  vJogadores[nome]['Gold'] -= 3
                  vJogadores[nome]['Itens'].append(item)
                  save("jogadores.json",vJogadores)
                  acao = Game_Inputs()

                else:
                  print("Voce nao possui dinheiro suficiente...")
                  time.sleep(0.5)
                  print("Não Tenho tempo para quem nao tem dinheiro!")
                  time.sleep(0.5)
                  acao = Game_Inputs()

      else:
        item = gerador_itens(vItens)                                        #Adicao de itens a um "Inventario" do jogador
        vJogadores[nome]['Itens'].append(item)
        print(f"Voce achou um - {item}\n")
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


def gerador_npc(vNPC):
  num = random.randint(1,len(vNPC))
  print("!NPC AVISTADO!")
  time.sleep(random.randint(1,3))
  return vNPC[str(num)].copy()

def gerador_comerciante(vComerciantes):
  num = random.randint(1,len(vComerciantes))
  print("!COMERCIANTE AVISTADO!")
  time.sleep(random.randint(1,3))
  return vComerciantes[str(num)].copy()
  
def gerador_inimigos(vInimigos):                                          #Escolhe um Inimigo do Dicionario de Inimigos
  num = random.randint(1,len(vInimigos))
  print("!INIMIGO AVISTADO!")
  time.sleep(random.randint(1,3))        
  return vInimigos[str(num)].copy()                 #faz uma copia do inimigo para nao alterar a variavel principal do inimigo

def gerador_itens(vItens):                                                #Escolhe um Item da lista de Itens do jogo
  num = random.randint(1,len(vItens))
  print("\tVoce ve algo brilhando a distancia...")
  time.sleep(4)
  return vItens[str(num)]

def Listas_Dicionarios():                                                 #Listas de Dicionarios com os principais elementos

    vAmbiente = {
        "1" : {"nome" : "Dangeon"},
        "2" : {"nome" : "Floresta"},
        "3" : {"nome" : "Campo Escuro"},
        "4" : {"nome" : "Casa Abandonada"}
    }


    vInimigos = {
      
      "1" : {"nome" : "Zumbi",        "vida" : 10 , "ataque" : 5, "xp" : 5, "gold" : 4},
      "2" : {"nome" : "Esqueleto",    "vida" : 15 , "ataque" : 10,"xp" : 12, "gold" : 6},
      "3" : {"nome" : "Mago Sombrio", "vida" : 20 , "ataque" : 15,"xp" : 10, "gold" : 7},
      "4" : {"nome" : "Bandido",      "vida" : 25 , "ataque" : 20,"xp" : 14, "gold" : 8},
      "5" : {"nome" : "Louco",        "vida" : 30 , "ataque" : 25,"xp" : 20, "gold" : 20}
    }

    vItens = {
      "1" : {"nome" : "Pocao de Cura"   , "Cura"   : 20 },
      "2" : {"nome" : "Pocao de Forca"  , "Ataque" : 1.5},
      "3" : {"nome" : "Totem de Negacao de Dano"},
      "4" : {"nome" : "Bomba"           , "Ataque" : 25},
      "5" : {"nome" : "Arco"            ,  "Ataque": 1.1},
      "6" : {"nome" : "Espada"          , "Ataque" : 1.2},
      "7" : {"nome" : "Escudo"          , "Defesa" : 1.2}
    }

    vComerciantes = {
        "1" : {"nome" : "Robert O comerciante", "item - 1" : vItens['1'],"item - 2" : vItens['4'] },
        "2" : {"nome" : "Gilbert O  Armoreiro", "item - 1" : vItens['6'],"item - 2" : vItens['5'] },
        "3" : {"nome" : "Venis o Alquimista",   "item - 1" : vItens['1'],"item - 2" : vItens['2'] },
        "4" : {"nome" : "Jhonny o UPGRADE"}
        
    }

    vNPC = {
        "1" : {"nome" : "Jorjinho", "Fala-1" : "Opa Amigo! Sabe onde fica o Banheiro?"},
        "2" : {"nome" : "Jhonny" ,  "Fala-1" : "É O JHONYYY!" },
        "3" : {"nome" : "Carpina" ,  "Fala-1" : "Como que eu sobrevivo assim eim?"},
        "4" : {"nome" : "Inimigo" ,  "Fala-1" : "Eu nao ataco nao piah!" }

    }

    vSkills = {
      
      "Guerreiro" : {"Slash" : 1.5 , "Porrada" : 1.1 , "Aumentar Defesa" : 1.2},
      "Mago"      : {"Bola de Fogo" : 1.5 , "Cajadada" : 0.9 , "Enfraquecimento" : 5},
      "Assassino"  : {"Corte Profundo" : 1.4  , "Ataque Escondido" : 1.2 , "Ataque baixo" : 1.7},
      "Arqueiro"  : {"Flecha Comum" : 1.1 , "Flecha com efeito" : 1.3, "Flecha Explosiva" : 1.5}    
                     
    }

    vClasse = {
      
      "Guerreiro" : {"vida" : 20 , "ataque" : 5 , "defesa" : 6 },
      "Mago"      : {"vida" : 10 , "ataque" : 15, "defesa" : 0 },
      "Assassino"  : {"vida":  5 , "ataque" : 20, "defesa" : 2 },
      "Arqueiro"  : {"vida" : 15 , "ataque" : 10, "defesa" : 3 }

    }
    
    save("classe.json",vClasse)
    save("inimigos.json",vInimigos)
    save("itens.json",vItens)
    save("skills.json",vSkills)
    save("comerciantes.json",vComerciantes)
    save("npc.json",vNPC)
    save("ambiente.json",vAmbiente)

#region CADASTRO/FUNCOES DE MENU

def ficha_jogador(vJogadores,nome):                                       #Ficha Simples com todos os Status
  time.sleep(0.5)
  print("-" * 40)
  time.sleep(0.5)
  print("\tNome: "  ,vJogadores[nome]["Nome"])
  time.sleep(0.5)
  print("\tIdade: " ,vJogadores[nome]["Idade"])
  time.sleep(0.5)
  print("\tGold: "  ,vJogadores[nome]["Gold"])
  time.sleep(0.5)
  print("\txp: "    ,vJogadores[nome]["xp"])
  time.sleep(0.5)
  print("\tLevel: " ,vJogadores[nome]["lvl"])
  time.sleep(0.5)
  print("\tClasse: ",vJogadores[nome]["Classe"])
  time.sleep(0.5)
  print("\tVida: "  ,vJogadores[nome]["Atributos"]["vida"])
  time.sleep(0.5)
  print("\tDefesa: ",vJogadores[nome]["Atributos"]["defesa"])
  time.sleep(0.5)
  print("\tAtaque: ",vJogadores[nome]["Atributos"]["ataque"])
  time.sleep(0.5)
  print("\tInimigos: ",vJogadores[nome]["Inimigos"])
  time.sleep(0.5)
  print("-" * 40)

def porcurar_jogador(vJogadores):                                         #Funcao de Procurar Jogador (obs: Posso implementar isso melhor para reutilizar em outros locais)
  nome = input("Nome do Jogador: ")
  while nome.isalpha() != True or len(nome) < 0:
    nome = input("Valor Inválido\nNome do Jogador: ")
  if nome in vJogadores:
    ficha_jogador(vJogadores,nome)
    return nome
  else:
    print("\n\t-=- Jogador Não Encontrado -=-\n")
  

def remover_jogador(vJogadores):
  nome = porcurar_jogador(vJogadores)
  op = input("Deseja realmente remover esse jogador? (S/N): ").upper()
  while op not in ["S", "N"]:
    op = input("Valor Inválido\nDeseja realmente remover esse jogador? (S/N): ").upper()
  if op == "S":
    del vJogadores[nome]
    print("Jogador Removido.")
  else:
    print("Jogador não removido.")
  save("jogadores.json",vJogadores)

def listar_jogadores(vJogadores):                                         #Listagem com nome/idade/clasee de cada jogador
  print("\n\t-=-Lista de Jogadores-=-\n ")
  print("-" * 20)
  for nome,dado in vJogadores.items():
    print(f"Nome:  {dado['Nome']}")
    print(f"Idade: {dado['Idade']}")
    print(f"Classe: {dado['Classe']}")
    print(f"Level: {dado['lvl']}")
    print(f"XP: {dado['xp']}")
    print(f"Kills: {dado['Inimigos']}")
    print("-" * 20)

def opcoesdeclasse():
  time.sleep(0.5)
  print("\n\tClasse do Jogador: ")
  time.sleep(0.5)
  print("\t1. Guerreiro")
  time.sleep(0.5)
  print("\t2. Mago")
  time.sleep(0.5)
  print("\t3. Assassino")
  time.sleep(0.5)
  print("\t4. Arqueiro")
  time.sleep(0.5)

def cad_player(vJogadores,vClasse,vSkills):                               #Cadastro Player
  #region Nome/Idade

  nome = input("Nome do Jogador: ")
  while nome.replace(" ","").isalpha() != True or len(nome) == 0:
    nome = input("Valor Inválido\nNome do Jogador:")
  
  idade = input("Idade do Jogador: ")
  while idade.isdigit() != True:
    idade = input("Valor Inválido\nIdade do Jogador: ")

  #endregion
          
  while True:       #Mostra cada tipo de Classe
     
      opcoesdeclasse()
      op = op_()

      if op == "1":
          classe = "Guerreiro"
          descricao = "-Possui Mais Vida\n-Ataque Equilibrado"
      elif op == "2":
          classe = "Mago"
          descricao = "-Vida Mediana\n-Aprende magias\n-Dano um pouco maior"
      elif op == "3":
          classe = "Assassino"
          descricao = "-Vida Baixa\n-Ataque Muito Alto"
      elif op == "4":
          classe = "Arqueiro"
          descricao = "-Vida e Ataque Equilibrados"
      else:
        print("\n\t-=-Valor Invalido-=-\n")
        continue #Volta pro inicio do While
        

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
        "ambiente" : 0,
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
  time.sleep(0.5)
  print("\n","-=" * 7 , "Menu", "=-" * 10,"\n")
  time.sleep(0.5)
  print("\t1. Jogar")
  time.sleep(0.5)
  print("\t2. Cadastrar Jogador")
  time.sleep(0.5)
  print("\t3. Listar Jogadores")
  time.sleep(0.5)
  print("\t4. Procurar Jogador")
  time.sleep(0.5)
  print("\t5. Remover Jogador")
  time.sleep(0.5)
  print("\t6. Encerrar o Programa")
  time.sleep(0.5)

def op_():
  op = input("Digito: ")
  while op not in ["1","2","3","4","5","6"]:
    op = input("Valor Inválido\nDigito: ")
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
  vComerciantes = load("comerciantes.json")
  vNPC = load("npc.json")

 #endregion

  print("\n\t -=-SISTEMA DE RPG-=-")   
  menu()
  op = op_()
  while op != "6":

    if op == "1":
###############################################################################
      print("\n","-=" * 7 , "Jogar", "=-" * 10,"\n")                                            
      nome = input("Nome do Jogador: ")
      while nome.isalpha() != True or len(nome) < 0 or nome not in vJogadores:
        if nome not in vJogadores:
          print("\n\t-=- Jogador Não Encontrado -=-\n")
          nome = input("Nome do Jogador: ")

        else:
          nome = input("Valor Inválido\nNome do Jogador: ")
      time.sleep(0.5)    
      print("=-" * 25)
      time.sleep(0.5)
      print("\t!BEM VINDO A ECHRONIA!")
      time.sleep(0.5)
      print("=-" * 25)
      time.sleep(0.5)
      print(f"\n\tOlá {nome}!")
      time.sleep(0.5)
      print(f"Nesse momento voce esta adentrando a... {vAmbiente[str(random.randint(1,4))]['nome']}\n")
      time.sleep(0.5)
      print("=-" * 25)
      time.sleep(0.5)
      controlador(vJogadores,nome,arm,vItens,vInimigos,vNPC,vComerciantes,vSkills,vAmbiente)
      menu()
      op = op_()
###############################################################################
    if op == "2":
      print("\n","-=" * 7 , "Cadastro", "=-" * 10,"\n")
      cad_player(vJogadores,vClasse,vSkills)
      menu()
      op = op_()

    if op == "3":
      listar_jogadores(vJogadores)
      menu()
      op = op_()

    if op == "4":
      print("\n","-=" * 7 , "Ficha", "=-" * 10,"\n")
      porcurar_jogador(vJogadores)
      menu()
      op = op_()
    
    if op == "5":
      print("\n","-=" * 7 , "Remover", "=-" * 10,"\n")
      remover_jogador(vJogadores)
      menu()
      op = op_()

  print("Saindo...")

main()
