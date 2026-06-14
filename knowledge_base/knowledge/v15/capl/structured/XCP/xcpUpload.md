# xcpUpload

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpUpload (char namespace[], char variable[], long errorIndication);
```

## Description

Initiates an upload of the XCP parameter from ECU and updates the dedicated system variable.

After finishing of the upload the callback function OnXcpUpload is called to indicate the upload status.

Use the return value of xcpUpload to check if an error occurred during initiation of the upload.

Use the errorIndication parameter of the OnXcpUpload callback function to check for errors occurred during the upload, if an error during call of xcpUpload occurs OnXcpUpload is not called.

## Parameters

| Name | Description |
|---|---|
| namespace | Namespace of the corresponding system variable. |
| variable | Name of the corresponding system variable. |
| sysvar | Name of the fully qualified name of the system variable, including all name spaces, separated by "::".The name must be preceded by "sysvar::" |
| errorIndication | 0: OK -4: Device is not connected |

## Example

```c
testcase TC_SignalInactive ()
{
xcpUpload("XCP::ECU","testword0");
....

}
//Callback function:
void OnXcpUpload (char namespace[], char variable[], long returnValue)
{
if (returnValue==0)
write("Systemvariable updated: %s %s", namespace,variable);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | 13.0 | — | — | 1.0 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
