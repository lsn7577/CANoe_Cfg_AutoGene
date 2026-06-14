# Map Window API

> Category: `MapWindowAPI` | Type: `notes`

## Description

Initially the object type is defined by means of CreateMapObject. In general the following functions are available independent of the object type:

In addition to this dependent on the object type the following functions can be used:

OnMapObjectClick

SetMapObjectSelectable

variables{ enum mapObjectType { Square = 1, Rectangle = 2, Ellipse = 3, Cross = 4, Triangle = 5, Line = 6, Bitmap = 7, Text = 8 }; long gHandle;}on start{ // init object gHandle = CreateMapObject( Rectangle ); // set position: Ingersheimer Straße 24, D-70499 Stuttgart SetMapObjectPosition(gHandle, 48.824892, 9.094265); // optional settings SetMapObjectHeading(gHandle, 359); SetMapObjectSize(gHandle, 2, 4.5); SetMapObjectFillColor(gHandle, makeRGB(183, 0, 50)); SetMapObjectLineColor(gHandle, makeRGB(76, 76, 76)); SetMapObjectPenStyle(gHandle, 2); SetMapObjectPenWidth(gHandle, 3); // draw object DrawMapObject(gHandle);}on key 'd'{ // delete object DeleteMapObject(gHandle);}

| Function | Object Type |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Square | Rectangle | Ellipse | Cross | Triangle | Line | Bitmap | Text |  |
| OnMapObjectClick | • | • | • | • | • | • | • | • |
| SetMapObjectBmpCount | — | — | — | — | — | — | • | — |
| SetMapObjectBmpFilePath | — | — | — | — | — | — | • | — |
| SetMapObjectBmpIndex | — | — | — | — | — | — | • | — |
| SetMapObjectFillColor | • | • | • | — | • | — | — | • |
| SetMapObjectHeading | • | • | • | • | • | — | • | — |
| SetMapObjectLineColor | • | • | • | • | • | • | — | — |
| SetMapObjectSelectable | • | • | • | • | • | • | • | • |
| SetMapObjectPenWidth | • | • | • | • | • | • | — | — |
| SetMapObjectSize | • | • | • | • | • | — | • | • |
| SetMapObjectText | — | — | — | — | — | — | — | • |
| SetMapObjectVisible | • | • | • | • | • | • | • | • |

| Example variables{ enum mapObjectType { Square = 1, Rectangle = 2, Ellipse = 3, Cross = 4, Triangle = 5, Line = 6, Bitmap = 7, Text = 8 }; long gHandle;}on start{ // init object gHandle = CreateMapObject( Rectangle ); // set position: Ingersheimer Straße 24, D-70499 Stuttgart SetMapObjectPosition(gHandle, 48.824892, 9.094265); // optional settings SetMapObjectHeading(gHandle, 359); SetMapObjectSize(gHandle, 2, 4.5); SetMapObjectFillColor(gHandle, makeRGB(183, 0, 50)); SetMapObjectLineColor(gHandle, makeRGB(76, 76, 76)); SetMapObjectPenStyle(gHandle, 2); SetMapObjectPenWidth(gHandle, 3); // draw object DrawMapObject(gHandle);}on key 'd'{ // delete object DeleteMapObject(gHandle);} |
|---|

| Version 15© Vector Informatik GmbH |
|---|
