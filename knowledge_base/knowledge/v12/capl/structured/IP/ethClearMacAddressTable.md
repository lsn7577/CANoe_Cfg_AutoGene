# ethClearMacAddressTable

> Category: `IP` | Type: `function`

## Syntax

```c
long ethClearMacAddressTable( long channel);
```

## Description

Clears the MAC address table of the Ethernet network interface.

The function can only be used with Vector network interface (i.e. VN5640) in operation mode which manages a MAC address table, i.e. Ethernet switch.

## Return Values

0: Success

## Example

```c
on '1'
{
  EthClearMacAddressTable( 1 ); // clear table on Eth 1
}
```

## Availability

| Since Version |
|---|
