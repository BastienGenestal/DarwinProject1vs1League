from DarwinBot import DarwinBot
import os

client = DarwinBot(command_prefix='.')
client.remove_command('help')
client.run(os.environ.get('TOKEN1VS1'))
