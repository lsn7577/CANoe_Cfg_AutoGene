# distObjContainerRef

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjContainerRef *
distObjContainerRef <Typedef name>
```

## Description

References a container of distributed objects or references.

The types provide an overload for the subscript operator to access the elements which have a distObjRef, distObjReferenceRef, or distObjContainerRef type. The wildcard container type (distObjContainerRef *) cannot be used with the subscript operator but it is possible to downcast it with a runtime check to a more specialized type.

The leaf elements of containers can be iterated over with a for loop (same syntax as C++ range-based for loop). The leaf elements are visited in the same order as in a depth-first search. Invalid elements (only possible in object containers) are skipped.

Containers are not covariant in their element type, as they are mutable.

## Parameters

| Name | Description |
|---|---|
| Typedef name | The fully qualified name of a distributed object or reference container. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {
    internal data int32 d;
  }
  typedef ObjListType  = list<SomeInterface>;
  typedef ObjArrayType = array<SomeInterface, 42>;
  typedef RefListType  = list<reference<SomeInterface>>;
  typedef RefArrayType = array<reference<SomeInterface>, 42>;

  ObjListType  ObjList;
  ObjArrayType ObjArray;
  RefListType  RefList;
  RefArrayType RefArray;
  array<array<SomeInterface, 42>, 42> NestedArray;
}

// CAPL
on start {
  UseVariable();
  SubscriptOperator();
  Iterate();
}

void UseVariable() {
  // variable declarations
  distObjContainerRef * c1;
  distObjContainerRef SomeNamespace::ObjListType  c2 = ObjList;
  distObjContainerRef SomeNamespace::ObjArrayType c3 = ObjArray;
  distObjContainerRef SomeNamespace::RefListType  c4 = RefList;
  distObjContainerRef SomeNamespace::RefArrayType c5 = RefArray;

  // check if a valid container is referenced
  write("%d", c1.IsValid); // output: 0
  write("%d", c2.IsValid); // output: 1

  // type conversions (checked at runtime)
  c1 = c2;                                  // implicit upcast
  c2 = (distObjContainerRef ObjListType)c1; // explicit downcast

  // check the name and path of the container
  write("%s", c1.Name); // output: ObjList
  write("%s", c1.Path); // output: SomeNamespace::ObjList
}

void SubscriptOperator() {
  write("%s", ObjArray[2].Name);       // output: ObjArray[2]
  write("%s", RefArray[2].Name);       // output: RefArray[2]
  write("%s", NestedArray[2][3].Name); // output: NestedArray[2][3]
}

void Iterate() {
  for (distObjRef SomeInterface obj : ObjArray) {
    write("%s", obj.Path)
  }
  for (distObjReferenceRef SomeInterface ref : RefArray) {
      write("%s", ref.Path)
  }
  for (distObjRef SomeInterface obj : NestedArray) {
    write("%s", obj.Path)
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | 15 | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
