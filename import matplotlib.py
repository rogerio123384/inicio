import matplotlib.pyplot as plt

# Dados organizados do maior para o menor (melhora a leitura formal)
dados = {
    'Funk': 25,
    'Samba': 20,
    'Sertanejo': 18,
    'Pagode': 15,
    'MPB': 10,
    'Rock Nacional': 7,
    'Outros': 5
}

categorias = list(dados.keys())
valores = list(dados.values())

# Paleta de cores sóbria (tons de azul e cinza profissional)
cores = ['#1a4a73', '#2469a5', '#3288bd', '#66c2a5', '#99d594', '#e6f598', '#d3d3d3']

# Criando a figura
plt.figure(figsize=(12, 7), facecolor='#ffffff')

# Gráfico de Rosca (Donut Chart) com estilo limpo
wedges, texts, autotexts = plt.pie(
    valores, 
    labels=categorias, 
    colors=cores, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.82,
    explode=[0.05 if i == 0 else 0 for i in range(len(categorias))], # Destaca levemente o líder
    wedgeprops={'width': 0.3, 'edgecolor': 'white', 'linewidth': 2}
)

# Estilização das fontes
plt.setp(texts, size=11, weight="bold", color="#333333")
plt.setp(autotexts, size=10, color="white", weight="bold")

# Título formal e subtítulo
plt.title('ANÁLISE DE MARKET SHARE: GÊNEROS MUSICAIS', fontsize=16, pad=20, weight='bold', color='#2c3e50')
plt.text(0, -1.2, 'Fonte: Dados de Mercado (Fictícios) | Período: 2026', ha='center', fontsize=9, color='gray')

# Ajuste final
plt.axis('equal')
plt.tight_layout()
plt.show()