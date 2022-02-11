from discord.ext import commands#type:ignore
import cv2 as cv#type:ignore
from typing import Generator
import discord#type:ignore
import numpy as np
import os

from culmination import cfs_combiner, filter_cfs, random_cfs, submit_cfs
from assisters.myconsts import CFS_ENTIRE_PROBLEM_FILENAME, TAG_OPTIONS
from assisters.mytypes import Problem

bot = commands.Bot(command_prefix='cf ')

@bot.event
async def on_ready() -> None:
    await bot.change_presence(status=discord.Status.invisible)
    print(f'{bot.user} connected')

async def export_cfs_to_discord(ctx, problem: Problem) -> None:
    crops: Generator[np.ndarray, None, None] = cfs_combiner(problem)
    await ctx.send(f'submit at ```{submit_cfs(problem)}```')

    for crop in crops:
        filename = f'temp.jpg'
        cv.imwrite(filename, crop)
        await ctx.send(file=discord.File(filename))
        os.remove(filename)


@bot.command(name="p", pass_context=True, help='sends codeforce problem with problem code requested, ex. 1540A, 1431E')
async def problem(ctx, problem: str):
    """user types a codeforce problem code, function crops and sends back"""
    
    try:
        await export_cfs_to_discord(ctx, problem)
    except AssertionError as error_msg:
        await ctx.send(f'```{error_msg}```')
    finally:
        os.remove(CFS_ENTIRE_PROBLEM_FILENAME)

@bot.command(name='rand', help='sends random codeforce problem')
async def random(ctx) -> None:
    """user types 'random' and function finds it, crops and sends it back"""

    try:
        random = random_cfs()
        await export_cfs_to_discord(ctx, random)
    except AssertionError as error_msg:
        await ctx.send(f'```{error_msg}```')
    finally:
        os.remove(CFS_ENTIRE_PROBLEM_FILENAME)

@bot.command(name='filt', help='sends random codeforce problem fitting given requirements')
async def filter(ctx, min_rating: int, max_rating: int, *tags: str) -> None:
    """filters problems using sent requests"""

    try:
        filtered_prob = filter_cfs(min_rating, max_rating, tags)
        await export_cfs_to_discord(ctx, problem=filtered_prob)
    except AssertionError as error_msg:
        await ctx.send(f'```{error_msg}```')
    finally:
        os.remove(CFS_ENTIRE_PROBLEM_FILENAME)

@bot.command(name='subm', help='links to codeforce page with submission space highlighted')
async def submit(ctx, problem: str) -> None:
    """function to submit a problem at the link"""

    try:
        link = submit_cfs(problem)
        await ctx.send(f'```Submit at {link}```')
    except:
        await ctx.send('```Problem does not exist```')

@bot.command()
async def filterslist(ctx):
    await ctx.send(TAG_OPTIONS)

TOKEN = 'YOUR TOKEN HERE'
bot.run(TOKEN)