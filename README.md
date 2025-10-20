<h1 align="center"> Terminal-RPG </h1>

<div align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green" alt="License"></a>
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Version-1.0.0-orange" alt="Version">
</div>

---

## 📝 Descrição

<p align="center">
Terminal-RPG é um jogo de RPG de console desenvolvido em <b>Python</b>, com exploração, combate por turnos, evolução de personagens e eventos aleatórios. O jogador cria seu herói, enfrenta inimigos, interage com NPCs, coleta itens e sobe de nível!
</p>

---

## ⚔️ Funcionalidades

<ul>
  <li>Cadastro de jogadores com validação</li>
  <li>Sistema de classes: Guerreiro, Mago, Assassino e Arqueiro</li>
  <li>Combate por turnos com habilidades e itens</li>
  <li>Sistema de level-up com atributos escaláveis</li>
  <li>Exploração de ambientes aleatórios</li>
  <li>Eventos aleatórios: inimigos, NPCs, comerciantes, armadilhas e itens</li>
  <li>Inventário com efeitos especiais (cura, ataque, defesa)</li>
  <li>Persistência de dados via arquivos JSON</li>
</ul>

---

## 🎮 Como Jogar

<ol>
  <li>Clone o repositório:
    <pre><code>git clone https://github.com/seuusuario/Terminal-RPG.git
cd Terminal-RPG</code></pre>
  </li>
  <li>Execute o jogo:
    <pre><code>python TerminalRPG.py</code></pre>
  </li>
  <li>Use o menu inicial para criar ou acessar seu personagem</li>
  <li>No jogo:
    <ul>
      <li><b>M</b> → Explorar</li>
      <li><b>S</b> → Status</li>
      <li><b>I</b> → Inventário/Itens</li>
      <li>Use ataques e habilidades para derrotar inimigos</li>
    </ul>
  </li>
</ol>

---

## 🧩 Estrutura do Projeto

<pre>
Terminal-RPG/
│
├─ TerminalRPG.py        # Arquivo principal do jogo
├─ jogadores.json        # Dados salvos dos jogadores
├─ itens.json            # Itens disponíveis
├─ inimigos.json         # Inimigos
├─ skills.json           # Habilidades das classes
├─ classe.json           # Informações de classes
├─ npc.json              # NPCs
├─ comerciantes.json     # Comerciantes
└─ ambiente.json         # Ambientes exploráveis
</pre>

---

## 📈 Roadmap

<ul>
  <li>✅ Sistema de cadastro de jogadores</li>
  <li>✅ Sistema de combate com habilidades e itens</li>
  <li>✅ Exploração e eventos aleatórios</li>
  <li>⬜ Adição de som e efeitos no console</li>
  <li>⬜ Sistema de quests e missões</li>
  <li>⬜ Salvamento em banco de dados (SQLite ou MongoDB)</li>
  <li>⬜ Interface gráfica com PyGame</li>
</ul>

---

## 🤝 Contribuição

<p align="center">
Contribuições são bem-vindas!<br>
Fork → Branch → Commit → Push → Pull Request
</p>

---

## 💬 Contato

<p align="center">
Criador: <b>Diogo Teodoro </b><br>
GitHub: <a href="https://github.com/seuusuario">TheTekig</a><br>
E-mail: diogo.teodoro015@gmail.com
</p>
