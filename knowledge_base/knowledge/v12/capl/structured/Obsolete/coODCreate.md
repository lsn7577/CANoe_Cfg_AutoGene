# coODCreate

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coODCreate( dword index, dword subIndex, dword dataType, dword access, dword errCode[] ); // form 1
```

## Description

Generates a new object in the local object dictionary. If the object already exists, it is replaced by the new object.

Form 1 generates a new object of the specified type and without a start value. The value of the object is initialized with null.

Form 2 generates a new object of the specified type with the specified initial data. If the length of the available start data is smaller than the size of the object, the remaining part is initialized with null.

Form 3 generates a new special object, with the internally assumed data type Domain. This object reads from and/or writes to a file on the local file system.

## Return Values

—

## Example

```c
dword errCode[1];
char data[10] = "myDevice";

// manufacturer device name
coODCreate( 0x1008, 0x0, 0x9, 0, data, elCount(data), errCode );
if (errCode[0] == 0) {
  write( "String object [0x1008] created" );
}

coODCreate( 0x2000, 0x0, 1, "./myFile.txt", errCode );
if (errCode[0] == 0) {
  write( "File object [0x2000] created" );
}
```

## Availability

| Up to Version |
|---|
