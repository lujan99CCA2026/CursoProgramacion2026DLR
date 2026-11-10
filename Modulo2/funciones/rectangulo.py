# 02
# Rectángulo
# rectangulo(ancho, alto) dibuja un rectángulo de asteriscos.

def rectangulo(ancho, alto):
    
    for fila in range(1,alto+1):
        if fila == 1 or fila == alto:
            print("*" * ancho )
        else:
            print("*" + " " *(ancho-2)+ "*" )



rectangulo(5,4)

rectangulo(15,41)
# ancho + 5 y alto + 4

# *****1
# *   *
# *   *
# *****alto