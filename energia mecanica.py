from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import warnings
import math


warnings.filterwarnings("ignore")


################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co4 = "#403d3d"   # letra
co7 = "#3fbfb9"   # verde


colors = ['#5588bb','#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']



valor = [0, 0, 0]

text1 = 'ENERGIA MECÂNCIA                   '
text2 = 'ENERGIA POTENCIAL                  '
text3 = 'ENERGIA CINÉTICA                   '

lista_meses = ['CINÉTICA', 'POTENCIAL', 'MECÂNICA']


lista_valores = [0,0,0]

Energia_Mecanica = 0



janela = Tk()
janela.title("Energia Mecanica")
janela.geometry('750x700')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

frameCimaLeft =  Frame(janela, width = 400,  height = 350, bg = co1, highlightbackground=co0, highlightthickness=1)
frameCimaLeft.place(x=0, y=0)

frameCimaRight =  Frame(janela, width = 350,  height = 350, bg = co1, highlightbackground=co0, highlightthickness=1)
frameCimaRight.place(x=399, y=0)

frameBaixoLeft =  Frame(janela, width = 400,  height = 350, bg = co2, highlightbackground=co0, highlightthickness=1)
frameBaixoLeft.place(x=0, y=350)

frameBaixoRight =  Frame(janela, width = 350,  height = 350, bg = co1, highlightbackground=co0, highlightthickness=1)
frameBaixoRight.place(x=400, y=350)






def energia_mecanica_ponto_A():
    global valor, text1, text2, text3
    global lista_valores, lista_meses, Energia_Mecanica, Massa, lista_valores_A, valor_A


    if ponto_A_altura_Entrada.get() =='':
        messagebox.showerror('Erro', 'Preencha todos os campos')
        return
    
    if ponto_A_velociade_Entrada.get()=='':
        messagebox.showerror('Erro', 'Preencha todos os campos')
        return
    if massa_Entrada.get() =='':
        messagebox.showerror('Erro', 'Preencha todos os campos')
        return

    

    
    
    altura = float(ponto_A_altura_Entrada.get())
    velocidade = float(ponto_A_velociade_Entrada.get())
    Massa = float(massa_Entrada.get())

    

    Energia_Potencial_A = Massa*10*altura
    Energia_Cinetica_A = (Massa*math.pow(velocidade,2))/2
    Energia_Mecanica = Energia_Potencial_A + Energia_Cinetica_A

    
    lista_valores_A = [Energia_Cinetica_A, Energia_Potencial_A,  Energia_Mecanica]
    valor_A =[Energia_Mecanica, Energia_Potencial_A, Energia_Cinetica_A]
    
    

    
    lista_valores=[Energia_Cinetica_A, Energia_Potencial_A,  Energia_Mecanica]
    valor=[Energia_Mecanica, Energia_Potencial_A, Energia_Cinetica_A]
    lista_meses = ['CINÉTICA A','POTENCIAL A', 'MECÂNICA A']

    text1 = 'ENERGIA MECÂNCIA PONTO A                 '
    text2 = 'ENERGIA POTENCIAL PONTO A                 '                
    text3 = 'ENERGIA CINÉTICA PONTO A                 '            
                

    

    
    ponto_A_altura_Entrada.delete(0, 'end')
    ponto_A_velociade_Entrada.delete(0, 'end')
    massa_Entrada.delete(0, 'end')

    grafico_bar()
    resumo()
    
    

def energia_mecanica_pontos():
    global valor, text1, text2, text3
    global lista_valores, lista_meses, Energia_Mecanica
    nome=pontos_caixa.get()

    if Energia_Mecanica==0:
        return   

    if nome=='Ponto A':
        
        
        lista_valores=lista_valores_A
        valor=valor_A
        lista_meses = ['CINÉTICA A','POTENCIAL A', 'MECÂNICA A']

        text1 = 'ENERGIA MECÂNCIA PONTO A                 '
        text2 = 'ENERGIA POTENCIAL PONTO A                 '                
        text3 = 'ENERGIA CINÉTICA PONTO A                 '

        grafico_bar()
        resumo()
        pontos_altura_Entrada.delete(0, 'end')
        pontos_caixa.set('')
        return

    

    if pontos_altura_Entrada.get()=='':
        messagebox.showerror('Erro', 'Preencha todos os campos')
        return
    if nome =='':
        messagebox.showerror('Erro', 'ESCOLHA UM PONTO:')
        return
    
    altura = float(pontos_altura_Entrada.get())
    Energia_Mecanica_controle = Massa*10*altura

    if Energia_Mecanica_controle>Energia_Mecanica:
        messagebox.showerror('Erro', 'ALTURA EXCEDE O QUE É FISICAMENTE POSSÍVEL!!!')
        return
    
    

    if nome=='Ponto B':
        Energia_Potencial_B = Massa*10*altura
        Energia_Cinetica_B = Energia_Mecanica-Energia_Potencial_B
        
        lista_valores=[Energia_Cinetica_B, Energia_Potencial_B,  Energia_Mecanica]
        valor=[Energia_Mecanica, Energia_Potencial_B, Energia_Cinetica_B]
        lista_meses = ['CINÉTICA B','POTENCIAL B', 'MECÂNICA B']

        text1 = 'ENERGIA MECÂNCIA PONTO B                 '
        text2 = 'ENERGIA POTENCIAL PONTO B                 '                
        text3 = 'ENERGIA CINÉTICA PONTO B                 '

        grafico_bar()
        resumo()

    if nome=='Ponto C':
        Energia_Potencial_C = Massa*10*altura
        Energia_Cinetica_C = Energia_Mecanica - Energia_Potencial_C
        
        lista_valores=[Energia_Cinetica_C, Energia_Potencial_C,  Energia_Mecanica]
        valor=[Energia_Mecanica, Energia_Potencial_C, Energia_Cinetica_C]
        lista_meses = ['CINÉTICA C','POTENCIAL C', 'MECÂNICA C']

        text1 = 'ENERGIA MECÂNCIA PONTO C                 '
        text2 = 'ENERGIA POTENCIAL PONTO C                 '                
        text3 = 'ENERGIA CINÉTICA PONTO C                 '


        grafico_bar()
        resumo()

    if nome=='Ponto D':
        Energia_Potencial_D = Massa*10*altura
        Energia_Cinetica_D = Energia_Mecanica - Energia_Potencial_D
        
        lista_valores=[Energia_Cinetica_D, Energia_Potencial_D,  Energia_Mecanica]
        valor=[Energia_Mecanica, Energia_Potencial_D, Energia_Cinetica_D]
        lista_meses = ['CINÉTICA D','POTENCIAL D', 'MECÂNICA D']

        text1 = 'ENERGIA MECÂNCIA PONTO D                 '
        text2 = 'ENERGIA POTENCIAL PONTO D                 '                
        text3 = 'ENERGIA CINÉTICA PONTO D                 '

        grafico_bar()
        resumo()

    pontos_altura_Entrada.delete(0, 'end')
    pontos_caixa.set('')
        
        

    
    


def grafico_bar():
    figura = plt.Figure(figsize=(6.3, 5.3), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)
    ax.bar(lista_meses, lista_valores,  color=colors, width=0.8)
    

    # create a list to collect the plt.patches data
    c = 0

    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=20, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')

        c += 1
    ax.set_xticklabels(lista_meses,fontsize=15)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    #ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameBaixoLeft)
    canva.get_tk_widget().place(x=3, y=20)








def resumo():
    
    l_linha = Label(frameBaixoRight, text="", width=260, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=5, y=54)
    l_sumario = Label(frameBaixoRight, text=text1.upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=5, y=35)
    l_sumario = Label(frameBaixoRight, text='{:,.1f}'.format(valor[0])+' Joules', height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=5, y=70)

    l_linha = Label(frameBaixoRight, text="", width=260, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=5, y=134)
    l_sumario = Label(frameBaixoRight, text=text2.upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=5, y=115)
    l_sumario = Label(frameBaixoRight, text='{:,.1f}'.format(valor[1])+' Joules',height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=5, y=150)

    l_linha = Label(frameBaixoRight, text="", width=260, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=5, y=209)
    l_sumario = Label(frameBaixoRight, text=text3.upper(), height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=5, y=190)
    l_sumario = Label(frameBaixoRight, text='{:,.1f}'.format(valor[2])+' Joules', height=1,anchor=NW, font=('arial 17 '), bg=co1, fg='#545454')
    l_sumario.place(x=5, y=220)



######################## frameCimaRight  ###############################


app_img  = Image.open('carrinho.png')
app_img = app_img.resize((349, 349))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCimaRight, image=app_img, text=" ")

app_logo.place(x=0, y=0)










####################  frameCimaLeft      #############################

ponto_A_Label = Label(frameCimaLeft, text="Massa, Altura e Velocidade Ponto A: ", height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
ponto_A_Label.place(x=5, y=10)
ponto_A_altura_Entrada = Entry(frameCimaLeft, justify='left',relief="solid")
ponto_A_altura_Entrada.place(x=5, y=45, width=35, height= 25)
metros_Label = Label(frameCimaLeft, text="Metros", height=1,anchor=NW, font=('Verdana 8'), bg=co1, fg=co4)
metros_Label.place(x=40, y=45)


ponto_A_velociade_Entrada = Entry(frameCimaLeft, justify='left',relief="solid")
ponto_A_velociade_Entrada.place(x=100, y=45, width=35, height= 25)
m_s_Label = Label(frameCimaLeft, text="M/S", height=1,anchor=NW, font=('Verdana 8'), bg=co1, fg=co4)
m_s_Label.place(x=135, y=45)


massa_Entrada = Entry(frameCimaLeft, justify='left',relief="solid")
massa_Entrada.place(x=190, y=45, width=35, height= 25)
massa_Label = Label(frameCimaLeft, text="Kg", height=1,anchor=NW, font=('Verdana 8'), bg=co1, fg=co4)
massa_Label.place(x=225, y=45)

botao_aplicar_ponto_A = Button(frameCimaLeft, command=energia_mecanica_ponto_A,text=" APLICAR ",  font=('Verdana 9 bold'),overrelief=SOLID, bg=co7, fg=co0 )
botao_aplicar_ponto_A.place(x=260, y=45)

l_linha = Label(frameCimaLeft, text="", width=350, height=1,anchor=NW, font=('arial 1 '), bg='#545454',)
l_linha.place(x=5, y=85)




pontos_Label = Label(frameCimaLeft, text="Altura dos Pontos: ", height=1,anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
pontos_Label.place(x=5, y=150)

pontos_caixa = ttk.Combobox(frameCimaLeft, width=7,font=('Ivy 10'))
pontos_caixa['values'] = ['Ponto A', 'Ponto B', 'Ponto C', 'Ponto D']
pontos_caixa.place(x=5, y=180)

pontos_altura_Entrada = Entry(frameCimaLeft, justify='left',relief="solid")
pontos_altura_Entrada.place(x=100, y=180, width=35, height= 23)

m_s_pontos_Label = Label(frameCimaLeft, text="Metros", height=1,anchor=NW, font=('Verdana 8'), bg=co1, fg=co4)
m_s_pontos_Label.place(x=135, y=180)

botao_aplicar_pontos = Button(frameCimaLeft, command=energia_mecanica_pontos,text=" APLICAR ",  font=('Verdana 9 bold'),overrelief=SOLID, bg=co7, fg=co0 )
botao_aplicar_pontos.place(x=205, y=180)






grafico_bar()
resumo()

















