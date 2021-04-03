import twint

config = twint.config()
config.Search = "GME"
config.limit = 10

twint.run.search(config)