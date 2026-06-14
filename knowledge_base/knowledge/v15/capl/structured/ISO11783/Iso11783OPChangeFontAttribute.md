# Iso11783OPChangeFontAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeFontAttribute( dword ecuHandle, dword objectID, dword color, dword size, dword type, dword style );
```

## Description

The function changes the properties of a font attribute object. A Change Font Attribute command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of the font attribute object |
| color | Color index |
| size | Size of the font: 0: 6x8 1: 8x8 2: 8x12 3: 12x16 4: 16x16 5: 16x24 6: 24x32 7: 32x32 8: 32x48 9: 48x64 10: 64x64 11: 64x96 12: 96x128 13: 128x128 14: 128x192 |
| type | Font type: 0: ISO8859-1 (ISO Latin 1) 1: ISO8859-15 (ISO Latin 9) 2: ISO8859-2 (ISO Latin 2) |
| style | Font style: Bit 0: 1 Bold Bit 1: 1 Crossed out Bit 2: 1 Underlined Bit 3: 1 Italic Bit 4: 1 Inverted Bit 5: 1 Flashing |

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeFontAttribute( handle, 1100, 10, 3, 0, 0x01 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
