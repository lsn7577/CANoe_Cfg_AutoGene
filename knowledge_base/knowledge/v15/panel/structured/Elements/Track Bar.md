# Track Bar

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Track Bar can be used as a control and display element for values within a defined value range.

The following use cases are possible with the Track Bar:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

Note

If the value of the assigned symbol exceeds the value range specified with Minimum and Maximum, the Track Bar remains in the rightmost or leftmost position.

| Note If the value of the assigned symbol exceeds the value range specified with Minimum and Maximum, the Track Bar remains in the rightmost or leftmost position. |
|---|

## Control Element

During runtime of CANalyzer, the Track Bar can be used to set a desired value; this value is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. In the Track Bar this value is displayed.

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

| Ribbon | Properties Window | Description |  |
|---|---|---|---|
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |
| Value Range Group | Value Range |  |  |
| Minimum | Minimum | Here you change the minimum of the value range. |  |
| Maximum | Maximum | Here you change the maximum of the value range. |  |
| Appearance Group | Appearance |  |  |
| Orientation | Here you change the orientation of the scale: HorizontalHorizontal orientation (minimum on the left) VerticalVertical orientation (minimum on the bottom) |  |  |
| Display Minimum/Maximum | Display Min/Max With a click on the symbol you switch on/off the display of Minimum and Maximum of the defined value range. |  |  |
| Tick Style | Here you change the display of the scale lines (ticks): No TicksNo scale lines Ticks TopScale lines above the scale Ticks BottomScale lines below the scale Ticks Top and BottomScale lines above and below the scale |  |  |
| Show Value Tooltip | Show Value Tooltip With a click on the symbol you switch on/off the display of the current value within a tooltip. |  |  |
| — | Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the Track Bar. With the function setDefaultControlColors, you can reset the background color to the default value defined in the Panel Designer. |  |
| — | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |  |
| Settings Group | Settings |  |  |
| Tick Frequency | Tick Frequency | Here you change the scale line (tick) spacing.Tick Frequency must always be a multiple of the Small Change increment. CAPL Access With the function setControlProperty, you can set this property of the control. |  |
| Small Change | Small Change | Here, you modify the increment by which the symbol value is modified when the drag point is moved (with the mouse) or when the arrow keys are pressed. CAPL Access With the function setControlProperty, you can set this property of the control. |  |
| Large Change | Large Change | Here, you modify the increment by which the symbol value is changed when the keys <Page Down>/<Page Up> are pressed and when you click next to the drag point. To use the functionality of the keys for the run-time in /CANalyzer, must be activated in the /CANalyzer status bar. Large Change must always be a multiple of the Small Change increment. CAPL Access With the function setControlProperty, you can set this property of the control. |  |
| Commit Value | Here you change the transmission behavior for pressing a mouse button: All ValuesAll defined values are sent until the mouse button will be released Only Last ValueOnly that value will be sent that is selected on release of the mouse button |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Value Range Group

Value Range

Minimum

Here you change the minimum of the value range.

Maximum

Here you change the maximum of the value range.

Appearance Group

Appearance

Orientation

Here you change the orientation of the scale:

Display Minimum/Maximum

Display Min/Max

With a click on the symbol you switch on/off the display of Minimum and Maximum of the defined value range.

Tick Style

Here you change the display of the scale lines (ticks):

Show Value Tooltip

With a click on the symbol you switch on/off the display of the current value within a tooltip.

Background Color

Here you change the background color of the text.

## CAPL Access

—

Border Style

Here you change the frame of the control:

Settings Group

Settings

Tick Frequency

Here you change the scale line (tick) spacing.Tick Frequency must always be a multiple of the Small Change increment.

## CAPL Access

With the function setControlProperty, you can set this property of the control.

Small Change

Here, you modify the increment by which the symbol value is modified when the drag point is moved (with the mouse) or when the arrow keys are pressed.

## CAPL Access

With the function setControlProperty, you can set this property of the control.

Large Change

Here, you modify the increment by which the symbol value is changed when the keys <Page Down>/<Page Up> are pressed and when you click next to the drag point.

To use the functionality of the keys for the run-time in /CANalyzer, must be activated in the /CANalyzer status bar.

Large Change must always be a multiple of the Small Change increment.

## CAPL Access

With the function setControlProperty, you can set this property of the control.

Commit Value

Here you change the transmission behavior for pressing a mouse button:

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

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
