# IMPORTAÇÕES DAS BIBLIOTECAS A SEREM UTILIZADAS
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import customtkinter as ctk 
from PIL import Image, ImageTk
import math
import sys

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuração da Janela Pricipal        
        self.title('MSA Engenharia e Tecnologia') #título da janela
        self.geometry('700x830') #dimensão da janela
        self.resizable(width=False, height=False) #redimensionar janela
        ctk.set_appearance_mode("system")  
        ctk.set_default_color_theme("dark-blue")

        # Configuração das Abas Superiores
        self.tabview = ctk.CTkTabview(master=self)
        self.tabview.pack(padx=5, pady=5)
        self.tabview.add("Inicial")  # add tab at the end        
        self.tabview.add("Dados Iniciais")  # add tab at the end
        self.tabview.add("Cálculos 1")  # add tab at the end
        self.tabview.add("Cálculos 2")  # add tab at the end
        self.tabview.add("Cálculos 3")  # add tab at the end
        self.tabview.set("Cálculos 3")  # set currently visible tab 

        ########################## FRAME 1 ########################## 
        frame1=ctk.CTkFrame(self.tabview.tab("Inicial"),
                      fg_color='#2E9AFE',
                      border_width=5,
                      border_color='white',
                      corner_radius=50,
                      width=500, 
                      height=500)
        frame1.pack(pady=15, padx=0)
         
        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame1, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com\n'
                    'Eng. Márcio Batista de Sá', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=30, padx=0)
        
        titulo1 = ctk.CTkLabel(master=frame1,
                      text="Dimensionamento de Estruturas em Concreto Armado\n"
                      "Vigas - Flexão Normal Simples\nConforme a NBR 6118:2014",
                      justify="center",                 
                      text_color='blue',
                      font=('arial narrow', 30, 'bold', 'italic'),                      
                      )
        titulo1.pack(pady=25, padx=10)
         
        img_viga = ctk.CTkImage(light_image=Image.open('img_viga.jpg'), 
        dark_image=Image.open('img_viga.jpg'), size=(400, 200))
        ctk.CTkLabel(master=frame1, text='', 
                    image=img_viga, 
                    compound='left', 
                    padx=10).pack(pady=25, padx=10)

        introdu = ctk.CTkLabel(master=frame1, 
                            text="Cálculo das Áreas de Aço das Armaduras\n"
                            "Seção Retangular - Armaduras Simples ou Duplas",                       
                            justify="center",                      
                            text_color='black',
                            font=('arial narrow', 25,'italic'),                      
                            )
        introdu.pack(pady=15, padx=10)  

        introdu1 = ctk.CTkLabel(master=frame1, 
                            text="Programa desenvolvido em Python com finalidade de produzir dimensionamento de Vigas em Concreto Armado.\n"
                                "Flexão Normal Simples - Baseado na Norma NBR 6118:2014.\n" 
                                "UTILIZAR APENAS PARA FINS ACADÊMICOS E ESTUDOS.",                       
                            justify="center",                      
                            text_color='#F7FE2E',
                            font=('arial narrow', 15,'italic'),                      
                            )
        introdu1.pack(pady=15, padx=10)        
        
        ########################## FRAME 2 ########################## 
        frame2=ctk.CTkFrame(self.tabview.tab("Dados Iniciais"),
                      fg_color='#1C1C1C',
                      border_width=5,
                      border_color='white',
                      corner_radius=50,
                      width=500, 
                      height=450)
        frame2.pack(padx=50, pady=10)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame2, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).grid(row=0, column=0, columnspan=3, pady=10)

        ########################## TÍTULO 2 ##########################
        titulo2 = ctk.CTkLabel(master=frame2,
                      text="2 - Dados Iniciais",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo2.grid(row=1, column=0, columnspan=2, pady=15) 

        ########################## MOMENTO Mk,máx ##########################
        momento_Mkmax = ctk.CTkLabel(master=frame2,
                      text="Momento Fletor Mk,máx (kN.m)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        momento_Mkmax.grid(row=2, column=0, padx=30, pady=15)

        n1 = ctk.DoubleVar()
        entry_momento_Mkmax = ctk.CTkEntry(master=frame2,
                       textvariable=n1,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_momento_Mkmax.grid(row=3, column=0, padx=30, pady=15)

        ########################## CORTANTE Vk,máx ##########################
        cortante_Vkmax = ctk.CTkLabel(master=frame2,
                      text="Força Cortante Vk,máx (kN)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        cortante_Vkmax.grid(row=2, column=1, padx=30, pady=15)

        n2 = ctk.DoubleVar()
        entry_cortante_Vkmax = ctk.CTkEntry(master=frame2,
                       textvariable=n2,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_cortante_Vkmax.grid(row=3, column=1, padx=30, pady=15)

        ########################## LARGURA bw ##########################
        larg_bw = ctk.CTkLabel(master=frame2,
                      text="Largura bw Viga (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        larg_bw.grid(row=4, column=0, padx=30, pady=15)

        n3 = ctk.DoubleVar()
        entry_larg_bw = ctk.CTkEntry(master=frame2,
                       textvariable=n3,                       
                       width=60,
                       height=30,                                             
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_larg_bw.grid(row=5, column=0, padx=30, pady=15)

        ########################## ALTURA h ##########################
        altura_h = ctk.CTkLabel(master=frame2,
                      text="Altura h Viga (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        altura_h.grid(row=4, column=1, padx=30, pady=15)

        n4 = ctk.DoubleVar()
        entry_altura_h = ctk.CTkEntry(master=frame2,
                       textvariable=n4,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_altura_h.grid(row=5, column=1, padx=30, pady=15)

        ########################## CONCRETO fck ##########################
        classe_fck = ctk.CTkLabel(master=frame2,
                      text="Concreto fck (MPa)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        classe_fck.grid(row=6, column=0, padx=30, pady=15)

        n5 = ctk.DoubleVar()
        entry_classe_fck = ctk.CTkEntry(master=frame2,
                       textvariable=n5,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_classe_fck.grid(row=7, column=0, padx=30, pady=15)

        ########################## AÇO fyk ##########################
        arma_fyk = ctk.CTkLabel(master=frame2,
                      text="Aço Armadura fyk (MPa)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        arma_fyk.grid(row=6, column=1, padx=30, pady=15)

        n6 = ctk.DoubleVar()
        entry_arma_fyk = ctk.CTkEntry(master=frame2,
                       textvariable=n6,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_arma_fyk.grid(row=7, column=1, padx=30, pady=15)    

        ########################## ALTURA ÚTIL d ##########################
        util_d = ctk.CTkLabel(master=frame2,
                      text="Altura Útil d (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        util_d.grid(row=8, column=0, padx=30, pady=15, columnspan=2) 

        n8 = ctk.DoubleVar()
        entry_util_d = ctk.CTkEntry(master=frame2,
                       textvariable=n8,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_util_d.grid(row=9, column=0, padx=30, pady=15, columnspan=2)

        ########################## TÍTULO 3 ##########################
        info = ctk.CTkLabel(master=frame2,
                      text="Obrigatório inserir todos os dados\n"
                      "Observar com atenção as unidades indicadas",
                      justify="center", 
                      text_color='red',
                      font=('arial narrow', 16, 'italic')                      
                      )
        info.grid(row=11, column=0, columnspan=2, pady=15)
       
        ########################## FRAME 3 ##########################
        frame3=ctk.CTkFrame(self.tabview.tab("Cálculos 1"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame3.pack(padx=10, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame3, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10)

        ########################## FUNÇÃO CALCULAR ##########################
        def calcular():        
            # Pegando os dados do usuário                         
            num_Mkmax = float(entry_momento_Mkmax.get()) 
            num_vk = float(entry_cortante_Vkmax.get())  
            num_bw = float(entry_larg_bw.get()) 
            num_d = float(entry_util_d.get())
            num_fck = float(entry_classe_fck.get())
            num_fyk = float(entry_arma_fyk.get())
            num_h = float(entry_altura_h.get())
            fcd = (num_fck/10)/(1.4)
            fyd = (num_fyk/10)/(1.15)  

            # Cálculo do Md        
            Md = round(num_Mkmax *1.4*100,2)
            resul_Md.configure(text=f"Md = {Md} kN.cm")
            
            # Cálculo da Posição da Linha Neutra (X)
            try:
             X = 1.25*num_d*(1-math.sqrt(1-(Md/(0.425*num_bw*num_d**2*fcd))))
            except ValueError:
                messagebox.showerror("Erro", "POR FAVOR, REVEJA SEUS DADOS DE PROJETO E CALCULE NOVAMENTE.")
                #sys.exit()

            except ZeroDivisionError:
                messagebox.showerror("Erro", "POR FAVOR, REVEJA SEUS DADOS DE PROJETO E CALCULE NOVAMENTE.")
                #sys.exit()

            except ArithmeticError:
                messagebox.showerror("Erro", "POR FAVOR, REVEJA SEUS DADOS DE PROJETO E CALCULE NOVAMENTE.")
                #sys.exit()       
            
            verifi_x.configure(text=f"X = {round(X,1)} cm")            
         
            if num_fck <= 50:                  
                    if float(X/num_d) <= 0.45:
                        verifi_045.configure(text=f"Verificação (x/d<0.45) Armadura Simples {round(X/num_d,2)} < 0.45 ")
                    else:
                        verifi_045.configure(text=f"x/d={round(X/num_d,2)} > 0.45\n" 
                                             "Adotar Armadura Dupla ou Rever Projeto")
            else:
                    if float(X/num_d) <= 0.35:
                        verifi_045.configure(text=f"Verificação (x/d<0.35) Armadura Simples {round(X/num_d,2)} < 0.35 ")
                    else:
                        verifi_045.configure(text=f"x/d={round(X/num_d,2)} > 0.45\n" 
                                             "Adotar Armadura Dupla ou Rever Projeto")                  

            # Cálculo dos Limtes X2lim e X3lim (Domínios 2 e 3)
            X2lim = round(num_d*0.26,2)
            X3lim = round(num_d*0.63,2)
            resul_X2lim.configure(text=f"Limite Domínio 2: X2lim = {X2lim} cm")
            resul_X3lim.configure(text=f"Limite Domínio 3: X3lim = {X3lim} cm")
            
            # Cálculo da Área de Aço (As)           
            As = Md/(fyd*(num_d-0.4*X))       
            resul_As.configure(text=f"Armadura Longitudinal As = {round(As,1)} cm2") 

            # Cálculo da Área Mínima de Aço (As,min)
            if num_fck <=30:
                 Asmin = (0.15*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2") 
            elif num_fck ==35:
                 Asmin = (0.164*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2") 
            elif num_fck ==40:
                 Asmin = (0.179*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")
            elif num_fck ==45:
                 Asmin = (0.179*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")
            elif num_fck ==50:
                 Asmin = (0.208*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")
            elif num_fck ==55:
                 Asmin = (0.211*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")
            elif num_fck ==60:
                 Asmin = (0.219*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")
            elif num_fck ==65:
                 Asmin = (0.226*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")
            elif num_fck >= 66:
                 Asmin = (0.245*num_bw*num_h)/100
                 resul_Asmin.configure(text=f"As,min = {round(Asmin,1)} cm2")

            else:
                 resul_Asmin.configure(text=f"REVER fck")

            if X/num_d >= 0.46:                               
                # Armadura Dupla X = 0.45*d
                X1 = 0.45*num_d
                dupla_X.configure(text=f"X = {round(X1,1)} cm")

                # M1d
                M1d = 0.68*num_bw*X1*fcd*(num_d-0.4*X1)
                dupla_M1d.configure(text=f"M1d = {round(M1d,1)} kN.cm")

                # M2d
                M2d = Md - M1d
                dupla_M2d.configure(text=f"M2d = {round(M2d,1)} kN.cm")

                # Cálculo da Área de Aço (As1)           
                As1 = M1d/(fyd*(num_d-0.4*X1))       
                resul_As1.configure(text=f"Armadura Longitudinal As1 = {round(As1,1)} cm2")

                # Cálculo da Área de Aço (As2)           
                As2 = M2d/(fyd*(num_d-3))       
                resul_As2.configure(text=f"Armadura Longitudinal As2 = {round(As2,1)} cm2")

            else:
                dupla_X.configure(text=f"Projetado com Armadura Simples")
                dupla_M1d.configure(text=f"Projetado com Armadura Simples")
                dupla_M2d.configure(text=f"Projetado com Armadura Simples")
                resul_As1.configure(text=f"Projetado com Armadura Simples")
                resul_As2.configure(text=f"Projetado com Armadura Simples")

            # Armadura de Pele Asp (Para h >= 60 cm)
            if num_h >= 60:                 
             Asp = (0.05*num_bw*num_h)/100
             resul_Asp.configure(text=f"As,pele/face vertical = {round(Asp,1)} cm2")
            else:
             resul_Asp.configure(text=f"Não Aplicável neste projeto")

            # Cálculo da Cortante Vsd
            Vsd = round(1.4*num_vk,1)
            resul_vsd.configure(text=f"Vsd = {round(Vsd,1)} kN")

            # Cálculo da Cortante Resistente VRd2
            if num_fck ==20:
                 VRd2 = 0.35*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN") 
            elif num_fck ==25:
                 VRd2 = 0.43*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            elif num_fck ==30:
                 VRd2 = 0.51*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN") 
            elif num_fck ==35:
                 VRd2 = 0.58*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")  
            elif num_fck ==40:
                 VRd2 = 0.65*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            elif num_fck ==45:
                 VRd2 = 0.71*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN") 
            elif num_fck ==50:
                 VRd2 = 0.77*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            elif 55 <= num_fck <=90:
                 VRd2 = 0.77*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            else:
                 resul_biela.configure(text=f"REVER fck")

            # Verificação da Compressão nas Bielas
            if Vsd <= VRd2: 
                verifi_biela.configure(text=f"OK! não ocorrerá esmagamento das bielas de concreto") 
            else: 
                verifi_biela.configure(text=f"Vsd={round(Vsd,1)} > VRd2={round(VRd2,1)}\n Rever Projeto!")

            # Cálculo do Vsd,min            
            if num_fck ==20:
                 Vsdmin = 0.101*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN") 
            elif num_fck ==25:
                 Vsdmin = 0.117*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            elif num_fck ==30:
                 Vsdmin = 0.132*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN") 
            elif num_fck ==35:
                 Vsdmin = 0.147*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")  
            elif num_fck ==40:
                 Vsdmin = 0.160*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            elif num_fck ==45:
                 Vsdmin = 0.173*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN") 
            elif num_fck ==50:
                 Vsdmin = 0.186*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            elif 55 <= num_fck <=90:
                 Vsdmin = 0.186*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            else:
                 resul_vsdmin.configure(text=f"REVER fck")

            # Verificação do Vsd,min (Armadura Transversal)
            if Vsd <= Vsdmin: 
                verifi_vsdmin.configure(text=f"OK! Adotar Armadura Transversal Mínima") 
            else: 
                verifi_vsdmin.configure(text=f"Vsd={round(Vsd,1)} > Vsdmin={round(Vsdmin,1)}\n Calcular Armadura Transversal!")

            # Cálculo do Asw            
            if num_fck ==20:
                 Asw = (2.55*(Vsd/num_d))-(0.17*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m") 
            elif num_fck ==25:
                 Asw = (2.55*(Vsd/num_d))-(0.20*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==30:
                 Asw = (2.55*(Vsd/num_d))-(0.22*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==35:
                 Asw = (2.55*(Vsd/num_d))-(0.25*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")  
            elif num_fck ==40:
                 Asw = (2.55*(Vsd/num_d))-(0.27*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==45:
                 Asw = (2.55*(Vsd/num_d))-(0.29*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==50:
                 Asw = (2.55*(Vsd/num_d))-(0.31*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif 55 <= num_fck <=90:
                 Asw = (2.55*(Vsd/num_d))-(0.31*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            else:
                 resul_Asw.configure(text=f"REVER fck")

            # Cálculo do Asw,min
            fctm = round(0.3*(math.cbrt(num_fck**2)),2)
            Aswmin = ((20*(fctm/10))/(num_fyk/10))*num_bw
            resul_Aswmin.configure(text=f"Asw,min = {round(Aswmin,2)} cm2/m")
            
        # Botão Confirmar
        button = ctk.CTkButton(master=frame3,
                           text='CALCULAR',
                           font=('Arial', 15),
                           width=100,
                           height=50,
                           fg_color='blue',
                           command=calcular)
        button.pack(pady=10)   

        ########################## CÁLCULO DO Md ##########################
        titulo3 = ctk.CTkLabel(master=frame3,
                      text="3 - Momento Fletor de Cálculo (Md)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo3.pack(padx=150, pady=10)

        resul_Md = ctk.CTkLabel(master=frame3,
                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Md.pack(pady=10)
      
        ########################## CÁLCULO DO X ##########################
        titulo4 = ctk.CTkLabel(master=frame3,
                      text="4 - Posição da Linha Neutra - Domínios (X)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo4.pack(padx=150, pady=10)  

        viga = ctk.CTkImage(light_image=Image.open('viga.jpg'), 
                            dark_image=Image.open('viga.jpg'), 
                            size=(350, 250))
        ctk.CTkLabel(master=frame3, 
                    text='', 
                    image=viga, 
                    compound='left', 
                    padx=10).pack(pady=0, padx=0)     

        resul_X2lim = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_X2lim.pack(pady=10)

        resul_X3lim = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_X3lim.pack(pady=10)

        ########################## VERIFICAÇÃO X ##########################
        verifi_x = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_x.pack(pady=10)

        verifi_045 = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_045.pack(pady=10)        

        ########################## FRAME 4 ##########################
        frame4=ctk.CTkFrame(self.tabview.tab("Cálculos 2"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame4.pack(padx=10, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame4, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10, padx=0)   

        ########################## CÁLCULO DA ÁREA DE AÇO AS ########################## 
        titulo5 = ctk.CTkLabel(master=frame4,
                      text="5 - Área de Aço (As)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo5.pack(padx=150, pady=10)

        resul_As = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As.pack(pady=10)

        ########################## CÁLCULO DE AS MÍNIMA ##########################
        titulo6 = ctk.CTkLabel(master=frame4,
                      text="6 - Área de Aço Mínima (As,min)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo6.pack(padx=150, pady=10)

        resul_Asmin = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Asmin.pack(pady=10)
        
        ########################## ARMADURA DUPLA ##########################
        titulo7= ctk.CTkLabel(master=frame4,
                      text="7 - Armadura Dupla",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo7.pack(padx=150, pady=10)

        dupla_X = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        dupla_X.pack(pady=10)

        dupla_M1d = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        dupla_M1d.pack(pady=10)

        dupla_M2d = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        dupla_M2d.pack(pady=10)

        resul_As1 = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As1.pack(pady=10)

        resul_As2 = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As2.pack(pady=10)

        ########################## ARMADURA DE PELE ##########################
        titulo8 = ctk.CTkLabel(master=frame4,
                      text="8 - Armadura de Pele (h >= 60 cm)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')
                      )
        titulo8.pack(padx=150, pady=10)

        resul_Asp = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Asp.pack(pady=10)

        ########################## FRAME 5 ##########################
        frame5=ctk.CTkFrame(self.tabview.tab("Cálculos 3"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame5.pack(padx=0, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame5, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10, padx=0)  
        
        ########################## CÁLCULO DA Vsd ########################## 
        titulo5 = ctk.CTkLabel(master=frame5,
                      text="9 - Cálculo da Força Cortante de Cálculo (Vsd)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo5.pack(padx=150, pady=10)

        resul_vsd = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_vsd.pack(pady=10)

        ########################## VERIFICAÇÃO DA BIELA ########################## 
        titulo6 = ctk.CTkLabel(master=frame5,
                      text="10 - Verificação da Compressão nas Bielas",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo6.pack(padx=150, pady=10)

        resul_biela = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_biela.pack(pady=10)

        verifi_biela = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_biela.pack(pady=10)

        ########################## CÁLCULO DA Vsd,min ########################## 
        titulo7 = ctk.CTkLabel(master=frame5,
                      text="11 - Cálculo da F. C. Solicitante Mínima (Vsd,min)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo7.pack(padx=150, pady=10)

        resul_vsdmin = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_vsdmin.pack(pady=10)

        verifi_vsdmin = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_vsdmin.pack(pady=10)

        ########################## CÁLCULO DA Asw ########################## 
        titulo8 = ctk.CTkLabel(master=frame5,
                      text="12 - Cálculo Área Aço Armadura Transversal (Asw)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo8.pack(padx=150, pady=10)

        resul_Asw = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Asw.pack(pady=10)

        ########################## CÁLCULO DA Asw,min ########################## 
        titulo9 = ctk.CTkLabel(master=frame5,
                      text="13 - Cálculo Armadura Transversal Mínima (Asw,min)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo9.pack(padx=150, pady=10)

        resul_Aswmin = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Aswmin.pack(pady=10)

      
if __name__ == "__main__":
    app = App()
    app.mainloop()

