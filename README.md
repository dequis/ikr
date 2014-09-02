# ikr

A more serious and decent take on the idea of lists of items that can be voted on. It's [idk][] for when you actually *know*.

Two hour short project for fun. This is pretty much just idk 2.0, with [dataset][] instead of [gspread][]

> *From ignorance, lead me to truth*

## Why

I realized I've been doing some sort of personal idea voting system in a
notepad. Etherpad, specifically. I'm trying to move away from pads, but the
TODO list software i'm using can't handle this kind of prioritization very
well, so i said "fuck it, i know i **can** make one myself in one hour or so."

Being able to say that is a sign that idk was a success, by the way.

## Features

 * Multiple lists
 * Javascript voting
 * Actually supports real databases through [dataset][] (defaults to sqlite)
 * Random list name generator for shallow privacy
 * General purpose
 * Less insanity, in general
 * Votes still lack any kind of rate limiting, though

## Is it any good?

[Yes][yes]

[yes]: https://news.ycombinator.com/item?id=3067434

## Screenshots

![](http://dump.dequis.org/jjhu9.png)

[idk]: http://github.com/dequis/idk
[dataset]: http://dataset.readthedocs.org/
[gspread]: https://github.com/burnash/gspread
