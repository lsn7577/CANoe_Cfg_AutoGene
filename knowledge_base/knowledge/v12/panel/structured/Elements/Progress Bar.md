# Progress Bar

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Progress Bar is used to display a value within a defined value range in the form of a bar. The bar display allows you to quickly see whether the current value is in the lower, medium, or upper range of possible values.

The following use cases are possible with the Progress Bar:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

## Display Element

During runtime of CANoe/CANalyzer the Progress Bar indicates the current symbol value.

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
| Font Group | Font |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. |  |  |
| Background Color | Here you change the background color of the text. |  |  |
| Appearance Group | Appearance |  |  |
| Orientation | Here you change the orientation of the bar chart: Horizontal orientation (minimum on the left side) Vertical orientation (minimum on the top) |  |  |
| Decimal Places | Decimal Places | Here you change the number of decimal places for the text output. |  |
| Display Value | Here you change the display whether the symbol value should be displayed as bar chart and text: Text LeftTo the left of the Progress Bar Text RightTo the right of the Progress Bar Text TopAbove the Progress Bar Text BottomBelow the Progress Bar Hide TextNo description |  |  |
| — | Style | Here you change the style of the bar chart. Windows Style The Windows style dependent color settings are used. Classic Style with/without Frame The set color settings are used. Level Meter Style The set color settings are used. Additionally a maximum value line is displayed. |  |
| — | Bar Align | Here you cahnge the filling direction of the bar chart. LeftTop With horizontal alignment, the bar chart fills from left to right. With vertical alignment from top to bottom. RightBottom With horizontal alignment, the bar chart fills from right to left. With vertical alignment from bottom to top. |  |
| — | Origin Value | Here you define the value for the zero point/origin of the bar chart. |  |
| Value Range Group | Value Range |  |  |
| Minimum | Minimum | Here you change the minimum of the value range. |  |
| Maximum | Maximum | Here you change the maximum of the value range. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Colors |  |  |
| — | Background Color | Here you change the background color of the bar chart. |  |
| — | Bar Color | Here you change the color of the bar chart. |  |
| Group: — | Level Meter Settings |  |  |
| — | Alarm Limit Display | Here you select whether the alarm limit line should be displayed or not. |  |
| — | Alarm Line Color | Here you change the color of the alarm limit line. |  |
| — | Alarm Upper Limit | Here you change the alarm limit value. There is only one upper value. |  |
| — | Alarm Upper Limit Color | Here you change the color of the maximum value line that should be used when the upper alarm limit value is exceeded. |  |
| — | LineWidth | Here you change the width of the upper alarm limit line and the maximum value line. |  |
| — | Maximum Hold Time (ms) | Here you change the time how long the current maximum value is displayed. |  |
| — | Maximum Line Color | Here you change the value of the maximum value line. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Font Group

Font

Font|Name/Size

Here you change the font and the font size.

—

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

Background Color

Here you change the background color of the text.

Appearance Group

Appearance

Orientation

Here you change the orientation of the bar chart:

Decimal Places

Here you change the number of decimal places for the text output.

Display Value

Here you change the display whether the symbol value should be displayed as bar chart and text:

Style

Here you change the style of the bar chart.

Bar Align

Here you cahnge the filling direction of the bar chart.

Origin Value

Here you define the value for the zero point/origin of the bar chart.

Value Range Group

Value Range

Minimum

Here you change the minimum of the value range.

Maximum

Here you change the maximum of the value range.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Colors

Here you change the background color of the bar chart.

Bar Color

Here you change the color of the bar chart.

Level Meter Settings

Alarm Limit Display

Here you select whether the alarm limit line should be displayed or not.

Alarm Line Color

Here you change the color of the alarm limit line.

Alarm Upper Limit

Here you change the alarm limit value. There is only one upper value.

Alarm Upper Limit Color

Here you change the color of the maximum value line that should be used when the upper alarm limit value is exceeded.

LineWidth

Here you change the width of the upper alarm limit line and the maximum value line.

Maximum Hold Time (ms)

Here you change the time how long the current maximum value is displayed.

Maximum Line Color

Here you change the value of the maximum value line.

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
