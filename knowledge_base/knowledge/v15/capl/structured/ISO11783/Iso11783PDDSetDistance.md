# Iso11783PDDSetDistance

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetDistance( dword ecuHandle, dword distance );
```

## Description

The distance covered is set with this function. The value is needed for the distance trigger and should be updated cyclically.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must previously have been created with Iso11783CreateECU. |
| distance | Distance covered in [m] |

## Return Values

Error code

## Example

```c
void ReceiveGBSDFromTractor( 
 pg GroundBasesSpeedPG thisPG ){
 Iso11783PDDSetDistance( ecuHandle, thisPG.GroundBasedDistance.phys );
}
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
