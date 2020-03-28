import discord
from discord.ext import commands

class NotInGuildError(Exception):
    def __init__(self, *args):
        print(
            "I don't appear to be in my master guild. Constants could not be initialized properly. Proceed with caution"
        )
        for arg in args:
            print(repr(arg))

class Constants(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if self.bot.is_ready():
            self.on_ready()

    @commands.Cog.listener()
    async def on_ready(self):
        guild = 684492926528651336
        roles = {
            "Owners": 684493117017161963,
            "Moderators": 686310450618695703,
            "Helpers": 686317204752302091,
            "Translators": 691778934471131136,
        }

        self.bot.set(
            "guild",
            self.bot.get_guild(guild)
        )

        if not self.bot.guild:
            raise NotInGuildError(f"Not in guild ID {guild}, have I been kicked or has it been deleted?")

        self.bot.set(
            "staff_roles",
            {}
        )

        for role, role_id in roles.items():
            found_role = self.bot.guild.get_role(role_id)
            if found_role:
                self.bot.staff_roles[role] = found_role
            else:
                print(f"The {role} role (ID {role_id}) was not found. Ignoring...")

        self.bot.set(
            "constants_initialized",
            True
        )

        print("Initialization completed!")


def setup(bot):
    bot.set(
        "constants_initialized",
        False
    )

    bot.set(
        "colors",
        {
            "error": discord.Color(0xf44336),
            "success": discord.Color(0x8bc34a),
            "status": discord.Color(0x3f51b5),
            "info": discord.Color(0x212121)
        }
    )

    bot.set(
        "emojis",
        {
            "choice": "<a:blobcouncil:527721654361522186>",
            "success": "<:blobenjoy:527721625257508866>",
            "status": "<:blobnitro:527721625659899904>",
            "error": "<:bloboutage:527721625374818305>",
            "valueerror": "<:blobfrowningbig:527721625706168331>",
            "leave": "<a:blobleave:527721655162896397>",
            "enter": "<a:blobjoin:527721655041261579>",
            "tsar": "<:blobfingerguns:527721625605636099>",
            "settings": "<:blobidea:527721625563693066>",
            "uhoh": "<a:blobnervous:527721653795291136>",
            "winner": "<a:blobparty:527721653673918474>",
        }
    )

    bot.add_cog(
        Constants(bot)
    )
