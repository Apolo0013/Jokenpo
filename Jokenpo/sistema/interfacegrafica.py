from tkinter import *
from time import sleep
from random import randint

#Aqui termos a interfacegrafica do jokenpo

class InterfaceGrafica():

    usuario = None # variavel que sera guardado a jogada do usuario
    ponto_usuario = 0
    ponto_pc = 0

    def __init__(self):
        self.Gui()


    def Gui(self): # Janela principal
        self.janela = Tk()
        
        self.janela.title('Começa')
        self.janela.geometry('800x500')
        self.janela.config(bg = '#B6EBDF')
        self.janela.iconphoto(False , PhotoImage(file=r'sistema\imagem\pedra.png'))
        
        #imagens
        self.imagem_start = PhotoImage(file=r'sistema\imagem\start.png') # Imagem de <a href="https://pixabay.com/pt/users/3rdmuffin-19978412/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=8870688">Lizzie</a> por <a href="https://pixabay.com/pt//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=8870688">Pixabay</a>

        #imagem do botao de voltar
        self.imagem_voltar = PhotoImage(file=r'sistema\imagem\voltar.png') # https://www.flaticon.com/br/icones-gratis/botao-voltar

        #imagem de pedra, papel e tesoura
        self.papel = PhotoImage(file=r'sistema\imagem\papel.png')
        self.pedra = PhotoImage(file=r'sistema\imagem\pedra.png')
        self.tesoura = PhotoImage(file=r'sistema\imagem\tesoura.png')

        self.lista_elementos = [self.pedra , self.papel , self.tesoura]

        self.botao_comecar = Button(self.janela , image=self.imagem_start , bg='#B6EBDF' , relief='flat', command=self.Carregandor)
        self.botao_comecar.place(x = 250 , y = 200)

        self.janela.mainloop()



    def recriar_janelaPri(self): # destruir os componetes da janela principal

        self.janela.title('Começa')
        self.janela.geometry('800x500')

        self.botao_comecar = Button(self.janela , image=self.imagem_start , bg='#B6EBDF' , relief='flat', command=self.Carregandor)
        self.botao_comecar.place(x = 250 , y = 200)


    def Carregandor(self): # Falso carregamento

        self.botao_comecar.destroy()
        self.carregandor = Label(self.janela , width=14 , height=1 , font = 'arial 30 bold' , relief='flat' , bg = '#B6EBDF')
        self.carregandor.place(x = 210 , y = 200)

        anima = 0 # responsavel pela aniamacao
        milis = randint(5 , 15) # quantos 500milisegundo vai durar

        for contador in range(1 , milis): #animcao
            print(f'{contador}  {milis}')
            if contador+1 == milis:
                self.carregandor['text'] = 'Pronto'
                self.carregandor.update()
                sleep(2)
            
            else:

                if anima == 0:
                    self.carregandor['text'] = 'Carregandor'

                elif anima == 1:
                    self.carregandor['text'] = 'Carregandor.'

                elif anima == 2:
                    self.carregandor['text'] = 'Carregandor..'

                else:
                    self.carregandor['text'] = 'Carregandor...'
                    anima = -1

                anima+=1
                self.carregandor.update()
                sleep(0.4)
                
        self.carregandor.destroy()
        self.escolhar()


    def escolhar(self): #Ondem o usuario vai escolher pedra, pepel e tesoura

        def voltar():
            self.frame_texto.destroy()
            self.freme_destaque.destroy()
            self.botao_voltar.destroy()
            self.label_orienta.destroy()
            self.pedra_botao.destroy()
            self.papel_botao.destroy()
            self.tesoura_botao.destroy()

            self.recriar_janelaPri()


        self.janela.title('Escolhar')
        self.janela.geometry('700x400')

        # o frame que ficaram exbaixo do texto pra destaca o mesmo
        self.frame_texto = Frame(self.janela , width = 700 , height=70 , bg = '#4D7373')
        self.frame_texto.place(x = 0 , y =5)

        # ja esse vai destaca os elementos do jogo
        self.freme_destaque = Frame(self.janela , width=700 , height = 230 , bg = '#92C0BE')
        self.freme_destaque.place(x = 0 , y =100)

        #botao de voltar pro menu
        self.botao_voltar = Button(self.janela , image = self.imagem_voltar , relief = 'flat' , bg = '#4D7373' , command = voltar)
        self.botao_voltar.place(x = 10 , y = 16)
        
        # orienta o mesmo pra escolhe uns do elementos
        self.label_orienta =Label(self.janela , bg = '#4D7373',fg = 'white' , text='Escolhar' , relief='flat' , font = 'arial 34 bold')
        self.label_orienta.place(x = 250 , y = 10)

        #pedra
        self.pedra_botao = Button(self.janela  , image=self.pedra , bg = '#92C0BE' , relief='flat' , command=self.Pedra)
        self.pedra_botao.place(x = 100 , y = 170)

        #papel
        self.papel_botao = Button(self.janela  , image=self.papel , bg = '#92C0BE' , relief='flat' , command=self.Papel)
        self.papel_botao.place(x = 275 , y = 130)

        #tesoura
        self.tesoura_botao = Button(self.janela  , image=self.tesoura , bg = '#92C0BE' , relief='flat' , command=self.Tesoura)
        self.tesoura_botao.place(x = 450 , y = 145)



    def recriar_escolhar(self): #recriação da janela 'escolhar'
        self.janela.config(bg = '#B6EBDF')

        self.frame_inferior.destroy()
        self.frame_nomes.destroy()
        self.x_label.destroy()
        self.label_pontoPlayer.destroy()
        self.label_pontoPC.destroy()
        self.label_pc.destroy()
        self.label_player.destroy()
        
        self.frame.destroy()
        self.ganhou.destroy()

        self.escolhar()
        
        self.janela.update()


    #Funcoes que vao da o valor da variavel(no caso a jogada): 'usuarios'

    def Pedra(self): # dando valor 0 a variavel 'usuario'
        self.usuario = 0
        self.Jogadas()


    def Papel(self):
        self.usuario = 1
        self.Jogadas()


    def Tesoura(self):
        self.usuario = 2
        self.Jogadas()


    def Jogadas(self): # janela que sera exbida o placa e a jogada do advesario

        #destruindo os componetes da janela escolhar
        self.tesoura_botao.destroy()
        self.pedra_botao.destroy() 
        self.papel_botao.destroy()
        self.frame_texto.destroy()
        self.label_orienta.destroy()
        self.freme_destaque.destroy()
        self.botao_voltar.destroy()


        def anima_esperar(): # Um Falso carregamento para exbir o resultado
            #jokenpô
            frame_esperar = Frame(self.janela , width = 700 , height = 180 , bg = '#4299B4')# frame para destacar o label de animação de esperar
            frame_esperar.place(x=0 , y = 100)

            espera_label = Label(self.janela , width=3 , height= 1 ,text = '' ,font='arial 110 bold' , relief='flat' , bg = '#4299B4' , anchor=CENTER) #label de esperar
            espera_label.place(x = 220 , y = 100)

            for contador in range(3):

                if contador == 0:
                    espera_label['text'] = 'jo'

                elif contador == 1:
                    espera_label['text'] = 'ken'

                else:
                    espera_label['text'] = 'pô'
                
                espera_label.update()# atualizar o label de esperar a cada 1s
                sleep(1)
            
            sleep(0.5)
            #destruido os mesmo
            frame_esperar.destroy()
            espera_label.destroy()
            self.janela.update()
            
        anima_esperar()

        self.janela.title('Jogando')

        # vermelho pc
        self.frame_vermelho = Frame(self.janela , width=350 , height= 450 , bg = '#F23030')
        self.frame_vermelho.place(x= 350 , y=0)        
        self.label_nameV = Label(self.janela , width = 2 , height = 1 ,text = 'PC' , fg = '#9B1F1F' , bg = '#F23030' , font = 'arial 60 bold')
        self.label_nameV.place(x = 480 ,y = 10)
        
        # azul usuario
        self.frame_azul = Frame(self.janela , width=350  , height = 450, bg = '#153BF8')
        self.frame_azul.place(x = 0 ,y = 0)
        self.label_nameA = Label(self.janela , width = 4 , height=1 , text = 'Você' , font = 'arial 60 bold' , fg = '#0E319B' , bg = '#153BF8')
        self.label_nameA.place(x = 55 ,y = 10) 

        #diviso entre o vermelho e azul
        self.frame_branco = Frame(self.janela , width=30  ,height=450 , bg = 'white')
        self.frame_branco.pack()

        #elementos do jokenpô
        self.jogadapc = randint(0,2) # jogada do pc

        self.jogada_player = Label(self.janela, image=self.lista_elementos[self.usuario] , bg = '#153BF8') # Jogada do player
        self.jogada_player.place(x = 90 , y = 160)

        self.jogada_pc = Label(self.janela , image=self.lista_elementos[self.jogadapc] , bg = '#F23030') # Jogada do pc
        self.jogada_pc.place(x = 460 , y = 160)

        self.janela.after(5000 ,self.Verificar)#verificar quem ganhou paeeeeee

    
    def Verificar(self):

        self.frame_azul.destroy()
        self.frame_branco.destroy()
        self.frame_vermelho.destroy()
        self.label_nameA.destroy()
        self.label_nameV.destroy()
        self.jogada_pc.destroy()
        self.jogada_player.destroy()


        if self.usuario == 1 and self.jogadapc == 0 or self.usuario == 0 and self.jogadapc == 2 or self.usuario == 2 and self.jogadapc == 1:
            resultado = 'Você Ganhou'
            cor_fundo = '#153BF8'
            cor_letra = 'black'
            self.ponto_usuario += 1

        elif self.jogadapc == 1 and self.usuario == 0 or self.jogadapc == 0 and self.usuario == 2 or self.usuario == 1 and self.jogadapc == 2:
            resultado = 'PC Ganhou'
            cor_fundo = '#F23030'
            cor_letra = 'black'
            self.ponto_pc += 1

        else:
            resultado = 'EMPARTE'
            cor_fundo = '#454545'
            cor_letra = 'white'

        self.janela.config(bg=cor_fundo)

        self.frame = Frame(self.janela)
        self.frame.pack(expand=True)
        self.ganhou = Label(self.frame , text = resultado ,  font= 'arial 80 bold' , bg = cor_fundo , fg = cor_letra)
        self.ganhou.pack(expand=True)
        self.janela.update()

        self.janela.after(3000 , self.Pontuação)


    def Pontuação(self): # janela que exbirar a pontuação
        self.frame.destroy()
        self.ganhou.destroy()

        self.janela.title('Pontuação')
        self.janela.config(bg = '#B6EBDF')

        #Frame que vai da destaque a os nome dos mesmo
        self.frame_nomes = Frame(self.janela , width=700 , height=120  ,bg ='#4A81E0')
        self.frame_nomes.place(x = 0 , y = 5)

        #frames de baixo pra deixa mais bonito
        self.frame_inferior = Frame(self.janela , width= 700 , height=80 , bg = '#4A81E0')
        self.frame_inferior.place(x = 0 , y= 330)

        # vermelho pc (pontuação)       
        self.label_pc = Label(self.janela , width = 2 , height = 1 ,text = 'PC' , fg = 'black' , bg = '#4A81E0' , font = 'arial 60 bold')
        self.label_pc.place(x = 480 ,y = 10)
        
        # azul usuario (pontuação)
        self.label_player = Label(self.janela , width = 4 , height=1 , text = 'Você' , font = 'arial 60 bold' , fg = 'black' , bg = '#4A81E0')
        self.label_player.place(x = 55 ,y = 10)

        #diviso dos valores
        self.x_label = Label(self.janela , width=1 , height = 1 , text = 'X' , font='arial 120 bold' , bg = '#B6EBDF')
        self.x_label.place(x = 296 , y = 130) # X que irar seperar as pontuação

        #labels com as pontuação em exbição

        # pontos do player
        self.label_pontoPlayer = Label(self.janela , width = 2 , height = 1  , text = self.ponto_usuario ,font = 'time 100 bold' , bg = '#B6EBDF' ,relief='flat')
        self.label_pontoPlayer.place(x = 55 ,y = 140)

        # ponto do pc
        self.label_pontoPC = Label(self.janela , width= 3 , height = 1 , text = self.ponto_pc , font = 'time 100 bold' , bg = '#B6EBDF' , relief = 'flat')
        self.label_pontoPC.place(x = 420 ,y = 140)

        self.janela.after(4000 , self.recriar_escolhar)



if __name__ == '__main__':
    InterfaceGrafica()
