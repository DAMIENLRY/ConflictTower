from abc import ABC
from .InterfaceCase import InterfaceCase
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide
from .states.StateCard import StateCard
import time
import sys
import os
import threading
import api.towerFinder as tf

from api.globaleVariable import COLUMNS, ROWS, TOWER_SIDE_1, TOWER_SIDE_2

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(current_file) # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from server.res.cases.DamageCase import DamageCase
from server.res.cards.states.FocusTowerState import FocusTowerState

class InterfaceCard(InterfaceCase):

    _SPEED: EnumEntitySpeed
    _RANGE: int
    _ATTAQUE_SPEED: EnumEntitySpeed
    _TYPE: EnumEntityType
    _HEALTH_POINT: int
    _POINT: int
    _state: StateCard
    _side: EnumSide
    _stop_movement = True
    _stop_attack = False
    _battlefield = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: StateCard):
        self._state = new_state

    def getSide(self) -> EnumSide:
        return self._side

    def isWithinBounds(self, x, y):
        return 0 <= x < ROWS and 0 <= y < COLUMNS


    def reduceHealth(self, damage_amount):
        self._HEALTH_POINT -= damage_amount
        if self._HEALTH_POINT <= 0:
            self.handleDefeat()
            self._HEALTH_POINT = 0

    def handleDefeat(self):
        print(f"{self.__class__.__name__} a été vaincu.")
        self._battlefield.removeTroop(self)




    def start_attack_thread(self):
        self.attack_thread = threading.Thread(target=self.attack_loop)
        self.attack_thread.start()

    def stop_attack_thread(self):
        self._stop_attack = True

    def attack_loop(self):
        self._stop_attack = False
        while not self._stop_attack and self._HEALTH_POINT > 0:
            print(self._NAME + " "+str(self._HEALTH_POINT))

            opponent = self.opponentInRange()            
            if(opponent):
                opponentEmptyCase = self.getNearestEmptyCase(opponent._x_position, opponent._y_position, opponent._RANGE)
                if(opponentEmptyCase is not False):
                    opponentCard = self._battlefield.isOccupiedByOpponent(opponent._x_position, opponent._y_position)
                    opponentCard.reduceHealth(self._ATTACK_DAMAGE)
                    if(opponentCard._HEALTH_POINT <= 0):
                        self._stop_attack = True
                    
                    dmgCase = DamageCase(opponentEmptyCase[0], opponentEmptyCase[1])
                    self._battlefield.addDamageCase(dmgCase)
                    time.sleep(0.3)
                    self._battlefield.removeDamageCase(dmgCase)
                    
                    time.sleep(self.getAttackSpeedInterval())
            else:
                self._stop_attack = True
        self.state = FocusTowerState()
        self.state.handle_request(self)



    def start_movement_thread(self):
        path = tf.pathToTower((self.getX(),self.getY()),self.getTowerFocusCoordoonates())
        self.movement_thread = threading.Thread(target=self.movement_loop, args=(path,))
        self.movement_thread.start()

    def stop_movement_thread(self):
        self._stop_movement = True

    def movement_loop(self, path):
        self._stop_movement = False
        for x, y in path:
            if self._stop_movement:
                break
            self.setLocation(x, y)
            time.sleep(self.getMoveSpeedInterval())
        print("Movement thread stopped.")


    def getAttackSpeedInterval(self):
        return self._ATTAQUE_SPEED.value

    def getMoveSpeedInterval(self):
        return self._SPEED.value

    def getTowerFocusCoordoonates(self):
        return TOWER_SIDE_2[0] if self.getSide() == EnumSide.SIDE_1 else TOWER_SIDE_1[0]

    def setLocation(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
            self._battlefield.onUpdateMap()
        else:
            return False

    def getNearestEmptyCase(self, xOp, yOp, rangeOp):
        offsets = [
            (dx, dy) for dx in range(-rangeOp, rangeOp + 1)
            for dy in range(-rangeOp, rangeOp + 1)
            if not (dx == 0 and dy == 0)
        ]

        for dx, dy in offsets:
            targetX, targetY = dx + xOp, dy + yOp

            if self.isWithinBounds(targetX, targetY):
                emptyCase = self._battlefield.isCaseEmpty(targetX, targetY)
                if emptyCase:
                    return (targetX,targetY)
        return False

    def opponentInRange(self):
        offsets = [
            (dx, dy) for dx in range(-self._RANGE, self._RANGE + 1)
            for dy in range(-self._RANGE, self._RANGE + 1)
            if not (dx == 0 and dy == 0)
        ]

        for dx, dy in offsets:
            targetX, targetY = dx + self._x_position, dy + self._y_position

            if self.isWithinBounds(targetX, targetY):
                opponent = self._battlefield.isOccupiedByOpponent(targetX, targetY)
                if opponent:
                    return opponent
        return False
