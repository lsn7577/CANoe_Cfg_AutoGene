# Iso11783ECUGoOnline

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783ECUGoOnline( dword ecuHandle, dword newAddress );
```

## Description

After this function has been called, the logical ECU logs on onto the CAN bus. It must be called separately for each logical ECU.

If it is not possible to log on the first time with Address Claiming, or if the node is "rejected" with a higher priority Address Claiming by the bus at a later point in time, the corresponding error message must be evaluated in Iso11783AppErrorIndication. If you want to make a network assignment over the network, the PG "CommandedAddress" can be sent to an ECU.

Use the Null Address (0xFE) to switch the ECU to offline mode. In that explicit case a "Cannot Claim" message ("Address Claim" PG from source address 0xFE) is sent once.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| newAddress | Address to be claimed or Null Address (0xFE) to go offline |

## Example

```c
Iso11783ECUGoOnline(ecuHdl, 0x06);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
