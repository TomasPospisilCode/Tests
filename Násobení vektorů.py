#skalární součin
def dot_product(vector1, vector2):
    #temporary proměnná do které ukládám výsledek
    tmp = 0
    #proměnná, do které ukládám iteraci cyklu
    i=0
    #podmínka která testuje, zda mají vektory stejnou délku
    majiStejnouDelku = len(vector1) == len(vector2)
    #podmínka která testuje, zda se jedná o 2D a 3D vektory
    majiSpravnouDelku = (len(vector1) == 2) or (len(vector1) == 3)

    #obě podmínky musí být splněny
    if majiStejnouDelku and majiSpravnouDelku:
        for x in vector1:
            tmp+=x*vector2[i]
            i+=1    
        return tmp
    else:
        return None
    
#vektorový součin
def cross_product(vector1, vector2):
    #trochu upravená podmínka protože vektorový součin může být jen 3D
    majiSpravnouDelku = len(vector1) == 3
    majiStejnouDelku = len(vector1) == len(vector2)
    
    if majiStejnouDelku and majiSpravnouDelku:
        #podle vzorce UxV=(U2*V3-V2*U3)
        expr1 = (vector1[1]*vector2[2])-(vector2[1]*vector1[2])
        #podle vzorce UxV=(U3*V1-V3*U1)
        expr2 = (vector1[2]*vector2[0])-(vector2[2]*vector1[0])
        #podle vzorce UxV=(U1*V2-V1*U2)
        expr3 = (vector1[0]*vector2[1])-(vector2[0]*vector1[1])
        result = [expr1, expr2, expr3]
 
        return result
