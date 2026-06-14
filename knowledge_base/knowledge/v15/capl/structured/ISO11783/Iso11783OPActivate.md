# Iso11783OPActivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPActivate( dword ecuHandle);
long Iso11783OPActivate( dword ecuHandle, dword options );
```

## Description

The function activates the Object Pool API. The initialization procedure with the Virtual Terminal is performed and the object pool is transmitted to the Virtual Terminal.

During the initialization procedure some information from the Virtual Terminal is requested. This can be suppressed with the options parameter. The requested information can be get with the function Iso11783OPGetVTInfo.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| options | Options: Bit 0 = 1: suppress Get Memory command Bit 1 = 1: suppress Get Number of Softkeys command Bit 2 = 1: suppress Get Text Font Data command Bit 3 = 1: suppress Get Hardware command |

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );

Iso11783OPLoad( handle, "ObjectPool.iop", 
 "pool001" );
Iso11783OPActivate( handle );
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
