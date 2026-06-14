# testGetTestUnitName

> Category: `Test` | Type: `function`

## Syntax

```c
testGetTestUnitName(char testUnitName[], long bufferSize);
```

## Description

Returns the name of the test unit. After your call of this function the name will be inside the character array testUnitName. The maximum length of the name is the length of the character array. This length will be saved in bufferSize.

## Example

```c
testcase TCExample()
{
  char name[100];

  testCaseComment("Test Unit:");
  testGetTestUnitName(name, elcount(name));
  testCaseComment(name);
}
```

## Availability

| Since Version |
|---|
