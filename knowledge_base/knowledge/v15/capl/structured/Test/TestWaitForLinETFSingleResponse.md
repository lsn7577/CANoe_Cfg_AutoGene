# TestWaitForLinETFSingleResponse

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinETFSingleResponse (dword aETFFrameId, dword aAssocFrameId, dword aTimeout);
```

## Description

Waits for the occurrence of a LIN Event-triggered frame with a single response for the specified associated frame. Should the event-triggered frame not occur before the expiration of the specified timeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aETFFrameId | Frame identifier of LIN event-triggered frame to be awaited. |
| aAssocFrameId | Frame identifier of a LIN unconditional frame associated with the awaited event-triggered frame |
| aTimeout | Timeout in milliseconds. Value 0: no timeout |

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
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
