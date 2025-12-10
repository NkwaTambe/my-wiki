# AWS Documentation

[← Back to Home](../../index.md)

## Core Services

### EC2 (Elastic Compute Cloud)
*   **Definition**: Web service that provides resizable compute capacity in the cloud.
*   **Key Concepts**:
    *   **AMI**: Amazon Machine Image, the blueprint for instances.
    *   **Instance Type**: Determines hardware (CPU, RAM).
    *   **Security Groups**: Virtual firewall for instances.

```bash
# Example: Connect to EC2 instance via SSH
ssh -i "key.pem" ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
```

### S3 (Simple Storage Service)
*   **Definition**: Object storage built to store and retrieve any amount of data.
*   **Key Concepts**:
    *   **Buckets**: Containers for objects (files).
    *   **Objects**: The actual data being stored.
    *   **Storage Classes**: Standard, Intelligent-Tiering, Glacier, etc.

## Best Practices
1.  **IAM**: Always follow the principle of least privilege.
2.  **MFA**: Enable Multi-Factor Authentication on the root account.
3.  **Billing**: Set up billing alerts immediately.