# KLine_SetUARTParameter

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetUARTParameter(dword dataBits, dword parity, dword stopBits);
```

## Description

Configures the way bytes are sent on K-Line, by setting the parameters the UART (universal asynchronous receiver/transmitter) uses.

## Return Values

On success 0, otherwise error code.

## Example

```c
KLine_CreateECURepresentation( gMsgChannel);
KLine_SetUARTParameter( 9, 1, 2); // 9 data bytes, odd parity, 2 stop bits => 13 bit/byte (including start bit)
```

## Availability

| Since Version |
|---|
