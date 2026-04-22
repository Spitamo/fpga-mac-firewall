<html>

<head>

&#x20; <meta charset="UTF-8" />

</head>

<body>



<h1>FPGA-Hardware-Firewall</h1>



<p>A lightweight hardware firewall and Ethernet frame sniffer implemented on FPGA using VHDL, with Python-based frame generation and simulation-driven validation.</p>



<h2>Project Overview</h2>



<p>This project implements a <strong>hardware firewall</strong> for monitoring and filtering Ethernet frames at the <strong>Data Link Layer</strong>. The core logic is written in VHDL and uses a finite state machine (FSM) to validate frames by checking destination MAC, source MAC, and payload content. A Python script built with Scapy generates test frames, and Wireshark is used to verify traffic and payload correctness.</p>



<h2>Features</h2>



<ul>

&#x20; <li>FPGA-based Ethernet frame filtering.</li>

&#x20; <li>FSM-driven validation of valid and invalid frames.</li>

&#x20; <li>Support for frame sniffing and lightweight monitoring.</li>

&#x20; <li>Python + Scapy frame generation for testing.</li>

&#x20; <li>Wireshark-based traffic inspection.</li>

&#x20; <li>VHDL testbench for simulation.</li>

</ul>



<h2>Architecture</h2>



<p>The system follows a simple pipeline:</p>



<ol>

&#x20; <li>Receive an incoming Ethernet frame.</li>

&#x20; <li>Check the destination MAC address.</li>

&#x20; <li>Check the source MAC address.</li>

&#x20; <li>Inspect the payload data.</li>

&#x20; <li>Mark the frame as valid or invalid.</li>

&#x20; <li>Forward only valid frames to the output.</li>

</ol>



<p>The design is implemented as an FSM with states such as <code>IDLE</code>, <code>CHECK\_DST\_MAC</code>, <code>CHECK\_SRC\_MAC</code>, <code>CHECK\_DATA</code>, <code>VALID</code>, and <code>INVALID</code>.</p>



<h2>Repository Structure</h2>



<pre><code>FPGA-Hardware-Firewall

┣  src

┃ ┣ vhdl.vhdl

┃ ┗ UCF.txt

┣  sim

┃ ┗ testbench.vhdl

┣  scripts

┃ ┗ framegen.py

┣  docs

┃ ┣ testbench\_st-2.jpg

┃ ┣ wireshark-output-1-3.jpg

┃ ┗ wireshark-output-2.jpg

┗  README.md

</code></pre>



<h2>Files</h2>



<ul>

&#x20; <li><code>src/vhdl.vhdl</code>: Main VHDL design for frame filtering.</li>

&#x20; <li><code>src/UCF.txt</code>: FPGA pin constraints file.</li>

&#x20; <li><code>sim/testbench.vhdl</code>: Testbench for validating the FSM in simulation.</li>

&#x20; <li><code>scripts/framegen.py</code>: Python script for generating Ethernet test frames.</li>

</ul>



<h2>Technologies Used</h2>



<ul>

&#x20; <li>VHDL</li>

&#x20; <li>FPGA</li>

&#x20; <li>Xilinx Artix-7 XC7A35T</li>

&#x20; <li>Python</li>

&#x20; <li>Scapy</li>

&#x20; <li>Wireshark</li>

&#x20; <li>Active-HDL</li>

&#x20; <li>Vivado</li>

</ul>



<h2>Simulation Results</h2>



<p>The simulation showed that the FSM correctly distinguishes valid frames from invalid ones. The <code>valid\_out</code> signal is asserted only when frame conditions are satisfied. The waveform below demonstrates the state transitions and output behavior.</p>



<p><img src="docs/testbench\_st-2.jpg" alt="VHDL simulation waveform" /></p>



<h2>Wireshark Validation</h2>



<p>The generated Ethernet frames were captured and verified in Wireshark. The filter <code>frame contains DEADBEEF</code> highlights packets carrying the expected payload. This confirms that the Python frame generator is producing the intended traffic.</p>



<p><img src="docs/wireshark-output-1-3.jpg" alt="Wireshark packet list with DEADBEEF filter" /></p>



<p>This packet detail view shows the frame structure, including source and destination MAC addresses, EtherType, and the payload bytes. The displayed bytes match the generated test data exactly.</p>



<p><img src="docs/wireshark-output-2.jpg" alt="Wireshark packet details" /></p>



<h2>Test Frame Generation</h2>



<p>The <code>framegen.py</code> script creates Ethernet frames using Scapy. Every tenth frame can carry a known payload such as <code>DEADBEEF</code>, while other frames may contain random data. This makes it easy to test both acceptance and rejection paths in the firewall logic.</p>



<h2>Limitations</h2>



<ul>

&#x20; <li>Hardware-level validation on the physical FPGA board was not completed in this phase.</li>

&#x20; <li>Simulation cannot reproduce all real-world effects such as noise, network delay, or NIC-specific behavior.</li>

&#x20; <li>CRC verification and end-to-end hardware testing can be added in future work.</li>

</ul>



<h2>Future Work</h2>



<ul>

&#x20; <li>Full deployment on the FPGA board.</li>

&#x20; <li>CRC checking for stronger frame validation.</li>

&#x20; <li>Rule-based filtering for MAC, EtherType, and payload patterns.</li>

&#x20; <li>Packet logging and statistics counters.</li>

&#x20; <li>Optional lightweight inspection features for network security applications.</li>

</ul>







</body>

</html>



