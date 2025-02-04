from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alex Dyer'

doc = """
Simulador de planeamiento 
"""


class Constants(BaseConstants):
    name_in_url = 'JUEGOSIMULADOR'
    players_per_group = None
    num_rounds = 1
    inventario_inicial = 1000
    inventario_inicialR = 1000

    inventario_inicial2 = 1000
    inventario_inicialR2 = 500

    inventario_inicial3 = 1000
    inventario_inicialR3 = 1000

    inventario_inicial4 = 1000
    inventario_inicialR4 = 500

    LimaDemanda1 = 1700
    LimaDemanda2 = 1400
    LimaDemanda3 = 1400
    LimaDemanda4 = 1700
    LimaDemanda5 = 300
    LimaDemanda6 = 1100
    rojoLimaDemanda1 = 300
    rojoLimaDemanda2 = 600
    rojoLimaDemanda3 = 500
    rojoLimaDemanda4 = 1000
    rojoLimaDemanda5 = 700
    rojoLimaDemanda6 = 800

    LimaDemanda7 = 900
    LimaDemanda8 = 300
    LimaDemanda9 = 1200
    LimaDemanda10 = 400
    LimaDemanda11 = 1700
    LimaDemanda12 = 800
    rojoLimaDemanda7 = 400
    rojoLimaDemanda8 = 1400
    rojoLimaDemanda9 = 100
    rojoLimaDemanda10 = 1100
    rojoLimaDemanda11 = 1400
    rojoLimaDemanda12 = 800

    JaponDemanda1 = 800
    JaponDemanda2 = 3000
    JaponDemanda3 = 1800
    JaponDemanda4 = 1500
    JaponDemanda5 = 1000
    JaponDemanda6 = 2000
    rojoJaponDemanda1 = 1300
    rojoJaponDemanda2 = 200
    rojoJaponDemanda3 = 600
    rojoJaponDemanda4 = 600
    rojoJaponDemanda5 = 1100
    rojoJaponDemanda6 = 200

    JaponDemanda7 = 1300
    JaponDemanda8 = 1100
    JaponDemanda9 = 100
    JaponDemanda10 = 1700
    JaponDemanda11 = 1500
    JaponDemanda12 = 900
    rojoJaponDemanda7 = 100
    rojoJaponDemanda8 = 600
    rojoJaponDemanda9 = 500
    rojoJaponDemanda10 = 600
    rojoJaponDemanda11 = 800
    rojoJaponDemanda12 = 700

    HanoiDemanda1 = 1300
    HanoiDemanda2 = 800
    HanoiDemanda3 = 800
    HanoiDemanda4 = 800
    HanoiDemanda5 = 700
    HanoiDemanda6 = 1000
    rojoHanoiDemanda1 = 900
    rojoHanoiDemanda2 = 600
    rojoHanoiDemanda3 = 600
    rojoHanoiDemanda4 = 800
    rojoHanoiDemanda5 = 800
    rojoHanoiDemanda6 = 800

    HanoiDemanda7 = 900
    HanoiDemanda8 = 800
    HanoiDemanda9 = 900
    HanoiDemanda10 = 1200
    HanoiDemanda11 = 800
    HanoiDemanda12 = 700
    rojoHanoiDemanda7 = 1000
    rojoHanoiDemanda8 = 900
    rojoHanoiDemanda9 = 800
    rojoHanoiDemanda10 = 1000
    rojoHanoiDemanda11 = 900
    rojoHanoiDemanda12 = 700

    MexicoDemanda1 = 1100
    MexicoDemanda2 = 1000
    MexicoDemanda3 = 800
    MexicoDemanda4 = 1400
    MexicoDemanda5 = 1300
    MexicoDemanda6 = 1200
    rojoMexicoDemanda1 = 500
    rojoMexicoDemanda2 = 500
    rojoMexicoDemanda3 = 600
    rojoMexicoDemanda4 = 600
    rojoMexicoDemanda5 = 500
    rojoMexicoDemanda6 = 500

    MexicoDemanda7 = 1200
    MexicoDemanda8 = 900
    MexicoDemanda9 = 1000
    MexicoDemanda10 = 1200
    MexicoDemanda11 = 1700
    MexicoDemanda12 = 1100
    rojoMexicoDemanda7 = 600
    rojoMexicoDemanda8 = 400
    rojoMexicoDemanda9 = 700
    rojoMexicoDemanda10 = 600
    rojoMexicoDemanda11 = 400
    rojoMexicoDemanda12 = 700


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    ProduccionLima1 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima2 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima3 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima4 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima5 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima6 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima7 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima8 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima9 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima10 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima11 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima12 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima1 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima2 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima3 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima4 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima5 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima6 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima7 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima8 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima9 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima10 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima11 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima12 = models.IntegerField(initial=0, min=0, max=1500, label="")

    tabla1 = models.BooleanField(label="¿Deseas calcular tus costos antes de pasar de periodo? - Si elige SI y apreta next se actualizaran los costos con la produccion que propuso")

    ProduccionJapon1 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon2 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon3 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon4 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon5 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon6 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon7 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon8 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon9 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon10 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon11 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionJapon12 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon1 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon2 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon3 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon4 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon5 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon6 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon7 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon8 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon9 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon10 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon11 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionJapon12 = models.IntegerField(initial=0, min=0, max=1500)

    ProduccionHanoi1 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi2 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi3 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi4 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi5 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi6 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi7 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi8 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi9 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi10 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi11 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi12 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi1 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi2 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi3 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi4 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi5 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi6 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi7 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi8 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi9 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi10 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi11 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi12 = models.IntegerField(initial=0, min=0, max=1500)

    ProduccionMexico1 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico2 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico3 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico4 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico5 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico6 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico7 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico8 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico9 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico10 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico11 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico12 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico1 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico2 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico3 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico4 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico5 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico6 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico7 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico8 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico9 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico10 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico11 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico12 = models.IntegerField(initial=0, min=0, max=1500)

