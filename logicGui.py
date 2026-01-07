import tkinter as tk
from tkinter import messagebox
import random

players = {
    "player1": {"position": 0, "cash": 1500, "property": {}, "jail": False, "dice_counter": 3, "get_out_of_jail_card": False},
    "player2": {"position": 0, "cash": 1500, "property": {}, "jail": False, "dice_counter": 3, "get_out_of_jail_card": False},
    "player3": {"position": 0, "cash": 1500, "property": {}, "jail": False, "dice_counter": 3, "get_out_of_jail_card": False},
    "player4": {"position": 0, "cash": 1500, "property": {}, "jail": False, "dice_counter": 3, "get_out_of_jail_card": False}
}
player_list = list(players.keys())
current_player_index = 0

tiles = {i: {"type": "street", "owner": "bank"} for i in range(40)}

chance_cards = [
    {"text": "Go to Jail", "action": lambda p: goto_jail(p)},
    {"text": "Collect $50", "action": lambda p: pay('bank', p, 50)}
]
community_chest_cards = [
    {"text": "Get Out of Jail Free", "action": lambda p: give_jail_card(p)},
    {"text": "Collect $100", "action": lambda p: pay('bank', p, 100)}
]

def roll_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1, die2

def next_turn():
    global current_player_index
    current_player_index = (current_player_index + 1) % len(player_list)
    update_gui()

def update_gui():
    player = player_list[current_player_index]
    current_player_label.config(text=f"Current Player: {player}")
    player_info_text.delete('1.0', tk.END)
    for p in player_list:
        info = f"{p}: Cash=${players[p]['cash']}, Position={players[p]['position']}, Properties={list(players[p]['property'].keys())}\n"
        player_info_text.insert(tk.END, info)

def pay(creditor, debtor, amount):
    if players[debtor]['cash'] >= amount:
        players[debtor]['cash'] -= amount
        if creditor != 'bank':
            players[creditor]['cash'] += amount
        messagebox.showinfo("Payment", f"{debtor} paid ${amount} to {creditor}")
    else:
        messagebox.showinfo("Payment", f"{debtor} does not have enough money!")

def goto_jail(player):
    players[player]['position'] = 10
    players[player]['jail'] = True
    messagebox.showinfo("Jail", f"{player} is sent to Jail!")

def give_jail_card(player):
    players[player]['get_out_of_jail_card'] = True
    messagebox.showinfo("Card", f"{player} received a Get Out of Jail Free card")

def roll_dice_action():
    player = player_list[current_player_index]
    die1, die2 = roll_dice()
    pos = (players[player]['position'] + die1 + die2) % 40
    players[player]['position'] = pos
    tile = tiles[pos]
    if tile['type'] == 'street' and tile['owner'] == 'bank':
        if messagebox.askyesno("Buy Property", f"{player} landed on a street. Buy it for $100?"):
            players[player]['cash'] -= 100
            tile['owner'] = player
            players[player]['property'][pos] = 0
    elif tile['type'] == 'street' and tile['owner'] != player:
        pay(tile['owner'], player, 20)
    if random.random() < 0.2:
        card = random.choice(chance_cards)
        messagebox.showinfo("Chance Card", card['text'])
        card['action'](player)
    if random.random() < 0.2:
        card = random.choice(community_chest_cards)
        messagebox.showinfo("Community Chest", card['text'])
        card['action'](player)
    update_gui()
    next_turn()

def build_house_action():
    player = player_list[current_player_index]
    if players[player]['property']:
        prop = random.choice(list(players[player]['property'].keys()))
        players[player]['property'][prop] += 1
        messagebox.showinfo("Build House", f"{player} built a house on property {prop}")
    else:
        messagebox.showinfo("Build House", f"{player} has no properties.")
    update_gui()
    next_turn()

window = tk.Tk()
window.title("🎲 Monopoly GUI Advanced 🎲")
window.geometry("450x450")
window.configure(bg="#FFF0F5")

header_font = ("Comic Sans MS", 16, "bold")
label_font = ("Comic Sans MS", 12, "bold")
button_font = ("Comic Sans MS", 12, "bold")

current_player_label = tk.Label(window, text="", bg="#FFF0F5", fg="#FF69B4", font=header_font)
current_player_label.pack(pady=10)

player_info_text = tk.Text(window, width=50, height=12, font=("Comic Sans MS", 11))
player_info_text.pack(pady=10)

roll_button = tk.Button(window, text="Roll Dice", command=roll_dice_action, width=25, height=2, bg="#FFB6C1", fg="white", font=button_font)
roll_button.pack(pady=5)

build_button = tk.Button(window, text="Build House", command=build_house_action, width=25, height=2, bg="#FFB6C1", fg="white", font=button_font)
build_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=window.destroy, width=25, height=2, bg="#FFB6C1", fg="white", font=button_font)
exit_button.pack(pady=5)

update_gui()
window.mainloop()
