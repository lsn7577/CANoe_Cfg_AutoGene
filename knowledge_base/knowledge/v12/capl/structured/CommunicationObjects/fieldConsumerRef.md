# fieldConsumerRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
fieldConsumerRef * <var>
```

## Description

References a field consumer endpoint.

## Example

```c
fieldConsumerRef long field1;
field1 = MirrorAdjustment.consumerSide[LeftMirror].CurrentPosition;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the consumer endpoint | char[] | Read only |
| Path Full path of the consumer endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if providers are added or removed. | dword | Read only |
| ServiceConsumer Reference to the consumer of the service containing the field. | serviceConsumerRef* | Read only |
