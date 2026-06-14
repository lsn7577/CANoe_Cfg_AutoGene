# File Button

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

With the File Button you can call up any desired file.

The following use cases are possible with the File Button:

## Configuration

Assign a file to the File Button in the Panel Designer.

You can configure the control via the ribbon or the Properties Window.

During runtime of CANalyzer you can open the selected file with the File Button.

If required, the program (Application) and also parameters can be provided along with the file, in order to open the file with the desired program.

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
| Settings Group | Settings |  |  |
| Filename | Filename | Here you select the file that should be opened. |  |
| Application | Application | Here you select the application to open the selected file. Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime. | Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime. |
| Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime. |  |  |  |
| — | Arguments | Here you enter an argument for the selected application. |  |
| — | Show Tooltip | Here you specify if a tooltip should be displayed. |  |
| — | Working Directory | Here you enter a working directory in that the program should be executed. |  |
| Settings Group | Appearance |  |  |
| Image File | Image | Here you change the image for the File Button. |  |
| — | Image Align | If a image is assigned to the Button you can change the position of the image here. |  |
| — | Border Color | Here you change the color of the frame. This setting depends on the set Button Style. |  |
| — | Button Style | Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed. |  |
| — | Hover Color | Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style. |  |
| — | Transparent Color | Change the transparent color. The picture transparency is always active. You must only define the color for which the picture should be transparent. |  |
| — | Use Transparent Color | Here you can set if the transparency should really be used. |  |
| — | Use Windows Style | Here you select whether the set background color Background Color is to be taken into account when Windows styles are used: If this property is True, the button is always displayed in the respective style, and the set background color is ignored. If this property is False, the set background color is taken into account. In the Windows style classic, the set background color is always taken into account, regardless of this property. Note The display of the Background Color depends on the Use Windows Style setting. | Note The display of the Background Color depends on the Use Windows Style setting. |
| Note The display of the Background Color depends on the Use Windows Style setting. |  |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Settings Group

Settings

Filename

Here you select the file that should be opened.

Application

Here you select the application to open the selected file.

Note

If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime.

Arguments

Here you enter an argument for the selected application.

Show Tooltip

Here you specify if a tooltip should be displayed.

Working Directory

Here you enter a working directory in that the program should be executed.

Appearance

Image File

Image

Here you change the image for the File Button.

Image Align

If a image is assigned to the Button you can change the position of the image here.

Border Color

Here you change the color of the frame. This setting depends on the set Button Style.

Button Style

Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed.

Hover Color

Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style.

Transparent Color

Change the transparent color.

The picture transparency is always active. You must only define the color for which the picture should be transparent.

Use Transparent Color

Here you can set if the transparency should really be used.

Use Windows Style

Here you select whether the set background color Background Color is to be taken into account when Windows styles are used:

In the Windows style classic, the set background color is always taken into account, regardless of this property.

The display of the Background Color depends on the Use Windows Style setting.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Assigning Controls

| Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime. |
|---|

| Note The display of the Background Color depends on the Use Windows Style setting. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
