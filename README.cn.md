# Nyaruko

我也不知道要干什么的一个仓库。

<div align=center>
  <img width="400" src="https://github.com/niracler/nyaruko/assets/24842631/23c3e818-2c06-4589-a226-2ccd310d51db">
</div>

## 构建

```bash
x pip install --editable .
```

## 用法

```bash
$ ny
用法: ny [选项] 命令 [参数]...

  这是 nyaruko 的主要入口点。

Options:
  --debug / --no-debug  打印调试消息。
  --help                显示此消息并退出。

Commands:
  ascii  打印 nyaruko 的 ASCII 艺术
  bot    运行 Telegram 机器人。
  list   列出所有来自 SQLite 的文章。
  sync   将 Obsidian 文章同步到 SQLite。
```

## 配置文件

```toml
[default]

article_dir = '/path/to/your/obsidian/vault'
block_dir_list = ["block", "block2"]

[telegram]

token = ********:************************************
proxy = socks5://<ip>:<port>
```

## 词源

Nyaruko 是 [Nyaruko: Crawling with Love](https://en.wikipedia.org/wiki/Nyaruko:_Crawling_with_Love) 中的一个角色。
