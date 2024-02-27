from customtkinter import *
from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image


class Funcs:
    def theme_color(self):
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light ="#F0F0F0"
        self.black = "#000000"
    def limpar_cadastro_paciente(self):
        self.entry_nome_cadastro_paciente.delete(0, END)
        self.entry_cpf_cadastro_paciente.delete(0, END)
        self.entry_nascimento_cadastro_paciente.delete(0, END)
        self.entry_cep_cadastro_paciente.delete(0, END)
        self.entry_endereco_cadastro_paciente.delete(0, END)
        self.entry_numero_cadastro_paciente.delete(0, END)
        self.entry_bairro_cadastro_paciente.delete(0, END)
        self.entry_cidade_cadastro_paciente.delete(0, END)
        self.entry_estado_cadastro_paciente.delete(0, END)
        self.entry_email_cadastro_paciente.delete(0, END)
        self.entry_telefone_cadastro_paciente.delete(0, END)
        self.entry_celular_cadastro_paciente.delete(0, END)
        self.entry_obervacao_cadastro_paciente.delete(0, END)
    def limpar_cadastro_medico(self):
        self.entry_nome_cadastro_medico.delete(0, END)
        self.entry_especialidade1_cadastro_medico.delete(0, END)
        self.entry_especialidade2_cadastro_medico.delete(0, END)
        self.entry_crm_cadastro_medico.delete(0, END)
        self.entry_cpf_cadastro_medico.delete(0, END)
        self.entry_email_cadastro_medico.delete(0, END)
        self.entry_telefone_cadastro_medico.delete(0, END)
        self.entry_celular_cadastro_medico.delete(0, END)
        self.entry_obervacao_cadastro_medico.delete(0, END)
    def get_cadastro_paciente(self):
        self.nome_cadastro_paciente = self.entry_nome_cadastro_paciente.get()
        self.cpf_cadastro_paciente = self.entry_cpf_cadastro_paciente.get()
        self.nascimento_cadastro_paciente = self.entry_nascimento_cadastro_paciente.get()
        self.cep_cadastro_paciente = self.entry_cep_cadastro_paciente.get()
        self.endereco_cadastro_paciente = self.entry_endereco_cadastro_paciente.get()
        self.numero_cadastro_paciente = self.entry_numero_cadastro_paciente.get()
        self.bairro_cadastro_paciente = self.entry_bairro_cadastro_paciente.get()
        self.cidade_cadastro_paciente = self.entry_cidade_cadastro_paciente.get()
        self.estado_cadastro_paciente = self.entry_estado_cadastro_paciente.get()
        self.email_cadastro_paciente = self.entry_email_cadastro_paciente.get()
        self.telefone_cadastro_paciente = self.entry_telefone_cadastro_paciente.get()
        self.celular_cadastro_paciente = self.entry_celular_cadastro_paciente.get()
        self.obervacao_cadastro_paciente = self.entry_obervacao_cadastro_paciente.get()
    def get_cadastro_medico(self):
        self.nome_cadastro_medico = self.entry_nome_cadastro_medico.get()
        self.especialidade1_cadastro_medico = self.entry_especialidade1_cadastro_medico.get()
        self.especialidade2_cadastro_medico = self.entry_especialidade2_cadastro_medico.get()
        self.crm_cadastro_medico = self.entry_crm_cadastro_medico.get()
        self.cpf_cadastro_medico = self.entry_cpf_cadastro_medico.get()
        self.email_cadastro_medico = self.entry_email_cadastro_medico.get()
        self.telefone_cadastro_medico = self.entry_telefone_cadastro_medico.get()
        self.celular_cadastro_medico = self.entry_celular_cadastro_medico.get()
        self.obervacao_cadastro_medico = self.entry_obervacao_cadastro_medico.get()
        

if __name__ == '__main__':
    app = CTk(fg_color="#fff")

    class Aplicação(Funcs):
        def __init__(self):
            self.theme_color()
            self.janela_inicial()
        def janela_inicial(self):
            # Configuração da Janela
            app._set_appearance_mode("light")
            app.iconbitmap("assets\icons\icon.ico")
            app.title("Bem-Vindo!")
            app.geometry("1000x500+500+200")
            app.resizable(False, False)
            
            # frames da Janela
            # Banner Inicial
            banner_image = CTkImage(light_image=Image.open("assets\imgs\BG_Inicial.png"),
                                  dark_image=Image.open("assets\imgs\BG_Inicial.png"),
                                  size=(640, 472))
            image_label = CTkLabel(app, image=banner_image, text="").place(x=14, y=14)
            # Frame das opções iniciais
            self.frame_opcoes = CTkFrame(app,
                                            fg_color=self.white,
                                            width=346,
                                            height=472,
                                            border_width=0).place(x=654, y=14)
            # Titulo das opções
            self.titulo_opcoes = CTkLabel(app,
                                            text="Vamos começar",
                                            font=("Calibri", 40, "bold"),
                                            text_color=self.black).place(x=691, y=48)
            # Subtitulo das opções
            self.subtitulo_opcoes = CTkLabel(app,
                                            text="Escolha uma opção",
                                            font=("Calibri", 16),
                                            text_color=self.black).place(x=691, y=91)
            
            # Widgets da Janela
            # Botão de Consulta
            self.bt_consultas = CTkButton(self.frame_opcoes,
                                            width=272,
                                            height=48,
                                            fg_color=self.blue_light_2,
                                            border_color=self.blue,
                                            border_width=2,
                                            text="Consultas",
                                            font=("Calibri", 16, "bold"),
                                            text_color=self.blue,
                                            hover_color=self.blue_light_1,
                                            command=self.janela_consulta).place(x=691, y=157) 
            # Botão Cadastro
            self.bt_cadastros = CTkButton(self.frame_opcoes,
                                            width=272,
                                            height=48,
                                            fg_color=self.blue_light_2,
                                            border_color=self.blue,
                                            border_width=2,
                                            text="Cadastros",
                                            font=("Calibri", 16, "bold"),
                                            text_color=self.blue,
                                            hover_color=self.blue_light_1,
                                            command=self.janela_cadastro).place(x=691, y=229)            
            # Botão Cancelamento e Remarcação
            self.bt_cancelamento_remarcação = CTkButton(self.frame_opcoes,
                                            width=272,
                                            height=48,
                                            fg_color=self.blue_light_2,
                                            border_color=self.blue,
                                            border_width=2,
                                            text="Cancelamento e Remarcação",
                                            font=("Calibri", 16, "bold"),
                                            text_color=self.blue,
                                            hover_color=self.blue_light_1).place(x=691, y=301)            
            # Divisor dos botões
            self.divisor_botoes = CTkFrame(self.frame_opcoes,
                                        width=240,
                                        height=2,
                                        fg_color=self.gray).place(x=707, y=373)            
            # Exporta Exportar Agendamento
            self.bt_exporta_agendamento = CTkButton(self.frame_opcoes,
                                            width=224,
                                            height=48,
                                            fg_color=self.blue,
                                            text="Exportar Agendamento",
                                            font=("Calibri", 16, "bold"),
                                            text_color=self.white,
                                            hover_color=self.dark_blue).place(x=715, y=398)    
        def janela_cadastro(self):
            # Configuração da Janela
            self.janela_cadastro = CTkToplevel(app, fg_color="#fff")
            self.janela_cadastro.iconbitmap("assets\icons\icon.ico")
            self.janela_cadastro.title("Novo Cadastro")
            self.janela_cadastro.geometry("750x780+600+100")
            self.janela_cadastro.resizable(False, False)
            self.janela_cadastro.focus_force()
            self.janela_cadastro.grab_set() 
                        
            # Frames da Janela
            # Banner
            self.frame_bane = CTkFrame(self.janela_cadastro,
                                    fg_color=self.blue_light_2,
                                    border_color=self.blue_light_1,
                                    border_width=3,
                                    width=900,
                                    height=135
                                    ).place(x=-10, y=-36)
            # Titulo da janela
            self.lb_titulo_cadastro = CTkLabel(self.janela_cadastro,
                                            text="Cadastro de Pacientes e Médicos",
                                            font=("Calibri", 40, "bold"),
                                            text_color=self.black,
                                            fg_color=self.blue_light_2).place(x=32, y=16)
            # subtitulo da janela
            self.lb_titulo_cadastro = CTkLabel(self.janela_cadastro,
                                            text="Os campos marcados com * são obrigatórios",
                                            font=("Calibri", 16),
                                            text_color=self.black,
                                            fg_color=self.blue_light_2,
                                            bg_color=self.blue_light_2).place(x=32, y=56)
            
            # TabView do Cadastro
            self.tb_cadastro = CTkTabview(self.janela_cadastro,
                                          fg_color=self.blue_light_2,
                                          corner_radius=8,
                                          width=730,
                                          height=652,
                                          border_color=self.blue_light_1,
                                          border_width=4,
                                          segmented_button_fg_color=self.blue_light_1,
                                          segmented_button_selected_color=self.blue,
                                          segmented_button_selected_hover_color=self.dark_blue,
                                          anchor="nw")
            self.tb_cadastro.place(x=10, y=118)
            # Abas do TabView
            self.tb_cadastro_paciente = self.tb_cadastro.add("Cadastro de Pacientes")
            self.tb_cadastro_medico = self.tb_cadastro.add("Cadastro de Médicos")  
                      
            # Widgets do cadastro de paciente
            ## Lab e Entry de Nome
            self.lb_none_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Nome do Paciente*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=10)
            self.entry_nome_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=312,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_nome_cadastro_paciente.place(x=16, y=40)
            
            ## Lab e Entry de CPF
            self.lb_cpf_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="CPF*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=348, y=10)
            self.entry_cpf_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_cpf_cadastro_paciente.place(x=348, y=40)
            
            ## Lab e Entry de Nascimento
            self.lb_nascimento_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Data de Nasc.*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=548, y=10)
            self.entry_nascimento_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=150,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_nascimento_cadastro_paciente.place(x=548, y=40)
            
            ## Lab e Entry de Cep
            self.lb_cep_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                            text="CEP",
                                            font=("Calibri", 16, "bold"),
                                            text_color=self.black).place(x=16, y=90)                                       
            self.entry_cep_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=150,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_cep_cadastro_paciente.place(x=16, y=120)
            
            ## Lab e Entry de Endereço
            self.lb_endereco_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Endereço",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=187, y=90)
            self.entry_endereco_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=340,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_endereco_cadastro_paciente.place(x=187, y=120)
            
            ## Lab e Entry de Número
            self.lb_numero_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Número",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=548, y=90)
            self.entry_numero_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=150,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_numero_cadastro_paciente .place(x=548, y=120)
            
            ## Lab e Entry de Bairro
            self.lb_bairro_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Bairro",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=170)
            self.entry_bairro_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=230,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_bairro_cadastro_paciente.place(x=16, y=200)
            
            ## Lab e Entry de Cidade
            self.lb_cidade_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Cidade",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=284, y=170)
            self.entry_cidade_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=208,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_cidade_cadastro_paciente.place(x=268, y=200)
            
            ## Lab e Entry de Estado
            self.lb_estado_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Estado",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=498, y=170)
            self.entry_estado_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=200,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_estado_cadastro_paciente.place(x=498, y=200)
            
            ## Lab e Entry de E-Mail
            self.lb_email_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="E-Mail",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=250)
            self.entry_email_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=278,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_email_cadastro_paciente.place(x=16, y=280)

            ## Lab e Entry de Telefone
            self.lb_telefone_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Telefone",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=317, y=250)
            self.entry_telefone_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_telefone_cadastro_paciente.place(x=317, y=280)
            
            ## Lab e Entry de Celular
            self.lb_celular_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Celular*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=518, y=250)
            self.entry_celular_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_celular_cadastro_paciente.place(x=518, y=280)
            
            ## Lab e Entry de Obervação
            self.lb_obervacao_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                             text="Obervação",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=330)
            self.entry_obervacao_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                width=682,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_obervacao_cadastro_paciente.place(x=16, y=360)
            
            ## Aviso
            ### Frame de aviso
            self.bane_frame_paciente = CTkFrame(master=self.tb_cadastro_paciente,
                                    width= 610,
                                    height= 48,
                                    fg_color=self.blue_light_1,
                                    border_color=self.blue,
                                    border_width=3).place(x=16, y=430,)
            self.lb_aviso_paciente = CTkLabel(master=self.tb_cadastro_paciente,
                                    text="●  Atenção: Certifique-se de que todos os campos estão devidamente preenchidos antes de salvar.",
                                    text_color=self.black, 
                                    font=("Calibri", 14, "bold"),
                                    fg_color=self.blue_light_1).place(x=24, y=440)
            
            # Botões      
            ## Botão de Limpar
            self.bt_limpar_paciente = CTkButton(self.tb_cadastro_paciente,
                                          text="Limpar",
                                          text_color=self.blue,
                                          font=("Calibri", 16, "bold"),
                                          width=126,
                                          height=48,
                                          fg_color=self.blue_light_2,
                                          hover_color=self.blue_light_1,
                                          border_width=2,
                                          border_color=self.blue,
                                          command=self.limpar_cadastro_paciente)
            self.bt_limpar_paciente.place(x=422, y=534)
            ## Botão de Salvar
            self.bt_salvar_paciente = CTkButton(self.tb_cadastro_paciente,
                                          text="Salvar",
                                          text_color=self.white,
                                          font=("Calibri", 16, "bold"),
                                          width=126,
                                          height=48,
                                          fg_color=self.blue,
                                          hover_color=self.dark_blue
                                          ).place(x=570, y=534)
   
   
            # Widgets do cadastro de medico
            ## Lab e Entry de Nome
            self.lb_none_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="Nome do Médico(a)*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=10)
            self.entry_nome_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=312,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_nome_cadastro_medico.place(x=16, y=40)
            
            ## Lab e Entry de Especialidade 1
            self.lb_especialidade1_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="Especialidade 1*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=348, y=10)
            self.entry_especialidade1_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=350,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_especialidade1_cadastro_medico.place(x=348, y=40)
            
            ## Lab e Entry de Especialidade 2
            self.lb_especialidade2_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="Especialidade 2",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=90)
            self.entry_especialidade2_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=278,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_especialidade2_cadastro_medico.place(x=16, y=120)
            
            ## Lab e Entry de CRM
            self.lb_crm_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="CRM*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=317, y=90)
            self.entry_crm_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_crm_cadastro_medico.place(x=317, y=120)
            
            ## Lab e Entry de CPF
            self.lb_cpf_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="CPF*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=518, y=90)
            self.entry_cpf_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_cpf_cadastro_medico.place(x=518, y=120)
            
            ## Lab e Entry de E-Mail
            self.lb_email_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="E-Mail",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=170)
            self.entry_email_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=278,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_email_cadastro_medico.place(x=16, y=200)

            ## Lab e Entry de Telefone
            self.lb_telefone_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="Telefone",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=317, y=170)
            self.entry_telefone_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_telefone_cadastro_medico.place(x=317, y=200)
            
            ## Lab e Entry de Celular
            self.lb_celular_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="Celular*",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=518, y=170)
            self.entry_celular_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=180,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_celular_cadastro_medico.place(x=518, y=200)
            
            ## Lab e Entry de Obervação
            self.lb_obervacao_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                             text="Obervação",
                                             font=("Calibri", 16, "bold"),
                                             text_color=self.black).place(x=16, y=250)
            self.entry_obervacao_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                width=682,
                                                height=40,
                                                border_width=2,
                                                border_color=self.black,
                                                fg_color=self.gray_light,
                                                font=("Calibri", 16),
                                                text_color=self.black)
            self.entry_obervacao_cadastro_medico.place(x=16, y=280)
            
            ## Aviso
            ### Frame de aviso
            self.bane_frame_medico = CTkFrame(master=self.tb_cadastro_medico,
                                    width= 610,
                                    height= 48,
                                    fg_color=self.blue_light_1,
                                    border_color=self.blue,
                                    border_width=3).place(x=16, y=350,)
            self.lb_aviso_medico = CTkLabel(master=self.tb_cadastro_medico,
                                    text="●  Atenção: Certifique-se de que todos os campos estão devidamente preenchidos antes de salvar.",
                                    text_color=self.black, 
                                    font=("Calibri", 14, "bold"),
                                    fg_color=self.blue_light_1).place(x=24, y=360)
            
            # Botões      
            ## Botão de Limpar
            self.bt_limpar_medico = CTkButton(self.tb_cadastro_medico,
                                          text="Limpar",
                                          text_color=self.blue,
                                          font=("Calibri", 16, "bold"),
                                          width=126,
                                          height=48,
                                          fg_color=self.blue_light_2,
                                          hover_color=self.blue_light_1,
                                          border_width=2,
                                          border_color=self.blue,
                                          command=self.limpar_cadastro_medico).place(x=422, y=534)
            ## Botão de Salvar
            self.bt_salvar_medico = CTkButton(self.tb_cadastro_medico,
                                          text="Salvar",
                                          text_color=self.white,
                                          font=("Calibri", 16, "bold"),
                                          width=126,
                                          height=48,
                                          fg_color=self.blue,
                                          hover_color=self.dark_blue
                                          ).place(x=570, y=534)
        def janela_consulta(self):
            self.janela_consulta = CTkToplevel(app, fg_color="#fff")
            self.janela_consulta.title("Agendar Consulta")
            self.janela_consulta.geometry("750x780+600+100")
            self.janela_consulta.focus_force()
            self.janela_consulta.grab_set()
            
    Aplicação()
    app.mainloop()