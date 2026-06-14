# J1939TestCommand

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestCommand( pg* command, pg* response, dword responseSize, dword timeout, dword options )//form 1
```

## Description

A command message is sent from the test module. The DUT must respond with the response message.

For the form 1, the source address of the configured command message is used as a destination address of the expected response message, and the source address of the configured response message is used as the destination address of the sent command message. This shortens the parameter list, but results in only the source addresses of the command and response message are used; destination addresses being automatically calculated.

For the form 2, the address of the commandNode is used as a source address of the sent command message and as a destination address of the expected response message, and the address of the responseNode is used as the destination address of the sent command message and as the source address of the expected response message. The both database nodes commandNode and responseNode need a defined NmStationAddress attribute.

J1939TestCommand is not able to send a command message as a broadcast. This function can only stimulate point-to-point communication.

## Example

```c
pg VTtoECU vt_to_ecu;
pg ECUtoVT ecu_to_vt;

vt_to_ecu.command = 12;
if (J1939TestCommand( VT, Sprayer, vt_to_ecu, ecu_to_vt, 100, 8, 0 ) != 1) {
  testFail( "Response from Sprayer not received" );
}
if (ecu_to_vt.Signal != 100) {
  testStepFail( "Wrong response from Sprayer" );
}
```

## Availability

| Since Version |
|---|
