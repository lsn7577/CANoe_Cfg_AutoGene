# Iso11783OPLoad

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLoad( dword ecuHandle, char filename[] );
long Iso11783OPLoad( dword ecuHandle, char filename[], char version[] );
```

## Description

The function loads an object pool file (*.iop). All other object pool access functions can only be used, if an object pool is loaded.

If the activation of the object pool was already done, the object pool is transmitted to the Virtual Terminal immediately. If not, this happens when the activation is done with Iso11783OPActivate.

Optional a version designator for the object pool can be specified. The node layer tries to load the version with the Load Version command. If this is successful the object pool must not be transmitted to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| filename | File name of an object pool file (*.IOP) |
| version | Optional designator of the object pool version |

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );

Iso11783OPLoad( handle, "ObjectPool.iop", "pool001"  );
ISo11783OPActivate( handle);
Iso11783ECUGoOnline(handle, gECUAddress );
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
