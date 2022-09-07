from automation import Automation


try:
    if __name__ == "__main__":
        navegacao = Automation()
        navegacao.iniciar_consultas()
except KeyboardInterrupt:
    pass
finally:
    print("\nProcesso finalizado.")
