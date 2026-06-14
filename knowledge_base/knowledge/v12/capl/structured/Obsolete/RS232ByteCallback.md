# RS232ByteCallback

> Category: `Obsolete` | Type: `function`

## Syntax

```c
RS232ByteCallback( dword port, dword datum, dword note )
```

## Description

Callback handler for reception of data from serial ports.

Each node which implements this handler will receive data. The handler receives data from all opened ports (i.e. opened by CANoe/CANalyzer).

It is cumbersome and slower by design since it gets one byte time by time. Block handlers receive blocks of data at an instant of time.

## Return Values

0: error
The error occurs if no serial port has been opened.

## Example

```c
if ( 0!=RS232WriteByte(2,65) )
   write(“Written byte to port 2.”);
// port 2 may be connected with port 1
...
// at node which listens to port 1 is connected to port 2
RS232ByteCallback(dword port, dword datum, dword note)
{
   // receive value 65 with port==1
}
```

## Availability

| Up to Version |
|---|
