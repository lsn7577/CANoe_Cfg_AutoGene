# on J1587Param

> Category: `J1587` | Type: `event`

## Description

Defines the event handler for a valid J1587 parameter, the this pointer is of type J1587Param.

## Example

```c
on J1587Param TextMessageAcknowledged
{
  if (this.MID == gECU_MID)
  {
    if (this.MessageDisplayed == 1)
    {
      gDisplayState = kDisplayed;
    }
    else
    {
      gDisplayState = kTimeout;
    }
  }
}
```

## Availability

| Since Version |
|---|
