# SCC_SLAC_GetCMSetKeyCnfData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SLAC_GetCMSetKeyCnfData ( dword& MyNonce, dword& YourNonce, dword& PID, dword& PRN, dword& PMN, dword& CCOCapability )
```

## Description

Queries the additional parameters of a CM_Set_Key.Cnf message, all at once, via references.

## Parameters

| Name | Description |
|---|---|
| MyNonce | Random number that will be used to verify next message (usually 0). |
| YourNonce | Last nonce received; used to verify this message (usually 0). |
| PID | Protocol (usually 0x04). |
| PRN | Protocol Run Number (usually 0). |
| PMN | Protocol Message Number (usually 0). |
| CCOCapability | STA’s CCo capability (usually 0). |

## Return Values

Data and length of the reserved field.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
