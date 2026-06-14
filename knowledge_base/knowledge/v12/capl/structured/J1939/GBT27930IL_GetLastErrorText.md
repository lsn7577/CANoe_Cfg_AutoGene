# GBT27930IL_GetLastErrorText

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_GetLastErrorText(dword bufferSize, char buffer[] ); // form 1
```

## Description

Returns the result of the last called GBT27930 IL function as string.

## Example

```c
on key 't' 
{
  char error[64];
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  GBT27930IL_SetSignalRaw( EEC1::EngSpeed, 6, data );

 GBT27930IL_GetLastErrorText( elCount(error), error );
  write( "Errorcode:  %s", error );
}
```

## Availability

| Since Version |
|---|
