from dataclasses import dataclass


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
    TradeGood(0x2D, -0x01, 0xFA, 0x0F, 2, "Gem-Strones"),
    TradeGood(0x35, +0x0F, 0xC0, 0x07, 0, "Alien Items")
]

AlienItems = len(commodities) - 1

unitnames = ("t", "kg", "g")

shipshold = [0 for _ in commodities]


class Market:
    def __init__(self):
        self.quantity = [0 for _ in commodities]
        self.price = [0 for _ in commodities]

    def display(self, cargohold) -> None:
        for i in range(len(commodities)):
            print(commodities[i].name.ljust(20), end="")
            print("  %.1f" % (self.price[i] / 10.0), end="")
            print("  ", self.quantity[i], end="")
            print(unitnames[commodities[i].units], end="")
            print("  ", cargohold[i], end="")
            print()


class PlanSys:
    x = 0
    y = 0
    economy = 0
    govtype = 0
    techlev = 0
    population = 0
    productivity = 0
    radius = 0
    goatsoupseed = (0, 0, 0, 0)
    name = ""


class PlanetDescriptions:
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
        ("\x82 \x81 for \x8A", "\x82 \x81 for \x8A and \x8A", "\x88 by \x89", "\x82 \x81 for \x8A but \x88 by \x89",
         "a\x90 \x91"),
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

    rnd_seed = [10, 20, 30, 40]  # todo proper init
    pairs0 = "ABOUSEITILETSTONLONUTHNOALLEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"

    def gen_rnd_number(self) -> int:
        x: int = (PlanetDescriptions.rnd_seed[0] * 2) & 0xFF
        a: int = x + PlanetDescriptions.rnd_seed[2]
        if PlanetDescriptions.rnd_seed[0] > 127:
            a += 1
        PlanetDescriptions.rnd_seed[0] = a & 0xFF
        PlanetDescriptions.rnd_seed[2] = x
        a //= 256  # a = any carry left from above
        x = PlanetDescriptions.rnd_seed[1]
        a = (a + x + PlanetDescriptions.rnd_seed[3]) & 0xFF
        PlanetDescriptions.rnd_seed[1] = a
        PlanetDescriptions.rnd_seed[3] = x
        return a

    def goat_soup(self, source: str, psy: PlanSys) -> None:
        for c in source:
            if c == '\x00':
                break
            elif c <= '\x80':
                print(c, end="")
            else:
                if c <= '\xa4':
                    rnd = self.gen_rnd_number()
                    self.goat_soup(
                        self.desc_list[ord(c) - 0x81][(rnd >= 0x33) + (rnd >= 0x66) + (rnd >= 0x99) + (rnd >= 0xCC)],
                        psy)
                else:
                    if c == '\xb0':
                        # planet name
                        print(psy.name.title(), end="")
                    elif c == '\xb1':
                        # planet name + ian
                        name = psy.name.title()
                        print(name[0], end="")
                        for nn in name[1:]:
                            if nn in ('E', 'I', '\0'):
                                break
                            print(nn, end="")
                        print("ian", end="")
                    elif c == '\xb2':
                        # random name
                        length = self.gen_rnd_number() & 3
                        for i in range(length + 1):
                            x = self.gen_rnd_number() & 0x3e
                            if i == 0:
                                print(self.pairs0[x], end="")
                            else:
                                print(self.pairs0[x].lower(), end="")
                            print(self.pairs0[x + 1].lower(), end="")
                    else:
                        raise ValueError("bad char data", c)


class Galaxy:
    GALSIZE = 256
    galaxy = []
    base0 = 0x5A4A
    base1 = 0x0248
    base2 = 0xB753  # Base seed for galaxy 1
    pairs = "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"

    def __init__(self, galaxynum: int):
        # init seed for galaxy 1
        self.seed = [self.base0, self.base1, self.base2]
        for galcount in range(galaxynum):
            self.nextgalaxy()
        # Put galaxy data into array of structures
        self.galaxy = []
        for syscount in range(Galaxy.GALSIZE):
            self.galaxy.append(self.makesystem())

    def nextgalaxy(self):
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

    def makesystem(self) -> PlanSys:
        thissys = PlanSys()
        longnameflag = self.seed[0] & 64
        thissys.x = self.seed[1] >> 8
        thissys.y = self.seed[0] >> 8
        thissys.govtype = (self.seed[1] >> 3) & 7  # bits 3,4 &5 of w1
        thissys.economy = (self.seed[0] >> 8) & 7  # bits 8,9 &A of w0
        if thissys.govtype <= 1:
            thissys.economy = (thissys.economy | 2)
        thissys.techlev = ((self.seed[1] >> 8) & 3) + (thissys.economy ^ 7)
        thissys.techlev += thissys.govtype >> 1
        if ((thissys.govtype) & 1) == 1:
            thissys.techlev += 1
        thissys.population = 4 * thissys.techlev + thissys.economy
        thissys.population += thissys.govtype + 1
        thissys.productivity = ((thissys.economy ^ 7) + 3) * (thissys.govtype + 4)
        thissys.productivity *= thissys.population * 8
        thissys.radius = 256 * (((self.seed[2] >> 8) & 15) + 11) + thissys.x
        thissys.goatsoupseed = (self.seed[1] & 0xFF,
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
        if longnameflag:   # bit 6 of ORIGINAL w0 flags a four-pair name
            namechars.append(self.pairs[pair4])
            namechars.append(self.pairs[pair4+1])
        thissys.name = "".join(namechars).replace(".", "")
        return thissys

    def tweakseed(self) -> None:
        temp = (self.seed[0])+(self.seed[1])+(self.seed[2])   # 2 byte aritmetic
        self.seed[0] = self.seed[1]
        self.seed[1] = self.seed[2]
        self.seed[2] = temp


class InputParser:
    tradnames = [c.name for c in commodities]

    numforLave = 7  # Lave is 7th generated planet in galaxy one
    numforZaonce = 129
    numforDiso = 147
    numforRied = 46
    fuelcost = 2  # 0.2 CR/Light year
    maxfuel = 70  # 7.0 LY tank

    def __init__(self):
        self.nativerand = True
        self.getcommand = ""
        self.mysrand(12345)  # ensure repeatability
        self.galaxynum = 1
        self.galax = Galaxy(1)
        self.currentplanet = InputParser.numforLave
        self.localmarket = self.genmarket(0x00, self.galax.galaxy[InputParser.numforLave])
        self.fuel = InputParser.maxfuel
        self.cash = 0.0
        self.lastrand = 0

    def mysrand(self, seed: int) -> None:
        self.lastrand = seed - 1

    def parser(self, command: str) -> None:
        # TODO
        pass

    def buildgalaxy(self, galnum: int) -> None:
        # TODO
        g = Galaxy(galnum)
        pass

    def genmarket(self, fluct: int, p: PlanSys) -> Market:
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
        market.quantity[AlienItems] = 0  # force nonavailibility
        return market

    def mainloop(self) -> None:
        print("\nWelcome to Text Elite 1.5.\n")
        self.parser("hold 20")
        self.parser("cash +100")
        self.parser("help")
        while True:
            print("\n\nCash: %.1f" % (self.cash / 10.0))
            getcommand = input()
            if len(getcommand) == 0:
                break
            print(repr(getcommand))
            self.parser(getcommand)


main = InputParser()
print("LAVE?", main.galax.galaxy[main.numforLave].name)
print("DISO?", main.galax.galaxy[main.numforDiso].name)
print("RIED?", main.galax.galaxy[main.numforRied].name)
print("ZAONCE?", main.galax.galaxy[main.numforZaonce].name)
