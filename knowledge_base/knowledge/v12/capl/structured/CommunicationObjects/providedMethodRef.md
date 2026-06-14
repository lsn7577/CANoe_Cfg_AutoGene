# providedMethodRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedMethodRef * <var>
```

## Description

References a provided method endpoint, which means a specific combination of consumer and provider for a service function on provider side.

## Example

```c
providedMethodRef MirrorAdjustment.Adjust method1;
method1 = MirrorAdjustment.providerSide[CANoe,LeftMirror].Adjust;
$method1.AutoAnswerTimeNS = ADJUST_DEFAULT_ANSWER_TIME;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the provided endpoint | char[] | Read only |
| Path Full path of the provided endpoint (including namespaces) | char[] | Read only |
| ConsumerIndex Index of the consumer. Note that the index may change if consumers are added or removed. | dword | Read only |
| ProviderIndex Index of the provider. Note that the index may change if providers are added or removed. | dword | Read only |
| LatestCall Information about the latest call received at this endpoint. | struct | Read only |
| LatestReturn Information about the latest return sent from this endpoint. | struct | Read only |
| ParamDefaults Default values for automatic return of the function for the out parameters. | struct | Read only |
| DefaultResult Default value for automatic return of the function for the return value. | <Data Type of the function return value> |  |
| AutoAnswerMode Mode for automatic answering function calls: Auto: calls are answered with the default values OffOrManual: calls are not automatically answered Discard: calls are discarded and will not be answered AutoField: only for field getters and setters; use the field value to answer the call. | enum |  |
| AutoAnswerTimeNS Time in nonoseconds until the call is answered if the AutoAnswerMode is Auto or AutoField. | int64 |  |
