from typing import Tuple
from customtkinter import *
from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        # Paleta de cores
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.black = "#000000"

        # Configuração da Janela
        self.title("Bem-Vindo!")
        self._set_appearance_mode("light")
        self.configure(fg_color='#fff')
        self.iconbitmap(default="assets\icons\icon.ico")
        self.geometry("1000x500+500+200")
        self.resizable(False, False)

        # frames da Janela
        # Banner Inicial
        banner_image = CTkImage(light_image=Image.open("assets\imgs\BG_Inicial.png"),
                                dark_image=Image.open(
                                    "assets\imgs\BG_Inicial.png"),
                                size=(640, 472))
        self.image_label = CTkLabel(self,
                                    image=banner_image,
                                    text="",
                                    fg_color='#fff').place(x=14, y=14)

        # Frame das opções iniciais
        self.frame_opcoes = CTkFrame(self,
                                     fg_color=self.white,
                                     bg_color=self.white,
                                     width=346,
                                     height=472,
                                     border_width=0).place(x=654, y=14)

        # Titulo das opções
        self.titulo_opcoes = CTkLabel(self,
                                      text="Vamos começar",
                                      font=("Calibri", 40, "bold"),
                                      text_color=self.black).place(x=691, y=48)
        # Subtitulo das opções
        self.subtitulo_opcoes = CTkLabel(self,
                                         text="Escolha uma opção",
                                         font=("Calibri", 16),
                                         text_color=self.black).place(x=691, y=91)

        # Widgets da Janela
        # Botão de Consulta
        self.bt_consultas = CTkButton(self,
                                      width=272,
                                      height=48,
                                      fg_color=self.blue_light_2,
                                      border_color=self.blue,
                                      border_width=2,
                                      text="Consultas",
                                      font=("Calibri", 16, "bold"),
                                      text_color=self.blue,
                                      hover_color=self.blue_light_1,
                                      command=self.open_ConsultaWindow).place(x=691, y=157)
        # Botão Cadastro
        self.bt_cadastros = CTkButton(self,
                                      width=272,
                                      height=48,
                                      fg_color=self.blue_light_2,
                                      border_color=self.blue,
                                      border_width=2,
                                      text="Cadastros",
                                      font=("Calibri", 16, "bold"),
                                      text_color=self.blue,
                                      hover_color=self.blue_light_1,
                                      command=self.open_CadastroWindow).place(x=691, y=229)
        # Botão Cancelamento e Remarcação
        self.bt_cancelamento_remarcação = CTkButton(self,
                                                    width=272,
                                                    height=48,
                                                    fg_color=self.blue_light_2,
                                                    border_color=self.blue,
                                                    border_width=2,
                                                    text="Cancelamento e Remarcação",
                                                    font=(
                                                        "Calibri", 16, "bold"),
                                                    text_color=self.blue,
                                                    hover_color=self.blue_light_1).place(x=691, y=301)
        # Divisor dos botões
        self.divisor_botoes = CTkFrame(self,
                                       width=240,
                                       height=2,
                                       fg_color=self.gray).place(x=707, y=373)
        # Exporta Exportar Agendamento
        self.bt_exporta_agendamento = CTkButton(self,
                                                width=224,
                                                height=48,
                                                fg_color=self.blue,
                                                text="Exportar Agendamento",
                                                font=("Calibri", 16, "bold"),
                                                text_color=self.white,
                                                hover_color=self.dark_blue).place(x=715, y=398)

    def open_CadastroWindow(self):
        CadastroWindow(self).grab_set()

    def open_ConsultaWindow(self):
        ConsultaWindow(self).grab_set()


class CadastroWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Paleta de cores
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.black = "#000000"

        # Configuração da Janela
        self.configure(fg_color="#fff")
        self.iconbitmap(default="assets\icons\icon.ico")
        self.title("Novo Cadastro")
        self.geometry("750x780+600+100")
        self.resizable(False, False)

        # Frames da Janela
        self.frames_cadastro()
        # TabView do Cadastro
        self.tabview_cadastro()
        # Widget do Cadastro
        self.widget_cadastro_paciente()
        # Widget do Cadastro
        self.widget_cadastro_medicos()

    def frames_cadastro(self):
        # Frames da Janela
        # Banner
        self.frame_bane = CTkFrame(self,
                                   fg_color=self.blue_light_2,
                                   border_color=self.blue_light_1,
                                   border_width=3,
                                   width=900,
                                   height=135).place(x=-10, y=-36)
        # Titulo da janela
        self.lb_titulo_cadastro = CTkLabel(self,
                                           text="Cadastro de Pacientes e Médicos",
                                           font=("Calibri", 40, "bold"),
                                           text_color=self.black,
                                           fg_color=self.blue_light_2).place(x=32, y=16)
        # subtitulo da janela
        self.lb_titulo_cadastro = CTkLabel(self,
                                           text="Os campos marcados com * são obrigatórios",
                                           font=("Calibri", 16),
                                           text_color=self.black,
                                           fg_color=self.blue_light_2,
                                           bg_color=self.blue_light_2).place(x=32, y=56)

    def tabview_cadastro(self):
        # TabView do Cadastro
        self.tb_cadastro = CTkTabview(self,
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
        self.tb_cadastro_paciente = self.tb_cadastro.add(
            "Cadastro de Pacientes")
        self.tb_cadastro_medico = self.tb_cadastro.add("Cadastro de Médicos")

    def widget_cadastro_paciente(self):
        # Widgets do cadastro de paciente
        # Lab e Entry de Nome
        self.lb_none_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                  text="Nome do Paciente*",
                                                  font=("Calibri", 16, "bold"),
                                                  text_color=self.black).place(x=16, y=10)
        self.entry_nome_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                     width=316,
                                                     height=40,
                                                     border_width=2,
                                                     border_color=self.black,
                                                     fg_color=self.gray_light,
                                                     font=("Calibri", 16),
                                                     text_color=self.black)
        self.entry_nome_cadastro_paciente.place(x=16, y=40)

        # Lab e Entry de CPF
        self.lb_cpf_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                 text="CPF*",
                                                 font=("Calibri", 16, "bold"),
                                                 text_color=self.black).place(x=348, y=10)
        self.entry_cpf_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                    width=184,
                                                    height=40,
                                                    border_width=2,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_cpf_cadastro_paciente.place(x=348, y=40)

        # Lab e Entry de Nascimento
        self.lb_nascimento_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                        text="Data de Nasc.*",
                                                        font=(
                                                            "Calibri", 16, "bold"),
                                                        text_color=self.black).place(x=548, y=10)
        self.entry_nascimento_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                           width=150,
                                                           height=40,
                                                           border_width=2,
                                                           border_color=self.black,
                                                           fg_color=self.gray_light,
                                                           font=(
                                                               "Calibri", 16),
                                                           text_color=self.black)
        self.entry_nascimento_cadastro_paciente.place(x=548, y=40)

        # Lab e Entry de Cep
        self.lb_cep_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                 text="CEP",
                                                 font=("Calibri", 16, "bold"),
                                                 text_color=self.black).place(x=16, y=90)
        self.entry_cep_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                    width=154,
                                                    height=40,
                                                    border_width=2,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_cep_cadastro_paciente.place(x=16, y=120)

        # Lab e Entry de Endereço
        self.lb_endereco_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                      text="Endereço",
                                                      font=(
                                                          "Calibri", 16, "bold"),
                                                      text_color=self.black).place(x=187, y=90)
        self.entry_endereco_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                         width=344,
                                                         height=40,
                                                         border_width=2,
                                                         border_color=self.black,
                                                         fg_color=self.gray_light,
                                                         font=("Calibri", 16),
                                                         text_color=self.black)
        self.entry_endereco_cadastro_paciente.place(x=187, y=120)

        # Lab e Entry de Número
        self.lb_numero_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Número",
                                                    font=(
                                                        "Calibri", 16, "bold"),
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

        # Lab e Entry de Bairro
        self.lb_bairro_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Bairro",
                                                    font=(
                                                        "Calibri", 16, "bold"),
                                                    text_color=self.black).place(x=16, y=170)
        self.entry_bairro_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                       width=234,
                                                       height=40,
                                                       border_width=2,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_bairro_cadastro_paciente.place(x=16, y=200)

        # Lab e Entry de Cidade
        self.lb_cidade_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Cidade",
                                                    font=(
                                                        "Calibri", 16, "bold"),
                                                    text_color=self.black).place(x=268, y=170)
        self.entry_cidade_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                       width=212,
                                                       height=40,
                                                       border_width=2,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_cidade_cadastro_paciente.place(x=268, y=200)

        # Lab e Entry de Estado
        self.lb_estado_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Estado",
                                                    font=(
                                                        "Calibri", 16, "bold"),
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

        # Lab e Entry de E-Mail
        self.lb_email_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                   text="E-Mail",
                                                   font=(
                                                       "Calibri", 16, "bold"),
                                                   text_color=self.black).place(x=16, y=250)
        self.entry_email_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                      width=282,
                                                      height=40,
                                                      border_width=2,
                                                      border_color=self.black,
                                                      fg_color=self.gray_light,
                                                      font=("Calibri", 16),
                                                      text_color=self.black)
        self.entry_email_cadastro_paciente.place(x=16, y=280)

        # Lab e Entry de Telefone
        self.lb_telefone_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                      text="Telefone",
                                                      font=(
                                                          "Calibri", 16, "bold"),
                                                      text_color=self.black).place(x=317, y=250)
        self.entry_telefone_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                         width=182,
                                                         height=40,
                                                         border_width=2,
                                                         border_color=self.black,
                                                         fg_color=self.gray_light,
                                                         font=("Calibri", 16),
                                                         text_color=self.black)
        self.entry_telefone_cadastro_paciente.place(x=317, y=280)

        # Lab e Entry de Celular
        self.lb_celular_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                     text="Celular*",
                                                     font=(
                                                         "Calibri", 16, "bold"),
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

        # Lab e Entry de Obervação
        self.lb_obervacao_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                       text="Obervação",
                                                       font=(
                                                           "Calibri", 16, "bold"),
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

        # Aviso
        # Frame de aviso
        self.bane_frame_paciente = CTkFrame(master=self.tb_cadastro_paciente,
                                            width=610,
                                            height=48,
                                            fg_color=self.blue_light_1,
                                            border_color=self.blue,
                                            border_width=3).place(x=16, y=430,)
        self.lb_aviso_paciente = CTkLabel(master=self.tb_cadastro_paciente,
                                          text="●  Atenção: Certifique-se de que todos os campos estão devidamente preenchidos antes de salvar.",
                                          text_color=self.black,
                                          font=("Calibri", 14, "bold"),
                                          fg_color=self.blue_light_1).place(x=24, y=440)

        # Botões
        # Botão de Limpar
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
        # Botão de Salvar
        self.bt_salvar_paciente = CTkButton(self.tb_cadastro_paciente,
                                            text="Salvar",
                                            text_color=self.white,
                                            font=("Calibri", 16, "bold"),
                                            width=126,
                                            height=48,
                                            fg_color=self.blue,
                                            hover_color=self.dark_blue
                                            ).place(x=570, y=534)

    def widget_cadastro_medicos(self):
        # Widgets do cadastro de medico
        # Lab e Entry de Nome
        self.lb_none_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                text="Nome do Médico(a)*",
                                                font=("Calibri", 16, "bold"),
                                                text_color=self.black).place(x=16, y=10)
        self.entry_nome_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                   width=316,
                                                   height=40,
                                                   border_width=2,
                                                   border_color=self.black,
                                                   fg_color=self.gray_light,
                                                   font=("Calibri", 16),
                                                   text_color=self.black)
        self.entry_nome_cadastro_medico.place(x=16, y=40)

        # Lab e Entry de Especialidade 1
        self.lb_especialidade1_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                          text="Especialidade 1*",
                                                          font=(
                                                              "Calibri", 16, "bold"),
                                                          text_color=self.black).place(x=348, y=10)
        self.entry_especialidade1_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                             width=350,
                                                             height=40,
                                                             border_width=2,
                                                             border_color=self.black,
                                                             fg_color=self.gray_light,
                                                             font=(
                                                                 "Calibri", 16),
                                                             text_color=self.black)
        self.entry_especialidade1_cadastro_medico.place(x=348, y=40)

        # Lab e Entry de Especialidade 2
        self.lb_especialidade2_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                          text="Especialidade 2",
                                                          font=(
                                                              "Calibri", 16, "bold"),
                                                          text_color=self.black).place(x=16, y=90)
        self.entry_especialidade2_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                             width=284,
                                                             height=40,
                                                             border_width=2,
                                                             border_color=self.black,
                                                             fg_color=self.gray_light,
                                                             font=(
                                                                 "Calibri", 16),
                                                             text_color=self.black)
        self.entry_especialidade2_cadastro_medico.place(x=16, y=120)

        # Lab e Entry de CRM
        self.lb_crm_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                               text="CRM*",
                                               font=("Calibri", 16, "bold"),
                                               text_color=self.black).place(x=317, y=90)
        self.entry_crm_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                  width=184,
                                                  height=40,
                                                  border_width=2,
                                                  border_color=self.black,
                                                  fg_color=self.gray_light,
                                                  font=("Calibri", 16),
                                                  text_color=self.black)
        self.entry_crm_cadastro_medico.place(x=317, y=120)

        # Lab e Entry de CPF
        self.lb_cpf_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                               text="CPF*",
                                               font=("Calibri", 16, "bold"),
                                               text_color=self.black).place(x=518, y=90)
        self.entry_cpf_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                  width=184,
                                                  height=40,
                                                  border_width=2,
                                                  border_color=self.black,
                                                  fg_color=self.gray_light,
                                                  font=("Calibri", 16),
                                                  text_color=self.black)
        self.entry_cpf_cadastro_medico.place(x=518, y=120)

        # Lab e Entry de E-Mail
        self.lb_email_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                 text="E-Mail",
                                                 font=("Calibri", 16, "bold"),
                                                 text_color=self.black).place(x=16, y=170)
        self.entry_email_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                    width=284,
                                                    height=40,
                                                    border_width=2,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_email_cadastro_medico.place(x=16, y=200)

        # Lab e Entry de Telefone
        self.lb_telefone_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                    text="Telefone",
                                                    font=(
                                                        "Calibri", 16, "bold"),
                                                    text_color=self.black).place(x=317, y=170)
        self.entry_telefone_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                       width=184,
                                                       height=40,
                                                       border_width=2,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_telefone_cadastro_medico.place(x=317, y=200)

        # Lab e Entry de Celular
        self.lb_celular_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                   text="Celular*",
                                                   font=(
                                                       "Calibri", 16, "bold"),
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

        # Lab e Entry de Obervação
        self.lb_obervacao_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                     text="Obervação",
                                                     font=(
                                                         "Calibri", 16, "bold"),
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

        # Aviso
        # Frame de aviso
        self.bane_frame_medico = CTkFrame(master=self.tb_cadastro_medico,
                                          width=610,
                                          height=48,
                                          fg_color=self.blue_light_1,
                                          border_color=self.blue,
                                          border_width=3).place(x=16, y=350,)
        self.lb_aviso_medico = CTkLabel(master=self.tb_cadastro_medico,
                                        text="●  Atenção: Certifique-se de que todos os campos estão devidamente preenchidos antes de salvar.",
                                        text_color=self.black,
                                        font=("Calibri", 14, "bold"),
                                        fg_color=self.blue_light_1).place(x=24, y=360)

        # Botões
        # Botão de Limpar
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
        # Botão de Salvar
        self.bt_salvar_medico = CTkButton(self.tb_cadastro_medico,
                                          text="Salvar",
                                          text_color=self.white,
                                          font=("Calibri", 16, "bold"),
                                          width=126,
                                          height=48,
                                          fg_color=self.blue,
                                          hover_color=self.dark_blue
                                          ).place(x=570, y=534)

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


class ConsultaWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Paleta de cores
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.black = "#000000"

        # Configuração da Janela
        self.configure(fg_color="#fff")
        self.title("Agendamento de Consultas")
        self.geometry("1280x850+350+100")
        self.resizable(False, False)

        # Frame
        self.frame_agendar_consulta()
        # TabView
        self.tabview_agendar_consulta()
        # Widgets
        self.widget_agendar_consulta()

    def frame_agendar_consulta(self):
        # Banner
        self.frame_bane_consulta = CTkFrame(self,
                                            fg_color=self.blue_light_2,
                                            border_color=self.blue_light_1,
                                            border_width=3,
                                            width=1300,
                                            height=144
                                            ).place(x=-10, y=-36)
        # Titulo da janela
        self.lb_titulo_consulta = CTkLabel(self,
                                           text="Agendamento de Consultas",
                                           font=("Calibri", 40, "bold"),
                                           text_color=self.black,
                                           fg_color=self.blue_light_2).place(x=32, y=16)
        # subtitulo da janela
        self.lb_titulo_consulta = CTkLabel(self,
                                           text="Os campos marcados com * são obrigatórios",
                                           font=("Calibri", 16),
                                           text_color=self.black,
                                           fg_color=self.blue_light_2,
                                           bg_color=self.blue_light_2).place(x=32, y=64)

    def tabview_agendar_consulta(self):
        # TabView do Cadastro
        # TabView
        self.tb_consulta = CTkTabview(self,
                                      fg_color=self.blue_light_2,
                                      corner_radius=8,
                                      width=1260,
                                      height=722,
                                      border_color=self.blue_light_1,
                                      border_width=4,
                                      segmented_button_fg_color=self.blue_light_1,
                                      segmented_button_selected_color=self.blue,
                                      segmented_button_selected_hover_color=self.dark_blue,
                                      anchor="nw")
        self.tb_consulta.place(x=10, y=118)
        # Abas do TabView
        self.tb_agendar_consulta = self.tb_consulta.add("Agendar Consulta")
        self.tb_consultar_agendamento = self.tb_consulta.add(
            "Consultar Agendamento")

    def widget_agendar_consulta(self):
        # Widgets do agendamento de consulta

        # Dados do Paciente
        # Frame dos dados do paciente
        self.frame_dados_paciente = CTkFrame(self.tb_agendar_consulta,
                                             width=1224,
                                             height=192,
                                             fg_color=self.white,
                                             border_color=self.blue_light_1,
                                             border_width=3).place(x=10, y=24)

        self.lb_dados_paciente = CTkLabel(self.tb_agendar_consulta,
                                          width=160,
                                          text='Dados do Paciente',
                                          font=('Calibri', 18, 'bold'),
                                          corner_radius=6,
                                          fg_color=self.blue_light_1,
                                          text_color=self.black).place(x=20, y=12)

        # Labels e Entrys
        # Label e Entry CPF
        self.lb_cpf_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                     text="CPF",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=24, y=50)
        self.entry_cpf_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                        width=158,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_cpf_agendamento_paciente.place(x=24, y=80)

        # Label e Entry Nome
        self.lb_none_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                     text="Nome Completo do Paciente",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=198, y=50)
        self.entry_nome_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                        width=360,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_nome_agendamento_paciente.place(x=198, y=80)

        # Label e Entry Nascimento
        self.lb_nascimento_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                     text="Data de Nasc.",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=576, y=50)
        self.entry_nascimento_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                        width=160,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_nascimento_agendamento_paciente.place(x=576, y=80)

        # Gênero
        self.lb_genero_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Gênero",
                                                       font=(
                                                           "Calibri", 16, "bold"),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=754, y=50)
        genero = ['null', 'Masculino', 'Feminino']
        self.cb_genero = CTkComboBox(self.tb_agendar_consulta,
                                     width=160,
                                     height=40,
                                     font=("Calibri", 16),
                                     dropdown_font=('Calibri', 16),
                                     dropdown_text_color=self.black,
                                     text_color=self.black,
                                     border_width=2,
                                     border_color=self.black,
                                     fg_color=self.white,
                                     button_hover_color=self.dark_blue,
                                     button_color=self.blue,
                                     dropdown_fg_color=self.white,
                                     dropdown_hover_color=self.blue_light_2,
                                     justify='left',
                                     values=genero).place(x=754, y=80)

        # Label e Entry Endereço
        self.lb_endereco_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                     text="Endereço",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=932, y=50)
        self.entry_endereco_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                        width=288,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_endereco_agendamento_paciente.place(x=932, y=80)

        # Label e Entry Bairro
        self.lb_bairro_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Bairro",
                                                       font=(
                                                           "Calibri", 16, "bold"),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=24, y=130)
        self.entry_bairro_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                          width=188,
                                                          height=40,
                                                          border_width=2,
                                                          border_color=self.black,
                                                          fg_color=self.gray_light,
                                                          font=("Calibri", 16),
                                                          text_color=self.black)
        self.entry_bairro_agendamento_paciente.place(x=24, y=160)

        # Label e Entry Cidade
        self.lb_cidade_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Cidade",
                                                       font=(
                                                           "Calibri", 16, "bold"),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=230, y=130)
        self.entry_cidade_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                          width=220,
                                                          height=40,
                                                          border_width=2,
                                                          border_color=self.black,
                                                          fg_color=self.gray_light,
                                                          font=("Calibri", 16),
                                                          text_color=self.black)
        self.entry_cidade_agendamento_paciente.place(x=230, y=160)

        # Label e Entry Número
        self.lb_numero_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Número",
                                                       font=(
                                                           "Calibri", 16, "bold"),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=468, y=130)
        self.entry_numero_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                          width=90,
                                                          height=40,
                                                          border_width=2,
                                                          border_color=self.black,
                                                          fg_color=self.gray_light,
                                                          font=("Calibri", 16),
                                                          text_color=self.black)
        self.entry_numero_agendamento_paciente.place(x=468, y=160)

        # Label e Entry E-Mail
        self.lb_email_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                      text="E-Mail",
                                                      font=(
                                                          "Calibri", 16, "bold"),
                                                      text_color=self.black,
                                                      fg_color=self.white).place(x=576, y=130)
        self.entry_email_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                         width=280,
                                                         height=40,
                                                         border_width=2,
                                                         border_color=self.black,
                                                         fg_color=self.gray_light,
                                                         font=("Calibri", 16),
                                                         text_color=self.black)
        self.entry_email_agendamento_paciente.place(x=576, y=160)

        # Label e Entry Celular
        self.lb_celular_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                        text="Celular",
                                                        font=(
                                                            "Calibri", 16, "bold"),
                                                        text_color=self.black,
                                                        fg_color=self.white).place(x=874, y=130)
        self.entry_celular_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                           width=168,
                                                           height=40,
                                                           border_width=2,
                                                           border_color=self.black,
                                                           fg_color=self.gray_light,
                                                           font=(
                                                               "Calibri", 16),
                                                           text_color=self.black)
        self.entry_celular_agendamento_paciente.place(x=874, y=160)

        # Label e Entry Telefone
        self.lb_telefone_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                         text="Telefone",
                                                         font=(
                                                             "Calibri", 16, "bold"),
                                                         text_color=self.black,
                                                         fg_color=self.white).place(x=1060, y=130)
        self.entry_telefone_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                            width=160,
                                                            height=40,
                                                            border_width=2,
                                                            border_color=self.black,
                                                            fg_color=self.gray_light,
                                                            font=(
                                                                "Calibri", 16),
                                                            text_color=self.black)
        self.entry_telefone_agendamento_paciente.place(x=1060, y=160)

        # Dados do medico
        # Frame dos dados do médico
        self.frame_dados_medico = CTkFrame(self.tb_agendar_consulta,
                                           width=1224,
                                           height=116,
                                           fg_color=self.white,
                                           border_color=self.blue_light_1,
                                           border_width=3).place(x=10, y=242)

        self.lb_dados_medico = CTkLabel(self.tb_agendar_consulta,
                                        width=160,
                                        text='Dados do Médico',
                                        font=('Calibri', 18, 'bold'),
                                        corner_radius=6,
                                        fg_color=self.blue_light_1,
                                        text_color=self.black).place(x=20, y=230)

        # Label e Entry CRM
        self.lb_crm_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                     text="CRM",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=24, y=270)
        self.entry_crm_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                        width=150,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_crm_agendamento_medico.place(x=24, y=300)
        
        # Label e Entry Médico
        self.lb_nome_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                     text="Médico",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=190, y=270)
        self.entry_nome_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                        width=356,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_nome_agendamento_medico.place(x=190, y=300)
        
        # Label e Entry Especialidade 1
        self.lb_especialidade1_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                     text="Especialidade 1",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=564, y=270)
        self.entry_especialidade1_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                        width=320,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_especialidade1_agendamento_medico.place(x=564, y=300)
        
        # Label e Entry Especialidade 2
        self.lb_especialidade2_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                     text="Especialidade 2",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=900, y=270)
        self.entry_especialidade2_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                        width=320,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_especialidade2_agendamento_medico.place(x=900, y=300)
        
        
        # Dados do Agendamento
        # Frame dos dados do médico
        self.frame_dados_agendamento = CTkFrame(self.tb_agendar_consulta,
                                           width=1224,
                                           height=116,
                                           fg_color=self.white,
                                           border_color=self.blue_light_1,
                                           border_width=3).place(x=10, y=384)

        self.lb_dados_agendamento = CTkLabel(self.tb_agendar_consulta,
                                        width=160,
                                        text='Dados do Agendamento',
                                        font=('Calibri', 18, 'bold'),
                                        corner_radius=6,
                                        fg_color=self.blue_light_1,
                                        text_color=self.black).place(x=20, y=372)

        # Label e Entry Data Agendamento
        self.lb_data_agendamento = CTkLabel(self.tb_agendar_consulta,
                                                     text="Data Agend.",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=24, y=410)
        self.entry_data_agendamento = CTkEntry(self.tb_agendar_consulta,
                                                        width=180,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_data_agendamento.place(x=24, y=440)
        
        # Label e Entry Médico
        self.lb_horario_agendamento = CTkLabel(self.tb_agendar_consulta,
                                                     text="Horário Agend.",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=222, y=410)
        self.entry_horario_agendamento = CTkEntry(self.tb_agendar_consulta,
                                                        width=180,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_horario_agendamento.place(x=222, y=440)
        
        # Label e Entry Observação
        self.lb_observacao_agendamento = CTkLabel(self.tb_agendar_consulta,
                                                     text="Observação",
                                                     font=(
                                                         "Calibri", 16, "bold"),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=420, y=410)
        self.entry_observacao_agendamento = CTkEntry(self.tb_agendar_consulta,
                                                        width=800,
                                                        height=40,
                                                        border_width=2,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_observacao_agendamento.place(x=420, y=440)
        
        


if __name__ == '__main__':
    app = MainWindow()

    app.mainloop()
