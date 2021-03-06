from discord import Embed
from discord.ext import commands
import praw
import random
from config import Config


class Redditor:
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(user_agent='milk', client_id=Config().r_id, client_secret=Config().r_secret)

    @commands.command(name='meme',
                      description="posts a meme",
                      brief="posts a meme",
                      pass_context=True)
    async def get_meme(self, context):
        post = self.get_hot_post("meme")
        print(str(post.url))
        embed = self.embed_post(post)
        await self.bot.send_message(context.message.channel, embed=embed)

    @commands.command(name='hacks',
                      description="display a life hackety hack",
                      brief="check me out",
                      pass_context=True)
    async def get_hack(self, context):
        post = self.get_hot_post("LifeHacks")
        embed = self.embed_post(post)
        await self.bot.send_message(context.message.channel, embed=embed)

    @commands.command(name='hungry',
                      description="Shows some tasty food",
                      brief="YUMMY yummy",
                      pass_context=True)
    async def get_food(self, context):
        post = self.get_hot_post("FoodPorn")
        embed = self.embed_post(post)
        await self.bot.send_message(context.message.channel, embed=embed)

    @commands.command(name='fortnite',
                      description="FortNiteBR",
                      brief="Ah ye",
                      pass_context=True)
    async def get_fortnite(self, context):
        post = self.get_hot_post("FortNiteBR")
        await self.bot.send_message(context.message.channel, post.url)

    @commands.command(name='code',
                      description="Programmer Humor",
                      brief="Programmer Humor",
                      pass_context=True)
    async def get_code_funny(self, context):
        post = self.get_hot_post("ProgrammerHumor")
        await self.bot.send_message(context.message.channel, post.url)

    @commands.command(name='moooies',
                      description="Tiddies",
                      brief="Hot Chicks, maybe nsfw",
                      pass_context=True)
    async def get_hot_chicks(self, context):
        post = self.get_hot_post(random.choice(["boobs", "fortyfivefiftyfive", "sideboob", "underboob", "goddesses"]))
        embed = self.embed_post(post)
        await self.bot.send_message(context.message.channel, embed=embed)

    def get_hot_post(self, topic):
        """Returns a random hot post from a given subreddit topic"""
        sub = self.reddit.subreddit(topic)
        submissions = [post for post in sub.hot(limit=20)]
        random_post_number = random.randint(0, 20)
        return submissions[random_post_number]

    @staticmethod
    def embed_post(post):
        """Returns an embedded post"""
        # if it has an image without filetype add .jpg
        embed = Embed(title=post.title, color=0xf5ffcd, url=post.url)
        embed.set_image(url=post.url)
        embed.set_footer(text=f"\U0001F44D {post.score} \U0001F4AC {post.num_comments}")
        return embed

    def video_post(self, post):
        if post.is_video:
            return post



def setup(bot):
    bot.add_cog(Redditor(bot))
