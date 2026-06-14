# Iso11783PDDSetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetValue( dword ecuHandle, dbSignal signal, dword elementNumber, float alue );
long Iso11783PDDSetValue( dword ecuHandle, dword ddi, dword elementNumber, float value );
```

## Description

Sets the value of a process variable.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must previously have been created with Iso11783CreateECU. |
| signal | Signal from the database. The attribute ddi must have been defined for the signal. The signal must be defined in the same database as the node! |
| ddi | Data Dictionary Identifier, 0x0000.0xFFFF |
| elementNumber | Element number, 0x000.0xFFF |
| value | New value of the process variable |

## Return Values

error code

## Example

```c
Iso11783PDDSetValue( Sprayer, 0x200. 3, value );
Iso11783PDDSetValue( Sprayer, 0x200. 4, value );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
