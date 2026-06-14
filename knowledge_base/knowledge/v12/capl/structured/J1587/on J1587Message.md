# on J1587Message

> Category: `J1587` | Type: `event`

## Description

Defines the event handler for a valid J1708 message, the thispointer is of type J1587Message.

For passing this message to other node, output(this) must be called inside the event handler.

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  J1587Param 0 param;
  if (GetParameterByPID(this, 30, param) == 0)
  {
    output(this);
  }
}
```

## Availability

| Since Version |
|---|
