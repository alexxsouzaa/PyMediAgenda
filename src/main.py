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

        self.monta_tabela_medicos()
        self.monta_tabela_pacientes()

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
                                                  font=("Calibri", 16),
                                                  text_color=self.black).place(x=16, y=10)
        self.entry_nome_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                     width=316,
                                                     height=40,
                                                     border_width=1,
                                                     border_color=self.black,
                                                     fg_color=self.gray_light,
                                                     font=("Calibri", 16),
                                                     text_color=self.black)
        self.entry_nome_cadastro_paciente.place(x=16, y=40)

        # Lab e Entry de CPF
        self.lb_cpf_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                 text="CPF*",
                                                 font=("Calibri", 16),
                                                 text_color=self.black).place(x=348, y=10)
        self.entry_cpf_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                    width=184,
                                                    height=40,
                                                    border_width=1,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_cpf_cadastro_paciente.place(x=348, y=40)

        # Lab e Entry de Nascimento
        self.lb_nascimento_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                        text="Data de Nasc.*",
                                                        font=(
                                                            "Calibri", 16),
                                                        text_color=self.black).place(x=548, y=10)
        self.entry_nascimento_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                           width=150,
                                                           height=40,
                                                           border_width=1,
                                                           border_color=self.black,
                                                           fg_color=self.gray_light,
                                                           font=(
                                                               "Calibri", 16),
                                                           text_color=self.black)
        self.entry_nascimento_cadastro_paciente.place(x=548, y=40)

        # Lab e Entry de Cep
        self.lb_cep_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                 text="CEP",
                                                 font=("Calibri", 16),
                                                 text_color=self.black).place(x=16, y=90)
        self.entry_cep_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                    width=154,
                                                    height=40,
                                                    border_width=1,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_cep_cadastro_paciente.place(x=16, y=120)

        # Lab e Entry de Endereço
        self.lb_endereco_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                      text="Endereço",
                                                      font=(
                                                          "Calibri", 16),
                                                      text_color=self.black).place(x=187, y=90)
        self.entry_endereco_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                         width=344,
                                                         height=40,
                                                         border_width=1,
                                                         border_color=self.black,
                                                         fg_color=self.gray_light,
                                                         font=("Calibri", 16),
                                                         text_color=self.black)
        self.entry_endereco_cadastro_paciente.place(x=187, y=120)

        # Lab e Entry de Número
        self.lb_numero_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Número",
                                                    font=(
                                                        "Calibri", 16),
                                                    text_color=self.black).place(x=548, y=90)
        self.entry_numero_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                       width=150,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_numero_cadastro_paciente .place(x=548, y=120)

        # Lab e Entry de Bairro
        self.lb_bairro_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Bairro",
                                                    font=(
                                                        "Calibri", 16),
                                                    text_color=self.black).place(x=16, y=170)
        self.entry_bairro_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                       width=234,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_bairro_cadastro_paciente.place(x=16, y=200)

        # Lab e Entry de Cidade
        self.lb_cidade_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Cidade",
                                                    font=(
                                                        "Calibri", 16),
                                                    text_color=self.black).place(x=268, y=170)
        self.entry_cidade_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                       width=212,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_cidade_cadastro_paciente.place(x=268, y=200)

        # Lab e Entry de Estado
        self.lb_estado_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                    text="Estado",
                                                    font=(
                                                        "Calibri", 16),
                                                    text_color=self.black).place(x=498, y=170)
        self.entry_estado_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                       width=200,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_estado_cadastro_paciente.place(x=498, y=200)

        # Lab e Entry de E-Mail
        self.lb_email_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                   text="E-Mail",
                                                   font=(
                                                       "Calibri", 16),
                                                   text_color=self.black).place(x=16, y=250)
        self.entry_email_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                      width=282,
                                                      height=40,
                                                      border_width=1,
                                                      border_color=self.black,
                                                      fg_color=self.gray_light,
                                                      font=("Calibri", 16),
                                                      text_color=self.black)
        self.entry_email_cadastro_paciente.place(x=16, y=280)

        # Lab e Entry de Telefone
        self.lb_telefone_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                      text="Telefone",
                                                      font=(
                                                          "Calibri", 16),
                                                      text_color=self.black).place(x=317, y=250)
        self.entry_telefone_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                         width=182,
                                                         height=40,
                                                         border_width=1,
                                                         border_color=self.black,
                                                         fg_color=self.gray_light,
                                                         font=("Calibri", 16),
                                                         text_color=self.black)
        self.entry_telefone_cadastro_paciente.place(x=317, y=280)

        # Lab e Entry de Celular
        self.lb_celular_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                     text="Celular*",
                                                     font=(
                                                         "Calibri", 16),
                                                     text_color=self.black).place(x=518, y=250)
        self.entry_celular_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                        width=180,
                                                        height=40,
                                                        border_width=1,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_celular_cadastro_paciente.place(x=518, y=280)

        # Lab e Entry de Obervação
        self.lb_obervacao_cadastro_paciente = CTkLabel(self.tb_cadastro_paciente,
                                                       text="Obervação",
                                                       font=(
                                                           "Calibri", 16),
                                                       text_color=self.black).place(x=16, y=330)
        self.entry_obervacao_cadastro_paciente = CTkEntry(self.tb_cadastro_paciente,
                                                          width=682,
                                                          height=40,
                                                          border_width=1,
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
                                            fg_color=self.white,
                                            hover_color=self.blue_light_2,
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
                                            hover_color=self.dark_blue,
                                            command=self.add_dados_pacientes
                                            ).place(x=570, y=534)

    def widget_cadastro_medicos(self):
        # Widgets do cadastro de medico
        # Lab e Entry de Nome
        self.lb_none_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                text="Nome do Médico(a)*",
                                                font=("Calibri", 16),
                                                text_color=self.black).place(x=16, y=10)
        self.entry_nome_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                   width=316,
                                                   height=40,
                                                   border_width=1,
                                                   border_color=self.black,
                                                   fg_color=self.gray_light,
                                                   font=("Calibri", 16),
                                                   text_color=self.black)
        self.entry_nome_cadastro_medico.place(x=16, y=40)

        # Lab e Entry de Especialidade 1
        self.lb_especialidade1_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                          text="Especialidade 1*",
                                                          font=(
                                                              "Calibri", 16),
                                                          text_color=self.black).place(x=348, y=10)
        self.entry_especialidade1_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                             width=350,
                                                             height=40,
                                                             border_width=1,
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
                                                              "Calibri", 16),
                                                          text_color=self.black).place(x=16, y=90)
        self.entry_especialidade2_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                             width=284,
                                                             height=40,
                                                             border_width=1,
                                                             border_color=self.black,
                                                             fg_color=self.gray_light,
                                                             font=(
                                                                 "Calibri", 16),
                                                             text_color=self.black)
        self.entry_especialidade2_cadastro_medico.place(x=16, y=120)

        # Lab e Entry de CRM
        self.lb_crm_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                               text="CRM*",
                                               font=("Calibri", 16),
                                               text_color=self.black).place(x=317, y=90)
        self.entry_crm_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                  width=184,
                                                  height=40,
                                                  border_width=1,
                                                  border_color=self.black,
                                                  fg_color=self.gray_light,
                                                  font=("Calibri", 16),
                                                  text_color=self.black)
        self.entry_crm_cadastro_medico.place(x=317, y=120)

        # Lab e Entry de CPF
        self.lb_cpf_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                               text="CPF*",
                                               font=("Calibri", 16),
                                               text_color=self.black).place(x=518, y=90)
        self.entry_cpf_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                  width=184,
                                                  height=40,
                                                  border_width=1,
                                                  border_color=self.black,
                                                  fg_color=self.gray_light,
                                                  font=("Calibri", 16),
                                                  text_color=self.black)
        self.entry_cpf_cadastro_medico.place(x=518, y=120)

        # Lab e Entry de E-Mail
        self.lb_email_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                 text="E-Mail",
                                                 font=("Calibri", 16),
                                                 text_color=self.black).place(x=16, y=170)
        self.entry_email_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                    width=284,
                                                    height=40,
                                                    border_width=1,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_email_cadastro_medico.place(x=16, y=200)

        # Lab e Entry de Telefone
        self.lb_telefone_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                    text="Telefone",
                                                    font=(
                                                        "Calibri", 16),
                                                    text_color=self.black).place(x=317, y=170)
        self.entry_telefone_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                       width=184,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_telefone_cadastro_medico.place(x=317, y=200)

        # Lab e Entry de Celular
        self.lb_celular_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                   text="Celular*",
                                                   font=(
                                                       "Calibri", 16),
                                                   text_color=self.black).place(x=518, y=170)
        self.entry_celular_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                      width=180,
                                                      height=40,
                                                      border_width=1,
                                                      border_color=self.black,
                                                      fg_color=self.gray_light,
                                                      font=("Calibri", 16),
                                                      text_color=self.black)
        self.entry_celular_cadastro_medico.place(x=518, y=200)

        # Lab e Entry de Obervação
        self.lb_obervacao_cadastro_medico = CTkLabel(self.tb_cadastro_medico,
                                                     text="Obervação",
                                                     font=(
                                                         "Calibri", 16),
                                                     text_color=self.black).place(x=16, y=250)
        self.entry_obervacao_cadastro_medico = CTkEntry(self.tb_cadastro_medico,
                                                        width=682,
                                                        height=40,
                                                        border_width=1,
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
                                          fg_color=self.white,
                                          hover_color=self.blue_light_2,
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
                                          hover_color=self.dark_blue,
                                          command=self.add_dados_medicos
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

    def conecta_bd(self):
        self.conn = sqlite3.connect('banco_dados.bd')
        self.cursor = self.conn.cursor()
        print('Conectado ao banco de dados.')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectado do banco de dados.')

    def monta_tabela_pacientes(self):
        self.conecta_bd()
        self.cursor.execute(""" 
                            CREATE TABLE IF NOT EXISTS pacientes (
                                cod INTEGER PRIMARY KEY,
                                cpf TEXT NOT NULL,
                                nome TEXT NOT NULL,
                                data_nascimento DATE,
                                cep TEXT,
                                endereco TEXT,
                                numero INTEGER,
                                bairro TEXT,
                                cidade TEXT,
                                estado TEXT,
                                email TEXT,
                                celular TEXT NOT NULL,
                                telefone TEXT,
                                observacao TEXT
                            );
                        """)
        print('Tabela de Pacintes montada.')
        self.conn.commit()
        self.desconecta_bd()

    def monta_tabela_medicos(self):
        self.conecta_bd()
        self.cursor.execute(""" 
                            CREATE TABLE IF NOT EXISTS medicos (
                                cod INTEGER PRIMARY KEY,
                                cpf TEXT NOT NULL,
                                nome TEXT NOT NULL,
                                crm TEXT NOT NULL,
                                especialidade1 TEXT NOL NULL,
                                especialidade2 TEXT,
                                email TEXT,
                                celular TEXT NOT NULL,
                                telefone TEXT,
                                observacao TEXT
                            );
                        """)
        print('Tabela de Médicos montada.')
        self.conn.commit()
        self.desconecta_bd()

    def add_dados_medicos(self):
        self.nome_medico = self.entry_nome_cadastro_medico.get()
        self.especialidade1_medico = self.entry_especialidade1_cadastro_medico.get()
        self.especialidade2_medico = self.entry_especialidade2_cadastro_medico.get()
        self.crm_medico = self.entry_crm_cadastro_medico.get()
        self.cpf_medico = self.entry_cpf_cadastro_medico.get()
        self.email_medico = self.entry_email_cadastro_medico.get()
        self.telefone_medico = self.entry_telefone_cadastro_medico.get()
        self.celular_medico = self.entry_celular_cadastro_medico.get()
        self.observacao_medico = self.entry_obervacao_cadastro_medico.get()

        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO medicos (cpf, nome, crm, especialidade1, especialidade2, email, celular, telefone, observacao)
                             VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.cpf_medico, self.nome_medico, self.crm_medico, self.especialidade1_medico, self.especialidade2_medico, self.email_medico, self.celular_medico, self.telefone_medico, self.observacao_medico))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_cadastro_medico()

    def add_dados_pacientes(self):
        self.nome_paciente = self.entry_nome_cadastro_paciente.get()
        self.cpf_paciente = self.entry_cpf_cadastro_paciente.get()
        self.data_nascimento_paciente = self.entry_nascimento_cadastro_paciente.get()
        self.cep_paciente = self.entry_cep_cadastro_paciente.get()
        self.endereco_paciente = self.entry_endereco_cadastro_paciente.get()
        self.numero_paciente = self.entry_numero_cadastro_paciente.get()
        self.bairro_paciente = self.entry_bairro_cadastro_paciente.get()
        self.cidade_paciente = self.entry_cidade_cadastro_paciente.get()
        self.estado_paciente = self.entry_estado_cadastro_paciente.get()
        self.email_paciente = self.entry_email_cadastro_paciente.get()
        self.telefone_paciente = self.entry_telefone_cadastro_paciente.get()
        self.celular_paciente = self.entry_celular_cadastro_paciente.get()
        self.observacao_paciente = self.entry_obervacao_cadastro_paciente.get()

        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO pacientes (cpf, nome, data_nascimento, cep, endereco, numero, bairro, cidade, estado, email, celular, telefone, observacao)
                             VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.cpf_paciente, self.nome_paciente, self.data_nascimento_paciente, self.cep_paciente, self.endereco_paciente, self.numero_paciente, self.bairro_paciente, self.cidade_paciente, self.estado_paciente, self.email_paciente, self.celular_paciente, self.telefone_paciente, self.observacao_paciente))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_cadastro_paciente()

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

        self.widget_consultar_agendamento()

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
                                             height=174,
                                             fg_color=self.white,
                                             border_color=self.blue_light_1,
                                             border_width=3).place(x=10, y=42)

        self.lb_dados_paciente = CTkLabel(self.tb_agendar_consulta,
                                          width=160,
                                          text='Dados do Paciente',
                                          font=('Calibri', 18, 'bold'),
                                          corner_radius=6,
                                          text_color=self.black).place(x=5, y=12)

        # Labels e Entrys
        # Label e Entry CPF
        self.lb_cpf_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                    text="CPF*",
                                                    font=(
                                                         "Calibri", 16),
                                                    text_color=self.black,
                                                    fg_color=self.white).place(x=24, y=50)
        self.entry_cpf_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                       width=158,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_cpf_agendamento_paciente.place(x=24, y=80)

        # Label e Entry Nome
        self.lb_none_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                     text="Nome Completo do Paciente*",
                                                     font=(
                                                         "Calibri", 16),
                                                     text_color=self.black,
                                                     fg_color=self.white).place(x=198, y=50)
        self.entry_nome_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                        width=360,
                                                        height=40,
                                                        border_width=1,
                                                        border_color=self.black,
                                                        fg_color=self.gray_light,
                                                        font=("Calibri", 16),
                                                        text_color=self.black)
        self.entry_nome_agendamento_paciente.place(x=198, y=80)

        # Label e Entry Nascimento
        self.lb_nascimento_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                           text="Data de Nasc.*",
                                                           font=(
                                                               "Calibri", 16),
                                                           text_color=self.black,
                                                           fg_color=self.white).place(x=576, y=50)
        self.entry_nascimento_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                              width=160,
                                                              height=40,
                                                              border_width=1,
                                                              border_color=self.black,
                                                              fg_color=self.gray_light,
                                                              font=(
                                                                  "Calibri", 16),
                                                              text_color=self.black)
        self.entry_nascimento_agendamento_paciente.place(x=576, y=80)

        # Gênero
        self.lb_genero_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Gênero",
                                                       font=(
                                                           "Calibri", 16),
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
                                     border_width=1,
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
                                                             "Calibri", 16),
                                                         text_color=self.black,
                                                         fg_color=self.white).place(x=932, y=50)
        self.entry_endereco_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                            width=288,
                                                            height=40,
                                                            border_width=1,
                                                            border_color=self.black,
                                                            fg_color=self.gray_light,
                                                            font=(
                                                                "Calibri", 16),
                                                            text_color=self.black)
        self.entry_endereco_agendamento_paciente.place(x=932, y=80)

        # Label e Entry Bairro
        self.lb_bairro_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Bairro",
                                                       font=(
                                                           "Calibri", 16),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=24, y=130)
        self.entry_bairro_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                          width=188,
                                                          height=40,
                                                          border_width=1,
                                                          border_color=self.black,
                                                          fg_color=self.gray_light,
                                                          font=("Calibri", 16),
                                                          text_color=self.black)
        self.entry_bairro_agendamento_paciente.place(x=24, y=160)

        # Label e Entry Cidade
        self.lb_cidade_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Cidade",
                                                       font=(
                                                           "Calibri", 16),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=230, y=130)
        self.entry_cidade_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                          width=220,
                                                          height=40,
                                                          border_width=1,
                                                          border_color=self.black,
                                                          fg_color=self.gray_light,
                                                          font=("Calibri", 16),
                                                          text_color=self.black)
        self.entry_cidade_agendamento_paciente.place(x=230, y=160)

        # Label e Entry Número
        self.lb_numero_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                       text="Número",
                                                       font=(
                                                           "Calibri", 16),
                                                       text_color=self.black,
                                                       fg_color=self.white).place(x=468, y=130)
        self.entry_numero_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                          width=90,
                                                          height=40,
                                                          border_width=1,
                                                          border_color=self.black,
                                                          fg_color=self.gray_light,
                                                          font=("Calibri", 16),
                                                          text_color=self.black)
        self.entry_numero_agendamento_paciente.place(x=468, y=160)

        # Label e Entry E-Mail
        self.lb_email_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                      text="E-Mail",
                                                      font=(
                                                          "Calibri", 16),
                                                      text_color=self.black,
                                                      fg_color=self.white).place(x=576, y=130)
        self.entry_email_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                         width=280,
                                                         height=40,
                                                         border_width=1,
                                                         border_color=self.black,
                                                         fg_color=self.gray_light,
                                                         font=("Calibri", 16),
                                                         text_color=self.black)
        self.entry_email_agendamento_paciente.place(x=576, y=160)

        # Label e Entry Celular
        self.lb_celular_agendamento_paciente = CTkLabel(self.tb_agendar_consulta,
                                                        text="Celular*",
                                                        font=(
                                                            "Calibri", 16),
                                                        text_color=self.black,
                                                        fg_color=self.white).place(x=874, y=130)
        self.entry_celular_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                           width=168,
                                                           height=40,
                                                           border_width=1,
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
                                                             "Calibri", 16),
                                                         text_color=self.black,
                                                         fg_color=self.white).place(x=1060, y=130)
        self.entry_telefone_agendamento_paciente = CTkEntry(self.tb_agendar_consulta,
                                                            width=160,
                                                            height=40,
                                                            border_width=1,
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
                                           height=96,
                                           fg_color=self.white,
                                           border_color=self.blue_light_1,
                                           border_width=3).place(x=10, y=260)

        self.lb_dados_medico = CTkLabel(self.tb_agendar_consulta,
                                        width=160,
                                        text='Dados do Médico',
                                        font=('Calibri', 18, 'bold'),
                                        corner_radius=6,
                                        text_color=self.black).place(x=2, y=230)

        # Label e Entry CRM
        self.lb_crm_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                  text="CRM",
                                                  font=(
                                                      "Calibri", 16),
                                                  text_color=self.black,
                                                  fg_color=self.white).place(x=24, y=270)
        self.entry_crm_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                     width=150,
                                                     height=40,
                                                     border_width=1,
                                                     border_color=self.black,
                                                     fg_color=self.gray_light,
                                                     font=("Calibri", 16),
                                                     text_color=self.black)
        self.entry_crm_agendamento_medico.place(x=24, y=300)

        # Label e Entry Médico
        self.lb_nome_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                   text="Médico",
                                                   font=(
                                                       "Calibri", 16),
                                                   text_color=self.black,
                                                   fg_color=self.white).place(x=190, y=270)
        self.entry_nome_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                      width=356,
                                                      height=40,
                                                      border_width=1,
                                                      border_color=self.black,
                                                      fg_color=self.gray_light,
                                                      font=("Calibri", 16),
                                                      text_color=self.black)
        self.entry_nome_agendamento_medico.place(x=190, y=300)

        # Label e Entry Especialidade 1
        self.lb_especialidade1_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                             text="Especialidade 1",
                                                             font=(
                                                                 "Calibri", 16),
                                                             text_color=self.black,
                                                             fg_color=self.white).place(x=564, y=270)
        self.entry_especialidade1_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                                width=320,
                                                                height=40,
                                                                border_width=1,
                                                                border_color=self.black,
                                                                fg_color=self.gray_light,
                                                                font=(
                                                                    "Calibri", 16),
                                                                text_color=self.black)
        self.entry_especialidade1_agendamento_medico.place(x=564, y=300)

        # Label e Entry Especialidade 2
        self.lb_especialidade2_agendamento_medico = CTkLabel(self.tb_agendar_consulta,
                                                             text="Especialidade 2",
                                                             font=(
                                                                 "Calibri", 16),
                                                             text_color=self.black,
                                                             fg_color=self.white).place(x=900, y=270)
        self.entry_especialidade2_agendamento_medico = CTkEntry(self.tb_agendar_consulta,
                                                                width=320,
                                                                height=40,
                                                                border_width=1,
                                                                border_color=self.black,
                                                                fg_color=self.gray_light,
                                                                font=(
                                                                    "Calibri", 16),
                                                                text_color=self.black)
        self.entry_especialidade2_agendamento_medico.place(x=900, y=300)

        # Dados do Agendamento
        # Frame dos dados do médico
        self.frame_dados_agendamento = CTkFrame(self.tb_agendar_consulta,
                                                width=1224,
                                                height=96,
                                                fg_color=self.white,
                                                border_color=self.blue_light_1,
                                                border_width=3).place(x=10, y=400)

        self.lb_dados_agendamento = CTkLabel(self.tb_agendar_consulta,
                                             width=160,
                                             text='Dados do Agendamento',
                                             font=('Calibri', 18, 'bold'),
                                             corner_radius=6,
                                             text_color=self.black).place(x=10, y=372)

        # Label e Entry Data Agendamento
        self.lb_data_agendamento = CTkLabel(self.tb_agendar_consulta,
                                            text="Data Agend.*",
                                            font=(
                                                "Calibri", 16),
                                            text_color=self.black,
                                            fg_color=self.white).place(x=24, y=410)
        self.entry_data_agendamento = CTkEntry(self.tb_agendar_consulta,
                                               width=180,
                                               height=40,
                                               border_width=1,
                                               border_color=self.black,
                                               fg_color=self.gray_light,
                                               font=("Calibri", 16),
                                               text_color=self.black)
        self.entry_data_agendamento.place(x=24, y=440)

        # Label e Entry Horário do Agendamento
        self.lb_horario_agendamento = CTkLabel(self.tb_agendar_consulta,
                                               text="Horário Agend.*",
                                               font=(
                                                   "Calibri", 16),
                                               text_color=self.black,
                                               fg_color=self.white).place(x=222, y=410)
        self.entry_horario_agendamento = CTkEntry(self.tb_agendar_consulta,
                                                  width=180,
                                                  height=40,
                                                  border_width=1,
                                                  border_color=self.black,
                                                  fg_color=self.gray_light,
                                                  font=("Calibri", 16),
                                                  text_color=self.black)
        self.entry_horario_agendamento.place(x=222, y=440)

        # Label e Entry Observação
        self.lb_observacao_agendamento = CTkLabel(self.tb_agendar_consulta,
                                                  text="Observação",
                                                  font=(
                                                      "Calibri", 16),
                                                  text_color=self.black,
                                                  fg_color=self.white).place(x=420, y=410)
        self.entry_observacao_agendamento = CTkEntry(self.tb_agendar_consulta,
                                                     width=800,
                                                     height=40,
                                                     border_width=1,
                                                     border_color=self.black,
                                                     fg_color=self.gray_light,
                                                     font=("Calibri", 16),
                                                     text_color=self.black)
        self.entry_observacao_agendamento.place(x=420, y=440)

        # Aviso
        # Frame de aviso
        self.bane_aviso_agendamento = CTkFrame(master=self.tb_agendar_consulta,
                                               width=700,
                                               height=48,
                                               fg_color=self.blue_light_1,
                                               border_color=self.blue,
                                               border_width=3).place(x=10, y=530,)
        self.lb_aviso_agendamento = CTkLabel(master=self.tb_agendar_consulta,
                                             text="●  Atenção: Certifique-se de que todos os campos estão devidamente preenchidos antes de agendar a consulta.",
                                             text_color=self.black,
                                             font=("Calibri", 14, "bold"),
                                             fg_color=self.blue_light_1).place(x=24, y=540)

        # Botões
        # Botão de Limpar
        self.bt_limpar_agendamento = CTkButton(self.tb_agendar_consulta,
                                               text="Limpar",
                                               text_color=self.blue,
                                               font=(
                                                   "Calibri", 16, "bold"),
                                               width=126,
                                               height=48,
                                               fg_color=self.white,
                                               hover_color=self.blue_light_2,
                                               border_width=2,
                                               border_color=self.blue,
                                               command=self.limpar_agendamento).place(x=960, y=612)
        # Botão de Buscar
        self.bt_disponibilidade_agendamento = CTkButton(self.tb_agendar_consulta,
                                                        text="Agendar",
                                                        text_color=self.white,
                                                        font=(
                                                            "Calibri", 16, "bold"),
                                                        width=126,
                                                        height=48,
                                                        fg_color=self.blue,
                                                        hover_color=self.dark_blue
                                                        ).place(x=1108, y=612)

    def widget_consultar_agendamento(self):

        # Dados de Busca
        # Frame dos dados do paciente
        self.frame_dados_paciente = CTkFrame(self.tb_consultar_agendamento,
                                             width=1224,
                                             height=96,
                                             fg_color=self.white,
                                             border_color=self.blue_light_1,
                                             border_width=3).place(x=10, y=42)

        self.lb_buscar_agendamento = CTkLabel(self.tb_consultar_agendamento,
                                              width=160,
                                              text='Dados de Busca',
                                              font=('Calibri', 18, 'bold'),
                                              corner_radius=6,
                                              text_color=self.black).place(x=0, y=12)

        # Labels e Entrys
        # Label e Entry Numero Agendamento
        self.lb_numero_agendamento_busca = CTkLabel(self.tb_consultar_agendamento,
                                                    text="Número do Agend.",
                                                    font=(
                                                         "Calibri", 16),
                                                    text_color=self.black,
                                                    fg_color=self.white).place(x=24, y=50)
        self.entry_numero_agendamento_busca = CTkEntry(self.tb_consultar_agendamento,
                                                       width=158,
                                                       height=40,
                                                       border_width=1,
                                                       border_color=self.black,
                                                       fg_color=self.gray_light,
                                                       font=("Calibri", 16),
                                                       text_color=self.black)
        self.entry_numero_agendamento_busca.place(x=24, y=80)

        # Label e Entry CPF
        self.lb_cpf_agendamento_busca = CTkLabel(self.tb_consultar_agendamento,
                                                 text="CPF",
                                                 font=(
                                                     "Calibri", 16),
                                                 text_color=self.black,
                                                 fg_color=self.white).place(x=198, y=50)
        self.entry_cpf_agendamento_busca = CTkEntry(self.tb_consultar_agendamento,
                                                    width=180,
                                                    height=40,
                                                    border_width=1,
                                                    border_color=self.black,
                                                    fg_color=self.gray_light,
                                                    font=("Calibri", 16),
                                                    text_color=self.black)
        self.entry_cpf_agendamento_busca.place(x=198, y=80)

        # Label e Entry Nome
        self.lb_none_agendamento_paciente_busca = CTkLabel(self.tb_consultar_agendamento,
                                                           text="Nome Completo do Paciente",
                                                           font=(
                                                               "Calibri", 16),
                                                           text_color=self.black,
                                                           fg_color=self.white).place(x=394, y=50)
        self.entry_nome_agendamento_paciente_busca = CTkEntry(self.tb_consultar_agendamento,
                                                              width=360,
                                                              height=40,
                                                              border_width=1,
                                                              border_color=self.black,
                                                              fg_color=self.gray_light,
                                                              font=(
                                                                  "Calibri", 16),
                                                              text_color=self.black)
        self.entry_nome_agendamento_paciente_busca.place(x=394, y=80)

        # Botões
        # Botão de Limpar
        self.bt_limpar_buscar_agendamento = CTkButton(self.tb_consultar_agendamento,
                                                      text="Limpar",
                                                      text_color=self.blue,
                                                      font=(
                                                          "Calibri", 16, "bold"),
                                                      width=126,
                                                      height=48,
                                                      fg_color=self.blue_light_2,
                                                      hover_color=self.blue_light_1,
                                                      border_width=2,
                                                      border_color=self.blue,
                                                      command=self.limpar_buscar_agendamento).place(x=944, y=72)
        # Botão de Buscar
        self.bt_buscar_agendamento = CTkButton(self.tb_consultar_agendamento,
                                               text="Buscar",
                                               text_color=self.white,
                                               font=("Calibri", 16, "bold"),
                                               width=126,
                                               height=48,
                                               fg_color=self.blue,
                                               hover_color=self.dark_blue
                                               ).place(x=1092, y=72)

        # Resultado da busca
        # Frame dos dados do paciente
        self.frame_buscar_agendamento = CTkFrame(self.tb_consultar_agendamento,
                                                 width=1224,
                                                 height=480,
                                                 fg_color=self.white,
                                                 border_color=self.blue_light_1,
                                                 border_width=3).place(x=10, y=180)

        self.lb_buscar_agendamento = CTkLabel(self.tb_consultar_agendamento,
                                              width=160,
                                              text='Resultado da Busca',
                                              font=('Calibri', 18, 'bold'),
                                              text_color=self.black).place(x=10, y=150)

        self.scroll_treeview = ttk.Scrollbar(self.tb_consultar_agendamento)
        self.scroll_treeview.place(x=1200, y=190, width=20, height=460)

        self.lista_resultado_agendamento = ttk.Treeview(self.tb_consultar_agendamento, height=3, columns=(
            'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9',), yscrollcommand=self.scroll_treeview, selectmode='browse')
        self.lista_resultado_agendamento.place(
            x=20, y=190, width=1178, height=460)

        self.lista_resultado_agendamento.heading('#0', text='')
        self.lista_resultado_agendamento.heading('#1', text='Agend.')
        self.lista_resultado_agendamento.heading('#2', text='CPF')
        self.lista_resultado_agendamento.heading('#3', text='Nome')
        self.lista_resultado_agendamento.heading('#4', text='Celular')
        self.lista_resultado_agendamento.heading('#5', text='Médico')
        self.lista_resultado_agendamento.heading('#6', text='Especialidade')
        self.lista_resultado_agendamento.heading('#7', text='Data Cons.')
        self.lista_resultado_agendamento.heading('#8', text='Hor. Cons')
        self.lista_resultado_agendamento.heading('#9', text='Observação')

        self.lista_resultado_agendamento.column('#0', width=1)
        self.lista_resultado_agendamento.column('#1', width=50)
        self.lista_resultado_agendamento.column('#2', width=80)
        self.lista_resultado_agendamento.column('#3', width=200)
        self.lista_resultado_agendamento.column('#4', width=80)
        self.lista_resultado_agendamento.column('#5', width=200)
        self.lista_resultado_agendamento.column('#6', width=150)
        self.lista_resultado_agendamento.column('#7', width=70)
        self.lista_resultado_agendamento.column('#8', width=50)
        self.lista_resultado_agendamento.column('#9', width=200)

        self.lista_resultado_agendamento.insert(parent='', index="end", text='', values=(
            '1', '000.000.000.-71', 'Alex Souza', '7198823-4398', 'Marcelo Zcard', 'Ortopedista', '01/02/2025', '14:00', ''))

        self.lista_resultado_agendamento.insert(parent='', index="end", text='', values=(
            '2', '000.000.000.-71', 'Thales Silva', '7198823-4398', 'Luzia Mendes', 'Nutricionista', '01/02/2025', '13:00', ''))

        self.lista_resultado_agendamento.insert(parent='', index="end", text='', values=(
            '3', '000.000.000.-71', 'Orlando Blun', '7198823-4398', 'Fernando Lima', 'Dermatologista', '02/02/2025', '08:00', ''))

    def limpar_buscar_agendamento(self):
        self.entry_numero_agendamento_busca.delete(0, END)
        self.entry_cpf_agendamento_busca.delete(0, END)
        self.entry_nome_agendamento_paciente_busca.delete(0, END)

    def limpar_agendamento(self):
        # Limpa os Dados do Paciente
        self.entry_cpf_agendamento_paciente.delete(0, END)
        self.entry_nome_agendamento_paciente.delete(0, END)
        self.entry_nascimento_agendamento_paciente.delete(0, END)
        self.entry_endereco_agendamento_paciente.delete(0, END)
        self.entry_bairro_agendamento_paciente.delete(0, END)
        self.entry_cidade_agendamento_paciente.delete(0, END)
        self.entry_numero_agendamento_paciente.delete(0, END)
        self.entry_email_agendamento_paciente.delete(0, END)
        self.entry_celular_agendamento_paciente.delete(0, END)
        self.entry_telefone_agendamento_paciente.delete(0, END)
        # Limpa os Dados do Médico
        self.entry_crm_agendamento_medico.delete(0, END)
        self.entry_nome_agendamento_medico.delete(0, END)
        self.entry_especialidade1_agendamento_medico.delete(0, END)
        self.entry_especialidade2_agendamento_medico.delete(0, END)
        # Limpa os Dados do Agendamento
        self.entry_data_agendamento.delete(0, END)
        self.entry_horario_agendamento.delete(0, END)
        self.entry_observacao_agendamento.delete(0, END)


if __name__ == '__main__':
    app = MainWindow()

    app.mainloop()
