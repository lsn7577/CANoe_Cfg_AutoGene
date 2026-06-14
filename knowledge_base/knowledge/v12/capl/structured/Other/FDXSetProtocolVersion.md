# FDXSetProtocolVersion

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXSetProtocolVersion(long fdxClientHandle, byte majorVersion, byte minorVersion);
```

## Description

This function configures the version of the FDX protocol that should be used for the communication with the specified client.

With each received FDX datagram, CANoe automatically adapts to the protocol version from the received datagram. The function FDXSetProtocolVersion is therefore only relevant in the rare case that CANoe should send datagrams to an FDX client without having received a datagram from this client.

## Return Values

0: Successful function call

## Example

See also: Coupling of two CANoe Instances using the FDX Protocol

```c
// Configure FDX protocol version 1.2 for the given client
FDXSetProtocolVersion(fdxClientHandle, 1, 2);

// Configure FDX protocol version 2.0 for the given client
FDXSetProtocolVersion(fdxClientHandle, 2, 0);
```

## Availability

| Since Version |
|---|
