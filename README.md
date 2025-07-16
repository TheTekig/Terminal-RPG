# ***🎮 Sistema de RPG por Terminal***

Projeto desenvolvido em **Python** para praticar lógica de programação, manipulação de arquivos JSON e construção de um sistema de RPG jogável por terminal.

## **🚀 Funcionalidades**

- 📋 **Cadastro de Jogadores**: Nome, idade e escolha de classe.
- 🧙‍♂️ **Classes com Atributos Diferentes**:
  - Guerreiro, Mago, Assassino e Arqueiro
  - Cada classe possui vida, ataque e skills específicas.
- 🗡️ **Sistema de Combate**:
  - Turnos alternados entre jogador e inimigo
  - Sistema de dano crítico, dano cheio, raspão ou desvio
  - Cálculo de dano baseado em skills e atributos
- 📜 **Listagem de Jogadores**
- 🔍 **Busca de Jogador por Nome**
- 💾 **Persistência de Dados**:
  - Utilização de arquivos JSON para salvar informações de jogadores, inimigos, classes, itens e skills.

## **📂 Estrutura do Projeto**

    📁 rpg_terminal/
    ├── main.py              # Arquivo principal que inicia o jogo
    ├── jogadores.json       # Dados dos jogadores
    ├── classe.json          # Informações das classes
    ├── inimigos.json        # Dados dos inimigos
    ├── itens.json           # Definições de itens
    ├── ambiente.json        # Ambientes de exploração (planejado)
    ├── skills.json          # Skills por classe

##**⚙️ Tecnologias**
-Python 3

-JSON para armazenamento de dados

-Random para eventos aleatórios no combate

-Funções e modularização do código

##**🎯 Objetivos de Aprendizado**
-Consolidação de lógica de programação

-Modelagem de sistemas com dicionários complexos

-Persistência de dados com JSON

-Simulação de mecânicas básicas de RPG

##**🚧 Melhorias Futuras**
-Sistema completo de exploração e ambientes

-Inventário e sistema de itens

-Evolução dos personagens com XP e níveis

-Sistema de defesa e buffs/debuffs

-Interface gráfica (GUI)

##**✅ Como Executar**
***Clone o repositório:***
-git clone https://github.com/seu-usuario/rpg_terminal.git

***Acesse a pasta:***
-cd rpg_terminal

***Execute o arquivo principal:***
-python main.py

##**🤝 Contribuição**
Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

***🛡️ Feito por TheTekig***
