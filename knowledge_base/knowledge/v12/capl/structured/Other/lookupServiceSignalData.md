# lookupServiceSignalData

> Category: `Other` | Type: `function`

## Syntax

```c
serviceSignalData * lookupServiceSignalData(char serviceSignalName[]);
```

## Description

Searches for a SOME/IP Service Signal in the database(s). If the Service Signal is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid serviceSignal.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

lookupServiceSignalData can be used to access a Service Signal, which was specified by a string during measurement. The function makes it possible to write dynamic tests with Service Signals, where the name of the Service Signal is not given at compile time.

lookupServiceSignalData is for Service Signals, which can be represented as data (byte array). For number and string types see lookupServiceSignalNumber and lookupServiceSignalString.

## Return Values

The found unique Service Signal or an invalid object.

## Example

```c
// set the data of some service-signals to empty data

int i;
char serviceSignalNames[2][70] = 
{ "sif_001::TrafficSignDetection::DetectedTrafficSign.SignData",
  "sif_2001::TrafficSignDetection::DetectedTrafficSign.Image" };
byte emptyData[8] = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };

for( i = 0; i < elcount(serviceSignalNames); i++ )
{
  serviceSignalData * sig;
  sig = lookupServiceSignalData( serviceSignalNames[i] );

  SetServiceSignalData( sig, emptyData, elcount(emptyData) );
}
```

## Availability

| Since Version |
|---|
