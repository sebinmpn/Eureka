PORT=/dev/ttyUSB0


all:
	usermod -a -G dialout ${USERNAME}
	chmod a+wr ${PORT}

list:
	echo ${USERNAME}
	python3 list_tty.py
clean:


