import streamlit as st
import requests

st.image("https://i.pinimg.com/originals/81/13/79/811379a19dbc300e4ef19f851fd8ca05.gif", use_container_width=True)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #0C118A, #5F66FA, #8287FF);
        color: #000000;
    }
        st.title {
        color: white;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

if "pokedex" not in st.session_state:
    st.session_state.pokedex = {}

    st.title("Pokédex Pessoal")
    st.divider()

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg", 
    use_container_width=True
)
menu = st.sidebar.radio("Menu", ["Cadastrar Pokémon", "Listar Pokémon", "Atualizar Pokémon", "Deletar Pokémon"])

if menu == "Cadastrar Pokémon":
    st.subheader("Cadastrar novo Pokémon")

    with st.form("form_cadastro"):
        nome = st.text_input("Nome do Pokémon (ex: pikachu)")
        usar_api = st.checkbox("Buscar dados automaticamente na PokéAPI")
        cadastrar = st.form_submit_button("Cadastrar")

        if cadastrar:
            if usar_api:

                url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
                resposta = requests.get(url)
                
                if resposta.status_code == 200:
                    dados = resposta.json()
                    tipos = [i["type"]["name"].capitalize() for i in dados["types"]]

                    pokemon = {
                        "codigo": dados["id"],
                        "nome": dados["name"].capitalize(),
                        "tipo": ", ".join(tipos),
                        "nivel": 1,
                        "hp": dados["stats"][0]["base_stat"],
                        "ataque": dados["stats"][1]["base_stat"],
                        "imagem": dados["sprites"]["front_default"]
                    }

                    st.session_state.pokedex[pokemon["codigo"]] = pokemon
                    st.success(f"Pokémon {pokemon['nome']} cadastrado com sucesso pela API!")
                else:
                    st.error("Pokémon não encontrado na PokéAPI.")
            else:
                codigo = st.number_input("Código", min_value=1, step=1)
                tipo = st.text_input("Tipo")
                nivel = st.number_input("Nível", min_value=1, step=1)
                hp = st.number_input("HP", min_value=1, step=1)
                ataque = st.number_input("Ataque", min_value=1, step=1)

                if codigo in st.session_state.pokedex:
                    st.warning("Já existe um Pokémon com esse código!")
                else:
                    st.session_state.pokedex[codigo] = {
                        "codigo": codigo,
                        "nome": nome,
                        "tipo": tipo,
                        "nivel": nivel,
                        "hp": hp,
                        "ataque": ataque
                    }
                    st.success(f"Pokémon {nome} cadastrado manualmente com sucesso!")

elif menu == "Listar Pokémon":
    st.subheader("Lista de Pokémons")
    if st.session_state.pokedex:
        for pk in st.session_state.pokedex.values():
            st.image(pk.get("imagem", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"), width=100)
            st.write(f"**Código:** {pk['codigo']}")
            st.write(f"Nome: {pk['nome']}")
            st.write(f"Tipo: {pk['tipo']}")
            st.write(f"Nível: {pk['nivel']}")
            st.write(f"HP: {pk['hp']}")
            st.write(f"Ataque: {pk['ataque']}")
            st.divider()
    else:
        st.info("Nenhum Pokémon cadastrado ainda.")

elif menu == "Atualizar Pokémon":
    st.subheader("Atualizar Pokémon")
    codigo = st.number_input("Digite o código do Pokémon", min_value=1, step=1)

    if codigo in st.session_state.pokedex:
        pokemon = st.session_state.pokedex[codigo]

        with st.form("form_update"):
            nome = st.text_input("Nome", value=pokemon["nome"])
            tipo = st.text_input("Tipo", value=pokemon["tipo"])
            nivel = st.number_input("Nível", value=pokemon["nivel"], step=1)
            hp = st.number_input("HP", value=pokemon["hp"], step=1)
            ataque = st.number_input("Ataque", value=pokemon["ataque"], step=1)
            atualizar = st.form_submit_button("Salvar alterações")

            if atualizar:
                st.session_state.pokedex[codigo] = {
                    "codigo": codigo,
                    "nome": nome,
                    "tipo": tipo,
                    "nivel": nivel,
                    "hp": hp,
                    "ataque": ataque,
                    "imagem": pokemon.get("imagem", None)
                }
                st.success("Pokémon atualizado com sucesso!")
    else:
        st.info("Informe um código válido para atualizar.")

elif menu == "Deletar Pokémon":
    st.subheader("Deletar Pokémon")
    codigo = st.number_input("Digite o código do Pokémon para deletar", min_value=1, step=1)
    if st.button("Deletar"):
        if codigo in st.session_state.pokedex:
            del st.session_state.pokedex[codigo]
            st.success("Pokémon deletado com sucesso!")
        else:
            st.error("Código não encontrado!")
