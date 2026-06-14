# serviceConsumerRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
serviceConsumerRef * <var>
```

## Description

References a service consumer endpoint.

## Example

```c
serviceConsumerRef MirrorAdjustment svc1;
svc1 = MirrorAdjustment.consumerSide[CANoe];
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the consumer endpoint | char[] | Read only |
| Path Full path of the consumer endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if consumers are added or removed. | dword | Read only |
| Address Generalized address of the endpoint. Can be used with binding-specific API like Abstract_GetDisplayName to retrieve information. | AddressHandle | Read only |
| Abstract_GetDisplayName | ../Functions/CAPLfunctionAbstractGetDisplayName.htm |  |
