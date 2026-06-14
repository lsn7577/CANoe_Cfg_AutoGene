# RS232SetSignalLine

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232SetSignalLine( dword port, dword line, dword state )
```

## Description

Sets signal lines on serial port.

If you use hardware handshake, then this function may conflict with the automatic handshaking.

## Return Values

0: error
The error occurs if

## Availability

| Since Version |
|---|
