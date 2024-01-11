#ib: Hashtag Programação
# Passo a passo do projeto


import pyautogui # RPA == automação
    #clicar        -> pyautogui.click --> (x, y, *button, *clicks)
    #escrever      -> pyautogui.write
    #apertar tecla -> pyautogui.press
    #atalho        -> pyautogui.hotkey
    #scroll(roalr) -> pyautogui.scroll --> (n) se n>0, scroll up, se n<0, pra baixo 
import time
import pandas 
# Passo 1 - Entrar no sistema da Empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    #bibliotecas 
pyautogui.PAUSE = 0.5 #tempo de 1s de espera em cada comando pyautogui
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = "pythonimpressionador@gmail.com"
senha = "sua senha"
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2 - fazer login
time.sleep(2)
pyautogui.click(x=683, y=538)
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")

# Passo 3 - Importar base de dados
time.sleep(2)
tabela = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=764, y=390)
    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write((tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    #cadastrar
    pyautogui.press("enter")
    #rolar pra cima
    pyautogui.scroll(5000)
    time.sleep(1)


# Passo 5 - Repetir isso até acabar a base de dados
# for da linha 39