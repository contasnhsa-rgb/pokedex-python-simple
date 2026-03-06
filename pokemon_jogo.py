print("Pokemon! Temos que pegá-los, eu sei!")

def adicionar_pokemon(nome, número, tipo, altura, peso, habilidades, fraquezas, evoluções, descrição):
    pokemon = {
        "nome": nome,
        "número": número,
        "tipo": tipo,
        "altura": altura,
        "peso": peso,
        "habilidades": habilidades,
        "fraquezas": fraquezas,
        "evoluções": evoluções,
        "descrição": descrição
    }

    return pokemon


Pikachu = adicionar_pokemon(
    "Pikachu",
    25,
    "Elétrico",
    "0.4 m",
    "6 kg",
    "Static",
    "Terra",
    "Raichu",
    "Um Pokémon elétrico que armazena energia em suas bochechas."
)

Charmander = adicionar_pokemon(
    "Charmander",
    4,
    "Fogo",
    "0.6 m",
    "8.5 kg",
    "Blaze",
    "Água, Terra, Rocha",
    "Charmeleon → Charizard",
    "Um Pokémon de tipo Fogo que é o parceiro inicial de muitos treinadores."
)

Squirtle = adicionar_pokemon(
    "Squirtle",
    7,
    "Água",
    "0.5 m",
    "9 kg",
    "Torrent",
    "Fogo, Elétrico",
    "Wartortle → Blastoise",
    "Um Pokémon de tipo Água que é o parceiro inicial de muitos treinadores."
)

Bulbasaur = adicionar_pokemon(
    "Bulbasaur",
    1,
    "Planta",
    "0.7 m",
    "6.9 kg",
    "Overgrow",
    "Fogo, Gelo, Psíquico, Voador",
    "Ivysaur → Venusaur",
    "Um Pokémon de tipo Planta que é o parceiro inicial de muitos treinadores."
)

Snorlax = adicionar_pokemon(
    "Snorlax",
    143,
    "Normal",
    "2.1 m",
    "460 kg",
    "Immunity",
    "Lutador",
    "Munchlax → Snorlax",
    "Passa a maior parte do tempo dormindo e só acorda para comer."
)

Gengar = adicionar_pokemon(
    "Gengar",
    94,
    "Fantasma, Venenoso",
    "1.5 m",
    "40.5 kg",
    "Cursed Body",
    "Fantasma, Psíquico, Sombrio",
    "Gastly → Haunter → Gengar",
    "Se esconde nas sombras e gosta de assustar pessoas."
)

Eevee = adicionar_pokemon(
    "Eevee",
    133,
    "Normal",
    "0.3 m",
    "6.5 kg",
    "Run Away, Adaptability",
    "Lutador",
    "Vaporeon → Jolteon → Flareon → Espeon → Umbreon → Leafeon → Glaceon → Sylveon",
    "Um Pokémon muito leal e que pode evoluir para várias formas diferentes."
)

Jigglypuff = adicionar_pokemon(
    "Jigglypuff",
    39,
    "Fada",
    "0.5 m",
    "5.5 kg",
    "Cute Charm",
    "Venenoso, Aço",
    "Wigglytuff",
    "Canta uma música que faz qualquer um dormir."
)

Meowth = adicionar_pokemon(
    "Meowth",
    52,
    "Normal",
    "0.4 m",
    "4.2 kg",
    "Pickup, Technician",
    "Lutador",
    "Persian",
    "Sofre constantemente com dores de cabeça misteriosas."
)

Psyduck = adicionar_pokemon(
    "Psyduck",
    54,
    "Água",
    "0.8 m",
    "19.6 kg",
    "Damp, Cloud Nine",
    "Gelo, Elétrico",
    "Golduck",
    "Sofre constantemente com dores de cabeça misteriosas."
)

pokedex = []
pokedex.append(Pikachu)
pokedex.append(Snorlax)
pokedex.append(Gengar)
pokedex.append(Eevee)
pokedex.append(Jigglypuff)
pokedex.append(Meowth)
pokedex.append(Psyduck)
pokedex.append(Charmander)
pokedex.append(Squirtle)
pokedex.append(Bulbasaur)

import random

while True:
    print("\n===== MINI POKÉDEX =====")
    print("1 - Mostrar todos os Pokémon")
    print("2 - Pokémon aleatório")
    print("3 - Digite o número do Pokémon para detalhes")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        for pokemon in pokedex:
            print(f"Nome: {pokemon['nome']}")
            print(f"Número: {pokemon['número']}")
            print(f"Tipo: {pokemon['tipo']}")
            print(f"Altura: {pokemon['altura']}")
            print(f"Peso: {pokemon['peso']}")
            print(f"Habilidades: {pokemon['habilidades']}")
            print(f"Fraquezas: {pokemon['fraquezas']}")
            print(f"Evoluções: {pokemon['evoluções']}")
            print(f"Descrição: {pokemon['descrição']}")
            print("=============================")

    elif escolha == "2":
        pokemon_aleatorio = random.choice(pokedex)
        print(f"Nome: {pokemon_aleatorio['nome']}")
        print(f"Número: {pokemon_aleatorio['número']}")
        print(f"Tipo: {pokemon_aleatorio['tipo']}")
        print(f"Altura: {pokemon_aleatorio['altura']}")
        print(f"Peso: {pokemon_aleatorio['peso']}")
        print(f"Habilidades: {pokemon_aleatorio['habilidades']}")
        print(f"Fraquezas: {pokemon_aleatorio['fraquezas']}")
        print(f"Evoluções: {pokemon_aleatorio['evoluções']}")
        print(f"Descrição: {pokemon_aleatorio['descrição']}")

    elif escolha == "3":
        numero_pokemon = input("Digite o número do Pokémon: ")
        encontrado = False
        for pokemon in pokedex:
            if str(pokemon['número']) == numero_pokemon:
                print(f"Nome: {pokemon['nome']}")
                print(f"Número: {pokemon['número']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Altura: {pokemon['altura']}")
                print(f"Peso: {pokemon['peso']}")
                print(f"Habilidades: {pokemon['habilidades']}")
                print(f"Fraquezas: {pokemon['fraquezas']}")
                print(f"Evoluções: {pokemon['evoluções']}")
                print(f"Descrição: {pokemon['descrição']}")
                encontrado = True
                break
        if not encontrado:
            print("Pokémon não encontrado. Tente novamente.")
    
    elif escolha == "4":
        print("Obrigado por usar a Pokédex! Até a próxima!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        