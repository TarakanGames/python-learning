import ollama
player_gold = 20
shop_inventory = {
    "Health Potion" : {
        "price" : 5,
        "stock" : 3,
    },
    "Mana Potion" :{
        "price" : 7,
        "stock" : 2}}
def buy_health_potion():
    global player_gold 
    if player_gold < shop_inventory["Health Potion"]["price"]:
        return ("You dont have enough gold, sorry!")
    shop_inventory["Health Potion"]["stock"] -= 1
    player_gold -= shop_inventory["Health Potion"]["price"]

    return f"Health Potion has been bought! Your gold: {player_gold}"

def buy_mana_potion():
    global player_gold 
    if player_gold < shop_inventory["Mana Potion"]["price"]:
        return ("You dont have enough gold, sorry!")
    shop_inventory["Mana Potion"]["stock"] -= 1
    player_gold -= shop_inventory["Mana Potion"]["price"]

    return f"Mana Potion has been bought! Your gold: {player_gold}"

def exit():
    return "Thank you for visiting my Shop! Safe travells traveller!" 

tools = [ 
      {
          "type" : "function",
          "function" : {
              "name" : "buy_health_potion",
              "description" : "Buys the Player a Health Potion"
              },
      },
      {
          "type" : "function",
          "function" : {
              "name" : "buy_mana_potion",
              "description" : "Buys the Player a Mana Potion"
              },
      },
      {
          "type" : "function",
          "function" : {
              "name" : "exit",
              "description" : "Ends the Session with the shop keeper and player"
              },
      },
]

print("Welcome to my potion shop, traveler! Take a look at what I've got in stock today:")
print("Health Potion — Restores your health points, costs 5 Gold.")
print("Mana Potion — Restores your magic power, costs 7 Gold.")
message = input("What can i do for you today? ")
messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly medieval potion shopkeeper in an RPG. "
                "Stay in character, be helpful to travelers, and keep your answers relatively brief. "
                "Always try to sell Health Potions (5 Gold) or Mana Potions (7 Gold)."
                "You start with 3 Health Potions in stock and 2 Mana Potions in stock."
                "The player starts with 20 Gold."
            )
        },
        {
            "role": "user",
            "content": message
        }
 ]
loop_count = 1
while True: 
    if loop_count > 1:
        message = input("Your Answer: ")
    messages.append({"role": "user", "content": message})
    response = ollama.chat(
        model="qwen3-vl:8b",
        messages=messages,
        tools=tools
    )
    if response.message.tool_calls:
        tool_name = response.message.tool_calls[0].function.name
        if tool_name == "buy_health_potion":
            result = buy_health_potion()
            print(result)
            messages.append(response.message)
        elif tool_name == "buy_mana_potion":
            result = buy_mana_potion()
            print(result)
            messages.append(response.message)
        elif tool_name == "exit":
            print(exit())
            break
    else:
        print(response.message.content)
        messages.append({"role": "assistant", "content": response.message.content})
    loop_count += 1