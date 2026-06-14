# testGetCurrentTestCaseTitle

> Category: `Test` | Type: `function`

## Syntax

```c
testGetCurrentTestCaseTitle(char testCaseTitle[], long bufferSize);
```

## Description

Returns the name of the current test case. After your call of this function the name will be inside the character array testCaseTitle. The maximum length of the name is the length of the character array. This length will be saved in bufferSize.

## Example

```c
testcase TCExample()
{
  char title[100];

  testCaseComment("Test Case:");
  testGetCurrentTestCaseTitle(title, elcount(title));
  testCasecomment(title);
}
```

## Availability

| Since Version |
|---|
