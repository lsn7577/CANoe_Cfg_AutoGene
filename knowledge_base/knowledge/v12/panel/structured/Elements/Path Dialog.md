# Path Dialog

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Path Dialog is a control and display element for selecting files and folders interactively.

The following use cases are possible with the Path Dialog:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you select a folder or file via in the File Dialog during the runtime of CANoe/CANalyzer, the information about the path and the name of the folder/file are stored in the symbol.

An existing path is opened with automatically.

## Display Element

The symbol value is not set manually. Rather it is set to a definite order/file by simulation or CAPL programs, for example. In the Path Dialog the corresponding content of the symbol is displayed.

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
| Font Group | Appearance |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| — | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |  |
| Dialog Group | Settings |  |  |
| Dialog Type | Here you change the dialog type: Open File dialogOpens a dialog for the file selection Open Folder dialogOpens a dialog for the directory selection Save File dialogOpens a Save dialog |  |  |
| File Filter | File Filter | Change the file formats in the Open dialog Example All Files\|*.* In Open dialog all files will be displayed. Excel Files\|*.XLS In Open dialog only XLS files will be displayed. Excel Files\|*.XLS\|All Files\|*.* Now you can select in the Data type field of the Open dialog, whether only XLS files or all files will be displayed. | Example All Files\|*.* In Open dialog all files will be displayed. Excel Files\|*.XLS In Open dialog only XLS files will be displayed. Excel Files\|*.XLS\|All Files\|*.* Now you can select in the Data type field of the Open dialog, whether only XLS files or all files will be displayed. |
| Example All Files\|*.* In Open dialog all files will be displayed. Excel Files\|*.XLS In Open dialog only XLS files will be displayed. Excel Files\|*.XLS\|All Files\|*.* Now you can select in the Data type field of the Open dialog, whether only XLS files or all files will be displayed. |  |  |  |
| — | Dialog Title | Here you change the title for the Open File dialog. With default the default title of the dialog is used. |  |
| — | Copy Name without Path | Option to specify whether or not the path should be displayed along with the folder or file name. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
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

Appearance

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

Border Style

Here you change the frame of the control:

Dialog Group

Settings

Dialog Type

Here you change the dialog type:

File Filter

Change the file formats in the Open dialog

Example

All Files|*.* In Open dialog all files will be displayed.

Excel Files|*.XLS In Open dialog only XLS files will be displayed.

Excel Files|*.XLS|All Files|*.* Now you can select in the Data type field of the Open dialog, whether only XLS files or all files will be displayed.

Dialog Title

Here you change the title for the Open File dialog. With default the default title of the dialog is used.

Copy Name without Path

Option to specify whether or not the path should be displayed along with the folder or file name.

More Group

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

| Example All Files\|*.* In Open dialog all files will be displayed. Excel Files\|*.XLS In Open dialog only XLS files will be displayed. Excel Files\|*.XLS\|All Files\|*.* Now you can select in the Data type field of the Open dialog, whether only XLS files or all files will be displayed. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
