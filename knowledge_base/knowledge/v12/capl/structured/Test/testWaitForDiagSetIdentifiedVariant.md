# testWaitForDiagSetIdentifiedVariant

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForDiagSetIdentifiedVariant(); // form 1
```

## Description

Performs a variant identification and activates the found variant.

## Return Values

<=0: An error occurred, e.g. a wrong variant Qualifier was used or a communication error occurred.

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
