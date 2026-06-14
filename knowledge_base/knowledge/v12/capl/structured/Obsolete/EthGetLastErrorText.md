# EthGetLastErrorText

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetLastErrorText( dword bufferSize, char[] buffer );
```

## Description

Gets the error code description of the last called Eth... function.

## Return Values

number of copied bytes

## Example

```c
CHAR error[100];
LONG value;
LONG packetHandle;

value = EthGetTokenInt( packetHandle, "eth", "type" );
if (EthGetLastError() == 0)
{
  write("Ethernet Type is 0x%x", value );
}
else
{
  EthGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Up to Version |
|---|
