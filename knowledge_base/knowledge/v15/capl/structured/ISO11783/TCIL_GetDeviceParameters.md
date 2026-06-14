# TCIL_GetDeviceParameters

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetDeviceParameters(byte addressClient, char designator[], char version[], byte deviceName[], char serialNumber[], byte structureLabel[], dword& lengthOfStructureLabel, byte localizationLabel[])); // form 1
long TCIL_GetDeviceParameters(dbNode tc, byte addressClient, char designator[], char version[], byte deviceName[], char serialNumber[], byte structureLabel[], dword& lengthOfStructureLabel, byte localizationLabel); // form 2
```

## Description

Returns parameters of the client device which are contained in the Device XML element (DVC) of the device description.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function. |
| addressClient | Address of the TC client node the data entity belongs to. |
| designator | Returns the device designator of the client device (as a NULL-terminated string). |
| version | Returns the software version of the client device (as a NULL-terminated string). |
| deviceName | Returns the NAME of the client device (as a byte array). |
| serialNumber | Returns the serial number of the client device (as a NULL-terminated string). |
| structureLabel | Returns the label of device descriptor structure (as a byte array). |
| lengthOfStructureLabel | Returns the length of the structureLabel. |
| localizationLabel | Returns the label of the device descriptor localization (as a byte array). |

## Example

Example (Form 2, applicable in a test node)

```c
long result;
char designator[33];
char version[33];
byte deviceName[8];
char serialNumber[33];
byte structureLabel[33];
dword lengthOfStructureLabel;
byte localizationLabel[7];

result = TCIL_GetDeviceParameters(TC, clientAddress, designator, version, deviceName, serialNumber, structureLabel, lengthOfStructureLabel, localizationLabel);
if (result < 0)
{
  write("TCIL_GetDeviceParameters failed with error %i", result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14.0 SP2 | 13.0 | — | — | 5.0 SP2 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
