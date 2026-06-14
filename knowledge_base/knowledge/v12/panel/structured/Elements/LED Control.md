# LED Control

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The LED Control can be used as a control and display element for selecting and displaying of two defined states (LED on/LED off). The individual statuses are shown graphically.

The following use cases are possible with the LED Control:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANoe/CANalyzer, you can actuate the LED Control; the corresponding symbol value is assigned to the symbol and the LED Control displays the associated state.

## Display Element

The symbol is not set manually to a defined condition. Rather it is set by simulation or CAPL programs, for example. The LED Control displays the associated state.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Display Only

With a click on the symbol you switch between control and display element.

With activated option the control is used as display element.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

| Ribbon | Properties Window | Description |  |  |
|---|---|---|---|---|
| General Group | General |  |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |  |
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |  |
| Switch Values Group | Switch Values |  |  |  |
| On | On LED Color On Value | Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. CAPL Access With the function setControlForeColor, you can change the LED Color On of the LED Control. |  |  |
| Off | Off LED Color Off Value | Here you change the symbol value and the color for the switched off LED Control. The color is displayed as long as the symbol value in not equal to switch value On. if you switch off the LED with click on the LED Control and the switch value Off is sent. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. |  |  |
| — | Epsilon | If the linked symbol is a double value, then a value may not be detected if it differs from the expected value because of an approximation of the decimal.Via the Epsilon property, you may set in the Panel Designer a value that specifies up to which tolerated inaccuracy a value is detected. Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. | Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. | Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. |
| Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. |  |  |  |  |
| Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. |  |  |  |  |
| — | Value Interpretation | Here you select whether the LED with the above defined switch values (On/Off) and colors is displayed (Use Switch Value) the symbol value is interpreted and displayed as color (RGB) For RGB the symbol value is interpreted as 4 bytes and the color results from which value is contained in which byte: [0] = ignored, [1] = Red, [2] = Green, [3] = Blue Date type Data: The bytes [0] to [3] are used. If fewer bytes are present, zeros are filled up.Data type Integer: The value is split into 4 bytes. With the function MakeARGB you can calculate from the alpha value (255) and the RGB values the symbol value for the Value Interpretation RGB. This symbol value is used for the display in the control. |  |  |
| Form Group | Appearance |  |  |  |
| LED Form | Here you change the form of the LED. |  |  |  |
| Appearance Group | Appearance |  |  |  |
| Display Frame | With a click on the symbol you activate/deactivate the display of a LED frame. |  |  |  |
| Resize Proportionally | Resize Proportionally With a click on the symbol you activate/deactivate the proportional increase/decrease (height = width). |  |  |  |
| More Group | — |  |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |  |
| Group: — | Layout |  |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |
| Group: — | Symbol |  |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Switch Values Group

Switch Values

On

On LED Color

On Value

Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

## CAPL Access

With the function setControlForeColor, you can change the LED Color On of the LED Control.

Off

Off LED Color

Off Value

Here you change the symbol value and the color for the switched off LED Control.

The color is displayed

If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

—

Epsilon

If the linked symbol is a double value, then a value may not be detected if it differs from the expected value because of an approximation of the decimal.Via the Epsilon property, you may set in the Panel Designer a value that specifies up to which tolerated inaccuracy a value is detected.

Note

The control has been configured with a Value = 2 and an Epsilon = 0.01.

If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status.

This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values.

Value Interpretation

Here you select whether

For RGB the symbol value is interpreted as 4 bytes and the color results from which value is contained in which byte:

[0] = ignored, [1] = Red, [2] = Green, [3] = Blue

Date type Data: The bytes [0] to [3] are used. If fewer bytes are present, zeros are filled up.Data type Integer: The value is split into 4 bytes.

With the function MakeARGB you can calculate from the alpha value (255) and the RGB values the symbol value for the Value Interpretation RGB. This symbol value is used for the display in the control.

Form Group

Appearance

LED Form

Here you change the form of the LED.

Appearance Group

Display Frame

With a click on the symbol you activate/deactivate the display of a LED frame.

Resize Proportionally

With a click on the symbol you activate/deactivate the proportional increase/decrease (height = width).

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Symbol

You can assign a symbol to the control.

With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter.

See also Configuration of the control.

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. |
|---|

| Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
