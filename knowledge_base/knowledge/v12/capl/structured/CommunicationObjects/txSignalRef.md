# txSignalRef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
txSignalRef * <var>
```

## Description

References a tx signal endpoint (from where the signal is sent).

## Example

```c
txSignalRef long signal1;
signal1 = StatusSignal.senderSide[CANoe];
$signal = newValue;
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the endpoint | char[] | Read only |
| Path Full path of the endpoint (including namespaces) | char[] | Read only |
| SenderIndex Index of the sender. Note that the index may change if senders are added or removed. | dword | Read only |
| ReceiverIndex Index of the receiver (only if the PDU is not a broadcast PDU). Note that the index may change if receivers are added or removed. | dword | Read only |
