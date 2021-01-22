import enum
import random

class Card(enum.Enum):
    spy = 0
    guard = 1
    elvish = 2
    sphere = 3
    simian = 4
    wraith = 5
    cantor = 6
    stinger = 7
    tinder = 8
    informer = 9
    rogue = 10
    florahedron = 11
    petal = 20
    forest = 21
    grant = 22
    dark = 23
    cabal = 24
    culling = 25
    songs = 26
    rite = 27
    manamorphose = 28
    commune = 29
    plunge = 30
    star = 31
    drum = 32
    looting = 33
    desperate = 34
    bauble = 35
    dread = 40
    dregscape = 41
    lotleth = 42
    narcomoeba = 42
    void = 50

    def __lt__(self, other):
        return self.value < other.value

class Game:
    def __init__(self, hand):
        self.from_deck(hand)

        self.G = 0
        self.R = 0
        self.B = 0
        self.played_forest = 1
        self.granted = 0
        self.threshold = 0
        self.rites_graveyard = 0
        self.creatures_graveyard = 0
        self.creatures = 0
        self.turn = 1
        self.best_turn = 99
        self.nb_cards = 7 # Modify maximum hand size here
        self.bottomed = 0
        self.drummable = 0
    
    def from_deck(self, hand):
        self.spy = hand.count(Card.spy)
        self.guard = hand.count(Card.guard)
        self.elvish = hand.count(Card.elvish)
        self.sphere = hand.count(Card.sphere)
        self.simian = hand.count(Card.simian)
        self.wraith = hand.count(Card.wraith)
        self.cantor = hand.count(Card.cantor)
        self.cabal = hand.count(Card.cabal)
        self.dark = hand.count(Card.dark)
        self.culling = hand.count(Card.culling)
        self.manamorphose = hand.count(Card.manamorphose)
        self.songs = hand.count(Card.songs)
        self.commune = hand.count(Card.commune)        
        self.rite = hand.count(Card.rite)
        self.petal = hand.count(Card.petal)
        self.dread = hand.count(Card.dread)
        self.dregscape = hand.count(Card.dregscape)
        self.lotleth = hand.count(Card.lotleth)
        self.narcomoeba = hand.count(Card.narcomoeba)
        self.stinger = hand.count(Card.stinger)
        self.tinder = hand.count(Card.tinder)
        self.forest = hand.count(Card.forest)
        self.grant = hand.count(Card.grant)
        self.informer = hand.count(Card.informer)
        self.plunge = hand.count(Card.plunge)
        self.star = hand.count(Card.star)
        self.drum = hand.count(Card.drum)
        self.rogue = hand.count(Card.rogue)
        self.florahedron = hand.count(Card.florahedron)
        self.looting = hand.count(Card.looting)
        self.desperate = hand.count(Card.desperate)
        self.bauble = hand.count(Card.bauble)

    def add_card(self, card, val = 1):
        if card == Card.spy:
            self.spy += val
        elif card == Card.guard:
            self.guard += val
        elif card == Card.elvish:
            self.elvish += val
        elif card == Card.sphere:
            self.sphere += val
        elif card == Card.simian:
            self.simian += val
        elif card == Card.wraith:
            self.wraith += val
        elif card == Card.cantor:
            self.cantor += val
        elif card == Card.stinger:
            self.stinger += val
        elif card == Card.tinder:
            self.tinder += val
        elif card == Card.cabal:
            self.cabal += val
        elif card == Card.dark:
            self.dark += val
        elif card == Card.culling:
            self.culling += val
        elif card == Card.plunge:
            self.plunge += val
        elif card == Card.rite:
            self.rite += val
        elif card == Card.songs:
            self.songs += val
        elif card == Card.manamorphose:
            self.manamorphose += val
        elif card == Card.commune:
            self.commune += val
        elif card == Card.petal:
            self.petal += val
        elif card == Card.forest:
            self.forest += val
        elif card == Card.grant:
            self.grant += val
        elif card == Card.dread:
            self.dread += val
        elif card == Card.dregscape:
            self.dregscape += val
        elif card == Card.lotleth:
            self.lotleth += val
        elif card == Card.narcomoeba:
            self.narcomoeba += val
        elif card == Card.star:
            self.star += val
        elif card == Card.drum:
            self.drum += val
        elif card == Card.rogue:
            self.rogue += val
        elif card == Card.florahedron:
            self.florahedron += val
        elif card == Card.looting:
            self.looting += val
        elif card == Card.desperate:
            self.desperate += val
        elif card == Card.bauble:
            self.bauble += val

class Deck:
    def __init__(self):
        # Modify decklist here
        deck = []
        deck += [Card.petal] * 4
        deck += [Card.simian] * 4
        deck += [Card.wraith] * 4
        deck += [Card.cantor] * 4
        deck += [Card.manamorphose] * 4
        deck += [Card.tinder] * 4
        deck += [Card.dark] * 4
        deck += [Card.cabal] * 4
        deck += [Card.rite] * 4
        deck += [Card.culling] * 4

        deck += [Card.plunge] * 1
        deck += [Card.sphere] * 6 # Or Ornithopter
        deck += [Card.star] * 3 # Or Chromatic Sphere

        deck += [Card.spy] * 4
        deck += [Card.informer] * 1
        deck += [Card.dread] * 1
        deck += [Card.dregscape] * 1 # If modified, need to change win condition (number of creatures)
        deck += [Card.lotleth] * 1
        deck += [Card.narcomoeba] * 2 # If modified, need to change win condition (number of creatures)

        deck += [Card.commune] * 0
        deck += [Card.songs] * 0
        deck += [Card.guard] * 0
        deck += [Card.grant] * 0 # If modified, need to change played_forest to 0
        deck += [Card.forest] * 0 # If modified, need to change played_forest to 0
        deck += [Card.elvish] * 0
        deck += [Card.drum] * 0
        deck += [Card.stinger] * 0

        deck += [Card.rogue] * 0
        deck += [Card.florahedron] * 0
        deck += [Card.looting] * 0
        deck += [Card.desperate] * 0 # Or pyretic
        deck += [Card.bauble] * 0 # If modified, need to change win condition (alternative kill)

        deck += [Card.void] * 0
        print(len(deck))
        self.deck = deck
        self.game = self.get_hand()
        
    def get_hand(self):
        random.shuffle(self.deck)
        game = Game(self.deck[:7])
         # Modify maximum hand size here
        game.draws = self.deck[7:7+4+4+3] # Wraiths + Manamorphoses + Stars
        game.draws.append(Card.spy)
        # game.draws.append(Card.forest)
        game.n_draws = 0
        return game

    def drumming(self, game):
        if game.drummable >= 1:
            game.drummable -= 1
            game.B += 1
            self.run(game)
            game.B -= 1
            game.R += 1
            self.run(game)
            game.R -= 1
            game.G += 1
            self.run(game)
            game.G -= 1
            game.drummable += 1

    def run(self, game):
        if game.turn >= game.best_turn:
            return game.best_turn

        # print(game.__dict__)
        if game.nb_cards >= 1:
            if game.wraith >= 1:
                card = game.draws[game.n_draws]
                game.n_draws += 1
                game.wraith -= 1
                game.creatures_graveyard += 1
                game.threshold += 1
                game.add_card(card, 1)
                self.run(game)
                game.add_card(card, -1)
                game.threshold -= 1
                game.creatures_graveyard -= 1
                game.wraith += 1
                game.n_draws -= 1
                return game.best_turn

            if game.commune >= 1 and game.G >= 1:
                cards = game.draws[game.n_draws:game.n_draws + 5]
                game.n_draws += 5

                game.commune -= 1
                game.G -= 1
                game.threshold += 1
                
                if Card.spy in cards:
                    game.spy += 1
                    self.run(game)
                    game.spy -= 1
                if Card.guard in cards:
                    game.guard += 1
                    self.run(game)
                    game.guard -= 1
                if Card.elvish in cards:
                    game.elvish += 1
                    self.run(game)
                    game.elvish -= 1
                if Card.sphere in cards:
                    game.sphere += 1
                    self.run(game)
                    game.sphere -= 1
                if Card.cantor in cards:
                    game.cantor += 1
                    self.run(game)
                    game.cantor -= 1
                if Card.simian in cards:
                    game.simian += 1
                    self.run(game)
                    game.simian -= 1
                if Card.wraith in cards:
                    game.wraith += 1
                    self.run(game)
                    game.wraith -= 1
                if Card.stinger in cards:
                    game.stinger += 1
                    self.run(game)
                    game.stinger -= 1
                if Card.tinder in cards:
                    game.tinder += 1
                    self.run(game)
                    game.tinder -= 1
                if Card.informer in cards:
                    game.informer += 1
                    self.run(game)
                    game.informer -= 1
                if Card.rogue in cards:
                    game.rogue += 1
                    self.run(game)
                    game.rogue -= 1
                if Card.florahedron in cards:
                    game.florahedron += 1
                    self.run(game)
                    game.florahedron -= 1

                game.threshold -= 1
                game.G += 1
                game.commune += 1
                game.n_draws -= 5

            if game.grant >= 1 and game.forest == 0 and game.played_forest == 0 and game.granted == 0:
                game.grant -= 1
                game.granted += 1
                game.threshold -= 1
                game.forest += 1
                pos = game.draws[game.n_draws:].index(Card.forest)
                game.draws[game.n_draws:].pop(pos)
                self.run(game)
                game.draws[game.n_draws:].insert(pos, Card.forest)
                game.forest -= 1
                game.threshold += 1
                game.granted -= 1
                game.grant += 1

            if game.guard >= 1 and game.spy == 0 and game.B >= 2 and (game.B + game.R + game.G) >= 3:
                game.guard -= 1
                game.creatures_graveyard += 1
                game.threshold += 1
                game.B -= 2
                if game.B >= 1:
                    game.B -= 1
                    game.spy += 1
                    pos = game.draws[game.n_draws:].index(Card.spy)
                    game.draws[game.n_draws:].pop(pos)
                    self.run(game)
                    game.draws[game.n_draws:].insert(pos, Card.spy)
                    game.spy -= 1
                    game.B += 1
                if game.G >= 1:
                    game.G -= 1
                    game.spy += 1
                    pos = game.draws[game.n_draws:].index(Card.spy)
                    game.draws[game.n_draws:].pop(pos)
                    self.run(game)
                    game.draws[game.n_draws:].insert(pos, Card.spy)
                    game.spy -= 1
                    game.G += 1
                if game.R >= 1:
                    game.R -= 1
                    game.spy += 1
                    pos = game.draws[game.n_draws:].index(Card.spy)
                    game.draws[game.n_draws:].pop(pos)
                    self.run(game)
                    game.draws[game.n_draws:].insert(pos, Card.spy)
                    game.spy -= 1
                    game.R += 1
                game.B += 2
                game.threshold -= 1
                game.creatures_graveyard -= 1
                game.guard += 1

            if game.star >= 1 and (game.B + game.G + game.R) >= 2:
                card = game.draws[game.n_draws]
                game.add_card(card, 1)
                game.n_draws += 1
                game.star -= 1
                game.threshold += 1
                if game.R >= 2:
                    for (b, r, g) in ((0, -1, 0), (1, -2, 0), (0, -2, 1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                if game.B >= 2:
                    for (b, r, g) in ((-1, 0, 0), (-2, 1, 0), (-2, 0, 1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                if game.G >= 2:
                    for (b, r, g) in ((0, 0, -1), (1, 0, -2), (0, 1, -2)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                if game.B >= 1 and game.R >= 1:
                    for (b, r, g) in ((-1, 0, 0), (0, -1, 0), (-1, -1, 1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                if game.B >= 1 and game.G >= 1:
                    for (b, r, g) in ((-1, 0, 0), (0, 0, -1), (-1, 1, -1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                if game.G >= 1 and game.R >= 1:
                    for (b, r, g) in ((0, 0, -1), (0, -1, 0), (1, -1, -1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                game.threshold -= 1
                game.star += 1
                game.n_draws -= 1
                game.add_card(card, -1)
            if game.manamorphose >= 1 and (game.R + game.G) >= 1 and (game.B + game.R + game.G) >= 2:
                card = game.draws[game.n_draws]
                game.add_card(card, 1)
                game.n_draws += 1
                game.manamorphose -= 1
                game.threshold += 1
                self.run(game)
                if game.R >= 2:
                    game.R -= 2
                    for (b, r, g) in ((2, 0, 0), (0, 0, 2), (1, 1, 0), (1, 0, 1), (0, 1, 1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                    game.R += 2
                if game.G >= 2:
                    game.G -= 2
                    for (b, r, g) in ((2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                    game.G += 2
                if game.B >= 1 and game.G >= 1 and game.R >= 1:
                    game.B -= 1
                    game.R -= 1
                    game.G -= 1
                    for (b, r, g) in ((3, 0, 0), (0, 0, 3), (2, 1, 0), (2, 0, 1), (1, 0, 2), (0, 1, 2)):
                        game.B += b
                        game.R += r
                        game.G += g
                        self.run(game)
                        game.G -= g
                        game.R -= r
                        game.B -= b
                else:
                    if game.B >= 1 and game.G >= 1:
                        game.B -= 1
                        game.G -= 1
                        for (b, r, g) in ((2, 0, 0), (0, 0, 2), (1, 1, 0), (1, 0, 1)):
                            game.B += b
                            game.R += r
                            game.G += g
                            self.run(game)
                            game.G -= g
                            game.R -= r
                            game.B -= b
                        game.G += 1
                        game.B += 1
                    elif game.B >= 1 and game.R >= 1:
                        game.B -= 1
                        game.R -= 1
                        for (b, r, g) in ((2, 0, 0), (0, 0, 2), (1, 0, 1), (0, 1, 1)):
                            game.B += b
                            game.R += r
                            game.G += g
                            self.run(game)
                            game.G -= g
                            game.R -= r
                            game.B -= b
                        game.R += 1
                        game.B += 1
                    elif game.G >= 1 and game.R >= 1:
                        game.G -= 1
                        game.R -= 1
                        for (b, r, g) in ((2, 0, 0), (0, 0, 2), (1, 1, 0), (0, 1, 1)):
                            game.B += b
                            game.R += r
                            game.G += g
                            self.run(game)
                            game.G -= g
                            game.R -= r
                            game.B -= b
                        game.R += 1
                        game.G += 1
                game.threshold -= 1
                game.manamorphose += 1
                game.n_draws -= 1
                game.add_card(card, -1)
            if game.stinger >= 1 and (game.G + game.R + game.B) >= 1:
                game.stinger -= 1
                game.threshold += 1
                game.creatures_graveyard += 1
                card = game.draws[game.n_draws]
                game.add_card(card, 1)
                game.n_draws += 1
                if game.G >= 1:
                    game.G -= 1
                    self.run(game)
                    game.G += 1
                if game.B >= 1:
                    game.B -= 1
                    self.run(game)
                    game.B += 1
                if game.R >= 1:
                    game.R -= 1
                    self.run(game)
                    game.R += 1
                game.n_draws -= 1
                game.add_card(card, -1)
                game.creatures_graveyard -= 1
                game.threshold -= 1
                game.stinger += 1
            if game.bauble >= 1 and (game.G + game.R + game.B) >= 1:
                game.bauble -= 1
                game.threshold += 1
                card = game.draws[game.n_draws]
                game.add_card(card, 1)
                game.n_draws += 1
                if game.G >= 1:
                    game.G -= 1
                    self.run(game)
                    game.G += 1
                if game.B >= 1:
                    game.B -= 1
                    self.run(game)
                    game.B += 1
                if game.R >= 1:
                    game.R -= 1
                    self.run(game)
                    game.R += 1
                game.n_draws -= 1
                game.add_card(card, -1)
                game.threshold -= 1
                game.bauble += 1

        if game.nb_cards >= 2:
            game.nb_cards -= 1
            if game.forest >= 1:
                game.forest -= 1
                game.played_forest += 1
                game.G += 1
                self.run(game)
                game.G -= 1
                game.played_forest -= 1
                game.forest += 1
                
                game.nb_cards += 1
                return game.best_turn
            if game.elvish >= 1:
                game.elvish -= 1
                game.G += 1
                self.run(game)
                game.G -= 1
                game.elvish += 1
                
                game.nb_cards += 1
                return game.best_turn
            if game.rogue >= 1:
                game.rogue -= 1
                game.B += 1
                game.turn += 1
                self.run(game)
                game.turn -= 1
                game.B -= 1
                game.rogue += 1
            if game.florahedron >= 1:
                game.florahedron -= 1
                game.G += 1
                game.turn += 1
                self.run(game)
                game.turn -= 1
                game.G -= 1
                game.florahedron += 1

            if game.petal >= 1:
                game.petal -= 1
                game.threshold += 1
                game.G += 1
                self.run(game)
                game.G -= 1
                game.R += 1
                self.run(game)
                game.R -= 1
                game.B += 1
                self.run(game)
                game.B -= 1
                game.threshold -= 1
                game.petal += 1

                game.nb_cards += 1
                return game.best_turn
            if game.simian >= 1:
                game.simian -= 1
                game.R += 1
                self.run(game)
                game.R -= 1
                game.simian += 1

                game.nb_cards += 1
                return game.best_turn
            
            if game.dark >= 1 and game.B >= 1:
                game.dark -= 1
                game.B += 2
                game.threshold += 1
                self.run(game)
                game.threshold -= 1
                game.B -= 2
                game.dark += 1

                game.nb_cards += 1
                return game.best_turn
            if game.culling >= 1 and game.B >= 1 and game.creatures >= 1:
                game.culling -= 1
                game.B += 3
                game.threshold += 2
                game.creatures -= 1
                game.creatures_graveyard += 1
                self.run(game)
                game.creatures_graveyard -= 1
                game.creatures += 1
                game.threshold -= 2
                game.B -= 3
                game.culling += 1
            if game.plunge >= 1 and game.R >= 1 and game.creatures >= 1:
                game.plunge -= 1
                game.R += 2
                game.threshold += 2
                game.creatures -= 1
                game.creatures_graveyard += 1
                self.run(game)
                game.creatures_graveyard -= 1
                game.creatures += 1
                game.threshold -= 2
                game.R -= 2
                game.plunge += 1
            if game.desperate >= 1 and game.R >= 1 and (game.B + game.R + game.G) >= 2:
                game.desperate -= 1
                game.threshold += 1
                if game.R >= 2:
                    game.R += 1
                    self.run(game)
                    game.R -= 1
                if game.G >= 1:
                    game.R += 2
                    game.G -= 1
                    self.run(game)
                    game.G += 1
                    game.R -= 2
                if game.B >= 1:
                    game.R += 2
                    game.B -= 1
                    self.run(game)
                    game.B += 1
                    game.R -= 2
                game.threshold -= 1
                game.desperate += 1
            if game.cabal >= 1 and game.B >= 1 and (game.B + game.R + game.G) >= 2:
                game.cabal -= 1
                game.threshold += 1
                if game.threshold >= 8:
                    game.B += 2
                if game.B >= 2:
                    game.B += 1
                    self.run(game)
                    game.B -= 1
                if game.G >= 1:
                    game.B += 2
                    game.G -= 1
                    self.run(game)
                    game.G += 1
                    game.B -= 2
                if game.R >= 1:
                    game.B += 2
                    game.R -= 1
                    self.run(game)
                    game.R += 1
                    game.B -= 2
                if game.threshold >= 8:
                    game.B -= 2
                game.threshold -= 1
                game.cabal += 1
            if game.songs >= 1 and game.B >= 1 and game.creatures_graveyard >= 2:
                game.songs -= 1
                game.B += game.creatures_graveyard - 1
                game.threshold += 1
                self.run(game)
                game.threshold -= 1
                game.B -= game.creatures_graveyard - 1
                game.songs += 1
            if game.rite >= 1 and game.R >= 1:
                game.rite -= 1
                game.R += game.rites_graveyard + 1
                game.rites_graveyard += 1
                game.threshold += 1
                self.run(game)
                game.threshold -= 1
                game.rites_graveyard -= 1
                game.R -= game.rites_graveyard + 1
                game.rite += 1

                game.nb_cards += 1
                return game.best_turn

            if game.drum >= 1 and (game.B + game.R + game.G) >= 1:
                game.drum -= 1
                game.drummable += 1
                if game.B >= 1:
                    game.B -= 1
                    self.run(game)
                    game.B += 1
                if game.R >= 1:
                    game.R -= 1
                    self.run(game)
                    game.R += 1
                if game.G >= 1:
                    game.G -= 1
                    self.run(game)
                    game.G += 1
                game.drummable -= 1
                game.drum += 1

            if game.sphere >= 1:
                game.sphere -= 1
                game.creatures += 1
                if game.drummable >= 1:
                    self.drumming(game)

                self.run(game)
                game.creatures -= 1
                game.sphere += 1

            if game.looting >= 1 and game.R >= 1:
                game.looting -= 1
                game.R -= 1
                game.threshold += 3
                card = game.draws[game.n_draws]
                game.add_card(card, 1)
                game.n_draws += 1
                card2 = game.draws[game.n_draws]
                game.add_card(card2, 1)
                game.n_draws += 1
                old_lotleth = game.lotleth
                old_dread = game.dread
                old_dregscape = game.dregscape
                game.lotleth = 0
                game.dread = 0
                game.dregscape = max(0, old_lotleth + old_dread + old_dregscape - 2)
                self.run(game)
                game.dregscape = old_dregscape
                game.dread = old_dread
                game.lotleth = old_lotleth
                game.n_draws -= 2
                game.add_card(card2, -1)
                game.add_card(card, -1)
                game.threshold -= 3
                game.R += 1
                game.looting += 1
            if game.stinger >= 1 and game.R >= 1 and (game.B + game.R + game.G) >= 2:
                game.stinger -= 1
                game.R -= 1
                game.creatures += 1
                if game.R >= 1:
                    game.R -= 1
                    if game.drummable >= 1:
                        self.drumming(game)
                    self.run(game)
                    game.R += 1
                if game.G >= 1:
                    game.G -= 1
                    if game.drummable >= 1:
                        self.drumming(game)
                    self.run(game)
                    game.G += 1
                if game.B >= 1:
                    game.B -= 1
                    if game.drummable >= 1:
                        self.drumming(game)
                    self.run(game)
                    game.B += 1
                game.creatures -= 1
                game.R += 1
                game.stinger += 1

            if game.tinder >= 1 and game.G >= 1:
                game.tinder -= 1
                game.G -= 1 
                game.creatures += 1
                if game.drummable >= 1:
                    self.drumming(game)
                self.run(game)
                game.creatures -= 1
                
                game.threshold += 1
                game.creatures_graveyard += 1
                game.R += 2
                self.run(game)
                game.R -= 2
                game.creatures_graveyard -= 1
                game.threshold -= 1
                game.G += 1
                game.tinder += 1
            if game.cantor >= 1:
                game.cantor -= 1
                if game.R >= 1:
                    game.R -= 1

                    game.creatures += 1
                    if game.drummable >= 1:
                        self.drumming(game)
                    self.run(game)
                    game.creatures -= 1
                    
                    game.threshold += 1
                    game.creatures_graveyard += 1
                    game.B += 1
                    self.run(game)
                    game.B -= 1
                    game.R += 1
                    self.run(game)
                    game.R -= 1
                    game.G += 1
                    self.run(game)
                    game.G -= 1
                    game.creatures_graveyard -= 1
                    game.threshold -= 1 
                    game.R += 1
                if game.G >= 1:
                    game.G -= 1
                    game.creatures += 1
                    if game.drummable >= 1:
                        self.drumming(game)
                    self.run(game)
                    game.creatures -= 1
                    
                    game.threshold += 1
                    game.creatures_graveyard += 1
                    game.B += 1
                    self.run(game)
                    game.B -= 1
                    game.R += 1
                    self.run(game)
                    game.R -= 1
                    game.G += 1
                    self.run(game)
                    game.G -= 1
                    game.creatures_graveyard -= 1
                    game.threshold -= 1
                    game.G += 1
                game.cantor += 1
            game.nb_cards += 1

        if game.nb_cards >= 1 and game.played_forest >= 1:
            if game.spy >= 1:
                game.creatures += 1
            if (game.spy + game.informer) >= 1 and game.B >= 1 and (game.G + game.R + game.B) >= 4:
                mana_C = game.G + game.R - 3
                mana_B = game.B - 1
                if mana_C < 0:
                    mana_B += mana_C
                    mana_C = 0

                """if game.informer >= 1:
                    game.creatures_graveyard += 1
                if game.songs >= 1 and mana_B >= 1:
                    game.best_turn = game.turn
                elif game.bauble >= 1 and mana_B >= 1 and mana_B + mana_C >= 2:
                    game.best_turn = game.turn

                if game.informer >= 1:
                    game.creatures_graveyard -= 1"""
                
                if game.lotleth >= 1:
                    if mana_B >= 1 and mana_B + mana_C >= 7:
                        game.best_turn = game.turn
                else:
                    if game.dread >= 1 and mana_B >= 2 and mana_B + mana_C >= 4:
                        mana_B -= 2
                        mana_C -= 2
                        if mana_C < 0:
                            mana_B += mana_C
                            mana_C = 0
                    if mana_B >= 1 and mana_B + mana_C >= 1 + game.dregscape:
                        game.creatures += 1
                    if (game.creatures + 2 - game.narcomoeba) >= 3:
                        game.best_turn = game.turn
                    if mana_B >= 1 and mana_B + mana_C >= 1 + game.dregscape:
                        game.creatures -= 1
            if game.spy >= 1:
                game.creatures -= 1

        return game.best_turn

    def to_remove(self, game, nb_mulls, nb_removed = 0):
        if nb_removed >= nb_mulls:
            # Modify to play OTD
            # game.add_card(game.draws[-3])
            # game.nb_cards += 1
            self.run(game)
            # game.nb_cards -= 1
            # game.add_card(game.draws[-3], -1)
        elif game.lotleth >= 1 or game.dread >= 1 or game.narcomoeba >= 1 or game.dregscape >= 1:
            if game.lotleth >= 1:
                game.lotleth -= 1
                self.to_remove(game, nb_mulls, nb_removed + 1)
                game.lotleth += 1
            elif game.dread >= 1:
                game.dread -= 1
                self.to_remove(game, nb_mulls, nb_removed + 1)
                game.dread += 1
            if game.narcomoeba >= 1:
                game.narcomoeba -= 1
                self.to_remove(game, nb_mulls, nb_removed + 1)
                game.narcomoeba += 1
            elif game.dregscape >= 1:
                game.dregscape -= 1
                self.to_remove(game, nb_mulls, nb_removed + 1)
                game.dregscape += 1
        else:
            self.to_remove(game, nb_mulls, nb_removed + 1)
        return game.best_turn

    def main_run(self, game, nb_mulls = 0):        
        while game.wraith >= 1:
            game.wraith -= 1
            game.threshold += 1
            game.creatures_graveyard += 1
            card = game.draws[game.n_draws]
            game.n_draws += 1
            game.add_card(card)

        self.to_remove(game, nb_mulls)
        #print(game.__dict__)
        if nb_mulls < 4 and game.best_turn == 99:
            game = deck.get_hand()
            nb_mulls += 1
            game.nb_cards = 7 - nb_mulls # Modify maximum hand size here
            return self.main_run(game, nb_mulls)

        #print(game.best_turn, nb_mulls)
        return game.best_turn, nb_mulls

deck = Deck()

total_t1 = [0, 0, 0, 0, 0]
total_t2 = [0, 0, 0, 0, 0]
total_t3 = [0, 0, 0, 0, 0]
for i in range(10000):
    game = deck.get_hand()
    nb_turns, nb_mulls = deck.main_run(game, 0)
    if nb_turns == 1:
        total_t1[nb_mulls] += 1
    elif nb_turns == 2:
        total_t2[nb_mulls] += 1
    elif nb_turns == 3:
        total_t3[nb_mulls] += 1

print("T1: ", [round(el / 100) / 100 for el in total_t1], round(sum(total_t1) / 100) / 100)
print("T2: ", [round(el / 100) / 100 for el in total_t2], round(sum(total_t2) / 100) / 100)
print("Other: ", round((10000 - (sum(total_t1) + sum(total_t2) + sum(total_t3))) / 100) / 100)
