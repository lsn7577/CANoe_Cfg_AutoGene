# Iso11783IL_PDDSetDistance

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetDistance( dword distance ); // form 1
long Iso11783IL_PDDSetDistance( dbNode implement, dword distance ); // form 2
```

## Description

The distance covered is set with this function. The value is needed for the distance trigger and should be updated cyclically.

## Parameters

| Name | Description |
|---|---|
| distance | distance covered in [m] |
| implement | Simulation node to apply the function. |

## Example

```c
void ReceiveGBSDFromTractor( 
 pg GroundBasesSpeedPG thisPG ){
 Iso11783IL_PDDSetDistance( thisPG.GroundBasedDistance.phys );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
