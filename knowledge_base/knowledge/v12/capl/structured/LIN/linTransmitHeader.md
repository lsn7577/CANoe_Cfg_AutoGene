# linTransmitHeader

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linTransmitHeader(dword frameId); // form 1
```

## Description

Transmits a frame header for a specific LIN frame.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

Returns 1 if the transmission succeeded, otherwise 0.

## Example

```c
// Transmit a LIN header with the id 0x01

linFrame 0x01 frm1;
linTransmitHeader(frm1);
```

## Availability

| Since Version |
|---|
