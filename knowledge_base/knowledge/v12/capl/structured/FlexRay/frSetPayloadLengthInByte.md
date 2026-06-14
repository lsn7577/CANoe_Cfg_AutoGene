# frSetPayloadLengthInByte

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frSetPayloadLengthInByte( <frame var>, dword <dlc> );
```

## Description

This function sets the payload (data length) of the object in bytes. In the event of an uneven value, the length of the buffer will be set to the next even value.

The payload length can also be set using the FR_PayloadLength frame variables selector. However, in this case, the length is set in 16-bit words.

The data length can only be manipulated for frames sent in the dynamic segment!

## Return Values

—

## Availability

| Since Version |
|---|
