# TestWaitForLinHeader

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinHeader (dbMsg aFrame, dword aTimeout);
long TestWaitForLinHeader (dword aFrameId, dword aTimeout);
long TestWaitForLinHeader (dword aTimeout);
```

## Description

Waits for the Header occurrence of the specified LIN frame. Should the header not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no frame is specified the wait condition is resolved on any LIN header.

## Parameters

| Name | Description |
|---|---|
| aFrame | Frame whose header should be awaited. |
| aFrameId | Numeric ID of a frame whose header should be awaited. |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |

## Example

```c
testcase tcTFS_linHdrEvent ()
{
   linheader  linHeaderData;

   if (testWaitForLinHeader(5000) == 1)
   {
      if (TestGetWaitLinHdrData(linHeaderData) == 0)
      {
         testStep("Evaluation", "LIN Header event occurred for FrameId=0x%X", linHeaderData.ID);
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
