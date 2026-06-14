# testGetTestConfigurationName

> Category: `Test` | Type: `function`

## Syntax

```c
testGetTestConfigurationName(char testConfigurationName[], long bufferSize);
```

## Description

Returns the name of the test configuration. After your call of this function the name will be inside the character array testConfigurationName. The maximum length of the name is the length of the character array. This length will be saved in bufferSize.

## Example

```c
testcase TCExample()
{
  char name[100];

  testCaseComment("Test Configuration:");
  testGetTestConfigurationName(name, elcount(name));
  testCaseComment(name);
}
```

## Availability

| Since Version |
|---|
