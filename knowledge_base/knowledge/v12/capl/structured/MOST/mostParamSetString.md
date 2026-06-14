# mostParamSetString

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSetString (mostAmsMessage msg, char paramAdr[], char value[])
```

## Description

Setting of parameters of the String type (for ASCII-coded strings only) or of the 'Enum' type in an AMS message using the parameter name from the XML function catalog.

This function supports ASCII-coded strings only. In case of other string encoding use the function mostParamSetData. For enumerations, the parameter value can be indicated symbolically. The mostParamSet function can be used to set the numeric value.

The message data must contain a parameter with the given parameter address.

Since the compiler is not able to validate this, errors are detected at run time of the CAPL program only. If the parameter is not part of the message or not the expected type, an error text is displayed in the Write Window and the measurement stops. The function mostParamIsAvailable can be applied to assure parameter availability.

When using function mostParamSetString to build a message dump, the parameters must be populated in the order specified by the MOST Function Catalog, particularly for messages with StreamCases.

## Return Values

See error codes

## Availability

| Since Version |
|---|
