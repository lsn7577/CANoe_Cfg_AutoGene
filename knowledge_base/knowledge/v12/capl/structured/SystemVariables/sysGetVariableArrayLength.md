# sysGetVariableArrayLength

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
dword sysGetVariableArrayLength(char namespace[], char variable[]); // form 1
```

## Description

Returns the length of the array of the system variable.

## Return Values

For system variables of type data, returns the current size (in bytes) of the value.
For system variables of type long or float array, returns the number of elements in the array.
For system variables of type string, returns the length of the string, excluding the terminating 0 character.
For system variables of type long or float, returns 1.

## Example

```c
// calculate the norm of a vector
dword length, i;
double element, sum, norm;
sum = 0.0;
length = sysGetVariableArrayLength(sysvar::MyVariables::MyVector);
for (i = 0; i < length; ++i) 
{
   element = @sysvar::MyVariables::MyVector[i];
   sum += element * element;
}
norm = sqrt(sum);
```

## Availability

| Since Version |
|---|
