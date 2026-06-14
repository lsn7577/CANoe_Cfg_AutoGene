# FDXSetByteOrder

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXSetByteOrder(long fdxClientHandle, long byteOrder);
```

## Description

This function configures the byte order of the FDX protocol that should be used for the communication with the specified client. The default is Little Endian.

With each received FDX datagram, CANoe automatically takes over the byte order from the datagram for the further communication with this client. The function FDXSetByteOrder is therefore only relevant in the rare case that CANoe should send datagrams to an FDX client without having received a datagram from this client.

## Return Values

0: Successful function call

## Availability

| Since Version |
|---|
