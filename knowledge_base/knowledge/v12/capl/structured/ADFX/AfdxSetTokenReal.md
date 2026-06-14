# AfdxSetTokenReal

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenReal( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, float value );
```

## Description

This function sets the specified token‘s data as a float value.

## Return Values

0 or error code

## Example

```c
{
  // have  a packet handle <packet> created already
  long err = 0;
  err = AfdxSetTokenReal( packet, "udp", "data", 8, 8, 1.234);
}
```

## Availability

| Since Version |
|---|
