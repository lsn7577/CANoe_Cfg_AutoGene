# lookupServiceSignal

> Category: `Other` | Type: `function`

## Syntax

```c
serviceSignal * lookupServiceSignal(char serviceSignalName[]);
```

## Description

Searches for a SOME/IP Service Signal in the database(s). If the Service Signal is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid serviceSignal.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

lookupServiceSignal can be used to access a Service Signal, which was specified by a string during measurement. The function makes it possible to write dynamic tests with a Service Signal, where the name of the Service Signal is not given at compile time.

To access the value of a Service Signal it is necessary to use a more specific variant of lookupServiceSignal depending by the type, see lookupServiceSignalNumber, lookupServiceSignalData and lookupServiceSignalString.

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

| Since Version |
|---|
