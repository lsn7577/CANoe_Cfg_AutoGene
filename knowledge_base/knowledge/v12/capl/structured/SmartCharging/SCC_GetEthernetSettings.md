# SCC_GetEthernetSettings

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetEthernetSettings(byte MacAddress[], byte IPv4Address[], dword& IPv4Available, byte IPv6Address[], dword& IPv6Available, long UDPPort, long TCPPort)
```

## Description

Retrieves the configured addresses and ports for the SCC node. These values may originate from the CANoe configuration or from the DLL’s XML configuration

## Return Values

—

## Availability

| Since Version |
|---|
