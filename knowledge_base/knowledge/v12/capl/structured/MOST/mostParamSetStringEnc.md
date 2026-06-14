# mostParamSetStringEnc

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSetStringEnc (mostAmsMessage msg, char paramAdr[], long encoding, char asciiStr[])
```

## Description

Encoding and setting of parameters of the String type (for ASCII-coded strings only) in an AMS message using the parameter name from the XML function catalog. Only ASCII-coded strings are supported.

The parameter description must go with the message content. The compiler is not able to validate this here. Errors only appear at run time of the CAPL program, if applicable. This function is primarily used to access messages, whose content was previously limited explicitly, e.g. by the declaration. The message must be populated in the order of its parameters particularly for messages with StreamCases. If the parameter is not part of the message or not the expected type, an error message it output in the Write Window and the measurement stops.

## Return Values

See error codes

## Example

-> Message parameter bytes: 00 00 61 00 62 00 63 00 00

```c
mostAmsMessage AmFmTuner.RadioText.Status msg;
mostParamSetString(msg, "TextA", 0x00, "abc");
```

## Availability

| Since Version |
|---|
