# mostPrepareReport

> Category: `MOST` | Type: `function`

## Syntax

```c
mostPrepareReport(mostAmsMessage * msgCommand, mostAmsMessage * msgReport)
```

## Description

Preparation of an AMS message as response (OpType>=9) to a received command message (OpType<9).

The destination address of the report message is set to the source address of the command message. The parameters FBlockId, InstId and FunctionId in msgReport are set as given by the msgCommand. Any wildcard InstId in msgCommand is transferred to a concrete value in msgReport with the help of the device’s Local FBlock list.

According to the MOST specification, the OpTypes are converted by the command into the associated report OpType:

Command OpType

Report OpType

GetInterface

Interface

any other

Status

Start, StartResult

Result

Abort

Error

StartAck, StartResultAck

ResultAck

AbortAck

ErrorAck

Messages with Ack-OpTypes contain a sender handle in the first two data bytes. This sender handle is also set in the first two data bytes of the report message.

## Return Values

—

## Availability

| Since Version |
|---|
