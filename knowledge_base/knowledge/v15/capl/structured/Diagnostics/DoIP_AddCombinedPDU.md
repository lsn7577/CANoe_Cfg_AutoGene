# DoIP_AddCombinedPDU

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_AddCombinedPDU(dword payloadType, byte payload[], dword payloadLen);
```

## Description

Append another well-formed PDU to the PDU combination buffer for later sending with DoIP_SendPDUCombination. The currently configured protocol version byte will be used for the PDU.

## Parameters

| Name | Description |
|---|---|
| payloadType | [0; 0xFFFF] type to send, i.e. this can be any value. |
| payload | The data following the generic DoIP header. |
| payloadLen | Length of the data following the header. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
