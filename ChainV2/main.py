from ErrorLogger import ErrorLogger
from FileLogger import FileLogger
from ConsoleLogger import ConsoleLogger
from AbstractLogger import AbstractLogger

def obtener_cadena_de_registradores():
    registrador_error = ErrorLogger(AbstractLogger.ERROR)
    registrador_archivo = FileLogger(AbstractLogger.DEBUG)
    registrador_consola = ConsoleLogger(AbstractLogger.INFO)

    registrador_error.set_siguiente_logger(registrador_archivo)
    registrador_archivo.set_siguiente_logger(registrador_consola)

    return registrador_error

if __name__ == "__main__":
    cadena_registradores = obtener_cadena_de_registradores()

    cadena_registradores.registrar_mensaje(AbstractLogger.INFO, "Esto es una información.")
    cadena_registradores.registrar_mensaje(AbstractLogger.DEBUG, "Esto es una información de nivel debug.")
    cadena_registradores.registrar_mensaje(AbstractLogger.ERROR, "Esto es una información de error.")
