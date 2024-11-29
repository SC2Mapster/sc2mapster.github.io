First things first, I expect that if you're reading this, you're clueless when it comes to beams. Why? Because you saw beginner and came to this tutorial. That being said, my job is to help you no longer be clueless and show off your awesome beam weapons and abilities in your future maps  :D  This will also help to prepare you for my more advanced beam tutorial.

## The Basics

Beams are nothing more than models. They can't do anything on their own and unlike missiles they aren't a physical unit that travels from point A to B. In order to get a Beam to do anything you must rely on actors and effects. Thus every proper Beam is made up of the following parts:

-   **Models**
-   **Actors**  (Control everything from size to location to whether or not your beam will crash the game)
-   **Effects**  (This is how you shoot at units and do damage)

We will be spending all of our time in these 3 tabs. If you have to go to another tab for any reason other than to make a turret, weapon or unit, you're in the wrong place. This is going to be all about the simple mechanics behind how beams work.

----------

  

## Goals

No introductory learning tool is complete without laying out goals. So we're going to make 3 of them:

-   A Unit that fires a beam weapon
-   A Vehicle that fires a beam that shoots 2 additional beams in a burst
-   A Non-Combat Structure that fires a beam that bounces twice

Let's get started!

----------

  

## Testing My Map

Before you create the beams it's important that you see what it is they do in game. Look at the terrain before you Test Document (Ctrl + F9). In the middle are the two units that shoot beams and in the NE corner is the tower that shoots lightning. All the other zerg units are stock. Now test the document. It's going to say it's tied (I ignore triggers in example maps) so click "Return to game."

Start by attack-moving all the Lancers (Marines) into the SW corner. Pew pew pew! Lots of dead zerg by colossi beams.

Now attack-move all the Ionic Splitters (Hellions) into the SE corner. Notice that it shoots a green void ray beam (instead of blue) that forks. This is done using  **Actor Events.** If you pay close attention, you'll also notice that the forks will almost always hit the Ultralisks. This is done using  **Target Sorts**

Now take both groups and attack-move into the NW corner. Again, notice that Ionic Splits will hit their target and then fork to the Ultralisks until they are almost dead.

Lastly, take everything and attack-move into the NE corner. Uh oh, massive lightning tower! If you've played any TD maps prior to this, you might notice that the lightning beams aren't coming from the very top. Instead they're coming from the rod slightly below that. It looks more realistic. This is done using  **Site Operations.** Also, the beams are brighter/thicker than they normally would be (you might not notice this if you haven't seen them as they normally are). That's more  **Actor Events.**

Everything you see was done with  Models,  Actors  and  Events.

----------

  

## The Lancer

Make sure your  Data Editor (F7)  is open and ready to go. You can either open the  Previewer (Ctrl + Shift + V)  to select the beams you want or you can use the sames ones I did. If you choose your own beams it will be up to you to swap them in where I place my beams and match their animations when we go into  Actor Events. I will give reminders along the way to help those who want to do this.

### Effects Tab

Open with  **Data Type**  menu if needed

We've only got one effect to make: damage. Click on the effects tab. The effects will show up on the upper left box, it's links (objects that are tied to it) will show up in the bottom left box and the entire right hand area is the data editing field. Make sure all 5 buttons (ignore the 6th on the other side of the divider) left of the search bar are pressed. This will allow you to follow my "short hand."

-   Create a new effect (upper left box) named  **Lancer (Damage)** with  **Effect Type: Damage**
    -   set (right side)  **AI - AI Notify Flags**  to Hurt Enemy
    -   set  **Combat - Amount**  to 20
    -   set  **Effect - Flags**  to Notificatin
    -   set  **Effect - Kind**  to Ranged
    -   set  **Effect - Response Flags**  to Acquire, Flee

AI Notify Flags, Flags and Response Flags are VERY important to apply to every damage effect you make. If you don't, the AI won't know what to do when attacked by them which will prevent units you attack from returning fire if your units aren't within their proximity auto-acquire range. In my more advanced tutorials I won't include these as I expect experienced mappers to know this and apply it on their own as needed. Additionally it can help to NOT have units return fire if you need them to hold still long enough to see what happens visually. Keep this in mind when testing abilities. The rest of this tutorial will have these included to help you get acquainted with these fields, however.

### Models Tab

Open with  **Data Type**  menu if needed

-   Create a new model named  **Lancer Beam**  with  **Model Type: Generic**
    -   set  **Model**  to ColossusBeam.m3

### Actors Tab

Open with  **Data Type**  menu if needed

-   Create a new actor named  **Lancer Beam**  with  **Actor Type: Beam (Simple)** and  **Based On: BeamSimpleAnimationStyleOneShot (Unknown)**
    -   set  **Model**  to Lancer Beam
    -   set  **Art - Scale**  to (0.5, 0.5, 0.5)
    -   open  **Event - Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play: (Name: Beam1; Animation Properties: Death; Flags: [empty]; Blend In: -1.0; Blend Out: -1.0; Time Variant 1.0; Time Type: Duration)
        -   Animation Done
            -   AnimName: Beam1 (Custom)
            -   Destroy

If you are using a different model, make sure you set  **Animation Properties**  to whichever animation actually shows up such as  **Birth**  or  **Stand.** Some models don't have more than one animation. For example most impact models just have a  **Death**  animation.

-   Create a new actor named  **Lancer Beam Attack**  with  **Actor Type: Action**  and  **Based On: GenericAttack**
    -   set  **Art - Beam**  to Lancer Beam
    -   open  **Combat - Launch Assets +**  and change sound to  **Colossus_AttackLaunch**
    -   open  **Event - Events +**  and create the following event:
        -   Effect - Lancer (Damage) - Start
            -   Create
    -   open  **Target - Impact Map +**  and select the 1st row and set sound to  **Colossus_AttackImpact**

Now your beam will show up every attack and make the proper sounds.

### Units Tab

Open with  **Data Type**  menu if needed

Duplicate  **Marine**  and check the following boxes:

![Marine](https://web.archive.org/web/20110724033316im_/http://static.sc2mapster.com/content/attachments/3/747/Marine.jpg "Marine")

Start by renaming the Marine model  **Lancer**. Go on to rename the actors  **Lancer**  and  **Lancer_Death**  and the weapon  **Plasma Lance ("Lancer -" in the Editor Prefix field)**. Now delete any abilities, command card buttons or behaviors you don't want and decide on your structure stats (HP, armor etc). Finish by renaming the unit  **Lancer**.

-   set  **Effect - Effect**  to Lancer (Damage)
-   set  **Stats - Period**  to 1.5
-   set both  **Random Delay Maximum and Minimum**  to 0
-   set  **Stats - Range**  to 7
-   set  **UI - Damage Display Effect**  to Lancer (Damage)
-   set  **UI - Icon**  to btn-upgrade-protoss-extended-thermallance.dds
-   set  **Weapon - Target Filters**  to exclude[Dead/Hidden/Invulnerable/Missile/Resource(both)/Self/Stasis] and require [Visible]

Now you have a beam weapon  :D

----------

  

## The Ionic Splitter

### Effects Tab

-   Create a new effect named  **Splitter (Damage2)**  with  **Effect Type: Damage**
    -   set  **AI - AI Notify Flags**  to Hurt Enemy
    -   set  **Combat - Amount**  to 30
    -   set  **Effect - Flags**  to Notificatin
    -   set  **Effect - Kind**  to Ranged
    -   set  **Effect - Response Flags**  to Acquire, Flee

-   Create a new effect named  **Splitter (Search)** with  **Effect Type: Search Area**
    -   set  **Search - Areas +**  to (Arc: 360; Effect: Splitter (Damage2); Maximum Count:2 and Radius: 4)
    -   set  **Search - Exclude +**  to Target
    -   set  **Search - Search Filters**  to exclude[Dead/Hidden/Invulnerable/Missile/Resource(both)/Self/Stasis] and require [Visible] and uncheck ally/player
    -   set  **Target - Target Sorts +**  to TSLifeLargestFirst(Unknown)

-   Return to  **Splitter (Damage2)**
    -   set  **Target - Launch Location +**  to Splitter (Search) at Target Unit/Point

This will cause the damage to originate from the search allowing your beams to connect from this impact as opposed to your unit. This is VERY important if you want your beams to chain in any capacity.

-   Create a new effect named  **Splitter (Damage)**  with  **Effect Type: Damage**
    -   set  **AI - AI Notify Flags**  to Hurt Enemy
    -   set  **Combat - Amount**  to 15
    -   set  **Effect - Flags**  to Notificatin
    -   set  **Effect - Kind**  to Ranged
    -   set  **Effect - Response Flags**  to Acquire, Flee

-   Create a new effect named  **Splitter (Set)**  with  **Effect Type: Set**
    -   set  **Effect - Effects**  to include Splitter (Search) and Splitter (Damage)
    -   set  **Effect - Maximum Count**  to -1

This should allow you to shoot a target and have two more beams shoot from that target to units close to it. If you find that not all of your effects are landing, there is a chance that  **Effect - Maximum Count**<</color>> on the  **Effect - Set**<</color>> is set to 1 instead of -1. This field sets the maximum number of effects the set can create at once. Thus -1 is infinity and 1 is only a single effect.

If you want more beams, set a higher  **Maximum Count**  on the  **Effect - Search Area.**  The Target Sort will also cause the forking beams to hit beefier targets first. You could even add bonus damage against armored/massive targets if you want the bounces to be extra effective against larger targets.

### Models Tab

-   Create a new model named  **Splitter Beam**  with  **Model Type: Generic**
    -   set  **Model**  to WarpRayMissile.m3

-   Create a new model named  **Splitter Beam 2**  with  **Model Type: Generic**
    -   set  **Model**  to SoulHunterBeam3.m3

### Actors Tab

-   Create a new actor named  **Splitter Beam**  with  **Actor Type: Beam (Simple)**  and  **Based On: BeamSimpleAnimationStyleOneShot (Unknown)**
    -   set  **Model**  to Splitter Beam
    -   set  **Art - Scale**  to (0.75, 0.75, 0.75)
    -   open  **Event - Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play: (Name: Beam1; Animation Properties: Attack, Variation 02; Flags: [empty]; Blend In: -1.0; Blend Out: -1.0; Time Variant 0.75; Time Type: Duration)
        -   Actor Creation
            -   Set Tint Color: (255 Red, 255 Green, 128 Blue)
        -   Animation Done
            -   AnimName: Beam1 (Custom)
            -   Destroy

This will make your void beams a similar shade of green as their forking beams.

-   Create a new actor named  **Splitter Beam Attack Launch**  with  **Actor Type: Action**  and  **Based One: GenericAttack**
    -   set  **Art - Beam**  to Splitter Beam
    -   open  **Combat - Launch Assets +**  and change sound to  **VoidRay_WeaponStart**
    -   open  **Event - Events +**  and create the following event:
        -   Effect - Splitter (Damage) - Start
            -   Create

Notice that I didn't put an impact sound. This is because we're going to attack it to the forking beams instead. This is because you don't want the impact sound to play if the forking beams aren't actually hitting anything. If you want a separate noise for the void beam itself, you can, however, add that. I left it out to avoid sound clutter.

-   Create a new actor named  **Splitter Beam 2**  with  **Actor Type: Beam (Simple)**  and  **Based On: BeamSimpleAnimationStyleOneShot (Unknown)**
    -   set  **Model**  to Splitter Beam 2
    -   set  **Art - Scale**  to (0.5, 0.5, 0.5)
    -   open  **Event - Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play: (Name: Beam2; Animation Properties: Birth; Flags: [empty]; Blend In: -1.0; Blend Out: -1.0; Time Variant 0.8; Time Type: Duration)
        -   Animation Done
            -   AnimName: Beam2 (Custom)
            -   Destroy

-   Create a new actor named  **Splitter Beam 2 Attack**  with  **Actor Type: Action**  and  **Based One: GenericAttack**
    -   set  **Art - Beam**  to Splitter Beam 2
    -   open  **Event - Events +**  and create the following event:
        -   Effect - Splitter (Damage2) - Start
            -   Create
    -   open  **Target - Impact Map +**  and select the 1st row and set sound to  **Stalker_AttackImpact**

### Units Tab

Duplicate  **Hellion**  and check the following boxes:

![Hellion](https://web.archive.org/web/20110724033316im_/http://static.sc2mapster.com/content/attachments/3/748/Hellion.jpg "Hellion")

Start by renaming the Hellion model  **Ionic Splitter.**  Go on to rename the actor  **Ionic Spliter,**  the turret  **Ionic Splitter**  and the weapon  **Ion Cannon ("Ionic Splitter -" in the Editor Prefix field)**. Now delete any abilities, command card buttons or behaviors you don't want and decide on your structure stats (HP, armor etc). Finish by renaming the unit  **Ionic Splitter**.

-   set  **Effect - Effect**  to Splitter (Set)
-   set  **Stats - Period**  to 2.0
-   set both**Random Delay Maximum and Minimum**  to 0
-   set  **Stats - Range**  to 8
-   set  **UI - Damage Display Effect**  to Splitter (Damage)
-   set  **UI - Icon**  to btn-techupgrade-terran-particlecannon.dds
-   set  **Weapon - Target Filters**  to exclude[Dead/Hidden/Invulnerable/Missile/Resource(both)/Self/Stasis] and require [Visible]

### Actors Tab

Because we have a turret, we need to enable it before it will be able to fire properly.

-   Create a new actor named  **Ionic Splitter Turret**  with  **Actor Type: Turret**
    -   open  **Event - Events +**  and create the following event:
        -   Turret Enable - Ionic Splitter
            -   Create

Now you have a forking beam weapon  :D

----------

  

## The Lightning Tower

### Effects Tab

-   Create a new effect named  **Beam Bounce 3 (Damage)**  with  **Effect Type: Damage**
    -   set  **AI - AI Notify Flags**  to Hurt Enemy
    -   set  **Combat - Amount**  to 30
    -   set  **Effect - Flags**  to Notificatin
    -   set  **Effect - Kind**  to Ranged
    -   set  **Effect - Response Flags**  to Acquire, Flee

-   Create a new effect named  **Beam Bounce 2 (Search)**  with  **Effect Type: Search Area**
    -   set  ****Search - Areas +****  to (Arc: 360; Effect: Beam Bounce 3 (Damage); Maximum Count:1 and Radius: 4)
    -   set  **Search - Exclude +**  to Target
    -   set  **Search - Search Filters**  to exclude[Dead/Hidden/Invulnerable/Missile/Resource(both)/Self/Stasis] and require [Visible] and uncheck ally/player
    -   set  **Target - Target Sorts +**  to TSLifeLargestFirst(Unknown)

-   Return to  **Beam Bounce 3 (Damage)**
    -   set  **Target - Launch Location +**  to Beam Bounce 2 (Search) at Target Unit/Point

-   Create a new effect named  **Beam Bounce 2 (Damage)**  with  **Effect Type: Damage**
    -   set  **AI - AI Notify Flags**  to Hurt Enemy
    -   set  **Combat - Amount**  to 45
    -   set  **Effect - Flags**  to Notificatin
    -   set  **Effect - Kind**  to Ranged
    -   set  **Effect - Response Flags**  to Acquire, Flee

-   Create a new effect named  **Beam Bounce 2 (Set)**  with  **Effect Type: Set**
    -   set  **Effect - Effects**  to include Beam Bounce 2 (Search) and Beam Bounce 2 (Damage)
    -   set  **Effect - Maximum Count**  to -1

-   Create a new effect named  **Beam Bounce 1 (Search)**  with  *Effect Type: Search Area**
    -   set  **Search - Areas +**  to (Arc: 360; Effect: Bounce Beam 2 (Set); Maximum Count:1 and Radius: 4)
    -   set  **Search - Exclude +**  to Target
    -   set  **Search - Search Filters**  to exclude[Dead/Hidden/Invulnerable/Missile/Resource(both)/Self/Stasis] and require [Visible] and uncheck ally/player
    -   set  **Target - Target Sorts +**  to TSLifeLargestFirst(Unknown)

-   Return to  **Beam Bounce 2 (Damage)**
    -   set  **Target - Launch Location +**  to Beam Bounce 1 (Search) at Target Unit/Point

-   Create a new effect named  **Beam Bounce 1 (Damage)**  with  **Effect Type: Damage**
    -   set  **AI - AI Notify Flags**  to Hurt Enemy
    -   set  **Combat - Amount*** to 60
    -   set  **Effect - Flags**  to Notificatin
    -   set  **Effect - Kind**  to Ranged
    -   set  **Effect - Response Flags**  to Acquire, Flee

-   Create a new effect named  **Beam Bounce 1 (Set)**  with  **Effect Type: Set**
    -   set  **Effect - Effects**  to include Beam Bounce 1 (Search) and Beam Bounce 1 (Damage)
    -   set  **Effect - Maximum Count**  to -1

It might not make complete sense working backwards, but this is how the series works:

**  
Weapon Fires > Set 1 [Search 1 + Damage 1] > Search 1 Impact: Set 2 [Search 2 + Damage 2 (Launches from Search 1)] > Search Impact 2: Damage 3 (Launches from Search 2)  
**

Following this pattern you can make the chain as long as you want  :)

### Models Tab

-   Create a new model named  **Bounce Beam**  with  **Model Type: Generic**
    -   set  ****Model****  to ArchonBeamSuper.m3

### Actors Tab

-   Create a new actor named  **SOpLowerBy1p25**  with  **Actor Type: Site Operation (Local Offset)**
    -   set  **Actor - Local Offset**  to (0.0, 0.0, -1.25)

This actor is what is going to allow us to adjust where the beam chain shoots from on our structure.

-   Create a new actor named  **Bounce Beam 1**  with  **Actor Type: Beam (Simple)**  and  **Based On: BeamSimpleAnimationStyleOneShot (Unknown)**
    -   set  **Model**  to Bounce Beam
    -   open  **Event - Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play: (Name: Beam1; Animation Properties: Birth; Flags: [empty]; Blend In: -1.0; Blend Out: -1.0; Time Variant 2.0; Time Type: Duration)
        -   Actor Creation
            -   Set Tint Color: (255 Red, 255 Green, 255 Blue); HDR Multiplier: 3
        -   Animation Done
            -   AnimName: Beam1 (Custom)
            -   Destroy
    -   set  set  **Hosting - Host Launch Site Ops +**  to SOpLowerBy1p25

-   Create a new actor named  **Bounce Beam 1 Attack Launch**  with  **Actor Type: Action**  and  **Based One: GenericAttack**
    -   set  **Art - Beam**  to Bounce Beam 1
    -   open  **Combat - Launch Assets +**  and change sound to  **Archon_AttackLaunch**
    -   open  **Event - Events +**  and create the following event:
        -   Effect - Beam Bounce 1 (Damage) - Start
            -   Create
    -   open  **Target - Impact Map +**  and select the 1st row and set sound to  **Stalker_AttackImpact**

-   Create a new actor named  **Bounce Beam 2**  with  **Actor Type: Beam (Simple)**  and  **Based On: BeamSimpleAnimationStyleOneShot (Unknown)**
    -   set  **Model**  to Bounce Beam
    -   set  **Art - Scale**  to (0.75, 0.75, 0.75)
    -   open  **Event - Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play: (Name: Beam2; Animation Properties: Birth; Flags: [empty]; Blend In: -1.0; Blend Out: -1.0; Time Variant 1.95; Time Type: Duration)
        -   Actor Creation
            -   Set Tint Color: (255 Red, 255 Green, 255 Blue); HDR Multiplier: 3
        -   Animation Done
            -   AnimName: Beam2 (Custom)
            -   Destroy

-   Create a new actor named  **Bounce Beam 2 Attack**  with  **Actor Type: Action**  and  **Based One: GenericAttack**
    -   set  **Art - Beam**  to Bounce Beam 2
    -   open  **Event - Events +**  and create the following event:
        -   Effect - Beam Bounce 2 (Damage) - Start
            -   Create

-   Create a new actor named  **Bounce Beam 3**  with  **Actor Type: Beam (Simple)**  and  **Based On: BeamSimpleAnimationStyleOneShot (Unknown)**
    -   set  **Model**  to Bounce Beam
    -   set  **Art - Scale**  to (0.5, 0.5, 0.5)
    -   open  **Event - Events +**  and create the following events:
        -   Actor Creation
            -   Animation Play: (Name: Beam3; Animation Properties: Birth; Flags: [empty]; Blend In: -1.0; Blend Out: -1.0; Time Variant 1.6; Time Type: Duration)
        -   Actor Creation
            -   Set Tint Color: (255 Red, 255 Green, 255 Blue); HDR Multiplier: 3
        -   Animation Done
            -   AnimName: Beam3 (Custom)
            -   Destroy

-   Create a new actor named  **Bounce Beam 3 Attack**  with  **Actor Type: Action**  and  **Based One: GenericAttack**
    -   set  **Art - Beam**  to Bounce Beam 3
    -   open  **Event - Events +**  and create the following event:
        -   Effect - Beam Bounce 3 (Damage) - Start
            -   Create

### Units Tab

Duplicate  **Sensor Tower**  and check the following boxes:

![Sensor Tower](https://web.archive.org/web/20110724033316im_/http://static.sc2mapster.com/content/attachments/3/749/Sensor-Tower.jpg "Sensor Tower")

Start by renaming the Sensor Tower model  **Lightning Tower.**  Go on to rename the actor  **Lightning Tower.**  This structure doesn't have a weapon so you'll have to add one. Hop over to the Weapons Tab and make a new weapon named  **Energy Coil**  using the default settings. Add "Lightning Tower -" in the  **Editor - Editor Prefix**  field. Now return to the unit to delete any abilities, command card buttons or behaviors you don't want and decide on your structure stats (HP, armor etc). Finish by renaming the unit  **Lightning Tower**  and adding a new weapon to  **Combat - Weapons +**  using the  **Ionic Splitter**  turret and your newly created weapon.

-   set  **Effect - Effect**  to Beam Bounce 1 (Set)
-   set  **Stats - Period**  to 3.0
-   set both**Random Delay Maximum and Minimum**  to 0
-   set  **Stats - Range**  to 10
-   set  **UI - Damage Display Effect**  to Beam Bounce 1 (Damage)
-   set  **UI - Icon**  to btn-ability-terran-protoss-psistorm.dds
-   set  **Weapon - Target Filters**  to exclude[Dead/Hidden/Invulnerable/Missile/Resource(both)/Self/Stasis] and require [Visible]

Now you have a beam chain weapon  :D

----------

  
If you have any questions or concerns, feel free to post them here. Especially if you see typos or possible errors. I'll do my best to keep to correct such issues  ;)

If you'd like to learn a more advanced method of beam chaining, see my  [Dynamic Beam Chains](https://web.archive.org/web/20110724033316/http://forums.sc2mapster.com/resources/tutorials/3888-data-dynamic-beam-chains-intermediate-difficulty/)  tutorial.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MDkwNjY2NjddfQ==
-->