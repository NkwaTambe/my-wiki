# The Linux Boot Process

[← Back to Home](../../index.md)

From the moment you press the power button to the login screen, a computer goes through a precise 6-stage sequence.

## 1. BIOS / UEFI (The Hardware Check)
*   **Action**: You press the power button.
*   **What happens**: The motherboard performs the **POST (Power-On Self-Test)** to ensure hardware (RAM, CPU, Keyboard) is functioning.
*   **Outcome**: It searches for a bootable device (Hard Drive, USB, CD) and hands control to the MBR or GPT.

## 2. MBR / GPT (The Map)
*   **MBR (Master Boot Record)**: The first 512 bytes of the disk. It contains the bootloader code.
*   **GPT (GUID Partition Table)**: The modern successor to MBR, used with UEFI.
*   **Outcome**: It locates and executes the Bootloader.

## 3. Bootloader (GRUB2)
*   **What happens**: You see the menu asking which OS to load (e.g., Ubuntu vs. Windows).
*   **Action**: It loads the Kernel into memory.
*   **Outcome**: Control is passed to the Kernel.

## 4. Kernel (The Brain)
*   **What happens**: The kernel mounts the **initrd** (Initial RAM Disk) file system.
*   **Action**: It detects hardware drivers and mounts the actual root file system (`/`).
*   **Outcome**: It executes the very first program: `/sbin/init`.

## 5. Init (The Manager)
*   **What happens**: `systemd` (or SysVinit) starts. This is Process ID 1 (PID 1).
*   **Action**: It reads configuration targets (runlevels) to know what services to start (Network, Sound, UI, SSH).
*   **Outcome**: It prepares the user environment.

## 6. Runlevel / Target (The Destination)
*   **What happens**: The system reaches its target state.
    *   **Runlevel 3 (Multi-user)**: Command line interface (CLI) only.
    *   **Runlevel 5 (Graphical)**: GUI with a display manager.
*   **Outcome**: The `getty` program displays the **Login Screen**.

---
*Summary Flow*: **BIOS** → **MBR** → **GRUB** → **Kernel** → **Init** → **Login**