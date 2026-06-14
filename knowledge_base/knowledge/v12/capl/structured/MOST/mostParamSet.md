# mostParamSet

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSet(mostAmsMessage msg, char paramAdr[], double value)
```

## Description

Setting of a parameter value in an AMS message using the parameter name from the XML function catalog.

Suitable for parameter types 'Number', 'Enum', 'BitField' and 'Bool'.

For parameters of the 'Enum' type, the numeric value can be specified. The mostParamSetString function can be used to set the symbolic value.

For arrays and sequences the size (number of elements) of the parameter is set. The array size cannot be set, if the parameter 'Pos' selects only one array element.

The message data must contain a parameter with the given parameter address.

Since the compiler is not able to validate this, errors are detected at run time of the CAPL program only. If the parameter is not part of the message or not the expected type, an error text is displayed in the Write Window and the measurement stops. The function mostParamIsAvailable can be applied to assure parameter availability.

When using function mostParamSet to build a message dump, the parameters must be populated in the order specified by the MOST Function Catalog, particularly for messages with StreamCases.

## Return Values

See error codes

## Example

```c
mostAmsMessage AudioDiskPlayer.MediaInfo.Status msg;

mostParamSet(msg, "Pos", 0x0200); // second array element selected
mostParamSet(msg, "Data", 6); // Returns an error code at run time! Array size can only be set if Pos selects all array 

elements.
```

## Availability

| Since Version |
|---|
