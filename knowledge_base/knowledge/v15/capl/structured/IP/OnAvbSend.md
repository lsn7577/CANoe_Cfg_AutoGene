# OnAvbSend

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAvbSend(dword talkerHandle, dword result, int buffer[], dword length); // form 1
void OnAvbSend(dword talkerHandle, dword result, long buffer[], dword length); // form 2
void OnAvbSend(dword talkerHandle, dword result, qword buffer[], dword length); // form 3
void OnAvbSend(dword talkerHandle, dword result, byte buffer[], dword length); // form 4
```

## Description

This callback is dispatched when an asynchronous send operation on a Talker completes.

## Parameters

| Name | Description |
|---|---|
| talkerHandle | The Talker handle. |
| result | The specific result code of the operation. If the operation completed successfully the value is zero. Otherwise the value is non-zero. |
| buffer | The buffer provided with the send operation. |
| size | The number of elements sent. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2: form 1-3 8.5: form 4 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
