# lookupServiceSignalNumber

> Category: `Other` | Type: `function`

## Syntax

```c
serviceSignalNumber * lookupServiceSignalNumber(char serviceSignalName[]);
```

## Description

Searches for a SOME/IP Service Signal in the database(s). If the Service Signal is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid serviceSignal.

lookupServiceSignalNumber can be used to access a Service Signal, which was specified by a string during measurement. The function makes it possible to write dynamic tests with Service Signals, where the name of the Service Signal is not given at compile-time.

lookupServiceSignalNumber is for Service Signals, which can be represented as number. For data and string types see lookupServiceSignalData and lookupServiceSignalString.

## Parameters

| Name | Description |
|---|---|
| serviceSignalName | The qualifier of the Service Signal. |

## Return Values

The found unique Service Signal or an invalid object.

## Example

```c
// set the values of some service-signals

int i;
char serviceSignalNames[3][70] = 
{ "sif_2001::TrafficSignDetection::DetectedTrafficSign[0].DistanceToSign",
  "sif_2001::TrafficSignDetection::DetectedTrafficSign[0].Reliability",
  "sif_2001::TrafficSignDetection::DetectedTrafficSign[0].SignType" };
double serviceSignalValues[3] = { 1.0, 2.0, 3.0 };

for( i = 0; i < elcount(serviceSignalNames); i++ )
{
  serviceSignalNumber * sig;
  sig = lookupServiceSignalNumber( serviceSignalNames[i] );

  $sig = serviceSignalValues[i];
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
