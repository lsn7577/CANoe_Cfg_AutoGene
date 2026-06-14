# Numeric Up/Down

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

Numeric Numeric Up/Down can be used as a control and display element for values within a defined value range.

The following use cases are possible with the Numeric Up/Down:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

## Control Element

During runtime of CANoe/CANalyzer, you can select a value in Numeric Up/Down that is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. In the Numeric Up/Down this value is displayed.

Note

If the value of the assigned symbol exceeds the value range specified with Minimum and Maximum, the Numeric Up/Down remains in the uppermost or bottommost position.

| Note If the value of the assigned symbol exceeds the value range specified with Minimum and Maximum, the Numeric Up/Down remains in the uppermost or bottommost position. |
|---|

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
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |
| Font Group | Font |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the Numeric Up/Down. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the Numeric Up/Down. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Text Align | With a click on the symbol you align the text on the left site of the control. |  |  |
| Text Align | With a click on the symbol you align the text in the middle of the control. |  |  |
| Text Align | With a click on the symbol you align the text on the right site of the control. |  |  |
| Value Range Group | Value Range |  |  |
| Minimum | Minimum | Here you change the minimum of the value range. |  |
| Maximum | Minimum | Here you change the maximum of the value range. |  |
| Settings Group | Settings |  |  |
| Increment | Increment | Here you change the increment size between two consecutive Numeric Up/Down values. |  |
| Decimal Places | Decimal Places | Here you change the number of decimal places. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Appearance |  |  |
| — | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |  |
| — | Up/Down Align | Here, you specify the position (left/right) of the Up and Down buttons. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Font Group

Font

Font|Name/Size

Here you change the font and the font size.

With a click on the symbol you increase the font size.

With a click on the symbol you reduce the font size.

Font|Bold

With a click on the symbol you format the text bold.

Font|Italic

With a click on the symbol you format the text italic.

Font|Underline

With a click on the symbol you underline the text.

Font|Strikeout

Here you strikeout the text.

Font|Unit

Here you change the unit of the font size.

Text Color

Here you change the color of the text.

## CAPL Access

Background Color

Here you change the background color of the text.

## CAPL Access

Text Align

With a click on the symbol you align the text on the left site of the control.

With a click on the symbol you align the text in the middle of the control.

With a click on the symbol you align the text on the right site of the control.

Value Range Group

Value Range

Minimum

Here you change the minimum of the value range.

Maximum

Here you change the maximum of the value range.

Settings Group

Settings

Increment

Here you change the increment size between two consecutive Numeric Up/Down values.

Decimal Places

Here you change the number of decimal places.

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Border Style

Here you change the frame of the control:

Up/Down Align

Here, you specify the position (left/right) of the Up and Down buttons.

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
