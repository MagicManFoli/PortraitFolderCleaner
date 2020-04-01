# PortraitFolderCleaner

This tool is used to clean up the folder structure created by Portrait Mode. 

1. all portrait photos will have their blurred photo moved to the parent directory
1. folders with remaining clear photos will be deleted
1. Empty folders will be deleted

Result will be a flat directory without subfolders.

```
./
- photo1
- IMG2
 - clear2
 - blurred2
- IMG3
 - clear3
 - blurred3
- photo4
- photo5
```
turns into 
```
./
- photo1
- blurred2
- blurred3
- photo4
- photo5
```

Usage:
  PFC.exe --path YOUR/PATH/

If no path was specified a prompt will be displayed.

**Use at your own risk!**

This will apply to owners of Google Pixel smartphones and maybe even some other manufacturers with a similar functionality.
