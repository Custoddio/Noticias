import requests
from bs4 import BeautifulSoup
import textwrap
import tkinter as tk
from tkinter import ttk

def fetch_news(url, css_selector):
    """
    Função para buscar notícias de um site específico.
    """
    try:
        headers = { 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        # Faz a requisição HTTP para o site
               
        response = requests.get(url, headers=headers)
        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.select(css_selector)
        return [headline.get_text(strip=True) for headline in headlines[:1000]]
    except Exception as e:
        return [f"Erro ao buscar notícias: {url}: {e}"]
                
                

def display_news():
    """Exibe as notícias na interface gráfica."""
    # Limpa as tabelas antes de inserir novos dados
    for table in [buscape_table, acoes_table, ibovespa_table]:
        for row in table.get_children():
            table.delete(row)

    # Busca as notícias
    news = get_all_news()

    # Insere as notícias em cada tabela
    for idx, buscape_news in enumerate(news[0], start=1):
        buscape_table.insert("", "end", values=(idx, textwrap.shorten(buscape_news, width=250, placeholder="...")))
    for idx, acoes_news in enumerate(news[1], start=1):
        acoes_table.insert("", "end", values=(idx, textwrap.shorten(acoes_news, width=250, placeholder="...")))
    for idx, ibovespa_news in enumerate(news[2], start=1):
        ibovespa_table.insert("", "end", values=(idx, textwrap.shorten(ibovespa_news, width=250, placeholder="...")))


def get_all_news():
    """Busca notícias de Alterosa Esporte, Globo.com e Band"""
    # Busca notícias de cada site
    buscape_news = fetch_news("https://www.buscape.com.br/cupom-de-desconto", "div")
    acoes_news = fetch_news("https://statusinvest.com.br/acoes", "div")
    ibovespa_news = fetch_news("https://statusinvest.com.br/indices/ibovespa", "div")

    # Retorna as notícias separadamente
    return [buscape_news, acoes_news, ibovespa_news]


# Configuração da interface gráfica
root = tk.Tk() 
root.title("Resumo de Notícias")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Tabela para exibir as notícias da ESPN
buscape_label = ttk.Label(frame, text="BUSCAPE", font=("Arial", 14, "bold"))
buscape_label.grid(row=0, column=0, pady=5)
buscape_table = ttk.Treeview(frame, columns=("#", "Notícia"), show="headings", height=10)
buscape_table.heading("#", text="#")
buscape_table.heading("Notícia", text="Notícia")
buscape_table.column("#", width=30, anchor="center")
buscape_table.column("Notícia", width=900)
buscape_table.grid(row=1, column=0, pady=10)

# Tabela para exibir as notícias da Globo.com
acoes_label = ttk.Label(frame, text="NUCELA", font=("Arial", 14, "bold"))
acoes_label.grid(row=2, column=0, pady=5)
acoes_table = ttk.Treeview(frame, columns=("#", "Notícia"), show="headings", height=10)
acoes_table.heading("#", text="#")
acoes_table.heading("Notícia", text="Notícia")
acoes_table.column("#", width=30, anchor="center")
acoes_table.column("Notícia", width=900)
acoes_table.grid(row=3, column=0, pady=10)

# Tabela para exibir as notícias da Band
ibovespa_label = ttk.Label(frame, text="FEBRABAN", font=("Arial", 14, "bold"))
ibovespa_label.grid(row=4, column=0, pady=5)
ibovespa_table = ttk.Treeview(frame, columns=("#", "Notícia"), show="headings", height=10)
ibovespa_table.heading("#", text="#")
ibovespa_table.heading("Notícia", text="Notícia")
ibovespa_table.column("#", width=30, anchor="center")
ibovespa_table.column("Notícia", width=900)
ibovespa_table.grid(row=5, column=0, pady=10)

# Botão para atualizar as notícias
refresh_button = ttk.Button(frame, text="Atualizar Notícias", command=display_news)
refresh_button.grid(row=6, column=0, pady=10)

# Inicia a interface
root.mainloop()