**🗂️ CHANGELOG - Versão 2.0**

***🔥 Novas Funcionalidades***
Sistema Completo de Combate Dinâmico:

-Inclusão de missChance aleatória para determinar: dano crítico, cheio, de raspão, medíocre ou desvio.

-Sistema de ataque do inimigo com o mesmo sistema de acerto/erro.

-Sistema de Skills por Classe:

-Cada classe possui habilidades específicas que multiplicam o ataque.

-Jogador escolhe qual skill usar no ataque.

Sistema de Itens:

-Itens podem ser coletados durante a exploração.

-Itens de cura e buffs de ataque/defesa podem ser usados durante o combate e fora dele.

-Sistema de consumo e remoção do item do inventário após uso.

Sistema de Nível (Level Up):

-O jogador acumula XP de inimigos derrotados.

-O XP necessário para subir de nível cresce conforme o nível atual.

-Ao subir de nível, vida e ataque aumentam multiplicativamente em 20%.

Sistema de Exploração Aleatória:

Sistema que sorteia situações:

-Encontrar um inimigo

-Cair em uma armadilha

-Encontrar um item

-Nada acontecer

-Armadilhas que causam dano depois de um número aleatório de quedas.

Sistema de Ouro (Gold):

-Jogadores ganham ouro ao derrotar inimigos.

***🛠️ Melhorias Gerais***

-Separação das funções com #region para melhor organização visual.

-Função controlador para organizar o fluxo de jogo de acordo com os inputs do jogador.

Implementação de persistência dos dados via JSON para:

-Jogadores

-Inimigos

-Itens

-Classes

-Skills

Sistema robusto para o cadastro de jogadores, com:

-Escolha de classe com descrição e confirmação.

-Atributos e skills inicializados conforme a classe.

-Ficha de jogador detalhada mostrando todos os atributos, XP, gold, etc.

Menu Principal para navegar entre:

-Jogar

-Cadastrar novo jogador

-Listar jogadores

-Procurar ficha de jogador

***🐞 Correções & Ajustes***

-Validação de entradas nos menus e inputs do usuário.

-Prevenção de edição indesejada nos objetos compartilhados através de .copy().

***🗺️ Planejamento Futuro Indicado no Código***

-Uso futuro da variável vAmbiente para ambientes específicos na exploração.

-Potencial para adicionar mais efeitos aos itens além de cura e ataque.

***🔖 Resumo Técnico:***

                Feature	Status
      Sistema de Combate	    ✅ Completo
      Itens e Inventário	    ✅ Completo
      Sistema de Level Up    	✅ Completo
      Ouro / Gold	            ✅ Completo
      Skills por Classe	      ✅ Completo
      Persistência com JSON	  ✅ Completo
      Sistema de Exploração	  ✅ Completo
      Ambientes Variados	    🕒 Planejado
      NPCs / Missões	        ❌ Não implementado

***🗂️ Arquivos de Dados Criados***

-jogadores.json

-classe.json

-inimigos.json

-itens.json

-skills.json

***📌 Possíveis Melhorias para Próximas Versões:***

-Implementar sistema de defesa usando itens como escudo.

-Evoluir o sistema de XP necessário para subir de nível de forma exponencial.

-Criar um sistema de ambientação que modifique o tipo de inimigo/item encontrado.

-Adicionar narrativa básica ou sistema de missões.

-Adicionar Bosses ou inimigos raros.

-Salvar o inventário do jogador em arquivos separados ou embutido de forma otimizada.

-------------------------------------------------------------------------------------------------------------------

**🗂️ CHANGELOG - Versão 1.0**

***✅ Funcionalidades Implementadas***

*Cadastro de Jogadores:*

-Criação de jogadores com nome, idade e classe.

-Validação de entrada para nome e idade.

*Sistema de Classes Básico:*

-Jogadores escolhem entre classes como Guerreiro, Mago, Assassino e Arqueiro.

-Cada classe com atributos pré-definidos de vida e ataque.

*Listagem e Consulta de Jogadores:*

-Função para listar todos os jogadores cadastrados, exibindo nome, idade e classe.

-Função para procurar e exibir ficha completa de um jogador específico.

*Sistema de Menus:*

*Menu interativo com opções para:*

-Jogar

-Cadastrar Jogador

-Listar Jogadores

-Procurar Jogador

-Encerrar o programa

***🛠️ Persistência de Dados***

Uso de arquivos JSON para:

-Salvar o cadastro dos jogadores (jogadores.json).

-Salvar as informações de classes (classe.json).

***🔎 Validações e Segurança***

-Validação de entrada para evitar valores incorretos nos campos de nome e idade.

-Validação nas opções de menu para prevenir erros de input.

***📌 Resumo Técnico***
            
               Feature	Status
    Cadastro de Jogadores	      ✅ Completo
    Escolha de Classe	          ✅ Completo
    Persistência JSON	          ✅ Completo
    Listar Jogadores	          ✅ Completo
    Procurar Jogadores	        ✅ Completo
    Sistema de Combate	        ❌ Não implementado
    Sistema de Itens	          ❌ Não implementado
    Sistema de XP e Level Up	  ❌ Não implementado
    Skills por Classe	          ❌ Não implementado
    Exploração Aleatória	      ❌ Não implementado
