from subprocess import call
call(["ifconfig", "wlan0", "192.168.151.10", "netmask", "255.255.255.0", "broadcast", "192.168.2.255"])
