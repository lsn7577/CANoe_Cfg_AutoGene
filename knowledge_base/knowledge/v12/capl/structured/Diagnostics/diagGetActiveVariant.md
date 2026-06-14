# diagGetActiveVariant

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetActiveVariant(char ecuQualifier[], char outputBuffer[], dword bufferSize);
```

## Description

Returns the currently active variant.

## Return Values

Length of qualifier written to buffer, may be truncated.

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

| Since Version |
|---|
