# Selected Databases

> Category: `DBC` | Subcategory: `windows` | Type: `concept`

To show a CANopen database (CODB) in the application the wanted database files have to be added to the database list after clicking button [Add]. In the new dialog one or more files can be selected. By default all new database files are marked by a check mark. Pressing [Ok] shows the database objects of the marked files in the Database Window.

It is possible to mark and unmark files with a click on the check box, by pressing <Enter> or the space bar.

Note

Vector delivers some databases together with the tool. For the current release of these databases or additional databases, the CiA® office should be contacted.

The order of the files in the dialog is important because objects with the same index or sub index, which are contained in different database files, are overwritten. Only the multiple object of the last file appears in the database window. Therefore the files in the list box can be moved by the buttons [Up] and [Down]. If the check box Check if objects are overwritten by a succeeding database is selected, a dialog informs about overwritten objects and in the database window these objects are marked.

In the column Object Shift a value can be set to shift the indexes of database objects in the range from 6000h to 6700h. This is useful for Multiple Device Modules. Objects outside this index range are not shifted (e.g. object 1000h). For more information on Multiple Device Modules see CiA301.

To delete one or more databases the files have to be selected and a click on [Remove] removes the files of the list.

If a database file has sub objects with no corresponding main object and the main object exist in no selected database file, the sub object is not shown in the database window.

| Note Vector delivers some databases together with the tool. For the current release of these databases or additional databases, the CiA® office should be contacted. |
|---|

| Note If a database file has sub objects with no corresponding main object and the main object exist in no selected database file, the sub object is not shown in the database window. |
|---|
