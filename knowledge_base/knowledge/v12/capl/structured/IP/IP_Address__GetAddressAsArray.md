# IP_Address::GetAddressAsArray

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::GetAddressAsArray(byte ipAddr[]); // form 1
```

## Description

Copies the current IP address to the byte array whereas the byte array's size needs to fit the current IP address value.

## Return Values

0: Success

## Example

```c
on start
{
  IP_Address FC00::0001 addr;
  byte addrData[16];

  if(addr.SetAddressAsArray( addrData ) == 0)
  {
    // do something with addrData
  }
}
```

## Availability

| Since Version |
|---|
