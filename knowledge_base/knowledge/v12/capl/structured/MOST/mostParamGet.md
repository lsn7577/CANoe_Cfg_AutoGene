# mostParamGet

> Category: `MOST` | Type: `function`

## Syntax

```c
double mostParamGet (mostAmsMessage msg, char paramAdr[])
```

## Description

Query of a parameter value from an AMS message using the parameter name from the XML function catalog.

Suitable for parameter types 'Number', 'Enum', 'BitField' and 'Bool'.

For parameters of type 'Array' or 'Sequence' the size (number of elements) of the parameter is retrieved. The array size cannot be determined, if the parameter 'Pos' selects only one array element.

The message data must contain a parameter with the given parameter address.

Since the compiler is not able to validate this, errors are detected at run time of the CAPL program only. If the parameter is not part of the message or not the expected type, an error text is displayed in the Write Window and the measurement stops. The function mostParamIsAvailable can be applied to assure parameter availability.

## Return Values

Raw value of the parameter. No conversion formula is applied.

## Example

```c
mostAmsMessage AudioDiskPlayer.MediaInfo.Status msg;
int arraySize;
mostParamSet(msg, "Pos", 0x0200); // second array element selected
arraySize = mostParamGet(msg, 
 "Data"); // Return value '0'
```

## Availability

| Since Version |
|---|
