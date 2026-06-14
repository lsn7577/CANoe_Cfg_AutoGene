# DoIP_SelectVehicle

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_SelectVehicle(byte EID[6]);
long DoIP_SelectVehicle(char VIN[]);
```

## Description

Specify which vehicle the tester shall target, i.e. indicate in the Vehicle Identification Request Message, or select one of the responding vehicles for communication.

To set the VIN and EID in an ECU simulation use the DoIP.DLL functions DoIP_SetEID and DoIP_SetVIN.

## Parameters

| Name | Description |
|---|---|
| EID | (6 bytes) entity ID, typically an Ethernet MAC address. |
| VIN | The vehicle identification number (17 characters). If an empty string is given, VIR messages without parameter are sent. |

## Return Values

Error code

## Example

```c
TestCase TC_AccessVehicle1
{
  diagRequest ReadEcuInfo req;

  DiagSetTarget( "ECU1"); // a DoIP description

  // --- start VIR targeting a specific vehicle via its VIN

  DoIP_SelectVehicle( "VECT0RVEH1CLE0123");

  req.SendRequest();
  // A VIR with VIN should be responded quite fast
  TestWaitForDiagResponse( req, 1000);

  diagCloseChannel(); // make sure that another VIR will be sent

  // --- send VIR without indicating a vehicle

  DoIP_SelectVehicle( ""); // no-parameter-VIR-message

  req.SendRequest();
  // A VIR without parameter may take a long time, including repeats
  TestWaitForDiagResponse( req, 9000);

  diagCloseChannel();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
