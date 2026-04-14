import os
os.system("cls")

peso = float(input("digite seu peso em KG:"))
altura = float(input("gite sua altura wm metros:"))

def cal_imc (peso,altura):
 imc= peso/ (altura * altura)
 return imc


def  classifica_imc(imc):
     if imc < 18.5:
      return "Abaixo do peso ideal","consute um nutricionista para orientaçao"
     elif imc <= 24.9:
      return "peso normal","mantenha habitos normais "
     elif imc <= 29.9:
      return "levimente acima do peso","considere uma dieta consideravel"
     elif imc <= 34.9:
      return"obesidade grau 1","proucura orientaçao de um profissinal"
     elif imc <=39.9:
      return "obesidade grau 2","consulte um medico para avaliaçao e orientalo"
 
     elif imc <=40.00:
      return "obesidade grau 3"," busque assistencia medica imediatamente"
 
resultado=cal_imc(peso,altura)
classificaçao,recomedação = classifica_imc(resultado)


print(f"o seu imc foi {resultado:.2f}")
print(f"a sua classificação foi {classificaçao}")
print(f"a sua recomendação  foi {recomedação}")
    
