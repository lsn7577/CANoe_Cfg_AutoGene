# AfdxGetLastError

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetLastError( void );
```

## Description

Returns the error code of the last called Afdx… function.

## Return Values

error code

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
