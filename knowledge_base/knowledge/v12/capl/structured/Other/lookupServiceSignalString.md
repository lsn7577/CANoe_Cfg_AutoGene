# lookupServiceSignalString

> Category: `Other` | Type: `function`

## Syntax

```c
serviceSignalString * lookupServiceSignalString(char serviceSignalName[]);
```

## Description

Searches for a SOME/IP Service Signal in the database(s). If the Service Signal is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid serviceSignal.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

lookupServiceSignalString can be used to access a Service Signal, which was specified by a string during measurement. The function makes it possible to write dynamic tests with Service Signals, where the name of the Service Signal is not given at compile time.

lookupServiceSignalString is for Service Signals, which can be represented as string. For data and number types see lookupServiceSignalData and lookupServiceSignalNumber.

## Return Values

The found unique Service Signal or an invalid object.

## Example

```c
// set the string of some service-signals to empty data

int i;
char serviceSignalNames[2][70] = 
{ "sif_001::TrafficSignDetection::DetectedTrafficSign.Name",
  "sif_2001::TrafficSignDetection::DetectedTrafficSign.Description" };
char emptyString[8] = "";

for( i = 0; i < elcount(serviceSignalNames); i++ )
{
  serviceSignalString * sig;
  sig = lookupServiceSignalString( serviceSignalNames[i] );

  SetServiceSignalString( sig, emptyString );
}
```

## Availability

| Since Version |
|---|
