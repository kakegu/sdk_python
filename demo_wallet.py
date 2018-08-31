import click
import sdk
import json
import os
@click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
@click.option('-i', help='address:')
@click.option('-s', help='send')
@click.option('-a', help='amount')
@click.option('-m', help='msg')

def cmd_wallet(i,s,a,m):
    if i:
        text = ""
        if (i == "address"):
            text = sdk.get_all_address()

        if (i == "balance"):
            text = sdk.get_balance_all()

        if (i == "keys"):
            keysfile = "{0}/.config/lightwallet/keys.json".format(os.environ['HOME'])
            text = open(keysfile).read()
        click.echo('{0}'.format(text))

    if s and a:
        if m:
            state,text = sdk.pay_with_msg(s,a,m)
            if state=="error":
                click.echo('{0}'.format(text))
            else:
                click.echo('http://dev.trustnote.org:3000/detail#{0}'.format(text))
        else:
            state,text = sdk.pay(s,a)
            if state=="error":
                click.echo('{0}'.format(text))
            else:
                click.echo('http://dev.trustnote.org:3000/detail#{0}'.format(text))
if __name__ == '__main__':
    cmd_wallet()
