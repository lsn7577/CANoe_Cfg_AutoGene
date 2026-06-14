# C2xSetMapObjectText

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by SetMapObjectText. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long C2xSetMapObjectText( long handle, char text[] ); // form 1 |  |  |  |
| long C2xSetMapObjectText( long handle, char formattedText[], float value ); // form 2 |  |  |  |  |
| Function | Sets text (form 1) or formatted text (form 2) for a map object of the type text. Note makeRGB Up to and including CANoe version 12.0 SP2, the function makeRGB returned the blue value in the second byte and the red value in the fourth byte.Functions that received this value as a parameter interpreted this exchange so that the color was displayed correctly. From CANoe 12.0 SP3, the function makeRGB returns the color values in the correct order.Functions that have received this value as a parameter have also been adjusted to display the correct color again. Existing programs only need to be adapted if you have not used the function makeRGB but you have passed the color hard coded. | Note makeRGB Up to and including CANoe version 12.0 SP2, the function makeRGB returned the blue value in the second byte and the red value in the fourth byte.Functions that received this value as a parameter interpreted this exchange so that the color was displayed correctly. From CANoe 12.0 SP3, the function makeRGB returns the color values in the correct order.Functions that have received this value as a parameter have also been adjusted to display the correct color again. Existing programs only need to be adapted if you have not used the function makeRGB but you have passed the color hard coded. |  |  |
| Note makeRGB Up to and including CANoe version 12.0 SP2, the function makeRGB returned the blue value in the second byte and the red value in the fourth byte.Functions that received this value as a parameter interpreted this exchange so that the color was displayed correctly. From CANoe 12.0 SP3, the function makeRGB returns the color values in the correct order.Functions that have received this value as a parameter have also been adjusted to display the correct color again. Existing programs only need to be adapted if you have not used the function makeRGB but you have passed the color hard coded. |  |  |  |  |
| Parameters | handle Reference of the map object |  |  |  |
| text Text which should be displayed |  |  |  |  |
| formattedText Text with a placeholder for a variable which should be displayed |  |  |  |  |
| value Variable which should be displayed in the text |  |  |  |  |
| Return Values | 0 if success, else the set went wrong |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1 | Car2x | — | • |  |
| Example void DrawTextObject(){ long handle; float timeRemaining = 5.8; handle = C2xCreateMapObject( 8 ); // set position: Motorstraße/Hemminger Straße, D-70499 Stuttgart C2xSetMapObjectPosition(handle, 48.825230, 9.095580); C2xSetMapObjectText(handle, "Traffic Light: time remaining %5.1f s", timeRemaining); C2xSetMapObjectFillColor(handle, makeRGB(0, 0, 0)); C2xDrawMapObject(handle);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
