BANKS
=====

Banks are the Editor’s method for storing information and using it
between projects. Below you can see a sample bank file.

.. figure:: ./051_Banks/image1.png
   :alt: Image

   Image

Custom Game Bank File

This bank stores a player’s personal statistics from a type of custom
game. Note the structure here. A bank is separated hierarchically first
by sections and then into key-value pairings. As values are stored in
the bank, they are written to the bank file in a target section, and by
their associated key, but in no particular order beyond that.

BANK ACTIONS
------------

The controls for bank handling can be found during action creation under
the label ‘Bank.’ This is shown below, followed by a table that breaks
down these controls.

.. figure:: ./051_Banks/image2.png
   :alt: Image

   Image

Bank Actions

+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Action                | Effect                                                                                                                                                                                                                       |
+=======================+==============================================================================================================================================================================================================================+
| Preload Bank          | Preloads and synchronizes a Bank for a specific Player.                                                                                                                                                                      |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Create Bank Section   | Creates a bank Section, which can then accept key-value pairs.                                                                                                                                                               |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Save Bank             | Saves a Bank, making sure that all changes to the file are maintained after the game.                                                                                                                                        |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Store Data            | Stores a Value as a Key to a certain Section of a Bank. There are several types available for storage: Boolean, Integer, Real, Point, String, Text, and Unit.                                                                |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reload Bank           | Reloads a Bank, reverting any changes that might have occurred between saves.                                                                                                                                                |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Open Bank             | Opens a Bank for use and alteration.                                                                                                                                                                                         |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Restore Unit          | Creates a unit that was previously stored through a Store Unit action. The unit is restored from a Key within a Section from a Bank. This results in the unit being created at a Point, for a Player, and facing an Angle.   |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wait For Bank         | This is a Wait control statement that pauses until the condition of a specific Bank being reloaded is True.                                                                                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Set Bank Option       | Sets the Signature option of a Bank to Enable or Disable. The signature provides an encryption option for banks, so that they cannot be altered by players.                                                                  |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Remove Bank Key       | Removes a Key from the Section of a Bank and its associate value.                                                                                                                                                            |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Remove Bank Section   | Removes a Section from a Bank and all of the key-value pairs it contains.                                                                                                                                                    |
+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

FINDING LOCAL BANK STORAGE
--------------------------

You can find the local bank storage at the Windows location described
below.

-  Libraries

   -  Documents

      -  StarCraft II

         -  StarCraftPlayer.ID@#

            -  Banks

               -  ID Code

                  -  Bank Files

This procedure is shown in the following image sequence.

.. figure:: ./051_Banks/image3.png
   :alt: Image

   Image

Accessing Local Bank Storage
