# Linux Cheat Sheet

[← Back to Home](../../index.md)

## File Permissions
Understanding `chmod` and `chown`.

*   `r` = read (4)
*   `w` = write (2)
*   `x` = execute (1)

```bash
chmod 755 file.sh   # rwx for owner, rx for group/others
chown user:group file.txt
```

## Essential Commands

| Command | Description |
| :--- | :--- |
| `ls -la` | List all files with details |
| `ps aux` | Show all running processes |
| `df -h` | Disk usage in human-readable format |
| `tar -czvf` | Compress files into a tarball |
| `grep -r` | Search recursively for text |

## Process Management
*   **htop**: Interactive process viewer.
*   **kill [PID]**: Terminate a process.
*   **systemctl status nginx**: Check service status.

## Networking
```bash
ip addr show      # Show IP addresses
netstat -tulpn    # Show listening ports
curl -I google.com # Fetch headers only