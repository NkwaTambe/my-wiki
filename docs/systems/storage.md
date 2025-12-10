# Disk Design & Storage Management

[← Back to Home](../../index.md)

## Physical vs. Logical Volumes

Understanding how Linux manages storage is crucial for system administration. The Logical Volume Manager (LVM) adds a layer of abstraction between your physical disks and your file system.

### 1. Physical Volumes (PV)
*   **Definition**: The actual raw hardware or partitions.
*   **What it is**: A hard drive (`/dev/sda`), a partition (`/dev/sdb1`), or a RAID array.
*   **Analogy**: The actual bricks and land you possess.

### 2. Volume Groups (VG)
*   **Definition**: A pool of storage created by combining one or more Physical Volumes.
*   **What it is**: A unified container of storage space.
*   **Analogy**: Piling all your bricks into one big "supply heap" so you don't care which specific truck they came from.

### 3. Logical Volumes (LV)
*   **Definition**: Virtual partitions carved out of the Volume Group.
*   **What it is**: This is where you actually put your filesystem (ext4, xfs).
*   **Analogy**: The actual rooms you build using bricks from your supply heap. You can easily make a room bigger (extend the LV) by taking more bricks from the heap.

### Summary Diagram
```text
[ Disk 1 ]  [ Disk 2 ]  <-- Physical Volumes (PV)
     |          |
     +----------+
          |
  [  Volume Group (VG)  ] <-- The Storage Pool
          |
     +----+-----+
     |          |
 [ /home ]  [ /var ]    <-- Logical Volumes (LV)
```

## Common LVM Commands
*   `pvcreate /dev/sdb` - Initialize a disk for LVM.
*   `vgcreate my_vg /dev/sdb` - Create a volume group.
*   `lvcreate -L 10G -n my_lv my_vg` - Create a 10GB logical volume.
*   `lvextend -L +5G /dev/my_vg/my_lv` - Add 5GB to a volume.