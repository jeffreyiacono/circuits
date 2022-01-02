# Legend of Zelda Secret Found Door
When door is closed, red LED is lit.
<br />
When door is opened, green LED is lit and Legend of Zelda [secret found](#file-02-loz-secret-wav) sound is played.

<a href="https://photos.app.goo.gl/nrxLiGpwgWGxYoKRA">
  <img alt="View Demo Video" src="https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/view-door-open-demo.png" />
</a>

## The Parts
### The Door
Made out of a wooden plank that was cut to size with a table and miter saw. Used
small hinges so the door can swing open and closed. Held together with a
combination of screws and nails. Used hand-held drill to make holes for the LEDs
to fit through.

[![Door Parts](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/door-parts.jpeg)](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/door-parts.jpeg "View Door Parts")

### The Circuit
The breadboard mockup is the following ...

[![Boardboard mockup](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/circuit.png)](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/circuit.png "View Circuit")

And here is the schematic view of the circuit ...

[![Schematic mockup](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/circuit-schematic.png)](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/circuit-schematic.png "View Schematic")

Apologies if this is not the standard/best way to present a schematic. I have no idea what I'm doing here 😉

### The Code
See [here](#file-01-door-monitor-py).

The script starts with some initial setup to get the board, pins, etc.
configured. When the switch changes, the `switchChangedFn` is
called and determines the state. If the switch is now open (ie. the door is
opened) the red LED is turned off, the green LED is turned on, and the wav file
is played by the pi. If the switch is closed (ie. the door is closed),
the green LED is turned off and the red LED is turned on.

## All Together
Here is what the pi, circuit, and back of the door look like:

[![All together now](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/back-of-door-breadboard-pi.jpeg)](https://raw.githubusercontent.com/jeffreyiacono/images/master/zelda-door/back-of-door-breadboard-pi.jpeg "Everything all together")

## Questions, comments, concerns
Just let me know via the comments below. Thanks!
