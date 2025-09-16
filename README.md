# Pokédex Pessoal 🕹️

Um aplicativo interativo desenvolvido em **Streamlit** que permite **cadastrar, listar, atualizar e deletar Pokémons**.  
Você pode adicionar manualmente as informações ou buscar automaticamente os dados oficiais através da **PokéAPI**.

---

## 🚀 Funcionalidades

- **Cadastrar Pokémon**  
  - Manualmente (inserindo código, nome, tipo, nível, HP e ataque).  
  - Automaticamente via **PokéAPI**, apenas informando o nome.  

- **Listar Pokémon**  
  - Exibe todos os Pokémons cadastrados, com imagem, código, nome, tipo, nível, HP e ataque.  

- **Atualizar Pokémon**  
  - Permite editar os dados de um Pokémon já cadastrado.  

- **Deletar Pokémon**  
  - Remove um Pokémon do sistema pelo seu código.  

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) → Interface gráfica web  
- [Requests](https://docs.python-requests.org/) → Consumo da PokéAPI  
- [PokéAPI](https://pokeapi.co/) → Fonte oficial de dados dos Pokémons  

---

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/pokedex-streamlit.git
cd pokedex-streamlit
pip install -r requirements.txt
