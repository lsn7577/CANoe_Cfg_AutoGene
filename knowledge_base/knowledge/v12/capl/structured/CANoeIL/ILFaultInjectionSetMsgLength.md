# ILFaultInjectionSetMsgLength

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
ILFaultInjectionSetMsgLength(dbMessage msg, dword msgLength)
```

## Description

Assigns a new message length (in bytes) to the message. To set the message length back to its original value, use ILFaultInjectionResetMsgLength.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
