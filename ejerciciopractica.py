import math

def calcular_eoq(D, S, H):
    """Calcula la cantidad óptima de pedido (EOQ)."""
    return math.sqrt((2 * D * S) / H)

def main():
    try:
        # Solicitar datos al usuario
        D = float(input("Ingrese la demanda anual (unidades): "))
        S = float(input("Ingrese el costo de realizar un pedido: "))
        H = float(input("Ingrese el costo de almacenamiento por unidad al año: "))

        # Validar que los valores sean positivos
        if D <= 0 or S <= 0 or H <= 0:
            print("Todos los valores deben ser mayores a 0.")
            return

        # Calcular EOQ
        Q = calcular_eoq(D, S, H)
        N = D / Q  # Número de pedidos por año
        TC = (D / Q * S) + (Q / 2 * H)  # Costo total del inventario

        # Mostrar resultados
        print(f"\nResultados:")
        print(f"La cantidad óptima de pedido (EOQ) es: {Q:.2f} unidades")
        print(f"Número de pedidos por año: {N:.2f}")
        print(f"Costo total del inventario: ${TC:.2f}")

    except ValueError:
        print("Por favor, ingrese solo valores numéricos.")

if __name__ == "__main__":
    main()
