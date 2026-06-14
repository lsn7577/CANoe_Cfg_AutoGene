# FSIL_SetBusyMode

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetBusyMode(byte flags); // form 1
long FSIL_SetBusyMode(dbNode* fs, byte flags); // form 2
```

## Description

Activates or deactivates the busy mode of the File Server.

If at least one of the busy mode flags is set:

Even busy mode is set the File Server responds to requests of a client.

## Parameters

| Name | Description |
|---|---|
| flags | bit 0: File Server is busy reading bit 1: File Server is busy writing |
| fs | FS simulation node to apply the function |

## Example

Example (applicable only in a test node)

```c
//Set File Server for 5 sec in a bisy mode
FSIL_SetBusyMode(FileServer, 0x2) // File Server is busy writing
testWaitForTimeout(5000);  // Wait for 5000 ms
FSIL_SetBusyMode(FileServer, 0) // File Server is not busy
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
