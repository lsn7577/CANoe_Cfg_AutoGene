# PDU

> Category: `Other` | Type: `function`

## Syntax

```c
PDU short <AUTOSAR short header ID> <PDU var>
```

## Description

Can be used to create a PDU object. The object data can be manipulated via the object's selectors. Additional object properties can be read from the selectors.

A PDU object can be sent using the TriggerPDU function.

## Example

```c
on PDU CAN_1::SOMEPDU1
{
  PDU CAN_2::SOMEPDU1 mypdu2;
  mypdu2.Payload = this.Payload;
  triggerPDU(mypdu2);
}
```

## Availability

| Since Version |
|---|

## Selectors

| Bus type | ../../../Shared/CAPL/General/EnumerationTypes.htm |
|---|---|
