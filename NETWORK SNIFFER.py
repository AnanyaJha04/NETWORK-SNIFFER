import socket
import struct
import sys

def unpack_ip(addr):
    return '.'.join(map(str, addr))

def main():
    try:
        # Create a raw socket to capture IP packets
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        # Include IP headers in the captured packets
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except PermissionError as e:
        print(f'Error: Permission denied. Please run this script with administrator/root privileges (using sudo on macOS/Linux).')
        print(f'Details: {e}')
        sys.exit()
    except socket.error as msg:
        print(f'Socket could not be created. Error: {msg}')
        sys.exit()

    print("Sniffing IP network traffic...")

    try:
        while True:
            raw_packet, addr = s.recvfrom(65565)

            # Unpack the IP header (20 bytes minimum)
            ip_header = struct.unpack("!BBHHHBBH4s4s", raw_packet[:20])
            version_ihl = ip_header[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
            iph_length = ihl * 4
            ttl = ip_header[5]
            protocol = ip_header[6]
            s_addr = socket.inet_ntoa(ip_header[8])
            d_addr = socket.inet_ntoa(ip_header[9])

            print(f"\nIP Header:")
            print(f"  Version: {version}")
            print(f"  IP Header Length: {iph_length} bytes")
            print(f"  TTL: {ttl}")
            print(f"  Protocol: {protocol}")
            print(f"  Source IP: {s_addr}")
            print(f"  Destination IP: {d_addr}")

            # Process TCP packets
            if protocol == 6:
                tcp_header = struct.unpack("!HHLLHHH", raw_packet[iph_length:iph_length + 20])
                source_port = tcp_header[0]
                dest_port = tcp_header[1]
                # ... (rest of your TCP processing code)

            # Process UDP packets
            elif protocol == 17:
                udp_header = struct.unpack("!HHHH", raw_packet[iph_length:iph_length + 8])
                source_port = udp_header[0]
                dest_port = tcp_header[1]
                # ... (rest of your UDP processing code)

    except KeyboardInterrupt:
        print("\nSniffing stopped.")
    finally:
        if 's' in locals():
            s.close()

if __name__ == "__main__":
    main()
 

