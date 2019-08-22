import telebot
from keys_pocket import ApiKeys
from cmc_info import getCoins
from bittrex_info import getBittrex


bot = telebot.TeleBot(ApiKeys.TG_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help', 'get_market_cap'])
def show_cryptocurrency(message):
    if message.text == '/get_market_cap' or message.text == '/get_market_cap@CmcBtrxBot':
        b = 'Balance: '
        c = 'Cost: '
        p = 'Volume: '
        t = 'Total revenues: '
        total = 0
        btx = getBittrex()
        btx = btx.get_bittrex_coins()
        coins = [k for k in btx.keys()]
        cmc = getCoins(coins)
        cmc_market = cmc.get_coins()
        
        for k, v in btx.items():
            for key, val in cmc_market.items():
                if k == key:
                    bot.send_message(message.chat.id, f"{str(k)} \n{b} {str(v)} \n{c} {str(val)} \n{p} {str(round(v * val, 2))}")
                    total += v * val
        bot.send_message(message.chat.id, f"{t} {str(round(total, 2))}")
    
    else:
        bot.send_message(message.chat.id, coins, 'Oh, something went wrong. Let\'s go again.')


bot.polling()