class Paginator:
    def __init__(self, ctx, pages):
        self.ctx = ctx
        self.pages = pages
        self.current_page = 0
        self.message = None

    async def start(self):
        self.message = await self.ctx.send(embed=self.create_embed())
        await self.message.add_reaction('⬅️')
        await self.message.add_reaction('➡️')
        bot.loop.create_task(self.wait_for_reactions())

    def create_embed(self):
        embed = discord.Embed(title="Commandes d'aide", description=self.pages[self.current_page], color=0x00000)
        embed.set_footer(text='# status du bot')
        return embed

    async def wait_for_reactions(self):
        def check(reaction, user):
            return user == self.ctx.author and str(reaction.emoji) in ['⬅️', '➡️'] and reaction.message.id == self.message.id

        while True:
            reaction, user = await bot.wait_for('reaction_add', check=check)
            if str(reaction.emoji) == '⬅️':
                self.current_page = max(0, self.current_page - 1)
            elif str(reaction.emoji) == '➡️':
                self.current_page = min(len(self.pages) - 1, self.current_page + 1)
            await self.message.edit(embed=self.create_embed())
            await self.message.remove_reaction(reaction, user)




@bot.command()
async def help(ctx):
    pages = [
        (
            "Commandes Page 1/2:\n"
            "1. `+exemple` - description\n"
            "2. `+exemple` - description\n"
            "3. `+exemple` - description\n"
            "4. `+exemple` - description\n"
            "5. `+exemple` - description\n"
        ),
        (
            "Commande Page 2/2:\n"
 
            "1. `+exemple` - description\n"
            "2. `+exemple` - description\n"
            "3. `+exemple` - description\n"
            "4. `+exemple` - description\n"
            "5. `+exemple` - description\n"
        )
    ]
 
    paginator = Paginator(ctx, pages)
    await paginator.start()
