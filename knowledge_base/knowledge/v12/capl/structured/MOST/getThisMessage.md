# getThisMessage

> Category: `MOST` | Type: `function`

## Syntax

```c
GetThisMessage(mostAMSMessage msg, long count);
```

## Description

Copies the data of a AMS message into the msg variable.

This function must be used exclusively within a an event procedure on mostAMSMessage.

## Return Values

—

## Example

The following program section copies 1000 bytes of a message's useful data to the local variable msg on Channel 1. Afterwards the contents of byte 500 are output to the Write Window.

```c
on mostAMSMessage MsgChannel1.*
{
   mostAMSMessage * msg = { DLC = 1000 };
   GetThisMessage(msg, 1000);
   write(“Byte 500: %02X”, msg.byte(500));
}
```

## Availability

| Since Version |
|---|
