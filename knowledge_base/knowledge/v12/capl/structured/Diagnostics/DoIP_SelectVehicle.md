# DoIP_SelectVehicle

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_SelectVehicle(byte EID[6]);
```

## Description

Specify which vehicle the tester shall target, i.e. indicate in the Vehicle Identification Request Message, or select one of the responding vehicles for communication.

To set the VIN and EID in an ECU simulation use the DoIP.DLL functions DoIP_SetEID and DoIP_SetVIN.

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

| Since Version |
|---|
