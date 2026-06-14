# mostMsgSet

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgSet(mostAmsMessage * msg, long destAdr, char symbolicMessage[], long instId)
```

## Description

Populating an AMS message using the syntax from the MOST specification and the description in the XML function catalog.

PosDescription, TelLen and StreamCases are checked in addition to Funktionsblock, FunktionsID and OpType.

See also Option .MOST: Symbolic Identification of Messages

## Return Values

0: OK (Parameter is available)

## Availability

| Since Version |
|---|
