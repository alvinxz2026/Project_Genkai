---
source_id: link-kirby-rng
author: Link_Kirby
url: https://gamefaqs.gamespot.com/gba/561356-golden-sun-the-lost-age/faqs/25734
type: mechanics
covers: [mechanics, items]
quality: default
summary: RNG 机制与掉落/锻造刷取方法（ICC、psynergy/djinn/battle RN 值）。机制向，非实体提取源。
gs1_counterpart:
notes: 这个不知道我们用不用的上
---

# Random Number Generator FAQ by Link_Kirby

## TABLE OF CONTENTS

 Table of Contents             Ctrl+F Search
+---------------------------------+-----+
| 1)Introduction                  | 010 |
| 2)Basics                        | 020 |
|   A)ICC and item rarity         | 021 |
|   B)Psynergy RN Values          | 022 |
|   C)Djinn RN Values             | 023 |
|   D)In-battle RN Values         | 024 |
| 3)Making your own RNG methods   | 030 |
|   A)Basic two-enemy RNG methods | 031 |
|   B)One-enemy RNG methods       | 032 |
|   C)Three-enemy RNG methods     | 033 |
| 4)Mentionable Item Drops        | 040 |
| 5)Premade RNG methods           | 050 |
|   A)Weapons                     | 051 |
|   B)Armor                       | 052 |
|   C)Forgable Items              | 053 |
|   D)Rare Healing Items          | 054 |
| 6)Frequently Asked Questions    | 060 |
| 7)Troubleshooting               | 070 |
| 8)Credits                       | 080 |
| 9)Version History               | 090 |
| 10)Legal Stuff                  | 100 |
+---------------------------------+-----+

---

END OF TABLE OF CONTENTS

---

Random Number Generator FAQ by Diego Gonzalez (a.k.a. Link Kirby)

Title: Golden Sun: The Lost Age
Platform: Game Boy Advance
E-mail: link_kirby34@hotmail.com



===============================================================================
1)Introduction - 010
===============================================================================


Welcome to the Golden Sun: The Lost Age RNG FAQ. Hopefully when you are done
reading this, you will know enough about RNG methods that you can make your
own. 

But what is an RNG, you ask? RNG stands for random number generator. Putting it
*VERY* simply, it is a hidden counter in the game that changes whenever certain
things happen in battle.

There are actually two different RNGs in the game, but we will only focus on
the one that is the determining factor in whether or not enemies drop items
(the "Battle RNG"). There is also a "General" RNG that determines other
"random" things in the game (such as which monsters are enountered after a hard
reset and which item you forge from the blacksmith), but it requires PRECISE
timing to take advantage of. I may go into it in later versions of this FAQ,
but I will ignore it for now.

For the purposes of this FAQ, the RNG is always a whole number. From here on
out, I will referring to these numbers as "RN".

In order to get a rare item from an enemy it must be killed on the right RN.
The RNG methods will work by manipulating the RNG so that the monster always
falls on the right RN.

The rarest items only can only be obtained on a few RNs; the chances of you
getting that item normally are about 1 in 256. Of course, we don't like those
odds. RNG methods are ways of beating the odds and getting the item at will.
But first you must learn how to manipulate the RNG in a working method.

Before you go deeper into this FAQ, please note that RNG methods are an abuse
of the poorly designed random number generator within the game. Some people may
consider it cheating, so if you have any ethical problems with this, leave now.

-------------------------------------------------------------------------------

If after reading how RNG methods work you still have problems with RNG methods,
check the Frequently Asked Questions and Troubleshooting sections at the bottom
of the FAQ.

Should you still have questions regarding RNG methods, contact me at:

link_kirby34@hotmail.com

Please try your best at grammar and puntuation if you do send me an e-mail,
it's easier on my eyes. I'll usually read and respond to well presented
questions or comments first. Keep that in mind should you decide to contact me.


===============================================================================
2)Basics - 020
===============================================================================


There are several basic requirements that an RNG method must meet in order to
work. The first and most important is that the enemy whose item you want must
die on the correct RN. More on that in the next section.

The next most important thing is HOW the enemy dies: it must be killed by a
character using an attacking Djinni as a weapon. Not just any Djinni will do;
it must be a Djinni of the element the enemy is weak against.

Killing the enemy with a Djinni of its weakness causes the enemy to flash a
rainbow of colors before it dies; this is known as the "Darkpanther method",
named after its discoverer.

Every enemy has an elemental weakness. So just attack the enemy with a Djinni
of its elemental weakness and kill it with that Djinni. Assuming your
elemental power is high enough and the enemy dies on the right RN as a result
of that attack, the method is a success and the item is dropped. Let's recap
so far:


-The enemy whose item you want must die on the correct RN.
-It must be killed by an attacking Djinni via the Darkpanther (DP) method.



+---------------------------+
| ICC and item rarity - 021 |
+---------------------------+


ICC stands for Item Chance Class, named by Terence back when he first extracted
the monster data from the first Golden Sun. It is the system of classification
that determines which items will drop on which RNs. It classifies the monsters
based on the rarity of the items they drop.

The monsters that drop the rarest items are classified as ICC 9. The second
rarest are ICC 8, third rarest ICC 7, and so on.

The easiest items to get are ICC 1. ICC 1 items will always fall, as you have a
100% chance of getting the item from the monster. For each subsequent ICC, the
chances of the item dropping are halved. Your odds of getting an ICC 2 item are
1/2, ICC 3 is 1/4, ICC 4 is 1/8... all the way up to ICC 9, the rarest one at
1/256.

Those odds are based on the total number of RNs that will drop that item. The
higher the ICC class it's in, the less RNs there are that will make that item
drop. Here is Terence's list of the different ICCs and the first few RNs that
are required for an item in that ICC class to drop WITHOUT the DP method:


ICC 9: 1
ICC 8: 1
ICC 7: 1, 31
ICC 6: 1, 3, 27, 31
ICC 5: 1, 3, 27, 31
ICC 4: 1, 3, 6, 8, 13, 14, 16, 21, 23, 26, 27, 30, 31


This list only goes up to RN 40. There are many more RNs at higher numbers
(over 4 billion in fact), but they are extremely difficult to use in simple RNG
methods. You'll see why shortly.

Unfortunately, if you knew anything about RNGs to begin with, you know it is
impossible to make an enemy die on anything less than 5 RN with the DP method,
which means that any RN of less than 5 is useless in RNG methods; there is no
way to make ICC 9 and ICC 8 items drop.

However, using the DP method makes the monster's ICC drop by two. So an ICC 9
item will drop on an RN that corresponds to an ICC 7 item. Let's remove the
"unusable" RNs from Terence's list and lower the ICCs by two. Here's what the
ICCs and the RNs required for an item in that ICC class to drop look like now
(the ICCs in parantheses are the original ICCs):


ICC 7(ICC 9): 31
ICC 6(ICC 8): 27, 31
ICC 5(ICC 7): 27, 31
ICC 4(ICC 6): 6, 8, 13, 14, 16, 21, 23, 26, 27, 30, 31


So after using the Darkpanther method to lower the ICC class of the item by
two, we can see that the previously unreachable ICC 9 and ICC 8 items can now
be obtained.

ICC 9 items now require the enemy to die (by DP method) on the 31st RN, and ICC
8 items can be obtained on 27 RN and 31 RN.

Note that ICCs are attached to monsters, not items; two monsters that drop the
same item could have different ICCs.

Also take note that 31 RN is the only RN that will work for every item in every
ICC with the DP method. It is the universal RN in RNG methods. This guarantees
the item will drop, regardless of how rare the desired item is.



+-------------------------+
|Psynergy RN Values - 022 |
+-------------------------+


Now you know the specific RN you have to kill the enemy on in order to make it
drop the item you want. Now you have to find a way to get to that RN. Here are
the RN values for several types of Psynergy:



Attack Psynergy: This is the only kind that actually damages enemies. This kind
                 of Psynergy has been dubbed "Area Psynergy" because almost all
                 of these damage multiple opponents. Shine Plasma, Eruption,
                 Glacier, and Mother Gaia are all examples of Attacking 
                 Psynergy. There are also some that only hit one enemy, like
                 Oddysey or Serpent Fume. All Attacking Psynergy "consumes"
                 (counts for) 2 RN for each enemy hit.

Healing Psynergy: This Psynergy is used to heal your entire party or just one
                  person. Wish Well and Healing Aura are examples of group
                  Healing Psynergy, and Ply Well, and Cure Well are all
                  examples of single Healing Psynergy. They all consume 2 RN
                  for each person healed.

Support Psynergy: All Psynergy that increases one or more of your characters'
                  stats (as in Attack, Defense and Resistance) is called
                  Support Psynergy. High Impact, Protect, and Resist increase
                  the group's stats, and Impact, Guard, and Ward all increase
                  one person's stats. They all consume 1 RN for each person
                  affected. This also applies to the Samurai versions of the
                  Support Psynergy.

Status Psynergy: All non-damaging Psynergy that targets enemies is Status
                 Psynergy. Almost every Psynergy that doesn't fit in the other
                 three categories goes in here. Sleep, Break, Impair, Bind, and
                 Blunt are all examples of Support Psynergy. They all consume 1
                 RN for each enemy affected. Drain is also in this category,
                 even though it causes damage if it connects.


*Cure Poison and Restore consume 0 RN if their target isn't affected by a
status ailment that they can cure. If the target is affected by a compatible
status ailment (meaning that Cure Poison/Restore get rid of it) then they
consume 1 RN.*


Now we have all the different types of Psynergy that you can use. This is
basically all we need to get to 31 RN and kill the enemy with the right RN.
Unfortuantely, we're missing one vital piece of information: the Djinn!
Remember that you need you finish off the enemy with a Djinni of its elemental
weakness for the method to work.



+-----------------------+
| Djinn RN Values - 023 |
+-----------------------+


What follows is a complete listing of the RN Values for every Djinn in the
game, courtesy of TheScythe. Because of the large number of different Djinn
effects, the following may be a bit hard to understand. Here's TheScythe's
shortened summary for all the different Djinn effects:

(Elemental Bonus is explained at the bottom)

-------------------------------------------------------------------------------
Normal Attack Djinn - 2 RN per target + Elemental Bonus
-------------------------------------------------------------------------------
Reviving/Status-Healing Djinn - 0 RN per target + Elemental Bonus
-------------------------------------------------------------------------------
HP or PP Recovery/PP Draining/Barrier Djinn - 1 RN per target + Elemental Bonus
-------------------------------------------------------------------------------
Hiding Away/Stat Altering/Readying For Action Djinn - 1 RN per target +
Elemental Bonus
-------------------------------------------------------------------------------
Recovery Speed-Up Djinn - 0 RN
-------------------------------------------------------------------------------
Forced Self-Attack Djinn - 2 RN + 1 standard enemy attack RN + Elemental Bonus
-------------------------------------------------------------------------------
Countering Djinn - 1 RN on your turn (and Elemental Bonus) + 2 RN on counter
(and Elemental Bonus)
-------------------------------------------------------------------------------
Two Part Djinn [A] (Whorl/Gale) - 1 RN for 'breathing in' (No Elemental Bonus)
+ 1 RN for damage (Elemental Bonus)
-------------------------------------------------------------------------------
Two Part Djinn [B] (Gust) - 1 RN for 'breathing in' (No Elemental Bonus) + 1 RN
for damage (Elemental Bonus)
-------------------------------------------------------------------------------
Ending Turn Djinn - 1 RN (No Elemental Bonus)
-------------------------------------------------------------------------------

And if you want specific Djinni RN Values, here is the table that TheScythe
provided. The Djinn are organized the way the game organizes them:


Venus Djinn:

Flint:   2 RN
Granite: 1 RN per target
Quartz:  0 RN
Vine:    1 RN per target
Sap:     2 RN
Ground:  1 RN
Bane:    2 RN

Echo:    2 RN
Iron:    1 RN per target
Steel:   2 RN
Mud:     1 RN per target
Flower:  1 RN per target
Meld:    2 RN
Petra:   1 RN
Salt:    0 RN per target
Geode:   2 RN
Mold:    3 RN
Crystal: 1 RN per target


Mercury Djinn:

Fizz:    1 RN
Sleet:   2 RN
Mist:    2 RN
Spritz:  1 RN per target
Hail:    2 RN
Tonic:   0 RN per target
Dew:     0 RN

Fog:     2 RN
Sour:    2 RN
Spring:  1 RN
Shade:   1 RN per target
Chill:   2 RN
Steam:   1 RN per target
Rime:    1 RN
Gel:     2 RN
Eddy:    0 RN(Just 0 RN. No Element Bonus.)
Balm:    0 RN per target
Serac:   2 RN


Mars Djinn:

Forge:   1 RN per target
Fever:   2 RN
Corona:  1 RN per target
Scorch:  2 RN
Ember:   1 RN per target
Flash:   1 RN per target
Torch:   2 RN

Cannon:  2 RN
Spark:   0 RN
Kindle:  1 RN per target
Char:    2 RN
Coal:    1 RN per target
Reflux:  1 RN on your turn, 2 RN on counter.
Core:    2 RN
Tinder:  0 RN
Shine:   2 RN
Fury:    2 RN
Fugue:   1 RN per target


Jupiter Djinn:

Gust:    1 RN(Breathing In, No Elemental Bonus) + 1 RN(Damage, Elemental Bonus)
Breeze:  1 RN per target
Zephyr:  1 RN per target
Smog:    2 RN
Kite:    1 RN
Squall:  2 RN
Luff:    1 RN

Breath:  1 RN
Blitz:   2 RN
Ether:   1 RN
Waft:    2 RN
Haze:    1 RN
Wheeze:  2 RN
Aroma:   1 RN per target
Whorl:   1 RN(Breathing In, No Elemental Bonus) + 1 RN(Damage, Elemental Bonus)
Gasp:    *Random Number Between 1 and 3* RN???
Lull:    1 RN(Just 1 RN. No Elemental Bonus.)
Gale:    1 RN(Breathing In, No Elemental Bonus) + 1 RN(Damage, Elemental Bonus)



These are all the Djinn RN Values. When a Djinni is unleashed in battle, the
value listed for it in the previous table is how many RNs it consumes.

I'm sure you're also wondering what "Elemental Bonus" means. Basically,
whenever a Djinni is unleashed, the Djinni consumes one more RN than normal per
target if its target is weak against it elementally. The Elemental Bonus is
applied even if the Djinni does no damage, and also to your party.

Your characters' weaknesses are dependent on their current class and equipment
setup. Your characters' natural weakest element is the Affinity of their
Primary elements, followed by their Weakness and Neutral elements.

For example, let's say Isaac is in his final base class, Slayer. In this
class he has nine Venus Djinn. Assuming he had no Resist-altering equipment on,
this is what his Resistances would look like:

Primary (Earth/Venus)  : 164
Affinity (Fire/Mars)   :  86
Weakness (Wind/Jupiter):  87
Neutral (Water/Mercury):  88

As you can see, Isaac's current elemental weakness is Fire. All Mars Djinn
unleashed (that target him) will consume 1 extra RN because of the Elemental
Bonus. Now let's change his class to Master. For Isaac to become a Master, he
needs to be equipped with five Jupiter Djinn and four Mars Djinn. Each Djinni
increases his Resistance of that element by five:

Primary (Earth/Venus)  : 114
Affinity (Fire/Mars)   : 106
Weakness (Wind/Jupiter): 112
Neutral (Water/Mercury):  88

Now Isaac's elemental weakness is Water. Now, all Mercury Djinn that target him
will consume 1 extra RN because of the Elemental Bonus.

All of this info is great to know to work out possible problems in the methods,
but there is only one type of Djinni that we are required to know about in RNG
methods. We need to know is how much RN an attacking Djinni would consume, and
that would be 2 RN.

However, the Djinni used in RNG methods is required to be of the element that
the enemy is weak against. That means that we always apply the Elemental Bonus
to the Djinni, so it consumes 3 RN total. All Djinni used to finish off the
enemy in RNG methods (DP method) consume 3 RN.



+---------------------------+
| In-battle RN Values - 024 |
+---------------------------+


The Psynergy and Djinn aren't the only things that affect the RNG. Some things
that always happen during the course of battle will also affect the RNG. They
are easily kept track of and shouldn't pose a problem.


Start of battle: The battle starting increases the RN by one if you get the
                 first strike. You'll know you got the first strike if the game
                 text says: "Felix's party attacks first!" at the start of the
                 battle. Don't worry about this one, as it will always happen
                 in an RNG method anyway. Just know that this will always be
                 the first RN consumed in the RNG method.

Enemy actions: Since most RNG methods take place over two turns, you only have
               to worry about this for the second turn. At the start of the
               every turn that enemies get to act in, the RNG increases by one
               for each "enemy action" (how many times the enemies attack).
               Since most enemies only get to attack once per turn, this is 
               usually 1 RN per enemy. 

               However, there are three enemies that get to attack more than 
               once: Pheonixes, Fire Birds, and Wonder Birds. Pheonixes and
               Fire Birds each attack twice per turn (2 RN), and Wonder Birds
               attack thrice per turn (3 RN). They are the only exceptions.

Enemy deaths: The death of an enemy consumes 1 RN. However, this is also the
              final step in all RNG methods. Remember how the enemy must die on
              the right RN? The death of the enemy must cause the RN to rise to
              the "Target RN". In an RNG method where the Target RN is 31, the
              death of the enemy must be the 31st RN to be consumed. The enemy
              must die on the correct RN or you won't get anything.


That's it. The Psynergy, Djinn, and In-battle RN values are all we need to
start making RNG methods. Now it's time to learn how to use the values in a
working RNG method.




===============================================================================
3)Making your own RNG methods - 030
===============================================================================


Now we'll start with RNG methods lessons. Since the most basic RNG methods
involve two enemies, I'll start with those. This is really the last part of the
FAQ you have to read to understand how to make your own RNG methods.

I should probably note the format the RNG methods will be in to avoid
confusion. First, the characters and their actions will be on the left. On the
right in the brackets [] will be the amount of RN consumed by that character's
action, and the current RN total next to that. Something like this:


Jenna casts Fume!             [2 RN, 3 RN total]  <---Single Attack Psynergy!
        |                       |      |                         |
        |                       |      |                         |
Character/action                |      |                         |
                   RN from action      Current RN total          Things to note


Every RNG method in this section will be written in this fashion. The RNG
methods in the Premade RNG method section will only include the characters'
actions.



+-----------------------------------+
| Basic two-enemy RNG methods - 031 |
+-----------------------------------+


Two-enemy RNG methods are the easiest to execute. You know that you need the
enemy to die on the 31st RN to make the item drop. So you need to consume a
certain number of RNs to make the monster fall on the 31st RN. How many RNs
would that be? Recall how some things that always happen in battle also affect
the RNG. Let's take those into consideration:


-The enemy must die on the 31st RN, so we must consume 30 RN before the enemy
 death (which is the 31st).

-The start of the battle consumes 1 RN, the start of the second turn consumes 1
RN per enemy action (2 enemies = 2 RN), and the unleashing of the weakness
Djinni (must always happen too) consumes 3 RN.

-So of the 30 RN we must consume before the enemy dies, 6 RN of it will always
happen anyway. That means we have to consume 24 RN in two-enemy RNG methods.


Have you figured out why two-enemy RNG methods are the simplest? 24 RN is a
very nice number to work with. Remember that Attack Psynergies consume 2 RN per
enemy hit? Since these RNG methods involve two enemies, that's 4 RN per Attack
Psynergy. All we have to do is use six Attack Psynergies, and that's our 24 RN!

There is also one more type of Psynergy that is very useful in two-enemy RNG
methods. Healing Psynergy, or group Healing Psynergy to be more specific. As
you know, Healing Psynergy consumes 2 RN for each ally healed. Group Healing
Psynergies like Aura and Wish consume 8 RN. That's the equivalent of two Attack
Psynergies. They can be very useful when you only have a limited number of
actions before the Djinni unleash. You'll see what I mean in the second example
RNG method.

Don't forget the Djinni unleash either, it must be the next action after the
last of the six Attack Psynergies. The enemy must flash colors and die as a
result of the unleash.

However, not just anyone can unleash the weakness Djinni. TheScythe has found
that your elemental Power must be greater than the monster's resistance by a
certain amount to make enemies flash using the DP method. When killing the
monster on RN 31 with the DP method, there has to be a difference of AT LEAST
38 between the unleasher's Power and the enemy's Resistance for the enemy to
flash.

DON'T WORRY ABOUT THAT. As long as your characters are in their BASE CLASSES,
it isn't a problem. Just keep it in mind.


To sum it all up:

-Hard Reset (turn GBA off/on)
-Battle Start
-Six Attack Psynergies
-Djinni unleash (DP method)
-Enemy dies
-Item dropped at end of battle

Here's an example RNG method to illustrate this better. I am using a party of
Felix, Sheba, Jenna, and Piers in base classes. Since this is just an example,
let's say they attack in that order (normally, Sheba would be the fastest by
far). 

I am trying to get a Tisiphone Edge, dropped by Cruel Dragons in the corridors
of Islet Cave. I hard reset (turn the GBA off/on). I find two Cruel Dragons
together:



Cruel Dragon1 appeared!
Cruel Dragon2 appeared!
Felix's party attacks first!  [1 RN]

TURN 1
Felix casts Mother Gaia!      [4 RN, 5 RN total]     <---1st Attack Psynergy!
Sheba casts Shine Plasma!     [4 RN, 9 RN total]     <---2nd Attack Psynergy!
Jenna casts Cycle Beam!       [4 RN, 13 RN total]    <---3rd Attack Psynergy!
Piers casts Glacier!          [4 RN, 17 RN total]    <---4th Attack Psynergy!

Second turn begins            [2 RN, 19 RN total]

TURN 2
Felix casts Earthquake!       [4 RN, 23 RN total]    <---5th Attack Psynergy!
Sheba casts Plasma!           [4 RN, 27 RN total]    <---6th Attack Psynergy!
**Jenna unleashes Core!**     [3 RN, 30 RN total]    <---Djinni unleash!
**You felled Cruel Dragon1!** [1 RN, 31 RN total]    <---Monster dies!


Felix and Sheba casted the last two Attack Psynergies, then Jenna unleashed an
attacking Djinni of the Cruel Dragon's weakness (Mars). The enemy flashed and
died on the 31st RN. That is all that matters. Now that the enemy has been
killed by a Djinni of its weakness on the 31st RN, I can kill the other enemy
any way I want. Physical attack, Psynergy, Djinni, summon, who cares? Once the
battle is over, I will get the Tisiphone Edge.

Anyway...

Now let's try another one. This time I'm trying to get Lachesis' Rule. Those
are dropped by Mad Demons in Anemos Inner Sanctum. This time, the attacking
order of my party is Jenna, Sheba, Felix, Piers. 

There is just one problem. The Mad Demon's weakness is Jupiter. The only person
who has that element of Djinn is Sheba. Sheba unleashing the Djinni in the
second turn means that I only have five actions before the Djinni unleash. Six
Attack Psynergies in five actions, how do I do that?

This is where "group" Healing Psynergy comes in handy. Unlike Attack Psynergy,
Healing Psynergy affects your party. It consumes 2 RN per ally healed. So a
group Healing Psynergy like Aura would consume 8 RN, 2 RN for each person.
That's twice as much as a regular Attack Psynergy! Group Healing Psynergy
counts as much as two Attack Psynergies. Problem solved.

Now for the example RNG method. I hard reset in Anemos Inner Sanctum, then I
encounter two Mad Demons:



Mad Demon1 appeared!
Mad Demon2 appeared!
Felix's party attacks first!  [1 RN]
f
TURN 1
Jenna casts Aura!             [8 RN, 9 RN total]   <---1st and 2nd Attack Psy!
Sheba casts Spark Plasma!     [4 RN, 13 RN total]  <---3rd Attack Psynergy!
Felix casts Grand Gaia!       [4 RN, 17 RN total]  <---4th Attack Psynergy!
Piers casts Megacool!         [4 RN, 21 RN total]  <---5th Attack Psynergy!

Second turn begins            [2 RN, 23 RN total]

TURN 2
Jenna casts Cycle Beam!       [4 RN, 27 RN total]  <---6th Attack Psynergy!
**Sheba unleashes Squall!**   [3 RN, 30 RN total]  <---Djinni unleash!
**You felled Mad Demon1!**    [1 RN, 31 RN total]  <---Monster dies!


I got a Lachesis' Rule. That wasn't too hard, now was it? Thanks to group
Healing Psynergy, I was able to get the monster to drop the item on RN 31 in
only five actions. Remember group Healing Psynergies when you are performing
RNG methods, they are useful when you only have a limited number of actions or
if the monster is too weakened to be hit with another Attack Psynergy.

+-----------------------------------------------------------------------------+
| NOTE: Remember how Pheonixes/Fire Birds/Wonder Birds consume 2/2/3 RN at    |
| the start of the second turn? If they are present in the RNG method, you    |
| have to subtract 1 RN for each Pheonix/Fire Bird present and 2 RN for each  |
| Wonder Bird present from the 24 RN you need to consume. Take it from there. |
+-----------------------------------------------------------------------------+

That's all for two-enemy RNG methods. Now one-enemy RNG methods. They are
slightly more complicated. 



+-----------------------------+
| One-enemy RNG methods - 032 |
+-----------------------------+


One enemy RNG methods can't be done in the same way as the two-enemy RNG
methods I just demonstrated. Attack Psynergies like Mother Gaia consume 2 RN
for each enemy hit, so they would only consume 2 RN if there is only one enemy.

Also, recall that in two-enemy RNG methods, you needed to consume 24 RN before
the enemy was hit with the Djinni. In one-enemy RNG methods, you need to
consume 25 RN because there is one less enemy action at the start of the second
turn. You have to find other ways of consuming RN as now you need to consume an
odd number of RN.

An easy way to solve this problem is to use group Healing Psynergy and Support
Psynergy. Unlike Attack Psynergy, group Healing Psynergy consistently consumes
the same amount of RN because it affects your party, while Attack Psynergy
depends on the number of monsters present. Wish and Aura are fine examples of
Healing Psynergy.

Support Psynergy takes care of the odd RN consumption. It affects the party and
consumes 1 RN per target affected. Impact is a good example of Support
Psynergy, and since it only affects one ally, it will consume the odd RN.

Using these Psynergies, let's try a one-enemy RNG method. We'll use Felix,
Sheba, Jenna, and Mia in their base classes, in that attack order. Sheba has
Support Psynergy, and Jenna and Mia have group Healing Psynergy. I'm trying to
get another Tisiphone Edge from a Cruel Dragon in the corridors of Islet Cave.
This time, however, I only encounter one of them:


Cruel Dragon appeared!
Felix's party attacks first!  [1 RN]

TURN 1
Felix casts Mother Gaia!      [2 RN, 3 RN total]   <---Attack Psynergy
Sheba casts Impact!           [1 RN, 4 RN total]   <---Support Psynergy
Jenna casts Aura!             [8 RN, 12 RN total]  <---Group Healing Psynergy
Mia casts Wish!               [8 RN, 20 RN total]  <---Group Healing Psynergy

Second turn begins            [1 RN, 21 RN total]  <---Need to consume 6 RN

TURN 2
Felix casts Spire!            [2 RN, 23 RN total]  <---Attack Psynergy
Sheba casts High Impact!      [4 RN, 27 RN total]  <---Group Support Psynergy
**Jenna unleashes Core!**     [3 RN, 30 RN total]  <---Djinni unleash!
**You felled Cruel Dragon!**  [1 RN, 31 RN total]  <---Monster dies!


The battle ends with me holding a Tisiphone Edge. Notice how Sheba casted High
Impact in the second round? Support Psynergy consumes 1 RN per ally affected,
and High Impact affected the whole party. That's 4 RN. So depending on which
Support Psynergy you use, it will consume either 1 RN or 4 RN. That makes it
useful in two-enemy RNG methods too, taking the place of one Attack Psynergy.

To simplify one-enemy RNG methods better than the example did, let's look at a
basic "template" of a one-enemy RNG method:


Attack Psynergy            2 RN
Support Psynergy           1 RN
Group Healing Psynergy     8 RN
Group Healing Psynergy     8 RN

Attack Psynergy            2 RN
Group Support Psynergy     4 RN
-------------------------------
                          25 RN


As long as the actions indicated are performed, you will get the item drop.
Simple, right? I think so.

+-----------------------------------------------------------------------------+
| NOTE: Remember how Pheonixes/Fire Birds/Wonder Birds consume 2/2/3 RN at    |
| the start of the second turn? If they are present in the RNG method, you    |
| have to subtract 1 RN for each Pheonix/Fire Bird present and 2 RN for each  |
| Wonder Bird present from the 25 RN you need to consume. Take it from there. |
+-----------------------------------------------------------------------------+

Very useful to know. Let's move on to the last part: three-enemy RNG methods.



+-------------------------------+
| Three-enemy RNG methods - 033 |
+-------------------------------+


Because there are now three enemies, you must consume 23 RN in these RNG
methods because now there is one more enemy action in the second turn instead
of one less.

Because there are now three enemies, Attack Psynergy may consume different
amounts of RN depending on how many enemies are hit. Recall that Attack
Psynergy consumes 2 RN per enemy hit. In three-enemy RNG methods, the number of
enemies that Attack Psynergy hits depends on the Psynergy and the targeted
character. An example to illustrate this better:


Eruption is an Attack Psynergy that hits the targeted enemy and one enemy on
both sides of it. When targeting the center enemy it looks like this:

          Enemy1     Enemy2    Enemy3
                       ^
            ^          ^          ^
                     Target

Eruption hits all enemies in the three-enemy RNG method when targeting the
center, consuming 6 RN. Target one of the other two enemies, however, and then
it changes:

          Enemy1     Enemy2    Enemy3
            ^
            ^          ^
          Target

When targeting the first enemy, the third one isn't even hit, only consuming 4
RN. In this way, you can change how many RNs are consumed by the way you target
the enemies. Keep in mind that this only applies to Attack Psynergies that have
an attack radius like Eruption (hits the target and one enemy on both sides of
it). Now that that is set, let's move on to the last type of Psynergy.

Status Psynergy is somewhat like Support Psynergy in that it consumes 1 RN per
target. However, Status Psynergy affects the enemies, not your team like
Support Psynergy does. Since there are three enemies, a Status Psynergy that
affects all of them will consume 3 RN.

There is one more thing you should note about Status Psynergy. The RN will be
consumed regardless of whether or not the target is affected. For example,
let's say I cast Sleep on one enemy, but it doesn't fall asleep. The RN is
still consumed even though the enemy was not affected by Sleep.

Of the 23 RN we need to consume, 3 RN of it will come from the Status Psynergy.
That means that we need 20 RN from other Psynergies. Remember how some Attack
Psynergies consume 6 RN in three-enemy RNG methods? Let's make a basic template
for three-enemy RNG methods:

3-target Status Psynergy: +3 RN
3-target Attack Psynergy: +6 RN
3-target Attack Psynergy: +6 RN
Group Healing Psynergy:   +8 RN
-------------------------------
                          23 RN

With this template, we can see that we can consume all the required RN in the
first turn, leaving the Djinni unleash as the only action in the second turn.
Now that we now what we're going to do, let's try an example RNG method. We'll
use Sheba, Jenna, Felix, and Piers, in that attack order. Sheba has a 3-target
Status Psynergy, Jenna has the group Healing Psynergy, and Felix and Piers have
3-target Attack Psynergies.

I've aquired enough weapons, now I need some Beserker Bands. Those are dropped
by Druj in Inner Islet Cave. They are weak to Mars, so Jenna will do the
unleashing. 

After hard reseting, I encounter one Druj and two Chimera Worms. The Chimera
Worms have very little HP compared to the Druj, so it's important not to kill
them. I'll have to use very weak Psynergy and target the Druj so that the
Chimera Worms take minimal damage.



Druj appeared!
Chimera Worm1 appeared!
Chimera Worm2 appeared!
Felix's party attacks first!  [1 RN]

TURN 1
Sheba casts Sleep!            [3 RN, 4 RN total]   <--3-target Status Psynergy!
Jenna casts Aura!             [8 RN, 12 RN total]  <--Group Healing Psynergy!
Felix casts Mother Gaia!      [6 RN, 18 RN total]  <--3-target Attack Psynergy!
Piers casts Supercool!        [6 RN, 24 RN total]  <--3-target Attack Psynergy!

Second turn starts            [3 RN, 27 RN total]

TURN 2
Sheba defends                 [0 RN, 27 RN total]  <--Defend to skip an action!
**Jenna unleashes Torch!**    [3 RN, 30 RN total]  <--Djinni unleash!
**You felled Druj!**          [1 RN, 31 RN total]  <--Monster dies!

By sticking to my strategy, I was able to make the Druj drop its Beserker Band.
The three-enemy RNG method template above can be completed in the first turn,
so the only thing left to do in the second turn is unleash the Djinni.


+-----------------------------------------------------------------------------+
| NOTE: Remember how Pheonixes/Fire Birds/Wonder Birds consume 2/2/3 RN at    |
| the start of the second turn? If they are present in the RNG method, you    |
| have to subtract 1 RN for each Pheonix/Fire Bird present and 2 RN for each  |
| Wonder Bird present from the 23 RN you need to consume. Take it from there. |
+-----------------------------------------------------------------------------+


Now you have all the knowledge you need to create and use your own RNG methods.
Let's recap what you learned in the previous sections:


-Attack Psynergy: 2 RN per target, affects enemies
-Healing Psynergy: 2 RN per target, affects allies
-Support Psynergy: 1 RN per target, affects allies
-Status Psynergy: 1 RN per target, affects enemies

-1 RN at battle start
-1 RN per enemy action at 2nd turn start
-1 RN per enemy death

-You must consume 24 RN in two-enemy RNG methods.
-You must consume 25 RN in one-enemy RNG methods.
-You must consume 23 RN in three-enemy RNG methods.


Basic two-enemy RNG method template:

Attack Psynergy:  4 RN  *or*  Group Healing Psynergy:  8 RN
Attack Psynergy:  4 RN        Group Healing Psynergy:  8 RN
Attack Psynergy:  4 RN        Group Healing Psynergy:  8 RN
Attack Psynergy:  4 RN        -----------------------------
                                                      24 RN
Attack Psynergy:  4 RN
Attack Psynergy:  4 RN
----------------------
                 24 RN

Basic one-enemy RNG method template:

Attack Psynergy:         2 RN  *or*  Group Healing Psynergy:  8 RN
Support Psynergy:        1 RN        Group Healing Psynergy:  8 RN
Group Healing Psynergy:  8 RN        Group Healing Psynergy:  8 RN
Group Healing Psynergy:  8 RN        Single Support Psynergy: 1 RN
                                     -----------------------------
Attack Psynergy:         2 RN                                25 RN
Group Support Psynergy:  4 RN
-----------------------------
                        25 RN

Basic three-enemy RNG method template:

3-target Status Psynergy: 3 RN
3-target Attack Psynergy: 6 RN
3-target Attack Psynergy: 6 RN
Group Healing Psynergy:   8 RN
------------------------------
                         23 RN


That concludes the "Making your own RNG methods" lessons. The rest of this FAQ
will focus on items that you can use RNG methods to get, and troubleshooting
any problems with RNG methods that you may have.



===============================================================================
4)Mentionable Item Drops - 040
===============================================================================


Now you know how to use RNG methods to get items that would normally be
extremely difficult to obtain. Here are several lists with rare items you can
use RNG methods to get, as well as the monster that drops the item and where
that monster is located. I even organized them by item type and arranged them
in alphabetical order. In the next section, I'll include more info on the item,
and even provide you with a premade RNG method for each of them. Aren't I nice?

Quite a few of the monster ICCs are missing from this chart. The ones I have
now were all provided by Terence. I am in the process of testing and
experimenting to fill in the empty spaces. They will be updated in the next
versions of this FAQ.


***Note the difference between "Islet Cave" and "Inner Islet Cave". Islet Cave
is the immediate area you have access to when you enter the cave. Inner Islet
Cave refers to the long corridors you can only reach by Teleporting to the
northern part of the cave.***


***Also, note that to gain access to Anemos Inner Sanctum, you must have
transferred your party from Golden Sun, gotten ALL 28 Djinn in that game, and
ALL 44 Djinn in this game. You must have every single Djinn from both games to
enter.***



---------
-Weapons-
---------

 Item               Enemy           Location               Weakness  Rarity
+------------------+---------------+----------------------+---------+-------+
| Atropos' Rod     | Fire Dragon   | Yampi Desert Cave    | Mercury | ICC 8 |
| Blessed Mace     | Turtle Dragon | Western Sea          | Mars    |       |
| Clotho's Distaff | Minos Warrior | Mars Lighthouse      | Jupiter | ICC 7 |
| Giant Axe        | Earth Golem   | Treasure Isle        | Jupiter |       |
| Lachesis' Rule   | Mad Demon     | Anemos Inner Sanctum | Jupiter | ICC 9 |
| Tartarus Axe     | Minotaurus    | Ankohl Ruins         | Jupiter |       |
| Tisiphone Edge   | Cruel Dragon  | Inner Islet Cave     | Mars    | ICC 9 |
| Rising Mace      | Blue Dragon   | Jupiter Lighthouse   | Mars    |       |
| Rune Blade       | Lesser Demon  | Magma Rock           | Jupiter |       |
| Staff of Anubis  | Red Demon     | Gagomba Statue       | Jupiter |       |
+------------------+---------------+----------------------+---------+-------+


-------
-Armor-
-------

 Item               Enemy           Location               Weakness  Rarity
+------------------+---------------+----------------------+---------+-------+
| Aeolian Cassock  | Wyvern        | Jupiter Lighthouse   | Jupiter |       |
| Aura Gloves      | Magicore      | Islet Cave           | Mercury |       |
| Berserker Band   | Druj          | Inner Islet Cave     | Mars    | ICC 8 |
| Feathered Robe   | Wild Gryphon  | Shaman Village Cave  | Jupiter |       |
| Gloria Helm      | Aka Manah     | Mars Lighthouse      | Mars    | ICC 8 |
| Healing Ring     | Nightmare     | Shaman Village Cave  | Venus   |       |
| Hitoko Mask      | Little Death  | Magma Rock           | Jupiter |       |
| Otafuku Mask     | Gressil       | Gaia Rock            | Jupiter |       |
| Prophet's Hat    | Dread Hound   | Gaia Rock            | Mercury |       |
| Riot Golves      | Minos Knight  | Yampi Desert Cave    | Jupiter | ICC 8 |
| Triton's Ward    | Ocean Dragon  | Treasure Isle        | Mars    |       |
| Unicorn Ring     | Sea Dragons   | Aqua Rock            | Mars    |       |
+------------------+---------------+----------------------+---------+-------+


----------------
-Forgable Items-
----------------

 Item               Enemy           Location               Weakness  Rarity
+------------------+---------------+----------------------+---------+-------+
| Dark Matter      | Wonder Bird   | Inner Islet Cave     | Mercury | ICC 8 |
| Dragon Skin      | Winged Lizard | Yampi Desert Cave    | Jupiter | ICC 7 |
| Golem Core       | Bombander     | Anemos Inner Sanctum | Mercury | ICC 7 |
| Mythril Silver   | Soul Army     | Yampi Desert Cave    | Jupiter | ICC 8 |
| Orihalcon        | Sky Dragon    | Anemos Inner Sanctum | Jupiter |       |
| Salamander Tail  | Pyrodra       | Treasure Isle        | Mars    |       |
| Stardust         | Sand Scorpion | Yampi Desert Cave    | Mars    | ICC 7 |
| Sylph Feather    | Great Seagull | Treasure Isle        | Jupiter |       |
| Tear Stone       | Gillman Lord  | Treasure Isle        | Mars    |       |
+------------------+---------------+----------------------+---------+-------+


--------------------
-Rare Healing Items-
--------------------

 Item               Enemy           Location               Weakness  Rarity
+------------------+---------------+----------------------+---------+-------+
| Mist Potion      | Grand Chimera | Magma Rock           | Mercury |       |
|                  | Macetail      | Jupiter Lighthouse   | Mercury |       |
| Psy Crystal      | Grave Wight   | Anemos Inner Sanctum | Jupiter | ICC 6 |
|                  | Wise Gryphon  | Magma Rock           | Jupiter |       |
|                  | Lich          | Magma Rock           | Jupiter |       |
| Water of Life    | Fire Bird     | Mars Lighthouse      | Mercury | ICC 7 |
|                  | Chimera Worm  | Inner Islet Cave     | Mars    | ICC 6 |
|                  | Living Armor  | Ankohl Ruins         | Jupiter |       |
|                  | Pheonix       | Magma Rock           | Mercury |       |
+------------------+---------------+----------------------+---------+-------+


If you know of anything rare you feel should be included in this list, send me
an e-mail. My address is at the top of this FAQ.




===============================================================================
5)Premade RNG methods - 050
===============================================================================


Now you have the knowledge you need to make your own RNG methods and a complete
list of rare and powerful items to use the methods to obtain. What more could
you want?

I know for a fact that there are many lazy people out there who don't feel like
learning how to make their own RNG methods. Lucky for you, I have gone through
and listed RNG methods for each of the rare items listed above. Don't start
thinking it was for you lazy people either; I'm only doing it for the sake of
completeness. You just happen to be in the right place at the right time. Get
over it.

All of the following RNG methods were done with level 50 characters that all
have nine Djinn of their respective elements all set. If you have some sort of
Agility-enhancing equipment that messes up the attack order of the RNG method,
remove it. 

All premade RNG methods will not work for everyone, however. The equipment,
levels, and classes vary from player to player. The rule of thumb in premade
RNG methods is to adjust to your specific situation:

-Do the enemies die too quickly? Use weaker Psynergies.
-Does the Djinni unleash not kill the enemy? Then use stronger Psynergies. Try
 killing it with a different Djinni of its elemental weakness.

With that said, don't e-mail me saying that so-and-so RNG method didn't work
"for you", because I will immediately delete your e-mail and not reply.

Before you go and e-mail me with other problems you may have, check the
Frequently Asked Questions and Troubleshooting sections at the end of this FAQ.
Anyway, make sure all of the following happens in the RNG method:



-HARD RESET!
-Find the enemy formation specified.
-The game text will say "Felix's party attacks first!"
-Do exactly as the method states
-All Psynergy targets item-dropping enemy unless otherwise specified. 
-The enemy should FLASH COLORS AND DIE as a result of the Djinni unleash.
-Afer Djinni unleash, kill off other enemy ANY way you want.
-Item dropped.



+---------------+
| Weapons - 051 |
+---------------+


Weapons are nice. The best weapons in this section are Atropos' Rod, Lachesis'
Rule, the Tisiphone Edge, and the Rune Blade.


+--------------------------------+
| Atropos' Rod                   |
|  -Staff                        |
|  -Attack + 169                 |
|  -Unleashes Life Shear         |
+--------------------------------+
| Dropped by: Fire Dragon        |
| Location: Yampi Desert Cave    |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Fire Dragon and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Cycle Beam!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba casts High Impact!
Jenna casts Flare Wall!
Felix defends
Piers unleashes Sour!

Fire Dragon flashes and dies.
Kill other enemy in any way.


+--------------------------------+
| Blessed Mace                   |
|  -Mace                         |
|  -Attack + 126                 |
|  -HP recovery + 2              |
|  -Use to recover 200 HP        |
+--------------------------------+
| Dropped by: Turtle Dragon      |
| Location: Western Sea          |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Turtle Dragon and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Flare Wall!
Felix casts Clay Spire!
Piers casts Tundra!

TURN 2
Sheba casts Whirlwind!
Jenna unleashes Torch!

Turtle Dragon flashes and dies.
Kill other enemy in any way.


+--------------------------------+
| Clotho's Distaff               |
|  -Staff                        |
|  -Attack + 168                 |
|  -Use to recover 1000 HP       |
+--------------------------------+
| Dropped by: Minos Warrior      |
| Location: Mars Lighthouse      |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Minos Warrior and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Aura!
Felix casts Stone Spire!
Piers casts Glacier!

TURN 2
Sheba unleashes Squall!

Minos Warrior flashes and dies.
Kill other enemy in any way.


+--------------------------------+
| Giant Axe                      |
|  -Axe                          |
|  -Attack + 114                 |
|  -Unleashes Meltdown           |
+--------------------------------+
| Dropped by: Earth Golem        |
| Location: Treasure Isle        |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter an Earth Golem and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Stone Spire!
Piers casts Glacier!

TURN 2
Sheba unleashes Gust!

Earth Golem flashes and dies.
Kill other enemy in any way.


+--------------------------------+
| Lachesis' Rule                 |
|  -Staff                        |
|  -Attack + 177                 |
|  -Unleashes Apocalypse         |
+--------------------------------+
| Dropped by: Mad Demon          |
| Location: Anemos Inner Sanctum |
+--------------------------------+

Attack Order: Sheba, Ivan, Jenna, Mia.
Encounter a Mad Demon and one other enemy.

TURN 1
Sheba casts Spark Plasma!
Ivan casts Spark Plasma!
Jenna casts Searing Beam!
Mia casts Wish!

TURN 2
Sheba casts Destruct Ray!
Ivan unleashes Squall!

Mad Demon flashes and dies.
Kill other enemy in any way.


+--------------------------------+
| Tartarus Axe                   |
|  -Axe                          |
|  -Attack + 127                 |
|  -Unleashes Vein Tap           |
+--------------------------------+
| Dropped by: Minotaurus         |
| Location: Ankohl Ruins         |
+--------------------------------+

Attack Order: Jenna, Sheba, Felix, Mia.
Encounter a Minotaurus and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Aura!
Felix casts Clay Spire!
Mia casts Wish!

TURN 2
Sheba unleashes Squall!

Minotaurus flashes and dies.
Kill other enemy in any way.


+--------------------------------+
| Tisiphone Edge                 |
|  -Light Blade                  |
|  -Attack + 178                 |
|  -Unleashes Vengeance          |
+--------------------------------+
| Dropped by: Cruel Dragon       |
| Location: Inner Islet Cave     |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Cruel Dragon and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Aura!
Felix casts Mother Gaia! ***(Felix casts Spire if Wonder Bird is present)***
Piers casts Glacier!

TURN 2
Sheba casts Plasma!
Jenna unleashes Torch!

Cruel Dragon flashes and dies.
Kill other enemy any way you like.

+--------------------------------+
| Rising Mace                    |
|  -Mace                         |
|  -Attack + 152                 |
|  -Unleashes High Vitals        |
+--------------------------------+
| Dropped by: Blue Dragon        |
| Location: Jupiter Lighthouse   |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Blue Dragon and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba casts High Impact!
Jenna unleashes Core!

Blue Dragon flashes and dies.
Kill other enemy any way you like.


+--------------------------------+
| Rune Blade                     |
|  -Long Sword                   |
|  -Attack + 162                 |
|  -Unleashes Void Beam          |
+--------------------------------+
| Dropped by: Lesser Demon       |
| Location: Magma Rock           |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Lesser Demon and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba unleashes Squall!

Lesser Demon flashes and dies.
Kill other enemy any way you like.


+--------------------------------+
| Staff of Anubis                |
|  -Staff                        |
|  -Attack + 83                  |
|  -Unleashes Sarcophagus        |
+--------------------------------+
| Dropped by: Red Demon          |
| Location: Gagomba Statue       |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Mia.
Encounter a Red Demon and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Gaia!
Mia casts Wish!

TURN 2
Sheba unleashes Gale!

Red Demon flashes and dies.
Kill other enemy any way you want.


+-------------+
| Armor - 052 |
+-------------+


A lot of this stuff becomes useless as you get farther into the game, like the
masks and the rings, but there's also some great defensive equipment here. The
best armor in this section are the Feathered Robe, Riot Gloves, and Triton's
Ward.


+--------------------------------+
| Aeolian Cassock                |
|  -Robe                         |
|  -Defense + 46                 |
|  -Wind Power + 15              |
|  -Wind Resist + 50             |
+--------------------------------+
| Dropped by: Wyvern             |
| Location: Jupiter Lighthouse   |
+--------------------------------+

Attack Order: Sheba, Jenna Felix, Mia.
Encounter a Wyvern and one other enemy.

TURN 1
Sheba casts Tornado!
Jenna casts Aura!
Felix casts Mother Gaia!
Mia casts Wish!

TURN 2
Sheba unleashes Whorl!

Wyvern flashes and dies.
Kill other enemy any way you want.


+--------------------------------+
| Aura Gloves                    |
|  -Gloves                       |
|  -Defense + 36                 |
|  -Use to increase Resistance.  |
+--------------------------------+
| Dropped by: Magicore           |
| Location: Islet Cave           |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Magicore and one other enemy.

TURN 1
Sheba casts Ray!
Jenna casts Flare Wall!
Felix casts Gaia!
Piers casts Tundra!

TURN 2
Sheba casts Whirlwind!
Jenna casts Flare!
Felix defends!
Piers unleashes Gel!

Magicore flashes and dies.


+--------------------------------+
| Berserker Band                 |
|  -Circlet                      |
|  -Attack + 15                  |
|  -Defense + 46                 |
+--------------------------------+
| Dropped by: Druj               |
| Location: Inner Islet Cave     |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Druj and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Aura!
Felix casts Grand Gaia! ***(Felix Spire if Wonder Bird is present)***
Piers casts Supercool!

TURN 2
Sheba casts Plasma!
Jenna unleashes Torch!

Druj flashes and dies.


+--------------------------------+
| Feathered Robe                 |
|  -Robe                         |
|  -Defense + 45                 |
|  -Wind Power + 20              |
|  -Wind Resist + 30             |
|  -Agility + 30                 |
+--------------------------------+
| Dropped by: Wild Gryphon       |
| Location: Shaman Village Cave  |
+--------------------------------+

Attack Order: Sheba, Ivan, Jenna, Mia.
Encounter a Wild Gryphon by itself.

TURN 1
Sheba casts Storm Ray!
Ivan casts Storm Ray!
Jenna casts Aura!
Mia casts Wish!

TURN 2
Sheba casts Impact (on Ivan)!
Ivan unleashes Squall!


Wild Gryphon flashes and dies.


+--------------------------------+
| Gloria Helm                    |
|  -Helm                         |
|  -Defense + 49                 |
|  -HP recovery + 10             |
+--------------------------------+
| Dropped by: Aka Manah          |
| Location: Mars Lighthouse      |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter an Aka Manah and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Tundra!

TURN 2
Sheba casts Plasma!
Jenna unleashes Torch!

Aka Manah flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Healing Ring                   |
|  -Use to recover 70 HP.        |
+--------------------------------+
| Dropped by: Nightmare          |
| Location: Shaman Village Cave  |
+--------------------------------+

Attack Order: 
Encounter a Nightmare and one other enemy.

TURN 1
Sheba casts Ray!
Jenna casts Flare!
Felix casts Quake!
Piers casts Cool!

TURN 2
Sheba casts Whirlwind!
Jenna casts Beam!
Felix unleashes Echo!


Nightmare flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Hitoko Mask                    |
|  -Defense + 33                 |
|  -Use to release Fire Breath.  |
|  -Only equippable by men.      |
+--------------------------------+
| Dropped by: Little Death       |
| Location: Magma Rock           |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Little Death and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Tundra!

TURN 2
Sheba unleashes Gale!


Little Death flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Otafuku Mask                   |
|  -Defense + 31                 |
|  -Use to release Water Breath. |
|  -Only equippable by women.    |
+--------------------------------+
| Dropped by: Gressil            |
| Location: Gaia Rock            |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Gressil and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Gaia!
Piers casts Cool!

TURN 2
Sheba unleashes Squall!


Gressil flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Prophet's Hat                  |
|  -Defense + 30                 |
|  -Use to cast Curse.           |
+--------------------------------+
| Dropped by: Dread Hound        |
| Location: Gaia Rock            |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Dread Hound and one other enemy.

TURN 1
Sheba casts Ray!
Jenna casts Flare Wall!
Felix casts Earthquake!
Piers casts Frost!

TURN 2
Sheba defends.
Jenna casts Flare!
Felix defends.
Piers unleashes Sour!

Dread Hound flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Riot Gloves                    |
|  -Gloves                       |
|  -Attack + 15                  |
|  -Defense + 45                 |
|  -Increases criticals (+20%)   |
+--------------------------------+
| Dropped by: Minos Knight       |
| Location: Yampi Desert Cave    |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Minos Knight and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba unleashes Squall!

Minos Knight flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Triton's Ward                  |
|  -Clothes                      |
|  -Defense + 47                 |
|  -Water Power + 30             |
|  -Water Resist + 70            |
+--------------------------------+
| Dropped by: Ocean Dragon       |
| Location: Treasure Isle        |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Ocean Dragon and one other enemy.

TURN 1
Sheba casts Tornado!
Jenna casts Aura!
Felix casts Stone Spire!
Piers casts Supercool!

TURN 2
Sheba casts High Impact!
Jenna unleashes Core!

Ocean Dragon flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Unicorn Ring                   |
|  -Use to remove poison.        |
+--------------------------------+
| Dropped by: Sea Dragon         |
| Location: Aqua Rock            |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Sea Dragon and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Beam!
Felix casts Clay Spire!
Piers casts Tundra!

TURN 2
Sheba casts High Impact!
Jenna unleashes Core!

Sea Dragon flashes and dies.
Kill the other enemy any way you want.


+----------------------+
| Forgable Items - 053 |
+----------------------+


These are all forgable items that you can take to Sunshine the blacksmith in
Yallam, a town in northeast Ocenia (the continent closest to Tundaria). You can
access the town before aquiring the flying ship through a delta in southeast
Ocenia and taking the river north until you are stopped by a bridge. Yallam is
directly north of this bridge.

None of these items have 'real' stats like equipment does. Instead, I have
included the names of all the items you can forge from the material, and your
approximate chances of forging those items, taken from the end of DarthMarth's
excellent GS:TLA walkthrough.


+--------------------------------+
| Dark Matter                    |
|  -Darksword      10%           |
|  -Demon Circlet  15%           |
|  -Fear Helm      20%           |
|  -Stealth Armor  30%           |
|  -Terra Shield   25%           |
+--------------------------------+
| Dropped by: Wonder Bird        |
| Location: Inner Islet Cave     |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter two (2) Wonder Birds.

TURN 1
Sheba casts Storm Ray!
Jenna casts Flare Wall!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba casts High Impact!
Jenna defends!
Felix defends!
Piers unleashes Gel!

Wonder Bird flashes and dies.
Kill the other enemy any way you want.

NOTE: It doesn't matter if the second Wonder Bird revives the first one with
Regen Dance. When the battle is finished, you will get the Dark Matter.


+--------------------------------+
| Dragon Skin                    |
|  -Dragon Boots   15%           |
|  -Dragon Helm    25%           |
|  -Dragon Mail    20%           |
|  -Dragon Robe    15%           |
|  -Dragon Shield  25%           |
+--------------------------------+
| Dropped by: Winged Lizard      |
| Location: Yampi Desert Cave    |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Winged Lizard and one other enemy.

TURN 1
Sheba casts Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Cool!

TURN 2
Sheba unleashes Squall!

Winged Lizard flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Golem Core                     |
|  -Chronos Mail   30%           |
|  -Gaia's Axe     15%           |
|  -Huge Sword     15%           |
|  -Titan Gloves   25%           |
|  -Tungsten Mace  15%           |
+--------------------------------+
| Dropped by: Bombander          |
9/11/03 19:56:58| Location: Anemos Inner Sanctum |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Bombander and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Flare Storm!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba casts High Impact!
Jenna defends!
Felix defends!
Piers unleashes Mist!

Bombander flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Mythril Silver                 |
|  -Levatine         10%         |
|  -Mythril Armlet   20%         |
|  -Mythril Blade    20%         |
|  -Mythril Clothes  20%         |
|  -Mythril Helm     15%         |
|  -Psychic Circlet  15%         |
+--------------------------------+
| Dropped by: Soul Army          |
| Location: Yampi Desert Cave    |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter three (3) Soul Armies.

TURN 1
Sheba casts Sleep! (target middle)
Jenna casts Aura!
Felix casts Mother Gaia! (target left)
Piers casts Supercool! (target right)

TURN 2
Sheba unleashes Squall! (target middle)

Soul Army flashes and dies.
Kill the other enemies any way you want.


+--------------------------------+
| Orihalcon                      |
|  -Big Bang Gloves  15%         |
|  -Cosmos Shield    15%         |
|  -Excalibur         5%         |
|  -Millenium Helm   20%         |
|  -Nebula Wand      15%         |
|  -Stellar Axe      10%         |
|  -Xylion Armor     20%         |
+--------------------------------+
| Dropped by: Sky Dragon         |
| Locaiton: Anemos Inner Sanctum |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Sky Dragon and one other enemy.

TURN 1
Sheba casts Spark Plasma!
Jenna casts Aura!
Felix casts Grand Gaia!
Piers casts Megacool!

TURN 2
Sheba unleashes Squall!

Sky Dragon flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Salamander Tail                |
|  -Apollo's Axe    15%          |
|  -Ardagh Robe     25%          |
|  -Burning Sword   15%          |
|  -Flame Shield    25%          |
|  -Salamander Rod  20%          |
+--------------------------------+
| Dropped by: Pyrodra            |
| Location: Treasure Isle        |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Pyrodra and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Flare Wall!
Felix casts Earthquake!
Piers casts Tundra!

TURN 2
Sheba casts High Impact!
Jenna unleashes Core!

Pyrodra flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Stardust                       |
|  -Astral Circlet  20%          |
|  -Comet Mace      20%          |
|  -Luna Shield     20%          |
|  -Planet Armor    20%          |
|  -Stardust Ring   20%          |
+--------------------------------+
| Dropped by: Sand Scorpion      |
| Location: Yampi Desert Cave    |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Sand Scorpion and one other enemy.

TURN 1
Sheba casts Ray!
Jenna casts Flare!
Felix casts Earthquake!
Piers casts Cool!

TURN 2
Sheba casts Whirlwind!
Jenna unleashes Core!

Sand Scorpion flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Sylph Feather                  |
|  -Aerial Gloves  25%           |
|  -Faery Vest     25%           |
|  -Floating Hat   25%           |
|  -Slyph Rapier   25%           |
+--------------------------------+
| Dropped by: Great Seagull      |
| Location: Treasure Isle        |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Great Seagull and one other enemy.

TURN 1
Sheba casts Plasma!
Jenna casts Aura!
Felix casts Earthquake!
Piers casts Tundra!

TURN 2
Sheba unleashes Squall!

Great Seagull flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Tear Stone                     |
|  -Clear Bracelet  30%          |
|  -Cloud Wand      25%          |
|  -Pure Circlet    25%          |
|  -Spirit Ring     20%          |
+--------------------------------+
| Dropped by: Gillman Lord       |
| Location: Treasure Isle        |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Gillman Lord and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Flare Wall!
Felix casts Clay Spire!
Piers casts Glacier!

TURN 2
Sheba casts High Impact!
Jenna unleashes Torch!

Gillman Lord flashes and dies.
Kill the other enemy any way you want.


+--------------------------+
| Rare Healing Items - 054 |
+--------------------------+


Rare healing items are dropped by many different enemies. I've included one RNG
method for each enemy that drops a specific item. Mist Potions are the only
ones that can be bought in shops infinitely. Some of the shops in towns later
on in the game also sell Psy Crystals and Waters of Life, but they only have
one of each in stock, and you can't buy more after that.

If you know of any enemies not listed here that drop the following items, send
me an e-mail. My address is at the top of this FAQ.


+--------------------------------+
| Mist Potion                    |
|  -Party recovers 300 HP.       |
+--------------------------------+
| Dropped by: Grand Chimera      |
| Location: Magma Rock           |
+--------------------------------+
| Dropped by: Macetail           |
| Location: Jupiter Lighthouse   |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Grand Chimera and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Cycle Beam!
Felix casts Earthquake!
Piers casts Tundra!

TURN 2
Sheba casts High Impact!
Jenna defends.
Felix defends.
Piers unleashes Gel!

Grand Chimera flashes and dies.
Kill the other enemy any way you want.



Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Macetail and one other enemy.

Sheba casts Storm Ray!
Jenna casts Cycle Beam!
Felix casts Earthquake!
Piers casts Cool!

TURN 2
Sheba casts High Impact!
Jenna defends.
Felix defends.
Piers casts Sour!

Macetail flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Psy Crystal                    |
|  -Replentishes all PP.         |
+--------------------------------+
| Dropped by: Grave Wight        |
| Location: Anemos Inner Sanctum |
+--------------------------------|
| Dropped by: Lich               |
| Location: Magma Rock           |
+--------------------------------+
| Dropped by: Wise Gryphon       |
| Location: Magma Rock           |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Grave Wight and one other enemy.

TURN 1
Sheba casts Shine Plasma!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Tundra!

TURN 2
Sheba unleashes Squall!


Grave Wight flashes and dies.
Kill the other enemy any way you want.



Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Lich and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Earthquake!
Piers casts Glacier!

TURN 2
Sheba unleashes Gale!

Lich flashes and dies.
Kill the other enemy any way you want.



Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Wise Gryphon and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Cool!

TURN 2
Sheba unleashes Squall!

Wise Gryphon flashes and dies.
Kill the other enemy any way you want.


+--------------------------------+
| Water of Life                  |
|  -Revives downed characters.   |
+--------------------------------+
| Dropped by: Chimera Worm       |
| Location: Inner Islet Cave     |
+--------------------------------+
| Dropped by: Fire Bird          |
| Location: Mars Lighthouse      |
+--------------------------------+
| Dropped by: Living Armor       |
| Location: Ankohl Ruins         |
+--------------------------------+
| Dropped by: Pheonix            |
| Location: Magma Rock           |
+--------------------------------+

Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Chimera Worm and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Flare Wall!
Felix casts Gaia! ***(Felix casts Spire if Wonder Bird is present)***
Piers casts Cool!

TURN 2
Sheba casts High Impact!
Jenna unleashes Torch!


Chimera Worm flashes and dies.
Kill the other enemy any way you want.



Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Fire Bird and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Mother Gaia!
Piers casts Tundra!

TURN 2
Sheba casts Impact! ***(Sheba defends if there are two Fire Birds)***
Jenna casts Fume!
Felix defends.
Piers unleashes Gel!


Fire Bird flashes and dies.
Kill the other enemy any way you want.



Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Living Armor and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Mother Gaia!
Piers casts Tundra!

TURN 2
Sheba unleashes Squall!


Living Armor flashes and dies.
Kill the other enemy any way you want.



Attack Order: Sheba, Jenna, Felix, Piers.
Encounter a Pheonix and one other enemy.

TURN 1
Sheba casts Storm Ray!
Jenna casts Aura!
Felix casts Clay Spire!
Piers casts Tundra!

TURN 2
Sheba casts Impact! ***(Sheba defends if there are two Pheonixes)***
Jenna casts Fume!
Felix defends.
Piers unleashes Gel!


Pheonix flashes and dies.
Kill the other enemy any way you want.

-------------------------------------------------------------------------------

That concludes the Premade RNG method section. If you are having trouble with
any of these, take a look at the Frequently Asked Questions and Troubleshooting
sections up ahead.

If the next two sections don't fix the problem, or you have a question that
isn't answered, contact me using the e-mail address at the top of the FAQ.
Remember, proper grammar and spelling make for a faster reply.


===============================================================================
6)Frequently Asked Questions - 060
===============================================================================


This section is for people who have questions regarding RNG methods. Check this
section and the following section before sending me any e-mail.

Q: Can you give me an RNG method for an item using specific levels and classes?
Q: Does all the info in this FAQ apply to the first Golden Sun, too?
Q: Does the order that the characters appear in and/or attack in matter?
Q: Does having HP or PP recovery equipment on mess up RNG methods?
Q: Does the Djinni you use to finish off the enemy affect the RNG method?
Q: What does making a character defend do?
Q: How does Luck affect RNGs?
Q: Does it matter which enemy is the main target of Psynergy in RNG methods?
Q: Is the enemy allowed to attack during the method?
Q: Is it possible to get two items in one RNG method?



-------------------------------------------------------------------------------
Q: Can you give me an RNG method for an item using specific levels and classes?
-------------------------------------------------------------------------------

A: No. The only RNG methods you get are in the previous section. Adapt to them
   or don't use them. It's always best to make your own.


-------------------------------------------------------------------------------
Q: Does all the info in this FAQ apply to the first Golden Sun, too?
-------------------------------------------------------------------------------

A: All the info as far as the "Battle RNG" goes. The only thing that changed is
   the "General RNG", affecting the way you encounter monsters after a hard
   reset. As far as the RNG methods themselves go, it's all exactly the same.


-------------------------------------------------------------------------------
Q: Does the order that the characters appear in and/or attack in matter?
-------------------------------------------------------------------------------


A: NO. The order that characters appear in and attack in has absolutely NO
   effect on RNG methods. The myth that the person who is unleashing the Djinni
   must act third in the second turn is COMPLETELY FALSE.


-------------------------------------------------------------------------------
Q: Does having HP or PP recovery equipment on mess up RNG methods?
-------------------------------------------------------------------------------

A: No. Even if someone recovers HP or PP at the end of a turn, nothing changes.


-------------------------------------------------------------------------------
Q: Does the Djinni you use to finish off the enemy affect the RNG method?
-------------------------------------------------------------------------------

A: No. As long as you use a Djinni of the element the enemy is weak against,
   the RNG method remains the same. For example, let's say the enemy is weak
   against Fire. No matter which Mars Djinni I use to kill the enemy (Torch,
   Char, Cannon, Core, etc.) I will still get the item.


-------------------------------------------------------------------------------
Q: What does making a character defend do?
-------------------------------------------------------------------------------

A: Absolutely nothing. A character defending consumes 0 RN, so it's an
   effective way of skipping someone's turn should you not need them to act.


-------------------------------------------------------------------------------
Q: How does Luck affect RNGs?
-------------------------------------------------------------------------------

A: Luck really doesn't affect RNG methods. Luck affects both your characters'
   and the enemy monsters' chances of being struck with negative status
   ailments, such as Sleep, Stun, and Poison. Status Psynergies that inflict
   such ailments consume the same amount of RN whether the enemy is affected by
   it or not, so the enemies' Luck doesn't matter.

   Luck does NOT increase your chances of making a monster flash using the DP
   method. It also has NO effect on which items are forged from the blacksmith
   or the unleash ratio of certain weapons (Excalibur, Tisiphone Edge, etc.).
   Just thought I'd clear up that rumor.

-------------------------------------------------------------------------------
Q: Does it matter which enemy is the main target of Psynergy in RNG methods?
-------------------------------------------------------------------------------

A: It could. The premade RNG methods in the previous section were designed in a
   way that the Psynergies will weaken the enemy for the Djinni unleash, which
   MUST kill it. None of that has any effect on how many RNs are consumed,
   however. All Psynergy consumes the same amount of RN regardless of who is
   targeted.

   In three-enemy RNG methods, the enemy targeted could affect how many of the
   enemies are hit with the Psynergy, thus changing how many RNs the Psynergy
   consumes. Check the Three-enemy RNG method section for greater detail on the
   subject.


-------------------------------------------------------------------------------
Q: Is the enemy allowed to attack during the method?
-------------------------------------------------------------------------------

A: During the method, no. However, once you have unleashed the weakness Djinni
   and the monster flashes and dies, the rest of the battle doesn't matter. You
   can kill the other monster any way you want, and the monster can even attack
   you.


-------------------------------------------------------------------------------
Q: Is it possible to get two items in one RNG method?
-------------------------------------------------------------------------------

A: It is very possible. Remember how monsters have ICCs? Work the RNG method so
   that both monsters die (by Djinni Kill) on RNs that correspond to their ICC
   so that both items drop. Just know that you can't get the SAME item twice in
   one RNG method, but you can get two different items. An example:


  Attack Order: Sheba, Jenna, Felix, Garet. All base classes.
  Encounter one Cruel Dragon and one Druj.

  Cruel Dragon appeared!
  Druj appeared!
  Felix's party attacks first!  [1 RN]

  TURN 1
  Sheba casts Storm Ray!        [4 RN, 5 RN total]
  Jenna casts Cycle Beam!       [4 RN, 9 RN total]
  Felix casts Clay Spire!       [4 RN, 13 RN total]
  Garet casts Eruption!         [4 RN, 17 RN total] 

  Second turn begins            [2 RN, 19 RN total]

  TURN 2
  Sheba casts High Impact!      [4 RN, 23 RN total]
  Jenna unleashes Torch!        [3 RN, 26 RN total]
  You felled Druj!              [1 RN, 27 RN total] <--Druj drops on 27 and 31
  Felix is defending!           [0 RN, 27 RN total]
  Garet unleashes Core!         [3 RN, 30 RN total]
  You felled Cruel Dragon!      [1 RN, 31 RN total] <--Cruel Dragon drops on 31


   In this RNG method you get both the Beserker Band and the Tisiphone Edge. As
   long as you know the ICCs of the monsters you are dealing with and which RNs
   their items drop on, you will be able to get two items in one RNG method.


-------------------------------------------------------------------------------

If you have any questions that aren't answered here, contact me by e-mail. My
address is at the top of this FAQ. Remember, grammar and punctuation make for a
faster reply.




===============================================================================
7)Troubleshooting - 070
===============================================================================

The RNG method won't work, but I do everything right.
Monsters always attack before the Djinni unleash.
The monster won't flash when the Djinni kills it.
The monster always appears with a weak monster that dies with a few Psynergies.

-------------------------------------------------------------------------------
The RNG method won't work, but I do everything right.
-------------------------------------------------------------------------------

There's a vague question. Here's some things that might make the RNG method go
bad:

1)Are any of the characters involved in the battle affected by status ailments?
  Ailments will ruin an RNG method *if* they take effect.

    -Remove Haunt with the Djinn Salt or Tonic or by visiting a sanctum. 

    -Give Cursed characters the Cleric's Ring. Lacking that, take them to a
     sanctum and get it removed. DON'T put the cursed item back on.

    -Remove Poison and Venom with Cure Poison or an Antidote.


2)Are you certain that you counted the RNs correctly?
   -Try the method again, taking care to count all RNs.

3)Are Pheonixes, Fire Birds, or Wonder Birds involved?

   -Remember that they consume more RN at the start of the second turn than
    normal enemies. Count the RNs again.

   -Find other enemy formations that don't involve them.


-------------------------------------------------------------------------------
Monsters always attack before the Djinni unleash.
-------------------------------------------------------------------------------

If monsters attack before the Djinni unleash, then you just need some more
Agility. Go to the slot machines in Contigo and use your Game Tickets to win
some Quick Boots (Agility + 20) and some Running Shirts (Agility + 15). Equip
everyone on your team with those. Use the Golden Boots (Agility +30) if you
have them.

Some armor also increases Agility. The Ninja Garb, Aerial Gloves, and the
Feathered Robe (Agility + 30), the Wild Coat (Agility + 40), and the Elven
Shirt (Agility x 1.5) are great Agility enhancers. As a last resort, you could
change your characters to faster classes, or just level up.


-------------------------------------------------------------------------------
The monster won't flash when the Djinni kills it.
-------------------------------------------------------------------------------

There are two reasons why this would happen. The first and most obvious one is
that the Djinni used to kill the enemy isn't of the element the enemy is weak
against. When you unleash the Djinni, the punctuation is important:

Garet unleashes Fever!
Cruel Dragon takes 432 damage!!! <--Three exclamation points = Weak to element.

Felix unleashes Echo!
Cruel Dragon takes 369 damage!   <---One exclamation point = Neutral.

Mia unleashes Fog!
Cruel Dragon takes 290 damage.   <---A period = Resistant to element.

You can tell if a Djinni is of the element that the monster is weak against if
you see three exclamation points at the end of the sentence in which the enemy
took damage.


There is one other possible reason that the Djinni wouldn't kill the enemy,
even if it is of the monster's weakness. Your corresponding elemental power is
also taken into account. Your elemental power must be greater than the
monster's resistance by a certain amount to make enemies flash using the DP
method. When killing the monster on RN 31 with the DP method, there has to be a
difference of at least 38 between the unleasher's Power (of the Djinni's
element) and the enemy's Resistance.

For example, a Cruel Dragon has a Fire Resistance of 25. That means whoever is
going to unleash the Mars Djinni that kills the Cruel Dragon must have a Fire
Power of at least 63. Not very difficult. However, some monsters have higher
resistances to their weakness element, and that may give you some trouble in
making it flash. Mad Demons are notable examples of this.

To fix this, give the person who is unleashing more Djinn of the correct
element, or equip him or her with Power-boosting equipment like the Feathered
Robe, Aerial Gloves, Pure Circlet, or Big Bang Gloves.


-------------------------------------------------------------------------------
The monster always appears with a weak monster that dies with a few Psynergies.
-------------------------------------------------------------------------------

The easiest way to avoid this problem is to just keep hard resetting until you
find the monster whose item you want with a stronger monster. If you find two
of the same monster you won't have to worry about this since they have the same
stats.

Another way is to just use strong Psynergy and *force* the weak monster to die
in the FIRST turn. If you know how to count RNs, you can make up for the early
death in the second turn and the method will still work.


-------------------------------------------------------------------------------


If your RNG methods aren't working for reasons not listed here, send me an
e-mail. My address is at the top of the FAQ. Remember, proper grammar and
punctuation make for a faster reply (I bet you're tired of hearing that).




===============================================================================
8) Credits - 080
===============================================================================


There is no way in hell that I could have done any of this alone. The
information in this FAQ is the work of many people (myself included) working
together for a greater cause. These are the people who provided the most
information in this FAQ:


Terence - The creator of RNG methods. Most of the info in this FAQ can be
          credited to him. He hacked into the game and discovered the RN values
          of different Psynergies and the RNs on which items would drop. He
          found that enemies have different chances of dropping items, which he
          dubbed Item Chance Class, or ICC for short. He then shared this
          information with us and showed us how to use it in "RNG methods".
          During the making of this FAQ, he also set me straight on how ICC
          works in RNG methods. He provided a list of the first 40 RNs and
          their respective ICCs, and even gave a list of some monster ICCs
          (that I used). Thanks for everything!

Rena Chan - Introduced us to Sleep, the first Psynergy known capable of
            consuming odd amounts of RN, making one-enemy and three-enemy RNG
            methods a reality, as well as making it possible to experiment with
            the RN values of other stuff. She was the first to sort Psynergies
            into well-defined categories, as well as the catetgories of unknown
            Psynergy, like Break.

TheScythe - Provided the accurate RN values for the many different types of
            Djinn, as well as each of the 72 Djinn in list form. He also
            exlained how the Elemental Bonus works and the effect that
            different classes have on it. He found the Power/Resist difference
            between the unleasher and the monster required for the enemy to
            flash.



There are many people who helped out with testing and experimenting (and
theories, problems, questions, and speculation) in the RNG topic where we
posted our research. Their help is very much appreciated:

Yadotian Spy
azngameplayer
aznweirdo718
Azure Dragoon
Dragon Mouse
nick1presta
neo3333
celestialwrath
montypylon10189
CobraGT
tothethirdpower
chumpa g
RavBolt
AncientMagus 
Encapturer
chaoticcranium
darkmage507


Others who provided information in this FAQ:

Darthmarth - Some of the stats for items in the Premade RNG method section and
             the percentages for the forgable items were taken from the end of
             his GS:TLA walkthrough.


Last but certainly not least, let's not forget:

CJayC - For the disclaimer, as well as putting this guide on his great website.

Nintendo/Camelot- For making this great game.




If you think your name deserves to be on this list (or you think you deserve
more credit), contact me by e-mail. My address is at the top of this FAQ.
Proper grammar and punctuation make for a faster reply.




===============================================================================
9)Version History - 090
===============================================================================


Version 0.9 09/14/2003: First posted version. This FAQ has been a long time in
                        the making. There is still some missing information,
                        but nothing imperative.




===============================================================================
10)Legal Stuff - 100
===============================================================================


The ONLY web site that this guide is available on is GameFAQs.com. This may be 
not be reproduced under any circumstances except for personal, private use. It 
may not be placed on any other web site or otherwise distributed publicly
without advance written permission. Use of this guide on any other web site or 
as a part of any public display is strictly prohibited, and a violation of 
copyright.

If you see this guide on any site other than GameFAQs.com, please let me know.
My address it as the top of the FAQ.

All trademarks and copyrights contained in this document are owned by their
respective trademark and copyright holders.


Copyright 2003 Diego Gonzalez. All rights reserved.


Line count: 2,599
Word count: 20,644
Character count: 91,158 (89.0 KB)
Restore Page

