AI-Driven Network Optimization Platform
A beginner-friendly prototype for learning how to use Mininet, Python, and Machine Learning to optimize network paths based on real, emulated latency data.

Project Overview
Goal: Simulate a small network, measure and analyze latency, and use a basic machine learning model to identify the path with lowest latency.

Tools: Mininet (for network emulation), Python (pandas, scikit-learn), and matplotlib.

1. Mininet Setup & Commands
Network Topology
Create a simple network of 3 hosts connected to a single switch:

bash
sudo mn --topo single,3 --mac --switch ovsk --controller=default
Key Mininet Commands Used
Once in the Mininet CLI (mininet> prompt):

Test connectivity (ping all hosts):
bash
pingall
Measure latency between pairs (ping each pair for 10 packets):
bash
h1 ping -c 10 h2
h1 ping -c 10 h3
h2 ping -c 10 h3
For each run, note the output statistics—for example:

text
--- 10.0.0.2 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9169ms
rtt min/avg/max/mdev = 0.078/0.578/4.153/1.217 ms
Copy these "min/avg/max" RTT values into your CSV for later analysis.

Exit Mininet:
bash
exit
2. Data Collection & Storage
Save your ping measure data in a file called network_latency.csv:

Source	Destination	MinRTT	AvgRTT	MaxRTT
h1	h2	0.078	0.578	4.153
h1	h3	0.072	0.990	8.409
h2	h3	0.074	0.739	5.424
Example CSV content:

text
Source,Destination,MinRTT,AvgRTT,MaxRTT
h1,h2,0.078,0.578,4.153
h1,h3,0.072,0.990,8.409
h2,h3,0.074,0.739,5.424
3. Python Analysis
Python script (network_optimizer.py) loads your CSV, labels the best path, fits a simple ML model, and visualizes average latency.

Basic usage:
bash
python3 network_optimizer.py
[You can see network_optimizer.py in this repository for all code and comments.]
