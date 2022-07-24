# SCE Development Environment
Command line tool to run any of the SCE projects. Works on Windows, Mac and
 Linux. Available with the `sce` command.

## Setup
Before starting, clone this repository to your computer with
```
git clone https://github.com/SCE-Development/SCE-CLI.git
```
Next, we will add the `sce` command to your terminal.

### Windows
You will need to add the location where the batch file is to your path. To do
 this:
1. Copy the path where `SCE-CLI` is installed. The path should look like
```
C:\Users\<username>\path\to\SCE-CLI\
```
2. We need to edit (your env vars or something) we can do this with:
- Press `Window + R` to open the Windows Run prompt.
- Type in `sysdm.cpl` and click `OK`.
![image](https://phoenixnap.com/kb/wp-content/uploads/2021/04/setting-environment-variables-in-windows-06.png)
- Then go to the `Advanced` tab and click `Environment Variables`:
![image](https://phoenixnap.com/kb/wp-content/uploads/2021/04/setting-environment-variables-in-windows-07.png)
- Click on path in `System variables`
![edit_path](https://user-images.githubusercontent.com/10038262/180634975-6a7c7947-5560-4df6-bd5a-3d8bda033c70.png)
- Add the location where `SCE-CLI` is installed from earlier into
 this path (see highlighted)
![path](https://user-images.githubusercontent.com/10038262/180634962-abd4ba91-30a2-47e7-8c50-4cc26a41b669.png)
3. After doing so, typing `sce` in the Command Prompt
 should work, and the help page should show like below:
![eb2015026b076e7b31a8caa2ff8f2e55](https://user-images.githubusercontent.com/10038262/180635207-2ea70c08-003f-4f59-95f8-35817bc6a51b.png)
