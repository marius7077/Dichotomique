def ask_check_input():
    while True:
        try:
            e = int(input("La valeur recherchée :"))
            if e in value_list:
                return e
            else:
                print(f'{e} n\'est pas dans la liste')
        except:
            print(f'{e} n\'est pas un nombre')


if __name__ == '__main__':
    value_list = [1, 3, 5, 6, 8, 12, 13, 14, 18, 22, 25, 35, 44, 55]
    _input = ask_check_input()
    tour = 0
    while True:
        milieu = value_list[int(len(value_list) / 2)]
        if _input == milieu:
            print(f"Vous l'avez trouver à l'index {value_list.index(_input)} au bout de {tour} boucles")
            break
        elif _input < milieu:
            value_list = value_list[:value_list.index(milieu)]
            print(value_list)
            tour += 1
        else:
            value_list = value_list[value_list.index(milieu):]
            print(value_list)
            tour += 1
