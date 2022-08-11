# -*- encoding=utf8 -*-
__author__ = "CPU60490"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.cocosjs import CocosJsPoco
poco = CocosJsPoco()

poco("shopPanel").offspring("treasure_section").offspring("shopPanelBackgroundImg").child("<no-name>")[1].offspring("buy_btn")