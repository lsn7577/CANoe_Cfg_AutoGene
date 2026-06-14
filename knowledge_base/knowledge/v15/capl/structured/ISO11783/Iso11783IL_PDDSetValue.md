# Iso11783IL_PDDSetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetValue( dbSignal signal, dword elementNumber, float value ); // form 1
long Iso11783IL_PDDSetValue( dword ddi, dword elementNumber, float value ); // form 2
long Iso11783IL_PDDSetValue( dbNode implement, dword ddi, dword elementNumber, float value ); // form 3
```

## Description

Sets the value of a process variable.

## Parameters

| Name | Description |
|---|---|
| signal | signal from the database The attribute ddi must have been defined for the signal. The signal must be defined in the same database as the node! |
| ddi | Data Dictionary Identifier, 0x0000.0xFFFF |
| elementNumber | element number, 0x000.0xFFF |
| value | new value of the process variable |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_PDDSetValue( 0x200. 3, value );
Iso11783IL_PDDSetValue( 0x200. 4, value );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 9.0: form 3 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
