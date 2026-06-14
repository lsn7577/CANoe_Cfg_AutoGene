# TestGetWaitLinSyncErrorData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitLinSyncErrorData (LinSyncError apEvent);
```

## Description

Retrieves the data of a synchronisation error that triggered the last wait instruction.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access was successful

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
