---
title: Data - Panic and Berserk Unit States (Beginner Difficulty)
date: 2010-08-24 00:00:00 Z
categories:
- Data
tags:
- data
author: ProzaicMuse
layout: post
---
To the best of my knowledge, there isn't any kind of "go into a frenzy" or "run around screaming" setting or object that you can readily apply to units. Instead, we are going to be making a system of  Effect - Issue Order's that will tell the affected units what to do.

----------

  

## Panic Unit State

### Effects Tab

-   Create a new Effect named  **Panic (Stop)**  with  **Effect Type: Issue Order**
    -   set  **Ability:**  Stop
    -   set  **Player +:**  Target
    -   set  **Target +:**  Source Unit
    -   set  **Unit +:**  Source

This will tell the unit to stop whatever it is doing. This will signify the "end" of the panic state.

-   Create a new Effect named  **Panic (Run)**  with  **Effect Type: Issue Order**
    -   set  **Ability:**  Move
    -   set  **Player +:**  Source
    -   set  **Target +:**  Target Point
    -   set  **Unit +:**  Source

This is the "panic" part of the ability. This tells the unit to run to each of the offset points we will create.

-   Create a new Effect named  **Panic (Offsets)**  with  **Effect Type: Create Persistent**
    -   set  **Flags:**  Random Offset
    -   set  **Period Count:**  1
    -   set  **Period Durations:**  0
    -   set  **Period Effects:**  Panic (Run)
    -   set  **Periodic Offsets:**  ([0,10], [10, 10], [10, 0], [10, -10], [0, -10], [-10, -10], [-10, 0], [-10, 10])
    -   set  **Location +:**  Source Unit/Point
    -   set  **Location Offset - End +:**  Target Point
    -   set  **Location Offset - Start +:**  Source Unit

This will randomly select an offset (direction) to tell the unit to run to based on its current location.

-   Create a new Effect named  **Panic (Panic)**  with  **Effect Type: Apply Behavior**
    -   set  **Unit +:**  Target

This is a placeholder in the effect chain until you have created the actual behavior.

-   Create a new Effect named  **Panic (Search)**  with  **Effect Type: Search Area**
    -   set  **Areas:**  (Arc: 360; Effect:  Panic (Panic)); Maximum Count: -1; Radius: 5)
    -   set  **Search Filters:**  Exclude [Dead/Hidden/Invulnerable/Missile/Self/Stasis]
    -   set  **Impact Location +:**  Target Unit/Point
    -   set  **Launch Location +:**  Source Unit

This effect is optional, but we will use this to apply the affect to units in a given blast area.

### Behaviors Tab

-   Create a new Behavior named  **Panic**  with  **Behavior Type: Buff**
    -   set  **Alignment:**  Negative
    -   set  **Categories:**  Temporary
    -   open  **Modification +:**
        -   Behavior >  **State Flags:**  Enable Uncommandable
        -   Movement >  **Movement Speed Multiplier:**  1.5
    -   set  **Effect - Final:**  Panic (Stop)
    -   set  **Effect - Initial:**  Panic (Offsets)
    -   set  **Effect - Periodic:**  Panic (Offsets)
    -   set  **Duration:**  10
    -   set  **Period:**  0.5
    -   link the  **Effect - Apply Behavior:**  Panic (Panic)

This behavior increases the speed of the panicked unit, prevents player control and determines how long the unit flees and how frequently it changes directions.

### Buttons Tab

-   Create a new Button named  **Panic**
    -   set  **Hotkey:**  D
    -   set  **Icon:**  btn-ability-zerg-infestation.dds

### Abilities Tab

-   Create a new Ability named  **Panic**  with  **Ability Type: Effect - Target**
    -   open  **Commands +**  and set the Default Button for Execute to  Panic
    -   set  **Target Filters:**  Exclude [Dead/Hidden/Invulnerable/Missile/Self/Stasis], Require [Visible] and Uncheck [Ally]
    -   open  **Cost +**  and set Cooldown > Time Use: 1
    -   set  **Effect:**  Panic (Search)
    -   set  **Range:**  6

### Models Tab

-   Create a new Model named  **Panic (Blast)**
    -   set  **Model:**  PredatorImpactShockwave.m3

-   Create a new Model named  **Panic (Icon)**
    -   set  **Model:**  PingBoss.m3

### Actors Tab

-   Create a new Actor named  **Panic (Blast)**  with  **Actor Type: Model Animation Style One Shot**
    -   set  **Model:**  Panic (Blast)
    -   set  **Scale:**  3.0
    -   open  **Host +:**  Subject > clear value
    -   open  **Events**  and create the following events:
        -   Actor Creation
            -   Animation Play (Name: Impact; Animation Properties: Death)
        -   Animation Done
            -   Destroy
        -   Effect - Panic (Search) - Start
            -   Create

This is the visual blast that represents the initial search area. It's important that you remove the  Host +  subject or the blast might end up attaching itself to a unit near the target point. While not game breaking, it can misalign the model so that it doesn't accurately represent where the search is actually created.

-   Create a new Actor named  **Panic (Icon)**  with  **Actor Type: Model Animation Style Continuous**
    -   set  **Model:**  Panic (Icon)
    -   set  **Scale:**  3.0
    -   set  **Host +:**  Subject > _Unit (Alias)
    -   set  **Host Site Operations +:**  Alias > SOpAttachOverhead
    -   open  **Events**  and create the following events:
        -   Actor Creation
            -   Animation Play (Name: Attach; Animation Properties: Stand; Flags: Play Forever)
        -   Behavior - Panic - Create
            -   Create
        -   Behavior - Panic - Destroy
            -   Destroy

This will create the "panicked" model and attach it to each unit affected by the given behavior. The current setup will allow you to change the behavior's duration without needed to modify the actor. It will play for as long as the behavior is active.

----------

  

## Berserk Unit State

### Effects Tab**

-   Create a new Effect named  **Berserk (Stop)**  with  **Effect Type: Issue Order**
    -   set  **Ability:**  Stop
    -   set  **Player +:**  Target
    -   set  **Target +:**  Source Unit
    -   set  **Unit +:**  Source

This will tell the unit to stop whatever it is doing. This will signify the "end" of the berserk state.

-   Create a new Effect named  **Berserk (Attack)**  with  **Effect Type: Issue Order**
    -   set  **Ability:**  Attack
    -   set  **Player +:**  Target
    -   set  **Target +:**  Target Unit
    -   set  **Unit +:**  Source

This is the "berserk" part of the ability. This tells the unit the target found by the search area..

-   Create a new Effect named  **Berserk (Search)**  with  **Effect Type: Search Area**
    -   set  **Areas:**  (Arc: 360; Effect:  Berserk (Attack)); Maximum Count: -1; Radius: 8 )
    -   set  **Search Filters:**  Exclude [Dead/Hidden/Invulnerable/Missile/Self/Stasis]
    -   set  **Impact Location +:**  Source Unit
    -   set  **Launch Location +:**  Source Unit
    -   set  **Target Sorts +:**  (Request Percentage: 1; Sorts: TSDistanceToTarget)

This effect is how the unit will find targets to attack, but we will use this to apply the affect to units in a given blast area.

-   Create a new Effect named  **Berserk (Berserk)**  with  **Effect Type: Apply Behavior**
    -   set  **Unit +:**  Target

This is a placeholder in the effect chain until you have created the actual behavior.

### Behaviors Tab

-   Create a new Behavior named  **Berserk**  with  **Behavior Type: Buff**
    -   set  **Alignment:**  Negative
    -   set  **Categories:**  Temporary
    -   open  **Modification +:**
        -   Combat >  **Damage Dealt Fraction:**  (Melee: 2; Ranged: 1.5; Spell: 1; Splash: 1.5)
        -   Movement >  **Movement Speed Multiplier:**  1.5
        -   Unit >  **Vital Regeneration Bonus:**  (Life: -3)
    -   set  **Player +:**  Neutral Player
    -   set  **Effect - Final:**  Berserk (Stop)
    -   set  **Effect - Periodic:**  Berserk (Search)
    -   set  **Duration:**  10
    -   set  **Period:**  1
    -   link the  **Effect - Apply Behavior:**  Berserk (Berserk)

This behavior increases the speed and damage of the berserking unit, shifts control to the neutral AI (an alternate method of preventing player control) and determines how long/frequently the unit rages and selects targets. It also causes negative life gain, degenerating 3 hit points per second to represent the self-destruction nature of rage.

### Buttons Tab

-   Create a new Button named  **Berserk**
    -   set  **Hotkey:**  F
    -   set  **Icon:**  btn-ability-zerg-corruption-multi.dds

### Abilities Tab

-   Create a new Ability named  **Berserk**  with  **Ability Type: Effect - Target**
    -   open  **Commands +**  and set the Default Button for Execute to  Berserk
    -   set  **Target Filters:**  Exclude [Dead/Hidden/Invulnerable/Missile/Self/Stasis] and Require [Visible]
    -   open  **Cost +**  and set Cooldown > Time Use: 1
    -   set  **Effect:**  Berserk (Berserk)
    -   set  **Range:**  6

### Models Tab

-   Create a new Model named  **Berserk (Rage)**
    -   set  **Model:**  ZergResearchPickUp.m3

### Actors Tab

-   Create a new Actor named  **Berserk (Rage)**  with  **Actor Type: Model Animation Style Continuous**
    -   set  **Model:**  Berserk (Rage)
    -   set  **Host +:**  Subject > _Unit (Alias)
    -   set  **Host Site Operations +:**  SOpAttachOrigin
    -   open  **Events**  and create the following events:
        -   Actor Creation
            -   Animation Play (Name: Attach; Animation Properties: Stand; Flags: Play Forever)
        -   Behavior - Berserk - Create
            -   Create
        -   Behavior - Berserk - Destroy
            -   Destroy
        -   Actor Creation
            -   Set Tint Color (Color: 255, 128, 128)
        -   Actor Creation
            -   Set Tint Color (Color: [255, 128, 128, HDR: 0.5]; Label: Enrage) - [Target: "::Host"]
        -   Actor Creation
            -   Set Scale (Scale: 2; Blend: 2; Label: Grow) - [Target: "::Host"]
        -   Actor Destruction
            -   Clear Tint Color (Blend: 2; Label: Enrage) - [Target: "::Host"]
        -   Actor Destruction
            -   Clear Scale (Blend: 2; Label: Grow) - [Target: "::Host"]

There is a lot going on with this actor, but it's actually quite simple when broken down. The actor creates a model, increases the unit's size and tints both red. Then when the actor is destroyed after the behavior ends, it returns the unit back to normal. Perhaps the most important part of the events is the  Target  field on each event action. This is how you tell the actor to change its host rather than itself.

----------

  

## Caster Test Unit

We're going to use an Observer for our abilities, so you won't need to do anything other than add abilities. I duplicated the Observer and its actor for the text map while renaming it  Provocateur.

### Units Tab

-   Select the  **Provocateur**  (duplicated or otherwise)
    -   open  **Abilities +**  and add  Berserk  and  Panic
    -   open  **Command Card +**  and add both ability buttons
        -   (Button: [NAME]; Command Type: Ability Command; Ability: [NAME]; Ability Command: [NAME])

----------

  
Feel free to use the attached Test Map or contact me via forum post/IRC if you encounter problems. Keep in mind that I'm a busy person so I may not reply right away, but I'll do my best to answer all questions/concerns that I am aware of  :)
<!--stackedit_data:
eyJoaXN0b3J5IjpbODA5MzM1NDQwXX0=
-->