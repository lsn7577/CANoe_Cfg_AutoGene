# TestWaitForLinSyncError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinSyncError(dword aTimeout);
```

## Description

Waits for a synchronisation error for the specified amount of time.

## Return Values

-2: Resume due to constraint violation

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

| Since Version |
|---|
