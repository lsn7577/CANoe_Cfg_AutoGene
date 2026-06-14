# Iso11783IL_GetLastError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_GetLastError();
```

## Description

Gets the return value of the last called ISO11783 IL function.

## Example

```c
on key 't'
{
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  ISO11783ILSetSignalRaw( EEC1::EngSpeed, 6, data );
  write( "Errorcode = %d", Iso11783IL_GetLastError() );
}
```

## Availability

| Since Version |
|---|
