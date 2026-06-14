# measuredPDURef

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
measuredPDURef * <var>
```

## Description

References a PDU measurement point, which means measuring a specific connection between sender and receiver for a PDU.

Not used for service PDUs, the data type of these is measuredServicePDURef.

## Example

```c
measuredPDURef StatusPDU pdu1;
pdu1 = StatusPDU.measure[LeftMirror,CANoe];
write("Latest x: %d", $pdu1.Position.x);
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| Name Name of the measurement endpoint | char[] | Read only |
| Path Full path of the measurement endpoint (including namespaces) | char[] | Read only |
| SenderIndex Index of the sender. Note that the index may change if senders are added or removed. | dword | Read only |
| ReceiverIndex Index of the receiver. Note that the index may change if receivers are added or removed. | dword | Read only |
