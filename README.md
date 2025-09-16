Pokédex Pessoal 🕹️

Um aplicativo interativo desenvolvido em Streamlit que permite cadastrar, listar, atualizar e deletar Pokémons.
Você pode adicionar manualmente as informações ou buscar automaticamente os dados oficiais através da PokéAPI.

🚀 Funcionalidades

Cadastrar Pokémon

Manualmente (inserindo código, nome, tipo, nível, HP e ataque).

Automaticamente via PokéAPI, apenas informando o nome.

Listar Pokémon

Exibe todos os Pokémons cadastrados, com imagem, código, nome, tipo, nível, HP e ataque.

Atualizar Pokémon

Permite editar os dados de um Pokémon já cadastrado.

Deletar Pokémon

Remove um Pokémon do sistema pelo seu código.

🛠️ Tecnologias Utilizadas

Python 3.11+

Streamlit
 → Interface gráfica web.

Requests
 → Consumo da PokéAPI.

PokéAPI
 → Fonte oficial de dados dos Pokémons.

📦 Instalação

Clone o repositório e instale as dependências:

git clone https://github.com/seu-usuario/pokedex-streamlit.git
cd pokedex-streamlit
pip install -r requirements.txt

▶️ Como Executar

No terminal, execute:

streamlit run Pokemon.py


O aplicativo será aberto no navegador em:
👉 http://localhost:8501

📂 Estrutura do Projeto
├── Pokemon.py          # Código principal do app Streamlit
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação

📸 Demonstração

Tela inicial com GIF animado e menu lateral.

Cadastro de Pokémon via PokéAPI.

Listagem dos Pokémons cadastrados.

Atualização e exclusão de registros.

🧾 Requisitos

Dependências principais (extraídas de requirements.txt):

streamlit==1.49.1

requests==2.32.5

pandas==2.3.2

numpy==2.3.3

Para a lista completa, consulte o arquivo requirements.txt
.

📜 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
Pokémon © é uma marca registrada da Nintendo, Game Freak e Creatures.
