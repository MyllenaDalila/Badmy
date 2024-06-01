import telebot
import re
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Informações do bot
TOKEN = "7284730348:AAExBcGtDS45cgK5KKleErxJl_JkYp_p3sw"
ADMIN_ID = 1074732606  # ID do Telegram do operador
GRUPO_ALVO_ID = -4130277805  # ID do seu grupo

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda mensagem: re.match(r"^[\d,\se]+$", mensagem.text))
def responder_numeros_questoes(mensagem):
    mensagem_usuario = "Avaliação concluída, até a próxima!"
    bot.reply_to(mensagem, mensagem_usuario)
  
@bot.message_handler(func=lambda mensagem: mensagem.text in ["Sim", "Não"])
def processar_resposta(mensagem):
    if mensagem.text == "Sim":
        bot.send_message(mensagem.chat.id, "Quais foram as questões que você errou essa semana?\n(responda apenas com o número das questões seguido por vírgula: Assim: 1, 2, ..., 18)")
    elif mensagem.text == "Não":
        bot.send_message(mensagem.chat.id, "Parabéns! Avaliação concluída, até a próxima!")

@bot.message_handler(commands=["pronto"])
def pronto(mensagem):
    texto = """Oi, eu sou Myllena² e estou aqui para verificar seu desempenho.
Você errou alguma questão essa semana?"""

    # Cria o teclado
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row(KeyboardButton("Sim"), KeyboardButton("Não"))

    # Envia a mensagem com o teclado
    bot.send_message(mensagem.chat.id, texto, reply_markup=keyboard)

def verificar (mensagem):
    if mensagem.text == "My, análise de desempenho":
        return True
    else: return False

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Claro, já vamos começar.
Assim que quiser, Cássio
Utilize /pronto para iniciar."""
    bot.reply_to (mensagem, texto)

bot.polling()