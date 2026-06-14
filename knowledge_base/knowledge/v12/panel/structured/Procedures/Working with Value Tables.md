# Working with Value Tables

> Category: `Panel` | Subcategory: `Procedures` | Type: `concept`

For the controls Button, Check Box, LED Control, Media Player, Radio Button and Switch/Indicator, you can assign switch values from value tables.

## Advantage over Numerical Switch Values

In the value tables a symbolic value is assigned to a numerical value, e.g. 3 = Warning

If you have configured a symbolic value as switch value (e.g. Warning), the behavior of the controls does not change when the numerical value changes.

Controls with numerical switch values must be adapted as soon as a numerical specification changes.

## What Happens when Working with a Numerical Value or a Value from a Value Table

The following example is intended to explain the behavior between two Radio Buttons.

## Configuration in Panel Designer

## Behavior at Run-time

Case 1: The value table of the system variable is changed before the measurement:

The numerical value changes to 4, the symbolic value remains Warning

Receiving

The Radio Button is not activated (4!=3)

The Radio Button is activated (Warning=Warning)

Sending

By pressing the Radio Button, the value 3 is still sent; it may no longer trigger the desired action.

By pressing the Radio Button, Warning is still sent.

Case 2: The value table of the system variable is changed before the measurement:

The numerical value remains 3, the symbolic value changes to Error

The Radio Button is activated (3=3)

The Radio Button is not activated (Error!=Warning)

By pressing the Radio Button, nothing is sent, Warning no longer exists.

| Behavior | Radio Button 1 Configured Switch Value: 3 | Radio Button 2 Configured Switch Value: Warning |
|---|---|---|
| Case 1: The value table of the system variable is changed before the measurement: The numerical value changes to 4, the symbolic value remains Warning |  |  |
| Receiving | The Radio Button is not activated (4!=3) | The Radio Button is activated (Warning=Warning) |
| Sending | By pressing the Radio Button, the value 3 is still sent; it may no longer trigger the desired action. | By pressing the Radio Button, Warning is still sent. |
| Case 2: The value table of the system variable is changed before the measurement: The numerical value remains 3, the symbolic value changes to Error |  |  |
| Receiving | The Radio Button is activated (3=3) | The Radio Button is not activated (Error!=Warning) |
| Sending | By pressing the Radio Button, the value 3 is still sent; it may no longer trigger the desired action. | By pressing the Radio Button, nothing is sent, Warning no longer exists. |
