# consumedServiceRef::ReleaseService

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
int consumedServiceRef::ReleaseService()
```

## Description

Releases the usage of a specific service: for the specified consumer from the specified provider. If the service is released, the (logical) connection to the provider will be cut and not be reestablished automatically. Without the connection, the service can’t be used by the consumer.

## Return Values

0: Success

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].ReleaseService();
```

## Availability

| Since Version |
|---|
