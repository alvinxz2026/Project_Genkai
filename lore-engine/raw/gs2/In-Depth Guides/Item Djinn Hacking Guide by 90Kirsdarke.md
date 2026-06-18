---
source_id: 90kirsdarke-hack
author: 90Kirsdarke
url: https://gamefaqs.gamespot.com/gba/561356-golden-sun-the-lost-age/faqs/44956
type: data-table
covers: [items, equipment, djinn, ids]
quality: default
summary: item/djinn 的内存地址与取值码（hex）。非叙述提取源；价值在于可做 canonical id/对照校验我方数据完整性。
gs1_counterpart:
notes: 我认为这个对于我们的价值主要在于可以有个complete list可以去check against our data，甚至可以用来给我们的数据提供一个code/identifier之类的标记，你怎么看？
---

# Item Djinn Hacking Guide by 90Kirsdarke

## TABLE OF CONTENTS

A.0 Version History
A.1 About this Guide

1.0 Item Hacking
    1.01 Character Addresses
    1.02 Item Values
1.1 Djinn Hacking
    1.11 Djinn Hacking Addresses
    1.12 Djinn Values
    

A.3 Frequently Asked Questions
A.4 Legal Stuff
A.5 Contact Info
A.6 Credits
A.7 Coming Soon

---

END OF TABLE OF CONTENTS

---

-----------------------------------
Golden Sun 2 Item/Djinn Hack Guide
-----------------------------------

Written by 9°Kirsdarke


--------------------
A.0 Version History
--------------------
9/15/06 Version 1.0
Well here you go. How to hack Items/Djinn in Golden Sun 2.


---------------------
A.1 About this Guide
---------------------

Welcome to my second guide. :) Since you are reading this I can assume that we
both have a huge respect for CAMELOT's Golden Sun series. The first time I ever
played these games I fell in love with them, as many have and many will.

This guide was written only for Golden Sun 2. Although many of the items and
psyenergies are the same in Golden Sun, many are different and all of the
addresses are different. If after reading this you wish to hack your Golden Sun
game a certain someone wrote a guide just for that purpose.

Well now that I've said my piece, it's time to get hacking!


------------
A.2 Hacking
------------

So by now you may be asking yourself "I've never heard of save game hacking. It
must be difficult." Fear not! Hacking a save can be incredibly simple. All you
have to do is understand the basics.

On your game, there is the game itself saved, and some RAM that holds all
of your game saves. Save game hacking deals directly with the hacking of
those save files. Unlike a Gameshark which bypasses code, hacking your save
physically (or electronically) alters your data permanently.

So how does one go about hacking a save game file? Well in order to do
it you need a Hex Editor, preferably (almost madatory) Winhex. I personally
like using it because it saves you a lot of clicking and dragging. This program
is free software and are available at www.download.com. It's not that big. Just
search for it.

So how do you get your game onto your computer? Well there's two basic ways.
One is to buy a special flash reader and transfer your game save onto the
computer. The other is to obtain a ROM from the internet. Either way you get
the save, this should be the method used to hack it.

So fire up that editor and open up your Golden Sun 2 save file. You will be
greeted with what appears to be a huge matrix of numbers; a long string of
numbers at the top and a long list of numbers at the side.

First off, let me explain the numbers. Golden Sun 2 uses what's called a
hexadecimal system. Every computer in the world is built off a system of on
and off switches. They can either be on or off, which leads to a two number
binary system. As humans we count everything as a decimal system, which
uses  ten numbers. So these two numbers are very difficult to convert from
one to another.

But fear not. Enter the hexadecimal system. It uses sixteen digits, 0-9 and
A-F. Since sixteen is a power of 2, hex and binary numbers can be easily
swapped. That's the job of the hex editor.

Notice how the hex numbers are grouped into pairs? Each group of two is one
byte of data. It is important you realize this because all of the information 
is saved on one byte, even if it is only a single digit number.

Of course it would be immensely difficult to just spew all the data out into
one continuous line. Enter the address: also known as the offset. On your
left, you have a long column of hex numbers like this:

00000000
00000010
00000020
00000030

and continues on...
00003AD0
00003AE0
00003AF0
00003B00

And so on, all the way to the end of your data. If your left column doesn't
contain any letters, click on it until it does. All the addresses in this
guide are written in hex form, and it would be difficult (if not impossible)
to find them otherwise.

Now each row contains the all of the possible locations for you data in that
address. They are written like:

00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

Since hex is a base of sixteen, the next number after 0F (which is 15 in
decimal) is 10. (which is 16 in decimal)

Each of those addresses has a value stored there, which are all of the
numbers you see in front of you.

So reading a address is quite simple. You read it exactly like you do a grid
on a map.

         00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
0000A060                      **
0000A070
0000A080
0000A090

If the address you are looking for is A067, then you would go down to A060,
and over to A067, which is indicated by the stars.

So when you wish to change a value for something, all you do is travel to the 
correct address, and then the correct byte.

Now if all you had to do to hack was load up your game, change some numbers
and load up your game, then life would be great. Unfortuantely for you
Golden Sun 2 includes two ways to stop the game save hacker: Libraries and
Checksums.

The comprehension of Libraries is crucial to be able to hack. Golden Sun 2
contains a total of three different libraries where your data could be
located. Now you may ask "But aren't there only three save slots?" To
which I will reply "Why, yes, I guess you're right." While its true there
only three save files, the game includes two "backup" libraries. Whenever
you save on your game, the data is automatically saved into two of these
files. Why two? Just in case your power goes off while saving, or any other
sort of saving nightmare. (Trust me, it's happened to me during a hack before,
and it is not fun :( )

The reason Libraries are so important becomes obvious very quickly if you
ignore them. Your game is saved in one of these five files. Now when I say
one, thats exactly what I mean. If you edit the wrong library, nothing will
happen. You must find the right library if you ever wish to succesfully hack
your game save. Failure to do so will result in hours of wasted time and tons
of effort and frustration on your part.

Thankfully, Golden Sun 2 is very easily divided into its libraries.
The start of each one is signified by the word CAMELOT in the right coloumn,
and continues all the way to the next CAMELOT.

Now how can one be sure they are editing the correct library? Well the
easiest way is to only have one save game. So if you just obtained a rom
and are starting your hacking, it's much easier if you only start one
game. That way there is only one possible library. If for some reason
you must have your save game data, then look at the level of your
characters or if they're the same the stats. Comparing them this way
makes it much easier to make a correct guess.

Golden Sun also uses another security method called the Checksum. The
checksum is the sum of all the values of each byte of data in a block
of code. Basically whenever you load up your game, the fileadds up
all of the bytes in your save and checks it against the checksum.If
they are the same, then you data loads up no problem. But if they
are not equal, the game does not recognise it as valid and you will
meet an empty save slot.

That may sound horrible to you but actually it is a great help. In
Golden Sun 2, the Checksum is always located in the exact same spot for
each library. Just scroll through checking all of your libraries until
you find the one with a Checksum. If you have two save different save
files, however, you will probably have to manually search character stats
to find the correct one. But rest assured if a file does not have a
checksum it is not one that you should be hacking.

The Checksum will always be writen as two bytes of data. So when even if you
add it and you get a checksum of 03, you still use two bytes.

And for all you WinHex users, I have good news. First, left click on the
offset listand go to edit block. Then set the block to *010 to *FFF. The *
is for whichever library you are in at the time, whether its 0010 or 3010.
Then go up to tools and click on Compute Hash/Checksum or something like
that, set it to 16 Checksum and viola, you have your Checksum.

** When storing the Checksum, the game automatically uses the "reverse-byte"
method of storage. Basically, if you get a checksum of 03A6, you would break
it into two bytes 03 and A6, and reverse them. The Checksum would then be
written as A6 03. If for any reason you get a Checksum larger than 2 bytes,
then just take the last four numbers and reverse them to get your Checksum.

Well thats basically everything you need to know (and I know) about hacking!:)


---------------------
A.3 A Few More Notes
---------------------

1) When you wish to save your game on the computer, make sure you use the
start + save method of saving. Otherwise it is almost impossible to hack.

2) When you back up your game, do not use your hex editors backup feature.
It is best to copy your game and paste it in a new folder. Then if something
goes wrong, you can just delete your corrupted file and substitute the good
one. Just make sure to rename it to whatever the first file was named.

3) Many times when you are hacking the "Your write time has changed. Would you
like to reload" message will appear on your screen. If you click yes, the data
is reloaded and you have to find the correct library again. The only time it
is necessary is if you have done something in the game and saved it. Otherwise
it is just a waste of time to keep doing it.

4) If you want a save file to practice hacking with all of the characters,
Gamefaqs offers a variety of game saves for you to download. However these files
are not .sav files that Visual Boy Advanced gets you. If you want to use one of
these files simply open your ROM and then go file->import->sharkport snapshot.
The emulator then reverts it to a .sav file and you're free to practice hacking.


--------------
1.0 CheckSum
--------------

CheckSum          -> *008 - *009
Range of Checksum -> *010 - (*+2)FFF

This is a nice, easy CheckSum to calculate. Just go to edit (or right click +
edit) and scroll down to Define Block. Set the top number to *010 and the
bottom to (*+2)FFF to get the correct CheckSum. So for example a very common
library is the 3000 block with the Checksum at 3008+3009 and stretches from
3010 to 5FFF.

Just make sure to put the resulting CheckSum in the "reverse byte" method,
where you put the second byte first and the first byte second. So a CheckSum
of 4F78 would be written as 78 4F.

Just make sure when you calculate your CheckSum you use 16 bit CheckSum.
Anything else will not work at all.




------------------
1.01 Item Hacking
------------------

Item hacking is actually incredibly simple. It's just like hacking psyenergy.


      00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
3680                  Item -> 0A 02 <- Equiped/Quantity
3690
36A0
36B0

Item: Very simple. You merely change this value to whatever item you want.

Equpied/Quantity: Again a fairly simple concept. Certain values signify
whether an item is equpied/unequiped or how many you have.


00 = Unequipped    48 = 10         98 = 20         E8 = 30
02 = Equipped      50 = 11         A0 = 21
08 = 2             58 = 12         A8 = 22
10 = 3             60 = 13         B0 = 23
18 = 4             68 = 14         B8 = 24
20 = 5             70 = 15         C0 = 25
28 = 6             78 = 16         C8 = 26
30 = 7             80 = 17         D0 = 27
38 = 8             88 = 18         D8 = 28
40 = 9             90 = 19         E0 = 29

There is also another subset of items that instead of using

00 = unequiped
02 = equiped

they instead use

01 = unequiped
03 = equiped

That is because basically the game had more items that could fit in one
byte and so they had to throw in a 01 so you could access another set of
items.

Just so you know it's best to hack your items as "unequiped" so that way
you won't accidentally have a conflict of intrest.


------------------------
1.01 Character Addresses
------------------------

Felix: 3B38 - 3B55
Jenna: 3C84 - 3CA1
Sheba: 3DD0 - 3DED
Piers: 3F1C - 3F39
Issac: 3608 - 3625
Garet: 3754 - 3771
Ivan: 38A0 - 38BD
Mia: 39EC - 3A09


----------------
 Item Values
----------------

-----------
Items + 00
-----------

--------
Weapons
--------

01 - Long Sword          0F - Machete              1A - Masamune
02 - Broad Sword         10 - Short Sword          1B - Bandit's Sword
03 - Claymore            11 - Hunter's Sword
04 - Great Sword         12 - Battle Rapier        1F - Battle Axe
05 - Shamshir            13 - Master Rapier        20 - Broad Axe
06 - Silver Blade        14 - Ninja Blade          21 - Great Axe
07 - Fire Brand          15 - Swift Sword          22 - Dragon Axe
08 - Arctic Blade        16 - Elven Rapier         23 - Giant Axe
09 - Gaia Blade          17 - Assassin Blade       24 - Vulcan Axe
0A - Sol Blade           18 - Mystery Blade        25 - Burning Axe
0B - Muramasa            19 - Kikuichimonji        26 - Demon Axe

2B - Mace                37 - Wooden Stick         3F - Crystal Rod  
2C - Heavy Mace          38 - Magic Rod            40 - Zodiac Wand  
2D - Battle Mace         39 - Witch's Wand         41 - Shaman's Wand
2E - War Mace            3A - Blessed Ankh
2F - Righteous Mace      3B - Psyenergy Rod
30 - Grevious Mace       3C - Frost Wand
31 - Blessed Mace        3D - Angelic Ankh
32 - Wicked Mace         3E - Demonic Staff

------
Armor
------

4B - Leather Armor       59 - Cotton Shirt         67 - One-Piece Dress   
4C - Psyenergy Armor     5A - Travel Vest          68 - Travel Robe
4D - Chain Mail          5B - Fur Coat             69 - Silk Robe
4E - Armored Shell       5C - Adept's Clothes      6A - China Dress
4F - Plate Mail          5D - Elven Shirt          6B - Jerkin
50 - Steel Armor         5E - Silver Vest          6C - Cocktail Dress
51 - Spirit Armor        5F - Water Jacket         6D - Blessed Robe
52 - Dragon Scales       60 - Storm Gear           6E - Magical Cassok
53 - Demon Mail          61 - Kimono               6F - Mysterious Robe
54 - Asura's Armor       62 - Ninja Garb           70 - Feathered Robe
55 - Spiked Armor                                  71 - Oracle's Robe

76 - Wooden Shield       7F - Padded Gloves        88 - Leather Armlet  
77 - Bronze Shield       80 - Leather Gloves       89 - Armlet
78 - Iron Shield         81 - Gauntlets            8A - Heavy Armlet
79 - Knight's Shield     82 - Vambrace             8B - Silver Armlet
7A - Mirrored Shield     83 - War Gloves           8C - Spirit Armlet
7B - Dragon Shield       84 - Spirit Gloves        8D - Virtuous Armlet
7C - Earth Shield        85 - Battle Gloves        8E - Guardian Armlet
                         86 - Aura Gloves

91 - Open Helm           9C - Leather Cap          A6 - Circlet
92 - Bronze Helm         9D - Wooden Cap           A7 - Silver Circlet
93 - Iron Helm           9E - Mail Cap             A8 - Guardian Circlet
94 - Steel Helm          9F - Jeweled Crown        A9 - Platinum Circlet
95 - Silver Helm         A0 - Ninja Hood           AA - Mythril Circlet
96 - Knight's Helm       A1 - Lucky Cap            AB - Glittering Tiara
97 - Warrior's Helm      A2 - Thunder Crown
98 - Adept's Helm        A3 - Prophet's Hat        FA - Mythril Shirt
                         A4 - Lure Cap             FB - Silk Shirt
                                                   FC - Running Shirt

------------             ----------------          ----------
Minor Items              Psyenergy Items           Key Items
------------             ----------------          ----------

B4 - Herb                C6 - Lash Pebble          B9 - Empty Bottle
B5 - Nut                 C7 - Pound Cube           DD - Venus Star
B6 - Vial                C8 - Orb of Force         DE - Mercury Star
B7 - Potion              C9 - Douse Drop           DF - Mythril Bag(Mars)
B8 - Hermes' Water       CA - Frost Jewel          E0 - Mythril Bag(Jupiter)
BA - Psy Crystal         CB - Lifting Gem          E1 - Mythril Bag
BB - Antidote            CC - Halt Gem             E2 - Small Jewel
BC - Elixir              CD - Cloak Ball           E7 - Dragon's Eye
BD - Water of Life       CE - Carry Stone          E8 - Bone
BE - Mist Potion         CF - Catch Beads          E9 - Anchor Charm
BF - Power Bread         D0 - Tremor Bit           EA - Corn
C0 - Cookie              D1 - Scoop Gem            EB - Cell Key
C1 - Apple               D2 - Cyclone Chip         EC - Boat Ticket
C2 - Hard Nut            D5 - Burst Brooch         EE - Mystic Draught
C3 - Mint                D6 - Grindstone           F3 - Red Key
C4 - Lucky Pepper        D8 - Hover Jade           F4 - Blue Key
E3 - Smoke Bomb          DA - Teleport Lapis       F5 - Mythril Bag(Mr + Jr)
E4 - Sleep Bomb                                    F6 - Jupiter Star
E5 - Game Ticket                                   F7 - Mars Star
86 - Lucky Medal
ED - Sacred Feather
EF - Oil Drop
F0 - Weasel's Claw
F1 - Bramble Seed
F2 - Crystal Powder


-----------
Items + 01
-----------

--------
Weapons
--------

01 - Quick Boots         0E - Huge Sword           1A - Rune Blade
02 - Fur Boots           0F - Mythril Blade        1B - Cloud Brand
03 - Turtle Boots        12 - Levatine             1D - Sylph Rapier
04 - Adept Ring          13 - Darksword            1E - Burning Sword
05 - War Ring            14 - Excalibur            1F - Pirate's Sabre
06 - Sleep Ring          15 - Robbers Blade        20 - Cosair's Edge
07 - Healing Ring        16 - Soul Brand           21 - Pirate's Sabre
08 - Unicorn Ring        17 - Storm Brand          22 - Hypnos' Sword
09 - Fairy Ring          18 - Hestia Blade         23 - Mist Sabre
0A - Cleric's Ring       19 - Lightning Sword      24 - Phaeton's Blade
                                                   25 - Tisiphone Edge

27 - Apollo's Axe        31 - Comet Mace           39 - Cloud Wand
28 - Gaia's Axe          32 - Tungsten Mace        3A - Salamander Rod
29 - Stellar Axe         33 - Demon Mace           3B - Nebula Wand
2A - Captain's Axe       34 - Hagbone Mace         3C - Dracomace
2B - Viking Axe          35 - Blow Mace            3D - Glower Staff
2C - Disk Axe            36 - Rising Mace          3E - Goblin's Rod
2D - Themis' Axe         37 - Thanatos Mace        3F - Meditation Rod
2E - Mighty Axe                                    40 - Fireman's Pole
2F - Tartarus Axe                                  41 - Atropos' Rod

42 - Lachesis' Rule      46 - Trident
43 - Clotho's Distaff
44 - Staff of Anubis

------
Armor
------

48 - Planet Armor        52 - Faery Vest           5B - Dragon Robe
49 - Dragon Mail         53 - Mythril Clothes      5C - Ardagh Robe
4A - Chronos Mail        54 - Full Metal Vest      5D - Muni Robe
4B - Stealth Armor       55 - Wild Coat            5E - Aeolian Cassock
4C - Xylion Armor        56 - Floral Dress         5F - Iris Robe
4D - Ixion Mail          57 - Festive Coat
4E - Phantasmal Mail     58 - Erinyes Tunic
4F - Erebus Armor        59 - Triton's Ward
50 - Valkyrie Mail

61 - Luna Shield         69 - Aerial Gloves        70 - Clear Bracelet
62 - Dragon Shield       6A - Titan Gloves         71 - Mythril Armlet
63 - Flame Shield        6B - Big Bang Gloves      72 - Bone Armlet
64 - Terra Shield        6C - Crafted Gloves       73 - Jester's Armlet
65 - Cosmos Shield       6D - Riot Gloves          74 - Leda's Braclet
66 - Fujin Shield        6E - Spirit Gloves
67 - Aegis Shield

76 - Dragon Helm         7E - Floating Hat         86 - Pure Circlet
77 - Mythril Helm        7F - Nurse's Cap          87 - Astral Circlet
78 - Fear Helm           80 - Thorn Crown          88 - Psychic Circlet
79 - Millenium Helm      81 - Otafuku Mask         89 - Demon Circlet
7A - Viking Helm         82 - Hiotoko Mask         8A - Clarity Circlet
7B - Gloria Helm         83 - Crown of Glory       8B - Brilliant Circlet
7C - Minerva Helm        84 - Alastor's Hood       8C - Beserker Band

8E - Divine Camisole     92 - Leather Boots        99 - Spirit Ring
8F - Herbed Shirt        93 - Dragon Boots         9A - Stardust Ring
90 - Golden Shirt        94 - Saftey Boots         9B - Aroma Ring
91 - Casual Shirt        95 - Knight's Greave      9C - Rainbow Ring
                         96 - Silver Greave        9D - Soul Ring
                         97 - Ninja Sandals        9E - Guardian Ring
                         98 - Golden Boots         9F - Golden Ring

--------------         ----------------            --------
Forge Weapons          Forge Materials             Trident
--------------         ----------------            --------

A1 - Rusty Sword         AD - Tear Stone           B7 - Right Prong
A2 - Rusty Sword         AE - Star Dust            B8 - Left Prong
A3 - Rusty Sword         AF - Sylph Feather        B9 - Center Prong
A4 - Rusty Sword         B0 - Dragon Skin
A5 - Rusty Axe           B1 - Salamander Tail
A6 - Rusty Axe           B2 - Golem Core
A7 - Rusty Mace          B3 - Mythril Silver
A8 - Rusty Mace          B4 - Dark Matter
A9 - Rusty Staff         B5 - Orihalcon
AA - Rusty Staff
AB - Rusty Staff

------------             -----------------
Class Items              Key Items (cont)
------------             -----------------

BB - Mysterious Card     C0 - Healing Fungus        C6 - Milk
BC - Trainers Whip       C1 - Laughing Fungus       C7 - Li'l Turtle
BD - Tomegathericon      C2 - Signal Whistle        C8 - Aquarius Stone
                         C3 - Dancing Idol          C9 - Large Bread
                         C4 - Pretty Stone          CA - Sea God's Tear
                         C5 - Red Cloth             CB - Ruin Key
                                                    CC - Magma Ball


-------------------
1.1 Djinn Hacking
-------------------

Let me start off by saying this: Djinn hacking is incredibly tricky. You
have to do everything perfectly or you will be greeted with usless and
unresponsive Djinn.

Up to this point, everything you've hacked has been controlled by multiple
bytes, aka items and psyenergy. Every different psyenergy and item has had
it's own byte that controls it.

Djinn hacking is far more complex. It is controlled by more than one byte,
which change depending on the status of your Djinn,(standby, set, recovery)
which elements you have and how many of each you have.

    
Felix's Djinn

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
B50                         80 00 00
B60                         80 00 00
B70                         01          01


All of those numbers control one Djinn. Unfortunately at this point I only
understand which numbers to add; not really what they do.

The byte at 608 controlls which Djinn you have. Unlike items and psyenergy,
where each item/psyenergy is accounted for in its own byte, which Djinn you
have is not controlled by seperate bytes. They are controlled by only two.


The game uses a binary system of counting to keep track of your Djinn.

01 - Flint
02 - Granite
04 - Quartz
08 - Vine
10(16) - Sap
20(32) - Ground
40(64) - Bane
80(128) - Echo

So then what the game does is it adds up the value for each indivdual djinn
and its total is what ends up at 608. So for example if you have Flint,
Granite and Quartz, the game adds up the values (1 + 2 + 4) and you get seven,
which goes at 608.

Here's where my understanding of Djinn fails. For some unknown reason you must
put the same value you got above (in my example its 7) and put it in the bytes
directly below in this case 618. I don't know why you have to do this; only
that if you don't bad things will happen.


Status bytes

The two bytes (08 + 0C) are determined by the status of Djinn you have. A value
of 1 means that the Djinn are all in standby. Make sure to ALWAYS use a 1. Then
all you have to do is count up the number of Djinn you hacked in (in my example
I would use 3) and put it in both of the status byte locations. As with the
first byte you must put this value in BOTH status byte locations.


Now as I previously stated, the location also determines which Djinn you have.
For Felix the bytes listed above all control Venus Djinn. If you were to put
the same value (in my case 80) and put it in another location, you would get
the same value Djinn of another element. So if you place the 80 in another
location instead of Echo you could also get Cannon, Fog or Breath.

Confused yet? Just read the addresses and values and maybe you'll get it.

**PLEASE note that if you hack the Djinn the way I do for this guide what you
must hack only one element at a time. If you try to hack multiple elements of
Djinn at once the addresses change and I am not going to list all of the
possiblities at this point. That also includes trying to hack when your
character has two or more Djinn of different elements. Your best off hacking
in all of the Djinn and then arranging them in game. That way the game will
take care of the messy points for you.


-----------------------------
1.11 Djinn Hacking Addresses
-----------------------------

Okay so maybe my explination isn't that clear but I think once you see what
I'm talking about you'll be able to successfully hack your Djinn and only
have to do it once.

Legend
Vs-> Venus
Ms-> Mars
Mc-> Mercury
Jr-> Jupiter


------
Felix 
------

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
B50                         Vs Vs Vs    Mc Mc Mc   
B60 Ms Ms Ms    Jr Jr Jr    Vs Vs Vs    Mc Mc Mc
B70 Ms Ms Ms    Jr Jr Jr

Status

Vs-> B78 + B7C
Mc-> B79 + B7D
Ms-> B7A + B7E
Jr-> B7B + B7F


------
Jenna
------

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
CA0             Vs Vs Vs    Mc Mc Mc    Ms Ms Ms
CB0 Jr Jr Jr    Vs Vs Vs    Mc Mc Mc    Ms Ms Ms
CC0 Jr Jr Jr

Status

Jr-> CC3 + CC7
Vs-> CC4 + CC8
Mr-> CC5 + CC9
Ms-> CC6 + CCA


------
Sheba
------

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
DF0 Vs Vs Vs    Mc Mc Mc    Ms Ms Ms    Jr Jr Jr
E00 Vs Vs VS    Mc Mc Mc    Ms Ms Ms    Jr Jr Jr

Status

Vs-> E10 + E14
Mc-> E11 + E15
Ms-> E12 + E16
Jr-> E13 + E17


------
Piers
------

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
F30                                     Vs Vs Vs
F40 Mc Mc Mc    Ms Ms Ms    Jr Jr Jr    Vs Vs Vs
F50 Mc Mc Mc    Ms Ms Ms    Jr Jr Jr

Status

Vs-> F5C + F60
Mc-> F5D + F61
Ms-> F5E + F62
Jr-> F5F + F63


------
Issac
------

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
620                         Vs Vs Vs    Mc Mc Mc
630 Ms Ms Ms    Jr Jr Jr    Vs Vs Vs    Mc Mc Mc
640 Ms Ms Ms    Jr Jr Jr

Status

Vs-> 648 + 64C
Ms-> 64A + 64E
Jr-> 64B + 64F
Mc-> 649 + 64D


------
Garet
------

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
770 Jr Jr Jr    Vs Vs Vs    Mc Mc Mc    Ms Ms Ms
780 Jr Jr Jr    Vs Vs Vs    Mc Mc Mc    Ms Ms Ms

Status

Ms-> 796 + 79A
Vs-> 794 + 798
Mc-> 795 + 799
Jr-> 797 + 79B


-----
Ivan
-----

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
8C0 Vs Vs Vs    Mc Mc Mc    Ms Ms Ms    Jr Jr Jr
8D0 Vs Vs Vs    Mc Mc Mc    Ms Ms Ms    Jr Jr Jr

Status

Jr-> 8E3 + 8E7
Mc-> 8E1 + 8E5
Vs-> 8E0 + 804
Ms-> 8E2 + 8E6


----
Mia
----

    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
A10 Mc Mc Mc    Ms Ms Ms    Jr Jr Jr    Vs Vs Vs
A20 Mc Mc Mc    Ms Ms Ms    Jr Jr Jr    Vs Vs Vs

Status

Mc-> A3C + A31
Jr-> A2F + A33
Ms-> A2E + A32
Vs-> A2C + A30


------------------
1.12 Djinn Values
------------------

The formula for figuring out which Djinn you have is simple: simply add up the
values assigned to each Djinn. Then use the hex converter to obtain the correct
hex value. Since there are say a few hundred thousand possible combinations per
element, I will only list the values assigned to each Djinn.

         Venus      Mars       Jupiter   Mercury 
1        Flint      Forge      Gust      Fizz
2        Granite    Fever      Breeze    Sleet
4        Quartz     Corona     Zephyr    Mist
8        Vine       Scorch     Smog      Spritz
16       Sap        Ember      Kite      Hail
32       Ground     Flash      Squall    Tonic
64       Bane       Torch      Luff      Dew
128      Echo       Cannon     Breath    Fog
256      Iron       Spark      Blitz     Sour
512      Steel      Kindle     Ether     Spring
1024     Mud        Char       Waft      Shade
2048     Flower     Coal       Haze      Chill
4096     Meld       Reflux     Wheeze    Steam
8192     Petra      Core       Aroma     Rime
16384    Salt       Tinder     Whorl     Gel
32768    Geode      Shine      Gasp      Eddy
65536    Mold       Fury       Lull      Balm
131072   Crystal    Fugue      Gale      Serac

** Also note the values listed above are NOT hex values. You must add up those
numbers and then convert them using the hex converter.

Just so you know, FF 01 will net you the first 9 Djinn and 00 EF 03 will net you
the 10th through 18th.


------------------------------
A.4 Frequently Asked Questions
-------------------------------

Q: How do I get my game onto the computer?

A: There are two ways that you can get your save on the computer. The first
is to buy a special flash reader that connects to your pc and allows you to
transfer your data, much the same way a gameshark works. The second is to
obtain a "ROM" of the game from the internet.

Q: So this works with my GBA, right?

A: Yes. If you can get your GBA save fileon the computer, this is exactly the
method to use to hack it.

Q: Where can I find a ROM for Golden Sun?

A: I honestly don't know.

Q: What should I use to play my ROM?

A: Visual Boy Advanced is top dog when it comes to GBA emulators, and it's
a free download.

Q: Is this even legal?

A: Read Gamefaqs section about roms/warez to find out.

Q: So what was the name of the hex editor again?

A: You really need to pay attention. I strongly recommend WinHex because it
allows you to highlight large chunks of code effortlessly.


----------------
A.5 Legal Stuff
----------------

This guide is to only be posted on
Gamefaqs.com
Neoseeker.com.
SuperCheat.com

If you wish to put this guide on your site contact and I'll let you know.
I'd say you've got a good chance though: any publicity is good for me.
This guide is not to be reproduced for profit; only personal use. But you
wouldn't even think of doing something like that, would you. :)

Copyright Cody Trombley 2006


-----------------
A.6 Contact Info
-----------------

If you have any questions, comments, typos, maybe some help please feel free 
to email me at keyblade_master_02(at)yahoo.com or AIM me at skye0052.
Unfortunately I do not check my email often enough and if I take a while to
get back to you I apologize in advance. If you are truely desperate to
contact me, I am almost always on Xfire as skye0053 whenever I'm online so
if you request to be added to my friends list please just make sure to say
for hacking help or I will most likely ignore you.


------------
A.7 Credits
------------

Ahh, so much credit to give. First I have to give credit to Camelot for
making undoutably the greatest RPG for GBA and one of my favorites of all
time. Second a huge amount of credit goes to Kaitia who wrote the other
game save hack guide and is responsible for getting me started in hacking
and in helping me explain the hacking process. And for my friend for
originally giving me the game.


----------------
A.8 Coming Soon
----------------

Well between my guide and Kaitia's there is not much left to be hacked in
Golden Sun 2.
Restore Page

