# TestGetWaitLinCSErrorData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinCSErrorData (linCSError apEvent); // form 1
long TestGetWaitLinCSErrorData (dword index, linCSError apEvent); // form 2
```

## Description

Retrieves the data of a checksum error triggered by the last wait instruction.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| apEvent | Data structure with the checksum error data. |
| index | Number of the "joined event" corresponds with the return value of "testJoin...". |

## Example

```c
testcase tcTFS_linCSError ()
{
   linCSError linCSErrorData;
   if (testWaitForLinCSError(5000) == 1)
   {
      if (testGetWaitLinCSErrorData(linCSErrorData) == 0)
      {
         testStep("Evaluation", "LIN CS Error event occurred for FrameId=0x%X", linCSErrorData.ID);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0: form 1 6.0: form 2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
