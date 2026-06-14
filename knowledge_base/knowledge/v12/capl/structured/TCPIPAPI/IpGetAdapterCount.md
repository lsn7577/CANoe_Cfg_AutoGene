# IpGetAdapterCount

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
dword IpGetAdapterCount();
```

## Description

The function returns the number of network interfaces for the local computer, not including the loopback interface.

All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack.

## Return Values

The number of network interfaces.

## Availability

| Since Version |
|---|
