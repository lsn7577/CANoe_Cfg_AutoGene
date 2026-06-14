# TestGetWaitADASDetectedObject

> Category: `ADAS` | Type: `function`

## Syntax

```c
long TestGetWaitADASDetectedObject (char[] detectedObjectName)
```

## Description

If a Detected Object was the last event that triggered a wait Instruction, the name of the Detected Object can be called up with the TestGetWaitADASDetectedObject function.

## Parameters

| Name | Description |
|---|---|
| detectedObjectName | The name of the Detected Object that triggered the wait instruction. |

## Example

```c
enum VWaitThreshold
{
  kUnderThreshold = 0,
  kOverThreshold = 1
};

distObjRef ::ADAS::IDetectedMovingObject detMovingObj;
char buffer[100];

if(TestWaitForADASDistance(kUnderThreshold,30, 1000))
  {
  if(TestGetWaitADASDetectedObject(buffer) == 0) //Get the name of the Detected Object that triggered the Wait Condition
  detMovingObj = (distObjRef ADAS::IDetectedMovingObject) lookupDistObj(buffer); //Get the Detected Object with the CAPL Function lookupDistObj
  if(detMovingObj.IsValid) //Check if the Detected Obejct is valid
    {
      //Do something with the Detected Object
    }
  }
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
