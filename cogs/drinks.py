from discord.ext import commands
from random import randint

import milkman
from cup import FreezeMilk


class Drinks:
    def __init__(self, bot):
        self.bot = bot

    def get_state(self, context):
        freeze_milk = FreezeMilk(context.message.server)
        freeze_milk.get_milk_stats()

        return freeze_milk

    @commands.command(name='cup',
                      description="Shows your cup's current level and fill",
                      brief="Show your cups current state",
                      pass_context=True)
    async def cup(self, context, mention: str = None):
        freeze_milk = self.get_state(context)

        if mention and context.message.mentions:
            current_cup = freeze_milk.stats[context.message.mentions[0]]
        else:
            current_cup = freeze_milk.stats[context.message.author]

        await self.bot.send_message(context.message.channel, current_cup.draw())

        freeze_milk.save_milk_stats()

    @commands.command(name='pour',
                      description="Pour some milk into a cup",
                      brief="Pour some milk",
                      pass_context=True)
    async def pour_cup(self, context, mention: str = None):
        freeze_milk = self.get_state(context)

        if mention and context.message.mentions:
            current_cup = freeze_milk.stats[context.message.mentions[0]]
        else:
            current_cup = freeze_milk.stats[context.message.author]
        filled_level = current_cup.pour()
        if not filled_level:
            pre_text = "Wtf dude you spilt the milk? You're getting a downgrade lol"
            await self.bot.send_file(context.message.channel,
                                     milkman.create_spillman(context.message.author.avatar_url))
        else:
            pre_text = "milk level: " + str(filled_level) + " "

        await self.bot.send_message(context.message.channel, pre_text + current_cup.draw())

        freeze_milk.save_milk_stats()

    @commands.command(name='drink',
                      description="Drink some milk",
                      brief="Drink some milk",
                      pass_context=True)
    async def drink(self, context, mention: str = None):
        chance = randint(0, 100)
        freeze_milk = self.get_state(context)

        if mention and context.message.mentions:
            current_cup = freeze_milk.stats[context.message.mentions[0]]
        else:
            current_cup = freeze_milk.stats[context.message.author]

        if mention and context.message.mentions:
            if chance < 2:
                current_cup.spill()
                pre_text = "God damn, you knocked your glass off the table. Downgrade for you"
            else:
                current_cup = freeze_milk.stats[context.message.mentions[0]]

        if chance < 2:
            current_cup.spill()
            pre_text = "God damn, you knocked your glass off the table. Downgrade for you"
        else:
            full_cup = current_cup.drink()
            pre_text = ""
            if full_cup:
                pre_text = "You drunk a full glass of milk. Upgrade time! "
            else:
                pre_text = "Aww jeez, your cup wasn't full. No upgrade for you"

        await self.bot.send_message(context.message.channel, pre_text + current_cup.draw())

        freeze_milk.save_milk_stats()


def setup(bot):
    bot.add_cog(Drinks(bot))
