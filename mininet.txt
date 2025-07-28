sudo mn --topo single,3 --mac --switch ovsk --controller=default
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) 
*** Configuring hosts
h1 h2 h3 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet> ping all
*** Unknown command: ping all
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)
mininet> h1 ping h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=4.82 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.093 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.079 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.080 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.078 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=0.066 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=0.133 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=0.127 ms
^C
--- 10.0.0.2 ping statistics ---
8 packets transmitted, 8 received, 0% packet loss, time 7149ms
rtt min/avg/max/mdev = 0.066/0.684/4.822/1.563 ms
mininet> h1 ping -c 10 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=4.15 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.929 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.083 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.107 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.078 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=0.079 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=0.099 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=0.081 ms
64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=0.093 ms
64 bytes from 10.0.0.2: icmp_seq=10 ttl=64 time=0.078 ms

--- 10.0.0.2 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9169ms
rtt min/avg/max/mdev = 0.078/0.578/4.153/1.217 ms
mininet> h1 ping -c 10 h3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
64 bytes from 10.0.0.3: icmp_seq=1 ttl=64 time=8.41 ms
64 bytes from 10.0.0.3: icmp_seq=2 ttl=64 time=0.868 ms
64 bytes from 10.0.0.3: icmp_seq=3 ttl=64 time=0.079 ms
64 bytes from 10.0.0.3: icmp_seq=4 ttl=64 time=0.077 ms
64 bytes from 10.0.0.3: icmp_seq=5 ttl=64 time=0.072 ms
64 bytes from 10.0.0.3: icmp_seq=6 ttl=64 time=0.089 ms
64 bytes from 10.0.0.3: icmp_seq=7 ttl=64 time=0.080 ms
64 bytes from 10.0.0.3: icmp_seq=8 ttl=64 time=0.077 ms
64 bytes from 10.0.0.3: icmp_seq=9 ttl=64 time=0.076 ms
64 bytes from 10.0.0.3: icmp_seq=10 ttl=64 time=0.078 ms

--- 10.0.0.3 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9175ms
rtt min/avg/max/mdev = 0.072/0.990/8.409/2.484 ms
mininet> h2 ping -c 10 h3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
64 bytes from 10.0.0.3: icmp_seq=1 ttl=64 time=5.42 ms
64 bytes from 10.0.0.3: icmp_seq=2 ttl=64 time=1.29 ms
64 bytes from 10.0.0.3: icmp_seq=3 ttl=64 time=0.085 ms
64 bytes from 10.0.0.3: icmp_seq=4 ttl=64 time=0.089 ms
64 bytes from 10.0.0.3: icmp_seq=5 ttl=64 time=0.078 ms
64 bytes from 10.0.0.3: icmp_seq=6 ttl=64 time=0.074 ms
64 bytes from 10.0.0.3: icmp_seq=7 ttl=64 time=0.076 ms
64 bytes from 10.0.0.3: icmp_seq=8 ttl=64 time=0.074 ms
64 bytes from 10.0.0.3: icmp_seq=9 ttl=64 time=0.074 ms
64 bytes from 10.0.0.3: icmp_seq=10 ttl=64 time=0.127 ms

--- 10.0.0.3 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9174ms
rtt min/avg/max/mdev = 0.074/0.739/5.424/1.602 ms
