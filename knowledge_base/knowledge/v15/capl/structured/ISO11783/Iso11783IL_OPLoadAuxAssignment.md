# Iso11783IL_OPLoadAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPLoadAuxAssignment( char filename[] ); // form 1
long Iso11783IL_OPLoadAuxAssignment( dbNode implement, char filename[] ); // form 2
```

## Description

This function loads the Preferred Auxiliary Input Assignment from an INI file. If the ECU is active the Preferred Assignment Message is sent immediately. Otherwise it is sent if the ECU gets active.

The Preferred Assignment must be saved with Iso11783IL_OPSaveAuxAssignment before.

## Parameters

| Name | Description |
|---|---|
| filename | File name of an INI file |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPLoad( "ObjectPool.iop", "pool001"  );
Iso11783IL_OPLoadAuxAssignment( "Sprayer.INI");
Iso11783IL_OPActivate( );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
