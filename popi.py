import discord
mesajlar = []
listee = []
wordcount={}
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        

    async def on_message(self, message,*args):
        global mesajlar
        global listee
        global wordcount
        if message.content.startswith('!yaz'):
            find_max = lambda x: [
                *filter(
                    lambda i: i, map(
                        lambda j: (j, y[j]) if y[j] == max(y.values()) else [],
                        (y := {k: x.count(k) for k in x})
                        )
                    )
                ]

            def unnest(x: list = []):
                result = []
                for i in x:
                    if isinstance(i, list):
                        result.extend(unnest(i))
                    else:
                        result.append(i)
                return result
            for i in mesajlar:
                listee.append(mesajlar.count(i))
            enBuyuk = (max(listee))
            await message.channel.send(find_max(unnest(mesajlar)))

##            await message.channel.send(mesajlar)
            return
        mesaj = message.content.split(" ")
        mesajlar.append(mesaj)

client = MyClient()
client.run("NzIzOTM0MTQ4NTgyMDQ3ODA1.Xu43Fw.8crkh9r1HKKm0x2X1KcqRl2H66g")
