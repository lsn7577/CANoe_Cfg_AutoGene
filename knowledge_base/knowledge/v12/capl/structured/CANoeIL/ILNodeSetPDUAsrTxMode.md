# ILNodeSetPDUAsrTxMode

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeSetPDUAsrTxMode (dbMessage, long mode, long disturbanceCount, long flags)
```

## Description

Overrides the current valid transmission mode of the PDU. The transmission mode can be False or True. The current transmission mode is defined by or-ing the current data filter condition value of all signal values of the PDU.

## Return Values

0: No error

## Availability

| Since Version |
|---|
