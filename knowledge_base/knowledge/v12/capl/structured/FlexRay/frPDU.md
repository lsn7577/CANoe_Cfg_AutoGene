# frPDU

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frPDU <FIBEX PDU name> <PDU var>;
```

## Description

This can be used to create a FlexRay PDU object. The object data can be manipulated via the object's selectors. Additional object properties can be read from the selectors.

The object is then registered using the frSetSendPDU and transmitted using the frUpdatePDU functions.

## Example

This is an example for using the PDU object in arrays.

All objects of an array must be initialized with an appropriate PDU definition!

```c
variables
{
  frPDU EngineData pdu1;

  // All objects are equal:
   frPDU EngineData frPDUArray1[10];

  // All objects may be different:
  frPDU * frPDUArray2[2] = { EngineStatus, pdu1 };
}
```

## Availability

| Since Version |
|---|
