# TestGetWaitLinSyncErrorData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinSyncErrorData (LinSyncError apEvent); // form 1
long TestGetWaitLinSyncErrorData (dword index, LinSyncError apEvent); // form 2
```

## Description

Retrieves the data of a synchronisation error that triggered the last wait instruction.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Parameters

| Name | Description |
|---|---|
| apEvent | Data structure that will be filled with the synchronisation error data. |
| index | Number of the "joined event" corresponds with the return value of "testJoin...". |

## Example

```c
testcase tcTFS_linSyncErrorEvent ()
{
   linSyncError linSyncErrorData;
   if (testWaitForLinSyncError(5000) == 1)
   {
      if (testGetWaitLinSyncErrorData(linSyncErrorData) == 0)
      {
         testStep("Evaluation", "LIN Sync Error event occurred. SyncBreak=%d ns; SyncDel=%d ns", linSyncErrorData.breaklen, linSyncErrorData.delimiterlen);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1 6.0: form 2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
