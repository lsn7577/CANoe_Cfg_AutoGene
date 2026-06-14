# on J1587ErrorMessage

> Category: `J1587` | Type: `event`

## Description

Defines the event handler for an erroneous J1708 message. The error code is contained in J1587ErrorMessage::J1587_Error.

For passing this message to other node, output(this) must be called inside the event handler.

## Example

```c
on J1587ErrorMessage 50 //50 is Sender MID, can be dbNode name or MID
{
  write (“Msg with ErrorCode %d received, MID %d”, this.J1587_MID,
  this.J1587_Error);
}
```

## Availability

| Since Version |
|---|
