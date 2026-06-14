# OnIpAddressRemoved

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnIpAddressRemoved(dword ifIndex, ip_address address, dword prefix, dword origin);
```

## Description

If the CAPL program implements this callback it is called when a address gets removed from a network interface.

The callback is only available for simulation nodes using the individual TCP/IP stack instance. Check this setting in the TCP/IP Stack configuration dialog.

## Return Values

—

## Example

```c
void OnIpAddressRemoved(dword ifIndex, ip_Address address, dword prefix, dword origin)
{
  char addrString[50];
  char originNames[6][25] = {"ORIGIN_UNKNOWN", "ORIGIN_USER", "ORIGIN_SYSTEM", "ORIGIN_DHCPv4CLIENT", "ORIGIN_DHCPv6CLIENT", "ORIGIN_RFC3927CLIENT"};
  address.PrintAddressToString(addrString);
  snprintf(addrString, elcount(addrString), "%s/%d", addrString, prefix);
  write("removed ip address: %s from adapter nr: %d. Origin: %s", addrString, ifIndex, originNames[origin]);
}
```

## Availability

| Since Version |
|---|
