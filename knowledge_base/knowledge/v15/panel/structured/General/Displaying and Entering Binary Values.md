# Displaying and Entering Binary Values

> Category: `Panel` | Subcategory: `General` | Type: `concept`

Binary display is supported in the Input/Output Box and the Combo Box in the Panel Designer. The Input/Output Box also supports the entry of binary values.

Symbols can be displayed and entered in binary format if their raw or physical value is an integer.

The Combo Box can only display raw values.

## Displaying Raw Values in Binary Format

Depending on the symbol definition, integer values are displayed binary. Leading zeros are not displayed in this case.

Example: Displaying Raw Values

3 Bit, signed

-43

3

10011

3 Bit, unsigned

07

0111

8 Bit, signed

-128127

8

100000001111111

8 Bit, unsigned

0255

011111111

| Example: Displaying Raw Values Symbol definition Min/Max values Symbol places (Bin) Values (Bin) 3 Bit, signed -43 3 10011 3 Bit, unsigned 07 3 0111 8 Bit, signed -128127 8 100000001111111 8 Bit, unsigned 0255 8 011111111 | Symbol definition | Min/Max values | Symbol places (Bin) | Values (Bin) | 3 Bit, signed | -43 | 3 | 10011 | 3 Bit, unsigned | 07 | 3 | 0111 | 8 Bit, signed | -128127 | 8 | 100000001111111 | 8 Bit, unsigned | 0255 | 8 | 011111111 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Symbol definition | Min/Max values | Symbol places (Bin) | Values (Bin) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 Bit, signed | -43 | 3 | 10011 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 Bit, unsigned | 07 | 3 | 0111 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 Bit, signed | -128127 | 8 | 100000001111111 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 Bit, unsigned | 0255 | 8 | 011111111 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Symbol definition | Min/Max values | Symbol places (Bin) | Values (Bin) |
|---|---|---|---|
| 3 Bit, signed | -43 | 3 | 10011 |
| 3 Bit, unsigned | 07 | 3 | 0111 |
| 8 Bit, signed | -128127 | 8 | 100000001111111 |
| 8 Bit, unsigned | 0255 | 8 | 011111111 |

## Displaying Physical Values in Binary Format

Example: Symbol with Factor and Offset

8 bit symbol, signed, with Factor = 2 and Offset = -100

The physical value range is -356..154.Even though the symbol consists of only one byte, two bytes are needed for the display.

-128

1000 0000

-356

11111110 10011100

-1

1111 1111

-102

11111111 10011010

100

0110 0100

01100100

127

0111 1111

154

10011010

| Example: Symbol with Factor and Offset 8 bit symbol, signed, with Factor = 2 and Offset = -100 The physical value range is -356..154.Even though the symbol consists of only one byte, two bytes are needed for the display. Raw value (decimal) Raw value (Bin) Physical value (decimal) Physical value (Bin) -128 1000 0000 -356 11111110 10011100 -1 1111 1111 -102 11111111 10011010 100 0110 0100 100 01100100 127 0111 1111 154 10011010 | Raw value (decimal) | Raw value (Bin) | Physical value (decimal) | Physical value (Bin) | -128 | 1000 0000 | -356 | 11111110 10011100 | -1 | 1111 1111 | -102 | 11111111 10011010 | 100 | 0110 0100 | 100 | 01100100 | 127 | 0111 1111 | 154 | 10011010 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Raw value (decimal) | Raw value (Bin) | Physical value (decimal) | Physical value (Bin) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -128 | 1000 0000 | -356 | 11111110 10011100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1 | 1111 1111 | -102 | 11111111 10011010 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 100 | 0110 0100 | 100 | 01100100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 127 | 0111 1111 | 154 | 10011010 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Raw value (decimal) | Raw value (Bin) | Physical value (decimal) | Physical value (Bin) |
|---|---|---|---|
| -128 | 1000 0000 | -356 | 11111110 10011100 |
| -1 | 1111 1111 | -102 | 11111111 10011010 |
| 100 | 0110 0100 | 100 | 01100100 |
| 127 | 0111 1111 | 154 | 10011010 |

## Tooltips

Tooltips help users interpret the data on the panel. For detailed information see CANalyzer help page Panel Configuration: Settings.

## Limitations
