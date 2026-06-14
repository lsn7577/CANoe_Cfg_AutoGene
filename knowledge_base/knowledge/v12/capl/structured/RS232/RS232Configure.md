# RS232Configure

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Configure( dword port, dword baudrate, dword numberOfDataBits, dword numberOfStopBits, dword parity ); // form 1
```

## Description

Configures a serial port.

Without setting up a configuration explicitly, the default configuration is used.

Default baud rate: 9600, 8 data bits, 1 stop bit, no parity.

If a deprecated INI file exists, the data of the INI file will be used.

With form 2 of this function you can configure a serial port to use parity without letting the operating system verify parity correctness. This form should only be used if the communication to a device was not possible when using parity and form 1 of this function.

## Return Values

0: error
The error occurs if

## Example

```c
if ( 0!=RS232Configure(1,9600,8,1,0) )
   write(“Set typical default at port 1.”);
```

## Availability

| Since Version |
|---|
