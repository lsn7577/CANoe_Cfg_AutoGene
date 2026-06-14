# Iso11783IL_OPActivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPActivate( ); // form 1
long Iso11783IL_OPActivate( dword options ); // form 2
long Iso11783IL_OPActivate( dbNode implement, dword options ); // form 3
```

## Description

The function activates the Object Pool API. The initialization procedure with the Virtual Terminal is performed and the object pool is transmitted to the Virtual Terminal.

During the initialization procedure some information from the Virtual Terminal is requested. This can be suppressed with the options parameter. The requested information can be get with the function Iso11783IL_OPGetVTInfo.

## Parameters

| Name | Description |
|---|---|
| options | Options bit 0 = 1: suppress Get Memory command bit 1 = 1:-suppress Get Number of Softkeys command bit 2 = 1: suppress Get Text Font Data command bit 3 = 1: suppress Get Hardware command |
| implement | Simulation node to apply the function. |

## Example

Example 1

Example 2 Move to another Virtual Terminal (VT)

```c
Iso11783IL_OPSetProperty("Version", 5);
Iso11783IL_OPLoad(  "ObjectPool.iop", "pool001" );
Iso11783IL_OPActivate( );
void MoveToVtWithFunctionInstance1()
{
  Iso11783IL_OPDeactivate();
  Iso11783IL_OPSetProperty( "VTFunctionInstance", 1 );
  SetTimer( mMoveTimer, 1000 );
}

on timer mMoveTimer
{
  Iso11783IL_OPLoad( "Sprayer.iop" );
  Iso11783IL_OPActivate();
}
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
