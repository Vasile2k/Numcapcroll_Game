import ctypes
from time import sleep

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002

VK_CAPITAL = 0x14
VK_NUMLOCK = 0x90
VK_SCROLL  = 0x91

keybd_event = ctypes.windll.user32.keybd_event

def pressKey(key):
	# Press key
	keybd_event(key, 0, KEYEVENTF_EXTENDEDKEY | 0, 0)
	# And release it
	keybd_event(key, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
	return

def playGame(game):
	return

def main():

	while True:
		pressKey(VK_NUMLOCK)
		sleep(0.2)
		pressKey(VK_NUMLOCK)
		pressKey(VK_CAPITAL)
		sleep(0.2)
		pressKey(VK_CAPITAL)
		pressKey(VK_SCROLL)
		sleep(0.2)
		pressKey(VK_SCROLL)

	return

if __name__ == '__main__':
	main()
