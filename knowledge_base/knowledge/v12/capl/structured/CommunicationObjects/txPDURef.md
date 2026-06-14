# txPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
txPDURef * <var>
```

## Description

References a tx PDU endpoint (from where the PDU is sent).

## Example

```c
txPduRef StatusPdu pdu1;
pdu1 = StatusPdu.senderSide[CANoe];
$pdu1.StatusSignal = newValue;
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
| <SignalName> Accesses the specified signal on the PDU. | <Data type of the signal> |  |
