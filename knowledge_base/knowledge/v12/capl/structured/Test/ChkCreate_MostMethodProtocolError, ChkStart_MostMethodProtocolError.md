# ChkCreate_MostMethodProtocolError, ChkStart_MostMethodProtocolError

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostMethodProtocolError(char aMethod[], long aInstanceID, dword aTimeoutWaitForProcessing1, dword aTimeoutWaitForProcessing2, dword aTimeoutMaxDuration, Callback aCallback);
```

## Description

This check monitors MOST protocol compliance for a given method supporting the optypes "StartResult" or "StartResultAck". This includes monitoring of the messages sequences and timeout conditions on answer times and send intervals.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
