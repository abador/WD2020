def zakupy(** lista):
    ile = 0
    for rzecz in lista:
        ile +=1
    return ile

print("Liczba rzeczy do kupienia: ", zakupy(mąka=2, dżem=3, bułki=20, mleko=2))