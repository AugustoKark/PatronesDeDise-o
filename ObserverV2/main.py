# DemoPatronObserver.py
from Observadores.ObservadorBinario import ObservadorBinario
from Observadores.ObservadorOctal import ObservadorOctal
from Observadores.ObservadorHexadecimal import ObservadorHexadecimal
from Sujeto import Sujeto

if __name__ == "__main__":
    sujeto = Sujeto()

    ObservadorHexadecimal(sujeto)
    ObservadorOctal(sujeto)
    ObservadorBinario(sujeto)

    print("Primer cambio de estado: 15")
    sujeto.establecer_estado(15)
    print(*"\n"*2)
    print("Segundo cambio de estado: 10")
    sujeto.establecer_estado(10)
