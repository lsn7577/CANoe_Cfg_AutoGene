# Displaying and Entering Hexadecimal Values

> Category: `Panel` | Subcategory: `General` | Type: `concept`

Hexadecimal display is supported in the Input/Output Box and the Combo Box in the Panel Designer. The Input/Output Box also supports the entry of hexadecimal values.

Symbols can be displayed and entered in hexadecimal format if their raw or physical value is an integer.

The Combo Box can only display raw values.

## Displaying Raw Values in Hexadecimal Format

Depending on the symbol definition, integer values are filled to form full bytes and displayed hexadecimally. Leading zeros are not displayed in this case.

Example: Displaying Raw Values

3 bit, signed

-43

2

FC3

3 bit, unsigned

07

8 bit, signed

-128127

807F

8 bit, unsigned

0255

0FF

| Example: Displaying Raw Values Symbol definition Min/max values Symbol places (Hex) Value (Hex) 3 bit, signed -43 2 FC3 3 bit, unsigned 07 2 07 8 bit, signed -128127 2 807F 8 bit, unsigned 0255 2 0FF | Symbol definition | Min/max values | Symbol places (Hex) | Value (Hex) | 3 bit, signed | -43 | 2 | FC3 | 3 bit, unsigned | 07 | 2 | 07 | 8 bit, signed | -128127 | 2 | 807F | 8 bit, unsigned | 0255 | 2 | 0FF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Symbol definition | Min/max values | Symbol places (Hex) | Value (Hex) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 bit, signed | -43 | 2 | FC3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 bit, unsigned | 07 | 2 | 07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 bit, signed | -128127 | 2 | 807F |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 bit, unsigned | 0255 | 2 | 0FF |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Symbol definition | Min/max values | Symbol places (Hex) | Value (Hex) |
|---|---|---|---|
| 3 bit, signed | -43 | 2 | FC3 |
| 3 bit, unsigned | 07 | 2 | 07 |
| 8 bit, signed | -128127 | 2 | 807F |
| 8 bit, unsigned | 0255 | 2 | 0FF |

## Displaying Physical Values in Hexadecimal Format

Example: Symbol with Factor and Offset

8 bit symbol, signed, with Factor = 2 and Offset = -100

The physical value range is -356..154.Even though the symbol consists of only one byte, two bytes are needed for the display.

-128

80

-356

FE9C

-1

FF

-102

FF9A

100

64

127

7F

154

9A

| Example: Symbol with Factor and Offset 8 bit symbol, signed, with Factor = 2 and Offset = -100 The physical value range is -356..154.Even though the symbol consists of only one byte, two bytes are needed for the display. Raw value (decimal) Raw value (Hex) Physical value (decimal) Physical value (Hex) -128 80 -356 FE9C -1 FF -102 FF9A 100 64 100 64 127 7F 154 9A | Raw value (decimal) | Raw value (Hex) | Physical value (decimal) | Physical value (Hex) | -128 | 80 | -356 | FE9C | -1 | FF | -102 | FF9A | 100 | 64 | 100 | 64 | 127 | 7F | 154 | 9A |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raw value (decimal) | Raw value (Hex) | Physical value (decimal) | Physical value (Hex) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -128 | 80 | -356 | FE9C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1 | FF | -102 | FF9A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | 64 | 100 | 64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 127 | 7F | 154 | 9A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Raw value (decimal) | Raw value (Hex) | Physical value (decimal) | Physical value (Hex) |
|---|---|---|---|
| -128 | 80 | -356 | FE9C |
| -1 | FF | -102 | FF9A |
| 100 | 64 | 100 | 64 |
| 127 | 7F | 154 | 9A |

## Tooltips

Tooltips help users interpret the data on the panel. For detailed information see CANalyzer help page Panel Configuration: Settings.

## Limitations
