# J1939ILGetLastError

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILGetLastError(); // form 1
```

## Description

Gets the return value of the last called J1939 IL function.

## Example

```c
on key 't'
{
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  J1939ILSetSignalRaw( EEC1::EngSpeed, 6, data );
  write( "Errorcode = %d", J1939ILGetLastError() );
}
```

## Availability

| Since Version |
|---|
