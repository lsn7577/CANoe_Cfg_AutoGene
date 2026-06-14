# mostParamGetString

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamGetString (mostAmsMessage msg, char paramAdr[], char buffer[], long buffersize)
```

## Description

Query of parameters of the String type from an AMS message using the parameter name from the XML function catalog.

This function supports ASCII-coded strings only. In case of other string encoding use the function mostParamGetData.

The message data must contain a parameter with the given parameter address.

Since the compiler is not able to validate this, errors are detected at run time of the CAPL program only. If the parameter is not part of the message or not the expected type, an error text is displayed in the Write Window and the measurement stops. The function mostParamIsAvailable can be applied to assure parameter availability.

## Return Values

>=0: Number of copied bytes.
<0: See error codes

## Availability

| Since Version |
|---|
