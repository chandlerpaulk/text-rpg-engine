from logic import Logic

engine = Logic(True)

# Preprogrammed Intro scene to be run in main script
class Intro():
    def __init__(self) -> None:
        pass

    def play(self):
        engine.call('cls')
        engine.type("Adventure Awaits")
        engine.type("...", speed = 0.9)
        print("\n\n\n")
        engine.pause(1.8)
        engine.type("                   `.`     \n", speed = 0.0005)
        engine.type("         `....--:/+oo:     `:++++++++++++  .+++++++++++++:  `//`       .++-   -/+++++++++++`  /+/              ./+++++++++/-   -+++++++++++++-  :+++++++++++/.   `:/+++++++++++`\n", speed = 0.0005)
        engine.type("      .--.```.-/osss/       shhyyyyyyyyyyy  -yyyyyhhhyyyyy+  /hhy/`     -hh/  +hhyyyyyyyyyyy. `hhs             .yhhyyyyyyyyhh+  :yyyyyhhhyyyyy/  ohhyyyyyyyyhhh.  shhyyyyyyyyyyy`\n", speed = 0.0005)
        engine.type("    .:`         `/so`      `hhs                   ohh`       +hhhhy/`   -hh/  shh             `hhs             -hh/       `hhs        yhy`       ohh.       /hh:  hhy            \n", speed = 0.0005)
        engine.type("   `/             :+       `hhy+++++++++/`        ohh`       +hh:+hhy:  -hh/  shh             `hhs             -hhs+++++++ohhs        yhy        ohho+++++++shh-  hhh+++++++++++`\n", speed = 0.0005)
        engine.type("   :.              +        .ossssssssshhy        ohh`       +hh- `+hhy:-hh/  shh             `hhs             -hhysssssssshhs        yhy        ohhsshhhhssso:   hhhsssssssssss`\n", speed = 0.0005)
        engine.type("   :.             `/                   yhh        ohh`       +hh-   .ohhyhh/  shh             `hhs             -hh/       `hhs        yhy        ohh. .ohhs-      hhy            \n", speed = 0.0005)
        engine.type("   `/     ``      :.       `ooooooooooohhy  -oooooyhhsoooo/  +hh-     .ohhh/  ohhooooooooooo.  yhhooooooooooo` -hh/       `hhs  :ooooohhhooooo:  ohh`   -ohhsoo-  yhhooooooooooo`\n", speed = 0.0005)
        engine.type("    `:.  .+o+:..-:.        `oooooooooooo+.  -ooooooooooooo/  :oo.       .+o.  `/oooooooooooo.  .+oooooooooooo` .oo:        oo/  :ooooooooooooo:  /oo`     -oooo-  .+oooooooooooo`\n", speed = 0.0005)
        engine.type("      .---ooooo/-          \n", speed = 0.0005)
        engine.type("         `...`             ", speed = 0.0005)
        engine.pause(2)
        print("\n\n\n")
        engine.type("A game by Chandler Paulk")
        engine.pause(6)
        engine.call('cls')
        engine.pause(1)
        engine.type("Dedicated to all the goofballs out there.\n")
        engine.pause(3)
        engine.call('cls')
        engine.blink(2, 0.45)
        engine.pause(0.8)