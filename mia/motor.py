
def motor(caso, reglas, ver=False):
    datos = dict(caso) 
    usadas = []        
    vueltas = []       
    explicacion = []     
    vuelta = 0

    while 'decision' not in datos:    
        vuelta = vuelta + 1

        cumplen = []
        nombres_cumplen = []
        for regla in reglas:
            nombre, se_cumple, apunta, prioridad, porque = regla
            if nombre in usadas:
                continue
            try:
                se_cumple_ahora = se_cumple(datos)
            except KeyError:  
                se_cumple_ahora = False
            if se_cumple_ahora:
                cumplen.append(regla)
                nombres_cumplen.append(nombre)

        if len(cumplen) == 0:
            break

        elegida = cumplen[0]
        for regla in cumplen:
            if regla[3] > elegida[3]:
                elegida = regla

        nombre, se_cumple, apunta, prioridad, porque = elegida
        datos.update(apunta)
        usadas.append(nombre)
        explicacion.append(nombre + ': ' + porque)

        vueltas.append({'vuelta': vuelta,
                        'se cumplen': ', '.join(nombres_cumplen),
                        'se aplica': nombre,
                        'apunta': str(apunta)})
        if ver:
            print('Vuelta', vuelta, ': se cumplen', nombres_cumplen, '-> se aplica', nombre, '-> apunta', apunta)

    decision = datos.get('decision', 'SIN DECISIÓN (ninguna regla encaja: falta una regla)')
    if ver:
        print()
        print(datos.get('nombre', 'Caso'), ':', decision, '  (reglas usadas:', ' -> '.join(usadas), ')')

    return {'decision': decision, 'usadas': usadas, 'porque': explicacion, 'vueltas': vueltas}
