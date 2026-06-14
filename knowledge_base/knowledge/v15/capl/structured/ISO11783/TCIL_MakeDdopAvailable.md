# TCIL_MakeDdopAvailable

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_MakeDdopAvailable(char[] ddopPath[]); // form 1
long TCIL_MakeDdopAvailable(dbNode tc, char[] ddopPath[]); // form 2
```

## Description

Loads a device descriptor object pool (DDOP) into the Task Controller.

Represents the situation that the DDOP is available on the side of Task Controller (e.g. via task file). An available DDOP can be activated with the Object-pool Activate message.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| ddopPath | Path of the DDOP file (*.XML). Path has to be absolute or relative relating to the folder of the CANoe configuration. |

## Example

Example form 2

```c
long result;
result =  TCIL_MakeDdopAvailable ( TC, "xml\\sprayerV1.xml");
if (result < 0)
{
  TestStepFail("Failed to make DDOP file available!");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
