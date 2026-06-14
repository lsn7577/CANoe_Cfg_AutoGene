# consumedPduRef::AbstractIsPduRequested

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword consumedPDURef::AbstractIsPDURequested()
```

## Description

Returns whether the specified service PDU is currently requested (if abstract binding is used).

## Return Values

0: PDU is not currently requested

## Example

```c
val = MirrorAdjustment.consumerSide[CANoe,LeftMirror].StatusPDU.AbstractIsPDURequested();
```

## Availability

| Since Version |
|---|
