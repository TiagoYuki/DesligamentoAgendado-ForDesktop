#Programa caseiro criado para que o usuário possa agendar o desligamento do computador.
#O programa é simples e fácil de usar, basta inserir o número de minutos que deseja para agendar o desligamento do computador.
#O programa também possui a opção de cancelar o desligamento agendado, caso o usuário mude de ideia.
#Desenvolvido por Tiago Y. Masuda
versao=0.2
status="Demo"

import os
import time
import curses
import sys



def masudaLogoFix():
    print("                   ░▒▓██████████████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ")
    print("                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ ")
    print("                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ")




#-----------------------------------------------------------

def limparConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#-----------------------------------------------------------

def desligar_em(minutos):
    limparConsole()
    masudaLogoFix()
    print("\n\n")
    segundos = minutos * 60
    mensagem = [
        f"                                      O COMPUTADOR SERÁ DESLIGADO EM {minutos} MINUTO(S)",
    ]
    for line in mensagem:
        for i in range(len(line) + 1):
            print(line[:i], end='\r', flush=True)
            time.sleep(0.01)
        print()  # Adiciona uma nova linha após a animação
    time.sleep(2)

    sistema = os.name

    if sistema == 'nt':
        os.system(f"shutdown /s /t {segundos}")
    elif sistema == 'posix':
        os.system(f"shutdown -h +{minutos}")
    else:
        limparConsole()
        masudaLogoFix()
        print("                                                        ┌─────────┐")
        print("                                                        │ ATENÇÃO │")
        print("                                                        └─────────┘")
        print("                                        ┌───────────────────────────────────────┐")
        print("                                        │   SISTEMA OPERACIONAL NÃO SUPORTADO   │")
        print("                                        └───────────────────────────────────────┘\n")
        print("                                        ┌───────────────────────────────────────┐")
        print("                                        │    TAL FUNÇÃO NÃO É SUPORTADA NESTE   │")
        print("                                        │          SISTEMA OPERACIONAL          │")
        print("                                        └───────────────────────────────────────┘\n")

#-----------------------------------------------------------

def cancelar_desligamento():
    sistema = os.name
    if sistema == 'nt':
        resultado = os.system("shutdown /a >nul 2>&1")
        if resultado == 0:
            mensagem = [
                "                                       ┌────────────────────────────────────────┐",
                "                                       │   DESLIGAMENTO CANCELADO COM SUCESSO   │",
                "                                       └────────────────────────────────────────┘\n"
            ]
            for line in mensagem:
                for i in range(len(line) + 1):
                    print(line[:i], end='\r', flush=True)
                    time.sleep(0.01)
                print()  # Adiciona uma nova linha após a animação
            main()
        else:
            print("                                                        ┌─────────┐")
            print("                                                        │ ATENÇÃO │")
            print("                                                        └─────────┘")
            print("                                        ┌────────────────────────────────────────┐")
            print("                                        │   NÃO HÁ DESLIGAMENTO AGENDADO PARA    │")
            print("                                        │                CANCELAR                │")
            print("                                        └────────────────────────────────────────┘\n")
            main()
    elif sistema == 'posix':
        resultado = os.system("shutdown -c")
        if resultado == 0:
            print("                                       ┌────────────────────────────────────────┐")
            print("                                       │   DESLIGAMENTO CANCELADO COM SUCESSO   │")
            print("                                       └────────────────────────────────────────┘\n")
        else:
            print("                                                        ┌─────────┐")
            print("                                                        │ ATENÇÃO │")
            print("                                                        └─────────┘")
            print("                                        ┌────────────────────────────────────────┐")
            print("                                        │   NÃO HÁ DESLIGAMENTO AGENDADO PARA    │")
            print("                                        │                CANCELAR                │")
            print("                                        └────────────────────────────────────────┘\n")
            main()
    else:
        print("                                                        ┌─────────┐")
        print("                                                        │ ATENÇÃO │")
        print("                                                        └─────────┘")
        print("                                        ┌───────────────────────────────────────┐")
        print("                                        │   SISTEMA OPERACIONAL NÃO SUPORTADO   │")
        print("                                        └───────────────────────────────────────┘\n")
        print("                                        ┌───────────────────────────────────────┐")
        print("                                        │    TAL FUNÇÃO NÃO É SUPORTADA NESTE   │")
        print("                                        │          SISTEMA OPERACIONAL          │")
        print("                                        └───────────────────────────────────────┘\n")

#-----------------------------------------------------------

def mainIntroducao():
    limparConsole()
    masudaLogoFix()
    print(f"                                           Boas-vindas ao Desligamento Agendado \n                                                         [",status,"]")
    print(f"(Versão: {versao})")
    print("Por: Tiago Y. Masuda")
    print("                                          _   _  ________  _________  __  _______")
    print("                                         | | /| / / __/ / / ___/ __ \/  |/  / __/")
    print("                                         | |/ |/ / _// /_/ /__/ /_/ / /|_/ / _/  ")
    print("                                         |__/|__/___/____\___/\____/_/  /_/___/  \n")

#-----------------------------------------------------------

def masudaLogo(stdscr):
    stdscr.clear()
    stdscr.refresh()

    logo = [
        "                                                                                       ",
        "                   ░▒▓██████████████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ",
        "                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ",
        "                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ",
        "                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ ",
        "                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ",
        "                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ",
        "                   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ",
        "                                           Boas-vindas ao Desligamento Agendado",
    ]

    height, width = stdscr.getmaxyx()
    logo_width = len(logo[0])

    for i in range(logo_width + 1):
        for line_index, line in enumerate(logo):
            if i < len(line):
                stdscr.addstr(line_index, 0, line[:i])
        stdscr.refresh()
        time.sleep(0.03)

    for line_index, line in enumerate(logo):
        stdscr.addstr(line_index, 0, line)
    stdscr.refresh()
    time.sleep(0.5)

def run_program():
    curses.wrapper(masudaLogo)


if __name__ == "__main__":
    run_program()

#-----------------------------------------------------------

def encerrar():
    import time
    mensagem = [
        "                                                  ┌────────────────────┐",
        "                                                  │ ENCERRAR  PROGRAMA │",
        "                                                  └────────────────────┘"
    ]
    for line in mensagem:
        for i in range(len(line) + 1):
            print(line[:i], end='\r', flush=True)
            time.sleep(0.01)
        print()  # Adiciona uma nova linha após a animação
    print("                                                     ┌──────────────┐")
    print("                                                     │ TEM CERTEZA? │")
    print("                                                     └──────────────┘")
    print("                                       ┌───────────────────┐ ┌──────────────────┐")
    print("                                       │   (1) CONFIRMAR   │ │   (2) CANCELAR   │")
    print("                                       └───────────────────┘ └──────────────────┘")
    closeterminal=int(input("USUÁRIO-----→ "))
    if (closeterminal!=1) and (closeterminal!=2):
            print("\n[INSIRA UM COMANDO VÁLIDO]\n")
            closeterminal=int(input("USUÁRIO-----→ "))
    if closeterminal==1:
        limparConsole()
        for loadingEncerrando in "\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                        [ENCERRANDO]":
            print(loadingEncerrando, end='', flush=True)
            time.sleep(0.01)
        time.sleep(1)
        limparConsole()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n                                                   ┌──────────────────────┐\n                                                   │ENCERRAMENTO CONCLUÍDO│\n                                                   └──────────────────────┘")
        time.sleep(2)
        sys.exit()
    else:
        print("                                                ┌────────────────────────┐")
        print("                                                │ ENCERRAMENTO CANCELADO │")
        print("                                                └────────────────────────┘")
        limparConsole()
        masudaLogoFix()
        main()
        return

#-----------------------------------------------------------

def mainAgendamento():
    while True:
        print("                                                ┌──────────────────────┐")
        print("                                                │ AGENDAR DESLIGAMENTO │")
        print("                                                └──────────────────────┘")
        print("                                             ┌──────────────────────────────┐")
        print("                                             │ [exit] PARA RETORNAR AO MENU │")
        print("                                             └──────────────────────────────┘")
        print("                             ┌────────────────────────────────────────────────────────────┐")
        print("                             │   APÓS QUANTOS MINUTOS O DISPOSITIVO DEVE SER DESLIGADO?   │")
        print("                             └────────────────────────────────────────────────────────────┘\n")
        
        entrada = input("USUÁRIO-----→ ")
        if entrada.strip().lower() == "exit":
            limparConsole()
            masudaLogoFix()
            main()
            return
        try:
            minutos = int(entrada)
            desligar_em(minutos)
            main()
            return
        except KeyboardInterrupt:
            print("                                           ┌─────────────────────────────────┐")
            print("                                           │ OPERAÇÃO CANCELADA PELO USUÁRIO │")
            print("                                           └─────────────────────────────────┘")
        except ValueError:
            print("                                                  ┌──────────────────┐")
            print("                                                  │ ENTRADA INVÁLIDA │")
            print("                                                  └──────────────────┘\n\n")
            print("                                         ┌────────────────────────────────────┐")
            print("                                         │ OBSERVAÇÃO: SOMENTE NÚMERO INTEIRO │")
            print("                                         └────────────────────────────────────┘")



def main():
    print("       ┌──────────────────────────────┐ ┌────────────────────────────────────────┐ ┌───────────────────────────┐")
    print("       │   (1) AGENDAR ENCERRAMENTO   │ │   (2) CANCELAR ENCERRAMENTO AGENDADO   │ │   (3) ENCERRAR PROGRAMA   │")
    print("       └──────────────────────────────┘ └────────────────────────────────────────┘ └───────────────────────────┘")

    while True:
        opcao = input("USUÁRIO-----→ ")

        if opcao == "1":
            limparConsole()
            masudaLogoFix()
            mainAgendamento()
        elif opcao == "2":
            limparConsole()
            masudaLogoFix()
            cancelar_desligamento()
        elif opcao == "3":
            limparConsole()
            masudaLogoFix()
            encerrar()
        else:
            limparConsole()
            masudaLogoFix()
            print("                                                   ┌──────────────────┐")
            print("                                                   │ ENTRADA INVÁLIDA │")
            print("                                                   └──────────────────┘")
            main()
if __name__ == "__main__":
    mainIntroducao()
    main()