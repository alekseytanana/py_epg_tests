# -*- coding: utf-8 -*-
from model.channel import Channel
from random import randint
from time import sleep


def test_create_channel(app):
    sleep(1)
    old_channels = app.channel.get_channel_list()
    #print "old_channels", old_channels
    app.channel.create(
        Channel(name='Channel' + str(randint(0, 9999)), service_id="2345", epg_name="epg_name2", offset="3", provider="Provider"))
    sleep(1)
    new_channels = app.channel.get_channel_list()
    #print "new_channels", new_channels
    assert len(new_channels) == len(old_channels) + 1