from typing import Any

class AnalizadorEventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_eventos(self) -> dict[str, Any]:
        total_eventos_registrados = 0
        eventos_por_tipo = {}
        eventos_por_servidor = {}

        with open(self.nombre_archivo, "r", encoding= "ISO-8859-1") as file:
            for linea in file:

                if "Tipo de evento" in linea:
                    total_eventos_registrados += 1
                    tipo_evento = linea.strip().split(": ")[1]
                    eventos_por_tipo[tipo_evento] = eventos_por_tipo.get(tipo_evento, 0) + 1


                elif "Servidor" in linea:
                    total_eventos_registrados += 0
                    nombre_servidor = linea.strip().split(": ")[1]
                    eventos_por_servidor[nombre_servidor] = eventos_por_servidor.get(nombre_servidor, 0) + 1

        estadisticas = {"Total Eventos": total_eventos_registrados,"Eventos por tipo": eventos_por_tipo,"Eventos por servidor": eventos_por_servidor}
        return estadisticas

Analizar_1 = AnalizadorEventos("eventos.txt")
resultado = Analizar_1.procesar_eventos()
print(resultado)







