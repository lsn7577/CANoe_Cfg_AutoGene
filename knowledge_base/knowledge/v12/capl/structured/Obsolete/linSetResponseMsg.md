# linSetResponseMsg

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSetResponseData(message msg);
```

## Description

Sets the response data for a transmit request. The LIN hardware is instructed to immediately respond to the transmit request with the same identifier as msg with the data bytes of msg.

When you use the first alternative of the syntax (see above), the checksum is automatically generated correctly.

When you use the second alternative of the syntax (see above), you can set any checksum.

If this function is called in the event procedure on preStart then the LIN hardware is configured so that the response is made to a suitable transmit request. During the measurement this method may only be called for transmit identifiers that were already configured in the event procedure on preStart or in the LIN database.

## Example

```c
message LinSlaveLeft sLinSlaveLeft;
sLinSlaveLeft.Angle = 50;
linSetResponseMsg(sLinSlaveLeft);
```

## Availability

| Up to Version |
|---|
