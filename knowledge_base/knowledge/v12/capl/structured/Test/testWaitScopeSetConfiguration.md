# testWaitScopeSetConfiguration

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeSetConfiguration (char deviceName[], char configurationName[]);
```

## Description

Configures the appropriate oscilloscope with the specified configuration.

Hint: The possible device names and configurations names can be requested with the function testWaitScopeGetConfigurationInformation

## Return Values

1 - Successful

## Example

```c
void SetScopeConfiguration()
{
  long res;

  res = testWaitScopeSetConfiguration(“Scope_1”, “MyConfiguration”);

  if (res != 1)
  {
    testStepFail("SetConfiguration","Set configuration MyConfiguration of Scope_1 was not possible. Result = %d", res);
  }

  else

  {
    testStepPass("SetConfiguration", "Configuration of Scope_1 is set to MyConfiguration”);
  }

}
```

## Availability

| Since Version |
|---|
