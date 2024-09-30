# TRY_Tor_Auto_Ip_Changer V 0.1
This is just a clone from main project for a tor app it can select port and change ip in static or dynamic time 

-change your Ip Address automatically This tool based on tor project

how to install this tools :

    : requirements:

    sudo apt-get install tor pip3 install requests[socks] or just run autoTor it will install everything

#Steps : (Run Commands)    

1: git clone https://github.com/mohammadham/TRY_Tor_Auto_Ip.git

2 : cd Auto_Tor_IP_changer

3 : python3 install.py

--> when show succ*...  in terminal type ( aut ) any where you want
---> you can use `-u` for start automatically in port 9050 else you can use `-p` and then set ports manually like this : "aut -p 9050 9051" or "aut -p 9051" 
    you can also use `-t` for time automatically change the ip address automatically and    `-f` for how many time change ip [0 to infinte IP change] 

*** EX :

     aut -u -t 500 -f 5
     
     aut -p 9051 -t 300
     
     aut -p 8585
     
     aut -u -f 5
     
     aut

4 : go to your browser / pc change sock proxy to 127.0.0.1:Port (9050)

5 : BOOOOOOMM!!!
