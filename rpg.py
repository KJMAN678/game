from cProfile import label
from dataclasses import dataclass
from enum import Enum
import tkinter

key = ""

def main():
    global root
    root = tkinter.Tk()
    root.title("タイトルネーム")
    root.geometry("800x600")
    root.bind("<KeyPress>", key_down)
    
    global label
    label = tkinter.Label(font=("Times New Roman", 80))
    label.pack()
    main_proc()
    root.mainloop()

# キー操作の受付
def key_down(e):
    global key
    key = e.keysym
    
# リアルタイム処理を行う
def main_proc():
    label["text"] = key
    root.after(100, main_proc)

def battle():
    draw_battle_screen

def draw_battle_screen():
    pass

@dataclass
class Character:
    name: str
    max_hp: int
    hp: int
    max_mp: int
    mp: int

class Monster_type(Enum):
    monster_player = 0 # プレイヤー
    monster_max = 0    # モンスターの種類の数

if __name__ == "__main__":
    
    monster = []
    
    monster.append(Character("ゆうしゃ", 15, 15, 15, 15))
    print(monster[0].name)
    print(f"HP:{monster[0].hp}/{monster[0].max_hp} MP:{monster[0].mp}/{monster[0].max_mp}")
    
    main()
    
