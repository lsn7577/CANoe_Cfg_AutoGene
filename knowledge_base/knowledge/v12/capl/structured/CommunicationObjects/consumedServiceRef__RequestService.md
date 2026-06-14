# consumedServiceRef::RequestService

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedServiceRef::RequestService()
```

## Description

Requests the usage of a specific service: for the specified consumer from the specified provider. If the service is requested, a (logical) connection to the provider will be created as soon as the provider is available for the consumer.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].RequestService();
```

## Availability

| Since Version |
|---|
