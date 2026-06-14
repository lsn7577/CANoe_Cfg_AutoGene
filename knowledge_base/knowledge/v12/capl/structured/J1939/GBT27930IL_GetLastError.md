# GBT27930IL_GetLastError

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_GetLastError(); // form 1
```

## Description

Gets the return value of the last called GBT27930 IL function.

## Example

```c
on key 't'
{
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  GBT27930IL_SetSignalRaw( EEC1::EngSpeed, 6, data );
  write( "Errorcode = %d", GBT27930IL_GetLastError() );
}
```

## Availability

| Since Version |
|---|
