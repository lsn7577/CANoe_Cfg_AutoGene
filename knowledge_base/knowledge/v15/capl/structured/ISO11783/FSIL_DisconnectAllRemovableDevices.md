# FSIL_DisconnectAllRemovableDevices

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_DisconnectAllRemovableDevices(dword flags); // form 1
long FSIL_DisconnectAllRemovableDevices(dbNode* fs, dword flags); // form 2
```

## Description

Disconnects all virtual and physical removeable devices from the File Server Server that were previously connected by FSIL_ConnectRemovableDevice or plugged in.

Depended of the parameter flags the volumes are removed at once or File Server sends a notification to the clients before the volume is removed.

If one of the connected volumes was the primary volume then no primary volume is set after the volumes are removed.

After a virtual device is disconnected the appropriate Windows folder is still available.

## Parameters

| Name | Description |
|---|---|
| flags | Bit 0 = 0: Removes all volumes at once and sends a Volume Status Response for every volume with the name of the volume (parameter volumeName) and with volume status Removed to all clients. Bit 0 = 1: For every removable volume: First sends a Volume Status Response with the name of the removable volume (parameter volumeName) and with volume status Preparing for removal to all clients. If within 2 seconds there are no more Volume Status Request with value In Use from a client or if the maximum time for removal is expired then the File Server sends a Volume Status Response with volume status Removed and removes the volume. |
| fs | FS simulation node to apply the function. |

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
