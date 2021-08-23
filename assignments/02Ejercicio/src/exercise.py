def areaRecto(largo , ancho):
    area=  largo * ancho
    return area
def perRecto(largo , ancho):
    per=  2*largo + 2*ancho
    return per


def main():
    #escribe tu código abajo de esta línea
    a = float(input("Ingresa el ancho: "))
    x = float(input("Ingresa el largo: "))
    print("Quiere calcular el área o el perímetro del rectángulo:")
    print("(a para área y p para perímetro)")
    op = input("op: ")
    if op=="a":
        print("area:",areaRecto(a,x))
    if op=="p":
        print("perimetro:",perRecto(a,x))
      

    
if __name__=='__main__':
    main()
