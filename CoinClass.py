import random

class Coin:
    def __init__(self, rare, clean = True, heads = "heads", **kwargs):
        
        for key,value in kwargs.items():
            settatr(self, key, value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color
    
    def rust(self):
        self.color = self.rusty_color
    
    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent!")
    
    def flip(self):
        heads_options = ["heads", "false"]
        choice = random.choice(heads_options)
        self.heads = choice

class Dollar(Coin):
    def __init__(self):
        data = {
            "original_value":1.00
            clean_color = "gold"
            rusty_color = "greenish"
            num_edges = 1
        }
        super().__init__(**data)

class HalfDollar(Coin):
    def __init__(self):
        data = {
            "original_value":.50
            clean_color = "gold"
            rusty_color = "greenish"
            num_edges = 1
        }

class Quarter(Coin):
    def __init__(self):
        data = {
            "original_value":.25
            clean_color = "silver"
            rusty_color = "greenish"
            num_edges = 1
        }

class Dime(Coin):
    def __init__(self):
        data = {
            "original_value":.10
            clean_color = "silver"
            rusty_color = "greenish"
            num_edges = 1
        }

class Nickel(Coin):
    def __init__(self):
        data = {
            "original_value":.05
            clean_color = "silver"
            rusty_color = "greenish"
            num_edges = 1
        }

class Penny(Coin):
    def __init__(self):
        data = {
            "original_value":.01
            clean_color = "copper"
            rusty_color = "greenish"
            num_edges = 1
        }

    



