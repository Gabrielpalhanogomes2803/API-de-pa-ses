import requests
import tkinter as tk
from tkinter import ttk, scrolledtext

# URL da API com os campos necessários
URL_ALL = "https://restcountries.com/v3.1/all?fields=name,capital,currencies,languages,region,population,cca2"
PAISES_CACHE = None  # cache global para não fazer múltiplas requisições

# -----------------------------
# FUNÇÕES PRINCIPAIS
# -----------------------------
def carregar_paises():
    """Carrega a lista de países da API (uma única vez)."""
    global PAISES_CACHE
    if PAISES_CACHE is not None:
        return PAISES_CACHE
    try:
        resp = requests.get(URL_ALL, timeout=10)
        resp.raise_for_status()
        PAISES_CACHE = resp.json()
        return PAISES_CACHE
    except Exception as e:
        print("Erro ao consultar API:", e)
        return None

def buscar_paises(filtro):
    """Filtra países cujo nome contém a string 'filtro' (case-insensitive)."""
    filtro = filtro.lower()
    todos = carregar_paises()
    if not todos:
        return []
    resultados = []
    for pais in todos:
        nome = pais.get("name", {}).get("common", "").lower()
        if filtro in nome:
            resultados.append(pais)
    return resultados

# -----------------------------
# FUNÇÕES DE AÇÃO PARA BOTÕES
# -----------------------------
def validar_entrada():
    termo = entrada.get().strip()
    if not termo:
        saida.delete(1.0, tk.END)
        saida.insert(tk.END, "⚠ Digite algo para pesquisar.\n")
        return None
    return termo

def bot_listar():
    termo = validar_entrada()
    if not termo:
        return
    resultados = buscar_paises(termo)
    saida.delete(1.0, tk.END)
    if not resultados:
        saida.insert(tk.END, "Nenhum país encontrado.\n")
        return
    for p in resultados:
        nome = p.get("name", {}).get("common", "Sem nome")
        saida.insert(tk.END, f"{nome}\n")

def bot_capital():
    termo = validar_entrada()
    if not termo:
        return
    resultados = buscar_paises(termo)
    saida.delete(1.0, tk.END)
    if not resultados:
        saida.insert(tk.END, "Nenhum país encontrado.\n")
        return
    for p in resultados:
        nome = p.get("name", {}).get("common", "Sem nome")
        capital_lista = p.get("capital")
        capital = capital_lista[0] if capital_lista else "Não encontrada"
        saida.insert(tk.END, f"{nome} → Capital: {capital}\n")


def bot_moeda():
    termo = validar_entrada()
    if not termo:
        return
    resultados = buscar_paises(termo)
    saida.delete(1.0, tk.END)
    if not resultados:
        saida.insert(tk.END, "Nenhum país encontrado.\n")
        return
    for p in resultados:
        nome = p.get("name", {}).get("common", "Sem nome")
        moedas = p.get("currencies", {})
        moedas_format = ", ".join([f"{k}-{v.get('name','?')}" for k,v in moedas.items()]) if moedas else "Não encontrada"
        saida.insert(tk.END, f"{nome} → Moeda(s): {moedas_format}\n")

def bot_idioma():
    termo = validar_entrada()
    if not termo:
        return
    resultados = buscar_paises(termo)
    saida.delete(1.0, tk.END)
    if not resultados:
        saida.insert(tk.END, "Nenhum país encontrado.\n")
        return
    for p in resultados:
        nome = p.get("name", {}).get("common", "Sem nome")
        idiomas = p.get("languages", {})
        idiomas_format = ", ".join(idiomas.values()) if idiomas else "Não encontrado"
        saida.insert(tk.END, f"{nome} → Idioma(s): {idiomas_format}\n")

def bot_contar():
    termo = validar_entrada()
    if not termo:
        return
    resultados = buscar_paises(termo)
    saida.delete(1.0, tk.END)
    saida.insert(tk.END, f"Quantidade de países encontrados: {len(resultados)}\n")

# -----------------------------
# INTERFACE TKINTER
# -----------------------------
janela = tk.Tk()
janela.title("Sistema de Consulta de Países")
janela.geometry("720x520")

tk.Label(janela, text="Digite parte do nome do país:").pack(pady=5)
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

frame = tk.Frame(janela)
frame.pack(pady=10)

ttk.Button(frame, text="Listar Países", command=bot_listar).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame, text="Capitais", command=bot_capital).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="Moedas", command=bot_moeda).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame, text="Idiomas", command=bot_idioma).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame, text="Contar Países", command=bot_contar).grid(row=2, column=0, columnspan=2, pady=5)

saida = scrolledtext.ScrolledText(janela, width=85, height=20)
saida.pack(pady=10)

janela.mainloop()
