🗂️ CHANGELOG - Versão 4.0
📆 2025-07-18

    Resumo: Grande expansão no ecossistema do jogo: novas interações com NPCs, buffs, comerciantes aprimorados, defesa com Totem, sistema avançado de exploração e itens únicos.

✅ Novas Funcionalidades

    -NPC Jhonny o UPGRADE
    
    -NPC que concede buffs aleatórios de ataque ou vida ao jogador, limitado a 1 buff por encontro.
    
    -Totem de Negação de Dano
    
    -Item especial que impede completamente o próximo ataque recebido.
    
    -Mensagem narrativa personalizada quando o efeito é ativado.
    
    -Sistema de Comprar Itens com Gold
    
    -Comerciante oferece itens diversos por valores variados de gold.
    
    -Validação de saldo e atualização automática do inventário.
    
    -Novos Itens Adicionados
    
    -Pocao de Cura, Pocao de Forca, Totem, Bomba, Arco, Espada, Escudo.
    
    -Cada item possui tipo (Cura, Ataque, Defesa) para tratamento específico.
    
    -Sistema de Encontrar Itens na Exploração
    
    -Durante a exploração, existe a chance de encontrar um item aleatório.
    
    -Item encontrado é automaticamente adicionado ao inventário com mensagem narrativa.
    
    -Consumir Itens Fora de Combate
    
    -Jogador pode acessar o inventário e consumir itens de cura ou buffs direto do menu de exploração.
    
    -Sistema de Armadilhas Avançado
    
    -Armadilhas agora acumulam ativações antes de causarem dano real.
    
    -Dano permanece aleatório entre 1 e 10.

🟠 Aprimoramentos e Melhorias

    -Combate Enriquecido
    
    -Jogador escolhe entre atacar ou usar itens.
    
    -Itens como Totem, Pocao de Forca e Cura aplicam efeitos estratégicos no turno.
    
    -Feedback Narrativo
    
    -Mensagens detalhadas informando buffs, usos de itens, bloqueio de ataques, etc.
    
    -Uso de time.sleep() para criar ritmo narrativo.
    
    -Organização de Funções

Criação de funções específicas para:

    -Gerar inimigos.
    
    -Gerar NPCs.
    
    -Gerar comerciantes.
    
    -Gerar ambientes.
    
    -Encontrar itens aleatórios.
    
    -Refino do Level Up
    
    -XP necessário: nível atual * 10.
    
    -Vida e ataque aumentam em 20% ao subir de nível.

🟢 Correções e Ajustes Técnicos

    -Controle aprimorado de inputs inválidos.
    
    -Salvamento dos dados do jogador após cada ação importante.
    
    -Otimização da busca e remoção de itens no inventário.
    
    -Uso adequado de .copy() para evitar mutação não-intencional dos dados carregados.

❌ Pontos Preparados mas Ainda Não Implementados

    -O atributo de defesa do Escudo ainda não é aplicado no cálculo do dano recebido.
    
    -Sistema de Ambientes com efeitos reais sobre o jogo ainda não integrado.
    
    -Missões, história e bosses ainda não presentes.

📌 Resumo Técnico
    
                Sistema	                    Status
    Uso de Itens no Combate	            ✅ Completo
    NPCs com buffs	                    ✅ Completo
    Totem de Defesa Total	            ✅ Completo
    Comerciante com sistema de compra	✅ Completo
    Encontrar Itens em Exploração	    ✅ Completo
    Armadilhas com contador	            ✅ Completo
    Defesa aplicada no cálculo	        ❌ Pendente
    Ambientes com efeitos	            ❌ Pendente
    Sistema de História/Missões	        ❌ Pendente

🗂️ CHANGELOG - Versão 3.0

    -2025-07-17	3.0	Expansão do sistema de RPG: melhorias em combate, itens, inventário, exploração e progressão do jogador.

✅ Novas Funcionalidades / Melhorias

    -Sistema de Uso de Itens dentro do Combate

    -O jogador agora pode optar por usar itens em vez de atacar.

    -Itens de cura e ataque aplicam efeitos diretamente durante o combate.

    -Implementada opção de cancelar o uso do item.

    -Consumo e Gerenciamento de Itens

    -Itens são removidos do inventário após uso.

    -Validação se o item existe antes do uso.

    -Feedback visual de item consumido ou não encontrado.

    -Sistema de Defesa Parcial (Estruturado nos Itens)

    -Adição do item "Escudo" com atributo de defesa (ainda não aplicado no cálculo de combate, mas preparado).

    -Exploração Refinada

    -Armadilhas agora acumulam um contador (arm) e só causam dano após um número aleatório de ativações.

    -Dano das armadilhas é aleatório entre 1 e 10 de vida.

    -Incrementos Narrativos e Ambientação

    -Mensagens narrativas aprimoradas: "Você sente uma presença...", "Você vê algo brilhando...".

    -Adicionado delay (time.sleep) para simular suspense e fluidez no jogo.

    -Aprimoramento na Exibição de Status

    -Ficha do jogador agora exibe inimigos derrotados.

    -Melhoria na Modularização

    -Adição de função Game_Inputs centralizando os inputs de comando (Mover, Status, Itens).

    -Validação reforçada para evitar opções inválidas em diversas escolhas.

    -Otimização do Sistema de Level Up

    -XP para o próximo nível definido por multiplicação do nível atual por 10.
    
    -Subida de nível aumenta vida e ataque em 20%.

✅ Ajustes Técnicos e de Organização

    -Uso de .copy() ao carregar inimigos, classes e skills para evitar mutação global de referências.
    -Salvamento do progresso dos jogadores após todas as operações importantes.
    -Inclusão de marcação de regiões do código para melhor organização.

❌ Pontos Preparados mas Não Implementados

    -O atributo de "Defesa" do escudo ainda não está integrado ao cálculo de dano.
    -Sistema de ambiente ainda pendente (vAmbiente é carregado mas não usado).
    -Sistema de missões, história ou objetivos ainda não introduzido.

-------------------------------------------------------------------------------------------------------------------

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

            Feature	            Status
      Sistema de Combate	      ✅ Completo
      Itens e Inventário	      ✅ Completo
      Sistema de Level Up      	  ✅ Completo
      Ouro / Gold	              ✅ Completo
      Skills por Classe	          ✅ Completo
      Persistência com JSON	      ✅ Completo
      Sistema de Exploração	      ✅ Completo
      Ambientes Variados	      🕒 Planejado
      NPCs / Missões	          ❌ Não implementado

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
            
            Feature              Status
    Cadastro de Jogadores	      ✅ Completo
    Escolha de Classe	          ✅ Completo
    Persistência JSON	          ✅ Completo
    Listar Jogadores	          ✅ Completo
    Procurar Jogadores	          ✅ Completo
    Sistema de Combate	          ❌ Não implementado
    Sistema de Itens	          ❌ Não implementado
    Sistema de XP e Level Up	  ❌ Não implementado
    Skills por Classe	          ❌ Não implementado
    Exploração Aleatória	      ❌ Não implementado
