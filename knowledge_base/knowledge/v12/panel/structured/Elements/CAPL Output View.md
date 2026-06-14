# CAPL Output View

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

Note

The CAPL Output View is not available in CANalyzer fun.

| Note The CAPL Output View is not available in CANalyzer fun. |
|---|

## Use Case

The CAPL Output View is used to output text information from CAPL at runtime.

The following uses cases are possible with the CAPL Output View:

## Configuration

You cannot assign a symbol to the control because it is solely text output and is controlled only via CAPL.

You can configure the control via the ribbon or the Properties Window.

Example

You can carry out the following actions at runtime and/or after measurement stops.

Select text

left mouse key

—

You can select a given text segment with the mouse.

Pause/Resume

None

If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears.

Copy

<Ctrl>+<C>

•

You can copy selected text segments, including the text and background colors.

Delete all

<Del>

Deletes everything in the CAPL Output View element.It is not possible to delete individual segments.

Select all

<Ctrl>+<A>

Selects everything in the CAPL Output View element.

| Example You can carry out the following actions at runtime and/or after measurement stops. Action Keyboard Operations Element Context Menu Description Select text left mouse key — You can select a given text segment with the mouse. Pause/Resume None — If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears. Copy <Ctrl>+<C> • You can copy selected text segments, including the text and background colors. Delete all <Del> • Deletes everything in the CAPL Output View element.It is not possible to delete individual segments. Select all <Ctrl>+<A> • Selects everything in the CAPL Output View element. | Action | Keyboard Operations | Element Context Menu | Description | Select text | left mouse key | — | You can select a given text segment with the mouse. | Pause/Resume | None | — | If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears. | Copy | <Ctrl>+<C> | • | You can copy selected text segments, including the text and background colors. | Delete all | <Del> | • | Deletes everything in the CAPL Output View element.It is not possible to delete individual segments. | Select all | <Ctrl>+<A> | • | Selects everything in the CAPL Output View element. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Action | Keyboard Operations | Element Context Menu | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Select text | left mouse key | — | You can select a given text segment with the mouse. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Pause/Resume | None | — | If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Copy | <Ctrl>+<C> | • | You can copy selected text segments, including the text and background colors. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Delete all | <Del> | • | Deletes everything in the CAPL Output View element.It is not possible to delete individual segments. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Select all | <Ctrl>+<A> | • | Selects everything in the CAPL Output View element. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Action | Keyboard Operations | Element Context Menu | Description |
|---|---|---|---|
| Select text | left mouse key | — | You can select a given text segment with the mouse. |
| Pause/Resume | None | — | If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears. |
| Copy | <Ctrl>+<C> | • | You can copy selected text segments, including the text and background colors. |
| Delete all | <Del> | • | Deletes everything in the CAPL Output View element.It is not possible to delete individual segments. |
| Select all | <Ctrl>+<A> | • | Selects everything in the CAPL Output View element. |

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Text

Here you change the description of the control.

This is shown as a tooltip at runtime when you hover the mouse over the CAPL Output View.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Group Font

Font

Font|Name/Size

Here you change the font and the font size.

With a click on the symbol you increase the font size.

With a click on the symbol you reduce the font size.

Font|Bold

With a click on the symbol you format the text bold.

Font|Italic

With a click on the symbol you format the text italic.

Font|Unit

With a click on the symbol you underline the text.

Font|Strikeout

Here you strikeout the text.

Here you change the unit of the font size.

Text Color

Here you change the color of the text.

Text Align

Background Color

Here you change the background color of the text.

Border Style Group

Appearance

Border Style

Here you change the frame of the control:

Output Mode Group

Settings

Output mode

Here you change the text output.You can specify whether the text is output continuously or whether new outputs overwrite existing ones.

| Ribbon | Properties Window | Description |  |
|---|---|---|---|
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |
| Text | Text | Here you change the description of the control. This is shown as a tooltip at runtime when you hover the mouse over the CAPL Output View. |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |
| Group Font | Font |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Unit | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. |  |  |
| — | Text Align |  |  |
| Background Color | Here you change the background color of the text. |  |  |
| Border Style Group | Appearance |  |  |
| Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |  |  |
| Output Mode Group | Settings |  |  |
| Output mode | Here you change the text output.You can specify whether the text is output continuously or whether new outputs overwrite existing ones. AppendThe text is appended continuously. OverwriteIncoming text outputs overwrite existing ones. CAPL Access Text Output You can use the putValueToControl CAPL function to output text, values, signal values and messages. The contents can be deleted with DeleteControlContent. With CANoe/CANalyzer version 7.5, you can also pass additional parameters with the putValueToControl function to modify the formatting of the output, e.g. to output text in a new paragraph or show values in hexadecimal format. Note The maximum length of the displayed text is limited to 16KB (= 16384 characters). If the text is longer older lines will be overwritten regardless of the Output Mode. Color Highlighting of Upcoming Outputs You can use the setControlForeColor and setControlBackColor CAPL functions to modify the text and background color of the upcoming text output at runtime. The setControlColors function lets you specify the text and background color in one step. The setDefaultControlColors function lets you reset the text and background colors to default values, which are defined in the Panel Designer. Note Changes to text and background colors made using setControlForeColor, setControlBackColor, setControlColors and setDefaultControlColors at runtime don't take effect until the putValueToControl function is called. Existing text outputs retain their current text and background color. Visibility With the function setControlVisibility, you can set, if the control is displayed during runtime or not. | Note The maximum length of the displayed text is limited to 16KB (= 16384 characters). If the text is longer older lines will be overwritten regardless of the Output Mode. | Note Changes to text and background colors made using setControlForeColor, setControlBackColor, setControlColors and setDefaultControlColors at runtime don't take effect until the putValueToControl function is called. Existing text outputs retain their current text and background color. |
| Note The maximum length of the displayed text is limited to 16KB (= 16384 characters). If the text is longer older lines will be overwritten regardless of the Output Mode. |  |  |  |
| Note Changes to text and background colors made using setControlForeColor, setControlBackColor, setControlColors and setDefaultControlColors at runtime don't take effect until the putValueToControl function is called. Existing text outputs retain their current text and background color. |  |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |

## CAPL Access

## Text Output

Note

The maximum length of the displayed text is limited to 16KB (= 16384 characters). If the text is longer older lines will be overwritten regardless of the Output Mode.

| Note The maximum length of the displayed text is limited to 16KB (= 16384 characters). If the text is longer older lines will be overwritten regardless of the Output Mode. |
|---|

## Color Highlighting of Upcoming Outputs

Note

| Note Changes to text and background colors made using setControlForeColor, setControlBackColor, setControlColors and setDefaultControlColors at runtime don't take effect until the putValueToControl function is called. Existing text outputs retain their current text and background color. |
|---|

## Visibility

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

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

Assigning Controls | CAPL Output View and panel conversion

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
