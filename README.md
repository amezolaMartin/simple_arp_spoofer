# simple_arp_spoofer
A simple ARP spoofing tool made to practice ARP poisoning with python. It can be used with my other repository Simple DNS Sniffer to make laboratories of dns request sniffing.


## Usage:

i tried it in my Kali Linux, first do this two commands:

```iptables --policy FORWARD ACCEPT``` 
Also, the file in path == ```/proc/sys/net/ipv4/ip_forward``` must be set to 1. Its usually set by default to 0, change it doing:

```sudo nano /proc/sys/net/ipv4/ip_forward``` and then closing it and saving it.

Now to use the actual ```arp_spoofer.py``` script just set in the code the router ip (its hardcoded because i was lazy) and then execute the python file like this:


python arp_spoofer.py -t <target_ip>


And you're done! The program will appear to get stuck but it works like that. It sends an arp response every 3 seconds (this can be easily changed in the code btw), and does this so the victim and the router don't get to update their arp tables and get out of the MITM attack.

See u.
