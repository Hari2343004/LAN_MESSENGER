LAN Messenger (Local Network Communication System)

A secure, real-time communication system designed for high-speed messaging and file sharing over a Local Area Network (LAN). This project demonstrates a robust Client-Server architecture utilizing WebSockets for full-duplex communication, specifically tested in a virtualized environment involving a Windows Host and a Kali Linux VM.

🚀 Overview

The LAN Messenger is built to operate in air-gapped or internal network environments where internet connectivity is unavailable or security is a priority. Unlike cloud-based messengers, all data remains within the local router's subnet, ensuring 100% privacy and zero external latency.

Key Features

Real-Time Messaging: Instant bi-directional communication powered by WebSockets.

Full-Duplex File Sharing: Users can share files to specified network folders while maintaining active chat sessions.

No Internet Required: Operates entirely on LAN, WAN, or VPN.

Cross-Platform: Successfully tested for interoperability between Windows 10/11 and Kali Linux.

Serverless Feel: Uses P2P-style logic for direct folder merging and sharing.

🛠️ Tech Stack

Backend: Python 3.x, FastAPI

Server: Uvicorn (ASGI)

Communication Protocol: WebSockets (WS), HTTP (for file transfers)

Networking Tools: ICMP (Ping) for connectivity verification

Environment: Oracle VirtualBox (Windows Host + Kali Linux VM)

🌐 Network Configuration

To ensure the systems communicate, the following setup was implemented:

Subnetting: Both machines assigned to the same subnet (e.g., 192.168.56.x).

Connectivity Check: Verified using the ICMP protocol:

# From Windows to Kali
ping 192.168.56.101


Firewall: Rules were configured to allow traffic on the specified port (default: 5000).

⚙️ Installation & Setup

1. Clone the Repository

git clone [https://github.com/yourusername/lan-messenger.git](https://github.com/yourusername/lan-messenger.git)
cd lan-messenger


2. Install Dependencies

pip install fastapi uvicorn


3. Start the Server

Run the server on the host machine (or the machine acting as the hub):

uvicorn server:app --host 0.0.0.0 --port 5000


Note: Using 0.0.0.0 allows the server to listen on all available network interfaces.

4. Access the Client

Open a web browser on any machine in the network and navigate to:

http://[SERVER_IP_ADDRESS]:5000


📸 Screenshots

Feature

Preview

Connectivity

[Insert Screenshot of Ping Results]

UI Interface

[Insert Screenshot of Windows/Kali Side-by-Side]

File Transfer

[Insert Screenshot of Shared Folder Listing]

🎓 Learning Outcomes

Through this project, I gained hands-on experience in:

Network Troubleshooting: Resolving subnet isolation and firewall bottlenecks.

Asynchronous Programming: Handling concurrent WebSocket connections with Python's FastAPI.

Virtualization: Managing networking between a Host OS and a Guest VM.

System Architecture: Designing a reliable full-duplex communication flow.

📜 License

This project is open-source and available under the MIT License.

Maintained by: [Your Name]

Usage Scenarios: Offices, Classrooms, Labs, and Secure Internal Environments.
