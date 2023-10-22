# Nyaruko

This repository is for someone to accomplish something.

[中文文档](README.cn.md)

<div align=center>
  <img width="400" src="https://github.com/niracler/nyaruko/assets/24842631/23c3e818-2c06-4589-a226-2ccd310d51db">
</div>

## Build

```bash
x pip install --editable .
```

## Usage

```bash
$ ny
Usage: ny [OPTIONS] COMMAND [ARGS]...

  This is the main entry point for nyaruko.

Options:
  --debug / --no-debug  Print debug messages.
  --help                Show this message and exit.

Commands:
  ascii  Prints the ASCII art of nyaruko.
  bot    Runs the telegram bot.
  list   Lists all article from the sqlite.
  sync   Syncs the obsidian article to the sqlite.
```

## Config

```toml
[default]

article_dir = '/path/to/your/obsidian/vault'
block_dir_list = ["block", "block2"]

[telegram]

token = ********:************************************
proxy = socks5://<ip>:<port>
```

## Etymology

Nyaruko is a character from [Nyaruko: Crawling with Love](https://en.wikipedia.org/wiki/Nyaruko:_Crawling_with_Love)
