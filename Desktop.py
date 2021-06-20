import os
from datetime import *
from time import strftime
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

janela = Tk()
janela.title('Desktop v2.0.3')
janela.iconbitmap('desktop.ico')
janela.resizable(False, False)
janela.config(bg='#C87D2B')

titulo = Label(janela, text='Aplicações Instaladas'.upper(), bg='#C87D2B', fg='#000000',
               font=('Arial serif', 20, 'bold'))
titulo.pack()

tempo = str(date.today())
data = tempo[8:10], tempo[5:7], tempo[0:4]

dia = Label(janela, text=data, bg='#C87D2B', fg='#ffffff', font=('Arial serif', 12, 'normal'))
dia.pack()


def relogio():
    agora = strftime('%H:%M:%S')
    if hora['text'] != agora:
        hora['text'] = agora
    hora.after(100, relogio)


hora = Label(janela, text='', bg='#C87D2B', fg='#ffffff', font=('Arial serif', 12, 'normal'))
hora.pack()

import time

espera = time.sleep


# Métodos para configuração do sistema

def desligar_s():
    desliga = messagebox.askquestion('Desligar', 'Esta opção irá encerrar o Computador\n\n\tDeseja Continuar?')
    if desliga == messagebox.YES:
        os.system('shutdown /p')


def reiniciar_s():
    reinicia = messagebox.askquestion('Reiniciar', 'Esta opção irá reiniciar o Computador\n\n\tDeseja Continuar?')
    if reinicia == messagebox.YES:
        os.system('shutdown -r')


def hibernar_s():
    hiberna = messagebox.askquestion('Hibernar', 'Seu Computador será Hibernado\n\n\tDeseja continuar?')
    if hiberna == messagebox.YES:
        os.system('shutdown -h')


def sair_s():
    sai = messagebox.askquestion('Sair', 'Sair da aplicação?')
    if sai == messagebox.YES:
        janela.destroy()
    else:
        pass


sistema = Frame(janela, bg='#C87D2B')
sistema.pack()

# Criação dos botões de configuração do sistema

bg_desligar = '#171717'

desligar = Button(sistema, text='Desligar', border=0, bg=bg_desligar, fg='white', font=('sans-serif', 10, 'normal'),
                  cursor='hand2', width=16, command=desligar_s)
desligar.grid(row=0, column=0, padx=5, pady=5)

reiniciar = Button(sistema, text='Reiniciar', border=0, bg=bg_desligar, fg='white', font=('sans-serif', 10, 'normal'),
                   cursor='hand2', width=16, command=reiniciar_s)
reiniciar.grid(row=0, column=1, padx=5, pady=5)

hibernar = Button(sistema, text='Hibernar', border=0, bg=bg_desligar, fg='white', font=('sans-serif', 10, 'normal'),
                  cursor='hand2', width=16, command=hibernar_s)
hibernar.grid(row=0, column=2, padx=5, pady=5)

sair = Button(sistema, text='Sair', border=0, fg='white', bg='red2', font=('sans-serif', 12, 'bold'), cursor='hand2',
              width=16, command=sair_s)
sair.grid(row=0, column=3, padx=10, pady=5)

frame = Frame(janela, bg='#C87D2B')
frame.pack()

# Inicialização das variáveis auxiliares
linha = 1
coluna = 0
altura = 0
linhaspan = 3
ficheiro = ''


# Instrução para carregar o ficheiro de texto ao inicializar a aplicação
def carregar_app():
    abrir_enderecos = open('Enderecos.txt', 'r')
    abrir_nomes = open('nomes.txt', 'r')

    lista_nomes = []
    contador = 0

    for nomes in abrir_nomes:

        lista_nomes.append(nomes)

    for files in abrir_enderecos:
        adicionar_botao(lista_nomes[contador], files)
        contador += 1
    print('Executando...\n')


nome_app = ''
endereco_app = ''
removed = FALSE


# Método para criação do botão da aplicação
def adicionar_botao(text, outro):
    global linha, coluna, altura, linhaspan, botao

    alterado = text.replace('_', ' ').replace('64', '').replace('32', '').replace('-', ' ').replace('.exe', '').replace(
        '.lnk', '')

    # Criação do método para iniciar a aplicação
    def abrir_app():
        global coluna, botao, nome_app, endereco_app, removed, frame
        try:
            if removed == FALSE:
                os.startfile(outro.replace('\n', ''))
                removed = FALSE
                print(removed)
            elif removed == TRUE:
                remov = remover_app(text, outro)
                if remov:
                    messagebox.showinfo('Remoção', 'Aplicação removida com sucesso...')
                    removed = FALSE
                    print(removed)
                    messagebox.showwarning('Atualização', 'A aplicação irá encerrar para fazer atualizações')
                    reinicio()
                else:
                    messagebox.showerror('Falha', 'Falha ao remover aplicação')
                print(removed)

        except FileNotFoundError:
            excluir = messagebox.askquestion('Aplicação removida',
                                             'Essa aplicação foi removida ou o seu endereço foi alterado\n'
                                             '\tDeseja excluir esse botão?')
            if excluir == messagebox.YES:
                remov = remover_app(text, outro)
                if remov:
                    messagebox.showinfo('Feito', 'Aplicação removida com sucesso...')
                    messagebox.showwarning('Atualização', 'A aplicação irá encerrar para fazer atualizações')
                    reinicio()
                else:
                    messagebox.showerror('Falha', 'Falha ao remover aplicação')
            else:
                pass

    botao = Button(frame, bg='#12247A', textvariable=outro, fg='#ffffff', font=('sans-serif', 12, 'normal'),
                   width=16, height=2, cursor='hand2', text=alterado, border=0, command=abrir_app)
    botao.grid(row=linha, column=coluna, padx=2, pady=5)

    # Código que verifica se o tamanho do nome do arquivo é maior e adiciona largura do botão
    if len(text) > 10:
        botao.configure(font=('sans-serif', 9, 'normal'), width=20, height=3, justify='center')
    elif len(text) > 15:
        botao.configure(font=('sans-serif', 4, 'normal'), width=22, height=6, justify='center')

    coluna += 1
    if coluna > 3:
        linha += 1
        coluna = 0
        altura += 2
        linhaspan += 4
        adicionar.config(height=altura)
        adicionar.grid(rowspan=linhaspan)


# Método que adiciona o caminho da aplicação no botão
def adicionar_App():
    global linha, coluna, arquivo, ficheiro, altura, linhaspan
    arquivo = filedialog.askopenfilename(title='Adicionar App', initialdir='C://Desktop', filetypes=(
        ('Aplicações', '*.exe'), ('Todos ficheiros', '*.*')))

    nome = os.path.basename(arquivo).lower()
    caminho = nome.replace(".exe", "").replace('_', ' ').replace('.lnk', '').upper()

    if nome != '' and len(nome) > 2 and (nome.endswith('.exe') or nome.endswith('.lnk')):

        # Instrução que adiciona o caminho da aplicação no ficheiro de texto
        ficheiro = open('Enderecos.txt', 'a')
        ficheiro.writelines(arquivo + '\n')

        adicionar_botao(caminho, arquivo)

        nome_app = open('nomes.txt', 'a')
        nome_app.writelines(caminho + '\n')

        ficheiro.close()
        nome_app.close()

        excluir_app(arquivo)

    else:
        pass


# Método que remove um botão e a sua aplicação
def remover_app(nome, caminho):
    global nome_app, endereco_app
    ler_nomes = open('nomes.txt', 'r')
    ler_enderecos = open('Enderecos.txt', 'r')

    nome_app, endereco_app = nome, caminho

    enderecos = []
    nomes = []

    for itens in ler_enderecos:
        if itens == caminho:
            caminho = ''
            continue
        else:
            enderecos.append(itens)

    for files in ler_nomes:
        if files == nome:
            nome = ''
            continue
        else:
            nomes.append(files)

    ler_enderecos.close()
    ler_nomes.close()

    abrir_enderecos = open('Enderecos.txt', 'w')
    abrir_nomes = open('nomes.txt', 'w')
    print(100 * '*')

    for i in enderecos:
        abrir_enderecos.writelines(i)

    for j in nomes:
        abrir_nomes.writelines(j)
        print(j)

    abrir_nomes.close()
    abrir_enderecos.close()
    return 'LSoft'


# Continuação do método de cima
def escolher_app():
    global nome_app, endereco_app, removed

    # if nome_app == '' and endereco_app == '':
    if removed == FALSE:
        messagebox.showwarning('Excluir', 'Click no botão para excluir')
        remover_app(nome_app, endereco_app)
        nome_app = ''
        endereco_app = ''
        removed = TRUE
        remover.configure(text='Cancelar')
        adicionar.configure(state=DISABLED)
    elif removed == TRUE:
        removed = FALSE
        messagebox.showinfo('Cancelar', 'Remoção cancelada com sucesso')
        remover.configure(text='Remover app')
        adicionar.configure(state=NORMAL)


# Método que faz o reinício do sistema após remover uma aplicação
def reinicio():
    carregar_app()
    remover.configure(text='Remover app')
    adicionar.configure(state=NORMAL)
    # quit(0)


apagar = FALSE


# Método que elimina a aplicação do Ambiente de Trabalho após ser adicionada no sistema
def excluir_app(aplicacao):
    global apagar, arquivo
    caminho = os.path.basename(aplicacao)
    opcao = 'C:\\Users\\User\\Desktop\\'
    if caminho.endswith('.lnk') or caminho.endswith('.exe'):
        execucao = os.system(f'del "{opcao}{caminho}'.replace('.exe', '.lnk') + '"')
        apagar = TRUE
        if execucao:
            print('Eliminado com sucesso...')
            print(aplicacao)
            print(execucao)
            print('Caminho: ', caminho)
            apagar = FALSE
        else:
            print('Erro ao eliminar app!')
            print('Aplicação:', aplicacao)
            print(execucao)
            apagar = FALSE
    else:
        print('Essa não é uma aplicação do tipo .lnk')
    print('Caminho:', caminho)


adicionar = Button(frame, bg='#000000', text='Adicionar', font=('Arial', 18, 'normal'), fg='#ffffff',
                   command=adicionar_App, border=0)
adicionar.config(cursor='hand2', width=15, height=9, justify='center')
adicionar.grid(row=1, column=4, padx=2, pady=2, rowspan=3)

remover = Button(sistema, text='Remover app', border=0, fg='#ffffff', bg='#000000', font=('sans-serif', 12, 'normal'),
                 cursor='hand2', width=23, command=escolher_app)
remover.grid(row=0, column=4, padx=2, pady=20)

if __name__ == '__main__':
    open('Enderecos.txt', 'a')
    open('nomes.txt', 'a')
    carregar_app()
    relogio()
    janela.mainloop()
