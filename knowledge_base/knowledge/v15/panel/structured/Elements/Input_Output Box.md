# Input/Output Box

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Input/Output Box can be used as a control and display element for inputting and outputting symbol values.

The following use cases are possible with the Input/Output Box:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

You can assign a color for the box background and/or box text to highlight a violation the valid signal value range (value range is exceeded or fallen below).

## Control Element

You can enter a value in the field during runtime of CANalyzer. This value is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. The Input/Output Box displays the symbol value automatically.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Text

Here you change the description of the control.

| Ribbon | Properties Window | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| General Group | General |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text | Text | Here you change the description of the control. CAPL Access With the function setControlProperty, you can set this property of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Font / Text Box Font Group | Font Text/Box |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | With a click on the symbol you increase the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the label. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the label. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Box Text Align | With a click on the symbol you align the text on the left site of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Box Text Align | With a click on the symbol you align the text in the middle of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Box Text Align | With a click on the symbol you align the text on the right site of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Appearance Group | Appearance |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Display Text | Here you change the alignment of the description: Text LeftTo the left of the Input/Output Box Text RightTo the right of the Input/Output Box Text TopAbove the Input/Output Box Text BottomBelow the Input/Output Box Hide TextNo description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text with MinMax Values | Here you select whether the min/max values of the assigned symbols should be appended at the description of the control. If no min/max values are defined nothing is displayed even if the display is activated. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text with Unit | Here you select whether the unit of the assigned symbols should be appended at the description of the control. If no unit is defined nothing is displayed even if the display is activated. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Text/Box Border Style | Here you change the frame of the text/box: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame Flat Only for Box Border Style |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Box Border Color | Here you change the frame color for the box.Only available for Flat box border style. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Value Group | Value |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Display | Value InterpretationDecimal Places | Here you change the interpretation of the values and the number of decimal places. Note When entering an improper value, the selection jumps automatically to a value that is permitted for the symbol and its data type. Value Interpretation Value Description Text Display of the symbol value as text. Decimal Display of the symbol value as decimal number. Hexadecimal Display of the symbol value as hexadecimal number. Binary Display of the symbol value as binary number. Double Display of the symbol value as floating-point number. Science Display of the symbol value in scientific notation. Symbolic If a symbol with value table is assigned to the Input/Output Box, the symbolic value from the value table is displayed.If the symbolic value is not available in the value table, the numeric value is displayed. If a diagnostic parameter is assigned to the Input/Output box, a textual representation of the value is displayed, e.g. the value and unit. If no special textual representation is available, the numeric value of the diagnostic parameter is displayed. Note When entering an improper Value Interpretation value, the selection jumps automatically to a value that is permitted for the symbol and its data type. CAPL Access With the function setControlProperty, you can set this property of the control. | Note When entering an improper value, the selection jumps automatically to a value that is permitted for the symbol and its data type. | Value | Description | Text | Display of the symbol value as text. | Decimal | Display of the symbol value as decimal number. | Hexadecimal | Display of the symbol value as hexadecimal number. | Binary | Display of the symbol value as binary number. | Double | Display of the symbol value as floating-point number. | Science | Display of the symbol value in scientific notation. | Symbolic | If a symbol with value table is assigned to the Input/Output Box, the symbolic value from the value table is displayed.If the symbolic value is not available in the value table, the numeric value is displayed. If a diagnostic parameter is assigned to the Input/Output box, a textual representation of the value is displayed, e.g. the value and unit. If no special textual representation is available, the numeric value of the diagnostic parameter is displayed. | Note When entering an improper Value Interpretation value, the selection jumps automatically to a value that is permitted for the symbol and its data type. |
| Note When entering an improper value, the selection jumps automatically to a value that is permitted for the symbol and its data type. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Value | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text | Display of the symbol value as text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Decimal | Display of the symbol value as decimal number. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Hexadecimal | Display of the symbol value as hexadecimal number. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Binary | Display of the symbol value as binary number. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Double | Display of the symbol value as floating-point number. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Science | Display of the symbol value in scientific notation. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Symbolic | If a symbol with value table is assigned to the Input/Output Box, the symbolic value from the value table is displayed.If the symbolic value is not available in the value table, the numeric value is displayed. If a diagnostic parameter is assigned to the Input/Output box, a textual representation of the value is displayed, e.g. the value and unit. If no special textual representation is available, the numeric value of the diagnostic parameter is displayed. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note When entering an improper Value Interpretation value, the selection jumps automatically to a value that is permitted for the symbol and its data type. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Type | Value Type | Here you change the display: Physical value Raw value |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Value Table | Here you select the value table from which the symbolic values are displayed. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Show Leading Zeros | Here you select whether hexadecimal or binary values are displayed with leading zeros. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Alarm Group | Alarm Settings |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Alarm DisplayLower LimitUpper Limit | Here you change the display for the overshot/undershot of a defined alarm limit value. NoneNo display AttributesDefine alarm limit values on the database level.You can implement this with special attributes. Please note that this option is only available if the corresponding attributes are defined in the database. Database ValuesTake over alarm limit values from database.If the limit values for the alarm function correspond to the min./max. values defined in the database, there is no need to define special attributes. User DefinedUser-defined alarm limit values.This makes it possible to assign a different limit value pair to each element even if these elements are all linked with the same symbol. This may be necessary for a write-protected database if you would like to change the alarm limit values. Please note that alarm limit values from the database are not adjusted until the panel is loaded. Lower: Change the lower alarm limit value Upper: Change the upper alarm limit value |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Lower | Lower Limit Background Color | Here you change the color of the Input/Output Box when undershot the alarm limit value. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Lower Limit Text Color | Here you change the text color of the Input/Output Box when undershot the alarm limit value. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Upper | Upper Limit Background Color | Here you change the color of the Input/Output Box when overshot the alarm limit value. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Upper Limit Text Color | Here you change the text color of the Input/Output Box when overshot the alarm limit value. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| More Group | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Settings |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Fix Text | If the text is too long, you can select here whether the start of the text (Left) or the end of the text (Right) should be displayed. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Send On Focus Lost | Here you specify when the value entered in the input/output box must be sent. Please note that the input/output box can programmatically receive (e.g. during loading of the configuration) and loose the focus again (e.g. in case of desktop replacement). Therefore, it may be a good idea to set the option to False. If this option is True, the entered value in the Input/Output Box will be sent as soon as the focus on the Input/Output Box is lost. If this option is False, the entered value in the Input/Output Box will only be sent after pressing <Return>. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Send the Same Value Again | If the option is True, the same value can be sent again. However, you must always explicitly confirm the value by pressing the <Enter> key to initiate sending. If the option is False, the same values cannot be sent. Values can be sent only if they change. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Layout |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Symbol |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## CAPL Access

With the function setControlProperty, you can set this property of the control.

Display Only

With a click on the symbol you switch between control and display element.

With activated option the control is used as display element.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Text Font / Text Box Font Group

Font Text/Box

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

Box Text Align

With a click on the symbol you align the text on the left site of the control.

With a click on the symbol you align the text in the middle of the control.

With a click on the symbol you align the text on the right site of the control.

Appearance Group

Appearance

Display Text

Here you change the alignment of the description:

Text with MinMax Values

Here you select whether the min/max values of the assigned symbols should be appended at the description of the control.

If no min/max values are defined nothing is displayed even if the display is activated.

Text with Unit

Here you select whether the unit of the assigned symbols should be appended at the description of the control.

If no unit is defined nothing is displayed even if the display is activated.

—

Text/Box Border Style

Here you change the frame of the text/box:

Box Border Color

Value Group

Value

Display

Value InterpretationDecimal Places

Here you change the interpretation of the values and the number of decimal places.

Note

When entering an improper value, the selection jumps automatically to a value that is permitted for the symbol and its data type.

Value Interpretation

Text

Display of the symbol value as text.

Decimal

Display of the symbol value as decimal number.

Hexadecimal

Display of the symbol value as hexadecimal number.

Binary

Display of the symbol value as binary number.

Double

Display of the symbol value as floating-point number.

Science

Display of the symbol value in scientific notation.

Symbolic

When entering an improper Value Interpretation value, the selection jumps automatically to a value that is permitted for the symbol and its data type.

| Note When entering an improper value, the selection jumps automatically to a value that is permitted for the symbol and its data type. |
|---|

| Value | Description |
|---|---|
| Text | Display of the symbol value as text. |
| Decimal | Display of the symbol value as decimal number. |
| Hexadecimal | Display of the symbol value as hexadecimal number. |
| Binary | Display of the symbol value as binary number. |
| Double | Display of the symbol value as floating-point number. |
| Science | Display of the symbol value in scientific notation. |
| Symbolic | If a symbol with value table is assigned to the Input/Output Box, the symbolic value from the value table is displayed.If the symbolic value is not available in the value table, the numeric value is displayed. If a diagnostic parameter is assigned to the Input/Output box, a textual representation of the value is displayed, e.g. the value and unit. If no special textual representation is available, the numeric value of the diagnostic parameter is displayed. |

| Note When entering an improper Value Interpretation value, the selection jumps automatically to a value that is permitted for the symbol and its data type. |
|---|

## CAPL Access

With the function setControlProperty, you can set this property of the control.

Type

Value Type

Here you change the display:

—

Value Table

Here you select the value table from which the symbolic values are displayed.

Show Leading Zeros

Here you select whether hexadecimal or binary values are displayed with leading zeros.

Alarm Group

Alarm Settings

Alarm DisplayLower LimitUpper Limit

Here you change the display for the overshot/undershot of a defined alarm limit value.

Lower

Lower Limit Background Color

Here you change the color of the Input/Output Box when undershot the alarm limit value.

Lower Limit Text Color

Here you change the text color of the Input/Output Box when undershot the alarm limit value.

Upper

Upper Limit Background Color

Here you change the color of the Input/Output Box when overshot the alarm limit value.

Upper Limit Text Color

Here you change the text color of the Input/Output Box when overshot the alarm limit value.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Settings

Fix Text

If the text is too long, you can select here whether the start of the text (Left) or the end of the text (Right) should be displayed.

Send On Focus Lost

Here you specify when the value entered in the input/output box must be sent. Please note that the input/output box can programmatically receive (e.g. during loading of the configuration) and loose the focus again (e.g. in case of desktop replacement). Therefore, it may be a good idea to set the option to False.

Send the Same Value Again

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

Note

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Symbol

You can assign a symbol to the control.

With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter.

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
