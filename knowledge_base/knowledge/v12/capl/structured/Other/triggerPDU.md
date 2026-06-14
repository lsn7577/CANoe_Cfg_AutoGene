# triggerPDU

> Category: `Other` | Type: `function`

## Syntax

```c
void triggerPDU(pdu myPDU);
```

## Description

Triggers a PDU to be sent. If the PDU has an update bit it will be set. After the PDU was sent the update bit will be reset.

## Return Values

—

## Example

```c
on timer cyclic100ms
{
  PDU randomPDU myPDU;
  myPDU.signal1 = 10;
  myPDU.signal2 = 20;
  triggerPDU(myPDU);
}
```

## Availability

| Since Version |
|---|
