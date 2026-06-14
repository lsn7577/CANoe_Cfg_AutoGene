# TestGetWaitLinETFSingleResponseData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinETFSingleResponseData (linFrame apEvent);
long TestGetWaitLinETFSingleResponseData (dword index, linFrame apEvent);
```

## Description

If LIN Event-triggered frame with a single response for the specified associated frame is the last event that triggers a wait instruction, the event content can be called up with this function.

When the triggering event is a part of a wait instruction for joined events, the index parameter has to correspond to the return value of "testJoin..." function.

## Parameters

| Name | Description |
|---|---|
| apEvent | Event variable that is filled with current data from the bus. |
| index | Index of the joined event. It corresponds to the return value of "testJoin..." function. |

## Example

```c
testcase tcTFS_linETFSingleResponse ()
{
   linFrame 0 linETFSingleResponseData;
   if (testWaitForLinETFSingleResponse(0x3A, 0x36, 5000) == 1)
   {
      if (testGetWaitLinETFSingleResponseData(linETFSingleResponseData) == 0)
      {
         testStep("Evaluation", "LIN Event-triggered frame with a single response occurred for FrameId=0x%X", linETFSingleResponseData.ID);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
