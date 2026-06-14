# rxSignalRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
rxSignalRef * <var>
```

## Description

References an rx signal endpoint (where the signal is received).

## Example

```c
rxSignalRef long signal1;
signal1 = StatusSignal.receiverSide[CANoe];
currentValue = $signal1;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the endpoint | char[] | Read only |
| Path Full path of the endpoint (including namespaces) | char[] | Read only |
| SenderIndex Index of the sender (only if the PDU is not a broadcast PDU). Note that the index may change if senders are added or removed. | dword | Read only |
| ReceiverIndex Index of the receiver. Note that the index may change if receivers are added or removed. | dword | Read only |
