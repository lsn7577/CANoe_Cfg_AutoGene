# FSIL_SetMsgRawData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetMsgRawData( dbMessage msg, long dataSize, byte data[] );
```

## Description

Sets the data bytes of the message. The length of the parameter group is adjusted to size of parameter dataSize.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
