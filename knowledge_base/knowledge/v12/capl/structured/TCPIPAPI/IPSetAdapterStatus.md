# IPSetAdapterStatus

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IPSetAdapterStatus( dword ifIndex, dword status);
```

## Description

With this function it is possible to activate or deactivate a network adapter of the TCP/IP stack.

When the adapter is set down all IP addresses of this adapter will be removed and sending or receiving packets on this adapter will be stopped.

If the default gateway was configured in a network which was configured on this adapter it will also be removed.

When the adapter is set up again the addresses configured in the TCP/IP Stack dialog will be reconfigured and the default gateway is set again.

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
