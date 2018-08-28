#!/usr/bin/env python3
# -*- coding: ascii -*-

# Simple basebot bot template.
import re, sys
import basebot

def maybe_exit(match, meta):
    # Ignore requests not directed at us.
    nickname = match.group(1)
    if not meta['self'].nick_matches(nickname): return
    # Otherwise, respond and exit.
    meta['reply']('/me exits')
    meta['self'].manager.shutdown()

def instant(match, info):
    return '<!' + match.group(0) + '>'

def link(match, info):
    return '<' + match.group(0) + '>'

def main():
    basebot.run_minibot(
        # Name of the bot for logging purposes. If in doubt, set it to the
        # same value as nickname.
        botname='piclink',
        # (Initial) nickname of the bot.
        nickname='piclink',
        # Text to respond with to a general !help command.
        #short_help='I am a testing bot.',
        # Text to respond with to a specific !help command.
        long_help='I make links for instant people. Blame L(eidenfrost) if something goes wrong. Currently hosted by ASCII-art, so you can also blame him. Actually, just blame him. You can also !kill me :D',
        # Bot behavior be here.
        regexes={
            # Insert 'regex': response pairs here.
            # Keep this one in place.
            r'i.imgur.com/[a-zA-Z0-9]+': instant,
            r'i.imgur.com/[a-zA-Z0-9]+(\.png)\S': instant,
            r'i.imgur.com/[a-zA-Z0-9]+(\.jpg)\S': instant,
            r'i.imgur.com/[a-zA-Z0-9]+(\.gif)\S': instant,
            r'i.imgur.com/[a-zA-Z0-9]+(\.mp4)\S': instant,
            r'http://i.imgur.com/[a-zA-Z0-9]+': instant,
            r'http://i.imgur.com/[a-zA-Z0-9]+(\.png)\S': instant,
            r'http://i.imgur.com/[a-zA-Z0-9]+(\.jpg)\S': instant,
            r'http://i.imgur.com/[a-zA-Z0-9]+(\.gif)\S': instant,
            r'http://i.imgur.com/[a-zA-Z0-9]+(\.mp4)\S': instant,
            r'https://i.imgur.com/[a-zA-Z0-9]+': instant,
            r'https://i.imgur.com/[a-zA-Z0-9]+(\.png)\S': instant,
            r'https://i.imgur.com/[a-zA-Z0-9]+(\.jpg)\S': instant,
            r'https://i.imgur.com/[a-zA-Z0-9]+(\.gif)\S': instant,
            r'https://i.imgur.com/[a-zA-Z0-9]+(\.mp4)\S': instant,
            r'imgs.xkcd.com/comics/.+(\.png)': instant,
            r'http://imgs.xkcd.com/comics/.+(\.png)': instant,
            r'https://imgs.xkcd.com/comics/.+(\.png)': instant,
            r'http://\S+':link,
            r'https://\S+':link,
            r'www\.\S+':link,
            r'^!kill\s+@(\S+)\s*$': maybe_exit
        }
    )

if __name__ == '__main__': main()