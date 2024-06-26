import click
import operator


@click.command()
@click.argument('a', type=float)
@click.argument('amal', type=click.Choice(['+', '-', '*', '/']))
@click.argument('b', type=float)
def hisobla(a, amal, b):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if b == 0 and amal == '/':
        click.echo("Nolga bo'lish mumkin emas!")
        return

    natija = ops[amal](a, b)
    click.echo(f"{a} {amal} {b} = {natija}")


@click.command()
def aboutme():

    click.echo("Ism: [Ruslanbek]")
    click.echo("Familiya: [Tulqinov]")
    click.echo("Yoshi: [22]")
    click.echo("Tug'ilgan shahri: [Samarqand]")
    click.echo("Kasbi: [Dasturchi]")
    click.echo("Hobbisi: [Shaxmat]")
    click.echo("Ma'lumoti: [Oliy]")
    click.echo("Tugatgan oliy ta'lim muassasasi: [Samarqand davlat universiteti]")
    click.echo("Hozirgi o'qiyotgan ta'lim muassasasi: [PDP University]")
