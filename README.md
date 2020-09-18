# Home-Temperature
Simple script that sends the temperature of surroundings to Reddit as a mail.

Any temperature sensor can be used but I used LM35 to calculate temperature.

If you don't have an LM35 or other temperature sensors then take a zener diode and add it to a voltage divider circuit using a resistor.
Then calculate the voltage using arduino pins. Usually this diode changes the voltage by 0.1mv per 1 degree celsius. But, This might not always be accurate.
