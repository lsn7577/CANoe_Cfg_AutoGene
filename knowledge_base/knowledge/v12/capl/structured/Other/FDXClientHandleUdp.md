# FDXClientHandleUdp

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXClientHandleUdp(dword ipv4Address, dword port); // form 1
```

## Description

This function creates an FDX client handle for the FDX client with the specified address.

Prerequisite for the function is to configure UPD/IPv4 or UDP/IPv6 as transport layer for the FDX feature.

## Return Values

If successful, the function returns a value greater than 0, which means the FDX client handle. Values smaller than or equal to zero indicate an error.

## Example

```c
long  fdxClientHandle = 0;
dword fdxClientPort = 0;
byte  fdxClientAddr[16];

IpGetAddressAsArray("::1", fdxClientAddr);
fdxClientPort = 2820;
fdxClientHandle = FDXClientHandleUdp(fdxClientAddr, fdxClientPort);
```

## Availability

| Since Version |
|---|
