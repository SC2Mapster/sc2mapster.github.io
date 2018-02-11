---
title: Testing your map without using the editor
date: 2018-02-07 08:04:00 Z
categories:
- UI
tags:
- ui
- layout
author: Alevice
layout: post
---

## Introduction

While the editor is a massively powerful tool for your map development, it is also pretty slow and on lower systems, it can tax a lot of your system resources. Sometimes it is preferable to work directly with the map/mod data files and test changes quickly. As you may or may not know, the game executable allows you to run your maps and mods (packed or unpacked as SC2components) using command line. The syntax is as follows:

```
SC2Switcher.exe -run <map>  -displaymode <mode> -trigdebug -preload <preload> -NoUserCheats 
	-reloadcheck -meleeMod <melee> -difficulty <diff> -speed <speed> -testmod <mod>

PARAMETERS:

-run			(REQUIRED) Runs the specified map
	<map>		Map filename. Can be relative or absolute path. Relative path
				assumes Maps\ folder under SC2 installation folder.
				Eg:
					-run "MyMap.SC2Map"
					-run "D:\Path\To\MyMap.SC2Map"
-testmod    
	<mod>		Mod filename. Can be relative or absolute path. Relative path
				assumes root SC2 installation folder.
				Eg:
					-testmod "Mods\MyMod.SC2Mod;ComponentList.SC2Components"
					-testmod "D:\Path\To\MyMod.SC2Mod;ComponentList.SC2Components"

-displaymode	Sets wether SC2 should be run windowed or fullscreen
	<mode>		0 - Windowed
				1 - Windowed Fullscreen
				2 - Fullscreen
-trigdebug		Causes the Trigger Debug window to open on load finish.

-preload		Sets wether resources should be preloaded or not
	<preload>	0 - No
				1 - Yes

-NoUserCheats	Unknown

-reloadcheck	Unknown

-meleeMod		Sets default Melee Mode when loading a melee map
	<melee>		Liberty
				Swarm
				Void
-difficulty		Sets the AI difficulty
	<diff>         1 - Casual
				2 - Normal
				3 - Hard
				4 - Brutal

-speed			Sets the initial game speed
	<speed>     0 - Slower 
				1 - Slow
				2 - Normal
				3 - Fast
				4 - Faster
```

While it is good those command exist, the syntax at time sproves unwieldy on its own when you just want to test. The nice thing, at least on windows, is that we can register those commands directly as context menu entries on your SC2Map and SC2Mod files and even on your Component folders. You do this through registry editing.

To make your life simpler, I have setup a Registry file you can deploy [here]({{ "/assets/files/SC2Submenu.reg.txt" | absolute_url }}). You will need to tweak, however. All instances of `D:\\Games\\StarCraft II\\Support64\\SC2Switcher_x64.exe` will need to be replaced with your correct SC2 install directory. Also, for testing mods, you will need to replace all the instances of `DummyTestMap.SC2Map` with a valid map file you have; I highly recommend to have a barebones map with a start location and resources nearby for both melee and custom mod testing, perhaps with a few debug triggers of your own design (but i can also recommend for the most part just using the debugger and the test document cheats available).

Once you have installed your regsitry file correctly, you will see something like this:

![Context menu for map files]({{ "/assets/posts/2018-02-10-testing-map-without-editor/mapcontextmenu.png" | absolute_url }})

![Context menu for mod files]({{ "/assets/posts/2018-02-10-testing-map-without-editor/modcontextmenu.png" | absolute_url }})

![Context menu for folders]({{ "/assets/posts/2018-02-10-testing-map-without-editor/foldercontextmenu.png" | absolute_url }})

When you work with Component folders, you have the gained extra benefit that you can edit your data files while the game is running, save, go back to the game and just restart the map (if you are using an english localization, you can just press this hotkey sequence  `F10 -> d -> r`). Generally this reloads get significantly faster.