# linSetResponseData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSetResponseData(int sendId, int dataLength, byte data[]);
```

## Description

Sets the response data for a transmit request. The LIN hardware is instructed to respond from now on to the transmit request sendID with the data data. The used data length code is passed in dlc.

DLC value range: 0…8 (bytes)When you use the first alternative of the syntax (see above), the checksum is automatically generated correctly. When you use the second alternative of the syntax (see above), you can set any checksum. If this function is called in the event procedure on preStart then the LIN hardware is configured so that the response is made to a suitable transmit request. During the measurement this method may only be called for transmit identifiers that were already configured in the event procedure on preStart or in the LIN database.

## Return Values

If a DLC has been set, a value unequal "0" will be returned.

## Availability

| Up to Version |
|---|
