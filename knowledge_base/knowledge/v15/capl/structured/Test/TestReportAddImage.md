# TestReportAddImage

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddImage (char description[], char filename[]); // form 1
TestReportAddImage (char description[], char filename[], char width[], char height[]); // form 2
```

## Description

With this function the reference to a file that contains an image can be taken over into the protocol. This command can be used in the context of the test module and also in the context of a test case.

The existence of the file is not checked.

A file path or URL can be provided for the image. Relative file paths are based on the folder that contains the XML report. If backslashes are used as separators, a double backslash ('\\') must be used to separate directories within the path.

The second variant of this function allows to set the width and/or height with which the image should be displayed in the report. If width or height is specified, the HTML report will automatically show the picture with a link which opens the picture in full size in a new window. The width and height parameters are transferred to the HTML report, their values can be given as pixels or percentage. See an HTML reference for details.

## Parameters

| Name | Description |
|---|---|
| description | Description text for the picture |
| filename | Name of the picture file, possibly with path specification |
| width | Width of the image. |
| height | Height of the image. |

## Return Values

—

## Example

See example: TestReportAdd* Functions

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1: form 1 7.2 SP3: form 2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
