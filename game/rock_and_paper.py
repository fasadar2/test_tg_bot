#rock_and_paper
import random
win_comb = ["камень_ножницы","бумага_камень","ножницы_бумага"]
def game(message):
    user_chose = message.text.lower().strip()
    user_name = message.from_user.first_name
    bot_chose = random.choice(['камень','ножницы','бумага'])
    comb = f"{user_chose}_{bot_chose}"
    if comb in win_comb:
        return (f"{user_name} победил выбрав: {user_chose}\nкомбинация {user_chose}:{bot_chose}",True)
    elif user_chose == bot_chose:
        return (f"Ничья оба выбрали {user_chose}",False)
    else:
        return (f"{user_name} проиграл выбрав: {user_chose}\nкомбинация {user_chose}:{bot_chose}",False)
