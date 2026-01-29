# --- DISEÑO DEL AGENTE DE CRUCE ---

def decidir_cruzar(semaforo, hay_autos):
    # REGLA: Si el semáforo está en verde Y no hay autos, cruza.
    if semaforo == "verde" and hay_autos == "no":
        return "CRUZAR" # El agente avanza con seguridad
    
    # REGLA: Si el semáforo está en rojo O hay autos, no cruza.
    elif semaforo == "rojo" or hay_autos == "si":
        return "NO CRUZAR" # El agente se detiene por seguridad
    
    else:
        return "ESPERAR" # Caso de precaución por defecto

# --- PRUEBA INTERACTIVA ---

# Solicitar datos al usuario para simular el entorno
color = input("Estado del semáforo (verde/rojo): ").lower()
trafico = input("¿Vienen autos? (si/no): ").lower()

# Mostrar la decisión final
print(f"Decisión del agente: {decidir_cruzar(color, trafico)}")

"""
ANÁLISIS DE LA ACTIVIDAD:
¿Qué tan flexible es?
Sigue siendo un agente reactivo simple basado en reglas fijas.
¿Cómo hacerlo sofisticado?
Podría incluir sensores de velocidad para calcular si un auto 
alcanzará a frenar o visión artificial para detectar el color real.
"""