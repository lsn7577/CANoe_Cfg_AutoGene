# IpGetAdapterGateway

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterGateway( dword ifIndex, dword& ipv4address); // form 1
```

## Description

The function retrieves the default gateway address associated with the specified network interface.

Gateway information is not yet available before the start of the measurement (on pre-start). Rather it is first available at the start of the measurement (on start) as soon as the stack has been completely initialized.

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  long ifIdx;
  for( ifIdx = 1; ifIdx <= ipGetAdapterCount(); ifIdx++)
  {
    ip_Address gatewayAddress;
    if (ipGetAdapterGateway( ifIdx, 0, gatewayAddress ) == 0)
    {
      char gatewayStr[30];
      gatewayAddress.PrintAddressToString( gatewayStr );
      write( "%d. Adapter Gateway Address: %s", ifIdx, gatewayStr );
    }
  }
}
```

## Availability

| Since Version |
|---|
