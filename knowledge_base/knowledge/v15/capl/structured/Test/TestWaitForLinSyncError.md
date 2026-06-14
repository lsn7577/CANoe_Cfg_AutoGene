# TestWaitForLinSyncError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinSyncError(dword aTimeout);
```

## Description

Waits for a synchronisation error for the specified amount of time.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Timeout in milliseconds |

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
| Since Version | — | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
