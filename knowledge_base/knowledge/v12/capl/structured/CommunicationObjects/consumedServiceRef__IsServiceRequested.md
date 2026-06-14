# consumedServiceRef::IsServiceRequested

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword consumedServiceRef::IsServiceRequested()
```

## Description

Returns whether the service is currently requested by the consumer.

## Return Values

0: Service is not currently requested

## Example

```c
val = MirrorAdjustment.consumerSide[CANoe,LeftMirror].IsServiceRequested();
```

## Availability

| Since Version |
|---|
