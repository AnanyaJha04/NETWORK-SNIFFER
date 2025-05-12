# NETWORK-SNIFFER
This Python script is a basic network sniffer.
## Purpose-
Its primary purpose is to capture and display network packets traveling through a network interface. It's a tool for network monitoring and basic network troubleshooting.  It allows you to see the raw data that is being sent across the network.

## Features-
1. Packet Capture: Captures raw network packets.
2. IP Header Decoding: Parses and displays the IP header of captured packets, including:
    * Version
    * IP Header Length
    * Time to Live (TTL)
    * Protocol
    * Source IP Address
    * Destination IP Address
3. TCP/UDP Header Decoding: Parses and displays the TCP and UDP headers, including:
    * Source Port
    * Destination Port
    * Sequence Number (TCP)
    * Acknowledgement Number (TCP)
    * Length (UDP)
4. Basic Data Display: Attempts to display the data payload of TCP and UDP packets as UTF-8 text (with error handling for non-text data).
5. Real-time Output: Displays captured packet information in the terminal as the packets are received.
6. Linux Compatibility: The code, as provided, uses `socket.AF_PACKET`, a Linux-specific feature. It has been adapted to work on macOS using `socket.AF_INET` and `socket.SOCK_RAW`.
7. Cross-Platform Compatibility (with caveats): The core concepts of packet capture are cross-platform, but the specific socket options and libraries may differ.  The code includes adaptations for macOS, but for full cross-platform compatibility, especially for capturing Ethernet frames, using libraries like `pypcap` is recommended.

## Terminology-
1. Packet: A fundamental unit of data transmitted over a network.
2. Network Interface: A hardware or software component that allows a computer to connect to a network (e.g., Wi-Fi adapter, Ethernet card).
3. IP Header: The header of an IP packet, containing information about the source and destination IP addresses, protocol, and other routing details.
4. TCP Header: The header of a TCP segment, containing information about source and destination ports, sequence numbers, acknowledgment numbers, and other connection-oriented details.
5. UDP Header: The header of a UDP datagram, containing information about source and destination ports and length for connectionless communication.
6. Raw Socket: A type of socket that allows direct access to the underlying network protocols, enabling the capture or sending of raw packets.
7. AF_PACKET: (Linux) A socket family that provides low-level access to network packets.
8. AF_INET: A socket family used for Internet Protocol (IP) networking.
9. SOCK_RAW: A socket type that allows sending or receiving raw packets, bypassing some of the operating system's network protocol processing.
10. Protocol Number: A number that identifies the protocol encapsulated within an IP packet (e.g., 6 for TCP, 17 for UDP).
11. TTL (Time to Live): A value in the IP header that limits the number of hops a packet can travel to prevent routing loops.
12. MAC Address: A unique identifier assigned to network interfaces for communication at the data link layer.

## Limitations-
1. Root Privileges Required: The script must be run with administrator/root privileges (using `sudo` on macOS/Linux) because creating raw sockets is a privileged operation.
2. Basic Functionality: This is a basic sniffer. It captures and displays packet headers and some data, but it doesn't have advanced features like:
    * Packet filtering
    * Protocol decoding beyond IP, TCP, and UDP
    * Data storage
    * Real-time analysis
3. Performance: Capturing and processing every packet can be resource-intensive, potentially impacting system performance under heavy network load.
4. No GUI: The script provides output only in the terminal.
5. Limited Error Handling: The error handling is basic.  More robust error handling would be beneficial for production use.
6. Data Loss: If the script cannot process packets quickly enough, some packets may be dropped.
7. Incomplete Protocol Dissection: The script only dissects the headers of IP, TCP, and UDP. It does not fully decode the contents of higher-level protocols like HTTP, DNS, or TLS.
8. Text-Based Data Only: The script attempts to decode the packet payload as UTF-8 text.  Binary data or data in other encodings will not be displayed correctly.
9. macOS `AF_INET` limitation: The macOS version of the code, which uses `AF_INET` and `SOCK_RAW`, does not capture the full Ethernet frame.

## Ethical Considerations-
"It is crucial to ensure legal compliance with all applicable laws and regulations regarding network monitoring and data privacy in your jurisdiction.  This script should only be used on networks that you own or have explicit permission to monitor, as unauthorized network sniffing is illegal and unethical.  Exercise extreme caution with any captured data, as network traffic may contain sensitive information such as passwords, personal communications, and confidential data.  Protect this data and only use it for legitimate purposes.  If you discover any security vulnerabilities while using this script, disclose them responsibly to the affected parties.  Avoid using this script for malicious purposes, including eavesdropping, denial-of-service attacks, or data theft."

## Further Improvement-
1. Packet Filtering: Implement Berkeley Packet Filter (BPF) support (using `pypcap` or a similar library) to allow filtering of packets based on specific criteria (e.g., source/destination IP, port, protocol).
2. Protocol Decoding: Add support for decoding more protocols, such as:
    * HTTP
    * DNS
    * TLS/SSL (Note: You can't decrypt TLS traffic without the private key)
    * ICMP
3. Data Storage: Implement options to save captured packets to a file in `pcap` format (using `pypcap`) for analysis with Wireshark, or to a database for structured storage and querying.
4. Real-time Analysis: Add features to analyze packets in real-time, such as:
    * Counting packet types
    * Detecting network anomalies
    * Calculating network statistics
5. Graphical User Interface (GUI): Develop a GUI (using a library like Tkinter, PyQt, or GTK) to provide a more user-friendly interface for capturing and analyzing network traffic.  Consider integrating with Wireshark.
6. Error Handling: Improve error handling to make the script more robust and handle unexpected situations gracefully.
7. Cross-Platform Enhancement: Use `pypcap` to make the script more cross-platform compatible and enable Ethernet frame capture on different operating systems.
8. Performance Optimization: Optimize the code for performance to minimize packet loss and reduce the impact on system resources, especially under heavy network load.  Consider using asynchronous programming.
9. Modular Design: Structure the code in a more modular way to make it easier to maintain, extend, and reuse components.
10. Logging: Implement a logging mechanism to record events, errors, and captured data for debugging and auditing purposes.

## Terminal/Command Prompts/Powershell-
In some operating systems, the Python IDLE might not support this code and would show an output error. So to tackle the situation, you can execute the prompts given in the codespace area on your Terminal/Command Prompt/Powershell, and in response, it would give you the output.
