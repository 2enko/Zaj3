import getpass
import random


# Zad1

print("Podaj swoje liczby:")
lista = input().split(",")
size = len(lista)
print(lista)

for x in range(size):
    for j in range(size - x - 1):
        if lista[j] < lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)
lista.sort(reverse=True)
print(lista)

# Zad2

listOfCities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
listOfCities = listOfCities.split(",")
print(listOfCities)
print("Miasta do odwiedzenia w kolejności losowej:")
listToPrint = []
for x in range(len(listOfCities)):
    listToPrint.append(random.choice(listOfCities))
print(listToPrint)

## Zad3

def get_player_choice(player_name):
    valid_choices = ['1', '2', '3']
    while True:
        choice = getpass.getpass(f'{player_name}, wybierz [1] papier, [2] nożyce, [3] kamień: ')
        if choice in valid_choices:
            return int(choice)
        else:
            print('Nieprawidłowy wybór, spróbuj ponownie.')


def get_computer_choice():
    return random.randint(1, 3)


def play_round(player1_name, player2_name, is_computer):
    if is_computer:
        player2_choice = get_computer_choice()
        player2_name = 'Komputer'
    else:
        player2_choice = get_player_choice(player2_name)

    player1_choice = get_player_choice(player1_name)

    print(f'{player1_name} wybrał {player1_choice}, {player2_name} wybrał {player2_choice}.')

    if player1_choice == player2_choice:
        print('Remis!')
        return 0
    elif player1_choice == 1 and player2_choice == 3 or player1_choice == 2 and player2_choice == 1 or player1_choice == 3 and player2_choice == 2:
        print(f'{player1_name} wygrywa rundę!')
        return 1
    else:
        print(f'{player2_name} wygrywa rundę!')
        return -1


def get_num_rounds():
    while True:
        try:
            num_rounds = int(input('Ile rund chcesz zagrać? '))
            if num_rounds > 0:
                return num_rounds
            else:
                print('Liczba rund musi być dodatnia, spróbuj ponownie.')
        except ValueError:
            print('Nieprawidłowa liczba, spróbuj ponownie.')


def get_game_mode():
    while True:
        mode = input('Wybierz tryb gry - [1] komputer lub [2] dwóch graczy (hot seats): ')
        if mode == '1':
            return True
        elif mode == '2':
            return False
        else:
            print('Nieprawidłowy wybór, spróbuj ponownie.')


def get_player_names():
    player1_name = input('Gracz 1, podaj swoje imię: ')
    player2_name = input('Gracz 2, podaj swoje imię: ')
    return player1_name, player2_name


def play_game():
    num_rounds = get_num_rounds()
    is_computer = get_game_mode()
    if not is_computer:
        player1_name, player2_name = get_player_names()
    else:
        player1_name = input('Podaj swoje imię: ')
        player2_name = None

    scores = [0, 0]
    for i in range(num_rounds):
        print(f'Runda {i + 1}:')
        result = play_round(player1_name, player2_name, is_computer)
        scores[0] += result
        scores[1] -= result

    print(f'\nWyniki końcowe:')
    print(f'{player1_name}: {scores[0]}')
    print(f'{player2_name or "Komputer"}: {scores[1]}')
    if scores[0] == scores[1]:
        print('Remis!')
    elif scores[0] > scores[1]:
        print(f'{player1_name} wygrywa grę!')
    else:
        print(f'{player2_name or "Komputer"} wygrywa grę!')


play_game()
