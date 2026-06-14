# TestWaitForADASSpeed

> Category: `ADAS` | Type: `function`

## Syntax

```c
long TestWaitForADASSpeed (long overUnder, float threshold, long aTimeout)
```

## Description

Waits for the occurrence of the first Detected Object matching the speed conditions passed as arguments. Should the Detected Object not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| overUnder | Specifies if the relative speed should be over or under the specified value. |
| threshold | Specified value that determines the maximum or minimum relative speed. An object moving towards the sensor has a negative relative speed. An object moving away from the sensor has a positive relative speed. The unit is specified in m/s. |
| aTimeout | Maximum time that should be waited [ms]. Transmission of 0: no timeout controlling. |

## Example

```c
enum VWaitThreshold
{
  kUnderThreshold = 0,
  kOverThreshold = 1
};
if(TestWaitForADASSpeed(kUnderThreshold, -30, 3000)) //Wait for Detected Object which moves with more than 30m/s towards the Sensor. (The relative speed is less than – 30 m/s)
{
  //Detected Object with relative speed less than –30 m/s detected
}
else
{
  //Timeout
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | 15 | 15 | — | 6 |
| Restricted To | — | Test | Test | Test | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
