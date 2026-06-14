# linGetHWTransmitAccuracy

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetHWTransmitAccuracy()
```

## Description

This function can be used to query the transmit resolution of the LIN hardware in units of 1 Hz.

## Return Values

Returns the transmit resolution of the LIN hardware.

## Example

```c
on key 't'
{
write("Transmit accuracy = %d", linGetHWTransmitAccuracy());
write("Receive  accuracy = %d", linGetHWReceiveAccuracy());
}
```

## Availability

| Since Version |
|---|
