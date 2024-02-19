import discord
from discord.ext import commands

TOKEN = "MTIwNTE1NTYwNzA4NzQxNTMwNw.GsI5Lo.mORzfy__X8s7zmvvfoscAINTB9gIcN17z0kfkw"
bot = commands.Bot(command_prefix="", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f'{bot.user} está conectado a los siguiente servidores:\n')
    for server in bot.guilds:
        print(f'{server.name}(id: {server.id})')
@bot.command()
async def hola(ctx):
    await ctx.send("callate albondiga")
@bot.command()
async def ip(ctx):
    await ctx.send("antrokiturco.aternos.me")
@bot.command()
async def puerto(ctx):
    await ctx.send("56797")
bot.run(TOKEN)

import wikipedia


def order0(fichero_open):
    try:
        termino_de_contenido = input("introduzca el nombre de la wiki que quieres leer: ")
        page_content = wikipedia.page(termino_de_contenido).content
        for line in page_content:
            fichero_open.write(line)
    except:
        print("pagina no existente, vuelvelo a intentar")

def order1():
    try:
        termino_de_busqueda = input("introduzca termino para ver relacionados: ")
        search_results = wikipedia.search(termino_de_busqueda)
        print(search_results)
    except:
        print("0 resultados")


def main(fichero):

    acabado = False
    while acabado == False:
        fichero_open = open(fichero, "w", )
        print("bienvenido a WikiCathee")
        print("quieres buscar el contenido de una cosa (0) o prefieres buscar paginas relacionadas con tu termino (1)")
        order = int(input("0/1: "))
        if order == 0:
            order0(fichero_open)
        else:
            order1()
        terminar = input("terminaste con el fichero (S/n): ")
        if terminar == "n":
            pass
        else:
            acabado = True
        fichero_open.close()      

if __name__ == "__main__":
    try:
        lengua = input("que idioma hablas (abreviatura): ")
        wikipedia.set_lang(lengua)
    except:
        aceptado = False
        while aceptado == False:
            print("no entiendo ese idioma asi que si eso usare ingles")
            aceptacion_español = input("aceptas S/n: ")
            if aceptacion_español == "n":
                pass
            else:
                aceptado = True
                wikipedia.set_lang("es")

    nombre_elegido = input("nombre del fichero donde quieres trabajar: ")
    fichero_elegido = f"{nombre_elegido}.csv"
    main(fichero_elegido)