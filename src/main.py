from typing import Tuple
from customtkinter import *
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import Image, ImageTk
import sqlite3


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        # =========== Paleta de cores ===========
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.gray_dark = "#545454"
        self.black = "#000000"
        self.red = "#F2497C"
        self.red_light = "#FFE8F1"

        # =========== Configuração da Janela ===========
        self.title("Bem-Vindo!")
        self._set_appearance_mode("light")
        self.configure(fg_color=self.white)
        self.geometry("900x500+500+200")
        self.resizable(False, False)

        # =========== Monta a tabela de usuários do sistema ===========
        self.monta_tabela_usuario()

        # =========== Images, Background e Logo ===========
        # Background
        self.bg_img = CTkImage(
            light_image=Image.open('assets\imgs\BG_Inicial2.png'),
            dark_image=Image.open('assets\imgs\BG_Inicial2.png'),
            size=(579, 500)
        )
        # label da imagem de fundo
        self.lb_image = CTkLabel(
            self,
            image=self.bg_img,
            text='',
            fg_color=self.white
        ).place(x=0, y=0)
        # Imagem do logo
        self.logo_img = CTkImage(
            light_image=Image.open('assets\imgs\logo.png'),
            dark_image=Image.open('assets\imgs\logo.png'),
            size=(169, 24)
        )
        # Label da Imagem de Logo
        self.lb_logo = CTkLabel(
            self,
            image=self.logo_img,
            text='',
            fg_color=self.white
        ).place(x=655, y=24)

        # =========== Frames ===========
        # Frame do login
        self.fr_login = CTkFrame(
            self,
            width=321,
            height=340,
            fg_color=self.blue_light_2,
            corner_radius=16,
        ).place(x=579, y=200)

        # =========== Widgets ===========
        # Titulo
        self.titulo = CTkLabel(
            self,
            text='Bem-vindo de\nvolta!',
            text_color=self.black,
            font=('Segoe UI', 28, 'bold'),
            justify='left'
        ).place(x=610, y=80)
        # Subtitulo
        self.subtitulo = CTkLabel(
            self,
            text='Faça o login para acessar sua conta:',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal'),
        ).place(x=610, y=154)

        # Labels e Entrys
        # Label e Entry Usuário
        self.lb_usuario = CTkLabel(
            self,
            text='Usuário',
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            fg_color=self.blue_light_2
        ).place(x=610, y=234)
        self.entry_usuario = CTkEntry(
            self,
            width=260,
            height=32,
            font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            border_color=self.dark_blue,
            border_width=1.5,
            corner_radius=8,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            placeholder_text='Ex. usuario123',
            placeholder_text_color=self.gray_dark
        )
        self.entry_usuario.place(x=610, y=258)
        # Label e Entry Senha
        self.lb_senha = CTkLabel(
            self,
            text='Senha',
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            fg_color=self.blue_light_2
        ).place(x=610, y=296)
        self.entry_senha = CTkEntry(
            self,
            width=260,
            height=32,
            font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            border_color=self.dark_blue,
            border_width=1.5,
            corner_radius=8,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            placeholder_text='Insira sua senha',
            placeholder_text_color=self.gray_dark,
            show='*'
        )
        self.entry_senha.place(x=610, y=320)

        # Botão
        # Botão Entrar
        self.bt_entrar = CTkButton(
            self,
            width=220,
            height=34,
            text='Entrar',
            font=('Segoe UI', 12, 'bold'),
            text_color=self.white,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            corner_radius=8,
            command=self.login
        ).place(x=630, y=366)

        # Rodapé
        # Texto
        self.subtitulo = CTkLabel(
            self,
            text='Dúvidas ou problemas? Entre em contato\ncom nosso suporte técnico.',
            text_color=self.gray_dark,
            font=('Segoe UI', 10, 'normal'),
            justify='center',
            fg_color=self.blue_light_2
        ).place(x=648, y=456)

    def login(self):

        self.conecta_bd()
        self.__usuario = self.entry_usuario.get()
        self.__senha = self.entry_senha.get()

        self.cursor.execute("""
                                SELECT usuario, senha FROM usuarios
                                WHERE usuario = ? AND senha = ?
                            """, (self.__usuario, self.__senha))

        self.__resultado = self.cursor.fetchall()
        print(self.__resultado)

        if self.__resultado:
            print('Login efetuado com sucesso!')
            # Limpa as entrys de login
            self.entry_usuario.delete(0, END)
            self.entry_senha.delete(0, END)
            # Exclui a janela MainWindows, mas não a destrói
            self.withdraw()
            # Chama a janela principal
            PrincipalWindow(self)
        else:
            print('Usuário ou senha incorreta!')
            # Muda as cores do entry de usuario e senha
            self.entry_usuario.configure(fg_color=self.red_light, border_color=self.red,
                                         placeholder_text='Usuário invalido', placeholder_text_color=self.red,
                                         text_color=self.black)

            self.entry_senha.configure(fg_color=self.red_light, border_color=self.red,
                                       placeholder_text='Senha invalida', placeholder_text_color=self.red,
                                       text_color=self.black, show='*')

            # Limpa as entrys de login
            self.entry_usuario.delete(0, END)
            self.entry_senha.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('usuarios.bd')
        self.cursor = self.conn.cursor()
        print('Conectado ao banco de dados')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectado do banco de dados')

    def monta_tabela_usuario(self):
        self.conecta_bd()
        self.cursor.execute(""" 
                            CREATE TABLE IF NOT EXISTS usuarios (
                                id_usuario INTEGER PRIMARY KEY,
                                usuario TEXT NOT NULL,
                                senha TEXT NOT NULL,
                                nivel TEXT NOT NULL
                            );
                        """)
        self.conn.commit()
        self.desconecta_bd()

    def cadastro_usuario(self):
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO usuarios (usuario, senha, nivel)
                                VALUES(?, ?, ?)""", (self.entry_usuario.get(), self.entry_usuario.get(), 'Admin'))
        self.conn.commit()
        self.desconecta_bd()


class PrincipalWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # =========== Paleta de cores ===========
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.gray_light2 = '#F5F6FA'
        self.gray_dark = "#545454"
        self.black = "#000000"
        self.red = "#F2497C"
        self.red_light = "#FFE8F1"

        # =========== Configuração da Janela ===========
        self.title("Home")  # Titulo da janela
        self.configure(fg_color=self.gray_light2)  # Cor da janela
        self.geometry("1200x700+370+130")  # Tamanho da janela
        self.resizable(False, False)

        # =========== Top Bar ===========
        # Frame
        self.fr_topbar = CTkFrame(
            self,
            width=995,
            height=53,
            fg_color=self.blue,
            corner_radius=0
        )
        self.fr_topbar.place(x=205, y=0)
        # Label do BG do Topbar
        self.img_bg_topbar = CTkImage(
            Image.open('assets/imgs/bg_topbar.png'),
            size=(691, 52))
        self.lb_bg_topbar = CTkLabel(
            self.fr_topbar,
            image=self.img_bg_topbar,
            text='',
            fg_color=self.blue
        ).place(x=310, y=0)

        # Label do Ícone de Usuário
        self.icon_user = CTkImage(
            Image.open('assets/icons/icon_pack/user.png'),
            size=(32, 32))
        self.lb_icon_user = CTkLabel(
            self.fr_topbar,
            image=self.icon_user,
            text='',
            fg_color=self.blue
        ).place(x=24, y=10)
        # Label do nome do Usuário
        self.lb_nome_usuario = CTkLabel(
            self.fr_topbar,
            text='Bruno Álex',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            height=12
        ).place(x=64, y=10)
        # Label do nível de acesso
        self.lb_nivel_acesso = CTkLabel(
            self.fr_topbar,
            text='Admin',
            text_color=self.white,
            font=('Segoe UI', 12, 'normal'),
            height=12
        ).place(x=64, y=28)

        # =========== Menu Lateral ===========
        # Frame
        self.fr_menu_lateral = CTkFrame(
            self,
            width=209,
            height=702,
            fg_color=self.white,
            bg_color=self.gray,
            border_color=self.gray,
            border_width=1,
            corner_radius=0
        )
        self.fr_menu_lateral.place(x=-2, y=0)
        # Logo
        self.img_logo = CTkImage(
            light_image=Image.open('assets\imgs\Logo_black.png'),
            dark_image=Image.open('assets\imgs\Logo_black.png'),
            size=(169, 24)
        )
        # Label do Logo
        self.lb_img_logo = CTkLabel(
            self.fr_menu_lateral,
            image=self.img_logo,
            text='',
            fg_color=self.white
        ).place(x=21, y=48)

        # Botões do menu lateral
        # Botão Dashboard
        self.icon_bt_dashboard = CTkImage(
            Image.open('assets/icons/icon_pack/graph.png'))
        self.bt_dashboard = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_dashboard,
            compound='left',
            text='  Dashboard',
            text_color=self.white,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            corner_radius=8,
            anchor=W
        )
        self.bt_dashboard.place(x=12, y=126)
        # Botão Consultas
        self.icon_bt_consultas = CTkImage(
            Image.open('assets/icons/icon_pack/clipboard.png'))
        self.bt_consultas = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_consultas,
            compound='left',
            text='  Consultas',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W,
            command=self.open_consulta
        )
        self.bt_consultas.place(x=12, y=174)
        # Botão Cadastros
        self.icon_bt_cadastro = CTkImage(Image.open(
            'assets/icons/icon_pack/personalcard.png'))
        self.bt_cadastro = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_cadastro,
            compound='left',
            text='  Cadastro',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W,
            command=self.open_cadastro
        )
        self.bt_cadastro.place(x=12, y=222)
        # Botão Pacientes
        self.icon_bt_pacientes = CTkImage(
            Image.open('assets/icons/icon_pack/people.png'))
        self.bt_pacientes = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_pacientes,
            compound='left',
            text='  Pacientes',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W
        )
        self.bt_pacientes.place(x=12, y=270)
        # Botão Médicos
        self.icon_bt_medico = CTkImage(Image.open(
            'assets/icons/icon_pack/personalcard.png'))
        self.bt_medicos = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_medico,
            compound='left',
            text='  Médicos',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W
        )
        self.bt_medicos.place(x=12, y=318)
        # Botão Exportar dados
        self.icon_bt_exportar = CTkImage(
            Image.open('assets/icons/icon_pack/document.png'))
        self.bt_exportar = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_exportar,
            compound='left',
            text='  Exportar dados',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W
        )
        self.bt_exportar.place(x=12, y=366)
        # Frame divisor
        self.fr_divisor = CTkFrame(
            self.fr_menu_lateral,
            width=154,
            height=2,
            fg_color=self.gray,
        ).place(x=27, y=422)
        # Botão Configurações
        self.icon_bt_configuracoes = CTkImage(
            Image.open('assets/icons/icon_pack/setting.png'))
        self.bt_configuracoes = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_configuracoes,
            compound='left',
            text='  Configurações',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W
        )
        self.bt_configuracoes.place(x=12, y=439)
        # Botão Logout
        self.icon_bt_logout = CTkImage(
            Image.open('assets/icons/icon_pack/logout.png'))
        self.bt_logout = CTkButton(
            self.fr_menu_lateral,
            image=self.icon_bt_logout,
            compound='left',
            text='  Logout',
            text_color=self.gray_dark,
            font=('Segoe UI', 13, 'normal'),
            width=185,
            height=40,
            fg_color=self.white,
            border_color=self.gray_light,
            hover_color=self.blue_light_2,
            corner_radius=8,
            anchor=W,
            command=self.logout
        )
        self.bt_logout.place(x=12, y=487)

        # =========== Main ===========
        # Titulo da Main
        self.lb_dashboard_main = CTkLabel(
            self,
            text='Dashboard',
            text_color=self.black,
            font=('Segoe UI', 18, 'bold')
        ).place(x=230, y=76)

        # Cards
        # Card de Consultas
        self.fr_card_consultas = CTkFrame(
            self,
            width=218,
            height=86,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=2,
            corner_radius=8,
        )
        self.fr_card_consultas.place(x=231, y=114)
        self.lb_total_consultas = CTkLabel(
            self,
            text='Total de Consultas',
            text_color=self.gray_dark,
            font=('Segoe UI', 12, 'normal'),
        ).place(x=247, y=124)
        self.lb_total_consultas_valor = CTkLabel(
            self,
            text='200',
            text_color=self.black,
            font=('Segoe UI', 32, 'bold'),
        )
        self.lb_total_consultas_valor.place(x=247, y=148)
        # Label do Ícone do Card de Consultas
        self.icon_card_consulta = CTkImage(
            Image.open('assets/icons/icon_pack/clipboard-card.png'),
            size=(52, 52))
        self.lb_card_consulta = CTkLabel(
            self.fr_card_consultas,
            image=self.icon_card_consulta,
            text='',
            fg_color=self.white
        ).place(x=160, y=10)

        # Card de Consultas
        self.fr_card_pacientes = CTkFrame(
            self,
            width=218,
            height=86,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=2,
            corner_radius=8,
        )
        self.fr_card_pacientes.place(x=473, y=114)
        self.lb_total_pacientes = CTkLabel(
            self,
            text='Total de Pacientes',
            text_color=self.gray_dark,
            font=('Segoe UI', 12, 'normal'),
        ).place(x=489, y=124)
        self.lb_total_pacientes_valor = CTkLabel(
            self,
            text='172',
            text_color=self.black,
            font=('Segoe UI', 32, 'bold'),
        )
        self.lb_total_pacientes_valor.place(x=489, y=148)
        # Label do Ícone do Card de Consultas
        self.icon_card_pacientes = CTkImage(
            Image.open('assets/icons/icon_pack/people-card.png'),
            size=(52, 52))
        self.lb_card_pacientes = CTkLabel(
            self.fr_card_pacientes,
            image=self.icon_card_pacientes,
            text='',
            fg_color=self.white
        ).place(x=160, y=10)

        # Card de Médicos
        self.fr_card_medicos = CTkFrame(
            self,
            width=218,
            height=86,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=2,
            corner_radius=8,
        )
        self.fr_card_medicos.place(x=715, y=114)
        self.lb_total_medicos = CTkLabel(
            self,
            text='Total de Médicos',
            text_color=self.gray_dark,
            font=('Segoe UI', 12, 'normal'),
        ).place(x=731, y=124)
        self.lb_total_medicos_valor = CTkLabel(
            self,
            text='6',
            text_color=self.black,
            font=('Segoe UI', 32, 'bold'),
        )
        self.lb_total_medicos_valor.place(x=731, y=148)
        # Label do Ícone do Card de Consultas
        self.icon_card_medicos = CTkImage(
            Image.open('assets/icons/icon_pack/user-card.png'),
            size=(52, 52))
        self.lb_card_medicos = CTkLabel(
            self.fr_card_medicos,
            image=self.icon_card_medicos,
            text='',
            fg_color=self.white
        ).place(x=160, y=10)

        # Card de Funcionários
        self.fr_card_funcionarios = CTkFrame(
            self,
            width=218,
            height=86,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=2,
            corner_radius=8,
        )
        self.fr_card_funcionarios.place(x=957, y=114)
        self.lb_total_funcionarios = CTkLabel(
            self,
            text='Total de Funcionários',
            text_color=self.gray_dark,
            font=('Segoe UI', 12, 'normal'),
        ).place(x=973, y=124)
        self.lb_total_funcionarios_valor = CTkLabel(
            self,
            text='14',
            text_color=self.black,
            font=('Segoe UI', 32, 'bold'),
        )
        self.lb_total_funcionarios_valor.place(x=973, y=148)
        self.icon_card_funcionarios = CTkImage(
            Image.open('assets/icons/icon_pack/personal-card.png'),
            size=(52, 52))
        self.lb_card_funcionarios = CTkLabel(
            self.fr_card_funcionarios,
            image=self.icon_card_funcionarios,
            text='',
            fg_color=self.white
        ).place(x=160, y=10)

        # Frame principal
        self.fr_frame_principal = CTkFrame(
            self,
            width=944,
            height=462,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=2,
            corner_radius=8,
        ).place(x=231, y=218)

        # =========== Chama a função que fecha a janela ===========
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def open_cadastro(self):
        self.janela_consulta = CadastroWindow(self)
        self.janela_consulta

    def open_consulta(self):
        self.janela_consulta = ConsultaWindows(self)
        self.janela_consulta

    def close_window(self):
        # Função chamada quando a janela é fechada
        print('Janela fechada!')
        self.quit()

    def logout(self):
        print('Logout')
        MainWindow(self)


class CadastroWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # =========== Paleta de cores ===========
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.blue_light_3 = "#EEF7FF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.gray_light2 = '#F5F6FA'
        self.gray_dark = "#545454"
        self.black = "#000000"
        self.red = "#F2497C"
        self.red_light = "#FFE8F1"

        # =========== Configuração da Janela ===========
        self.title("Cadastro")  # Titulo da janela
        self.configure(fg_color=self.gray_light2)  # Cor da janela
        self.geometry("1200x700+300+130")  # Tamanho da janela
        self.resizable(False, False)

        # =========== Top Bar ===========
        # Frame
        self.fr_topbar = CTkFrame(
            self,
            width=1200,
            height=53,
            fg_color=self.blue,
            corner_radius=0
        )
        self.fr_topbar.place(x=0, y=0)
        # Label do BG do Topbar
        self.img_bg_topbar = CTkImage(
            Image.open('assets/imgs/bg_topbar.png'),
            size=(691, 52))
        self.lb_bg_topbar = CTkLabel(
            self.fr_topbar,
            image=self.img_bg_topbar,
            text='',
            fg_color=self.blue
        ).place(x=515, y=0)

        # Label do Ícone de Usuário
        self.icon_user = CTkImage(
            Image.open('assets/icons/icon_pack/user.png'),
            size=(32, 32))
        self.lb_icon_user = CTkLabel(
            self.fr_topbar,
            image=self.icon_user,
            text='',
            fg_color=self.blue
        ).place(x=24, y=10)
        # Label do nome do Usuário
        self.lb_nome_usuario = CTkLabel(
            self.fr_topbar,
            text='Bruno Álex',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            height=12
        ).place(x=64, y=10)
        # Label do nível de acesso
        self.lb_nivel_acesso = CTkLabel(
            self.fr_topbar,
            text='Admin',
            text_color=self.white,
            font=('Segoe UI', 12, 'normal'),
            height=12
        ).place(x=64, y=28)

        # =========== Formulário ===========
        # Tabview
        self.tbv_cadastros = CTkTabview(
            self,
            width=1152,
            height=610,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=1.5,
            corner_radius=8,
            text_color=self.white,
            segmented_button_fg_color=self.gray,
            segmented_button_selected_color=self.blue,
            segmented_button_selected_hover_color=self.dark_blue,
            segmented_button_unselected_color=self.gray_dark,
            anchor=W
        )
        self.tbv_cadastros.place(x=24, y=66)
        # Adicionando as abadas do Tabview
        self.tab_cadastro_paciente = self.tbv_cadastros.add(
            'Cadastro de Pacientes')
        self.tab_cadastro_medicos = self.tbv_cadastros.add(
            'Cadastro de Médicos')

        # Formulário de cadastro de pacientes
        self.cadastro_paciente()
        # Formulário de cadastro de médicos
        self.cadastro_medico()

    def cadastro_paciente(self):
        # Frame dos dados do paciente
        self.fr_dados_paciente = CTkFrame(
            self.tab_cadastro_paciente,
            width=1117,
            height=458,
            fg_color=self.blue_light_3,
            border_color=self.blue_light_1,
            border_width=1,
            corner_radius=6,
        )
        # Dados Pessoais do Paciente
        self.fr_dados_paciente.place(x=10, y=10)
        # Geral
        self.lb_campos_geral = CTkLabel(
            self.fr_dados_paciente,
            text='GERAL',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold')
        ).place(x=16, y=18)
        # Label e Entry do nome do paciente
        self.lb_nome_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Nome completo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=46)
        self.ent_nome_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=381,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_nome_paciente_cadastro.place(x=16, y=72)
        # Label e Entry do data de nascimento do paciente
        self.lb_nascimento_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Data de nascimento',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=413, y=46)
        self.ent_nascimento_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=214,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='dd/mm/aaaa'
        )
        self.ent_nascimento_paciente_cadastro.place(x=413, y=72)
        self.icon_bt_calendario_nascimento = CTkImage(
            Image.open('assets/icons/icon_pack/calendar-search.png'),
            size=(20, 20))
        self.bt_calendario_nascimento = CTkButton(
            self.fr_dados_paciente,
            width=32,
            height=32,
            text='',
            image=self.icon_bt_calendario_nascimento,
            compound='left',
            fg_color=self.blue_light_1,
            bg_color=self.blue_light_3,
            hover_color=self.blue_light_2,
            corner_radius=6,
            command=self.pop_calendario
        ).place(x=634, y=72)
        # Label e Entry do CPF do paciente
        self.lb_cpf_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='CPF',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=687, y=46)
        self.ent_cpf_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=210,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')

        )
        self.ent_cpf_paciente_cadastro.place(x=687, y=72)
        # Label e ComBox do Sexo do paciente
        self.lb_sexo_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Sexo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=913, y=46)
        self.cb_sexo_paciente_cadastro = CTkComboBox(
            self.fr_dados_paciente,
            width=186,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Masculino', 'Feminino', 'Não-binário',
                    'Agênero', 'Gênero fluido', 'Não declarado'])

        )
        self.cb_sexo_paciente_cadastro.place(x=913, y=72)

        # Dados de Endereço do Paciente
        # Endereço
        self.lb_campos_endereco = CTkLabel(
            self.fr_dados_paciente,
            text='ENDEREÇO',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold'),
            height=12
        ).place(x=16, y=124)
        # Label e Entry do CEP do paciente
        self.lb_cep_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='CEP',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=148)
        self.ent_cep_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=200,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_cep_paciente_cadastro.place(x=16, y=176)
        # Label e Entry do Endereço do paciente
        self.lb_endereco_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Endereço',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=232, y=148)
        self.ent_endereco_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=867,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_endereco_paciente_cadastro.place(x=232, y=176)
        # Label e Entry do Bairro do paciente
        self.lb_bairro_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Bairro',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=212)
        self.ent_bairro_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=373,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_bairro_paciente_cadastro.place(x=16, y=238)
        # Label e Entry do Cidade do paciente
        self.lb_cidade_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Cidade',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=405, y=212)
        self.ent_cidade_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=357,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_cidade_paciente_cadastro.place(x=405, y=238)
        # Label e Entry do Cidade do paciente
        self.lb_estado_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Estado',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=778, y=212)
        self.ent_estado_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=320,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_estado_paciente_cadastro.place(x=778, y=238)

        # Dados de Contato do
        # Contatos
        self.lb_campos_endereco = CTkLabel(
            self.fr_dados_paciente,
            text='CONTATOS',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold'),
            height=12
        ).place(x=16, y=292)
        # Label e Entry do Email do paciente
        self.lb_email_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='E-Mail',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=316)
        self.ent_email_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=341,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_email_paciente_cadastro.place(x=16, y=342)
        # Label e Entry do Observação do Email do paciente
        self.lb_observacao_email_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Observação',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=373, y=316)
        self.ent_observacao_email_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=726,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_observacao_email_paciente_cadastro.place(x=373, y=342)
        # Label e ComBox do Celular/Telefone do paciente
        self.lb_celular_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Celular/Telefone',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=380)
        self.cb_celular_paciente_cadastro = CTkComboBox(
            self.fr_dados_paciente,
            width=228,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Celular', 'Celular/WhatsApp', 'Telefone'])
        )
        self.cb_celular_paciente_cadastro.place(x=16, y=406)
        # Label e ComBox do Topo de contato do paciente
        self.lb_celular_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Tipo de contato',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=262, y=380)
        self.cb_celular_paciente_cadastro = CTkComboBox(
            self.fr_dados_paciente,
            width=228,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Pessoal', 'Residencial', 'Comercial'])
        )
        self.cb_celular_paciente_cadastro.place(x=262, y=406)
        # Label e Entry do Número do paciente
        self.lb_celular_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Número',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=508, y=380)
        self.ent_celular_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=200,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='Ex. 7190000-0000'
        )
        self.ent_celular_paciente_cadastro.place(x=508, y=406)
        # Label e Entry da Observação do Número do paciente
        self.lb_obsevacao_celular_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Observação',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=724, y=380)
        self.ent_obsevacao_celular_paciente_cadastro = CTkEntry(
            self.fr_dados_paciente,
            width=376,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_obsevacao_celular_paciente_cadastro.place(x=724, y=406)

        # Botões
        # Botão Limpar
        self.bt_cancelar_cadastro_paciente = CTkButton(
            self.tab_cadastro_paciente,
            width=148,
            height=40,
            text='Cancelar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.white,
            hover_color=self.blue_light_2,
            border_color=self.blue,
            border_width=1.5,
            corner_radius=8,
            command=self.fechar_cadastro
        )
        self.bt_cancelar_cadastro_paciente.place(x=26, y=500)
        # Botão Limpar
        self.bt_limpar_cadastro_paciente = CTkButton(
            self.tab_cadastro_paciente,
            width=148,
            height=40,
            text='Limpar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.blue_light_1,
            hover_color=self.blue_light_2,
            corner_radius=8,
            command=self.limpar_cadastro_paciente
        )
        self.bt_limpar_cadastro_paciente.place(x=792, y=500)
        # Botão Cadastrar
        self.bt_salvar_cadastro_paciente = CTkButton(
            self.tab_cadastro_paciente,
            width=148,
            height=40,
            text='Cadastrar',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.blue,
            hover_color=self.dark_blue,
            corner_radius=8
        )
        self.bt_salvar_cadastro_paciente.place(x=962, y=500)

    def cadastro_medico(self):
        # Frame dos dados do médico
        self.fr_dados_medico = CTkFrame(
            self.tab_cadastro_medicos,
            width=1117,
            height=458,
            fg_color=self.blue_light_3,
            border_color=self.blue_light_1,
            border_width=1,
            corner_radius=6,
        )
        self.fr_dados_medico.place(x=10, y=10)
        # Dados pessoais do médico
        # Geral
        self.lb_campos_geral_medico = CTkLabel(
            self.fr_dados_medico,
            text='GERAL',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold')
        ).place(x=16, y=18)
        # Label e Entry do codigo do medico
        self.lb_codigo_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Código',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=46)
        self.ent_codigo_paciente_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=90,
            height=32,
            fg_color=self.gray_light,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            state='disabled'
        )
        self.ent_codigo_paciente_cadastro.place(x=16, y=72)
        # Label e Entry do nome do medico
        self.lb_nome_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Nome completo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=122, y=46)
        self.ent_nome_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=363,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_nome_medico_cadastro.place(x=122, y=72)
        # Label e ComBox do CRM/CFM do médico
        self.lb_especialidade_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='CRM/CFM',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=501, y=46)
        self.cb_especialidade_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=200,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Clinico', 'Obstetra', 'Pediatra', 'Ortopedista',
                    'Dermatologista', 'Cardiologista', 'Ginecologista'])

        )
        self.cb_especialidade_paciente_cadastro.place(x=501, y=72)
        # Label e ComBox do Especialidade do médico
        self.lb_crm_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Especialidade',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=717, y=46)
        self.cb_crm_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=128,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['CRM', 'CFM'])

        )
        self.cb_crm_paciente_cadastro.place(x=717, y=72)
        # Label e Entry do numero do CRM/CFM do medico
        self.lb_numero_crm_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Número',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=861, y=46)
        self.ent_numero_crm_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=122,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_numero_crm_medico_cadastro.place(x=861, y=72)
        # Label e ComBox do UF do crm do médico
        self.lb_uf_crm_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='UF',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=999, y=46)
        self.cb_uf_crm_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=100,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                     'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
                     'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
                     ])

        )
        self.cb_uf_crm_paciente_cadastro.place(x=999, y=72)
        # Label e Entry do numero do CPF do medico
        self.lb_cpf_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='CPF',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=110)
        self.ent_cpf_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=186,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_cpf_medico_cadastro.place(x=16, y=134)
        # Label e Entry do numero do RG do medico
        self.lb_rg_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='RG',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=218, y=110)
        self.ent_rg_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=186,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_rg_medico_cadastro.place(x=218, y=134)
        # Label e ComBox do órgão do RG do médico
        self.lb_orgao_rg_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Órgão',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=420, y=110)
        self.cb_orgao_rg_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=117,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['SSP'])

        )
        self.cb_orgao_rg_paciente_cadastro.place(x=420, y=134)
        # Label e ComBox do UF do RG do médico
        self.lb_uf_rg_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='UF',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=553, y=110)
        self.cb_uf_rg_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=100,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                     'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
                     'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
                     ])

        )
        self.cb_uf_rg_paciente_cadastro.place(x=553, y=134)
        # Label e ComBox do Sexo do paciente
        self.lb_sexo_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Sexo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=669, y=110)
        self.cb_sexo_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=162,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Masculino', 'Feminino', 'Não-binário',
                    'Agênero', 'Gênero fluido', 'Não declarado'])

        )
        self.cb_sexo_paciente_cadastro.place(x=669, y=134)
        # Label e Entry do data de nascimento do paciente
        self.lb_nascimento_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Data de nascimento',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=847, y=110)
        self.ent_nascimento_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=210,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='dd/mm/aaaa'
        )
        self.ent_nascimento_medico_cadastro.place(x=847, y=134)
        self.icon_bt_calendario_nascimento_medico = CTkImage(
            Image.open('assets/icons/icon_pack/calendar-search.png'),
            size=(20, 20))
        self.bt_calendario_nascimento_medico = CTkButton(
            self.fr_dados_medico,
            width=32,
            height=32,
            text='',
            image=self.icon_bt_calendario_nascimento,
            compound='left',
            fg_color=self.blue_light_1,
            bg_color=self.blue_light_3,
            hover_color=self.blue_light_2,
            corner_radius=6,
            command=self.pop_calendario
        ).place(x=1063, y=134)

        # Dados de Endereço do Paciente
        # Endereço
        self.lb_campos_endereco_medico = CTkLabel(
            self.fr_dados_medico,
            text='ENDEREÇO',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold'),
            height=12
        ).place(x=16, y=186)
        # Label e Entry do CEP do medico
        self.lb_cep_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='CEP',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=208)
        self.ent_cep_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=141,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_cep_medico_cadastro.place(x=16, y=232)
        # Label e Entry do CEP do medico
        self.lb_endereco_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Endereço',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=173, y=208)
        self.ent_endereco_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=352,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_endereco_medico_cadastro.place(x=173, y=232)
        # Label e Entry do Numero do medico
        self.lb_numero_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Número',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=541, y=208)
        self.ent_numero_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=70,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_numero_medico_cadastro.place(x=541, y=232)
        # Label e Entry do Bairro do medico
        self.lb_bairro_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Bairro',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=627, y=208)
        self.ent_bairro_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=170,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_bairro_medico_cadastro.place(x=627, y=232)
        # Label e Entry do Cidade do medico
        self.lb_cidade_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Cidade',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=813, y=208)
        self.ent_cidade_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=177,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_cidade_medico_cadastro.place(x=813, y=232)
        # Label e ComBox do Estado do médico
        self.lb_estado_paciente_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Estado',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=1006, y=208)
        self.cb_estado_paciente_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=95,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                     'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
                     'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
                     ])

        )
        self.cb_estado_paciente_cadastro.place(x=1006, y=232)

        # Dados de Contato do
        # Contatos
        self.lb_campos_contato_medico = CTkLabel(
            self.fr_dados_medico,
            text='CONTATOS',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold'),
            height=12
        ).place(x=16, y=292)
        # Label e Entry do Email do paciente
        self.lb_email_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='E-Mail',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=316)
        self.ent_email_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=341,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_email_medico_cadastro.place(x=16, y=342)
        # Label e Entry do Observação do Email do paciente
        self.lb_observacao_email_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Observação',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=373, y=316)
        self.ent_observacao_email_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=726,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_observacao_email_medico_cadastro.place(x=373, y=342)
        # Label e ComBox do Celular/Telefone do paciente
        self.lb_celular_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Celular/Telefone',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=380)
        self.cb_celular_medico_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=228,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Celular', 'Celular/WhatsApp', 'Telefone'])
        )
        self.cb_celular_medico_cadastro.place(x=16, y=406)
        # Label e ComBox do Topo de contato do paciente
        self.lb_celular_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Tipo de contato',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=262, y=380)
        self.cb_celular_medico_cadastro = CTkComboBox(
            self.fr_dados_medico,
            width=228,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Pessoal', 'Residencial', 'Comercial'])
        )
        self.cb_celular_medico_cadastro.place(x=262, y=406)
        # Label e Entry do Número do paciente
        self.lb_celular_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Número',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=508, y=380)
        self.ent_celular_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=200,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='Ex. 7190000-0000'
        )
        self.ent_celular_medico_cadastro.place(x=508, y=406)
        # Label e Entry da Observação do Número do paciente
        self.lb_obsevacao_celular_medico_cadastro = CTkLabel(
            self.fr_dados_medico,
            text='Observação',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=724, y=380)
        self.ent_obsevacao_celular_medico_cadastro = CTkEntry(
            self.fr_dados_medico,
            width=376,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_obsevacao_celular_medico_cadastro.place(x=724, y=406)

        # Botões
        # Botão Cancelar
        self.bt_cancelar_cadastro_medico = CTkButton(
            self.tab_cadastro_medicos,
            width=148,
            height=40,
            text='Cancelar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.white,
            hover_color=self.blue_light_2,
            border_color=self.blue,
            border_width=1.5,
            corner_radius=8,
            command=self.fechar_cadastro
        )
        self.bt_cancelar_cadastro_medico.place(x=26, y=500)
        # Botão Limpar
        self.bt_limpar_cadastro_medico = CTkButton(
            self.tab_cadastro_medicos,
            width=148,
            height=40,
            text='Limpar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.blue_light_1,
            hover_color=self.blue_light_2,
            corner_radius=8,
            command=self.limpar_cadastro_medico
        )
        self.bt_limpar_cadastro_medico.place(x=792, y=500)
        # Botão Cadastrar
        self.bt_salvar_cadastro_medico = CTkButton(
            self.tab_cadastro_medicos,
            width=148,
            height=40,
            text='Cadastrar',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.blue,
            hover_color=self.dark_blue,
            corner_radius=8
        )
        self.bt_salvar_cadastro_medico.place(x=962, y=500)

    def limpar_cadastro_paciente(self):
        self.ent_nome_paciente_cadastro.delete(0, END)
        self.ent_nascimento_paciente_cadastro.delete(0, END)
        self.ent_cpf_paciente_cadastro.delete(0, END)
        self.ent_cep_paciente_cadastro.delete(0, END)
        self.ent_endereco_paciente_cadastro.delete(0, END)
        self.ent_bairro_paciente_cadastro.delete(0, END)
        self.ent_cidade_paciente_cadastro.delete(0, END)
        self.ent_estado_paciente_cadastro.delete(0, END)
        self.ent_email_paciente_cadastro.delete(0, END)
        self.ent_observacao_email_paciente_cadastro.delete(0, END)
        self.ent_celular_paciente_cadastro.delete(0, END)
        self.ent_obsevacao_celular_paciente_cadastro.delete(0, END)

    def limpar_cadastro_medico(self):
        self.ent_nome_medico_cadastro.delete(0, END)
        self.ent_numero_crm_medico_cadastro.delete(0, END)
        self.ent_cpf_medico_cadastro.delete(0, END)
        self.ent_rg_medico_cadastro.delete(0, END)
        self.ent_nascimento_medico_cadastro.delete(0, END)
        self.ent_cep_medico_cadastro.delete(0, END)
        self.ent_endereco_medico_cadastro.delete(0, END)
        self.ent_numero_medico_cadastro.delete(0, END)
        self.ent_bairro_medico_cadastro.delete(0, END)
        self.ent_cidade_medico_cadastro.delete(0, END)
        self.ent_email_medico_cadastro.delete(0, END)
        self.ent_observacao_email_medico_cadastro.delete(0, END)
        self.ent_celular_medico_cadastro.delete(0, END)
        self.ent_obsevacao_celular_medico_cadastro.delete(0, END)

    def pop_calendario(self):
        self.pop = CTkToplevel(
            self,
            fg_color=self.white
        )
        self.pop.geometry('386x287+780+350')
        self.pop.title('Calendário')
        self.pop.resizable(False, False)
        self.pop.grab_set()
        self.pop.focus_force()

        self.calendario = Calendar(
            self.pop,
            selectmode='day',
        )
        self.calendario.place(x=0, y=0, width=386, height=207)

        self.bt_confirmar = CTkButton(
            self.pop,
            text='Confirmar',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            width=167,
            height=36,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            command=self.get_data
        )
        self.bt_confirmar.place(x=18, y=231)
        self.bt_cancelar = CTkButton(
            self.pop,
            text='Cancelar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            width=167,
            height=36,
            fg_color=self.blue_light_1,
            hover_color=self.blue_light_2,
            command=self.fecha_calendario
        )
        self.bt_cancelar.place(x=201, y=231)

    def get_data(self):
        self.ent_nascimento_paciente_cadastro.delete(0, END)
        data_nascimento = self.calendario.get_date()
        self.ent_nascimento_paciente_cadastro.insert(END, data_nascimento)
        self.pop.destroy()

    def fecha_calendario(self):
        self.pop.destroy()

    def fechar_cadastro(self):
        self.destroy()


class ConsultaWindows(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # =========== Paleta de cores ===========
        self.dark_blue = "#0057A7"
        self.blue = "#0076E3"
        self.blue_light_1 = "#A5D4FF"
        self.blue_light_2 = "#DAEDFF"
        self.blue_light_3 = "#EEF7FF"
        self.white = "#FFFFFF"
        self.gray = "#BCBCBC"
        self.gray_light = "#F0F0F0"
        self.gray_light2 = '#F5F6FA'
        self.gray_dark = "#545454"
        self.black = "#000000"
        self.red = "#F2497C"
        self.red_light = "#FFE8F1"

        # =========== Configuração da Janela ===========
        self.title("Consultas")  # Titulo da janela
        self.configure(fg_color=self.gray_light2)  # Cor da janela
        self.geometry("1550x674+170+130")  # Tamanho da janela
        self.resizable(False, False)

        # =========== Top Bar ===========
        # Frame
        self.fr_topbar = CTkFrame(
            self,
            width=1550,
            height=53,
            fg_color=self.blue,
            corner_radius=0
        )
        self.fr_topbar.place(x=0, y=0)
        # Label do BG do Topbar
        self.img_bg_topbar = CTkImage(
            Image.open('assets/imgs/bg_topbar.png'),
            size=(691, 52))
        self.lb_bg_topbar = CTkLabel(
            self.fr_topbar,
            image=self.img_bg_topbar,
            text='',
            fg_color=self.blue
        ).place(x=858, y=0)

        # Label do Ícone de Usuário
        self.icon_user = CTkImage(
            Image.open('assets/icons/icon_pack/user.png'),
            size=(32, 32))
        self.lb_icon_user = CTkLabel(
            self.fr_topbar,
            image=self.icon_user,
            text='',
            fg_color=self.blue
        ).place(x=24, y=10)
        # Label do nome do Usuário
        self.lb_nome_usuario = CTkLabel(
            self.fr_topbar,
            text='Bruno Álex',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            height=12
        ).place(x=64, y=10)
        # Label do nível de acesso
        self.lb_nivel_acesso = CTkLabel(
            self.fr_topbar,
            text='Admin',
            text_color=self.white,
            font=('Segoe UI', 12, 'normal'),
            height=12
        ).place(x=64, y=28)

        # =========== Tabview ===========
        # Tabview
        self.tbv_consulta = CTkTabview(
            self,
            width=1502,
            height=580,
            fg_color=self.white,
            bg_color=self.gray_light2,
            border_color=self.gray,
            border_width=1.5,
            corner_radius=8,
            text_color=self.white,
            segmented_button_fg_color=self.gray,
            segmented_button_selected_color=self.blue,
            segmented_button_selected_hover_color=self.dark_blue,
            segmented_button_unselected_color=self.gray_dark,
            anchor=W
        )
        self.tbv_consulta.place(x=24, y=66)
        # Adicionando as abadas do Tabview
        self.tab_agendar_consulta = self.tbv_consulta.add(
            'Agendar Consulta')
        self.tab_buscar_consulta = self.tbv_consulta.add(
            'Buscar Consulta')

        self.agendar_consulta()

    def agendar_consulta(self):
        # Frame dos dados de agendamento
        self.fr_dados_agendamento = CTkFrame(
            self.tab_agendar_consulta,
            width=1458,
            height=418,
            fg_color=self.blue_light_3,
            border_color=self.blue_light_1,
            border_width=1,
            corner_radius=6,
        )
        self.fr_dados_agendamento.place(x=14, y=10)

        # Dados do paciente
        self.lb_campos_dados_paciente = CTkLabel(
            self.fr_dados_agendamento,
            text='DADOS DO PACIENTE',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold')
        ).place(x=16, y=18)
        # Label e Entry do nome do paciente
        # Botão de buscar paciente
        self.bt_buscar_paciente = CTkButton(
            self.fr_dados_agendamento,
            width=131,
            height=32,
            text='Buscar paciente',
            compound='left',
            fg_color=self.blue,
            bg_color=self.blue_light_3,
            hover_color=self.dark_blue,
            corner_radius=6
        ).place(x=16, y=72)
        # Label e Entry do nome do paciente
        self.lb_nome_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Nome completo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=163, y=46)
        self.ent_nome_paciente_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=342,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_nome_paciente_agendamento.place(x=163, y=72)
        # Label e Entry do data de nascimento do paciente
        self.lb_nascimento_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Data de nascimento',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=521, y=46)
        self.ent_nascimento_paciente_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=150,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='dd/mm/aaaa'
        )
        self.ent_nascimento_paciente_agendamento.place(x=521, y=72)
        self.icon_bt_calendario_nascimento = CTkImage(
            Image.open('assets/icons/icon_pack/calendar-search.png'),
            size=(20, 20))
        self.bt_calendario_nascimento_agendamento = CTkButton(
            self.fr_dados_agendamento,
            width=32,
            height=32,
            text='',
            image=self.icon_bt_calendario_nascimento,
            compound='left',
            fg_color=self.blue_light_1,
            bg_color=self.blue_light_3,
            hover_color=self.blue_light_2,
            corner_radius=6
        ).place(x=678, y=72)
        # Label e Entry do CPF do paciente
        self.lb_cpf_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='CPF',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=730, y=46)
        self.ent_cpf_paciente_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=178,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')

        )
        self.ent_cpf_paciente_agendamento.place(x=730, y=72)
        # Label e ComBox do Sexo do paciente
        self.lb_sexo_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Sexo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=924, y=46)
        self.cb_sexo_paciente_agendamento = CTkComboBox(
            self.fr_dados_agendamento,
            width=176,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Masculino', 'Feminino', 'Não-binário',
                    'Agênero', 'Gênero fluido', 'Não declarado'])

        )
        self.cb_sexo_paciente_agendamento.place(x=924, y=72)
        # Label e Entry do Email do paciente
        self.lb_email_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='E-Mail',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=1116, y=46)
        self.ent_email_paciente_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=324,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_email_paciente_agendamento.place(x=1116, y=72)
        # Label e ComBox do Celular/Telefone do paciente
        self.lb_celular_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Celular/Telefone',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=108)
        self.cb_celular_paciente_agendamento = CTkComboBox(
            self.fr_dados_agendamento,
            width=228,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Celular', 'Celular/WhatsApp', 'Telefone'])
        )
        self.cb_celular_paciente_agendamento.place(x=16, y=134)
        # Label e ComBox do Topo de contato do paciente
        self.lb_celular_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Tipo de contato',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=262, y=108)
        self.cb_celular_paciente_agendamento = CTkComboBox(
            self.fr_dados_agendamento,
            width=228,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Pessoal', 'Residencial', 'Comercial'])
        )
        self.cb_celular_paciente_agendamento.place(x=262, y=134)
        # Label e Entry do Número do paciente
        self.lb_celular_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Número',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=508, y=108)
        self.ent_celular_paciente_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=200,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='Ex. 7190000-0000'
        )
        self.ent_celular_paciente_agendamento.place(x=508, y=134)
        # Label e Entry da Observação do Número do paciente
        self.lb_obsevacao_celular_paciente_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Observação',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=725, y=108)
        self.ent_obsevacao_celular_paciente_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=716,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_obsevacao_celular_paciente_agendamento.place(x=725, y=134)

        # Dados do médico
        self.lb_campos_dados_medico = CTkLabel(
            self.fr_dados_agendamento,
            text='DADOS DO MÉDICO',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold')
        ).place(x=16, y=190)
        # Label e Entry do nome do paciente
        # Botão de buscar médico
        self.bt_buscar_medico = CTkButton(
            self.fr_dados_agendamento,
            width=131,
            height=32,
            text='Buscar médico',
            compound='left',
            fg_color=self.blue,
            bg_color=self.blue_light_3,
            hover_color=self.dark_blue,
            corner_radius=6
        ).place(x=16, y=244)
        # Label e Entry do nome do médico
        self.lb_nome_medico_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Nome do médico',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=164, y=218)
        self.ent_nome_medico_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=434,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_nome_medico_agendamento.place(x=164, y=244)
        # Label e Entry do especialidade do médico
        self.lb_especialidade1_medico_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Especialidade 1',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=618, y=218)
        self.ent_especialidade1_medico_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=272,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_especialidade1_medico_agendamento.place(x=618, y=244)
        # Label e Entry do especialidade do médico
        self.lb_especialidade2_medico_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Especialidade 2',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=908, y=218)
        self.ent_especialidade2_medico_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=272,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_especialidade2_medico_agendamento.place(x=908, y=244)
        # Label e Entry do crm do médico
        self.lb_crm_medico_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='CRM/CFM',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=1198, y=218)
        self.ent_crm_medico_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=242,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_crm_medico_agendamento.place(x=1198, y=244)

        # Dados da Consulta
        self.lb_campos_dados_consulta = CTkLabel(
            self.fr_dados_agendamento,
            text='DADOS DA CONSULTA',
            text_color=self.black,
            font=('Segoe UI', 14, 'bold')
        ).place(x=16, y=300)
        # Label e Entry do nome do paciente
        # Label e Entry do Convênio médico
        self.lb_convenio_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Convênio médico',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=16, y=328)
        self.cb_convenio_agendamento = CTkComboBox(
            self.fr_dados_agendamento,
            width=150,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(['Sim', 'Não'])
        )
        self.cb_convenio_agendamento.place(x=16, y=354)
        # Label e Entry do plano médico
        self.lb_plano_saude_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Convênio médico',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=184, y=328)
        self.cb_plano_saude_agendamento = CTkComboBox(
            self.fr_dados_agendamento,
            width=350,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            button_color=self.blue,
            button_hover_color=self.dark_blue,
            dropdown_fg_color=self.white,
            dropdown_hover_color=self.blue_light_2,
            dropdown_text_color=self.black,
            dropdown_font=('Segoe UI', 14, 'normal'),
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            values=(["Amil", "Bradesco Saúde", "SulAmérica Saúde", "Unimed",
                     "Golden Cross", "Hapvida", "NotreDame Intermédica",
                     "Porto Seguro Saúde", "São Francisco Saúde", "Medial Saúde", 'SUS'])
        )
        self.cb_plano_saude_agendamento.place(x=184, y=354)
        # Label e Entry do data da consulta medica
        self.lb_data_consulta_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Data da consulta',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=554, y=328)
        self.ent_data_consulta_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=170,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='dd/mm/aaaa'
        )
        self.ent_data_consulta_agendamento.place(x=554, y=354)
        self.icon_bt_calendario_nascimento = CTkImage(
            Image.open('assets/icons/icon_pack/calendar-search.png'),
            size=(20, 20))
        self.bt_calendario_data_agendamento = CTkButton(
            self.fr_dados_agendamento,
            width=32,
            height=32,
            text='',
            image=self.icon_bt_calendario_nascimento,
            compound='left',
            fg_color=self.blue_light_1,
            bg_color=self.blue_light_3,
            hover_color=self.blue_light_2,
            corner_radius=6
        ).place(x=732, y=354)
        # Label e Entry do hora da consulta medica
        self.lb_observacao_convenio_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Horário da consulta',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=788, y=328)
        self.ent_hora_consulta_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=170,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal'),
            placeholder_text='EX. 09:30'
        )
        self.ent_hora_consulta_agendamento.place(x=788, y=354)
        # Label e Entry do observação do plano de saúde
        self.lb_observacao_convenio_agendamento = CTkLabel(
            self.fr_dados_agendamento,
            text='Observação',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=978, y=328)
        self.ent_observacao_convenio_agendamento = CTkEntry(
            self.fr_dados_agendamento,
            width=462,
            height=32,
            fg_color=self.white,
            bg_color=self.blue_light_2,
            corner_radius=6,
            border_color=self.black,
            border_width=1,
            text_color=self.black,
            font=('Segoe UI', 14, 'normal')
        )
        self.ent_observacao_convenio_agendamento.place(x=978, y=354)
        
        # Botões
        # Botão Cancelar
        self.bt_cancelar_cadastro_paciente = CTkButton(
            self.tbv_consulta,
            width=148,
            height=40,
            text='Cancelar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.white,
            hover_color=self.blue_light_2,
            border_color=self.blue,
            border_width=1.5,
            corner_radius=8,
            command=self.fechar_consulta
        )
        self.bt_cancelar_cadastro_paciente.place(x=38, y=510)
        # Botão Limpar
        self.bt_limpar_cadastro_paciente = CTkButton(
            self.tbv_consulta,
            width=148,
            height=40,
            text='Limpar',
            text_color=self.blue,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.blue_light_1,
            hover_color=self.blue_light_2,
            corner_radius=8
        )
        self.bt_limpar_cadastro_paciente.place(x=1144, y=510)
        # Botão Agendar
        self.bt_salvar_cadastro_paciente = CTkButton(
            self.tbv_consulta,
            width=148,
            height=40,
            text='Agendar',
            text_color=self.white,
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.blue,
            hover_color=self.dark_blue,
            corner_radius=8
        )
        self.bt_salvar_cadastro_paciente.place(x=1312, y=510)
        
    def fechar_consulta(self):
        self.destroy()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
