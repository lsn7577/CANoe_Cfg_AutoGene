# IP_Address::SetAddressAsArray

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::SetAddressAsArray(byte ipAddr[]); // form 1
```

## Description

Copies the byte array to the IP address value.

## Return Values

0: Success

## Example

```c
on start
{
  byte addrData[16] = { 0xFC, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01 };
  IP_Address addr;

  if(addr.SetAddressAsArray( addrData ) == 0)
  {
    // do something with addrData
  }
}
```

## Availability

| Since Version |
|---|
