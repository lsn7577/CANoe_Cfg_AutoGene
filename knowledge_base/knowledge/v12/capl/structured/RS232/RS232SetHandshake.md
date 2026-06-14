# RS232SetHandshake

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232SetHandshake( dword port, dword handshake, dword XonLimit, dword XoffLimit, dword XonChar, dword XoffChar )
```

## Description

Sets handshake parameters on serial port.

If you use hardware handshake, then the functions which change signal lines directly (RS232SetSignalLine, RS232EscapeCommFunc, RS232EscapeCommExt) may conflict with the automatic handshaking.

## Return Values

0: error
The error occurs if

## Example

```c
if ( 0!=RS232SetHandshake(1,0,0,0,0,0) )
  write("No handshake at port 1.");
```

## Availability

| Since Version |
|---|
