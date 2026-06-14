# LED Control

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The LED Control can be used as a control and display element for selecting and displaying of defined states. The individual states are graphically illustrated with colors.

The following use cases are possible with the LED Control:

Indicating that certain states have occurred

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANalyzer, you can actuate the LED Control; the corresponding symbol value is assigned to the symbol and the LED Control displays the associated state.

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

| Ribbon | Properties Window | Description |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| General Group | General |  |  |  |  |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |  |  |  |  |
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |  |  |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |  |  |  |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |  |  |  |  |
| Switch Values Group | Switch Values |  |  |  |  |  |  |
| State Count | State Count | Here you change the number of states. |  |  |  |  |  |
| Switch Values | Switch Values | Here you change the value for the status change. The LED always has at least the two states On and Off. Off Value (Sate 0) Here you change the symbol value and the color for the switched off LED Control. The color is displayed as long as the symbol value in not equal to switch value On. if you switch off the LED with click on the LED Control and the switch value Off is sent. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. The Off state receives all values that are not received by the other On states (marked with *). For Off, you therefore only configure the transmit value . Therefore only a concrete value or a value from the value table can be entered. If the value of the value table is a value range, you must specify with Tx whether the lower or the upper value is to be used as transmit value. The color you have selected for Off is also displayed for all undefined values. On Value (1-n) Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. CAPL Access With the function setControlForeColor, you can change the LED Color On of the LED Control.Only the first On-value can be changed with CAPL. The values entered during a state change can be concrete values and value ranges. Concrete values The symbol value is used both for sending (control element) and receiving (display element). For one state, only one value can be configured for sending and receiving. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. Value ranges When receiving (display element) the symbol, the system checks in which value range the symbol value lies and the corresponding state is displayed. For sending (control element), still a concrete value is required. If required, you can configure it in the Tx column. Notation of a Value Range Input using .. or - between the start value and the end value: for example a..b Input using square brackets: for example [a..b]Closed interval, i.e. the values are within the value range. Input using round brackets: for example (a..b)Open interval, i.e. the values are not within the value range. Input using a round and a square bracket: for example (a..b] or [a..b)(a..b]: the first value is not within the value range and the second value is within it[a..b): the first value is within the value range and the second value is not within it Note If you enter the value range without brackets, square brackets will be added automatically. The value for sending is automatically set to the mean value of the value range and is recalculated only when it lies outside the value range. In the meantime you must adjust it, if required. If the value is assigned to two states, the first state (the state with the smaller index) is displayed. | Off Value (Sate 0) | Here you change the symbol value and the color for the switched off LED Control. The color is displayed as long as the symbol value in not equal to switch value On. if you switch off the LED with click on the LED Control and the switch value Off is sent. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. The Off state receives all values that are not received by the other On states (marked with *). For Off, you therefore only configure the transmit value . Therefore only a concrete value or a value from the value table can be entered. If the value of the value table is a value range, you must specify with Tx whether the lower or the upper value is to be used as transmit value. The color you have selected for Off is also displayed for all undefined values. | On Value (1-n) | Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. CAPL Access With the function setControlForeColor, you can change the LED Color On of the LED Control.Only the first On-value can be changed with CAPL. | Note If you enter the value range without brackets, square brackets will be added automatically. The value for sending is automatically set to the mean value of the value range and is recalculated only when it lies outside the value range. In the meantime you must adjust it, if required. If the value is assigned to two states, the first state (the state with the smaller index) is displayed. |
| Off Value (Sate 0) | Here you change the symbol value and the color for the switched off LED Control. The color is displayed as long as the symbol value in not equal to switch value On. if you switch off the LED with click on the LED Control and the switch value Off is sent. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. The Off state receives all values that are not received by the other On states (marked with *). For Off, you therefore only configure the transmit value . Therefore only a concrete value or a value from the value table can be entered. If the value of the value table is a value range, you must specify with Tx whether the lower or the upper value is to be used as transmit value. The color you have selected for Off is also displayed for all undefined values. |  |  |  |  |  |  |
| On Value (1-n) | Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. CAPL Access With the function setControlForeColor, you can change the LED Color On of the LED Control.Only the first On-value can be changed with CAPL. |  |  |  |  |  |  |
| Note If you enter the value range without brackets, square brackets will be added automatically. The value for sending is automatically set to the mean value of the value range and is recalculated only when it lies outside the value range. In the meantime you must adjust it, if required. If the value is assigned to two states, the first state (the state with the smaller index) is displayed. |  |  |  |  |  |  |  |
| — | Epsilon | If the linked symbol is a double value, then a value may not be detected if it differs from the expected value because of an approximation of the decimal.Via the Epsilon property, you may set in the Panel Designer a value that specifies up to which tolerated inaccuracy a value is detected. Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. | Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. | Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. |  |  |  |
| Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. |  |  |  |  |  |  |  |
| Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. |  |  |  |  |  |  |  |
| — | Value Interpretation | Here you select whether the LED with the above defined switch values and colors is displayed (Use Switch Values) the symbol value is interpreted and displayed as color (RGB) For RGB the symbol value is interpreted as 4 bytes and the color results from which value is contained in which byte: [0] = ignored, [1] = Red, [2] = Green, [3] = Blue Date type Data: The bytes [0] to [3] are used. If fewer bytes are present, zeros are filled up.Data type Integer: The value is split into 4 bytes. With the function MakeRGB you can calculate from the RGB values the symbol value for the Value Interpretation RGB. This symbol value is used for the display in the control. |  |  |  |  |  |
| Form Group | Appearance |  |  |  |  |  |  |
| LED Form | Here you change the form of the LED. |  |  |  |  |  |  |
| Appearance Group | Appearance |  |  |  |  |  |  |
| Display Frame | With a click on the symbol you activate/deactivate the display of a LED frame. |  |  |  |  |  |  |
| Resize Proportionally | Resize Proportionally With a click on the symbol you activate/deactivate the proportional increase/decrease (height = width). |  |  |  |  |  |  |
| More Group | — |  |  |  |  |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |  |  |  |  |
| Group: — | Layout |  |  |  |  |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |
| Group: — | Symbol |  |  |  |  |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |  |  |  |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |  |  |  |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Switch Values Group

Switch Values

State Count

Here you change the number of states.

Here you change the value for the status change.

The LED always has at least the two states On and Off.

Off Value

(Sate 0)

Here you change the symbol value and the color for the switched off LED Control.

The color is displayed

If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

The Off state receives all values that are not received by the other On states (marked with *). For Off, you therefore only configure the transmit value . Therefore only a concrete value or a value from the value table can be entered. If the value of the value table is a value range, you must specify with Tx whether the lower or the upper value is to be used as transmit value.

The color you have selected for Off is also displayed for all undefined values.

On Value

(1-n)

Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

| Off Value (Sate 0) | Here you change the symbol value and the color for the switched off LED Control. The color is displayed as long as the symbol value in not equal to switch value On. if you switch off the LED with click on the LED Control and the switch value Off is sent. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. The Off state receives all values that are not received by the other On states (marked with *). For Off, you therefore only configure the transmit value . Therefore only a concrete value or a value from the value table can be entered. If the value of the value table is a value range, you must specify with Tx whether the lower or the upper value is to be used as transmit value. The color you have selected for Off is also displayed for all undefined values. |
|---|---|
| On Value (1-n) | Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. CAPL Access With the function setControlForeColor, you can change the LED Color On of the LED Control.Only the first On-value can be changed with CAPL. |

## CAPL Access

With the function setControlForeColor, you can change the LED Color On of the LED Control.Only the first On-value can be changed with CAPL.

The values entered during a state change can be concrete values and value ranges.

The symbol value is used both for sending (control element) and receiving (display element). For one state, only one value can be configured for sending and receiving. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

Note

—

Epsilon

If the linked symbol is a double value, then a value may not be detected if it differs from the expected value because of an approximation of the decimal.Via the Epsilon property, you may set in the Panel Designer a value that specifies up to which tolerated inaccuracy a value is detected.

The control has been configured with a Value = 2 and an Epsilon = 0.01.

If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status.

This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values.

Value Interpretation

Here you select whether

For RGB the symbol value is interpreted as 4 bytes and the color results from which value is contained in which byte:

[0] = ignored, [1] = Red, [2] = Green, [3] = Blue

Date type Data: The bytes [0] to [3] are used. If fewer bytes are present, zeros are filled up.Data type Integer: The value is split into 4 bytes.

With the function MakeRGB you can calculate from the RGB values the symbol value for the Value Interpretation RGB. This symbol value is used for the display in the control.

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

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note If you enter the value range without brackets, square brackets will be added automatically. The value for sending is automatically set to the mean value of the value range and is recalculated only when it lies outside the value range. In the meantime you must adjust it, if required. If the value is assigned to two states, the first state (the state with the smaller index) is displayed. |
|---|

| Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. |
|---|

| Note This setting shall explicitly not be used for displaying ranges of values. The maximum epsilon value is therefore limited to a tenth of the difference between two expected values. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
