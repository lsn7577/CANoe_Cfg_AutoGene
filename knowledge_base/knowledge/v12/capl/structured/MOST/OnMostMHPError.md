# OnMostMHPError

> Category: `MOST` | Type: `function`

## Syntax

```c
long OnMostMHPError(long sourceDevID, long destDevID, long fBlockID, long instID, long functionID, long opType)
```

## Description

The event procedure is called up as soon as a MOST High protocol violation is observed.

Within this event procedure the following functions are available

Indicates the MHP observer error number. See possible MHP observer error codes.Parameter:NoneReturns: Observer error number

Indicates the error value. Not supported by all error codes.Parameter:NoneReturns: Error value or 0

Indicates the expected value. Not supported by all error codes.Parameter:NoneReturns: Expected value or 0

Indicates if this is a warning. Warnings may indicate a communication problem.Parameter:NoneReturns: Error value or 0

The functions mostEventChannel, mostEventTime and mostEventTimeNS can be used to call up supplemental information.

## Return Values

The return value determines whether the MHP error event is relayed to the next function block in the Measurement Setup (e.g. a Trace Window).

## Availability

| Since Version |
|---|
