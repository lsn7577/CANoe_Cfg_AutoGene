# CarMaker_Connect

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_Connect(char host[], char user[]);
```

## Description

Creates a connection to the CarMaker instance running on the selected host by the given user. If the user name is an empty string, only the host name is used to select the CarMaker instance. An IPv4 address is also accepted as host name.

## Parameters

| Name | Description |
|---|---|
| host | Host name or IP address of the CarMaker host computer. |
| user | Name of the user running the CarMaker instance. If this value is an empty string and multiple CarMaker instances are running on the specified host, any instance is connected. If the special name localuser is given the current user of the CANoe RT kernel is resolved and used for the connection. |

## Return Values

APO return code

## Example

```c
on start
{
  // connect to CarMaker instance
  gErrorState = CarMaker_Connect("localhost", "localuser");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
