# frSetSendPDU

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetSendPDU( <PDU object> );
```

## Description

Configures the hardware to transmit the specified PDU.

All relevant slots are submitted for transmission.

This submission must take place in the On preStart routine in the transmit branch.

If a frPDU object was created using frPDU, it can be submitted for transmission with this function.

## Return Values

—

## Availability

| Since Version |
|---|
