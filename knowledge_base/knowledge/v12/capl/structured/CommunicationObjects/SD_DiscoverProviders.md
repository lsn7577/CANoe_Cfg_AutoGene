# SD_DiscoverProviders

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SD_DiscoverProviders(serviceConsumerRef * consumer)
```

## Description

Starts service discovery by requesting over the network to be informed of all running providers of a service. You can react to the response(s) with an on SD_provider_discovered handler.

## Return Values

—

## Example

```c
SD_DiscoverProviders(MirrorAdjustment[CANoe]);
```

## Availability

| Since Version |
|---|
