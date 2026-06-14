# GPIBResponse

> Category: `GPIB` | Type: `function`

## Syntax

```c
GPIBResponse (long deviceDescriptor, char queryString[], char resultString[]);
```

## Description

This function is called when the query returns. Users must implement this function and receive the original query string, the result as a string and the device ID.

## Parameters

| Name | Description |
|---|---|
| deviceDescriptor | The Device Descriptor of the device, that transmitted the response. |
| queryString | The data transmitted in the GPIBQuery or GPIBQueryEx call, respectively. |
| resultString | The device response. |

## Return Values

—

## Example

```c
char myQuery[3] = "V?";
GPIBQuery(myDevice, "V?");
...
GPIBResponse 
 (long deviceDescriptor, char queryString[], char resultString[])
{
   if 
 (deviceDescriptor == myDevice)
   {
      if 
 ( !strncmp(queryStr, myQuery, len))
      {
         putValue(EnvVoltage, GPIBGetFloatResult(resultString));
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.1 SP2 |
| Restricted To | — | GPIB | — | — | — | GPIB |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
