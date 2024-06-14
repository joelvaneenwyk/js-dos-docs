# Fork (Clone) Drive

sockdrive acts as a repository of disks, allowing you to choose any available disk and make a 
copy of it. However, to do this, you need to be registered on the js-dos platform and have a 
subscription.

After successful authentication, you will see a list of all your disks.

![My Drives](my-drives.jpg)

## How to Fork

> [js-dos subscription](Subscription.md) is required for disk cloning and writing
> 
{style="note"}

You are able to fork any drive that in visible list. The list contains your drives as well as
system drives. 

1. Open drives sidebar
2. Press **Fork** button
3. Enter the drive name (rember it)
4. Press **Fork** button

![How to fork](fork.jpg)

## Delete drive

Press the corresponding **Delete** button.

> This operation cannot be undone.
>
{style="warning"}

> We will really appreciate if you delete unused images
> 
{style="note"}

## How to boot with empty drive

Empty drives are just formatted drives without any data. It's a good choice if you want to start with
blank image. But because they are empty, you can't boot from it. You need to install some OS to boot from
empty drive.

1. To do this, you need first boot with newly created drive. The easiest way to do it is to download DOS bootable
diskette. You can get one [here](https://cdn.dos.zone/custom/tools/dos.img) (dos.img).

2. Open [studio](https://dos.zone/studio-v8/), pick your forked drive as **C:** and press **Play**
![pick drive](set-drive.jpg)
{style="block"}

3. Open FS sidebar, press upload file select `dos.img` from.
![boot from A:](boot-from-a.jpg)
{style="block"}

4. Type `imgmount a: dos.img` to mount image as drive **A:**
5. Now boot from **A:** by typing `boot a:`
6. When you booted, you can change to drive **C:**. Do what you want: copy files, [install OS](install-windows.md), etc.
![drive C:](drive-c.jpg)
{style="block"}