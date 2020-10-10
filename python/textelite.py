from typing import List
from dataclasses import dataclass
import random
from math import sqrt


@dataclass
class TradeGood:
    baseprice: int
    gradient: int
    basequant: int
    maskbyte: int
    units: int
    name: str


commodities = [
    TradeGood(0x13, -0x02, 0x06, 0x01, 0, "Food"),
    TradeGood(0x14, -0x01, 0x0A, 0x03, 0, "Textiles"),
    TradeGood(0x41, -0x03, 0x02, 0x07, 0, "Radioactives"),
    TradeGood(0x28, -0x05, 0xE2, 0x1F, 0, "Slaves"),
    TradeGood(0x53, -0x05, 0xFB, 0x0F, 0, "Liquor/Wines"),
    TradeGood(0xC4, +0x08, 0x36, 0x03, 0, "Luxuries"),
    TradeGood(0xEB, +0x1D, 0x08, 0x78, 0, "Narcotics"),
    TradeGood(0x9A, +0x0E, 0x38, 0x03, 0, "Computers"),
    TradeGood(0x75, +0x06, 0x28, 0x07, 0, "Machinery"),
    TradeGood(0x4E, +0x01, 0x11, 0x1F, 0, "Alloys"),
    TradeGood(0x7C, +0x0d, 0x1D, 0x07, 0, "Firearms"),
    TradeGood(0xB0, -0x09, 0xDC, 0x3F, 0, "Furs"),
    TradeGood(0x20, -0x01, 0x35, 0x03, 0, "Minerals"),
    TradeGood(0x61, -0x01, 0x42, 0x07, 1, "Gold"),
    TradeGood(0xAB, -0x02, 0x37, 0x1F, 1, "Platinum"),
    TradeGood(0x2D, -0x01, 0xFA, 0x0F, 2, "Gem-Stones"),
    TradeGood(0x35, +0x0F, 0xC0, 0x07, 0, "Alien Items")
]

unitnames = ("t", "kg", "g")
govnames = ("Anarchy", "Feudal", "Multi-gov", "Dictatorship", "Communist", "Confederacy", "Democracy", "Corporate State")
econnames = ("Rich Industrial", "Average Industrial", "Poor Industrial", "Mainly Industrial",
             "Mainly Agricultural", "Rich Agricultural", "Average Agricultural", "Poor Agricultural")


class Market:
    def __init__(self):
        self.quantity = [0 for _ in commodities]
        self.price = [0 for _ in commodities]

    def display(self, cargohold: List[int]) -> None:
        for i in range(len(commodities)):
            print(commodities[i].name.ljust(20), end="")
            print("  %.1f" % (self.price[i] / 10.0), end="")
            print("  ", self.quantity[i], end="")
            print(unitnames[commodities[i].units], end="")
            print("  ", cargohold[i], end="")
            print()


class Planet:
    desc_list = [
        ("fabled", "notable", "well known", "famous", "noted"),
        ("very", "mildly", "most", "reasonably", ""),
        ("ancient", "\x95", "great", "vast", "pink"),
        ("\x9E \x9D plantations", "mountains", "\x9C", "\x94 forests", "oceans"),
        ("shyness", "silliness", "mating traditions", "loathing of \x86", "love for \x86"),
        ("food blenders", "tourists", "poetry", "discos", "\x8E"),
        ("talking tree", "crab", "bat", "lobst", "\xB2"),
        ("beset", "plagued", "ravaged", "cursed", "scourged"),
        ("\x96 civil war", "\x9B \x98 \x99s", "a \x9B disease", "\x96 earthquakes", "\x96 solar activity"),
        ("its \x83 \x84", "the \xB1 \x98 \x99", "its inhabitants' \x9A \x85", "\xA1", "its \x8D \x8E"),
        ("juice", "brandy", "water", "brew", "gargle blasters"),
        ("\xB2", "\xB1 \x99", "\xB1 \xB2", "\xB1 \x9B", "\x9B \xB2"),
        ("fabulous", "exotic", "hoopy", "unusual", "exciting"),
        ("cuisine", "night life", "casinos", "sit coms", " \xA1 "),
        ("\xB0", "The planet \xB0", "The world \xB0", "This planet", "This world"),
        ("n unremarkable", " boring", " dull", " tedious", " revolting"),
        ("planet", "world", "place", "little planet", "dump"),
        ("wasp", "moth", "grub", "ant", "\xB2"),
        ("poet", "arts graduate", "yak", "snail", "slug"),
        ("tropical", "dense", "rain", "impenetrable", "exuberant"),
        ("funny", "wierd", "unusual", "strange", "peculiar"),
        ("frequent", "occasional", "unpredictable", "dreadful", "deadly"),
        ("\x82 \x81 for \x8A", "\x82 \x81 for \x8A and \x8A", "\x88 by \x89", "\x82 \x81 for \x8A but \x88 by \x89", "a\x90 \x91"),
        ("\x9B", "mountain", "edible", "tree", "spotted"),
        ("\x9F", "\xA0", "\x87oid", "\x93", "\x92"),
        ("ancient", "exceptional", "eccentric", "ingrained", "\x95"),
        ("killer", "deadly", "evil", "lethal", "vicious"),
        ("parking meters", "dust clouds", "ice bergs", "rock formations", "volcanoes"),
        ("plant", "tulip", "banana", "corn", "\xB2weed"),
        ("\xB2", "\xB1 \xB2", "\xB1 \x9B", "inhabitant", "\xB1 \xB2"),
        ("shrew", "beast", "bison", "snake", "wolf"),
        ("leopard", "cat", "monkey", "goat", "fish"),
        ("\x8C \x8B", "\xB1 \x9F \xA2", "its \x8D \xA0 \xA2", "\xA3 \xA4", "\x8C \x8B"),
        ("meat", "cutlet", "steak", "burgers", "soup"),
        ("ice", "mud", "Zero-G", "vacuum", "\xB1 ultra"),
        ("hockey", "cricket", "karate", "polo", "tennis")
    ]
    # pairs0 = "ABOUSEITILETSTONLONUTHNOALLEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"
    pairs0 = "ABOUSEITILETSTONLONUTHNOALLEXEGEZACEBISOUSESARMAINDIREA.ERATENBE"

    def __init__(self):
        self.x = 0
        self.y = 0
        self.economy = 0
        self.govtype = 0
        self.techlev = 0
        self.population = 0
        self.productivity = 0
        self.radius = 0
        self.goatsoup_seed = (0, 0, 0, 0)
        self.goatsoup_rnd = [0, 0, 0, 0]
        self.name = ""
        # TODO: species, read below:
        """
  Species type
  ------------
  The species type is either Human Colonials, or it's an alien species that
  consists of up to three adjectives and a species name (so you can get
  anything from "Rodents" and "Fierce Frogs" to "Black Fat Felines" and "Small
  Yellow Bony Lobsters").
  
  As with the rest of the system data, the species is built from various bits
  in the seeds. Specifically, all the bits in w2_hi are used, along with bits
  0-2 of w0_hi and w1_hi, and bit 7 of w2_lo.
  
  First, we check bit 7 of w2_lo. If it is clear, print "Human Colonials" and
  stop, otherwise this is an alien species, so we move onto the following
  steps. (In the following steps, the potential range of the calculated value
  of A is 0-7, and if a match isn't made, nothing is printed for that step.)
  
    1. Set A = bits 2-4 of w2_hi
  
      * If A = 0,  print "Large "
      * If A = 1,  print "Fierce "
      * If A = 2,  print "Small "
  
    2. Set A = bits 5-7 of w2_hi
  
      * If A = 0,  print "Green "
      * If A = 1,  print "Red "
      * If A = 2,  print "Yellow "
      * If A = 3,  print "Blue "
      * If A = 4,  print "Black "
      * If A = 5,  print "Harmless "
  
    3. Set A = bits 0-2 of (w0_hi EOR w1_hi)
  
      * If A = 0,  print "Slimy "
      * If A = 1,  print "Bug-Eyed "
      * If A = 2,  print "Horned "
      * If A = 3,  print "Bony "
      * If A = 4,  print "Fat "
      * If A = 5,  print "Furry "
  
    4. Add bits 0-1 of w2_hi to A from step 3, and take bits 0-2 of the result
  
      * If A = 0,  print "Rodents"
      * If A = 1,  print "Frogs"
      * If A = 2,  print "Lizards"
      * If A = 3,  print "Lobsters"
      * If A = 4,  print "Birds"
      * If A = 5,  print "Humanoids"
      * If A = 6,  print "Felines"
      * If A = 7,  print "Insects"
  
  So if we print an adjective at step 3, then the only options for the species
  name are from A to A + 3 (because we add a 2-bit number) in step 4. So only
  certain combinations are possible:
  
    * Only rodents, frogs, lizards and lobsters can be slimy
    * Only frogs, lizards, lobsters and birds can be bug-eyed
    * Only lizards, lobsters, birds and humanoids can be horned
    * Only lobsters, birds, humanoids and felines can be bony
    * Only birds, humanoids, felines and insects can be fat
    * Only humanoids, felines, insects and rodents can be furry
  
  So however hard you look, you will never find slimy humanoids, bony insects,
  fat rodents or furry frogs, which is probably for the best.
        """

    def gen_rnd_number(self) -> int:
        x: int = (self.goatsoup_rnd[0] * 2) & 0xFF
        a: int = x + self.goatsoup_rnd[2]
        if self.goatsoup_rnd[0] > 127:
            a += 1
        self.goatsoup_rnd[0] = a & 0xFF
        self.goatsoup_rnd[2] = x
        a //= 256  # a = any carry left from above
        x = self.goatsoup_rnd[1]
        a = (a + x + self.goatsoup_rnd[3]) & 0xFF
        self.goatsoup_rnd[1] = a
        self.goatsoup_rnd[3] = x
        return a

    def goat_soup(self) -> str:
        result = ""
        self.goatsoup_rnd = list(self.goatsoup_seed)

        def soup(source: str) -> None:
            nonlocal result
            for c in source:
                if c == '\x00':
                    break
                elif c <= '\x80':
                    result += c
                else:
                    if c <= '\xa4':
                        rnd = self.gen_rnd_number()
                        soup(self.desc_list[ord(c) - 0x81][(rnd >= 0x33) + (rnd >= 0x66) + (rnd >= 0x99) + (rnd >= 0xCC)])
                    else:
                        if c == '\xb0':
                            # planet name
                            result += self.name.title()
                        elif c == '\xb1':
                            # planet name + ian
                            name = self.name.title()
                            result += name[0]
                            for nn in name[1:]:
                                if nn in ('e', 'i', '\0'):
                                    break
                                result += nn
                            result += "ian"
                        elif c == '\xb2':
                            result += self.random_name()
                        else:
                            raise ValueError("bad char data", c)

        soup("\x8F is \x97.")
        return result

    def random_name(self) -> str:
        name = ""
        length = self.gen_rnd_number() & 3
        for i in range(length + 1):
            x = self.gen_rnd_number() & 0x3e
            if self.pairs0[x] != '.':
                if i == 0:
                    name += self.pairs0[x]
                else:
                    name += self.pairs0[x].lower()
            if self.pairs0[x+1] != '.':
                name += self.pairs0[x + 1].lower()
        return name

    def display(self, compressed: bool = False) -> None:
        if compressed:
            print(self.name, " TL:", self.techlev + 1, " ", econnames[self.economy], " ", govnames[self.govtype], end="")
        else:
            print("\nSystem: ", self.name)
            print("Position: ", self.x, ",", self.y)
            print("Economy:", self.economy, econnames[self.economy])
            print("Government:", self.govtype, govnames[self.govtype])
            print("Tech Level:", self.techlev + 1)
            print("Turnover:", self.productivity)
            print("Radius:", self.radius)
            print("Population: %d Billion" % (self.population >> 3))
            print(self.goat_soup())


class Galaxy:
    GALSIZE = 256
    galaxy: List[Planet]
    base0 = 0x5A4A
    base1 = 0x0248
    base2 = 0xB753  # Base seed for galaxy 1
    pairs = "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"
    numforLave = 7  # Lave is 7th generated planet in galaxy one
    numforZaonce = 129
    numforDiso = 147
    numforRied = 46

    def __init__(self, galaxynum: int, createAllPlanets: bool = True) -> None:
        # init seed for galaxy 1
        self.number = galaxynum
        self.seed = [self.base0, self.base1, self.base2]
        for galcount in range(galaxynum - 1):
            self.nextgalaxy()
        if createAllPlanets:
            # Put galaxy data into array of structures
            self.galaxy = [self.makesystem() for _ in range(Galaxy.GALSIZE)]
        else:
            self.galaxy = []

    def nextgalaxy(self) -> None:
        # Apply to base seed; once for galaxy 2
        # twice for galaxy 3, etc.
        # Eighth application gives galaxy 1 again
        self.seed[0] = self.twist(self.seed[0])
        self.seed[1] = self.twist(self.seed[1])
        self.seed[2] = self.twist(self.seed[2])

    def twist(self, x: int) -> int:
        return (256 * self.rotatel(x >> 8)) + self.rotatel(x & 255)

    def rotatel(self, x: int) -> int:
        temp = x & 128
        return (2 * (x & 127)) + (temp >> 7)

    def makesystem(self) -> Planet:
        thissys = Planet()
        longnameflag = self.seed[0] & 64
        thissys.x = self.seed[1] >> 8
        thissys.y = self.seed[0] >> 8
        thissys.govtype = (self.seed[1] >> 3) & 7  # bits 3,4 &5 of w1
        thissys.economy = (self.seed[0] >> 8) & 7  # bits 8,9 &A of w0
        if thissys.govtype <= 1:
            thissys.economy = (thissys.economy | 2)
        thissys.techlev = ((self.seed[1] >> 8) & 3) + (thissys.economy ^ 7)
        thissys.techlev += thissys.govtype >> 1
        if (thissys.govtype & 1) == 1:
            thissys.techlev += 1
        thissys.population = 4 * thissys.techlev + thissys.economy
        thissys.population += thissys.govtype + 1
        thissys.productivity = ((thissys.economy ^ 7) + 3) * (thissys.govtype + 4)
        thissys.productivity *= thissys.population * 8
        thissys.radius = 256 * (((self.seed[2] >> 8) & 15) + 11) + thissys.x
        thissys.goatsoup_seed = (self.seed[1] & 0xFF,
                                 self.seed[1] >> 8,
                                 self.seed[2] & 0xFF,
                                 self.seed[2] >> 8)

        # Always four iterations of random number
        pair1 = 2 * ((self.seed[2] >> 8) & 31)
        self.tweakseed()
        pair2 = 2 * ((self.seed[2] >> 8) & 31)
        self.tweakseed()
        pair3 = 2 * ((self.seed[2] >> 8) & 31)
        self.tweakseed()
        pair4 = 2 * ((self.seed[2] >> 8) & 31)
        self.tweakseed()

        namechars = [self.pairs[pair1],
                     self.pairs[pair1 + 1],
                     self.pairs[pair2],
                     self.pairs[pair2 + 1],
                     self.pairs[pair3],
                     self.pairs[pair3 + 1]]
        if longnameflag:  # bit 6 of ORIGINAL w0 flags a four-pair name
            namechars.append(self.pairs[pair4])
            namechars.append(self.pairs[pair4 + 1])
        thissys.name = "".join(namechars).replace(".", "")
        return thissys

    def tweakseed(self) -> None:
        temp = (self.seed[0]) + (self.seed[1]) + (self.seed[2]) & 65535  # 2 byte aritmetic
        self.seed[0] = self.seed[1]
        self.seed[1] = self.seed[2]
        self.seed[2] = temp

    def genmarket(self, fluct: int, p: Planet) -> Market:
        # Prices and availabilities are influenced by the planet's economy type
        # (0-7) and a random "fluctuation" byte that was kept within the saved
        # commander position to keep the market prices constant over gamesaves.
        # Availabilities must be saved with the game since the player alters them
        # by buying (and selling(?))
        #
        # Almost all operations are one byte only and overflow "errors" are
        # extremely frequent and exploited.
        #
        # Trade Item prices are held internally in a single byte=true value/4.
        # The decimal point in prices is introduced only when printing them.
        # Internally, all prices are integers.
        # The player's cash is held in four bytes.
        market = Market()
        for i in range(len(commodities)):
            product = p.economy * commodities[i].gradient
            changing = fluct & commodities[i].maskbyte
            q = commodities[i].basequant + changing - product
            q &= 0xff
            if q & 0x80:
                q = 0  # clip to positive 8-bit
            market.quantity[i] = q & 0x3f
            q = commodities[i].baseprice + changing + product
            q &= 0xff
            market.price[i] = q * 4
        for idx, c in enumerate(commodities):
            if c.name == "Alien Items":
                market.quantity[idx] = 0  # force nonavailibility
        return market

    def matchsys(self, name: str, currentplanet: int) -> int:
        pnum = currentplanet
        current = self.galaxy[currentplanet]
        if name:
            d = 9999
            for idx, planet in enumerate(self.galaxy):
                if planet.name.lower().startswith(name.lower()):
                    if self.distance(planet, current) < d:
                        d = self.distance(planet, current)
                        pnum = idx
        return pnum

    def distance(self, a: Planet, b: Planet) -> int:
        # separation between two planets
        return int(0.5 + 4.0 * sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) / 4.0))


class Trader:
    tradnames = [c.name for c in commodities]
    fuelcost = 2  # 0.2 CR/Light year
    maxfuel = 70  # 7.0 LY tank

    def __init__(self):
        random.seed(12345)
        self.galax = Galaxy(1)
        self.currentplanet = Galaxy.numforLave
        self.localmarket = self.galax.genmarket(0x00, self.galax.galaxy[Galaxy.numforLave])
        self.fuel = Trader.maxfuel
        self.cash = 0.0
        self.shipshold = [0 for _ in commodities]
        self.holdspace = 0

    def randbyte(self) -> int:
        return random.randint(0, 255)

    def parser(self, command: str) -> None:
        cmd, _, arg = command.partition(" ")
        funcs = {
            "buy": self.do_buy,
            "sell": self.do_sell,
            "fuel": self.do_fuel,
            "jump": self.do_jump,
            "sneak": self.do_sneak,
            "galhyp": self.do_galhyp,
            "info": self.do_info,
            "mkt": self.do_mkt,
            "local": self.do_local,
            "cash": self.do_cash,
            "hold": self.do_hold,
            "quit": self.do_quit,
            "help": self.do_help,
        }
        for fname, func in funcs.items():
            if fname.startswith(cmd):
                func(arg)
                break
        else:
            print("Bad command", cmd)

    def do_buy(self, what: str) -> None:
        goods, astr = what.split()
        amount = int(astr)
        if amount == 0:
            amount = 1
        i = self.stringmatch(goods, self.tradnames)
        if i <= 0:
            print("Unknown trade good")
        else:
            i -= 1
            t = self.gamebuy(i, amount)
            if t == 0:
                print("Can't buy any ", end="")
            else:
                print("Buying", t, unitnames[commodities[i].units], "of ", end="")
            print(self.tradnames[i])

    def do_sell(self, what: str) -> None:
        goods, astr = what.split()
        amount = int(astr)
        if amount == 0:
            amount = 1
        i = self.stringmatch(goods, self.tradnames)
        if i <= 0:
            print("Unknown trade good")
        else:
            i -= 1
            t = self.gamesell(i, amount)
            if t == 0:
                print("Can't sell any ", end="")
            else:
                print("Selling", t, unitnames[commodities[i].units], "of ", end="")
            print(self.tradnames[i])

    def do_fuel(self, amount: str) -> None:
        # buy an amount of fuel
        f = self.gamefuel(10*int(amount))
        if f == 0:
            print("Can't buy any fuel")
        else:
            print("Buying %.1f LY fuel" % (f/10.0))

    def do_jump(self, name: str) -> None:
        planetnum = self.galax.matchsys(name, self.currentplanet)
        if planetnum == self.currentplanet:
            print("Bad jump")
            return
        current = self.galax.galaxy[self.currentplanet]
        planet = self.galax.galaxy[planetnum]
        d = self.galax.distance(planet, current)
        if d > self.fuel:
            print("Jump too far")
            return
        self.fuel -= d
        self.currentplanet = planetnum
        self.localmarket = self.galax.genmarket(self.randbyte(), planet)
        planet.display(False)

    def do_sneak(self, name: str) -> None:
        fuelkeep = self.fuel
        self.fuel = 666
        self.do_jump(name)
        self.fuel = fuelkeep

    def do_galhyp(self, _):
        galnum = self.galax.number + 1
        if galnum == 9:
            galnum = 1
        self.galax = Galaxy(galnum)

    def do_local(self, _):
        current = self.galax.galaxy[self.currentplanet]
        print("Galaxy number", self.galax.number)
        for planet in self.galax.galaxy:
            d = self.galax.distance(planet, current)
            if d <= self.maxfuel:
                if d <= self.fuel:
                    print(" * ", end="")
                else:
                    print(" - ", end="")
                planet.display(True)
                print(" (%.1f LY)" % (d/10.0))

    def do_quit(self, _):
        raise SystemExit(0)

    def do_mkt(self, _) -> None:
        self.localmarket.display(self.shipshold)
        print("\nFuel: %.1f" % (self.fuel/10.0), "      Holdspace :", self.holdspace, "t", end="")

    def do_info(self, name: str) -> None:
        planetnum = self.galax.matchsys(name, self.currentplanet)
        self.galax.galaxy[planetnum].display(False)

    def do_hold(self, size: str) -> None:
        total = 0
        hsize = int(size)
        for i, c in enumerate(commodities):
            if c.units == 0:
                total += self.shipshold[i]
        if total > hsize:
            print("Hold too full")
        else:
            self.holdspace = hsize - total

    def do_cash(self, cash: str) -> None:
        self.cash += 10 * int(cash)  # cheat...

    def do_help(self, _) -> None:
        print("Commands are:")
        print("Buy   tradegood amount")
        print("Sell  tradegood amount")
        print("Fuel  amount    (buy amount LY of fuel)")
        print("Jump  planetname (limited by fuel)")
        print("Sneak planetname (any distance - no fuel cost)")
        print("Galhyp           (jumps to next galaxy)")
        print("Info  planetname (prints info on system")
        print("Mkt              (shows market prices)")
        print("Local            (lists systems within 7 light years)")
        print("Cash number      (alters cash - cheating!)")
        print("Hold number      (change cargo bay)")
        print("Quit or ^C       (exit)")
        print("Help             (display this text)")
        print("\nAbbreviations allowed eg. b fo 5 = Buy Food 5, m= Mkt")

    def gamefuel(self, f: int) -> int:
        if f+self.fuel > self.maxfuel:
            f = self.maxfuel-self.fuel
        if self.fuelcost > 0:
            if f*self.fuelcost > self.cash:
                f = int(self.cash/self.fuelcost)
        self.fuel += f
        self.cash -= self.fuelcost * f
        return f

    def mainloop(self) -> None:
        print("\nWelcome to Text Elite 1.5.")
        self.parser("hold 20")
        self.parser("cash +100")
        self.parser("help")
        while True:
            print("\nCash: %.1f" % (self.cash / 10.0))
            print("> ", flush=True, end="")
            getcommand = input()
            if len(getcommand) == 0:
                break
            self.parser(getcommand)

    def stringmatch(self, s: str, names: List[str]) -> int:
        for idx, name in enumerate(names):
            if name.lower().startswith(s.lower()):
                return idx+1
        return 0

    def gamebuy(self, i: int, a: int) -> int:
        # Try to buy amount a  of good i  Return amount bought
        # Cannot buy more than is availble, can afford, or will fit in hold
        if self.cash < 0:
            t = 0
        else:
            t = min(self.localmarket.quantity[i], a)
            if commodities[i].units == 0:
                t = min(self.holdspace, t)
            t = min(t, int(self.cash/self.localmarket.price[i]))
        self.shipshold[i] += t
        self.localmarket.quantity[i] -= t
        self.cash -= t*self.localmarket.price[i]
        if commodities[i].units == 0:
            self.holdspace -= t
        return t

    def gamesell(self, i: int, a: int) -> int:
        t = min(self.shipshold[i], a)
        self.shipshold[i] -= t
        self.localmarket.quantity[i] += t
        if commodities[i].units == 0:
            self.holdspace += t
        self.cash += t * self.localmarket.price[i]
        return t


def test():
    gx = Galaxy(1)
    assert gx.galaxy[Galaxy.numforLave].name == "LAVE"
    assert gx.galaxy[Galaxy.numforZaonce].name == "ZAONCE"
    assert gx.galaxy[Galaxy.numforRied].name == "RIEDQUAT"
    assert gx.galaxy[Galaxy.numforDiso].name == "DISO"
    lave = gx.galaxy[Galaxy.numforLave]
    market = gx.genmarket(0, lave)
    assert market.quantity[0] == 16
    assert market.price[0] == 36
    assert market.quantity[6] == 55
    assert market.price[6] == 496
    assert market.quantity[16] == 0
    assert market.price[16] == 512
    assert gx.galaxy[Galaxy.numforLave].goat_soup() == "Lave is most famous for its vast rain forests and the Lavian tree grub."
    assert gx.galaxy[Galaxy.numforZaonce].goat_soup() == "This planet is a tedious place."
    assert gx.galaxy[Galaxy.numforRied].goat_soup() == "This planet is most notable for its fabulous cuisine but beset by occasional civil war."
    assert gx.galaxy[Galaxy.numforDiso].goat_soup() == "This planet is mildly noted for its ancient Ma corn plantations but beset by frequent solar activity."
    t = Trader()
    assert t.galax.number == 1
    assert t.currentplanet == Galaxy.numforLave
    assert t.localmarket.quantity == market.quantity
    assert t.localmarket.price == market.price
    # p = Planet()
    # p.goatsoup_seed = (0x11, 0x22, 0x9e, 0xf1)
    # p.goatsoup_rnd = list(p.goatsoup_seed)
    # for i in range(20):
    #     print(p.random_name())


def testGG():
    gg = Galaxy(1, createAllPlanets=False)
    print("start!!!")
    print("seed0=", hex(gg.seed[0]))
    print("seed1=", hex(gg.seed[1]))
    print("seed2=", hex(gg.seed[2]))
    for i in range(Galaxy.numforLave+1):
        planet = gg.makesystem()
    print("seed0=", hex(gg.seed[0]))
    print("seed1=", hex(gg.seed[1]))
    print("seed2=", hex(gg.seed[2]))
    print("goatseed=", planet.goatsoup_seed)
    planet.display()


if __name__ == "__main__":
    # testGG()
    t = Trader()
    t.mainloop()
