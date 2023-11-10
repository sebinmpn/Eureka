# Micropython parallel processing

## Processing edgeAI using a cluster of microcontrollers in a microphone


### Data is transferred using SPI communication and controls the slave processors from the master.
A trained model is run in the slave microcontrollers it will produse output for data the feed by the master.


ESP32 will be the entry point and rp2040 will process data behind the system.

# Fitting a Pytorch model in Micropython.
* converting all numeric into 32 bit number space
* single clock mathematical operations are only using
