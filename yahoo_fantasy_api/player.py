#!/bin/python

from yahoo_fantasy_api import yhandler
import objectpath

class Player:
    """An abstraction for all of the player-level APIs in Yahoo! fantasy

    :param sc: Fully constructed session context
    :type sc: :class:`yahoo_oauth.OAuth2`
    :param player_id: Player ID to setup this class for.  All API requests
        will be for this player.
    :type player_id: str
    """
    def __init__(self, sc, player_id, handler=None) -> None:
        self.sc = sc
        self.player_id = player_id
        if (handler != None):
            self.yhandler = handler
        else:
            self.yhandler = yhandler.YHandler(sc)
    
    def inject_yhandler(self, yhandler):
        self.yhandler = yhandler
