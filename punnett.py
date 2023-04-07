def autossomica_um_par():
    #perguntar quais são os parceiros
    print("informe o genótipo dos parceiros:")
    parceiro1=str(input())
    while bool(parceiro1 == "heterozigoto") is False and bool(parceiro1 == "homoozigoto dominante") is False and bool(parceiro1 == "homozigoto recessivo") is False:
        print("Seu input não foi aceito, por favor, tente novamente, as opções são: heterozigoto, monozigoto dominante, monozigoto recessivo")
        parceiro1=str(input())
    parceiro2=str(input())
    while bool(parceiro2 == "heterozigoto") is False and bool(parceiro2 == "homozigoto dominante") is False and bool(parceiro2 == "homozigoto recessivo") is False:
        parceiro2=str(input())
    b1=bool(parceiro1=="heterozigoto" and parceiro2=="heterozigoto")
    b2=bool((parceiro1=="heterozigoto" and parceiro2=="homozigoto dominante") or (parceiro1=="homozigoto dominante" and parceiro2=="heterozigoto"))
    b3=bool((parceiro1=="heterozigoto" and parceiro2=="homozigoto recessivo") or (parceiro1=="homozigoto recessivo" and parceiro2=="heterozigoto"))
    b4=bool((parceiro1=="homozigoto dominante" and parceiro2=="homozigoto recessivo") or (parceiro1=="homozigoto recessivo" and parceiro2=="homozigoto dominante"))
    b5=bool((parceiro1=="homozigoto dominante" and parceiro2==parceiro1))
    b6=bool((parceiro1=="homozigoto recessivo" and parceiro2==parceiro1))
    if b1==True:
        return("25 por cento de chance de ser homozigoto dominante(AA), 50 por cento de chance de ser heterozigoto(Aa), 25 por cento de chance de ser homozigoto recessivo(aa)\nProporção de 1:2:1")
    elif b2==True:
        return("50 por cento de chance de ser homozigoto dominante(AA), 50 por cento de chance de ser heterozigoto(Aa)\nProporção de 1:1")
    elif b3==True:
        return("50 por cento de cahnce de ser heterozigoto(Aa), 50 por cento de chance de ser heterozigoto recessivo(aa)\nProporção de 1:1")
    elif b4==True:
        return("100 por cento de chance de ser heterozigoto(Aa)\nProporção de 1")
    elif b5==True:
        return("100 por cento de chance de ser homozigoto dominante(AA)\nProporção de 1")
    elif b6==True:
        return("100 por cento de chance de ser homozigoto recessivo(aa)\nProporção de 1")
print(autossomica_um_par())