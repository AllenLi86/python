import random

class prince:
    hp = 500
    def __init__(self, name):
        self.name = name
        
    def attack(self, atk_cmd):
        if atk_cmd == 1:
            print(f"{self.name}使出普通攻擊!")
            return 200
        elif atk_cmd == 2:
            print(f"{self.name}使出特殊攻擊!")
            return random.choice([100, 300])
        
    def defense(self, de_cmd):
        if de_cmd == 1:
            print(f"{self.name}一般格擋!")
            return 0.5
        elif de_cmd == 2:
            print(f"{self.name}嘗試閃避!")
            return random.choice([0.2, 1])
        
        
player_name = input("請輸入玩家名稱: ")
player = prince(player_name)
computer = prince("evil")

while True:
    # 玩家選擇攻擊方式
    atk_cmd = int(input("請選擇攻擊方式(1)普通攻擊 (2)魔法攻擊 : "))
    # 攻擊力
    atk = player.attack(atk_cmd)
    
    # 電腦選擇防禦方式
    com_choice = random.choice([1, 2])
    
    # 損失血量 
    hp_decrease = atk*computer.defense(com_choice)
    computer.hp -= hp_decrease
    if computer.hp <= 0:
        print("You won!")
        break
    else:
        print(f"{computer.name}受到{hp_decrease}點傷害，剩下{computer.hp}點")
        print("")
        
        
    # 電腦選擇攻擊方式
    com_choice = random.choice([1, 2])
    # 攻擊力
    atk = computer.attack(com_choice)
    
    # 玩家選擇防禦方式
    de_cmd = int(input("請選擇防禦方式(1)格擋 (2)閃避 : "))
    
    # 損失血量 
    hp_decrease = atk*player.defense(de_cmd)
    player.hp -= hp_decrease
    if player.hp <= 0:
        print("You lose!")
        break
    else:
        print(f"{player.name}受到{hp_decrease}點傷害，剩下{player.hp}點")
        print("")
    
    