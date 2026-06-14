# SCC_GetPreparedEXIMessage

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetPreparedEXIMessage ( byte data[], dword& dataLength ) // form 1
```

## Description

Finalizes a message without sending. The message data is returned to an output buffer instead. Usually this data consists of the V2G header and the EXI encoded V2G payload.

## Return Values

The Id attribute of the message body, if existing (to the output buffer)

## Availability

| Since Version |
|---|
