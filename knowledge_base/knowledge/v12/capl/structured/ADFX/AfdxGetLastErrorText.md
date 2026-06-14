# AfdxGetLastErrorText

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetLastErrorText( dword bufSize, char[] buffer );
```

## Description

Gets the error code description of the last called Afdx... function.

## Return Values

number of copied bytes

## Example

```c
char error[100];
long value;
long packetHandle;

value = AfdxGetTokenInt( packetHandle, "eth", "type" );
if (AfdxGetLastError() == 0)
{
  write("Ethernet Type is 0x%x", value );
}
else
{
 AfdxGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Since Version |
|---|
