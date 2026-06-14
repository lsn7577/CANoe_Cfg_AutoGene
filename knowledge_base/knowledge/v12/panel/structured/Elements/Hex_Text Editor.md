# Hex/Text Editor

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Hex/Text Editor can be used as a control and display element for inputting and displaying larger quantities of data.

In the Hex/Text Editor Ascii characters or decimal values can be displayed in hex format.

The following use cases are possible with the Hex/Text Editor:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANoe/CANalyzer, you can enter text/hexadecimal values in the Hex/Text Editor.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. The Hex/Text Editor displays the symbol value automatically.

Note

If the Text field is read only, values cannot be copied from it.

| Note If the Text field is read only, values cannot be copied from it. |
|---|

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

| Ribbon | Properties Window | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| General Group | General |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font Group | Font |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | With a click on the symbol you increase the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Color | Here you change the color of the text. CAPL Access The control can be activated with the following CAPL functions: With the function setControlForeColor, you can change the Text Color of the Hex/Text Editor. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Background Color | Here you change the background color of the text. CAPL Access The control can be activated with the following CAPL functions: With the function setControlBackColor, you can change the Background Color of the Hex/Text Editor. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Editor Layout Group | Settings |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Editor Layout | Here you change the display of the Hex/Text Editor: Hex and Text FieldDisplay hex and text field Only Hex FieldDisplay hex field only Only Text FieldDisplay text field only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Settings Group | Settings |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Columns per Line | Columns/letters per line | Here you change the display of columns in the Hex field and thus the display of the data bytes. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Interpretation | Text Field Interpretation | Here you change the value interpretation: Ascii Encoding Decimal For Data data type, two hex values (1 byte) are always converted as a three-digit decimal number. For IntegerArray data type, eight hex values (4 bytes) are always converted as a signed ten-digit decimal number. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Fixed Length | (for data type Data and String) Specifies how many bytes (characters) are to be displayed. This allows the rear part of a symbol to be hidden.When sending, Fixed Length bytes (characters) of the old symbol value are always replaced. If less than Fixed Length bytes are specified, null bytes (0x00) are added for Data data type and blank spaces are added for String data type until Fixed Length is filled.If Fixed Length <= 0, the length is variable as before.Possible values: Integers > 0 and -1. For values <= 0, Fixed Length is set to -1. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Start Offset | (for data type Data and String) Specifies the position starting from which the bytes (characters) of the symbol are to be displayed. This allows the front part of a symbol to be hidden.When sending, the bytes before the Start Offset are not changed. If Start Offset is greater than the length of the existing symbol, null bytes (0x00) are added for Data data type and blank characters are added for String data type until Start Offset is filled.Possible values: Integers > = 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Behavior of Various Data Types and Representations Data Type Text File Interpretation Text field "read only" Columns/Letter per Line String AsciiEncoding — variable Data AsciiEncoding — variable Decimal • variable Integer-Array AsciiEncoding • 4 Decimal • 4 Note for Fixed Length and Start Offset Example 1 Start Offset = 2Fixed Length = 3Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38Value is changed to: 3FNew symbol value: 34 35 3F 00 00 39 3A Example 2 Start Offset = 2Fixed Length = 3Existing symbol value: 34Displayed value:Value is changed to: 3A 3BNew symbol value: 34 00 3A 3B 00 Example 3 Start Offset = 2Fixed Length = -1Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38 39 3AValue is changed to: 3FNew symbol value: 34 35 3F Example 4 Start Offset = 2Fixed Length = -1Existing symbol value: 34Displayed value:Value is changed to: 3FNew symbol value: 34 00 3F | Data Type | Text File Interpretation | Text field "read only" | Columns/Letter per Line | String | AsciiEncoding | — | variable | Data | AsciiEncoding | — | variable | Decimal | • | variable | Integer-Array | AsciiEncoding | • | 4 | Decimal | • | 4 | Note for Fixed Length and Start Offset Example 1 Start Offset = 2Fixed Length = 3Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38Value is changed to: 3FNew symbol value: 34 35 3F 00 00 39 3A Example 2 Start Offset = 2Fixed Length = 3Existing symbol value: 34Displayed value:Value is changed to: 3A 3BNew symbol value: 34 00 3A 3B 00 Example 3 Start Offset = 2Fixed Length = -1Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38 39 3AValue is changed to: 3FNew symbol value: 34 35 3F Example 4 Start Offset = 2Fixed Length = -1Existing symbol value: 34Displayed value:Value is changed to: 3FNew symbol value: 34 00 3F |
| Data Type | Text File Interpretation | Text field "read only" | Columns/Letter per Line |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| String | AsciiEncoding | — | variable |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Data | AsciiEncoding | — | variable |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Decimal | • | variable |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Integer-Array | AsciiEncoding | • | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Decimal | • | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note for Fixed Length and Start Offset Example 1 Start Offset = 2Fixed Length = 3Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38Value is changed to: 3FNew symbol value: 34 35 3F 00 00 39 3A Example 2 Start Offset = 2Fixed Length = 3Existing symbol value: 34Displayed value:Value is changed to: 3A 3BNew symbol value: 34 00 3A 3B 00 Example 3 Start Offset = 2Fixed Length = -1Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38 39 3AValue is changed to: 3FNew symbol value: 34 35 3F Example 4 Start Offset = 2Fixed Length = -1Existing symbol value: 34Displayed value:Value is changed to: 3FNew symbol value: 34 00 3F |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| More Group | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Layout |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Symbol |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

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

The control can be activated with the following CAPL functions:

Background Color

Here you change the background color of the text.

## CAPL Access

The control can be activated with the following CAPL functions:

Editor Layout Group

Settings

Editor Layout

Here you change the display of the Hex/Text Editor:

Settings Group

Columns per Line

Columns/letters per line

Here you change the display of columns in the Hex field and thus the display of the data bytes.

Interpretation

Text Field Interpretation

Here you change the value interpretation:

—

Fixed Length

(for data type Data and String)

Specifies how many bytes (characters) are to be displayed. This allows the rear part of a symbol to be hidden.When sending, Fixed Length bytes (characters) of the old symbol value are always replaced. If less than Fixed Length bytes are specified, null bytes (0x00) are added for Data data type and blank spaces are added for String data type until Fixed Length is filled.If Fixed Length <= 0, the length is variable as before.Possible values: Integers > 0 and -1. For values <= 0, Fixed Length is set to -1.

Start Offset

Specifies the position starting from which the bytes (characters) of the symbol are to be displayed. This allows the front part of a symbol to be hidden.When sending, the bytes before the Start Offset are not changed. If Start Offset is greater than the length of the existing symbol, null bytes (0x00) are added for Data data type and blank characters are added for String data type until Start Offset is filled.Possible values: Integers > = 0

Behavior of Various Data Types and Representations

String

AsciiEncoding

variable

Data

Decimal

•

Integer-Array

4

Note for Fixed Length and Start Offset

| Data Type | Text File Interpretation | Text field "read only" | Columns/Letter per Line |
|---|---|---|---|
| String | AsciiEncoding | — | variable |
| Data | AsciiEncoding | — | variable |
| Decimal | • | variable |  |
| Integer-Array | AsciiEncoding | • | 4 |
| Decimal | • | 4 |  |

| Note for Fixed Length and Start Offset Example 1 Start Offset = 2Fixed Length = 3Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38Value is changed to: 3FNew symbol value: 34 35 3F 00 00 39 3A Example 2 Start Offset = 2Fixed Length = 3Existing symbol value: 34Displayed value:Value is changed to: 3A 3BNew symbol value: 34 00 3A 3B 00 Example 3 Start Offset = 2Fixed Length = -1Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38 39 3AValue is changed to: 3FNew symbol value: 34 35 3F Example 4 Start Offset = 2Fixed Length = -1Existing symbol value: 34Displayed value:Value is changed to: 3FNew symbol value: 34 00 3F |
|---|

## Example 1

Start Offset = 2Fixed Length = 3Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38Value is changed to: 3FNew symbol value: 34 35 3F 00 00 39 3A

## Example 2

Start Offset = 2Fixed Length = 3Existing symbol value: 34Displayed value:Value is changed to: 3A 3BNew symbol value: 34 00 3A 3B 00

## Example 3

Start Offset = 2Fixed Length = -1Existing symbol value: 34 35 36 37 38 39 3ADisplayed value: 36 37 38 39 3AValue is changed to: 3FNew symbol value: 34 35 3F

## Example 4

Start Offset = 2Fixed Length = -1Existing symbol value: 34Displayed value:Value is changed to: 3FNew symbol value: 34 00 3F

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

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
