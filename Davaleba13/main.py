import json
import os

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

with open('players.json', 'w', encoding='utf-8') as f:
    json.dump(chess_players, f, indent=2)


1.
def sruli_gza(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return os.path.abspath(f.name)
    except FileNotFoundError:
        return f"ფაილი სახელით '{filename}' ვერ მოიძებნა."


print(sruli_gza('players.json'))


2.
def read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


print(read('players.json'))

3.
def damateba(filename, new_players_list):
    current_content = read(filename)

    current_content.extend(new_players_list)
    

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(current_content, f, indent=2)
    print("ახალი მოთამაშეები დაემატა")


new_data = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]


damateba('players.json', new_data)

4.
def ganaxleba(filename, player_id, update_data):
  
    content = read(filename)
    updated = False
    
    for player in content:
        if player['id'] == player_id:
            player.update(update_data)
            updated = True
            break
            
    if updated:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2)
        print(f"მოთამაშე ID-ით {player_id}  განახლდა.")
    else:
        print(f"მოთამაშე ID-ით {player_id} ვერ მოიძებნა.")

 
ganaxleba('players.json', 84, {'rating': 2885})