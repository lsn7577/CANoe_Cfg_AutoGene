# OnAvbReceive

> Category: `IP` | Type: `function`

## Syntax

```c
void OnAvbReceive(dword listenerHandle, dword result, int buffer[], dword length); // form 1
void OnAvbReceive(dword listenerHandle, dword result, long buffer[], dword length); // form 2
void OnAvbReceive(dword listenerHandle, dword result, byte buffer[], dword length); // form 3
```

## Description

This callback is dispatched when an asynchronous receive operation on a Listener completes.

## Parameters

| Name | Description |
|---|---|
| listenerHandle | The Listener handle. |
| result | The specific result code of the operation. If the operation completed successfully the value is zero. Otherwise the value is non-zero. |
| buffer | The buffer into which the data was stored. |
| size | The length of the received data. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2: form 1-2 8.5: form 3 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
