# Iso11783OPLoadAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLoadAuxAssignment( dword ecuHandle, char filename[] );
```

## Description

This function loads the "Preferred Auxiliary Input Assignment" from an ini file. If the ECU is active the "Preferred Assignment Message" is sent immediately. Otherwise it is sent if the ECU gets active.

The "Preferred Assignment" must be saved with Iso11783OPSaveAuxAssignment before.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| filename | File name of an INI file |

## Return Values

0 or error code

## Example

```c
Iso11783OPLoad( handle, "ObjectPool.iop", "pool001"  );
Iso11783OPLoadAuxAssignment( handle, "Sprayer.INI");
Iso11783OPActivate( handle);
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
