# Calcula el interés simple
def interes_simple(capital, tasa, tiempo):
    return capital * tasa * tiempo

# Calcula el monto final con interés compuest.
def interes_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa) ** tiempo

# Calcula la cuota mensual de un préstamo (sistema francés).
def cuota_prestamo(monto, tasa_mensual, meses):
    if tasa_mensual == 0:
        return monto / meses
    return monto * (tasa_mensual * (1 + tasa_mensual) ** meses) / ((1 + tasa_mensual) ** meses - 1)

# Calcula el valor futuro de aportes periódicos.
def valor_futuro_aportes(aporte, tasa_mensual, meses):
    return aporte * (((1 + tasa_mensual) ** meses - 1) / tasa_mensual)
