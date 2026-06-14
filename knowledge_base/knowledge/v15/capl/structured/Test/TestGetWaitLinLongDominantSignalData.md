# TestGetWaitLinLongDominantSignalData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinLongDominantSignalData (linLongDominantSignal apEvent);
long TestGetWaitLinLongDominantSignalData (dword index, linLongDominantSignal apEvent);
```

## Description

If LIN LongDominantSignal is the last event that triggers a wait instruction, the frame content can be called up with the first function.

The second function can only be used for joined events. The number of the joined event (return value of testJoin...) is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| apEvent | Event variable that should be filled in with this function. |
| index | Number of the joined event corresponds with the return value of testJoin.... |

## Example

```c
testcase tcTFS_linLongDominantSignal ()
{
   linLongDominantSignal linLongDominantSignal;
   if (testWaitForLinLongDominantSignal (5000) == 1)
   {
      if (testGetWaitLinLongDominantSignalData(linLongDominantSignal) == 0)
      {
         testStep("Evaluation", "LIN LongDominantSignal event occurred. Signal length is %d ns", linLongDominantSignalData.length_ns);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
