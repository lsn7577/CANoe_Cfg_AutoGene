# LED Band

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The LED Band is a display element to highlight areas on a panel for a defined state.

The following use cases are possible with the LED Band:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Display Element

During runtime of CANoe/CANalyzer the symbol value is interpreted as a color value including transparency level. The LED Band is displayed in the indicated color and the indicated transparency.

## Changing the LED Band with the Mouse

Select the LED Band and move the mouse over the displayed image. The following white selection points are then displayed.

Use the two outer points to move the endpoints of the LED Band and thus change the properties

Use the middle point to change the height of the LED Band and thus change the properties

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

| Ribbon | Properties Window | Description |  |
|---|---|---|---|
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |
| Appearance Group | Appearance |  |  |
| Length | LED Band Length | Here you change the length of the LED Band |  |
| Height | LED Band Height | Here you change the height of the LED Band |  |
| Rotation | Rotation | Here you change the rotation angle of the LED Band. Rotation range -180° bis +180° Example: |  |
| Round Corners | Here you change the rounding of the corners: RoundLED Band with rounded corners SquareLED Band without rounded corners |  |  |
| Fade Color | Here you change the color fading: Fading OnThe color becomes transparent at the edges Fading OffThe LED Band has a hard colored edge |  |  |
| — | Designer Color | Here you change the color the LED Band should have at the time of the design.This property is not used during runtime because the color is determined here by the symbol value. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Settings |  |  |
| — | Value Interpretation | Defines how the symbol value should be interpreted as color.For this the symbol value is interpreted as 4 bytes and the color results from which value is contained in which byte. A RGB: [0] = Alpha (transparency), [1] = Red, [2] = Green, [3] = Blue RGB A: [0] = Red, [1] = Green, [2] = Blue, [3] = Alpha (transparency) Transparency range: 0 corresponds to 0% color opacity 255 corresponds to 100% color opacity Date type Data: The bytes [0] to [3] are used. If fewer bytes are present, zeros are filled up.Data type Integer: The value is split into 4 bytes. With the function MakeARGB you can calculate from the alpha value and the RGB values the symbol value for the Value Interpretation ARGB. This symbol value is used for the display in the control. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Appearance Group

Appearance

Length

LED Band Length

Here you change the length of the LED Band

Height

LED Band Height

Here you change the height of the LED Band

Rotation

Here you change the rotation angle of the LED Band.

Rotation range -180° bis +180°

Example:

Round Corners

Here you change the rounding of the corners:

Fade Color

Here you change the color fading:

—

Designer Color

Here you change the color the LED Band should have at the time of the design.This property is not used during runtime because the color is determined here by the symbol value.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Settings

Value Interpretation

Defines how the symbol value should be interpreted as color.For this the symbol value is interpreted as 4 bytes and the color results from which value is contained in which byte.

Transparency range:

Date type Data: The bytes [0] to [3] are used. If fewer bytes are present, zeros are filled up.Data type Integer: The value is split into 4 bytes.

With the function MakeARGB you can calculate from the alpha value and the RGB values the symbol value for the Value Interpretation ARGB. This symbol value is used for the display in the control.

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

Note

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

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
