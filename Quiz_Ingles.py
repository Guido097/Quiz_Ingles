import json
import random

def cargar_palabras(archivo="palabras.json"):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def jugar_quiz(palabras):
    puntaje = 0
    total_preguntas = min(5, len(palabras))  # Asegurar que no se pidan más preguntas de las disponibles
    preguntas_incorrectas = []
    preguntas_realizadas = set()

    for _ in range(total_preguntas):
        palabra = random.choice(palabras)
        while palabra['ingles'] in preguntas_realizadas:
            palabra = random.choice(palabras)
        preguntas_realizadas.add(palabra['ingles'])

        print(f"Traduce al español: {palabra['ingles']}")
        respuesta = input("Tu respuesta: ").strip().lower()

        if respuesta == palabra['espanol'].lower():
            print("✅ Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {palabra['espanol']}")
            preguntas_incorrectas.append(palabra)
        print(f"Ejemplo: {palabra['ejemplo']}")
        print("-" * 30)

    print(f"Puntaje final: {puntaje}/{total_preguntas}")

    if preguntas_incorrectas:
        print("\nVamos a repetir las preguntas incorrectas:")
        for palabra in preguntas_incorrectas:
            print(f"Traduce al español: {palabra['ingles']}")
            respuesta = input("Tu respuesta: ").strip().lower()
            if respuesta == palabra['espanol'].lower():
                print("✅ Correcto!")
            else:
                print(f"❌ Incorrecto. La respuesta era: {palabra['espanol']}")
            print(f"Ejemplo: {palabra['ejemplo']}")
            print("-" * 30)

if __name__ == "__main__":
    palabras = cargar_palabras()
    jugar_quiz(palabras)