from typing import Tuple
from customtkinter import *
from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image


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
            self.update()
            self.entry_usuario = CTkEntry(
                self,
                width=260,
                height=32,
                font=('Segoe UI', 14, 'normal'),
                text_color=self.black,
                border_color=self.red,
                border_width=1.5,
                corner_radius=8,
                fg_color=self.red_light,
                bg_color=self.blue_light_2,
                placeholder_text='Usuário invalido',
                placeholder_text_color=self.red,
            )
            self.entry_usuario.place(x=610, y=258)

            self.entry_senha = CTkEntry(
                self,
                width=260,
                height=32,
                font=('Segoe UI', 14, 'normal'),
                text_color=self.black,
                border_color=self.red,
                border_width=1.5,
                corner_radius=8,
                fg_color=self.red_light,
                bg_color=self.blue_light_2,
                placeholder_text='Senha invalida',
                placeholder_text_color=self.red,
            )
            self.entry_senha.place(x=610, y=320)
            self.update()
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
        self.gray_dark = "#545454"
        self.black = "#000000"
        self.red = "#F2497C"
        self.red_light = "#FFE8F1"

        # =========== Configuração da Janela ===========
        self.title("Home")  # Titulo da janela
        self.configure(fg_color=self.white)  # Cor da janela
        self.geometry("1200x700+450+100")  # Tamanho da janela
        self.resizable(False, False)

        # =========== TopBar ===========
        # Frame
        self.fr_topbar = CTkFrame(
            self,
            width=1300,
            height=48,
            fg_color=self.blue,
            border_width=0,
            corner_radius=0
        )
        self.fr_topbar.place(x=0, y=0)

        # Imagem do logo
        self.logo_topbar_img = CTkImage(
            light_image=Image.open('assets\imgs\logo_white.png'),
            dark_image=Image.open('assets\imgs\logo_white.png'),
            size=(168, 24)
        )
        # Label da Imagem de Logo
        self.lb_logo_topbar_img = CTkLabel(
            master=self.fr_topbar,
            image=self.logo_topbar_img,
            text='',
            fg_color=self.blue,
            bg_color=self.blue,
            anchor=CENTER
        ).place(x=516, y=12)

        # Ícone de usuario
        self.usuario_topbar_img = CTkImage(
            light_image=Image.open('assets/icons/icon_pack/user.png'),
            dark_image=Image.open('assets/icons/icon_pack/user.png'),
            size=(22, 22)
        )
        # Label do ícone de usuario
        self.lb_usuario_topbar_img = CTkLabel(
            master=self.fr_topbar,
            image=self.usuario_topbar_img,
            text='',
            fg_color=self.blue,
            bg_color=self.blue,
            anchor=N
        ).place(x=24, y=13)
        # Label do nome Usuário
        self.lb_usuario_topbar_nome = CTkLabel(
            self.fr_topbar,
            text='Olá, Bruno Álex',
            font=('Segoe UI', 12, 'bold'),
            text_color=self.white,
            anchor=N
        ).place(x=54, y=16)
        
        # Ícone de Notificação
        self.notificacao_topbar_img = CTkImage(
            light_image=Image.open('assets/icons/icon_pack/notification.png'),
            dark_image=Image.open('assets/icons/icon_pack/notification.png'),
            size=(18, 18)
        )
        # Label do ícone de Notificação
        self.lb_notificacao_topbar_img = CTkLabel(
            master=self.fr_topbar,
            image=self.notificacao_topbar_img,
            text='',
            fg_color=self.blue,
            bg_color=self.blue,
            anchor=N
        ).place(x=1108, y=15)

        # Ícone de Configurações
        self.configuracoa_topbar_img = CTkImage(
            light_image=Image.open('assets/icons/icon_pack/setting.png'),
            dark_image=Image.open('assets/icons/icon_pack/setting.png'),
            size=(18, 18)
        )
        # Label do ícone de Configurações
        self.lb_configuracoa_topbar_img = CTkLabel(
            master=self.fr_topbar,
            image=self.configuracoa_topbar_img,
            text='',
            fg_color=self.blue,
            bg_color=self.blue,
            anchor=N
        ).place(x=1158, y=15)

        # =========== Menu Lateral ===========
        # Frame
        self.fr_menu_lateral = CTkFrame(
            self,
            width=216,
            height=760,
            fg_color=self.blue_light_2,
            border_width=0,
            corner_radius=0
        ).place(x=0, y=49)
        
        # =========== Top Frame ===========
        # Frame
        self.fr_top_frame = CTkFrame(
            self,
            width=968,
            height=100,
            fg_color=self.blue_light_2,
            border_color=self.blue_light_1,
            border_width=2,
            corner_radius=8
        ).place(x=224, y=56)
        
        # =========== Main Frame ===========
        # Frame
        self.fr_main_frame = CTkFrame(
            self,
            width=968,
            height=528,
            fg_color=self.blue_light_2,
            border_color=self.blue_light_1,
            border_width=2,
            corner_radius=8
        ).place(x=224, y=164)
        


        # =========== Chama a função que fecha a janela ===========
        self.protocol("WM_DELETE_WINDOW", self.close_window)


    def close_window(self):
        # Função chamada quando a janela é fechada
        print('Janela fechada!')
        self.quit()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
