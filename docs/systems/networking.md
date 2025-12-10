# Networking Basics

[← Back to Home](../../index.md)

## OSI Model Layers
1.  **Physical**: Cables, hubs (Bits)
2.  **Data Link**: Switches, MAC addresses (Frames)
3.  **Network**: Routers, IP addresses (Packets)
4.  **Transport**: TCP/UDP (Segments)
5.  **Session**: Session management
6.  **Presentation**: Encryption, compression
7.  **Application**: HTTP, FTP, DNS

## Common Ports

| Port | Protocol | Service |
| :--- | :--- | :--- |
| 21 | FTP | File Transfer |
| 22 | SSH | Secure Shell |
| 53 | DNS | Domain Name System |
| 80 | HTTP | Web Traffic |
| 443 | HTTPS | Secure Web Traffic |
| 3306 | MySQL | Database |

## Subnetting Quick Reference
*   `/24` = 255.255.255.0 (254 hosts)
*   `/16` = 255.255.0.0 (65,534 hosts)
*   `/8` = 255.0.0.0 (16M+ hosts)