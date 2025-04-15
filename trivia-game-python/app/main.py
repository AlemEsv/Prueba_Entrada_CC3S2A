from trivia import run_quiz

if __name__ == "__main__":
    print("""
████████╗██████╗ ██╗██╗   ██╗██╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗
╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
   ██║   ██████╔╝██║██║   ██║██║███████║    ██║  ███╗███████║██╔████╔██║█████╗  
   ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
   ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                            
                             ─────────────────────
                             ¡Bienvenido al juego!
                             ─────────────────────
                             1. Empezar Juego
                             2. Leaderboard
                             3. Salir
""")
    while True:
        opcion = input("Elije una opción: ")
        if opcion == '1':
            run_quiz()
            exit()
        elif opcion == '2':
            print("Mirar al leaderboard.") 
        elif opcion == '3':
            print("\nGracias por jugar!")
            exit()
        else:
            print("Opción invalida.")