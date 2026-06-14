# MOST Send Button

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The MOST Send Button is a control with which assigned MOST messages can be sent on a specified channels.

## Configuration

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you click the MOST Send Button during runtime of ,CANalyzer the defined messages are sent to the corresponding channel at the specified sending interval.

In addition, you can specify whether a waiting period for the receipt confirmation is to be set and, if so, the length of the waiting period.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Text

Here you change the description of the control.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

| Ribbon | Properties Window | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| General Group | General |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text | Text | Here you change the description of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font Group | Font |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | With a click on the symbol you increase the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Color | Here you change the color of the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Background Color | Here you change the background color of the text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Align | With a click on the symbol you align the text on the left site of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Align | With a click on the symbol you align the text in the middle of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Text Align | With a click on the symbol you align the text on the right site of the control. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Send Settings Group | Settings |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Wait for Ack | Wait for Ack With a click on the symbol you activate/deactivate waiting for a Tx acknowledgment of a sent message, before the next message will be sent. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Timeout (ms) | Timeout | Here you change the maximum waiting time for an acknowledgment of a sent message before the next message is sent. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Delay (ms) | Delay | Here you change the waiting time between messages that have to be sent. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Channel | Device Name | Here you change the channel on which the messages should be sent. (MOST1, MOST2, …). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Message Hex Dump | Message HexDump | Here you specify the messages to be sent. Separate particular messages with a comma. Format: XXXXDDDDTTPPPPPP DDDD Destination address TT=00 Normal control message TT=01 RemoteRead TT=02 RemoteWrite TT=03 Alloc TT=4F The configured messages will be sent over the Application Message Service (AMS). The TelLen and TelId byte in the payload area of the Hexdump is ignored. The length of the message is determined by the number of bytes in the payload area. PPPPPP…PP Payload hex dump | DDDD | Destination address | TT=00 | Normal control message | TT=01 | RemoteRead | TT=02 | RemoteWrite | TT=03 | Alloc | TT=4F | The configured messages will be sent over the Application Message Service (AMS). The TelLen and TelId byte in the payload area of the Hexdump is ignored. The length of the message is determined by the number of bytes in the payload area. | PPPPPP…PP | Payload hex dump |
| DDDD | Destination address |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TT=00 | Normal control message |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TT=01 | RemoteRead |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TT=02 | RemoteWrite |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TT=03 | Alloc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TT=4F | The configured messages will be sent over the Application Message Service (AMS). The TelLen and TelId byte in the payload area of the Hexdump is ignored. The length of the message is determined by the number of bytes in the payload area. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PPPPPP…PP | Payload hex dump |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| More Group | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Appearance |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Border Color | Here you change the color of the frame. This setting depends on the set Button Style. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Button Style | Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Hover Color | Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Image | Here you can assign a image to the Button. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Image Align | If a image is assigned to the Button you can change the position of the image here. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Text Align | .Here you change the position of the Text. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Transparent Color | Change the transparent color. The picture transparency is always active. You must only define the color for which the picture should be transparent. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Use Transparent Color | Here you can set if the transparency should really be used. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Use Windows Style | Here you select whether the set background color Background Color is to be taken into account when Windows styles are used: If this property is True, the button is always displayed in the respective style, and the set background color is ignored. If this property is False, the set background color is taken into account. In the Windows style classic, the set background color is always taken into account, regardless of this property. Note The display of the Background Color depends on the Use Windows Style setting. | Note The display of the Background Color depends on the Use Windows Style setting. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note The display of the Background Color depends on the Use Windows Style setting. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Group: — | Layout |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

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

Background Color

Here you change the background color of the text.

Text Align

With a click on the symbol you align the text on the left site of the control.

With a click on the symbol you align the text in the middle of the control.

With a click on the symbol you align the text on the right site of the control.

Send Settings Group

Settings

Wait for Ack

With a click on the symbol you activate/deactivate waiting for a Tx acknowledgment of a sent message, before the next message will be sent.

Timeout (ms)

Timeout

Here you change the maximum waiting time for an acknowledgment of a sent message before the next message is sent.

Delay (ms)

Delay

Here you change the waiting time between messages that have to be sent.

Channel

Device Name

Here you change the channel on which the messages should be sent. (MOST1, MOST2, …).

Message Hex Dump

Message HexDump

Here you specify the messages to be sent.

Separate particular messages with a comma.

Format: XXXXDDDDTTPPPPPP

DDDD

Destination address

TT=00

Normal control message

TT=01

RemoteRead

TT=02

RemoteWrite

TT=03

Alloc

TT=4F

The configured messages will be sent over the Application Message Service (AMS). The TelLen and TelId byte in the payload area of the Hexdump is ignored. The length of the message is determined by the number of bytes in the payload area.

PPPPPP…PP

Payload hex dump

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance

Border Color

Here you change the color of the frame. This setting depends on the set Button Style.

Button Style

Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed.

Hover Color

Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style.

Image

Here you can assign a image to the Button.

Image Align

If a image is assigned to the Button you can change the position of the image here.

.Here you change the position of the Text.

Transparent Color

Change the transparent color.

The picture transparency is always active. You must only define the color for which the picture should be transparent.

Use Transparent Color

Here you can set if the transparency should really be used.

Use Windows Style

Here you select whether the set background color Background Color is to be taken into account when Windows styles are used:

In the Windows style classic, the set background color is always taken into account, regardless of this property.

Note

The display of the Background Color depends on the Use Windows Style setting.

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Assigning Controls | Transparency Color

| DDDD | Destination address |
|---|---|
| TT=00 | Normal control message |
| TT=01 | RemoteRead |
| TT=02 | RemoteWrite |
| TT=03 | Alloc |
| TT=4F | The configured messages will be sent over the Application Message Service (AMS). The TelLen and TelId byte in the payload area of the Hexdump is ignored. The length of the message is determined by the number of bytes in the payload area. |
| PPPPPP…PP | Payload hex dump |

| Note The display of the Background Color depends on the Use Windows Style setting. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
