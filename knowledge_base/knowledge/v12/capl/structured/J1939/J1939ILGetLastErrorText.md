# J1939ILGetLastErrorText

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILGetLastErrorText(dword bufferSize, char buffer[] ); // form 1
```

## Description

Returns the result of the last called J1939 IL function as string.

## Example

```c
on key 't' 
{
  char error[64];
  BYTE date = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06 };
  J1939ILSetSignalRaw( EEC1::EngSpeed, 6, data );

 J1939ILGetLastErrorText( elCount(error), error );
  write( "Errorcode:  %s", error );
}
```

## Availability

| Since Version |
|---|
