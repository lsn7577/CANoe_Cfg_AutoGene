# SCC_LoadCommunicationConfig

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_LoadCommunicationConfig ( long ConfigID )
```

## Description

Loads the section within the XML configuration file designated with configID. If SCC_LoadCommunicationConfig has not yet been called when the simulation starts, section 0 is loaded automatically.

The function SCC_LoadCommunicationConfig loads the configuration globally, i.e. for all connections to be created. This call is only possible when simulation is deactivated.

The function SCC_LoadV2GConfig loads the configuration for an already active connection, applying only those parameters relevant to an individual connection. This function can only be used within a callback; the configuration is then applied to the connection that has triggered the callback.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
