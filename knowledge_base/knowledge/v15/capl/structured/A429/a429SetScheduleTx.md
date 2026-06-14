# a429SetScheduleTx

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429SetScheduleTx( a429word myA429word, dword myCycle );
```

## Description

Prepare an ARINC word to be transmitted cyclically by means of the hardware scheduling support. Calling this function modifies the selectorsTxCycle and TxCtrl.

Note: This modifies the ARINC word attributes only. For transmission call the function output.

## Parameters

| Name | Description |
|---|---|
| myA429word | ARINC word |
| myCycle | cycle time with microseconds resolution; value range [0 .. 600.000.000 (600 s)]; with 0 the behavior is switched to ON_REQ (see selector TxCtrl). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
