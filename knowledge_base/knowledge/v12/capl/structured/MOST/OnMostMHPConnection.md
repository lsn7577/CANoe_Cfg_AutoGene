# OnMostMHPConnection

> Category: `MOST` | Type: `function`

## Syntax

```c
long OnMostMHPConnection(long sourceDevID, long destDevID, long fBlockID, long instID, long functionID, long opType)
```

## Description

The event procedure is called up as soon as a MOST High connection version 2.2 or higher is terminated.

Within this event procedure the following functions are available

Indicates whether the connection was made up of Spy messages.Parameters:NoneReturns: 0: Comprised of node messages1: Comprised of Spy messages

Indicates the used MOST High Protocol version.Parameters:NoneReturns: 0: Version 2.11: Version 2.2

Indicates the number of negative frame acknowledge messages.Parameter:NoneReturns: Number of NegAcks (see MHP specification)

Indicates the number of single or multiple frame request messages.Parameter:NoneReturns: Number of (multiple) frame requests

Indicates the number of block request messages.Parameter:NoneReturns: Number of block requests

Indicates the number of MHP observer warnings. Warnings may indicate communication problems.Parameter:NoneReturns: Number of Observer warnings

Indicates the number of MHP Observer errors. Errors indicate MOST High Protocol violations.Parameter:NoneReturns: Number of Observer errors

Indicates the number of connections transmitted during the MHP connection.Parameter:NoneReturns: Number of packets

The functions mostEventChannel(), mostEventTime() and mostEventTimeNS() can be used to call up supplemental information.

## Return Values

The return value determines whether the MHP connection event is relayed to the next function block in the Measurement Setup (e.g. a Trace Window).

## Availability

| Since Version |
|---|
