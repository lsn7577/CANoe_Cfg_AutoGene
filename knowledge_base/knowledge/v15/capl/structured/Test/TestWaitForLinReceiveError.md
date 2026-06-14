# TestWaitForLinReceiveError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinReceiveError (dword aFrameId, dword aTimeout);
long TestWaitForLinReceiveError (dword aTimeout);
```

## Description

Waits for the occurrence of LIN Receive Error event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aFrameId | Numeric ID of a frame whose Receive Error should be awaited. Default value: wait for any ID |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |

## Example

```c
testcase tcTFS_linReceiveErrorEvent ()
{
   linReceiveError linReceiveErrorData;

   if (testWaitForLinReceiveError(5000) == 1)
   {
      if (TestGetWaitLinReceiveErrData(linReceiveErrorData) == 0)
      {
         testStep("Evaluation", "LIN Receive Error event occurred for FrameId=0x%X", linReceiveErrorData.ID);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
