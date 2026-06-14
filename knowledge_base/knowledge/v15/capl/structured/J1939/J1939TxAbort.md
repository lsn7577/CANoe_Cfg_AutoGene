# J1939TxAbort

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939TxAbort( dword ecuHandle, dword pgn );
```

## Description

Interrupt of a transfer that has previously been started with J1939TxReqPG(). Please note in this regard that for technical reasons, it is only possible to interrupt PGs that are fragmented.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| pgn | parameter group handle |

## Return Values

0 on success or error code

## Example

```c
J1939TxAbort(ecuHdl, 
 0xFE09)
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
