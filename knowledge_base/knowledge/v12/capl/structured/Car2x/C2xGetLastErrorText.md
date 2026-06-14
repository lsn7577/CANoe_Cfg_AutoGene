# C2xGetLastErrorText

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetLastErrorText( dword bufferSize, char[] buffer );
```

## Description

Gets the error code description of the last called C2x... function.

## Return Values

Number of copied bytes.

## Example

```c
char error[100];
long value;
long packetHandle;

value = C2xGetTokenInt( packetHandle, "eth", "type" );
if (C2xGetLastError() == 0)
{
  write("Ethernet Type is 0x%x", value );
}
else
{
  C2xGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Since Version |
|---|
