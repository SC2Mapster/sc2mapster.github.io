---
title: Data - Working with Attachments (Beginner Difficulty)
date: 2010-08-24 00:00:00 Z
categories:
- Data
tags:
- data
author: ProzaicMuse
layout: post
---
I got a lot of requests for a more basic and intuitive guide for attachments after making the Uberlisk Tutorial. So this will serve to bridge the gap between those needing to understand what attachments are and those who have a solid understanding of them. It's important to note that this doesn't cover all aspects of attachments given that there are some fairly complex methods of attaching objects together. These are merely the methods that I think are likely to become commonplace once more widely understood.

----------

  

## Attachment Basics

The vast majority of attachments are based upon  Site Operation Actors. Even when using  Site Actors  to create custom launch points you are likely still using a  Site Operation  to specify its exact location. This means understanding related fields is central to using them:

-   **Host:**  The actor the attachment is anchored to
-   **Host Launch:**  The unit/location a beam/projectile is fired from.
-   **Host Impact:**  The unit/location a beam/projectile is fired to.
-   **Host Supporter:**  The actor that  Signals  are sent to/from. This is ONLY needed used with  Signals,  ::Supporter  values or  SupporterDestruction  events. We won't be covering this, but it's important to understand that this field has a wide range of uses. Look at stock units made by Blizzard to see the various ways they use it.
-   **[ANY] Site Operations:**  This is where you specify offsets, rotations and other modifications by linking Site Operation Actors.

## Bunker Turret

We're going to make a bunker with a fully functioning turret. The turret will fire a beam and have its own attachment. In my Test Map I've removed all abilities unrelated to this turret, but you can easily keep the basic functions of the bunker as well as the added turret weapon.

### Effects Tab

-   Create a new Effect named  **Attachment Turret (Damage)**  with  **Effect Type: Damage**
    -   set  **AI Notify Flags:**  Hurt Enemy
    -   set  **Amount:**  10
    -   set  **Armor Reduction:**  1
    -   set  **Death:**  Fire
    -   set  **Flags:**  Notification
    -   set  **Kind:**  Ranged
    -   set  **Response Flags:**  [Acquire/Flee]

The 3 Flag fields are what cause the unit you attack to respond to you. Either they will attack you or run away based upon what responses the unit has been given.

### Weapons Tab

-   Create a new Weapon named  **Attachment Turret**
    -   set  **Effect:**  Attachment Turret (Damage)
    -   set  **Damage Point:**  0.5
    -   set  **Period:**  1.5
    -   set  **Range:**  6
    -   set  **Damage Display Effect:**  Attachment Turret (Damage)
    -   set  **Icon:**  btn-techupgrade-terran-particlecannon.dds
    -   set  **Target Filters:**  Exclude [Dead/Hidden/Invulnerable/Missile/Self/Stasis] and Require [Visible]

This is the Turrets weapon that will go on the unit.

### Turrets Tab

-   Create a new Turret named  **Attachment Turret**
    -   set  **Idle:**  Spin
    -   set  **Yaw Arc:**  360
    -   set  **Yaw Idle Rate:**  45
    -   set  **Yaw Rate:**  720
    -   set  **Yaw Start:**  0

You can set these to whatever you'd prefer, but  Idle  controls the turrets action when not in combat,  Yaw Arc  controls its range of motion,  Yaw Idle Rate  is how quickly the turret rotates out of combat,  Yaw Rate  is how quickly the turret rotates in combat and  Yaw Start  determines the angle the turret begins facing.

### Models Tab

-   Create a new Model named  **Attachment Shield**
    -   set  **Model:**  MarineShieldUpgrade.m3

-   Create a new Model named  **Attachment Turret**
    -   set  **Model:**  FlameTurret.m3

-   Create a new Model named  **Beam Example**
    -   set  **Model:**  DiamondbackBeam.m3

### Units Tab

Duplicate the Bunker structure and its corresponding Actor. Everything else will be stock or made from scratch.

-   Name it  **Attachment Bunker**
    -   open  **Abilities +**  and remove all but [Attack/Stop]
    -   open  **Command Card+**  and add [Attack/Stop] buttons
    -   remove everything in  **Behaviors +**
    -   open  **Weapons +**  and add  Attachment Turret  (Weapon and Turret)

-   Name the building's Actor  **Attachment Bunker**

### Actors Tab

##### Site Operation Actors

-   Create a new Actor named  **SOpAttachDamage03**  with  **Actor Type: Site Operation (Attachment)**
    -   set  **Attachment Query +:**  Direct > Damage [Index 3]

-   Create a new Actor named  **SOpAttachTurretZ**  with  **Actor Type: Site Operation (Attachment)**
    -   set  **Attachment Query +:**  Direct > Turret Z

Attachment Query +  is where you use Attachment Methods (AMs) or Direct values to specify how attachments link together.

AMs are filters in that  AMFilterWeapon  wouldlook for any attachment point with the name Weapon to use. It usually takes the lowest index (0, 1 etc) first and before looking for other points. This can be convenient for use with a wide range of models. Direct allows you to pick a specific point and index. If you didn't want  Weapon00/01  you could use Direct to attach to  Weapon07  instead.

-   Create a new Actor named  **SOpAdjustTurret**  with  **Actor Type: Site Operation (Local Offset)**
    -   set  **Local Offset:**  (0.0, -0.02, -0.1)

-   Create a new Actor named  **SOpAdjustShield**  with  **Actor Type: Site Operation (Local Offset)**
    -   set  **Local Offset:**  (-0.06, -0.035, 0.17)

These  Site Operations  will offset the attachments in any direction while preserving its facing and rotational axis. Using the objects original point as the origin:

+X is right of the object, -X is left of the object  
+Y is towards/into the object, -Y is away from/out of the object  
+Z is above the object, -Z is below the object

One thing to note is that while it preserves its rotational axis, some anchor (attachment) points will actually tilt this axis to align it with the plane it's attached to. In other words, if you attach it to a surface that's at a 45 degree angle to ground, the attached model will also be at a 45 degree angle. Thus it's important to pick the right anchor point to move from before applying offsets.

-   Create a new Actor named  **SOpTiltShield**  with  **Actor Type: Site Operation (Explicit Rotation)**
    -   set  **Forward:**  (0.2, -1.0, 0.1)
    -   set  **Is Local:**  Enabled
    -   set  **Up:**  (-1.0, 0.0, 0.0)

This  Site Operation  tilts and rotates the shield model. It's important that local is enabled so that the vectors rotate with the attachment. If it is not, the rotation is static and faces the map direction created by the vectors. Also, you must have a value for BOTH vectors even if using the default forward/facing (0.0, -1.0, 0.0) or up/axis (0.0, 0.0, -1.0). If either field is left with (0.0, 0.0, 0.0) the attachment will spin sporadically as the attachment  Host  moves.

The directions from offsets are the same, but instead of moving the object you are going to create new vectors.  Forward  is the facing vector and  Up  is the rotational axis vector. Some examples:

**Face North**  
Forward - (X: 0.0,Y:  **1.0**, Z: 0.0)  
Up - (X: 0.0,Y: 0.0, Z:  **1.0**)

**Face Up**  
Forward - (X: 0.0, Y: 0.0, Z:  **1.0**)  
Up - (X: 0.0, Y: 0.0, Z:  **1.0**)

**Face South West**  
Forward - (X:  **-1.0**, Y:  **-1.0**, Z: 0.0)  
Up - (X: 0.0,Y: 0.0, Z:  **1.0**)

**Tilt West**  
Forward - (X: 0.0, Y:  **-1.0**, Z: 0.0)  
Up - (X:  **-1.0**, Y: 0.0, Z: 0.0)

**Tilt North East**  
Forward - (X: 0.0, Y:  **-1.0**, Z: 0.0)  
Up - (X:  **1.0**, Y:  **1.0**, Z: 0.0)

**Flip Upside Down**  
Forward - (X: 0.0, Y:  **-1.0**, Z: 0.0)  
Up - (X: 0.0, Y: 0.0, Z:  **-1.0**)

##### Model Actors

-   Create a new Actor named  **Attachment Turret**  with  **Actor Type: Model**  and  **Based On: ModelAddition**
    -   set  **Model:**  Attachment Turret
    -   set  **Scale:**  0.75
    -   set  **Host +:**  Subject >  Attachment Bunker
    -   set  **Host Site Operations+:**  SOpAttachTurretZ  and  SOpAdjustTurret
    -   open  **Events +**  and create the following events:
        -   Unit Birth - Attachment Bunker
            -   Create
        -   Unit Death - Attachment Bunker
            -   Destroy
        -   Actor Creation
            -   Animation Play (Name: Attach; Animation Properties: Stand; Flags: Play Forever)
        -   Weapon Start - Attachment Turret - Attack Start
            -   Animation Play (Name: Attack; Animation Properties: Attack)
        -   Weapon Stop - Attachment Turret - Attack Stop
            -   Animation Clear (Name: Attack)

This will create the turret model, attach it to the bunker with the specified offset and play its attack animation whenever the bunker's weapon fires. Its creation and destruction both tied to the  Attachment Bunker.

-   Create a new Actor named  **Attachment Shield**  with  **Actor Type: Model**  and  **Based On: ModelAddition**
    -   set  **Model:**  Attachment Shield
    -   set  **Host +:**  Subject >  Attachment Turret
    -   set  **Host Site Operations+:**  SOpAttachDamage03,  SOpAdjustShield  and  SOpTiltShield
    -   open  **Events +**  and create the following events:
        -   Unit Birth - Attachment Bunker
            -   Create
        -   Unit Death - Attachment Bunker
            -   Destroy
        -   Actor Creation
            -   Animation Play (Name: Attach; Animation Properties: Stand; Flags: Play Forever)

This will create the shield model and attach it to the turret with the specified offset and rotation. Its creation and destruction both tied to the  Attachment Bunker.

-   Create a new Actor named  **Beam Example**  with  **Actor Type: Beam (Simple)**  and  **Based On: Beam Simple Animation Style One Shot**
    -   set  **Model:**  Beam Example
    -   open  **Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play (Name: Beam; Animation Properties: Stand; Time Variant: 0.5; Time Type: Duration)
        -   Animation Done
            -   Destroy

This actor is part of pair. We're going to create its  Attack Actor  next.

##### Other Actors

-   Create a new Actor named  **Beam Example Site**  with  **Actor Type: Site**
    -   set  **Host +:**  Subject >  Attachment Turret
    -   set  **Host Site Operations +:**  SOpAttachWeapon
    -   open  **Events +**  and create the following events:
        -   Unit Birth - Attachment Bunker
            -   Create
        -   Unit Death - Attachment Bunker
            -   Destroy

This actor will allow you to shoot the beam from the turret by creating a point of reference. This can be any attachment point or even a random point in space. All that matters is that this actor is created at the same time the unit it will be associated with.

-   Create a new Actor named  **Beam Example Attack**  with  **Actor Type: Action**  and  **Based On: GenericAttack**
    -   set  **Attack Effect Token:**  Attachment Turret (Damage)
    -   set  **Beam:**  Beam Example  (Actor)
    -   set  **Launch Assets +:**  Sound > Diamondback_AttackLaunch
    -   set  **Impact Map +:**  1st Row > (Art > Immortal Attack Impact | Sound > Diamondback_AttackImpact)
    -   set  **Launch Site:**  Beam Example Site  (Actor)

If you use the token, you don't need to mess with the events. While I didn't do so in the Test Map, I'll typically change the token AND clear out the extra events that I don't need. This is just for my own personal organization and isn't required at all. That asside, The  Launch Assets +  controls the sounds/models created at the  Launch Site  and the  Impact Map +  controls the sounds/models created at the impact point.

-   Create a new Actor named  **Turret Actor**  with  **Actor Type: Turret**
    -   set  **Turret Body +:**  Attachment Turret
    -   set  **Yaw Query +:**  Direct > Turret Z
    -   open  **Events +**  and create the following events:
        -   Turret Enable - Attachment Turret
            -   Create

This actor allows the turret to function by tying the Turret object to the Turret actor. The  Turret Body +  is the model that will rotate while the  Yaw Query +  is the axis.

----------

  

## Flipped Wraith

Fairly self-explanatory. We're going to flip a Wraith upside down. While not incredibly impressive on its own, this is to demonstrate how to change the angle of ships. I've seen a lot of posts asking how to change the Yaw, Pitch and Roll of flying ships and this portion of the tutorial aims to answer those questions.

### Actors Tab

-   Create a new Actor named  **SOpFlip**  with  **Actor Type: Site Operation (Explicit Rotation)**
    -   set  **Forward:**  (0.0, -1.0, 0.0)
    -   set  **Is Local:**  Enabled
    -   set  **Up:**  (0.0, 0.0, -1.0)

This actor does nothing more than reverse a unit's axis. As mentioned before you need to input values for both vectors (default or otherwise) and ensure local is enabled.

-   Find the Actor named  **Wraith**
    -   set  **Host Site Operations +:**  SOpBankerWraith  and  SOpFlip

Now the Wraith flies upside down  :)

(Note,  SOpBankerWraith  is a  Site Operation  made by Blizzard. It does not contribute to attaching models together or flipping the Wraith. It controls how much a unit banks (tilts/rolls)as it turns. You can see this when you make sharp turns while flying around.

----------

  
Feel free to use the attached Test Map or contact me via forum post/IRC if you encounter problems. Keep in mind that I'm a busy person so I may not reply right away, but I'll do my best to answer all questions/concerns that I am aware of  :)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0ODMyOTE1MzIsMTE1MzYwNzY2OCwyMD
A4MDAyMzgwXX0=
-->