musicas = [
    ("Música 1", "Rock"),
    ("Música 2", "Pop"),
    ("Música 3", "Jazz"),
    ("Música 4", "Rock"),
    ("Música 5", "Pop")
]

# Histórico de músicas ouvidas pelo usuário
historico_usuario = ["Rock", "Jazz", "Pop", "Jazz", "Pop"]

# Função para recomendar músicas
def recomendar_musica(historico):
    # Contar a frequência de cada gênero no histórico
    frequencia = {}
    for genero in historico:
        if genero in frequencia:
            frequencia[genero] += 1
        else:
            frequencia[genero] = 1

    # Encontrar o gênero mais frequente
    genero_mais_frequente = max(frequencia, key=frequencia.get)

    # Recomendar músicas desse gênero
    recomendacoes = []
    for titulo, genero in musicas:
        if genero == genero_mais_frequente:
            recomendacoes.append(titulo)
    return recomendacoes

# Obter recomendações para o usuário
    if recomendacoes_usuario = recomendar_musica(historico_usuario)
        print("Músicas recomendadas:", recomendacoes_usuario)
    