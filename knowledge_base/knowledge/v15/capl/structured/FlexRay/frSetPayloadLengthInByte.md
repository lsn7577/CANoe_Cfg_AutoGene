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

## Parameters

| Name | Description |
|---|---|
| <frame var> | Name of the variable referenced by the frame object. The variable name was defined when the object was created using frFrame. |
| <dlc> | Defines the payload (data length) in bytes. |

## Return Values

—

## Example

For an example see function frUpdateStatFrame.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
