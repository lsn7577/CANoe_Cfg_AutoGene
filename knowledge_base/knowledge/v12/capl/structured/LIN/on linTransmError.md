# on linTransmError

> Category: `LIN` | Type: `event`

## Description

The event procedure on linTransmError is called when no Slave responded to a transmission request.

The keyword this and the selectors (see Option .LIN: linTransmError selectors) can be used to access the data of the event that has just been received.

## Example

Handle transmission error for a certain frame on channel 1:

```c
on linTransmError
{
if (this.MsgChannel == 1 && this.ID == 0x33) {
…
}
}
```

## Availability

| Since Version |
|---|

## Selectors

| linTransmError | ../Selectors/CAPLfunctionLINTransmError.htm |
|---|---|
