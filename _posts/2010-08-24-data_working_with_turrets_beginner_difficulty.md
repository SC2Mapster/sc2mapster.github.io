---
title: Data - Working with Turrets (Beginner Difficulty)
date: 2010-08-24 00:00:00 Z
categories:
- Data
tags:
- data
- turrets
- siteops
author: ProzaicMuse
layout: post
---

Collected from: https://web.archive.org/web/20160603042600/http://www.sc2mapster.com/forums/resources/tutorials/9000-data-working-with-turrets-beginner-difficulty/

Original Author: ProzaicMuse

[Data] Working with Turrets (Beginner Difficulty)

If you're like me, one of the first things you did was add a weapon to a building in the hopes that you could have structures start shooting laser beams at everything that moves. What you probably discovered is that the weapon never fired and you were left with a normal building that just spewed errors at you. This tutorial remedies this problem by walking through the process of creating turrets.


# Turret Basics
While we will be working with attached turret models, they aren't required and are merely for aesthetics. The core parts of any turret are:

* **Turret Object:** This controls the turrets rotation speeds, range of motion and behavior. Without this you WILL get errors any time you try to attack with your `Weapon`. The only exception is if the unit can change its own facing through movement. Thus this is crucial to stationary objects like buildings.
* **Turret Actor:** This is responsible for "turning on" the turret. Without this, your turret won't function even if your `Turret Object` is setup properly. It allows you to control what model rotates (as the turret) and what anchor point to use for the axis. Keep in mind that only certain points can be used. `Turret Z` being the most obvious choice.
* **Weapon:** Once you have your turret setup, you need to attach it to a `Weapon`. Then whenever the `Weapon` would fire, the `Turret Object` will rotate to face its target and fire away. In the case of buildings, you won't see any rotation (unless you chose to), but the `Turret Object` will rotate the invisible, non-existent `Turret Actor` to face the target.


# Turret Hub
## Effects Tab
* Create a new Effect named **NE Turret (Damage)** with **Effect Type: Damage**
  * set **AI Notify Flags**: Hurt Enemy
  * set **Amount**: 10
  * set **Death**: Fire
  * set **Flags**: Notification
  * set **Kind**: Ranged
  * set **Response Flags**: [Acquire/Flee]
* Duplicate 3 times and change **NE** to **NW**, **SE** and **SW**

(Because very little changes between objects I'll be having you duplicate frequently.)

## Weapons Tab
* Create a new Weapon named **NE Turret**
  * set **Effect**: NE Turret (Damage)
  * set **Backswing**: 0
  * set **Damage Point**: 0.3333
  * set **Period**: 1.5
  * set **Damage Display Effect**: NE Turret (Damage)
  * set **Icon**: btn-building-protoss-photoncannon.dds
  * set **Options**: [Can Initiate Attack/Only Fire While Attacking]
  * set **Target Filters**: Exclude [Dead/Hidden/Invulnerable/Missile/Self/Stasis] and Require [Visible]
* Duplicate 3 times and change **NE** to **NW**, **SE** and **SW**
  * set **Damage Point**: 0.6666, 1.0 and 1.3333

These are the Turret weapons that will go on the building.

## Turrets Tab
* Create a new Turret named **NE Turret**
	* set **Idle**: Spin
	* set **Yaw Arc**: 360
	* set **Yaw Idle Rate**: 45
	* set **Yaw Rate**: 360
	* set **Yaw Start**: 0
* Duplicate 3 times and change **NE** to **NW**, **SE** and **SW**

You can set these to whatever you'd prefer, but **Idle** controls the turrets action when not in combat, **Arc** controls its range of motion, **Idle Rate** is how quickly the turret rotates out of combat, **Rate** is how quickly the turret rotates in combat and **Start** determines the angle the turret begins facing.

## Models Tab
* Create a new Model named **Hub Turret**
	* set **Model**: PhotonCannon.m3
* Create a new Model named **Turret Beam**
	* set **Model**: ColossusBeam.m3
* Create a new Model named **Turret Death**
	* set **Model**: PhotonCannonDeath.m3

## Units Tab
Duplicate the Nexus structure and its corresponding Actor. Everything else will be stock or made from scratch.

* Name it **Turret Hub**
	* open **Abilities +** and remove all but [Attack/Stop]
	* open **Command Card +** and remove all but [Attack/Stop]
	* remove everything in **Behaviors +**
	* open **Weapons +** and add **NW/NE/SW/SE Turret** (Weapon and Turret)
* Name the building's Actor **Turret Hub**

## Actors Tab
### Site Operation Actors
* Create a new Actor named **SOpAdjustNE** with **Actor Type: Site Operation (Local Offset)**
	* set **Local Offset**: (0.0, 3.0, 0.0)
* Create a new Actor named **SOpAdjustNW** with **Actor Type: Site Operation (Local Offset)**
	* set **Local Offset**: (-3.0, 0.0, 0.0)
* Create a new Actor named **SOpAdjustSE** with **Actor Type: Site Operation (Local Offset)**
	* set **Local Offset**: (3.0, 0.0, 0.0)
* Create a new Actor named **SOpAdjustSW** with **Actor Type: Site Operation (Local Offset)**
	* set **Local Offset**: (0.0, -3.0, 0.0)

 Each of these will offset the attached turret models to the specified coordinates.

### Model Actors
* Create a new Actor named **NE Turret** with **Actor Type: Model and Based On: ModelAddition**
	* set **Model**: Hub Turret
	* set **Scale**: 0.8
	* set **Host +**: Subject > Turret Hub
	* set **Host Site Operations +**: SOpAttachOrigin and SOpAdjustNE
	* open **Events +** and create the following events:
		* Unit Birth - Turret Hub
			* Create
		* Unit Death - Turret Hub
			* Model Swap (Name: Turret Death)
		* Actor Creation
			* Animation Play (Name: Attach; Animation Properties: Stand; Flags: Play Forever)
		* Model Swapped
			* Animation Play (Name: Death; Animation Properties: Death)
		* Animation Done
			* Animation Name Death (Term)
			* Destroy
* Duplicate 3 times and change **NE** to **NW**, **SE** and **SW**

These actors will create the turret models and upon dying swap in a Death Model rather than snuffing the model from existence the moment the Host dies.

* Create a new Actor named Turret Beam with Actor Type: Beam (Simple) and Based On: Beam Simple Animation Style One Shot
* set Model: Turret Beam
* open Events + and create the following events:
* Actor Creation
* Animation Play (Name: Beam; Animation Properties: Stand; Time Variant: 0.5; Time Type: Duration)
* Animation Done
* Destroy

This actor is part of pair. We're going to create its Attack Actors next.

### Site Actors
* Create a new Actor named NE Site with Actor Type: Site
* set Host +: Subject > NE Turret
* set Host Site Operations +: SOpAttachWeapon
* open Events + and create the following events:
* Unit Birth - Turret Hub
* Create
* Unit Death - Turret Hub
* Destroy
* Duplicate 3 times and change NE to NW, SE and SW

These will allow you to shoot the beams from the turrets by creating reference points.

## Attack Actors
* Create a new Actor named NE Beam Attack with Actor Type: Action and Based On: GenericAttack
* set Beam: Turret Beam (Actor)
* set Launch Assets +: Sound > Colossus_AttachLaunch
* set Impact Map +: 1st Row > (Art > Colossus Attack Beam Impact | Sound > Colossus_AttackImpact)
* set Launch Site: NE Site (Actor)
* open Events + and create the following events:
* Effect - NE Turret (Damage) - Start
* Create
* Duplicate 3 times and change NE to NW, SE and SW

The Launch Assets + controls the sounds/models created at the Launch Site and the Impact Map + controls the sounds/models created at the impact point.

## Turret Actors
* Create a new Actor named NE Turret Actor with Actor Type: Turret
* set Turret Body +: NE Turret (Actor)
* set Yaw Query +: Direct > Turret Z
* open Events + and create the following events:
* Turret Enable - NE Turret
* Create
* Duplicate 3 times and change NE to NW, SE and SW

These actors allow the turrets to function by tying the Turret objects to their Turret actors.

You should now have a fully functioning multi-turret structure :D
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjI0NTM3NjgsLTEzODU5Mzg2NTddfQ
==
-->