# Iso11783IL_GetLastErrorText

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_GetLastErrorText( dword bufferSize, char buffer[] );
```

## Description

Returns the result of the last called ISO11783 IL function as string.

## Example

```c
on key 't' 
{
  char error[64];
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  ISO11783ILSetSignalRaw( EEC1::EngSpeed, 6, data );

  Iso11783IL_GetLastErrorText( elCount(error), error );
  write( "Errorcode:  %s", error );
}
```

## Availability

| Since Version |
|---|
