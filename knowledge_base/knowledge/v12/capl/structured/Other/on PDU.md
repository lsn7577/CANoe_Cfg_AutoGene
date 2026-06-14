# on PDU

> Category: `Other` | Type: `event`

## Syntax

```c
on PDU <PDU name>;
```

## Description

This event procedure is called if the corresponding PDU is received of which the updated bit is set or undefined. For the event procedure of type * and [*] keyword this is an untyped PDU object. For all other event procedures keyword this is a typed PDU object.

The form on pdu * is also called for SOME/IP PDUs. Keyword this is an untyped PDU object. The data contains the SOME/IP header and payload. Security selectors are not available.

## Example

```c
on PDU *
{
  write( "on pdu: LongHeaderID %X length %d", this.LongHeaderID, this.PduLength );
}
```

## Availability

| Since Version |
|---|
