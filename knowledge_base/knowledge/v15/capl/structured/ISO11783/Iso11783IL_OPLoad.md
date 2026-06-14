# Iso11783IL_OPLoad

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPLoad( char filename[] ); // form 1
long Iso11783IL_OPLoad( char filename[], char version[] ); // form 2
long Iso11783IL_OPLoad( dbNode implement, char filename[], char version[] ); // form 3
```

## Description

The function loads an object pool file (*.iop or *.iopx). All other object pool access functions can only be used, if an object pool is loaded.

If the activation of the object pool was already done, the object pool is transmitted to the Virtual Terminal immediately. If not, this happens when the activation is done with Iso11873IL_OPActivate.

Optional a version designator for the object pool can be specified. The node layer tries to load the version with the Load Version command. If this is successful the object pool must not be transmitted to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| filename | File name of an object pool file (*.iop or *.iopx) |
| version (optional) | Designator of the object pool version |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPLoad( "ObjectPool.iop", "pool001"  );
Iso11783IL_OPActivate( );
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
