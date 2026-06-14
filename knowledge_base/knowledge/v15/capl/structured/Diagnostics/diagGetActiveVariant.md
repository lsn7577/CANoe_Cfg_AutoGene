# diagGetActiveVariant

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetActiveVariant(char ecuQualifier[], char outputBuffer[], dword bufferSize);
long diagGetActiveVariant(char outputBuffer[], dword bufferSize);
```

## Description

Returns the currently active variant.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | If given, returns the active variant of this target. If omitted, the target formerly set by diagSetTarget is used. |
| outputBuffer | Output field |
| bufferSize | Size of the output buffer |

## Return Values

Length of qualifier written to buffer, may be truncated.
Error code

## Example

```c
testcase SetActiveVariantFromSystemVariable()
{
  char variantName[100];
  char outputBuffer[100];
  long retVal;
  diagSetTarget("ECU");

  retVal = sysGetVariableString(sysvar::VariantSwitch::VariantToUse,
  variantName, elcount(variantName));

  if( 0 > retVal)
  {
    testStepFail("", "Could not get variant name from system variable (%d)", retVal);
  }

  retVal = testWaitForDiagChangedActiveVariant(variantName);

  if(0 >= retVal)
  {
    diagGetErrorString(retVal, outputBuffer, elcount(outputBuffer));
    testStepFail("", "Error %d when changing variant (%s)", retVal, outputBuffer);
  }
}

testcase SwitchToIdentifiedVariant()
{
  char variantName[100];
  char outputBuffer[100];
  long retVal;

  diagSetTarget("ECU");

  retVal = testWaitForDiagSetIdentifiedVariant();

  if(0 >= retVal)
  {
    diagGetErrorString(retVal, outputBuffer, elcount(outputBuffer));
    testStepFail("", "Error %d while setting identified variant (%s)", retVal, outputBuffer);
  }

  retVal = diagGetActiveVariant(variantName, elcount(variantName));

  if( 0 > retVal)
  {
    testStepFail("", "Could not get active Variant");
  }

  sysSetVariableString(sysvar::VariantSwitch::ActiveVariant, variantName);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | 2.0 |
| Restricted To | Online mode | Online mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
