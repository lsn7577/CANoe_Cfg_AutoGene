# IP_Address::PrintAddressToString

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Address::PrintAddressToString(char ipAddr[]);
```

## Description

Converts the IP address to a character string.

## Return Values

0: Success

## Example

```c
on start
{
  IP_Address 192.168.1.1 addr;
  char addrStr[20];
  if (addr.PrintAddressToString( addrStr ) == 0)
  {
    write( "Address is %s", addrStr );
  }
}
```

## Availability

| Since Version |
|---|
