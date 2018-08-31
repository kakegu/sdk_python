# TrustNote SDK for Python

TrustNote Python SDK is suitable for tokenized applications running on servers, PCs, and IoT devices.

## Setting Up

1. Clone:

```
git clone https://github.com/TrustNoteDevelopers/sdk_python.git
```

2. Install:

```
pip3 install -r requirements.txt
```


## APIs

1. get address

```
python3 demo_wallet.py -i address
```

```
['OQ6VUHO6GLUZBAWKKIMQOE2QQ5HJOQKT', 'ZEA5TC7VOFT52HFTF7C7JX42JSANJR5V', 'BV3T2GYHGML5CGRG5EQNQAEGMB2GKHXX']
```

2. get balance

```
python3 demo_wallet.py -i balance
```

```
{'balance': 487.998695, 'pending': 0.0, 'stable': 487.998695}
```

3. send TTT to address

```
python3 demo_wallet.py -s TTCNYZ72CRDCRLVWF6Y4PYRVNXFPDSUX -a 10 -m "testing for send TTT"
```

## DAG explorer

You can use DAG explorer to check all your transactions now!
```
http://dev.trustnote.org:3000/detail#SLhObv0dFn3bhzzERHt7LujtjQ06+IadHXgzf7YDwlM=

```

## Example videos

[1. get address](https://github.com/TrustNoteDevelopers/sdk_python/raw/master/demo/wallet_get_address.mp4)

[2. get balance](https://github.com/TrustNoteDevelopers/sdk_python/raw/master/demo/wallet_get_balance.mp4)

[3. send ttt](https://github.com/TrustNoteDevelopers/sdk_python/raw/master/demo/send_ttt.mp4)

[4. explorer address](https://github.com/TrustNoteDevelopers/sdk_python/raw/master/demo/explorer_address.mp4)
