# RS232OnError

> Category: `RS232` | Type: `function`

## Syntax

```c
RS232OnError( dword port, dword errorFlags )
```

## Description

Callback handler for reception of errors at a serial port.

Will be called only at the node which issued send/receive operations.

For repetitive errors (stable error condition) just the first one is returned. That case may happen for reception errors above all, i.e. at configuration mismatches of both connected ends.

It is possible that in case of configuration mismatches errors may not occur at once, e.g. a configuration of 9600/8/1/no parity at one port and 115200/8/1/no parity at the other end may seem to work (though rubbish is received).

## Return Values

—

## Example

```c
RS232OnError(dword port, dword errorFlags)
{
   if ( errorFlags & 1 )
      writeLineEx(0,3,“send failed”);
   if ( errorFlags & 2 )
      writeLineEx(0,3,“receive failed”);
}
```

## Availability

| Since Version |
|---|
