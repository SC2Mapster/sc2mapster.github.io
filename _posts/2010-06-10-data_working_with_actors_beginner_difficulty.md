---
title: Data - Working with Actors (Beginner Difficulty)
date: 2010-06-10 00:00:00 Z
categories:
- Data
tags:
- data
- actors
author: ProzaicMuse
layout: post
---
First and foremost, this will not begin as a full index of all the actors and every event combination in the editor. A tutorial on that would take weeks or even months to put together and would be unable to properly teach you anything other than how to make your eyes bleed. As amusing as that might be to witness, I'm certain I would /wrist myself long before I completed such a tutorial. Instead, I'll be covering the most common actors and their fields/events that you will use while tossing in a few less used actors that should probably be more widespread. Treat this as a catalog of actors every competent mapper should be familiar with. Also, as I continue to make more tutorials I may remove details from certain actors and replace them with a link to a tutorial that focuses on that specific actor and objects related to it. This will help reduce clutter as you help me expand the tutorial and hopefully turn this into a stepping stone to other tutorials you might need.

----------

## Actor Basics

Actors are essentially the Data Editor's version of triggers. The simplest way to understand them would be to take a look at anything in the game that has a graphical representation. Whatever it is, there is a 95% (yes, I mathematically deduced this through rigorous calculations and hard facts. My findings are immutable!) chance that an actor was involved. This is not their only function, however, as they also play sounds, control abilities, deform terrain and setup turrets amongst other things. Thus it is safe to say that if you haven't yet created an actor in your map, you haven't been properly introduced to the Data Editor.

Typically the most important field for an actor is  **Events +**. This field controls what creates/destroys it and when. Events also trigger certain animations, change the actors color, shape, opacity and other such physical attributes. They can even be used to communicate with other actors. These events can be broken down into the following:

**Conditions:**  Determine what triggers the event, the trigger's name and when this happens

-   Message Type  is the Trigger.
-   Source Name  is the Trigger's Name.
-   Sub Name  is when during the Trigger the Condition is met.

**Terms:**  List requirements either for when it can be triggers OR how it must react once triggered.  
**Actions:**  Determine what the actor will do once Conditions and Terms have been met.

----------

  

## Index:

-   Action
-   Beam (Simple)
-   Missile
-   Model
-   Range
-   Site
-   Site Operations
-   Sound
-   Terrain Deformer
-   Text
-   Turret
-   Unit

----------

  

### Action

Any time you have an effect that deals damage, launches a projectile or creates a beam model you will need what I call the  Attack Actor  This actor controls where a weapon fires from, where it impacts and all of the sounds and graphics associated with these two locations. If a beam is flying off in random directions or missiles are skidding along the ground, this actor is the first place you should check.

##### Important Fields

* **Attack Effect Token**:  Damage effect of a chainless attack - (Effect - Damage).

**OR**

-   **Launch Effect Token:**  Firing effect in an attack effect chain - (Effect - Launch Missile).
-   **Impact Effect Token:**  Impact effect in an attack effect chain - (Effect - Damage).

Tokens auto-fill portions of the actor they are tied to. Most of these changes will occur in  **Events +**  and should be used if you're making something simple with only a few steps. I typically won't use tokens if I'm making very complex abilities or weapons that have more than one damage phase.

-   **Beam:**  The associated  Beam Actor.
-   **Container Model:**  Visual effect for units firing from inside a transport - (Medivac, Bunker etc).
-   **Impact Model:**  Visual model for your Impact Effect - (Ex: Explosion).
-   **Impact Model Reaction:**  Target units visual reaction to your Impact Effect.
-   **Launch Model:**  Visual model for your Launch Effect - (Ex: Muzzle Flash).
-   **Missile:**  The associated  Missile Actor.

The majority of fields after the  Art  section will be referring to these models. Thus it's important to remember that:

**Launch**  refers to the effect that creates this actor.  
**Container**  refers to when this actor is created by a unit inside a transport (Ex: Medivac or Bunker).  
**Impact**  refers to the effect that hits the target unit - (Ex: Explosion or Blood Spatter).  
**Damage**  refers to units hits by splash around the target - (Ex: Blood Spatter).

-   **Attachment - [Anything]:**  These fields are responsible for deciding where the action launches from, what part of the target it impacts and where splash damage impacts nearby targets. With exception to the Container Site, these fields do not use Sites or Site Operations. You need these in order for your action to work, but all other fields that affect Launch, Impact, Damage or Containers will override these fields.

The default values are  Methods  with a specific point as the fallback (Center by default). Attachment Methods (AM) search for points to attach to for you and allow for rotating launch points. Thus if you used  AMFilterWeapon00, the actor would look for any attachment point with  Weapon00  in its name on whatever model you are launching from. If it can't find one the fallback is used.

Additionally you can use multiple AMs at a time that narrow down the search parameters. For example, if you used  **AMClosestToTarget**  and  **Filter Weapon**  the actor would launch from whatever attachment point was closest to the target AND had "Weapon" in its name.

Alternatively, you can use  Direct  which allows you to pick a specific launch point instead of multiple. This isn't as dynamic as AMs, but that's the point. This is typically ideal if you are firing weapons that need to launch from a specific attachment point every time.

-   **[Anything] Site:**  These fields allow you use the point designated by a Site Actor in place of the Launch, Container, Impact or Damage point. This is important for firing from models attached to a unit.
-   **[Anything] Site Operations:**  These fields allow you to use Site Operations to adjust the Launch, Container, Impact or Damage point instead of replacing it with a Site. Keep in mind that you CAN use a Site Actor as well in which case the Site Operations will adjust from the Site Actor's point.
-   **[Anything] Assets:**  These fields allow you to set the animation, model and sound of the actions Launch or Container Launch effects.
-   **[Anything] Map:**  These fields are identical to the  ****Assets****  field, but are for Impact/Damage effects and have an index allowing you to create specific animations/models/sounds for certain target types.  None, the first row, is applied to all targets unless an index below it like  Flesh  or  Metal  has different animations/models/sounds.
-   **[Anything] Sound:**  Self-explanatory, but it's important to note that this field does not allow you to simply pick a sound file. You need to have a Sound Actor with the sound that you want before you can link to it with this field.

##### Important Events

**Normal Attack Actors:**

-   **Condition:** Effect.[Effect - Damage].Start
-   **Action:**  Create

This would tell the actor to create every time the Damage Effect "lands" on the target. Fairly straight forward.

**Beam Attack Actors:**

-   **Condition:**  Effect.[ Effect - Damage].Start
-   **Action:**  Create

Ironically Beam Attack Actors don't require much more than normal attacks in terms of effects as the important events will be on the Beam Actor.

**Missile Attack Actors:**

-   **Condition:**  Effect.[Effect - Launch Missile].Start
-   **Term:**  At Caster
-   **Action:**  Create

This event ties launch models and assets to the effect. It's important that the term is included otherwise the missile will shoot from the unit's feet and drag along the ground.

-   **Condition:**  Effect.[Effect - Damage].Start
-   **Term:**  At Caster
-   **Term:**  FromEffectTreeDescendant
-   **Action:**  ActionImpact

This event ties the impact models and assets to the effect. As before, both terms are important or the models won't display properly and the sounds will be unusually quiet.

**Channeling Attack Actors:**

-   **Condition:**  Effect.[NAME].Stop
-   **Action:**  Destroy

This event is added to any actor that is created by a channeled ability. This destroys the actor to prevent the models from sticking around even after the unit has ceased firing and moved on.

----------

  

### Beam (Simple)

-   (Reference:  [Beams (Beginner)](https://web.archive.org/web/20110912063649/http://forums.sc2mapster.com/resources/tutorials/3939-data-working-with-beams-beginner-difficulty/))

If you want to create a Beam in any capacity, this is the actor that does it. The only time you wouldn't use this actor is when you want your Beam to be a physical attachment to another model. In that case you would use a  Model Actor. In the case of Beam Actors, I have never found a reason to use (Standard) over (Simple) and, if you look through the editor, neither has Blizzard. That being said, if I ever DO find such a reason I'll update this tutorial. Until then, this is the actor for you.

##### Important Fields

-   **Model:**  The associated  Model.
-   **Scale:**  This allows you to change the model's size without affecting the model itself.
-   **Hosting - [Anything]:**  These fields control Site Operations. If you want to change where a beam appears in relation to the unit that creates it, especially in the case of Beams lacking an  Attack Actor, these fields will allow you to attach the model to the unit that creates it or offset it from the weapon that fires it.

##### Important Events

**Attack Beams:**

-   **Condition:**  Actor Creation
-   **Action:**  Animation Play - (Name: [NAME]; Animation Properties: [ANIMATION]; Flags: [CHECKBOXES]; Blend In: [TIME]; Blend Out: [TIME]; Time Variant: [INTEGER]; Time Type: [TYPE]
    -   **[NAME]**  - Customized name that allows you to target this event action specifically with other events
    -   **[ANIMATION]**  - Many models have multiple animations. This is where you pick what specific animation you want your model to play. If set incorrectly, this could also prevent your model from showing up at all if it doesn't have the chosen animation.
    -   **[CHECKBOXES]**  - The options themselves are self-explanatory, but the most common choices are  Non Looping  and  Play Forever. The first choice freezes the model after one complete play through while the latter causes it to repeat forever until destroyed
    -   **[TIME]**  - These control the length over which the animation blends in and out.
    -   **[INTEGER]**  - Depending on the type, this will either be left at -1, determine your scalar quantity or set the animation's total length.
    -   **[TYPE]**  -  Automatic  is the default choice and lets the game determine how long to run the animation.  Duration  and  Time Scale  do exactly what they are named. Set the length or scale the length.

This event probably looks strange at first given all the brackets, but it is actually very simple in nature. This tells the actor to play the model animation whenever this actor is created. Without this event, your model won't show up.

-   **Condition:**  Animation Done
-   **Action:**  Destroy

This even destroys the actor when the animation is done to prevent overlapping beams.

-   **Condition:**  Actor Creation
-   **Action:**  Set Tint Color (Color; Blend In Duration; Blend Type: [TYPE]; Label: [NAME])
    -   **[TYPE]**  - If you didn't set a blend time, set this to  One Shot.  This will cause it to change colors only once. The other two types are best used with a blend time.  Bounce  causes the beam to shift back and forth between the two colors while  Cycle  shifts to the tint color and then jumps back to the original color immediately before shifting again.
    -   **[NAME]**  - Like with animations, this is a customized name you can reference with other events.

This optional event is for changing the color of your beams. It's important to note that this is based upon color math. Thus if your beam is blue and you apply a yellow tint thinking it will turn yellow it will actually turn green.

**AoE Beams:**

-   **Condition:**  [Effect].[NAME].[Start]
-   **Action:**  Create

If your beam doesn't have an  Attack Actor  this event will also be needed to create itself.

----------

  

### Missile

For the purpose of sanity, we're going to ignore Tentacle Missiles as they are incredibly complicated to create despite the brevity of their attacks. Refer to my Customized Projectiles tutorial if you want to see how this is done in detail.

##### Important Fields

-   **Model:**  The associated  Model.
-   **Scale:**  This allows you to change the model's size without affecting the model itself.
-   **Hosting - [Anything]:**  These fields control Site Operations. The fields are particularly important for returning missiles as you must specify what part of the unit the missile returns to.

##### Important Events

-   **Condition:**  UnitBirth.[NAME]
-   **Action:**  Create

This event creates the actor whenever the  Unit Missile  is fired.

-   **Condition:**  Unit Birth
-   **Action:**  Animation Bracket Start - (Name: [NAME]; Opening: Birth; Content: Stand; Closing: - ; Flags [CHECKBOXES]; Time Variant: [INTEGER]; Time Type: [TYPE])
    -   **[NAME]**  - Customized name that allows you to target this event action specifically with other events
    -   **[CHECKBOXES]**  - I have never used one of these flags, so I can't give a good reason why you would need to.  Leave a comment below if you have and I'll include it
    -   **[INTEGER]**  - Depending on the type, this will either be left at -1, determine your scalar quantity or set the animation's total length.
    -   **[TYPE]**  -  Automatic  is the default choice and lets the game determine how long to run the animation.  Duration  and  Time Scale  do exactly what they are named. Set the length or scale the length.

This event tells the actor to play the model animation whenever the  Unit Missile  is created. Without this event, your model won't show up. Even though this is the default editor event for the actor, changing the condition from  Unit Birth  to  Actor Creation  will accomplish the same thing. Also, Animation Bracket differs from Animation Play in that it contains multiple animation phases for the model to pass through. In this case, it plays the  Birth  animation and then stays in the  Stand  animation until the actor is destroyed.

-   **Condition:**  UnitDeath.[NAME]
-   **Action:**  Destroy

This event destroys the actor whenever the  Unit Missile  is killed.

----------

  

### Model

This actor has a wide range of uses and is very simple to use. The  Based On  menu selection will need to be changed based upon what you want to use the actor for. The most common selections are  BuffContinuous  (for auras),  BuffOneShot  (for spell casting animations),  Model Addition  (for attachments) and  ModelAnimationStyleOneShot  (for impact animations). These won't change the fields available to you, but will pre-fill various fields to save you time when configuring your actor.

##### Important Fields

-   **Model:**  The associated  Model.
-   **Scale:**  This allows you to change the model's size without affecting the model itself.
-   **Hosting - [Anything]:**  These fields control Site Operations. If you want impact explosions to center on a target, these fields will allow you to do that. Additionally, if you are using the Model actor as attachments these fields are required to anchor the model to the position you want.
-   **Properties - [Anything]:**  These fields control what properties the model will receive from the units it attaches to or fires from. So if you wanted an attachment to NOT cloak when its host cloaks, these fields would allow that.

##### Important Events

**Visual Effects:**

-   **Condition:**  [Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Create

This event creates the model whenever an  Ability,  Behavior  or  Effect  with a given name begins a certain phase.

-   **Condition:**  Actor Creation
-   **Action:**  Animation Play - (Name: [NAME]; Animation Properties: [ANIMATION]; Flags: [CHECKBOXES]; Blend In: [TIME]; Blend Out: [TIME]; Time Variant: [INTEGER]; Time Type: [TYPE]
    -   **[NAME]**  - Customized name that allows you to target this event action specifically with other events
    -   **[ANIMATION]**  - Many models have multiple animations. This is where you pick what specific animation you want your model to play. If set incorrectly, this could also prevent your model from showing up at all if it doesn't have the chosen animation.
    -   **[CHECKBOXES]**  - The options themselves are self-explanatory, but the most common choices are  Non Looping  and  Play Forever. The first choice freezes the model after one complete play through while the latter causes it to repeat forever until destroyed
    -   **[TIME]**  - These control the length over which the animation blends in and out.
    -   **[INTEGER]**  - Depending on the type, this will either be left at -1, determine your scalar quantity or set the animation's total length.
    -   **[TYPE]**  -  Automatic  is the default choice and lets the game determine how long to run the animation.  Duration  and  Time Scale  do exactly what they are named. Set the length or scale the length.

This event tells the actor what animation to play and is probably the most important part of the actor. This is where you control what the animation will be and how long it will last for. If you want to match model animations to unit casting animations or to weapon attack rates this is where you would do just that.

-   **Condition:**  Animation Done
-   **Action:**  Destroy

This even destroys the actor when the animation is done to prevent overlapping visual effects.

**Attachment Models:**

-   **Condition:**  UnitBirth.[NAME]
-   **Action:**  Create

This event creates the actor whenever the given unit is created. If you set this unit as the host, the actor will then attach itself to the unit with the specified  Site Operations.

-   **Condition:**  Actor Creation
-   **Action:**  Animation Play - (Name: [NAME]; Animation Properties: [ANIMATION]; Flags: Play Forever)
    -   **[NAME]**  - Customized name that allows you to target this event action specifically with other events
    -   **[ANIMATION]**  - Many models have multiple animations. This is where you pick what specific animation you want your model to play. If set incorrectly, this could also prevent your model from showing up at all if it doesn't have the chosen animation.

This event is different from other  Animation Play  events in that you don't need to set a duration and or type. This is because you want to pick a given animation and play it forever until the hosting unit dies. Thus this event tells the actor to play the specified animation forever.

-   **Condition:**  UnitDeath.[NAME]
-   **Action:**  Destroy

This event destroys the attachment whenever the hosting unit dies.

----------

  

### Range

This actor is responsible for creating the range indicators for  Abilities,  Behaviors,  Weapons  and the  Sensor Tower  in particular.

##### Important Fields

-   **Ability:**  The associated  Ability.
-   **Arc:**  Normally 360, this can be used to create cone shaped range indicators.
-   **Fog Visibility:**  This determines whether or not the enemy can see your range indicator.
-   **Range:**  If you don't have a linked Ability/Behavior/Sight/Weapon with its own range, this is where you set the range radius.
-   **Range Flags:**  This determines whether or not the range indicator is shown on the minimap.
-   **Sight:**  The associated  Unit  sight radius.
-   **Behavior:**  The associated  Behavior.
-   **Weapon:**  The associated  Weapon.
-   **Hosting - [Anything]:**  These fields determine what part of the unit the range circle originates from. Thus if you want to offset the center point use these fields.

##### Important Events

**Ability Range:**

-   **Condition:**  Abil.[NAME].TargetOn
-   **Action:**  Create

This event creates the actor when the target cursor is active.

-   **Condition:**  Abil.[NAME].TargetOff
-   **Action:**  Destroy

This event destroys the actor when the target has been chosen.

**Sight Range:**

-   **Condition:**  UnitBirth.[NAME]
-   **Action:**  Create

This event creates the actor whenever the given unit is created. This is particularly useful for stealth games where you want the player to visually see the sight range of units they are trying to avoid.

-   **Condition:**  UnitDeath.[NAME]
-   **Action:**  Destroy

This event destroys the actor when the hosting unit dies.

**Behavior Range:**

-   **Condition:**  Behavior.[NAME].On
-   **Action:**  Create

This event creates the actor whenever the behavior is active.

-   **Condition:**  Behavior.[NAME].Off
-   **Action:**  Destroy

This event destroys the actor whenever the behavior is inactive.

**Weapon Range:**

-   **Condition:**  UnitBirth.[NAME]
-   **Action:**  Create

-   **Condition:**  UnitDeath.[NAME]
-   **Action:**  Destroy

These events are identical to those needed for the  Sight  field, but you are instead indicating the units weapon range. Thus these events are best used with stationary objects like turrets where sight radius won't matter.

----------

  

### Site

These actors are points of reference for other actors. If you want something to originate from a custom anchor point that isn't on a model, this actor allows you to do that. The following tutorials cover this in detail:

-   [Attachments (Beginner)](https://web.archive.org/web/20110912063649/http://forums.sc2mapster.com/resources/tutorials/8926-data-working-with-attachments-beginner-difficulty/)
-   [The Uberlisk (Advanced)](https://web.archive.org/web/20110912063649/http://forums.sc2mapster.com/resources/tutorials/4284-data-working-with-hosting-and-site-operations-the-uberlisk/)

----------

  

### Site Operations

These actors determine where and how objects attach to each other. The following tutorials cover these in detail:

-   [Attachments (Beginner)](https://web.archive.org/web/20110912063649/http://forums.sc2mapster.com/resources/tutorials/8926-data-working-with-attachments-beginner-difficulty/)
-   [The Uberlisk (Advanced)](https://web.archive.org/web/20110912063649/http://forums.sc2mapster.com/resources/tutorials/4284-data-working-with-hosting-and-site-operations-the-uberlisk/)

----------

  

### Sound

This actor is so complex. . . that it actually defines the meaning of life. . . or not. It creates sounds. Fairly straightforward. If you want your visual effects to make noise, you need this actor.

##### Important Fields

-   **Host:**  The actor creating the sound.
-   **Host Site Operations:**  Where on the actor the sound originates. This generally only matters when you forget to put anything here after selecting a host OR when you are creating a sound for a very large object.
-   **Host Supporter:**  The actor creating the continuous sound.
-   **Inherit Type:**  The determines whether the sound is continuous or not.
-   **Sound:**  The associated  Sound.

##### Important Events

**One Shot Sound:**

-   **Condition:**  [Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Create

This event creates the model whenever an  Ability,  Behavior  or  Effect  with a given name begins a certain phase.

-   **Condition:**  Actor Creation
-   **Action:**  Timer Set (Name: [NAME]; Duration: [TIME])

This optional event allows you to set a specific duration for your sound.

-   **Condition:**  Timer Expired
-   **Action:**  Destroy

This optional event allows you to destroy the sound when your custom duration has expired. The two  Timer  events are especially important when you want to associate a very long sound with a short animation. Without these, long sounds can continue to play even after their trigger has finished and moved on. Sound pollution is very bad.

-   **Condition:**  Sound Done
-   **Action:**  Destroy

This event destroys your event when the sound completes its default length.

**Continuous Sound:**

-   **Condition:**  [Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Create

This event creates the sound whenever an  Ability,  Behavior  or  Effect  with a given name begins a certain phase.

-   **Condition:**  [Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Destroy

This event destroys the sound whenever an  Ability,  Behavior  or  Effect  with a given name begins a certain phase.

-   **Condition:**  Supporter Destruction
-   **Action:**  Destroy

This event destroys the sound when the object channeling the sound is destroyed. This event prevents sounds from looping forever after its creator dies (Ex: Sentry Beam).

-   **Condition:**  Sound Done
-   **Action:**  Destroy

This event destroys your event when the sound completes its default length. If you aren't using a looping sound, this is important to prevent sound stacking.

----------

  

### Terrain Deformer

This actor allows you to physically change the terrain during a game. While it does little more than change terrain elevation, you can combine this with other actors or triggers to make new ramps, walls and other physical barriers.

##### Important Fields

-   **Blend Time:**  The duration over which the elevation changes.
-   **Footprint:**  The shape of terrain that changes.
-   **Height Delta:**  The up or down change in elevation.
-   **Influence Range:**  The radius of elevation change.
-   **Terrain Deformation Flags**  Determines whether or not foliage is destroyed and if the elevation change is permanent.
-   **Hosting - [Anything]:**  These fields are only important if you want the elevation change to occur at the units location or an offset relative to that point.

##### Important Events

**Permanent Deformation:**

-   **Condition:**  [Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Create

This event starts the elevation change whenever an  Ability,  Behavior  or  Effect  with a given name begins a certain phase.

**Temporary Deformation:**

-   **Condition:**  [Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Destroy

This event stops the elevation change whenever an  Ability,  Behavior  or  Effect  with a given name begins a certain phase. You only need this if the elevation change is going to be channeled over time OR you want the elevation to return to normal.

-   **Condition:**  Actor Creation
-   **Action:**  Timer Set (Name: [NAME]; Duration: [TIME])

This event sets a specific duration for the elevation change to last.

-   **Condition:**  Timer Expired
-   **Action:**  Destroy

This event reverts the elevation change after the specified duration has expired.

----------

  

### Text

This actor creates floating text that you can see in the game. This is useful for making damage counters, visual updates at specific locations (like quests) or even scrolling text for visual queues of DoT ticks or resource collection cycles. The possibilities are endless.

##### Important Fields

-   **Options:**  Determines the origin for  Height Offset.
-   **Hosting - [Anything]:**  These fields determine where the text shows up.
-   **UI - [Anything]:**  These fields determine the visual appearance of the text. Everything from alignment to color.

##### Important Events

**Static Text:**

-   **Condition:**  [UnitBirth/Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Create

This event creates the text whenever a  Unit,  Ability,  Behavior  or  Effect  with a given name begins a certain phase. You only need this if the elevation change is going to be channeled over time OR you want the elevation to return to normal.

-   **Condition:**  [UnitBirth/Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Destroy

This event destroys the text whenever a  Unit,  Ability,  Behavior  or  Effect  with a given name begins a certain phase. You only need this if the elevation change is going to be channeled over time OR you want the elevation to return to normal.

**Fading Text:**

-   **Condition:**  [UnitBirth/Ability/Behavior/Effect].[NAME].[WHEN]
-   **Action:**  Create

This event creates the text whenever a  Unit,  Ability,  Behavior  or  Effect  with a given name begins a certain phase. You only need this if the elevation change is going to be channeled over time OR you want the elevation to return to normal.

-   **Condition:**  Actor Creation
-   **Action:**  Timer Set (Name: [NAME]; Duration: [TIME])

This event sets a specific duration for the text to fade out over.

-   **Condition:**  Actor Creation
-   **Action:**  Set Opacity (Opacity: 0.0; Blend in Duration: [TIME])

This event reduces the text's opacity to 0 over the specified duration.

-   **Condition:**  Timer Expired
-   **Action:**  Destroy

This event destroys the text after the specified duration has expired.

**Scrolling Text:**

-   **Condition:**  Actor Creation
-   **Action:**  Timer Set (Name: [NAME]; Duration: [TIME])

This event sets a specific duration before the text changes height.

-   **Condition:**  Timer Expired
-   **Action:**  Set Height

This event adjusts the text's height after the specified duration.

-   **Condition:**  Timer Expired
-   **Action:**  Timer Set (Name: [NAME]; Duration: [TIME])

This event sets another duration before the next height change.

-   **Condition:**  Timer Expired
-   **Action:**  Destroy

This event destroys the text after the last  Timer  has expired. By adding these to the events for fading text, you can set a time for the whole fading process with the opacity change and then multiple stages for height changes that add up to the opacity change. Thus over time the text fades and scrolls whatever direction you want.

----------

  

### Turret

(Reference:  [Turrets (Beginner)](https://web.archive.org/web/20110912063649/http://forums.sc2mapster.com/resources/tutorials/9000-data-working-with-turrets-beginner-difficulty/))

If you want a structure to fire a weapon or a unit's weapon to fire independently of its facing, you need a  Turret Actor  that will create the actual turret from the  Turrets Tab.  Otherwise your weapon won't work properly and the weapon that should be rotating will be stuck in place.

##### Important Fields

-   **Pitch Query:**  Determines the point of rotation for up and down movement.
-   **Turret Body:**  The associated  Actor  that will rotate.
-   **Yaw Query:**  Determines the point of rotation for left and right movement.

##### Important Events

-   **Condition:**  TurretEnable.[NAME]
-   **Action:**  Create

This event allows the weapon's turret to function properly.

-   **Condition:**  TurretEnable.[NAME]
-   **Action:**  Destroy

This event destroys the turret when the  Turret Body  morphs into another unit (Ex: Spine Crawler uprooting).

-   **Condition:**  TurretDisable.[NAME]
-   **Action:**  Destroy

This event destroys the actor when the turret has been destroyed or disabled.

----------

  

### Unit

This actor is, in my opinion, the most complex and involved actor to make from scratch. Thus it is typically better to duplicate a unit and simply rename the actor before making the needed adjustments and adding your own events. I'm aware it's not complete and only covers some of the MANY things you might need. I'll do my best to update this as people have questions about it.

##### Important Fields

-   **[Token] Unit Name:**  This is the field at the top that is set apart. This is VITAL to connecting your actor to its unit. Without it, your unit won't have an actor.
-   **Actor - Aliases:**  These function like labels or categories. You can use an alias as a  Host  for any  Site Operation. If you used  _Unit, a common alias, the SOp would attach itself to any actor with that alias provided that its events create it at or very near to said actor. You can even create your own so that if you need to divide your custom units into groups, you could do so with this.
-   **Art - Model [Anything]:**  The fields determine the various models used in certain situations ranging from when you place the unit in the editor to the portrait down by the command card.
-   **Art - Random Scale Range:**  If you like variety, you can set minimum and maximum values for your unit's size. This is a very easy way to add diversity to your unit. If you combine this with model variations you can easily create an single unit army that appears to be many different units.
-   **Art - Scale:**  This determines the unit's size.
-   **Combat - Death [Anything]:**  These fields allow you to customize what happens to the unit when it dies. This includes the animations and sounds.
-   **Hosting - [Anything]:**  These fields allow you to rotate, offset, tilt etc. I'm currently exploring the possibility of multi-unit bosses using these fields.
-   **Sound - Ability Sounds +:**  This field is an alternate way to attach sounds to abilities. I'd only advise using this with sounds that you don't have complex events for. One limitation for this method is that you have to take sounds you have already added to the  Group Sounds  and  Sounds  fields.
-   **Sound - Group Sounds +:**  This field controls what sounds your unit plays while it is in a group. These can be much different from the sounds it would have played if it were the only unit selected.
-   **Sound - Sounds +:**  This field controls what sounds your unit plays regardless of situation but only if another field doesn't specify a different sound to play.
-   **UI - Bar [Anything]:**  These fields allow you to adjust or move the status bars that appear over the unit's head.
-   **UI - Cooldown Display:**  This field lets you add the cooldown of an ability to your status bar.
-   **UI - [Anything] Icon [Anything]:**  These fields control The various icons that show up in groups, hero frames, the minimap and unit stats. You can even add variations to go with your diversified model scale range and variations.
-   **UI - Status Bar Flags:**  This field allows you to turn off some or all of the status bars.
-   **UI - Status Colors +:**This field allows you to change the color of any status bar.

##### Important Events

-   **Condition:**  UnitBirth.[NAME]
-   **Action:**  Create

This event creates the actor whenever the unit is brought into existence.

-   **Condition:**  UnitConstruction.[NAME]
-   **Action:**  Create

This event creates the actor whenever it is built from a structure or other "training" type object.

-   **Condition:**  UnitRevive.[NAME]
-   **Action:**  Create

This event creates the actor whenever it is revived as in the case of Heroes.

-   **Condition:**  UnitDeath.[NAME]
-   **Action:**  Destroy

This even destroys the actor when the unit dies.

-   **Condition:**  UnitBirth.*.Normal
-   **Action:**  Animation Bracket Start - (Name: BSD; Opening: Birth; Content: Stand; Closing: Death ; Flags -; Time Variant: -1; Time Type: Automatic)

This event tells the actor to play the model animation whenever the  Unit  is created. Without this event, your model won't show up. Even though this is the default editor event for the actor, changing the condition from  Unit Birth  to  Actor Creation  will accomplish the same thing. Also, Animation Bracket differs from Animation Play in that it contains multiple animation phases for the model to pass through. In this case, it plays the  Birth  animation and then stays in the  Stand  animation until the unit dies. At that point it plays the  Death  animation.

-   **Condition:**  WeaponStart.[NAME].AttackStart
-   **Action:**  Animation Play - (Name: [NAME]; Animation Properties: [ANIMATION]; Time Variant: [INTEGER]; Time Type: [TYPE]
    -   **[NAME]**  - Customized name that allows you to target this event action specifically with other events
    -   **[ANIMATION]**  - Many models have multiple animations. This is where you pick what specific animation you want your model to play. If set incorrectly, this could also prevent your model from showing up at all if it doesn't have the chosen animation.
    -   **[INTEGER]**  - Depending on the type, this will either be left at -1, determine your scalar quantity or set the animation's total length.
    -   **[TYPE]**  -  Automatic  is the default choice and lets the game determine how long to run the animation.  Duration  and  Time Scale  do exactly what they are named. Set the length or scale the length.

This event allows you to tie specific animations to your weapon attacks.

-   **Condition:**  WeaponStop.[NAME].AttackStop
-   **Action:**  Animation Clear [NAME]

This event will clear the animation associated with the given weapon whenever it finishes stops firing. This prevents animation freezing.

-   **Condition:**  UnitMovementUpdate.*.Walk
-   **Action:**  Animation Clear [NAME]

This event will clear a given animation whenever the unit moves. This prevents animation freezing.

----------

  

## Building the Catalog

If you have an actor that isn't on this list that you need help with, just ask. I'll slowly add actors as people begin to experiment with them. The idea being that you should look at these actors first before moving on to the more advanced ones. The same goes for events. If you want to know how to implement certain events with an actor in this catalog, let me know.

Likewise if you think a tutorial other than one of my own should be linked to one of the actors I cover, PM me a link and I'll take a look at the tutorial. If I think it can teach more about the actor that the listed details can I'll swap in the link.

As always please inform me of typos or errors in this post. It's quite lengthy and I probably didn't catch all of my mistakes. If you're just plain confused, that's ok too. Ask and I or someone else is likely to come along and set yeh straight  ;)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUwNjQwMzM4MiwtNzA4MzUyNzExXX0=
-->