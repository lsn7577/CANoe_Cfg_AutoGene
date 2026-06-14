# GetFrFrame

> Category: `Other` | Type: `function`

## Syntax

```c
long GetFrFrame(this, FrFrame * frame);
```

## Description

This function can only be called inside of an on PDU handler. The function will return in its second parameter the FlexRay frame, the PDU was contained.

## Return Values

0: Data access successful.

## Example

```c
on PDU PDU_C
{
  FrFrame (1,0,1) aFrFrame_01;
  long result;
  result = GetFrFrame(this, aFrFrame_01); // PDU is assumed to be sent on FlexRay
  if (result == 0)
  {
    write("Received PDU 'PDU_C' in FlexRay Slot %lu", aFrFrame_01.FR_SlotID);
  }
  else
  {
    write("Error accessing PDU!");
  }
}
```

## Availability

| Since Version |
|---|
