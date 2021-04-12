from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']



client = discord.Client()

@client.event
@asyncio.coroutine
async def on_ready():
    pass
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    matchDice = re.search(r'1d100 <= (\d+)', message.content)
    
    # 1d100 <= '数字' で1d100の判定が出来る
    if matchDice:
        num = randNum()
        targetNum = matchDice.group(1)
        resultMessage = '1D100 <= ' + str(targetNum) + '→' + str(num)
        if num <= int(targetNum):
            await client.send_message(message.channel, resultMessage + '成功')
        else:
            await client.send_message(message.channel, resultMessage + '失敗')
    # お試し100面ダイス振るだけよう
    elif message.content == '1d100':
        num = randNum()
        await client.send_message(message.channel, str(num) + 'だよ')

def randNum():
    # 乱数精製
    randomNum = random.randint(1,100)
    return randomNum

client.run(【Token】)

bot.run(token)
