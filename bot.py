import discord
from discord.ext import commands
from datetime import timedelta

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

VOICE_EMOJI = "🎧"   # الإيموجي الذي يظهر بجانب الاسم داخل الفويس

@bot.event
async def on_ready():
    print(f"{bot.user} شغال !")

# -------------------------------
#  Emoji Voice
# -------------------------------
@bot.event
async def on_voice_state_update(member, before, after):
    try:
        if after.channel is not None:  # دخل فويس
            new_nick = f"{VOICE_EMOJI} {member.name}"
            await member.edit(nick=new_nick)
        else:  # خرج من الفويس
            await member.edit(nick=None)
    except:
        pass

# -------------------------------
#  Ban user
# -------------------------------
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="بدون سبب"):
    await member.ban(reason=reason)
    await ctx.send(f"تم حظر {member.mention}")

# -------------------------------
# Timeout user
# -------------------------------
@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, minutes: int):
    duration = timedelta(minutes=minutes)
    await member.timeout(duration)
    await ctx.send(f"تم تقييد {member.mention} لمدة {minutes} دقيقة")

# -------------------------------
#  Move user
# -------------------------------
@bot.command()
@commands.has_permissions(move_members=True)
async def move(ctx, member: discord.Member, channel: discord.VoiceChannel):
    await member.move_to(channel)
    await ctx.send(f"تم نقل {member.mention} إلى {channel.name}")

# -------------------------------
#  Create Role
# -------------------------------
@bot.command()
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, *, name):
    role = await ctx.guild.create_role(name=name)
    await ctx.send(f"تم إنشاء رتبة: {role.name}")

# -------------------------------
#  Add Role / Give Role
# -------------------------------
@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"تم إعطاء {role.name} إلى {member.mention}")

# -------------------------------
#  Send Message
# -------------------------------
@bot.command()
@commands.has_permissions(manage_messages=True)
async def sendmsg(ctx, channel: discord.TextChannel, *, message):
    await channel.send(message)
    await ctx.send("تم إرسال الرسالة")

# -------------------------------
#  Tag Everyone
# -------------------------------
@bot.command()
@commands.has_permissions(mention_everyone=True)
async def alleveryone(ctx, *, message=""):
    await ctx.send(f"@everyone {message}")

# -------------------------------
# Panel Punishment (قائمة أوامر)
# -------------------------------
@bot.command()
async def panel(ctx):
    await ctx.send(
        "**Panel Punishment:**\n"
        "`!ban @user <reason>`\n"
        "`!timeout @user <minutes>`\n"
        "`!move @user <voice>`\n"
        "`!create_role <name>`\n"
        "`!addrole @user <role>`\n"
        "`!sendmsg <channel> <message>`\n"
        "`!alleveryone <msg>`"
    )

# -------------------------------
# تشغيل البوت
# -------------------------------
bot.run("MTQ0OTA2MzQzNTkwMjkxMDUyNg.G2m9a-.dFVA_SsrJ-ORq-GmfPBJhLib8DyKg_KQlLC0-Y")