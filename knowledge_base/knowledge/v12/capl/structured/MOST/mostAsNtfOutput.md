# mostAsNtfOutput

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfOutput(long destAdr, mostMessage msg)
```

## Description

destAdr != 0xFFFF:

The command sends the message to the stated address.

destAdr == 0xFFFF:

The message is sent to the address of all notification clients. The FBlockID, InstID and FunctionID values, which are needed to read the addresses from the notification matrix, are extracted from the message variable (msg).

## Return Values

See error codes

## Availability

| Since Version |
|---|
