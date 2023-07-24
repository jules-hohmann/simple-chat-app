class store:
    def __init__(self, avatars, emojis, wallet):
        self.avatars = {
            "avatardragon": 100,
            "avatarogre": 150,
            "avatargod": 200
        }
        self.emojis = {
            "emojihappy": 50,
            "emojisad": 75,
            "emojirizzler": 100
        }
        self.wallet = wallet

    def buy_avatar(self, user, avatar_name):
        if avatar_name in self.avatars:
            price = self.avatars[avatar_name]
            if user in self.wallet and self.wallet[user] >= price:
                self.wallet[user] -= price
                return f"Congratulations! You bought {avatar_name} for {price} pentacephalus points."
            else:
                return "Insufficient pentacephalus points to buy this avatar."
        else:
            return "Avatar not found in the store."

    def buy_emoji(self, user, emoji_name):
        if emoji_name in self.emojis:
            price = self.emojis[emoji_name]
            if user in self.wallet and self.wallet[user] >= price:
                self.wallet[user] -= price
                return f"Congratulations! You bought {emoji_name} for {price} pentacephalus points."
            else:
                return "Insufficient pentacephalus points to buy this emoji."
        else:
            return "Emoji not found in the store."

    def check_balance(self, user):
        if user in self.wallet:
            return f"Your current balance: {self.wallet[user]} pentacephalus points."
        else:
            return "User not found in the store."

    def add_points(self, user, points):
        if user in self.wallet:
            self.wallet[user] += points
        else:
            self.wallet[user] = points

if __name__ == "__main__":
    store = store()

    store.add_points("user1", 500)
    store.add_points("user2", 300)

    print(store.check_balance("user1"))
    print(store.check_balance("user2"))

    print(store.buy_avatar("user1", "avatargod"))  
    print(store.buy_avatar("user1", "avatardragon"))  
    print(store.buy_avatar("user1", "avatarnothing")) 
    print(store.buy_emoji("user2", "emojihappy"))   

    print(store.check_balance("user1")) 
    print(store.check_balance("user2")) 