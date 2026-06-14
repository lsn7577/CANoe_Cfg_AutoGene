# RS232Open

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Open( dword port )
```

## Description

Opens a serial port.

The serial port is available on exactly the node which executed the CAPL code. One and the same port may be opened by several nodes. If the port has been opened, other programs cannot access the serial port any more.

## Return Values

0: error
The error occurs if

## Example

```c
if ( 1==RS232Open(1) ) write(“It works with port 1.”);
```

## Availability

| Since Version |
|---|
