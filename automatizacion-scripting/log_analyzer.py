import re
from datetime import datetime

LOG_FILE = "server.log"

PATRONES = [
    (r"(\bor\b|\bOR\b)\s+1=1", "SQL Injection OR 1=1"),
    (r"--", "Comentario SQL"),
    (r"UNION\s+SELECT", "UNION SELECT"),
    (r"DROP\s+TABLE", "DROP TABLE"),
    (r"EXEC\s*\(", "EXEC comando"),
]

def analizar_logs():
    try:
        with open(LOG_FILE, "r") as archivo:
            lineas = archivo.readlines()

        total = len(lineas)
        alertas = []

        for linea in lineas:
            for patron, tipo in PATRONES:
                if re.search(patron, linea, re.IGNORECASE):
                    alertas.append((tipo, linea.strip()))

        print("\n===== REPORTE DE SEGURIDAD =====")
        print("Fecha:", datetime.now())
        print("Total de líneas:", total)
        print("Incidentes detectados:", len(alertas))

        print("\n--- DETALLES ---")
        for tipo, contenido in alertas:
            print(f"[!] {tipo} -> {contenido}")

        print("\n===== FIN DEL REPORTE =====")

    except FileNotFoundError:
        print("ERROR: No existe server.log")

if __name__ == "__main__":
    analizar_logs()
