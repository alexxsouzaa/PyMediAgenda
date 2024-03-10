from typing import Tuple
from customtkinter import *
from tkinter import *
from tkinter import ttk
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
            height=32,
            text='Entrar',
            font=('Segoe UI', 14, 'bold'),
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
        __usuario_admin = ['admin', '']
        __senha_admin = ['admin', '']

        __usuario = self.entry_usuario.get()
        __senha = self.entry_senha.get()

        if __usuario in __usuario_admin and __senha in __senha_admin:
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
            self.entry_usuario.configure(fg_color=self.red_light, border_color=self.red,
                                         placeholder_text='Usuário invalido', placeholder_text_color=self.red)

            self.entry_senha.configure(fg_color=self.red_light, border_color=self.red,
                                       placeholder_text='Senha invalida', placeholder_text_color=self.red)

            # Limpa as entrys de login
            self.entry_usuario.delete(0, END)
            self.entry_senha.delete(0, END)


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
        self.geometry("1200x700+450+100")  # Tamanho da janela
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
            command=self.open_consultas
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
            anchor=W
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

    def open_consultas(self):
        self.janela_consulta = ConsultasWindow(self)
        self.janela_consulta.grab_set()

    def close_window(self):
        # Função chamada quando a janela é fechada
        print('Janela fechada!')
        self.quit()

    def logout(self):
        print('Logout')


class ConsultasWindow(CTkToplevel):
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
        self.geometry("1200x700+450+100")  # Tamanho da janela
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

        # Frame dos dados do paciente
        self.fr_dados_paciente = CTkFrame(
            self.tab_cadastro_paciente,
            width=1117,
            height=448,
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
            corner_radius=6
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
        # Label e ComBox do CPF do paciente
        self.lb_cpf_paciente_cadastro = CTkLabel(
            self.fr_dados_paciente,
            text='Sexo',
            text_color=self.black,
            font=('Segoe UI', 12, 'normal')
        ).place(x=913, y=46)
        self.ent_cpf_paciente_cadastro = CTkComboBox(
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
            values=(['Maculino', 'Feminino', 'Não declarado'])

        )
        self.ent_cpf_paciente_cadastro.place(x=913, y=72)

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


if __name__ == '__main__':

    app = MainWindow()
    app.mainloop()
