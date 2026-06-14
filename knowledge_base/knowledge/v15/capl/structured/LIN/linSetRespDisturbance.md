# linSetRespDisturbance

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetRespDisturbance (long frameId, long lengthInBits, long level, long offsetInSixteenthBits);
```

## Description

Activates a disturbance in the response space of the specified LIN frame. A normal response by a simulated slave will be deactivated as long as the disturbance is active.

## Parameters

| Name | Description |
|---|---|
| frameId | LIN frame identifier in the range 0 .. 63. |
| lengthInBits | The duration of the disturbance [in bit times]. |
| level | The level of the disturbance. 0: dominant disturbance (inverts recessive bits) 1: recessive disturbance (inverts dominant bits - requires mag-Cab/Piggyback and external power supply) |
| offsetInSixteenthBits | The offset [in 1/16th bits] of the disturbance relative to the end of the header, i.e. to the PID byte. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

On pressing 'c' key start corrupting the response space and the first databyte of the response for LIN frame Motor1State_Cycl.

```c
on key 'c'
{
linFrame Motor1State_Cycl mMotor1State_Cycl;
if (0!=linSetRespDisturbance (mMotor1State_Cycl.id, 
 1, 0, 20))
{
// for the next the first bit of the response space 
 or of the first databyte
// (if the response space is zero) is inverted from recessive to 
dominant
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
