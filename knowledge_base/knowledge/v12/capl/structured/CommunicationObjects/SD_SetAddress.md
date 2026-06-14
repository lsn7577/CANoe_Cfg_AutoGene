# SD_SetAddress

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long SD_SetAddress(serviceConsumerRef * consumer, addressHandle address, serviceConsumerRef * simulatedEndpoint)
```

## Description

Sets the address for an endpoint, normally after it has been added dynamically to a service. The address can be created with binding specific functions. The third parameter is the simulated endpoint where the new endpoint has been discovered and where the address for the new endpoint is now known.

## Return Values

0: Success

## Example

```c
SD_SetAddress(newProvider, Abstract_CreateAddress(MirrorAdjustment, "RearMirror"), MirrorAdjustment[CANoe]);
```

## Availability

| Since Version |
|---|
