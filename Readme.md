

# Resumo de Notícias

Este projeto é uma aplicação Python que busca notícias de diferentes fontes da web e as exibe em uma interface gráfica. Ele utiliza as bibliotecas `requests` e `BeautifulSoup` para buscar e processar os dados da web, e `tkinter` para criar a interface gráfica.

---

## **Funcionalidades**

- Busca notícias de três fontes:
  - **Buscapé**: Notícias relacionadas a cupons de desconto.
  - **Status Invest (Ações)**: Notícias sobre ações.
  - **Status Invest (Ibovespa)**: Notícias sobre o índice Ibovespa.
- Exibe as notícias em tabelas separadas na interface gráfica.
- Limita o texto das notícias a 250 caracteres para facilitar a visualização.
- Permite atualizar as notícias com o clique de um botão.

---

## **Requisitos**

Certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:

- `requests`
- `beautifulsoup4`

Para instalar as dependências, execute:
```bash
pip install requests beautifulsoup4
```

---

## **Como executar**

1. Certifique-se de que você tem o Python instalado (versão 3.6 ou superior).
2. Salve o código em um arquivo chamado `app.py`.
3. Execute o arquivo no terminal:
   ```bash
   python app.py
   ```
4. A interface gráfica será exibida, mostrando as notícias de cada fonte em tabelas separadas.

---

## **Estrutura do Código**

### **1. Função `fetch_news(url, css_selector)`**
Busca notícias de um site específico usando o URL e um seletor CSS.

- **Parâmetros:**
  - `url`: O endereço do site.
  - `css_selector`: O seletor CSS para localizar os elementos desejados.
- **Retorno:**
  - Uma lista de manchetes (limitada a 1000 itens).

### **2. Função `get_all_news()`**
Busca notícias de três fontes diferentes e organiza os resultados.

- **Fontes:**
  - Buscapé: `https://www.buscape.com.br/cupom-de-desconto`
  - Status Invest (Ações): `https://statusinvest.com.br/acoes`
  - Status Invest (Ibovespa): `https://statusinvest.com.br/indices/ibovespa`
- **Retorno:**
  - Uma lista contendo as notícias de cada fonte.

### **3. Função `display_news()`**
Exibe as notícias na interface gráfica.

- Limpa as tabelas antes de inserir novos dados.
- Insere as notícias em tabelas separadas, limitando o texto a 250 caracteres.

### **4. Interface Gráfica**
- **Biblioteca usada:** `tkinter`
- **Componentes:**
  - Três tabelas (`Treeview`) para exibir as notícias de cada fonte.
  - Um botão para atualizar as notícias.

---

## **Interface Gráfica**

A interface gráfica é composta por:

1. **Tabelas:**
   - **Buscapé:** Exibe notícias relacionadas a cupons de desconto.
   - **Nuclea:** Exibe notícias sobre ações.
   - **Febraban:** Exibe notícias sobre o índice Ibovespa.

2. **Botão de Atualização:**
   - Atualiza as notícias exibidas nas tabelas.

---

## **Exemplo de Saída**

### **Tabela 1: Buscapé**
| #   | Notícia                              |
|-----|--------------------------------------|
| 1   | Cupom de desconto para eletrônicos...|
| 2   | Promoção de final de ano no Buscapé...|

### **Tabela 2: Nuclea**
| #   | Notícia                              |
|-----|--------------------------------------|
| 1   | Ações da empresa X sobem 10%...      |
| 2   | Mercado financeiro fecha em alta... |

### **Tabela 3: Febraban**
| #   | Notícia                              |
|-----|--------------------------------------|
| 1   | Ibovespa registra queda de 2%...     |
| 2   | Expectativas para o mercado em 2025...|

---

## **Possíveis Melhorias**

1. **Adicionar mais fontes de notícias:**
   - Expandir o código para buscar notícias de outros sites.

2. **Interface Web:**
   - Migrar a interface gráfica para uma aplicação web usando Flask ou Django.

3. **Tratamento de Erros:**
   - Melhorar o tratamento de erros para lidar com problemas de conexão ou mudanças na estrutura dos sites.

4. **Estilo da Interface:**
   - Melhorar o design da interface gráfica com bibliotecas como `ttkbootstrap`.

---

## **Licença**

Este projeto é de uso livre e pode ser modificado conforme necessário.

---

