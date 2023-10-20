import ccxt
import config

bybit = ccxt.bybit()
bybit.set_sandbox_mode(True)

bybit.apiKey = config.bybit_api_key
bybit.secret = config.bybit_secret_key

balance = bybit.fetch_balance()

print(balance)
