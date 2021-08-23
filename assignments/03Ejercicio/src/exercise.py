
def funcion(va1, va2, clave) :
    if clave=="s":
        return va1+va2
    elif clave=="r":
        return va1-va2
    elif clave=="d":
          return va1/va2
    elif clave=="m":
          return va1*va2

    

def main() :
    # pido el tipo de silla (B E L)
    v1 = int(input("introducir valor 1: "))
    v2 = int(input("introducir valor 2: "))
    # pido el tipo de cliente (N F)
    c = input("introducir clave  (s, r, m, d): ")
    print("resultado:",funcion(v1,v2,c))



if __name__=='__main__':
    main()
