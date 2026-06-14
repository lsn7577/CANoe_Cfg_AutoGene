# vFlashGetFlashAttributeConfigValue, vFlashGetFlashAttributeLastRunValue, vFlashSetFlashAttribute

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long vFlashGetFlashAttributeConfigValue(char flashAttributeName[], char valueOut[], dword maxLen); // form 1
long vFlashGetFlashAttributeLastRunValue(char flashAttributeName[], char valueOut[], dword maxLen); // form 2
long vFlashSetFlashAttribute(char flashAttributeName[], char attributeValue[]); // form 3
```

## Description

Get the value of a Flash attribute, either as configured in the vFlash project (form 1), or the value set by the flash procedure the last time the flash project was executed (form 2). It is also possible to set the value of the Flash attribute (form 3) used for next execution (not persistently in project).

## Parameters

| Name | Description |
|---|---|
| flashAttributeName | Name of the attribute as shown in vFlash. |
| valueOut | Buffer for returning the value of the attribute. |
| maxLen | Length of the buffer provided. |
| attributeValue | New value of the attribute, as text. Note that it must be possible to convert the text into the type defined for the attribute. For example, integer attributes accept only values in the form 1234 or 0xABC, otherwise an error is returned. |

## Example

```c
char valueOut[200];
char attributeName[30] = "Flash Attribute";

// Read the value configured in the project
vFlashGetFlashAttributeConfigValue(attributeName, valueOut, elcount(valueOut));

// Set the value to use the next time
vFlashSetFlashAttribute(attributeName, "1234");

// perform flashing
TestWaitForvFlashReprogrammed();

// Retrieve the value the flash procedure might have set during the last run
vFlashGetFlashAttributeLastRunValue(attributeName, valueOut, elcount(valueOut));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 + DLL 6.0.4100 | — | — | — | 6 + DLL 6.0.4100 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
