# rxPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
rxPDURef * <var>
```

## Description

References an rx PDU endpoint (where the PDU is received).

## Example

```c
rxPduRef StatusPdu pdu1;
pdu1 = StatusPdu.receiverSide[CANoe];
currentValue = $pdu1.StatusSignal;
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
| <SignalName> Accesses the specified signal on the PDU. | <Data type of the signal> |  |
