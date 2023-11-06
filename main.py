# -*- coding: utf-8 -*-

import requests, json, telebot, time

token = 'TOKEN_BOT' # Criar usando BOT Father
chat_id = 'ID_PESSOA_OU_GRUPO' # Obter atraves do GetUpdates
bot = telebot.TeleBot(token)

control_rain_prob = 100

while True:
    url = "https://api.hgbrasil.com/weather?woeid=455838"
    r = requests.get(url)
    tasks = json.loads(r.text)
    for temp in tasks['results']['forecast']:
        if temp['date'] == '01/01': ## INFORME AQUI CASO QUEIRA FILTRAR UMA DATA ESPECIFICA
            #print(temp)
            temp_min = temp['min']
            temp_max = temp['max']
            rain_prob = temp['rain_probability']
            wind_speed = temp['wind_speedy']
            description = temp['description']


            if rain_prob != control_rain_prob:
                if rain_prob < control_rain_prob:
                    text = """<b>😁 Probabilidade de chuva abaixou!!!</b> \n\n🌡️<b>Temp Max:</b> %s\n🌡️<b>Temp Min:</b> %s\n🌧️ <b>Prob. Chuva:</b> %s\n✍️ <b>Desc:</b> %s""" %(str(temp_max),str(temp_min),str(rain_prob),str(description))
                    bot.send_message(chat_id, text, parse_mode='html')
                if rain_prob > control_rain_prob:
                    text = """<b>😢 Probabilidade de chuva aumentou!!!</b> \n\n🌡️<b>Temp Max:</b> %s\n🌡️<b>Temp Min:</b> %s\n🌧️ <b>Prob. Chuva:</b> %s\n✍️ <b>Desc:</b> %s""" %(str(temp_max),str(temp_min),str(rain_prob),str(description))
                    bot.send_message(chat_id, text, parse_mode='html')
                
                control_rain_prob = rain_prob
                
    # Consultar temperatura de hora em hora
    time.sleep(3600)


        