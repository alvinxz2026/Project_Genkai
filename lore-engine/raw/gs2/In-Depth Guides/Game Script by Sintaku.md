---
source_id: sintaku-script
author: Sintaku
url: https://gamefaqs.gamespot.com/gba/561356-golden-sun-the-lost-age/faqs/47032
type: general
covers: [story]
quality: default
summary: 全游戏剧本逐场对白 dump（含 djinn/summon、transfer 触发事件、可选 boss 附录）。非实体提取源。
gs1_counterpart:
notes: 这个纯script，感觉我们用不上
---

# Game Script by Sintaku

## TABLE OF CONTENTS


 [01'00]  Administrative
 [01'01]    Format
 [01'02]    Credits
 [01'03]    Versions
 [01'04]    Legal



 [02'00]  Script
 [02'01]    Prologue

 [02'02]    [Indra]  Daila
 [02'03]    [Indra]  Kandorean Temple
 [02'04]    [Indra]  Shrine of the Sea God
 [02'05]    [Indra]  Daila
 [02'06]    [Indra]  East Indra Shore
 [02'07]    [Indra]  Madra
 [02'08]    [Indra]  Madra Drawbridge

 [02'09]    [Indra / Osenia]  Osenia Cliffs
 [02'10]    [Osenia]  Yampi Desert
 [02'11]    [Osenia]  Alhafra
 [02'12]    [Osenia]  Air's Rock
 [02'13]    [Osenia]  Garoh
 [02'14]    [Osenia]  Mikasalla

 [02'15]    [Indra]  Madra
 [02'16]    [Indra / Gondowan]  Gondowan Cliffs
 [02'17]    [Gondowan]  Naribwe
 [02'18]    [Gondowan]  Kibombo Mountains
 [02'19]    [Gondowan]  Kibombo
 [02'20]    [Gondowan]  Naribwe

 [02'21]    [Indra]  Madra
 [02'22]    [Indra]  East Indra Shore

 [02'23]    [Great Eastern Sea]  Apojii Islands
 [02'24]    [Great Eastern Sea]  Aqua Rock

 [02'25]    [Great Eastern Sea]  Izumo
 [02'26]    [Great Eastern Sea]  Gaia Rock
 [02'27]    [Great Eastern Sea]  Izumo

 [02'28]    [Angara]  Champa
 [02'29]    [Osenia]  Alhafra
 [02'30]    [Angara]  Champa

 [02'31]    [Sea of Time]  Lemuria

 [02'32]    [Osenia]  Yallam
 [02'33]    [Great Eastern Sea]  Isles
 [02'34]    [Great Western Sea]  Isles

 [02'35]    [Hesperia]  Hesperia Settlement
 [02'36]    [Hesperia]  Shaman Village

 [02'37]    [Atteka]  Atteka Inlet
 [02'38]    [Atteka]  Contigo
 [02'39]    [Atteka]  Jupiter Lighthouse
 [02'40]    [Atteka]  Contigo
 [02'41]    [Atteka]  Atteka Inlet
 [02'42]    [Atteka]  Contigo

 [02'43]    [Gondowan]  Gondowan Settlement
 [02'44]    [Gondowan]  Magma Rock
 [02'45]    [Angara]  Loho

 [02'46]    [Great Western Sea]  Northern Reaches
 [02'47]    [Northern Reaches]  Prox
 [02'48]    [Northern Reaches]  Mars Lighthouse
 [02'49]    [Northern Reaches]  Prox
 [02'50]    Epilogue



 [03'00]  Addenda
 [03'01]    Djinn & Summons
 [03'02]    Transfer-prompted Events
 [03'03]    Naribwe Fortuneteller
 [03'04]    Optional Bosses
 [03'05]    Link Lobby

---

END OF TABLE OF CONTENTS

---
                           Golden Sun: The Lost Age

                           Game Script (US, English)

Author    : mtkennerly (formerly known as TheSinnerChrono)
Email     : mtkennerly+faq@gmail.com
Version   : v04
Created   : 2007-02-16
Updated   : 2024-07-29
Project # : 14
Profile 1 : https://www.gamefaqs.com/community/mtkennerly/contributions
Profile 2 : https://www.neoseeker.com/members/TheSinnerChrono/faqs

Note 1    : To skip to a particular section, initiate the search function in the
            program with which this file is being viewed, and input the [] code
            that precedes the desired portion's name in the table of contents.
            Include the brackets to ensure the propriety of the result.

Note 2    : In section titles, the name in []s is that of the continent or sea
            in which a smaller area (such as a village) is located.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$                                       $#$#$#$#$#$#$#$#$#$#
#$#$#   [01'00]   ---            Administrative           ---   [01'00]   #$#$#
#$#$#$#$#$#$#$#$#$#$                                       $#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [01'01] ---            Format           --- [01'01] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

   "  * - Text  "
Descriptions of character actions, etcetera.


     -(Text)
Following the above would be the events prompted by a particular option.
The number of hyphens corresponds to the choice layer; i.e., the first set
of options will have one hyphen, the second set will have two, and so on.
One equal sign accounts for two hyphens.

* "<see below>" is used when a given option must be selected to proceed.

* "<no script>" is used when any option can be chosen to progress, but the one
  in question has no responses associated with it (i.e., it skips to the set of
  script that is triggered regardless of one's choice/s).


"{S}"  =  Spoken
"{M}"  =  Mental  (using Mind Read)
"{O}"  =  Object  (the message displayed upon examination)


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Speaker identification  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

[Item]      =  Item vendor
[Weapon]    =  Weapon vendor
[Armor]     =  Armor vendor
[General]   =  Item/weapon/armor vendor


Dau  =  Daughter
G.   =  Great  (Great Healer)
X's  =  Xyz's  (e.g., I's = Isaac's)


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [01'02] ---            Credits          --- [01'02] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

   [ Kyarorain ]
* Composed "The Adepts of Weyard", which provides Mind Read script for Karst and
  Agatio in Jupiter Lighthouse (02'39), and for the final visit to Prox (02'49).

  http://kprs.laronmi.net/taow/info/trivia.htm
  http://kprs.laronmi.net/taow/miscellany/mindread/mindread.htm


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [01'03] ---           Versions          --- [01'03] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

   [ v01  -  2007-02-16 ]
* Initial release.



   [ v02  -  2007-02-26 ]
* Added the scene that occurs after being carried out of the Sea of Time
  by a current. (02'31)



   [ v03  -  2008-07-21 ]
* Made "[###]" designations continuous throughout each area, rather than using
  different sets of numbers for characters outside and inside of buildings.

* Added "Link Lobby" section. (03'05)

* Added the scene that occurs after Jenna is downed in battle. (02'01)

* Added Kraden's alternate reply upon saying "No" to Man 1's question of
  "Do we have your word?". (02'31)

* Added the result of the Lash Pebble being unavailable. (02'31)

* Added Mind Read script for Karst and Agatio in Jupiter Lighthouse (02'39),
  and for the final visit to Prox (02'49).


   [ v04  -  2024-07-29 ]
* Updated contact information.
* Added legal section.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [01'04] ---             Legal           --- [01'04] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

This document is released under CC-BY-SA 4.0:
https://creativecommons.org/licenses/by-sa/4.0

This does not apply to the game's verbatim dialogue or characters,
which I do not own. This document is intended to encourage and assist
discussions of the game and its story.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$                                       $#$#$#$#$#$#$#$#$#$#
#$#$#   [02'00]   ---               Script                ---   [02'00]   #$#$#
#$#$#$#$#$#$#$#$#$#$                                       $#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'01] ---           Prologue          --- [02'01] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#
$#  Recap  #$
#$#$#$#$#$#$#

Ages ago, or so the stories tell, the power of Alchemy ruled over the world of
Weyard. Alchemy wrought the base elements of humanity into thriving civil-
izations, like lead into gold. But in time, man's dreams gave birth to untold
strife. Dreams of endless riches, of eternal life, of dominion over all that
lived... Dreams of conquest and of war. These dreams would have torn the world
apart if not for a few brave and wise men, who sealed away the power of Alchemy
deep in Mt. Aleph's Sol Sanctum.



Prologue from Book One

The town of Vale guarded the secret for many years, until Isaac and Jenna,
whose parents died in a storm 3 years before, disturbed the sanctum. Saturos
and Menardi, of the Mars Clan, following them into the sanctum. With them
traveled Jenna's brother, Felix, thought lost in that same tragic storm.
Saturos and Menardi stole the Elemental Stars, the keys to breaking the seal
on the power of Alchemy, and kidnapped Jenna and the scholar Kraden.

If these four jewels were used to fire the elemental lighthouses, the seal on
Alchemy would be broken.

Isaac and Garet set out to stop Saturos, rescue their friends, and return the
Elemental Stars to their home in Sol Sanctum. They banded together with a young
Wind Adept named Ivan and pursued Saturos and Menardi to Imil, a winter-locked
town near Mercury Lighthouse. There, they met the guardian of the lighthouse,
a Water Adept named Mia. With her, they pursued Saturos to the aerie high atop
Mercury Lighthouse. Isaac was too late to stop Saturos from lighting the beacon
and escaping.

Again Isaac chased him, crossing Angara to the shores of the Karagol Sea.
Taking passage on a troubled ship, Isaac crossed the Karagol to Tolbi. He spoke
with Tolbi's leader, a strange man named Babi. Babi entered Isaac in Colosso as
a test of his powers. Isaac's Psynergy won Colosso and earned him Babi's trust.
Babi revealed a great secret to Isaac... Thanks to mystic draught from the lost
land of Lemuria, Babi had lived for 150 years! He offered to help Isaac,
who then headed deep into Gondowan.

In the town of Lalivero, Isaac learned that Saturos and Menardi had kidnapped a
young girl named Sheba, whom they needed within the lighthouse. Isaac fought and
defeated them atop the lighthouse, but he was too late--the beacon had been lit.

A great cataclysm followed. Sheba fell into the sea. Felix jumped in to save
her, but both were lost in the roiling waves. Jenna left the lighthouse to
find them, but to no avail...

Isaac went to Lalivero, where Babi asked him to find Lemuria and the remaining
lighthouses. He gave Isaac a Lemurian ship to make the journey for the lost
land.

This chapter of our story begins with Jenna, just before the beacon on Venus
Lighthouse is lit...



Camelot Presents
Golden Sun Book Two
The Lost Age


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Venus Lighthouse  -  Room with electric barrier  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Felix, Jenna and Kraden are present. Felix uses the Psynergy "Move" to
    push a statue onto the switch that deactivates the electrical barrier.
    Afterwards, Felix heads back through the lighthouse to the aerie, leaving
    Jenna and Kraden to head out of the building themselves. They head for
    the nearby stairway, but Jenna stops.

Jenna     : Are you sure we should be leaving like this? Once we go down those
            stairs, we can't get back into the lighthouse. Maybe I should have
            stopped my brother...

Kraden    : Jenna, is something troubling you?

Jenna     : I just...

Kraden    : What is it? What's wrong?

Jenna     : I have a bad feeling... Like something terrible is going to happen.

* - Alex teleports into the room.

Alex      : How unlike you, Jenna.

* - Jenna and Kraden appear caught off guard.

Alex      : Surprised to see me?

Kraden    : A-Alex... Were you listening?

* - Alex looks around.

Alex      : Where's Felix? Why isn't he here with you?

Jenna     : My brother? He left us.

Alex      : What can Felix possibly be thinking?

Kraden    : He was worried about Sheba. He went to check on her.

Alex      : He was supposed to be leading you out of here! I thought you would
            have been far from this lighthouse by now. Why are you still here?

Kraden    : We tried to stop Felix from going back up to the aerie.

Alex      : How like him. Once Felix gets an idea into his head, he rarely
            changes his mind.

Jenna     : Alex, what were you talking about just now? What did you mean when
            you said... "How unlike you"?

Alex      : I was merely surprised to hear you expressing such concern, Jenna.
            Nevertheless, I'm impressed Felix went back...

Jenna     : Don't change the subject, Alex! What did you mean!? Are you saying
            that I'm insensitive!?

Alex      : If that's what you heard, then I must have misspoken.
            Accept my apologies.

Kraden    : Well, Jenna, I think Alex has said his piece on the matter...

Jenna     : I'm not sure he has, Kraden.

* - She turns back to him.

Jenna     : Who do you think you are, talking to me like that!?

Alex      : I retract my statement, my dear. Forget all about it, Jenna.
            So tell me about this "feeling," Jenna...

Jenna     : I'm just...I'm not sure we should be leaving Venus Lighthouse yet...

Kraden    : What are you saying?

Alex      : You can't really mean to remain here...

Kraden    : Alex is right. It's far too dangerous, Jenna. We would only hinder
            the others...

Jenna     : The others? Did Isaac follow us to the lighthouse?

Kraden    : It would seem so.

Jenna     : He must be trying to stop Saturos and Menardi! If my brother goes
            back and finds Isaac, they're going to end up fighting.

Alex      : If the Venus Lighthouse has not yet been lit, yes. They will fight.

Kraden    : Felix is a terribly rash young man, is he not?

Jenna     : Why are boys such fools?

Kraden    : He may be rash, but Felix is no fool. His good qualities outweigh
            his bad...

Jenna     : That's why I think Isaac would understand if we just talked to him.
            Why didn't I think of this before now? Please... Can't we go back up
            and talk to Isaac?

Alex      : I'm afraid that's not possible.

Jenna     : Alex, why?

Alex      : He is an enemy.

Jenna     : Isaac? An enemy?

Alex      : Our methods may differ, but you and I ultimately want the same
            thing...

Kraden    : To light the elemental lighthouses...

Alex      : Isaac and his friends would prevent this from happening.

Jenna     : So that makes them enemies?

Alex      : But fear not... They won't be able to defeat Saturos and Menardi.

            So... Felix went back to the top of the lighthouse?

Kraden    : Why do you seem so pleased, Alex?

Alex      : Why shouldn't I be? After all, the lighthouse will soon shine
            brightly once again!

Jenna     : Alex, why do you want to see the beacon lit so badly?

Alex      : Oh, so it's my turn to answer questions, is it? Once, Alchemy was
            commonplace throughout this world... With its power, mankind worked
            wonders across the land...

Kraden    : The lost age of man...

Alex      : I want to see that world restored once again, and...

Jenna     : And what, Alex?

Alex      : We've spoken long enough already. Let us continue this another time.
            We should leave the lighthouse now, before the beacon is fired...

Kraden    : I concur... Let's meet at the location we agreed on and wait for
            Felix.

Jenna     : All right, Kraden, let's go.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Venus Lighthouse  -  Outside  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

?????     : There they are! Get 'em!

* - Five soldiers and five other men are present.

Soldier 1 : Iodem sent us to stand guard here, but...

Soldier 2 : I never thought we'd actually run into them!

Man 1     : Scoundrels! What have you done with Sheba?

Man 2     : Return her now, or you're really going to regret it!

Soldier 4 : Um... Aren't there supposed to be more of them?

Soldier 5 : Huh... Maybe they're just the first ones to come out...

Man 4     : Great! That means we've got 'em outnumbered!

Man 5     : We can probably take 'em, you think?

Soldier 5 : Go fetch the other Tolbi soldiers still stationed in Lalivero...

Soldier 3 : Yes, sir!

* - Soldier 3 departs.

Man 5     : And we'll go tell the guys in the caves!

Man 3     : Got it, Boss!

Kraden    : How unfortunate... It looks like an ambush. What should we do,
            Jenna?

Jenna     : What do you mean? Look around... We'll have to fight them!

Alex      : Are you serious? Jenna, are you really prepared to fight these men?

Jenna     : We don't have any other choice. We have to...

Alex      : Well, then. Allow me to shoulder some of your burden.

* - Alex steps forward.

Kraden    : ...Burden?

Alex      : We regroup along the road leading away from Lalivero. Do you
            understand?

-----------------------------------------------------------
     -(Yes)
Kraden    : You don't need to remind us, Alex. We know the place.



     -(No)
Kraden    : It's quite simple, Jenna. The meeting place is in the direction
            opposite Lalivero.
-----------------------------------------------------------

Alex      : Follow this road west, and take the path down through the canyon
            to the cave. On the other side of that cave, you will find a small
            peninsula called Idejima. We meet there.

            Thankfully, only those workmen block your route.

Jenna     : And fortunately...

Kraden    : They don't look too tough...

Man 1     : Hello! We can hear you!!!

Man 2     : That's just plain rude!

Alex      : Why don't the two of you escape and leave the Tolbi soldiers to me?

Jenna     : The two of us? Alone?

Alex      : You can use Psynergy, can't you, Jenna?

Jenna     : Um... Yes.

Alex      : Then you'll be fine. We shall reconvene at the peninsula.

Soldier 1 : You think you can take on Tolbi's finest on your own, little man?

Alex      : I do not wish to inflict unnecessary bloodshed.

Soldier 2 : Don't wish to... What's that supposed to mean?

Alex      : If you lay a hand on these two, I assure you that you will be made
            to regret it.

* - Two of the soldiers approach Alex.

Alex      : By advancing, I assume you mean to fight. Permit me to strike the
            first blow.

* - He uses his Mercury Psynergy to throw the two soldiers away with a blast
    of water.

Soldier 4 : What was that!?

Soldier 5 : I don't know, but whatever he did, it's out of our league!

* - Soldier 4 turns to the workmen.

Soldier 4 : You guys deal with him until backup arrives!

Alex      : Oh, so you're next?

Man 1     : Hey, no need to worry about us!

Man 2     : We're not soldiers... We're not anybody!

Man 4     : Seriously, there's no way we're gonna face off against you.

Man 5     : Let's get outta here!

* - The workmen flee.

Alex      : How undignified... and how shameful. Jenna, now is your chance.
            Go to Idejima and wait for me.

* - Soldier 4 approaches Alex.

Alex      : I'm not finished with you yet.

* - The soldier backs up.

Alex      : You mentioned backup from Lalivero? Let's go meet them together,
            shall we?

Soldier 4 : Hey, pal! When they get here, you'll really be in for it!

Alex      : Do you honestly believe that even a hundred of you could stop me?
            How amusing... This I must see.

* - The soldiers continue to back up as Alex advances.

Kraden    : They're gone... Come on, Jenna. Let's be going. There's nothing
            standing in our way now!

Jenna     : But...

Kraden    : What is it now? Ah... You're worried about hurting any innocents?

-----------------------------------------------------------
     -(Yes)
Kraden    : Well, just try to hold back when you're fighting.



     -(No)
Kraden    : Oh. You must be concerned about Felix. We can't do anything to help
            him here.
-----------------------------------------------------------

Kraden    : Let's get going! To the peninsula!





* - If you try to head to the east:

Kraden    : Not that way, Jenna! The meeting spot is west of here. We must go
            down that road and into the hills.





* - To the west, Man 3 is present.

Man 3     : Why do I gotta be the one to wait for backup!?

* - He notices Jenna and Kraden.

Man 3     : Yaaah! P-P-Please! Just let me go, and... Hey! That scary guy with
            the blue hair's not with you... Great! Now, you'll see what I'm
            really made of!

* - The man engages Jenna in combat. After defeating him:

Man 3     : Ugggh. I can't believe I got beaten by a girl...





* - If Jenna is downed in any of the prologue's battles, then she awakens
    on the ground outside of the lighthouse.

Kraden    : Jenna... Are... Are you all right?

Alex      : Ah, Jenna... You're awake.

Kraden    : Can you stand?

* - She does so.

Alex      : It's a good thing I came back for you two...

Kraden    : Perhaps you ought to come with us this time...

Alex      : No. Someone has to keep Tolbi's soldiers at bay. I'll have to go
            to Lalivero and confront them there. We'll meet at Idejima.

* - He leaves.

Kraden    : He's gone again. And we'd best be going as well...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Suhalla Gate  -  Section 1  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

Man       : Waahhh! It's them! Whoa there... Where'd the blue-haired guy go?
            Who cares! I can handle some girl and her grandpa!

* - After defeating him:

Man       : Ooooog. Maybe I shouldn't have underestimated her...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Suhalla Gate  -  Section 2  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - When trying to head past the path to the Gateway Cave:

Kraden    : Not that way, Jenna! The meeting spot is down this way. We must
            climb down here and go into that cave.





* - When trying to enter the Gateway Cave, three men jump out.

Man 1     : Ha! That was a good idea, waiting here for 'em! You two aren't going
            anywhere!

Man 3     : Except with us, back to Master Iodem!

* - After defeating them:

Man 1     : Maybe I should have eaten a bigger breakfast.

Man 2     : Oh, man... There goes my big promotion...

Man 3     : All right, so maybe you are going somewhere after all...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Suhalla Gate  -  Gateway Cave  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A "Punch Ant" (a human-sized ant with boxing gloves) appears.
    After defeating it:

Kraden    : My! That was invigorating! He wasn't too strong... I never knew
            fighting could be so fun! Ah, but we'd better get on to the
            peninsula...


#$#$#$#$#$#$#$#
$#  Idejima  #$
#$#$#$#$#$#$#$#

Kraden    : This is the place, isn't it?

* - Regardless of whether the player selects yes or no:

Kraden    : The peninsula at the end of the road to the west... That's what he
            told us. This must be Idejima! Hm... Menardi said a ship would be
            here... We ought to see if we can find it.

* - They look for a short time.

Kraden    : Jenna, it's over here! At first glance, it seems like a normal ship,
            but... There's something odd about it...

* - Kraden darts onto the ship.

Jenna     : Kraden, wait! Oh, I swear! You're like a kid with a new toy!

* - After a while, he still hasn't come back.

Jenna     : Hurry up in there!

* - He returns.

Jenna     : What's wrong?

Kraden    : It's missing...

Jenna     : Hm? What are you talking about?

Kraden    : The thingie... that makes it go.

Jenna     : What do you mean? What's so important about this... thingie?

Kraden    : The boat can't move without it...

Jenna     : That Menardi! She tricked us!

Kraden    : Tricked us?

Jenna     : Yeah, by passing this dud boat off on us!

Kraden    : There's no trick. If this boat is a dud, how did it get here in the
            first place?

Jenna     : Oh, right.

* - Kraden paces, thinking.

Kraden    : It must have been the orb...

Jenna     : What orb?

Kraden    : Don't you remember that crystal Saturos was carrying?

Jenna     : That big, black pearl thing?

Kraden    : I'm certain he said he could move the ship with it.

Alex      : Jenna, Kraden!

* - Alex emerges from the Gateway Cave.

Alex      : There you are. I see you've found the boat. We set sail as soon as
            the beacon has been fired, correct?

* - Jenna nods. Everyone looks at the lighthouse across the water.

Kraden    : Strange...

Alex      : What is it?

Kraden    : The beacon... It hasn't been lit yet.

Alex      : You're right... Why is it taking so long?

Jenna     : And why hasn't my brother returned?

* - Light shines from the aerie. The area around the lighthouse vibrates.

Kraden    : They've done it, Jenna! They've lit the beacon!

* - The vibrations intensify, becoming an earthquake.

Jenna     : What's happening, Kraden!? Why won't the ground stop shaking?

* - The foundation of the lighthouse begins to crumble.

Alex      : Strange... I think it might actually be getting worse!

Jenna     : I think the lighthouse is collapsing! Look! The ground around it is
            crumbling!

Kraden    : Mercury Lighthouse didn't react this way... What makes Venus
            different?

* - Due the earthquake, Idejima is completely severed from Gondowan.

Alex      : That last tremor tore a rift in the Suhalla Range!

Jenna     : How are we going to get back to Gondowan now!?

* - Idejima begins to drift out to sea.

Kraden    : Idejima... It's drifting away from the mainland!

Jenna     : But... what will happen to us?

* - The screen blanks out. Some time passes.

Jenna     : Oh, Kraden... How long will this island continue to drift?

Kraden    : I don't know... I wish you could tell me.

Jenna     : Sheesh... You're no help in times like this.

Kraden    : Hey, I'm hungry...

Jenna     : How can you even think about food? I wonder what happened to my
            brother..

Kraden    : I can't be certain, but it looks like they lit the Venus beacon.

Jenna     : Yeah, I know. You don't have to tell me that. That's how we wound up
            adrift at sea, right?

Kraden    : My, aren't you cranky today, Jenna! Well, I suppose you're just
            worried about Felix.

Jenna     : Isaac and the others must have been at the lighthouse, too.

Kraden    : I suspect you're right...

Jenna     : I miss them... Isaac... Felix...

* - Alex walks up to them.

Alex      : Come with me. There is something I wish to show you.

* - They head to the beach at the other end of the peninsula, where Felix and
    Sheba have washed ashore.

Kraden    : Felix! Sheba!
Jenna     : Felix... Sheba...

Kraden    : They... They're alive...

Jenna     : They're really alive!

Kraden    : What is this? Alex, what happened?

* - The screen blanks out. The Golden Sun: The Lost Age logo appears. When the
    scene switches back to the game, Felix and Sheba have been brought off the
    beach.

Kraden    : I thought Felix and Sheba were still inside the lighthouse.

Alex      : It's miraculous.

Jenna     : Miracle or no, I'm just happy my brother's alive.

* - Sheba moves a bit. Kraden doesn't notice.

Kraden    : What happened back there?
Alex      : ...

* - Kraden seems puzzled as to Alex's lack of response.

Jenna     : Sheba...

Sheba     : Oh...

Kraden    : Thank the elements, she's awake!

Jenna     : Sheba, are you all right? It's me, Jenna.

Sheba     : Jenna?

* - Sheba sits up.

Sheba     : What... happened?

Kraden    : It seems you drifted here with Felix.

Sheba     : With Felix...?

* - Sheba comes to her feet.

Jenna     : Take your time... Do you feel all right, Sheba?

* - She nods and examines her surroundings.

Sheba     : Where are we?

Alex      : Idejima. We were all to meet here... But now, the island is floating
            away from Gondowan.

Sheba     : This island is moving?

Kraden    : I know it must be very hard to believe, Sheba.

Jenna     : When the Venus Lighthouse was lit, a massive tremor tore us off
            the continent...

Alex      : The ground beneath the lighthouse roiled, as though it might crumble
            away.

Sheba     : I remember now... And that's what carried us away from Gondowan.

Kraden    : But what happened to you, Sheba? You were in the sea, and Saturos--

Sheba     : Saturos and Menardi are gone...

Alex      : What do you mean?

Sheba     : Another group came... They fought Saturos and Menardi and won.

Jenna     : Was it Isaac?

Sheba     : Isaac... Yes, I think that's what they called him...

Alex      : You expect me to believe Isaac and his companions defeated Saturos
            and Menardi?

* - Sheba nods.

Alex      : Have they really grown so powerful in so short a time?

Kraden    : But how did you wind up in the sea?

Sheba     : When the beacon was lit, the earthquake knocked me off the light-
            house tower.

* - Felix moves slightly. No one notices quite yet.

Jenna     : Then what's my brother doing here?

Sheba     : He tried to save me from drowning...

Kraden    : Felix jumped from the top of the lighthouse!? Dear me!

* - Alex notices Felix moving.

Alex      : Felix... are you awake?

Kraden    : Ah! Felix, you're awake!

Jenna     : Brother...

* - He stands.

Jenna     : Are you sure you should be standing?

* - He looks around.

Kraden    : You don't seem very surprised to find yourself on a floating island.

Alex      : Felix, once you'd saved Sheba, you must have swum out here, correct?
            You must have seen that this island was floating when you were
            swimming.

Jenna     : But what do we do now?

Sheba     : I have no idea. Nobody knows what lies beyond the Eastern Sea.

Kraden    : Unfortunately, I am a student of Alchemy, not geography...

* - Alex sees something.

Sheba     : What is it... Alex?

Kraden    : What's the matter?

Alex      : Can't you see it?

Jenna     : It's land! An island!

Sheba     : It's a little... big for an island.

Kraden    : That's no island... It's a new continent!

Jenna     : We're saved!

Kraden    : So it would seem...

Sheba     : Wait...

Jenna     : What is it?

Sheba     : We're going to pass north of the continent...

Kraden    : She's right!

Sheba     : I don't think we're going to make it!

Jenna     : Oh, Kraden... Felix... What are we going to do?

Felix     : ???

* - Kraden notices something else.

Kraden    : Oh... This can't be good.

Jenna     : What... is it?

Sheba     : It's... a tidal wave.

Jenna     : A tidal wave?

Sheba     : The earthquake must have caused it!

Kraden    : Oh... Oh my... It's coming right at us!

Jenna     : Alex... How can you stay so calm at a time like this?

Alex      : At times like this, where would be the good in panicking?

Sheba     : We'll be washed away!

Kraden    : Help!!!

* - The tidal wave collides with Idejima, during which Felix's group is rendered
    unconcious. By the time that Felix awakens, Alex and Saturos's ship are
    missing, and Idejima has drifted to the new continent: Indra.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Idejima  -  Indra  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - Felix is the first to regain consciousness.

<game>    : Do you want to check yourself for injuries?

-----------------------------------------------------------
     -(Yes)
<game>    : Looks like the arms are still attached. That's a good start.
            The legs are working fine, too. Yup. You're fine!



     -(No)
<game>    : You walk around a bit, and everything seems fine.
-----------------------------------------------------------





* - Jenna:

Jenna     : What... What am I doing down here? Oh... I must have blacked out
            when the wave hit... Hey! We've hit land! That wave must have
            carried us here! What luck! Have you checked everyone else?
            Are they all right?

-----------------------------------------------------------
     -(Yes)
Jenna     : Great! Then let's go!



     -(No)
Jenna     : Then let's go find them and get off this island!
-----------------------------------------------------------

<game>    : Jenna joined your party.





* - Kraden:

Kraden    : Oooog... Oh... Felix... Ouch... That was quite a blow... What
            happened when that wave hit? Felix, look! That wave carried us
            to the continent! We've hit solid land! Let's go, Felix!

<game>    : Kraden joined your party.





* - Sheba:

Sheba     : Ohhh... Nnng. The wave! What happened to the tidal wave? I thought
            we were done for, but we're all fine... And we've run aground!
            The tidal wave turned out to be a stroke of luck! I wonder where
            we are... We should take a look around!

<game>    : Sheba joined your party.





* - Trying to leave Idejima without the others:

Kraden    : Hey, Felix! You weren't planning on leaving me, were you?
            Hm? Well! It's land! The wave carried us back ashore! I assume you
            merely... forgot about me in your excitement? Understandable, but
            you should have waited for me, Felix. Nevertheless, let us be on
            our way!

<game>    : Kraden has joined your party.



Jenna     : I can't believe you two! How could you!? Leaving me on that island
            while you go off exploring on your own! And here I was, looking
            everywhere for you!

Kraden    : I'm sorry, my dear... Can you ever forgive us?

Jenna     : Oh... All right. Just don't leave me alone like that again...
            Anyway, look! That wave must have carried us to a new continent!
            Let's go exploring!

<game>    : Jenna joined your party.



Sheba     : Wa-Wait! Aren't you worried about me in the slightest? Did you
            rescue me from the lighthouse just to leave me for dead on this
            island?

Kraden    : Now, I'm sure he meant to do no such thing...

Sheba     : I wonder... Oh, don't give me that sad face... You know I can't
            stay mad at you... After all, you did save me, Felix. I won't soon
            forget that... But don't leave me behind like that again, OK?
            So that big wave pushed us aground? Way to go, Nature! What's out
            here, anyway?

Kraden    : That's what we were about to find out!

Sheba     : Let's get started then!

<game>    : Sheba joined your party.





* - When heading west of Idejima:

Kraden    : By the way... Where has Alex gone? He doesn't seem to be anywhere on
            the island. You don't think he set out on his own, do you?

-----------------------------------------------------------
     -(Yes)
Kraden    : Then I guess there's no reason to look for him here.



     -(No)
Kraden    : Well, he's no longer on Idejima, at any rate.
-----------------------------------------------------------

Kraden    : He might have gone to look for a ship.

Jenna     : Alex wants a ship?

Kraden    : Did you forget what he was saying?

-----------------------------------------------------------
     -(Yes)
Kraden    : He wants to return Alchemy to its former place in the world.



     -(No)
Kraden    : Then you know he wants to restore Alchemy to the world.
-----------------------------------------------------------

Jenna     : By lighting the four elemental lighthouses, he might just succeed.

Sheba     : But why the ship?

Kraden    : The remaining two lighthouses are unreachable by land. None remain
            to be lit across the Eastern Sea.

Jenna     : So what should we--

Kraden    : We must go to the Great Western Sea...

Sheba     : The Western Sea...

Jenna     : Is that where we're going, Felix?

-----------------------------------------------------------
     -(Yes)
Kraden    : Well said, Felix! And go there, we shall!



     -(No)
Kraden    : Don't be foolish, Felix. We must pursue Alex. We have to go there...
-----------------------------------------------------------

Jenna     : That's right! Our parents' lives depend on it!

Kraden    : What about you, Sheba?

Sheba     : What do you mean?

Jenna     : It's... not going to be an easy trip.

Kraden    : And there is no reason you should have to face that danger...
            Right, Felix?

-----------------------------------------------------------
     -(Yes)
Sheba     : Then you should know my reason for traveling with all of you,
            Felix...



     -(No)
Sheba     : Felix remembers... I have a reason to be traveling with you...
-----------------------------------------------------------

Kraden    : What do you mean, Sheba? What reason?

Sheba     : It's my destiny...

Jenna     : This quest is your... destiny?

Kraden    : And you couldn't tell us about this earlier?

* - Sheba nods.

Jenna     : But how can we trust you when we don't know why you're with us?

Sheba     : I'm sorry... But please, you have to take me! You must! You need me!

Kraden    : I don't understand. Why exactly do we need you?

Sheba     : You know that I am an Adept, don't you? I can control the wind, as
            Felix already knows...

Kraden    : You knew that we was a Wind Adept?

-----------------------------------------------------------
     -(Yes)
Kraden    : Saturos must have mentioned it atop the lighthouse... I see...



     -(No)
Kraden    : Saturos must have known it, even though he never told you...
-----------------------------------------------------------

Sheba     : They saw that I was a Wind Adept right away... They kidnapped me for
            my powers... They needed them on their journey.

Jenna     : Oh, yeah... They would have needed an alignment that complemented
            their own.

Sheba     : They said they would need a Wind Adept in order to light Jupiter's
            beacon.

Kraden    : Ah, of course... And I suspect we'll need your power there as well.

Sheba     : So you see, you do need me.

Jenna     : All right... I guess I understand now.

* - Jenna turns to Felix.

Jenna     : But you want to know what she meant by destiny, too, don't you?

-----------------------------------------------------------
     -(Yes)
Jenna     : I wish we could read minds like Sheba. Then we'd know...



     -(No)
Jenna     : Oh, so it's just me? Too bad I can't read minds like Sheba, huh?
-----------------------------------------------------------

Kraden    : I'm sure she will tell us in her own time. Won't you, Sheba?

* - She nods.

Kraden    : I think, for now, that we should simply trust Sheba.

            Now, I am quite famished. Shall we get moving?


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'02] ---           [Indra]           --- [02'02] #$#
#$#$#                      Daila                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} You don't look familiar. Have you been to Daila before?

               --------------------------------------------
                    -(Yes)
               Strange... I just don't remember ever seeing you around here
               before.



                    -(No)
               Well then, welcome to Daila, the northernmost town on the
               continent of Indra!
               --------------------------------------------

                 * - 2nd+ time:

               We were hit by a gigantic tidal wave, but there were no
               injuries... It was miraculous!

           {M} That wave turned this place into a swamp! Everything smells
               like brine!

[002]     :{S} I saw a bright light in the northwestern sky earlier... Somewhere
               over Gondowan. It was right before the tidal wave... I wonder if
               there's a connection...

           {M} I thought I saw some lights in the northwestern skies... Maybe I
               just imagined them.

[003]     :{S} That tidal wave left a lot of standing water in our village...
               The worst part is that it's all salt water.

           {M} With all this salt water on the ground, what will happen to our
               crops?

[004]     :{S} Didn't it feel like all of Indra moved when that wave hit?

               --------------------------------------------
                    -(Yes)
               I knew it! You felt it, too! And that shock afterward! It felt
               like the whole continent got rammed into something!



                    -(No)
               Wow... That wave must have knocked you silly if you didn't notice
               it...
               --------------------------------------------

           {M} That must have been one serious wave to make the whole continent
               move... I didn't even know continents did that!

[005]     :{S} Thank goodness for that mountain range to the north... If that
               range weren't there, we would have been washed away for sure...

           {M} The sea god must have saved us from the wave. It's good we have a
               shrine honoring him.

[Item]    :{S} I haven't seen Tavi and Riki around lately... I like those little
               guys, so I'm kind of worried about 'em.

           {M} I'm sure those two went to the Shrine of the Sea God. They never
               listen! I told them they were way too small to climb those
               cliffs...

[006]     :{S} Riki and Tavi sure are out late...

           {M} The Shrine of the Sea God stopped the wave, but I'm worried...
               Riki and Tavi were playing in there, and I'm too scared to tell
               anyone.

[007]     :{S} I wonder if those two are still out there... They know it's
               off-limits.

           {M} I can't believe those losers were inside the shrine when the wave
               hit! If Riki and Tavi want to be idiots, I say, let 'em!

[008]     :{S} Huh? You want a boat?

               --------------------------------------------
                    -(Yes)
               What kind of insensitive jerk are you? Everyone knows all our
               boats were destroyed by the tidal wave!



                    -(No)
               Of course not! The tidal wave ruined all our boats... Asking us
               for a boat now would be just plain mean!
               --------------------------------------------

           {M} With all the boats gone, we sailors are stuck here! What are we
               supposed to do on dry land? Knit!?

[009]     :{S} Ohhh... that wave knocked me over, and now I can't get up. I must
               have been born to suffer!

           {M} My hip's killing me, and all that woman cares about is how muddy
               my clothes are! She cares more about the laundry than she does
               me!

[010]     :{S} Our village survived the wave, but all our boats were destroyed..
               We won't be sailing for a while, but we'll pull through somehow..

           {M} That wave was brutal! It smashed my boat to splinters!

[011]     :{S} Bleah! I fell in a puddle and got my clothes dirty! Mom's gonna
               have a fit!

           {M} Bleccch! This water's saaalty!

[012]     :{S} Yaaay! Puddles in the village! Yaaay!

           {M} Yay! We never get puddles like this, not even when it rains!

[013]     :{S} The ancient tower to the east? It's the Shrine of the Sea God...
               Listen, if you're not into being cursed horribly, you should stay
               away from there.

           {M} I can't believe those children play in the shrine! It's danger-
               ous, and it will only bring them misfortune...





   [ Buildings ]
* - Riki's residence:

[014]     :{S} Riki's really in for it when he gets home! He's been out playing
               with his friend for days!

           {M} Riki, Tavi... Where are you? What are you up to?

[015]     :{S} That no-good kid of mine! Taking his father's fishing pole!
               I mean, really! If he doesn't come home soon, he's really going
               to get it!

           {M} That Tavi's a bad influence on Riki... Just because he lives next
               door doesn't mean they have to be friends!

-----
* - Tavi's residence:

[016]     :{S} I wonder where our little Tavi has gone. I'm getting worried.
               He was gone when the wave hit, and he hasn't been home since...

           {M} I'll bet that, wherever Tavi is, Riki is with him... The neigh-
               bors must be pretty worried, too.

[017]     :{S} Tavi never misses three o'clock snacksies! Where could he be?
               His food's getting cold...

           {M} If Tavi isn't home soon, we're going to have to go looking
               for him.

-----

G. Healer :{S} Travelers! Well, I'll be! Do you have a lot of time and nowhere
               to go?

               --------------------------------------------
                    -(Yes)
               Then I suggest you visit the Kandorean Temple to see Master Poi.
               He performs great feats, but I'll warn you, he might not let
               you in...



                    -(No)
               Oh, going to Madra, are you? It's a dangerous road, but no one
               will stop you from taking it, my children.
               --------------------------------------------

           {M} Travelers with nowhere to go... This is bad. I hope they stay
               out of the shrine... If they anger the sea god, there's nowhere
               they could hide, not anywhere in Indra!

-----

Innkeeper1:{S} What should I cook for our guests tonight? I just can't decide.

           {M} We can't sail, and we can't fish... Not with our ships in this
               condition... Oh... I'm not looking forward to becoming a
               vegetarian...

Innkeeper2:{S} We run a very small inn, so we make do with just the two of us
               working here...

           {M} Look at all these guests! We need more help... but how will we
               afford it?

[018]     :{S} I don't know when I'll be able to return to Madra. I sure miss
               the food there.

           {M} After all that shaking, I wouldn't be surprised if the roads were
               unusable.

[019]     :{S} I heard the seafood in Madra is wonderful! I wonder what kinds of
               fish they catch in Madra...

           {M} I'm so torn... Do I like my fish grilled? Or do I prefer poached?
               It's hard to say... Why is life so difficult?

-----

[020]     :{S} If you're looking for a boat, you might check in Madra... Head
               south, and then when the road forks, follow the path to the east.

           {M} I wonder how the road to Madra is holding up after that flood...
               The ground was always pretty soft around there...

[021]     :{S} If you head south, you'll find a fork in the road. Take the road
               west, and you'll hit the Kandorean Temple in no time.

           {M} I wonder if the holy man at the Kandorean Temple is as powerful
               as they say...

-----

[Weapon]  :{S} You folks ain't thinkin' 'bout goin' south, are ya? The roads to
               the south are a real mess from the earthquake. Dangerous, too.

           {M} I'm glad I'm not going to Madra now... It had been so parched
               for so long... And now, after the quake, I'm sure it's full of
               cracks and fissures and gaps...

[Armor]   :{S} You guys look new 'round these parts! What bring you to here?
               There's nothing much to see on this forsaken continent. You must
               be odd folk indeed!

           {M} If those two scamps knew there were travelers in town, they'd
               have a field day.

-----

Mayor     :{S} In all my years as mayor, I've never seen a wave like that
               before... I'm grateful that nobody was seriously injured.

           {M} At least, nobody seems to have been injured too badly. Maybe I
               should make another inspection later.

[022]     :{S} The wave was awful, but the noise that followed was even worse...
               The shock alone could probably have destroyed the road to Madra.

           {M} I still don't know what that sound I heard was... With everything
               that's been going on lately, I'm still a little edgy...

[023]     :{S} A lot of folk said they heard a terrible rumbling from the south-
               east. You ask me, it was the road to Madra crumbling to bits...

           {M} We should find a different way to get to Madra. That shoddy
               road's a mess...

[024]     :{S} Between the pirates and the tidal wave, this town has the worst
               luck! Now that Briggs has been arrested in Madra, maybe our luck
               is changing...

           {M} Now that Briggs is locked away, we shouldn't have any pirate
               trouble this year. Of course, that tidal wave did more damage
               than those pirates ever managed...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Upon exiting to the south  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A Venus Djinni named Echo is flying around. Felix notices it.

Echo      : Hey! You look like you already know a little about us, huh?

-----------------------------------------------------------
     -(Yes)
Echo      : See, you know all about us, so you must be an Adept.



     -(No)
Echo      : Well, you weren't very surprised when you saw me. Am I right?

    --(Yes)
Echo      : I thought so. I could tell you were an Adept from a mile away!

    --(No)
Echo      : No way! You? Surprised? Nah, I can't believe that! I mean, look at
            you! You're an Adept!
-----------------------------------------------------------

* - Felix appears surprised that the Djinni knew he was an Adept.

Echo      : Even I know that! You look like you're new around here. Embarking on
            a dangerous journey in a strange land? I thought so... Well, I'm
            looking for my companions... We were parted when Mt. Aleph erupted.
            Would you mind helping me find my companions? Come on, take me with
            you. I'll even lend you and your allies my powers! You see, the more
            Djinn you have with you, the more powerful your Psynergy becomes!
            All you have to do is set us and then unleash us in battle! If you
            gather a bunch of us, you'll have all that power at your disposal!
            So what do you say? Will you be a pal and take me with you?

-----------------------------------------------------------
     -(Yes)
Echo      : I'm so happy! Oh, you won't regret this, I promise!

* - Echo responds the same way to being accepted regardless of when it occurs.



     -(No)
Echo      : Oh, come on! I promise I won't be a burden and eat all your chips
            or anything!

    --(No)
Echo      : But if I'm with you, you'll be all kinds of strong!

   ---(No)
Echo      : Wait, that's not it... There's more! Your allies with develop
            exciting new abilities!

  ----(No)
Echo      : And I'll be your best friend ever in combat! I'll be all over the
            bad guys, I promise!

 -----(No)
Echo      : What, you want to see me beg? Fine! I'm begging! PLEASE! Let me
            join your group!

------(No)
Echo      : You just don't get it, do you? I'm not used to being ignored,
            you know. Take me with you!

-----=(No)
Echo      : Don't be a meanie, OK? Nobody likes a meanie. I'm serious here.
            You don't really want to leave me behind, do you?

----==(Yes)
Echo      : Oh, all right. If that's the way you're gonna be, fine.
            I'm coming with you anyway!
-----------------------------------------------------------

<game>    : The Venus Djinni Echo has become Felix's pal.

Echo      : While I'm here, would you like me to give you a quick explanation
            about Djinn?

-----------------------------------------------------------
     -(Yes)
Echo      : After bringing a Djinni into your party, you must set it to
            somebody.

* - Echo opens up the Djinn menu to demonstrate some things.

Echo      : To give your Djinni to someone else, move it like this. After
            choosing who gets the Djinni, you can "set" it. Setting a Djinni
            changes your attributes and sometimes even your class. When your
            class changes, the Psynergy you can use may also change.

            Next, I'll show you how you can use us in battle. Each Djinni has
            different, unique powers. Once we have been set, you can unleash us
            in battle to use our powers. So, Felix, let me demonstrate the power
            of my attack now.

* - They automatically engage an enemy in battle.

Echo      : Choose this command when you want to unleash me in battle,
            all right? That's all you have to do to unleash a set Djinni!

* - Felix uses Echo's ability.

Echo      : See! What did I tell you? When you unleashed me, I used my special
            attack ability! After being unleashed, we Djinn will then stand by,
            ready to be summoned back again... If you have multiple standby
            Djinn, you can summon even greater powers into battle!

* - With one Venus Djinni (Echo) on standby, Felix summons Venus.

Echo      : See! We Djinn can be pretty useful, can't we? But... there's one
            more thing. After a Djinni has been used to summon, it must spend
            time in recovery. And once we've recovered, we automatically set
            ourselves again, so we're ready to attack! So, we go from set to
            standby to recovery, then back to set. That's just a simple little
            explanation of how to use us.

            Did you get all that?


    --(Yes)
Echo      : Well, that's it. Now, we're pals forever!


    --(No)
Echo      : Hmmmm... Do you want me to explain it all to you again?

   ---(Yes)
Echo      : Well, then, I guess I'll go back to the beginning, OK?

* - Echo repeats the explanation.

   ---(No)
Echo      : Well, that's it. Now, we're pals forever!





     -(No)
Echo      : Well, that's it. Now, we're pals forever!
-----------------------------------------------------------

Echo      : Oh, yeah! If you want to learn more about Djinn, refer to the help,
            OK? You and your friends should make sure you get the most out of
            us Djinn.

<game>    : Felix found the Venus Djinni Echo!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'03] ---           [Indra]           --- [02'03] #$#
#$#$#                 Kandorean Temple                #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - The gate to the temple grounds is shut.

Guard 1   :{S} Have you come to see Master Poi?

               --------------------------------------------
                    -(Yes)
               The master will see no one. Leave now, and do not return.



                    -(No)
               I'm sorry, but the temple is closed to sightseers. Go home now.
               --------------------------------------------

           {M} I do not understand Master Poi. If I were him, I would allow
               more people to enter. Instead, I must turn away the very people
               who would benefit from his teachings.

Guard 2   :{S} Once the period of meditation has begun, none may enter the
               temple grounds. Master Poi's teachings require absolute
               concentration.

           {M} I was hoping to hear Master Poi speak. Instead, I got guard duty.
               How boring...



* - Upon approaching the cave entrance to the northwest covered by a bush:

Kraden    : This wall looks rather suspicious, wouldn't you say, Felix?

* - Sheba can use Whirlwind to dispose of the bush.

Kraden    : Fantastic work, Felix! Keep a watchful eye for any strange-looking
            areas!

* - The cave leads to within the temple walls.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Temple exterior ]
[001]     :{S} I am not just meditating. I am guarding the entry as well.
               It is important work. But someday, I will be permitted to enter
               the temple...

           {M} Empty the mind to lighten the body... I've been fasting for
               days... I've got to be light enough now!

[002]     :{S} Please don't break my concentration! I am... lighter than air...
               floating, rising up...

           {M} My mind is empty; my body is light... Now... float... float...

[003]     :{S} I hope to enter the temple one day... I want to learn from the
               master himself...

           {M} I still can't believe that the older monks can levitate through
               meditation. If I work hard enough, maybe I'll be able to do it,
               too. Maybe.


#$#$#$#$#$#$#$#$#$#$#$#
$#  Temple interior  #$
#$#$#$#$#$#$#$#$#$#$#$#

* - Poi, who is atop a high ledge, yells at [004] below.

Poi       : You there! Focus your mind!

* - The individual does so, and begins to levitate, albeit with some difficulty.

[004]     : Did you see that, Master?

Poi       : No, no, no! You lack discipline!

* - He turns to [005].

Poi       : Now, you!

* - The individual does so, with slightly less trouble than the other man.

[005]     : How was that, master?

Poi       : Improving... slowly! Continue your meditation!

* - Poi turns to [006].

Poi       : Your turn!

* - The individual does so, quickly correcting whatever small errors he makes.

[006]     : Master, have I done it?

Poi       : Not bad... You might stand a chance to succeed...

[006]     : I can do it, Master! Please, just let me try!

Poi       : Your skills lack polish... It may be dangerous. Do you still wish
            to enter?

[006]     : Yes, I do! I do!

Poi       : If you fail, you may lose more than just your pride...

[006]     : I do not fear death, Master!

Poi       : Ho ho! Is that so? Very well, then! It is time for your trial,
            my son!

* - [006] approaches an entranceway.

Poi       : Enter the cave, and ascend!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Temple interior ]
[004]     :{S} HE went in before ME? What nonsense! Wait... I guess I ought to
               be more supportive and hope for his success...

           {M} There's no way I'm rooting for that loser! Choke! Choke!
               Fail the test! Then, I'll get my chance!

[005]     :{S} Empty mind, empty body. By clearing my thoughts, I can ascend...

           {M} Arrgh! I was so close! I can't believe I didn't make it! Gah...
               I'm so consumed with frustration that I can't clear my thoughts..





   [ Trial area ]
* - [006] lies on the ground.

[006]     :{S} It seems I may not have been ready after all... I should start my
               meditations over again...

           {M} Is it really possible for anyone to pass this test?



* - Room with boiling pot blocking the path:

Signpost  : Extinguish your desire, and the fire will cool. Empty your mind,
            and you will feel no pain!
               -Poi-


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Upon clearing the trial  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

Poi       : You have passed a very difficult test. You have pleased your
            teacher! Wait... You're not one of my students! Who are you!?
            How did you... come this far?

Kraden    : Ah, yes... How indeed?

* - Poi runs out of the room to the ledge where he was shouting to the others,
    and looks below.

Poi       : The rope is still on the floor.

* - Poi returns to Felix's group.

Poi       : You must have come through the cave... That means... I must give
            you... the secret of Lash!

Kraden    : Master Poi... You seem perturbed.

Poi       : Oh, no... Not at all...

Kraden    : Felix, am I imagining it, or does he seem perturbed?

-----------------------------------------------------------
     -(Yes)
Poi       : I am not perturbed. Merely... surprised.



     -(No)
Poi       : No one from outside the temple has ever passed the test.
            It's amazing...
-----------------------------------------------------------

Kraden    : What is this "Lash" you mentioned a moment ago?

Poi       : Lash is a sacred power, passed down for years to the followers of
            this temple.

Kraden    : A sacred power? And it's called Lash, you say?

Poi       : And now, I must pass it on to you. It is our way. It is a gift
            given to all those who pass the test, as it has been for ages.

Kraden    : What type of power is this Lash?

Poi       : Allow me to show you.

* - Using Lash, Poi telekinetically ties a rope to a stake atop a ledge.

Kraden    : Lash looks quite a bit like Psynergy, doesn't it?

-----------------------------------------------------------
     -(Yes)
Poi       : Psynergy, hm? We call it spiritual strength, but it seems the same.



     -(No)
Poi       : I do not know of your Psynergy, but our power comes from within.
-----------------------------------------------------------

Poi       : This technique uses the spiritual to affect the physical. One with a
            strong spirit can lift and move heavy objects farther.

Kraden    : The distance changes with your level of power? Fascinating!

Poi       : Those who cannot pass this cave's trials are not worthy of the
            technique.

Kraden    : Felix, do you think this cave was designed to test one's control of
            Psynergy?

-----------------------------------------------------------
     -(Yes)
Poi       : Yes, yes! Well done, old man!

Kraden    : Who are you calling an old man!? You're no spring chicken yourself!



     -(No)
Poi       : You are quite mistaken... You should listen to the old man.
            He speaks wisely.

Kraden    : Tha--HEY! Who are you calling an old man? You're no schoolboy
            yourself!
-----------------------------------------------------------

Poi       : I wondered if it would be right to allow an outsider to use this
            power...

Kraden    : You're... not going to teach us?

Poi       : But I like you, so I will let you learn our secret. Please,
            follow me.

* - Poi and Felix's group climb the rope to the ledge. A stone rests on a
    pedestal.

Poi       :{S} Take the power of Lash. It is yours now.

           {M} Ho ho! I feel the strength of your spirit flowing toward me!
               Splendid!

* - Examining the stone on the pedestal:

Poi       : This is the power and the secret of our temple! If you are worthy,
            you will use it with ease! When you see a rope, use Lash on it...
            perhaps you will find this useful on your travels. Take this power
            with you, and do good.

<game>    : Felix got the Lash Pebble.

Poi       : I hope that someday, my students will be worthy of this honor, too.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Gate ]
* - The two guards have left, as the meditation period has ended.





   [ Temple exterior ]
[001]     :{S} Someday, I'm going to be a great monk, like Master Poi.

           {M} Whenever the master goes to town, the villagers are all in such
               awe of him... Maybe someday, they'll look at me the same way.

[002]     :{S} Looks like none of our brothers passed this time, either.
               At this rate, maybe we'll be able to surpass them after all.

           {M} I've been meditating all day, but my body just doesn't want to
               float...

[003]     :{S} Hey, what's an outsider doing on the temple grounds? Oh,
               meditations must be over... That's why they let you in...

           {M} Gah! I kept my eyes shut in meditation so long that the sun hurts
               when I open them!





   [ Temple interior ]
[004]     :{S} You were the ones who passed the test?

               --------------------------------------------
                    -(Yes)
               Wow! I can't believe it! Are you monks? Where did you study?



                    -(No)
               Well, if it wasn't you, who was it?
               --------------------------------------------

           {M} The master seemed so disappointed that someone passed the test...
               I think it was just that none of his students can do it yet...

[005]     :{S} I hear that someone passed the test... No matter, though...
               I am here to improve myself, to mediate... Not to show off.

           {M} I knew it! It should have been me taking that test!

[006]     :{S} When I awoke, I learned that someone else had passed my test...
               How disgraceful.

           {M} Before I passed out, I saw... something... Some sort of...
               cute little monster. Was I delirious?

                 * - He is referring to Fog, a Mercury Djinni.

Poi       :{S} If you wish to practice, these caves may hold a place of interest
               to you...

           {M} Ho ho! I feel the strength of your spirit flowing toward me!
               Splendid!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'04] ---           [Indra]           --- [02'04] #$#
#$#$#              Shrine of the Sea God              #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

Riki      : All right! I'm gonna throw the rope again!

* - Tavi and Riki are standing on two different ledges, separated by a stream.

Tavi      : Just don't miss this time!

* - Riki throws it.

Tavi      : Aww, no! You missed again!

Riki      : Sorry, Tavi... I can't do it!

Tavi      : I thought I got lucky when that wave carried me up here...

Riki      : What are you, crazy? It knocked you stupid for a good ten minutes!

Tavi      : Yeah, yeah! Just find some way to get me down from here!

Riki      : Fine! Just don't jump down or do anything dumb, OK?

* - Riki goes to another area.





Riki      :{S} Wah! You scared me! I thought you were one of the grown-ups from
               Daila... So, who are you? Look, I'm kinda busy trying to help my
               pal Tavi right now, OK?

           {M} I can't find anything around here that'll help get him down from
               there!





* - Felix can use Lash on the rope to tie it to the stake on the other ledge.

Kraden    : Excellent work, Felix!

Tavi      : Hey, the rope! Awesome, Riki! Way to go!

* - He climbs down the rope. As he examines Felix's group:

Tavi      : Who are you?

Kraden    : We're just passing through.

Tavi      : How come you threw me the rope?

Kraden    : We'd heard that you needed some assistance.

Tavi      : Well, whatever. Thanks anyway.

* - Riki returns.

Riki      : Hey, Tavi! How'd ya get down from there?

Tavi      : These guys threw me the rope...

Riki      : Really? These grown-ups? Well, whatever. Now we can go nab that
            critter we saw!

* - He is referring to Breath, a Jupiter Djinni. Tavi pauses.

Riki      : What? What is it?

Tavi      : That little guy's so fast, I can't catch him!

Riki      : Do you think we could catch him together?

Tavi      : Well, yeah, except that every time I'm about to grab him, he flies
            off!

Riki      : So I guess it wouldn't matter if we worked together or not.

Tavi      : Yeah, I guess not.

Riki      : Well, that's too bad.

Tavi      : Hey, I'm really hungry! I haven't eaten since before I got stuck!

Riki      : Yeah, same here... My stomach's growling up a storm!

Tavi      : Let's go home, Riki.

Riki      : Sounds good, Tavi.

* - They depart.

Kraden    : They're gone... Well, it was good of you to help them. We should be
            going, too.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'05] ---           [Indra]           --- [02'05] #$#
#$#$#                      Daila                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Mayor's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - Alex comes out.

Alex      : Felix... Well, well... Our happy little family is back together
            again.

Jenna     : Alex... Where did you go?

Alex      : To look for a ship, of course.

Sheba     : That's what Kraden said...

Kraden    : And did you find one?

Alex      : Unfortunately, there are none to be had. I spoke to the mayor, and
            he suggested that we try the large town south of us.

Kraden    : Is that where you're going?

Alex      : Yes. Madra may have boats available. That would be the most logical
            move.

Jenna     : So what do you think? Should we go to Madra with Alex?

-----------------------------------------------------------
     -(Yes)
Alex      : Ah... You... want to travel with me?

Jenna     : What, you don't like that idea?



     -(No)
Alex      : Ah. Felix doesn't think it's a good idea.

Jenna     : You seem awfully pleased about that...
-----------------------------------------------------------

Alex      : No, that's not it. I'm just... preoccupied.

Sheba     : Self-absorbed is more like it!

Alex      : I simply prefer to work alone.

Kraden    : If that's the case, we'll let you be...

Alex      : Perhaps you will see me in Madra...

* - Alex departs.

Jenna     : Gah! The nerve of that guy!

Sheba     : Yeah, I know... Now, I just want to find a boat before he does!

Kraden    : Let's be on our way.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} After that wave hit, I was worried about Daila, but we're pulling
               through...

           {M} Thank our lucky stars our little town survived that ordeal.

[002]     :{S} Those puddles of seawater the wave left have almost all
               evaporated now.

           {M} Those puddles stank! I thought I'd get sick from the smell of
               stagnant brine!

[003]     :{S} It was creepy--right before the wave hit, the water got all
               quiet and calm. I don't know how to explain it, but it was
               really creepy.

           {M} Before the wave hit, the tide went way out... It was like the sea
               had been drained away...

[004]     :{S} Sure are a lot of travelers coming through here today. That last
               one, though... He was awful cute.

           {M} Is that guy still meeting with the mayor?

[005]     :{S} Ah, the sea is calm again, and we can all get back to our normal
               lives.

           {M} I'm glad everything is back to normal here in Daila...

[Item]    :{S} Tavi and Riki are back home, safe and sound... They stopped by
               to say hello on their way... What nice kids.

           {M} I hope their parents didn't punish them too severely... They must
               have worried their parents half to death!

[006]     :{S} The dread pirate Briggs was captured in Madra... If that guy
               were free, you could bet he'd be coming after our village...

           {M} I wonder what happened to Briggs when they caught him...

[007]     :{S} Those two losers are back home now, eating their snacks...

           {M} Tavi and Riki must have been starving. They were gone for days...

[008]     :{S} So... I hear they caught the pirate Briggs down in Madra...
               The seas should be safe now. Makes me with I still had a boat...

           {M} The seas are peaceful and free of pirates at last, and I don't
               even have a boat. Life's funny like that.

[009]     :{S} I bet you thought it was the wave that knocked me over and hurt
               my hip, huh?

               --------------------------------------------
                    -(Yes)
               It'd take more than a little water to knock this old-timer down!
               No, it was the earthquake afterward that made me fall on my
               tush...



                    -(No)
               Nobody believes me when I tell them the continent moved... Why do
               you think I fell? The ground shifts, you fall on your fanny!
               It's a fact!
               --------------------------------------------

           {M} Nobody believes a wave could be big enough to move a continent...
               I'm starting to think it's a sign of things to come, personally..

[010]     :{S} I thought I saw something when those puddles dried. Maybe it was
               just my eyes.

           {M} It's probably nothing but junk and garbage, but it's not my
               problem...

[011]     :{S} I got hurt when I was playing in the puddles, so not I'm not.

           {M} I caught my foot on something that was in one of those dried-up
               puddles.

[012]     :{S} The puddles are gone, and now I'm bored.

           {M} I hope some of the little puddles stay, at least.

[013]     :{S} I've always heard that the Shrine of the Sea God holds an
               amazing treasure...

           {M} I'd sure like to see what that treasure is...





   [ Buildings ]
* - Riki's residence:

Riki      :{S} Mmm... Mmnph... Dad was SO mad that we were late... He said,
               "No dinner for you!" And I was like, "Whatever!"

                 * - He appears to be eating something.

           {M} I still want to catch that monster. We are SO going back there
               tomorrow.

[014]     :{S} Let me tell you, kids are a lot of work... If they're not
               getting in trouble, they're inside, and they're eating!

           {M} Darn that Riki! Ah... I'm glad he's home, though... He's so cute
               when he's stuffing his face.

[015]     :{S} Who stays outside until he's absolutely famished? And would it
               have hurt to let us know where he was going!?

           {M} Hee hee. My little Riki is mommy's little monster! Just look
               how he eats!

-----
* - Tavi's residence:

Tavi      :{S} Mmmph... Mmmm. Don't tell anyone we were in the Shrine of the
               Sea God.

                 * - He appears to be eating something.

           {M} I'm sure glad I made it down from that cliff... I could have
               starved up there!

[016]     :{S} Our little one is finally home. I don't know where he got to
               for all that time.

           {M} I guess Riki next door made it home, too. Those two are just
               inseparable.

[017]     :{S} Tavi wolfed down his snack and just asked for more! He must
               think we're here to feed him, I swear!

           {M} Once Tavi finishes eating, I'm putting him right outside again!

-----

G. Healer :{S} There is nothing left for you in Daila... Please be careful on
               your journey to Madra.

           {M} Daila's probably pretty boring for travelers.

-----
* - Innkeeper2 and a new woman ([025]) are practicing a dance here.

Innkeeper1:{S} Our fishermen still can't head out to sea... When will they
               start fixing all those boats!?

           {M} Until we get our seafood back, we have to put on these shows
               for guests... My feet hurt... I wonder if they'll let me skip
               tonight's performance...

Innkeeper2:{S} Oh, I was just practicing. It's part of our dinner show for
               guests... You know, because we don't actually have any food
               for dinner...

           {M} Shoot... What was my first line? "Welcome to the Palace of the
               Dragon King"?

[018]     :{S} When do we get to sample some of Daila's famous seafood?

           {M} I just hope they don't make us watch another one of those
               awful shows! I'd rather eat a pile of steamed cabbage than
               watch them again!

[019]     :{S} I'm sick of eating nothing but vegetables... And the service
               stinks! At least there's a show. I wonder what we'll see
               tonight...

           {M} Maybe I'll just get up on stage and do a little dance of my own
               tonight.

[025]     :{S} Er... Aheh heh... You... weren't watching, were you? I was just
               practicing for the show we're putting on tonight.

           {M} Putting on shows instead of serving good food is fine, I guess...
               But won't stories about sea dragons make people think about
               seafood?

-----

[020]     :{S} Are you going to Madra?

               --------------------------------------------
                    -(Yes)
               You'll have to cross the Dehkan Plateau... It's a dangerous
               place. You'll want to be very, very careful out there.



                    -(No)
               Walking into trouble just for a boat ain't exactly smart...
               But sometimes, you have to face danger to move forward.
               --------------------------------------------

           {M} Daila got hit pretty hard. I wonder how Madra is doing...

[021]     :{S} I think Madra is east of the crossroads... I think....

           {M} Someone should see how the road to Madra held up in the quake...

-----

[Weapon]  :{S} Way back when, Daila used to be a hideout for a band of pirates..
               They were all captured, but no one ever found their stolen
               treasure.

           {M} This town may be dirt-poor, but we still get a good variety of
               travelers. They're searching for treasure, I'll bet. I hear
               even Briggs was after it!

[Armor]   :{S} We don't have a lot of people in Daila, but it's a very spacious
               town... The layout confuses me sometimes!

           {M} Maybe they hid treasure here because this town is so mazelike...

-----

Mayor     :{S} Don't tell me you're all looking for a boat, too!

               --------------------------------------------
                    -(Yes)
               Look, there aren't any boats here, not for you or anyone!
               Try Madra, down south!



                    -(No)
               If I had one, I'd let you use it, but I don't.
               --------------------------------------------

           {M} He said he'd pay me a fortune for a boat. I'm not sure he'd pay
               me even if I'd had one, though...

[022]     :{S} It's too dangerous to go to Madra now. I wonder if that man who
               wanted the boat will survive on the Dehkan Plateau.

           {M} The road to Madra goes through the Dehkan Plateau. It's nearly
               impossible to cross over that soft, crumbly soil right now.

[023]     :{S} Who was that guy? I wonder why he needed a boat so badly.

           {M} Maybe that guy washed up on shore when the wave hit...

[024]     :{S} Why did the pirate Briggs plague us for so long? If I were
               going to Madra, I'd go look him in the eyes and ask him!

           {M} Briggs probably has lots of men under him... If I lived in Madra,
               I'd be more worried about them coming to rescue him.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'06] ---           [Indra]           --- [02'06] #$#
#$#$#                 East Indra Shore                #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

Kraden    : Look... It's Menardi's ship!

Jenna     : It doesn't look like they sailed it here, though...

Sheba     : Of course not... They were killed at the lighthouse, weren't they?

Kraden    : Do you think it could have drifted here?

-----------------------------------------------------------
     -(Yes)
Kraden    : Yes, Felix, That [sic] would be logical...



     -(No)
Kraden    : How else could it have come to be here, Felix?
-----------------------------------------------------------

Jenna     : If we had that thingie Saturos had, we could just take their boat.

Sheba     : For all we know, the orb is at the bottom of the sea... with them...

Kraden    : Well, there's no point in hanging around here all day. Let's go
            see about finding ourselves a ship we can use.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'07] ---           [Indra]           --- [02'07] #$#
#$#$#                      Madra                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Town entrance  #$
#$#$#$#$#$#$#$#$#$#$#

Guard 1   : You there! Hold your ground!

Kraden    : What seems to be the trouble?

Guard 2   : Just wait there...

* - Guard 1 examines Felix's group.

Guard 1   : They don't look like they're Champa...

Guard 2   : I agree.

Guard 1   : Sorry for the delay. You may pass.

Kraden    : What were you checking us for?

Guard 2   : Our town was sacked by pirates...

Guard 1   : They'd come to free their leader, Briggs. They came from the east,
            a small party, and we repelled them with ease...But then, foreigners
            struck from the west, exploiting a weak point near our prison.

Guard 2   : That's over now, though... Feel free to relax and enjoy your time
            here safely.


#$#$#$#$#$#$#$
$#  Prison  #$
#$#$#$#$#$#$#$

* - Two men are speaking with another man named Piers, who is locked in a cell.

Man 1     : Admit it! You're one of the Champa, aren't you, Piers?

Shin      : Speak! Or let your silence condemn you!

Piers     : I told you already... I'm not a Champa.

Shin      : Then where did you come from?

Piers     : The heart of the Eastern Sea... If I told you where, you'd never
            believe me.

Shin      : Look at me when I'm talking to you! Are you trying to mock me!?

Piers     : I implore you, do not anger me.

Shin      : Oh, do you? So what's going to happen if I make you angry?

Man 1     : Hey, Shin... Maybe we should go easy on him.

Shin      : Hey, it wasn't your girlfriend who got hurt!

Piers     : I'm sorry she was injured, but I cannot--

Shin      : I don't want your sympathy, freak! I want you to get angry for me!

Piers     : Stop, please... Even my patience has its limits.

* - Shin turns to Man 1.

Shin      : Hey, don't you want to see what he'll do?

Man 1     : I think we should just stop...

Piers     : If my words will not cool your temper, then...

* - Piers uses the Psynergy "Frost", which turns a small puddle of water below
    Shin into a large pillar of ice.

Kraden    : Oh! That was Psynergy!

* - Shin falls off the pillar. He pauses, and then...

Shin      : Waaaaaaaaaahh!

* - ...scurries out the door.

Man 1     : Did you do that?

Piers     : What did your friend expect?

Man 1     : You monster!

Piers     : I... I am no monster.

* - Man 1 backs up.

Man 1     : Help!!!

* - He takes off running. Kraden turns to Felix.

Kraden    : This man... He must be an Adept!

-----------------------------------------------------------
     -(Yes)
Kraden    : Of course! That was clearly Psynergy he used...



     -(No)
Kraden    : You're right... We only know what we just saw.
-----------------------------------------------------------

Kraden    : Perhaps we should try to learn a little more about him.






* - Piers:

Piers     :{S} Ah... When will that kindly elder return and end my imprisonment?
               I have no time to wait, but I don't want to have to hurt
               anyone...

           {M} Why did I use my Psynergy in anger? I must maintain control...
               My actions should never cause regret-- I... sense someone...
               using Psynergy... That person... Could he be--no, he is not of
               my people... When will I be freed?





* - Upon exiting the prison:

Elder Dau : Has Piers escaped!?

* - The elder's daughter and a man appear. They enter the prison.

Elder Dau : Oh, I'm so relieved... So Piers hasn't escaped?

Man 2     : If he had escaped, the elder would no longer be able to protect him.

Elder Dau : But... from the look of things, it seems there was a scuffle...

* - The man nods.

Man 2     : The cell is in disarray...

Elder Dau : What happened in there, I wonder?

Man 2     : It seems Piers is a man of many mysteries.

Elder Dau : Not the least of which being that boat he arrived in...

* - She notices Felix's group.

Elder Dau : Oh, you there... You look like travelers.

Man 2     : Milady, now is not the time to be speaking with strangers!

Elder Dau : It's all right... This one has such kind eyes. When did you arrive?
            And where are you going?

Man 2     : My lady, please...

Elder Dau : Are you... going to Osenia?

-----------------------------------------------------------
     -(Yes)
Elder Dau : I knew it!



     -(No)
Elder Dau : No need to be shy, my friends.
-----------------------------------------------------------

* - She turns to the man.

Elder Dau : One requires permission to cross the bridge to Osenia, correct?

* - The man nods.

Elder Dau : Then I hereby grant my permission to these four travelers!
            Relay that message at once!

* - The man nods and takes his leave.

Elder Dau : You may all continue your journey and cross into Osenia.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
Guard 1   :{S} All of Indra shifted and collided with Osenia... Everyone's
               talking about it. As it dealing with invading pirate soldiers
               wasn't enough!

           {M} These are rough times... We don't have nearly enough people
               to help us.

Guard 2   :{S} There's no way those pirates are coming back... Not after Indra
               slammed into Osenia. I hear you can even walk there if you want.

           {M} It's so weird that we can just walk to Osenia now. Crazy,
               crazy world...

[001]     :{S} You picked the wrong time to come to Madra... We've had
               disasters, pirate attacks, all sorts of nonsense...

           {M} The town elder is getting pretty elderly. I hope he's OK?
               traveling out there...

[002]     :{S} Those Champa curs dug a hole here to sneak into Madra... And to
               think, it was just a decoy so they could break into the prison...
               What a crazy plan!

           {M} The Champa must have known exactly where Briggs was... But how
               did they know the layout of the town?

[003]     :{S} I doubt the Champa could have come up with that plan on their
               own... I'm not even sure that strange boat we found up north
               is even theirs...

           {M} It's not like the Champa to plan out elaborate strategies...
               I think the two raids were entirely coincidental.

[004]     :{S} The Champa were swarming over the village... But I screamed like
               the dickens and scared 'em off! It's true! Heh!

           {M} When I saw those Champa, I was so surprised that I let out a
               yelp... I must have startled them, because they all ran away!

[005]     :{S} Maybe we'll learn Briggs's whereabouts from that captured Champa.

           {M} That Champa in the cell looks a bit pale for a pirate...
               I thought pirates were supposed to be all tan and leathery...

[Weapon]  :{S} After the Champa opened the jail cells, they came over here...
               All of us merchants grabbed our own swords and started
               fighting...

           {M} The item vendor got wounded in the attack... She's still
               recovering. I don't think her boyfriend will ever forgive that
               man in the jail cell...

[Armor]   :{S} Ow. Ow. Ow... I think I got a bone bruise. I hate those...

           {M} Those lousy Champa... Next time I see them, they'll be the ones
               with the bruises!

[Item Sis]:{S} My sister was hurt when the Champa attacked... She's recovering,
               but I sure hope Shin gets the guy who did it.

           {M} Briggs and his men are horrid. Imagine, hitting a woman...
               When I think about it, I just get so angry!

[006]     :{S} That big wave moved the whole continent of Indra to the south.
               Now, we're sandwiched between the two continents of Gondowan
               and Osenia.

           {M} If a big wave can move the whole continent of Indra... Does that
               mean that all of Indra is just floating on the water?

[007]     :{S} It's like all three continents got together to form a
               supercontinent! [sic]

           {M} Now, Madra is pinned between two continents! People from Gondowan
               can walk here to visit! What fun!

[008]     :{S} If I could walk to Osenia, I'd like to see Air's Rock, out near
               Garoh.

           {M} I've always wanted to see Air's Rock... but Garoh is such a long
               way away...

[009]     :{S} Did you come here over the Dehkan Plateau? Yeah? You must have
               seen that boat grounded near the cave, right?

               --------------------------------------------
                    -(Yes)
               I hear it was a Champa boat! And on it, they found an unconscious
               Champa! So they nabbed him, of course, and they tossed him in our
               jail!



                    -(No)
               You didn't? Weird... I wonder if it drifted away...
               --------------------------------------------

           {M} Who was it who told me the Champa boat was damaged? Doesn't
               matter... But I bet Briggs went to Osenia to find himself a
               new boat.

[010]     :{S} Let me guess... You want a boat, right? Look, like I told that
               last guy, the tidal wave went and ruined all our boats!

           {M} It's a bit of a problem that the tidal wave destroyed our boats..
               But the tidal wave sort of solved the problem, too... Now,
               all three continents are wedged together, and we don't really
               need boats.

[011]     :{S} The town elder took off to deal with Briggs... I wonder where
               he is now.

           {M} Everyone thinks Briggs fled to the east after the breakout...
               I think that must be where the elder went with the others.

[012]     :{S} We took that unconscious guy from the boat and tossed him in
               jail. He keeps saying that he's not a Champa, though.

           {M} I looked into that man's eyes. He looked so serene and calm...
               No with such pretty eyes could be a liar.

[013]     :{S} I don't care what the elder says... That prisoner is filthy
               Champa scum! Until someone proves otherwise, I say, let him rot!

           {M} I'll never forgive those dogs for what they've done to our
               village.

* - Prison entrance:

Guard 3   :{S} My partner was guarding the prison... When the Champa attacked,
               he was so scared, he ran off. Disgraceful!

           {M} I miss my partner... It's a shame he turned tail and ran like
               that... But who knows? Maybe I would have done the same thing
               in his place.

Guard 4   :{S} My friend was on guard duty when Briggs's men attacked...
               Who would let a menace like Briggs go free?

           {M} I wonder how many of the raiders were actually Champa.


Man 1     :{S} Was I just dreaming when that shaft of ice appeared?

               --------------------------------------------
                    -(Yes)
               Yeah! That's what it was... It was all just a dream...



                    -(No)
               What!? Oh! Oh... You're just... You're joking with me, right?
               Yeah... joking...
               --------------------------------------------

           {M} It was all just a dream... If I keep on saying it, maybe I'll
               believe it...

Shin      :{S} Even if we tried to tell someone what we saw... Who would believe
               us!? I think I'll just guard him from out here, where it's safe.

           {M} My sore bottom tells me it was all real... But I'm not about to
               say that out loud...





   [ Buildings ]
Innkeeper1:{S} Earthquakes, pirate attacks... What a week!

           {M} The new land bridges between the continents should bring more
               business.

Innkeeper2:{S} Our inn is quite safe... The Champa themselves couldn't fight
               their way in!

           {M} Actually, I think it was just that the Champa knew we didn't
               have anything worth stealing. I wonder how they knew...

Employee  :{S} I hope those Champa don't come back for a rematch...

           {M} No one was safe from the Champa... not even innocent women!
               I should learn to defend myself!

[014]     :{S} I slept right through the pirate raid! It's too bad, too.
               I would have given those pirates the thumping of a lifetime!

           {M} I was hiding under my bed the whole time... But I'm not about
               to tell him that!

[015]     :{S} I'm glad my partner and I weren't injured when the Champa
               attacked.

           {M} We were fine because our karma is good. Only people with bad
               karma got hurt, I'll bet...

-----

[016]     :{S} Madra and Alhafra, off in Osenia, have a long history together...
               Alhafra's a thriving seaport, up on the northern coast.

           {M} Alhafra has long been a trade partner with Madra. I should go
               there one day... It's such an easy trip from North Osenia...

[017]     :{S} In all this chaos, everyone here has clean forgotten about
               Alhafra... Sure, it's all the way in Osenia, but they're bound to
               have a boat or two.

           {M} Wait a second...I'll bet Briggs is heading to Alhafra! Of course!
               That'd be the place to go if you were looking for a boat!

-----

[Item]    :{S}   * - She is lying in a bed.

               Ohh... Ohhh...

           {M} Eyes... Shining in the darkness... No! Go away!!!

-----

[018]     :{S} Everything happened so suddenly... The earth moved, and every-
               thing fell down... It's going to take me forever to clean up...

           {M} Everything's on the floor, and all my dishes are broken.
               What a chore!

[019]     :{S} A wave big enough to move a continent is a terrible portent...
               Could the legendary beast of the deep have awakened?

           {M} If the mythical sea creature has awakened, we're all in trouble..
               The legends say that only one armed with an enchanted trident
               can kill it.

-----

[020]     :{S} The boat that ran aground in the cove out east looks like a
               normal ship, almost... But I'm not sure a boat like that can
               even sail.

           {M} It didn't even have any oars! How does it move? I don't get it.

[021]     :{S} They say that boat belongs to the Champa... But I keep telling
               them, that boat looks like no Champa ship I've seen.

           {M} That boat's far sturdier and far more sleek than any Champa
               could build.

-----

Healer    :{S} Surely, this town is enduring some sort of test... We must
               not fail...

           {M} How could one explain a continent moving? Surely, it is the work
               of a greater power...

[022]     :{S} We must pass this test. Now is the time to be strong! Come,
               join hands, and let us give thanks.

           {M} If this is a test, please give us a sign. We are your flock...
               Do with us as you will...

[023]     :{S} A wave that moves the very earth... This is no act of man...
               But certain forces do move in mysterious ways...

           {M} The raid was just another part of the test. It must have been.

-----

[024]     :{S} Indra is in direct contact with southern Gondowan... Will it
               be safe?

               --------------------------------------------
                    -(Yes)
               You're just trying to make me feel better, but you don't have
               a clue, do you?



                    -(No)
               Listen, we don't need you running around getting folks worked up!
               Buzz off!
               --------------------------------------------

           {M} They say there are people who use a frightening kind of magic
               in Gondowan... I don't know if it's true, but it's absolutely
               terrifying!

[025]     :{S} The lands to the south of Gondowan are full of barbarians,
               I'm told.

           {M} The Kibombo are warlike, but they live far off in the center of
               Gondowan... I can't imagine they'd come all the way out here...

-----
* - Elder and mayor's residence:

    Note: The mayor is the elder's son.

Mayor Wife:{S} Milady and I have been told to guard that jewel on the mantel.

                 * - She is referring to the elder's daughter.

           {M} I wish I knew why the elder wanted us to protect this thing...

Elder Dau :{S} My father was opposed to arresting the man we found on the boat..
               But the townspeople were in an uproar about the Champa, and they
               locked him up.

           {M} Until my father returns, I'll protect this gem with my life.

Mayor Son :{S} Dad and Grandpa have gone to Osenia to look for Briggs...

           {M} If Dad has to fight, I wonder if he'll go...

Mayor Dau :{S} Whenever Dad goes on trips, he brings back presents! I wonder
               what he'll bring back this time...

           {M} I hope he brings me a nice doll. I want a wooden one!

Elder Wife:{S} When the elder gets back, I'm sure he will prove that young man
               innocent.

           {M} He intends to find Briggs and prove that young man's innocence.


* - When examining the jewel on the mantel, which bears a striking resemblance
    to the Black Orb that controls Babi's Lemurian ship:

Mayor Wife: Don't tough that gem! The elder gave us strict orders to protect it!





   [ Madra Catacombs ]
* - Before being examined by the guards, a man pops up from the hole outside of
    the town walls.

[026]     :{S} You comin' through here?

               -----------------------------------------------
                    -(Yes)
               Yeah, well... We're workin' in the hole right now, so...
               Until we're done here, you're gonna have to enter Madra
               through the gates.



                    -(No)
               That's good, 'cause we can't let anyone through right now.
               If you're goin' to Madra, you're gonna have to go through the
               front gates.
               -----------------------------------------------

           {M} The Champa dug this hole when they raided our town, but there's
               more to it... The hole they dug uncovered a cave that runs all
               the way under our town!

* - After being examined by the guards, the man goes further into the catacombs.

[026]     :{S} I can't believe the Champa just stumbled onto this cave accident-
               ally... That's like winning the lottery or something!

           {M} Who dug this cave? And why?

* - Near the other entrance to the catacombs:

[027]     :{S} I got someone to show me around inside... It's just a really
               big hole. Nobody could dig that much in such a short time without
               us noticing, you'd think...

           {M} I'm not sure the Champa actually dug this hole...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'08] ---           [Indra]           --- [02'08] #$#
#$#$#                Madra Drawbridge                 #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Without permission to cross  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Upon approaching the bridge:

Guard 2   : if you wanna cross here, you'll need permission from the town elder!

Guard 1   : Without permission, ain't no one's gonna cross this bridge,
            no matter what!





* - Social Script:

Guard 1   :{S} If you have permission, you can cross anytime. But try to cross
               illegally, and we'll throw you in the hoosegow with Mr. Bluehair!

           {M} I'm startin' to wonder when the elder and the others'll come back
               from Osenia.

Guard 2   :{S} You goin' to Osenia?

               --------------------------------------------
                    -(Yes)
               You'll have to head back to town and get a permit! Just go to the
               elder's house and ask real nice-like.



                    -(No)
               Then get lost, pal. These parts can be dangerous...
               --------------------------------------------
           {M} I wish I could tell 'em it's nothing personal... It's for their
               own good. Who knows what's waiting to gobble 'em up in Osenia!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  With permission to cross  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - Upon approaching the bridge:

Guard 2   : Yeah, we heard about you already. If you're going to Osenia,
            you'd better get moving.

Guard 1   : Alhafra is up along the northeast of Osenia... You'll see it
            eventually.





* - Social Script:

Guard 1   :{S} If you try heading straight through Osenia to Alhafra, you'll hit
               Yampi Desert. You'd be better off avoiding the desert and just
               following the coast to Alhafra instead.

           {M} These guys must be looking for trouble. Me, I'd rather stay home
               and relax. It's so pleasant and comfortable. And safe.

Guard 2   :{S} Head to Southeast Osenia, and you'll hit Mikasalla. It's a small
               village, though. Probably not much to interest you there.

           {M} Unless I had a boat, I wouldn't go to Osenia with permission or
               without.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'09] ---       [Indra / Osenia]      --- [02'09] #$#
#$#$#                  Osenia Cliffs                  #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - The wreckage of a ship floats in the waters here.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

[001]     :{S} This is a Champa boat...You can see their mark on the flag there.
               They must have been run aground here by the tidal wave.

           {M} I guess even if they did free Briggs... They wouldn't have been
               able to go back out to sea...

[002]     :{S} Look at all the damage... That wave must have been gigantic...
               I wonder how many Champa died in the wreck...

           {M} They still had enough men to dig that hole and attack Madra.
               And enough to form two attack parties, too...

[003]     :{S} Wait, if this is the Champa ship, then that must mean Piers
               isn't a Champa! So... why does the elder still need Briggs to
               clear his name?

           {M} Briggs must be trying to get a new ship in Alhafra. I hope the
               elder finds him first!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'10] ---          [Osenia]           --- [02'10] #$#
#$#$#                  Yampi Desert                   #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Due to a broken bridge, this is the only way to get to Alhafra.

    "M."   =  Madran
    "MEG"  =  Madran elder's group





[MEG#5]   : Can't we just forget about Briggs?

M. Elder  : No. I'm not about to quit looking for him. There must be some way
            through this desert! We must press onward! This is where my son
            must prove himself as mayor... So, Son. How are you planning to
            get us through this desert and on to Alhafra?





M. Elder  :{S} So, Son. How are you planning to get us through this desert and
               on to Alhafra?

           {M} My son is in quite a fix, but I'm not going to help him. Only by
               overcoming adversity can he ever hope to become a strong leader.

M. Mayor  :{S} Father, how am I supposed to get us through the desert?
               I think you're overestimating my abilities.

           {M} My father's always telling me to overcome adversity, but he
               never tells me how! I don't understand why we can't just go home
               and forget about Alhafra.

[MEG#3]   :{S} Ooooh... This desert... It's so hot out here! I feel dizzy!

           {M} Sure, it's hot. But it's a dry heat... and I can't stand it!
               I want to go somewhere cool and just relax!

[MEG#4]   :{S} Water... My throat is so parched! *Gasp!* ...It's no use...

           {M} There's a spring over there, but we can't reach it... I hear Fate
               mocking us.

[MEG#5]   :{S} As you can see, the elder is quite insistent on finding a way
               through. He feels the only way to Alhafra is through this
               desert...

           {M} We've reached a dead end... I just want to go home to Madra.

[MEG#6]   :{S} We followed the pirates here from Madra... Are you going to
               Alhafra, too?

               --------------------------------------------
                    -(Yes)
               I don't think you can get there through the desert...You probably
               should've crossed the bridge you passed on the way here.



                    -(No)
               You guys are lucky. We've gotta find some way through this
               desert.
               --------------------------------------------

           {M} Briggs and the Champa are nowhere to be seen.

[MEG#7]   :{S} If that accursed pirate Briggs hadn't smashed the bridge,
               we wouldn't be here! Maybe we won't find him, but I promise you
               Piers will pay the price for him!

           {M} That Piers is SO one of the Champa... We don't need Briggs to
               prove it. When we get back home, he's gonna pay for helping
               Briggs.





* - Upon traversing to the ledge above the group:

[MEG#7]   : Hey! Look! Up there! How did those guys get up there?

[MEG#4]   : Maybe there's path up ahead that we missed...

* - The mayor takes of running, looking for the path.

[MEG#7]   : Maybe... Maybe we can get through the desert after all!

[MEG#6]   : We can find a way through to Alhafra!

[MEG#3]   : I don't care where we go, as long as it's cool.

* - The mayor shouts from a bit away.

M. Mayor  : Hey! I found it! I found a way through!

* - The group heads towards the mayor's location. Following him, they manage to
    arrive at the oasis that they previously thought was unreachable.





M. Elder  :{S} My son... has passed his first test as mayor. I'll have to
               congratulate him. Eventually. Now, to see if his luck holds up.

           {M} Regardless of what happens next, know that you have done well,
               my son.

M. Mayor  :{S} If we remain here much longer, Briggs will be beyond our reach...
               We have to press on just a little farther...

           {M} Hooo... I can't believe we're going to all this trouble for a
               stranger... I'm still not convinced that Piers isn't one of
               Briggs's henchmen...

[MEG#3]   :{S} I'm just glad we're finally able to rest. It doesn't feel like
               my brain is on fire anymore...

           {M} Maybe we should have the mayor go on ahead while we rest here...

[MEG#4]   :{S} Oh, man! This is the best water I've ever tasted! Yowza!

           {M} I don't want to leave! At least let me fill up on water before
               we go.

[MEG#5]   :{S} Osenia is so much larger than I'd thought... I wonder how much
               farther it is to Alhafra.

           {M} How much longer will we be walking, anyway? I feel like we've
               walked off the edge of the world as it is...

[MEG#6]   :{S} At last, we can get through this accursed desert! Except that
               the elder and the others need to rest before we go.

           {M} Oh, not again! Don't tell me they want to rest again!

[MEG#7]   :{S} I was certain this was a dead end. What's wrong with this desert?
               This is only delaying Piers's punishment...

           {M} My job is to find evidence that Piers is a Champa. The elder is
               with us, so I wouldn't dream of lying...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'11] ---          [Osenia]           --- [02'11] #$#
#$#$#                     Alhafra                     #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

"M."   =  Madran
"MEG"  =  Madran elder's group
"A."   =  Alhafran


#$#$#$#$#$#$#$#$#$#$#
$#  Town entrance  #$
#$#$#$#$#$#$#$#$#$#$#

* - Shortly after Felix's group sets foot in town, [MEG#6] and [MEG#7] arrive.

[MEG#7]   : Finally! We made it!

[MEG#6]   : We-We're here?

* - [MEG#3] and [MEG#4] enter Alhafra.

[MEG#7]   : Where's the Elder?

[MEG#3]   : He's coming now...

* - [MEG#5] gets there first.

[MEG#5]   : Haaa hoo hooo... Are we... here? I fee like I just walked 500 miles.
            I'm fine... I feel like I could walk 500 more!

* - The Madran mayor and elder arrive.

M. Mayor  : So... is this Alhafra? Madra's a pretty big place, but this town
            is huge!

M. Elder  : We didn't come to Alhafra to shop, Mister Mayor. We're here to
            bring in Briggs the Champa.

M. Mayor  : I know that!

M. Elder  : Then we should go straight to speak with Alhafra's mayor.

[MEG#7]   : We're in no shape to go present ourselves to the mayor right now!

* - [MEG#6] looks around.

[MEG#6]   : Look, Briggs is obviously not here, and besides, we already know
            Piers is--

M. Elder  : Silence!

* - The elder notices damaged walls near the sea.

M. Elder  : It seems Alhafra has felt the effects of the tidal wave as well...

[MEG#3]   : It looks like they suffered a good deal of damage...

M. Elder  : That would explain why Alhafra doesn't seem to have any boats
            for sale, either!

[MEG#5]   : You know, just looking around, I get the impression they only had
            one boat to begin with!

M. Elder  : So if you really needed a boat, the only way to get one would be
            to steal it. Hmmm... But wouldn't that cause quite an uproar?

M. Mayor  : ...Which means the pirates must still be here, trying to get a boat!

[MEG#7]   : So, you think we've actually caught up with Briggs?

[MEG#6]   : No doubt about it!

M. Elder  : That's why I want to meet the mayor of Alhafra before the Champa
            steal a ship.

M. Mayor  : Oh yeah... I get it now. In that case, let's go see Alhafra's mayor
            right away.

* - A man walks by.

M. Mayor  : Um... Say, excuse me... Where would we find the mayor of Alhafra?

Man       : Uh...The mayor? Just keep going down this road. It's the last house.
            You can't miss it.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Path to mayor's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A pirate is hiding behind some of the trees here.

Pirate    : Ooo... This ain't good! That guy looked like the mayor of Madra...
            He must have come here looking for Briggs. I'd better go tell
            the others!

* - The pirate runs off if Felix is not in his way.

    If Felix is in a position such that the pirate bumps into him, then:

Pirate    : What's your problem? What are you, some kind of freak? Well? What!?
            You got a problem with me?

-----------------------------------------------------------
     -(Yes)
Pirate    : Ah, who cares what you think? I've got stuff to do, so scram, kid!



     -(No)
Pirate    : So where do you get off invading my personal space, huh?
            Scram, stinkbreath!
-----------------------------------------------------------

Pirate    : Where was I? Oh yeah, I was going to tell them about the mayor
            of Madra!

* - He departs.


#$#$#$#$#$#$#$#
$#  Inn, 2F  #$
#$#$#$#$#$#$#$#

Alex      : So, you've finally come. I had suspected we might run into each
            other again, since we both are looking for boats. Unfortunately,
            the only boat this town possesses has already been sold.

            I will be resting here in Alhafra a bit longer. I have traveled
            long and hard, and I am weary. Perhaps we can get along at least
            until we both depart.

* - Speaking to him again:

Alex      :{S} The broken mast on the ship they sold won't be easily fixed.
               That is, as long as we Adepts don't do anything about it.

           {M} Really, I do wish you would quit using your Mind Read on me...
               Trust me, my thoughts will become all too clear in due time...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Eastern Alhafra  -  Ship with broken mast  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - One of the ropes tied to the mast has caught on a stone pillar in the water.
    A large stone sits atop the tip of the mast.
    A wooden crate has fallen onto the sail.
    A wooden log sits partially on the boat and partially on the mast.

Pirate 1  : It's... It's no use! The mast just won't budge, no matter how many
            people we get to help us!

Pirate 3  : We're going to have to get all this junk off the mast first. If we
            could just get some decent footing, we could have this thing clear
            in no time!

Pirate 2  : There's more to it than that, though...

Pirate 4  : We still have to do something about that rope over there.

Pirate 3  : Untangling that'll be a piece of cake, once we get a boat we can
            use...

Pirate 1  : Oh, yeah... A piece of cake... Except for that huge rock over there!

Pirate 3  : Oh yeah... The rock...

Pirate 4  : How are we supposed to get the mast out from under that thing?
            It's huge!

Pirate 2  : There's no way we're gonna move it by ourselves...

Pirate 3  : Well, either way, we can't do anything until Zack finishes
            the canoe.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Welcome to Alhafra. This is the largest town in western Osenia...
               You can find anything you need here! ...Unless you need a boat,
               that is...

           {M} This guy's probably wondering about that boat sitting down at the
               pier... It still floats, but I don't think the thing can move...

[002]     :{S} A massive tidal wave hit us and destroyed every ship in Alhafra.

           {M} Losing out boats was awful... But I feel so bad for all the
               people whose houses were destroyed by the tidal wave.

[003]     :{S} Right after my boat got crushed, a group of men came by asking
               if I had one for sail. They were pretty swarthy, like they might
               have been sailors or something.

           {M} Those guys looking for a boat sure were in a hurry. I wonder
               why... Hey, at least I was able to unload that boat with the
               busted mast on them.

[004]     :{S} I hear the tidal wave knocked Indra into Osenia. Is that true?

               --------------------------------------------
                    -(Yes)
               Really? It's just so hard to believe, you know? Still, that would
               explain the massive jolt we felt right after the tidal wave hit.



                    -(No)
               I was hoping a traveler like you might have a better idea of
               what happened... Oh well...
               --------------------------------------------

           {M} I just can't believe a single tidal wave could cause an entire
               continent to move like that. But I used to be able to see Indra
               to the north of us, and it's definitely not there...

[005]     :{S} Those men didn't look like they were from Osenia... I wonder
               what business they have in Alhafra...

           {M} If this guy's looking to buy a boat, he's looking in the wrong
               town... I already sold the last boat in town, and it had a
               broken mast!

[006]     :{S} Those people that just came through looked totally exhausted.
               You don't suppose they passed through Yampi Desert to get here,
               do you?

           {M} Who would come to Alhafra across the Yampi Desert? It's way too
               dangerous! Anyone with half a brain would've just taken the
               bridge to the northwest...

* - [007] is guarding the entrance to a cave.

[007]     :{S} No one is allowed beyond this point. Don't even think about it.

           {M} The mayor said no one goes through, and I mean to make sure
               no one goes through!

[Armor]   :{S} That tidal wave may well wash out both my business and the
               weapon shopkeeper's!

           {M} It doesn't matter how well-crated a suit of armor is... If you
               soak it in seawater, it's junk. All my furs are ruined... All my
               steels is rusted. It's nothing but garbage now...

[Weapon]  :{S} We were hit by a wave so strong that it swept homes off their
               foundations! What's worse is, all my best weapons were washed
               out to sea!

           {M} Losing all my most expensive items may well ruin my business
               entirely...

[008]     :{S} Our port was ruined by the tidal wave, so kids aren't allowed
               there anymore... But all I want to do is just see what kind of
               wind is blowing in off the sea...

           {M} I don't know why they won't let us kids go down to see the dock..
               I wanna see what kind of damage the tidal wave did!

[009]     :{S} We've had a lot of strangers coming through here lately.

           {M} This tidal wave's actually been good for Alhafra. The town is
               bustling with activity... I think I'll steer clear of those
               swarthy men at the wharf, though... They're a scary lot!

[010]     :{S} Let me guess... You're here because you want to buy a canoe,
               right?

               --------------------------------------------
                    -(Yes)
               Sorry, but I'm totally backlogged with preorders. I'm gonna be
               up late finishing these as it is...



                    -(No)
               That's good, because I've got a ton of work to do already...
               And then I have to head down to the wharf and help clean up
               the wreck...
               --------------------------------------------

           {M} We can't raise the mast until we get rid of the debris. But I
               can't help get rid of the debris until I finish at least this
               one last canoe!

[011]     :{S} That boat at the wharf uses a sail, so it's more efficient than
               any galley. But since the mast is broken, it's not going any-
               where. What a waste.

           {M} I still can't believe those guys wanted to buy my busted boat!
               One man's junk...

[012]     :{S} Why would the mayor go and sell our boat to a bunch of
               foreigners? I know it's got a broken mast, but come on!

           {M} It may be newfangled, but it's no good if it's broken. Forget
               technology! I'm sticking with boats with oars! No masts for me!

[013]     :{S} The only boat spared by the tidal wave is that newfangled ship
               that catches wind in a sail... The thing is... the mast that
               holds up the sail got snapped apart!

           {M} I wonder if my partner has finished up that canoe yet...
               The sooner he finishes, the sooner we can clean things up
               down at the jetty.





   [ Mayor's residence ]
Guard 1   :{S} Listen, you look like an OK guy, and I'd love to let you through,
               but I just can't... I mean, if I let you in, then I'd have to let
               everyone in, right? I'm sorry, but it wouldn't be fair.

           {M} My partner's always in such a bad mood... Maybe I should
               bake him a cake...

Guard 2   :{S} Did you want to see the mayor?

               --------------------------------------------
                    -(Yes)
               Sorry, but he's meeting with some visitors from Madra right now..
               Maybe you can see him once he's finished with them.



                    -(No)
               The mayor is very open to meeting visitors, but he's in an
               important meeting now... So it's probably good that you're not
               here to see him...
               --------------------------------------------

           {M} I hate my job. I always have to be so tough and secretive
               around people. Deep down inside, all I really want to do is
               read them some of my poetry...





   [ Buildings ]
Innkeeper1:{S} Maybe you've noticed, but a lot of folk here lost their homes
               in the wave, but I don't mind them.

           {M} I never imagined anyone from Alhafra would ever stay at my inn.

Innkeeper2:{S} You see how full our inn is? You'd think we'd be making money
               hand over fist... But that's not true... We just don't have the
               heart to charge the people who lost their homes.

           {M} Perhaps the mayor will cover the cost of lodging everyone so we
               can feed them a decent meal. We're just trying to be helpful,
               but we're the ones who end up looking cheap.

Chef      :{S} The innkeeper told me to use only the cheapest ingredients to
               help save money.

           {M} I can't believe I'm only supposed to feed the villagers vegetable
               dishes.

[014]     :{S} The town ought to give money to all the people who suffered
               from the tidal wave... That way, maybe the innkeeper could afford
               to make us better food...

           {M} I bet the master of the inn could afford to give us better food
               than he's been giving us.

[015]     :{S} We're all guests in the same inn, so why is my meal so awful?
               At the very least, they should let us go back for seconds of
               that stinking slop!

           {M} I think I've lost weight form all these vegetables! Sure,
               I'm looking skinnier than ever, but something tells me this
               just isn't healthy.

[016]     :{S} I don't think I've had a bite of meat or fish ever since setting
               foot in this inn.

           {M} *Sniff sniff* That smell! That's the smell of fish... No!
               Now I'm drooling!

[017]     :{S} Ohhh... I'm hungry... My tummy hurts... When's dinnertime?

           {M} Maybe I'm just hungry, but everything they put in front of me
               looks delicious. I'm so hungry I could eat my own hand...

[018]     :{S} The innkeeper serves his paying guests better meals than we
               Alhafrans get. That's so cheap! I want gourmet meals, too!

           {M} Maybe it's 'cause all we've been eating is vegetables, but I
               just never seem to fill up.

[019]     :{S} I can't believe the innkeeper is renting out more rooms when
               we're as busy as this.

           {M} I can't believe the innkeeper is cramming all those poor people
               into that tiny room. He certainly can't badmouth the mayor...
               they're both stingy!

[020]     :{S} We all have to bear the discomfort of this place until our homes
               are repaired.

           {M} When you're living packed in together like this, you're bound to
               get on each other's nerves. I just hope everything goes back to
               normal once we move back into our own homes.

[021]     :{S} I heard there's only one person staying in the room next door.
               Can't they just move one more person into that room? Like me?

           {M} That warrior next door is so suave and handsome, just how I
               like 'em. I hope we can be friends.

[022]     :{S} I'll never forgive the mayor for failing to come to our aid
               when we were all suffering... I wonder what I can do to make
               him suffer...

           {M} I hope the mayor's treasure room doesn't run too close to the
               prison... If those thieves found out about it, they'd dig their
               way out in no time flat!

[023]     :{S} Our guests are very upset with the mayor. I just hope they don't
               do anything... rash...

           {M} I know our mayor's bad, but he wouldn't stoop to stealing from
               his own people, would he?

[024]     :{S} Why do we all have to be cooped up in such a small room? How am I
               supposed to sleep with Grandpa grinding his teeth all night?

           {M} I think they put me next to Grandpa so they wouldn't have to
               listen to him grind his teeth.

[025]     :{S} My pop's been lookin' around, an' he says the mayor keeps all his
               treasure underground. He says it's south of the palace, but
               that's all I know about it.

           {M} Everyone says the hill beneath the mayor's mansion is full of
               tunnels. I wonder if that's true.

-----

[026]     :{S} We're taking care of some people whose house was destroyed by
               the tidal wave. But... they're just so demanding! My wife feels
               so overwhelmed that she can't take it anymore!

           {M} I just wish that old man would stop pestering my wife all the
               time!

[027]     :{S} Augh! With all these demanding houseguests, I feel like I've
               lost control of my own house!

           {M} I don't mind helping people in need, but I won't be taken
               advantage of...



* - When speaking to [028] or [029] for the first time:

[028]     : Aren't you thirsty, my dear?

[029]     : Oh, you're right, dear. I am!

* - [028] approaches [027].

[028]     : Sorry to bother you, but we'd like some tea.

[027]     : Are you talking to me?! If you want tea, you can go right ahead
            and fix it yourself!



[028]     :{S} Well! I say! It seems the lady of the house is no lady at all!

           {M} All I ask is for a little tea, and that's the behavior i get!?
               I just want to get out of this inhospitable house and back into
               my own sweet home...

[029]     :{S} When we lost our house in the tidal wave, the master of this
               house offered his home to us. But living with another family
               isn't easy. Hahhh... They're absolutely exhausting!

           {M} Is this how a young bridge treats her husband these days?
               Back in my day, we were never like that!

-----

Healer    :{S} In the middle of Osenia, there's a terrible village where they
               worship a foul and vengeful god.

           {M} The people of Garoh brought the curse upon themselves for
               worshipping their wicked god...

-----

[Item]    :{S} Don't mention the tidal wave to the other merchants... It did a
               lot of damage, and we'd really just rather not talk about it,
               you know?

           {M} If all my goods were damaged by seawater, they'd be useless.
               I'd have to throw them all away... I'm lucky the wave missed
               my shop.

-----

[030]     :{S} Those guys who bought the boat looked kinda shabby... But I hear
               they paid the mayor a whole wad of cash for it...

           {M} Why would anyone pay so much for a broken old boat? I know I
               shouldn't be so suspicious, but there's something odd about
               them...

[031]     :{S} I don't care if it WAS broken! The mayor shouldn't have up and
               sold the town's only boat!

           {M} I wonder if the mayor will use that money to repair our poor
               town...





   [ Alhafran Cave (prison) ]
Guard     :{S} Everything's so boring here... Why doesn't anybody do anything...
               criminal?

           {M} I don't know why there are so many outsiders in Alhafra now,
               but it's bound to mean trouble.





   [ Eastern Alhafra ]
Pirate 1  :{S} What's your problem? You're new in town, aren't you?

               --------------------------------------------
                    -(Yes)
               You're probably curious about this here ship, huh?


                   --(Yes)
               They call this a "sailing" ship... Wind is the only thing
               that'll make it move... Isn't that incredible?

                  ---(Yes)
               Yeah, well, think of how surprised we were to find that Alhafra
               had learned to build sailing ships! I suppose the age when anyone
               could sail the seas was bound to come someday.

                  ---(No)
               You kids today, with your "been there, done that" attitudes...
               It's a shame...


                   --(No)
               Masted ships like this were originally built by the Champa...
               Oh, forget it. It's lost on you.



                    -(No)
               Well, I've never seen you before, but whatever...
               --------------------------------------------

           {M} People call us Champa a seafaring people because we make sail-
               boats... And sure, maybe we do a little pillaging on the side...
               But now that Alhafra can build sailboats, Briggs's pirating days
               may be ending.

Pirate 2  :{S} We sent my pal into town to get some supplies, but he came back
               looking pale... He went straight down to talk to Briggs, and I
               haven't seen him since...

           {M} That lousy rat... If something happened back there, he should
               have told all of us! Now I can't stop worrying... What's taking
               him so long!?

Pirate 3  :{S} We paid big money for this ship. It's ours now, so don't you go
               cryin' about it.

           {M} I thought it would be easy to right the mast, but I think I must
               have been crazy....

Pirate 4  :{S} If we could just raise the mast, we could head back to Champa...

           {M} When I think about how long it will be until we go home, I miss
               Champa all the more. I'm just glad nobody in Champa knows we're
               pirates.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Eastern Alhafra  -  Below the ship's deck  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Briggs is speaking with a pirate within a room. From the hallway,
    Felix's group is able to eavesdrop.

Briggs    : The mayor of Madra? Here? You're certain? How did he know we came to
            Alhafra?

Pirate    : He knew we needed a ship, and he knew we went east. It seems pretty
            easy to me.

Briggs    : Arr... Well, yeah... When you put it that way, it does make sense...

Pirate    : He was looking to find the mayor of Alhafra...

Briggs    : He must be hoping the mayor will tell him where we are...

Pirate    : He'll probably tell the Alhafrans we're pirates, too, huh?

Briggs    : Pirates!? That seems a little unfair!

Pirate    : What do you mean? We... are pirates, aren't we? I mean, we've taken
            all sorts of stuff that didn't belong to us.

Briggs    : That's only because everyone in Champa would starve otherwise!
            We don't have any choice.

Pirate    : Ah...

Briggs    : And even then, it's never a lot.

Pirate    : Wha-What's not?

Briggs    : The stuff we take. We never take too much from any one town.

Pirate    : Yeah, I guess not...

Briggs    : And why do you think that is?

Pirate    : Er... Why?

Briggs    : Because you never can tell how these wealthy towns will react.
            It's too risky, right?

Pirate    : Hey, yeah! Which is why we didn't steal anything from Alhafra...

Briggs    : Right! That's why we avoid the risky towns and just take what we
            need from the others!

Pirate    : See? That's why you're our captain, Briggs! You've got brains
            coming out your ears!

Jenna     : Hmph! There's nothing brainy about that!

Briggs    : Did you hear that? It sounded like a girl! Who's out there!?

* - They go to the hallway.

Pirate    : What do you think you're doing?

Sheba     : Don't you know that someone has been falsely imprisoned for your
            crimes?

Briggs    : Er... What's your point?

Jenna     : You have to come with us and attest to that man's innocence!

Briggs    : And... why would I want to do something like that?

* - Jenna and Sheba turn to Kraden. With some hesitation, he forms a reply.

Kraden    : Oh-ho! I was hoping we could avoid any ugliness, but you leave us
            no choice! We'll bring you in against your will if we must, but
            either way, you're coming with us! Isn't that right, Felix?

-----------------------------------------------------------
     -(Yes)
Jenna     : Good for you! Let's teach these guys a lesson!



     -(No)
Jenna     : After what they've done? Come on, we need to make them fess up!
-----------------------------------------------------------

Pirate    : You don't stand a chance! We're hardened criminal types!
            We eat punks like you for breakfast!

Briggs    : Watch yourselves, you self-righteous little brats! You're the ones
            with a lesson to learn!





* - Briggs and the pirate engage Felix's group in combat. After the fight:

Jenna     : Well, that takes care of that!

Sheba     : And I'm willing to bet everyone Briggs has been harassing will be
            quite happy to hear it!

Kraden    : This should set everyone in Indra at ease... They all seemed to
            fear the pirate Briggs...

Briggs    : We lost... Even pirates have honor... I'll go quietly. I won't make
            a scene just because I lost... Go on... Hand us over to Madra or
            Alhafra or whoever...

Jenna     : Good... First off, you can tell the Madrans that the man called
            Piers is innocent.

Briggs    : Fine. So, what, I just have to say that Piers isn't one of my men?

-----------------------------------------------------------
     -(Yes)
Sheba     : That's right. You tell the Madrans that, and they can release
            their prisoner.



     -(No)
Sheba     : Saying Piers is innocent won't clear you of your own crimes...
-----------------------------------------------------------

Kraden    : We've secured Briggs's vow... We should take him to the Madrans...

* - A woman rushes in.

Chaucha   : Wait! Can't you find it in your hearts to forgive Briggs and
            his men?

Kraden    : And who are you?

Chaucha   : My name is Chaucha. I am Briggs's wife.

Jenna     : So you're a pirate, too?

Briggs    : No! Chaucha hasn't done a thing! Let her be!

Chaucha   : I know Briggs and his men have caused some great trouble with their
            piracy... And I know their crimes cannot be ignored...

Sheba     : If you know all that, then how can you ask us just to forgive him?

Chaucha   : The only reason Briggs became a pirate was to help the people of
            Champa. We Champa are a seafaring folk. Our livelihood depends
            entirely upon the sea. But in recent years, the sea has changed...
            We can't live the life we once could.

Briggs    : The oceans have warmed, and the fish have vanished from our waters.

Chaucha   : The soil in Champa is rocky and barren. No crops can grow there.

Kraden    : No crops? So you have no grains? And no meat? It sounds like life
            in Champa is hard...

Briggs    : It's not hard! It's unbearable! Our children can't eat! Our village
            is dying!

Chaucha   : These men promised to return with food enough for all our people,
            but they found none...

Jenna     : So you became pirates... thieves...

Sheba     : We don't know where Champa is...

Kraden    : It sits on the southeast corner of Angara...

Jenna     : Southeast Angara? Isn't that near Xian and Lama Temple?

Kraden    : You have a good memory! If you were to head south through the
            mountains, you'd find it.

Jenna     : That's so far away...

Briggs    : Well, yeah! You think we could be successful pirates so close
            to home?

Chaucha   : If they raided any towns near Champa, it would be obvious to all
            who the attackers were...

Briggs    : And no one back home could forgive me if they knew. Not even my
            grandmother...

M. Mayor  : But where does that leave us? Are we simply to accept your looting
            here on Indra?

* - The Madran mayor, elder, the Alhafran mayor, two guards and [MEG#7] have
    entered.

A. Mayor  : I'm shocked, I tell you. Shocked!

M. Elder  : What's so shocking?

A. Mayor  : It looks like they really are pirates, just like you said...

M. Mayor  : Mister Mayor, I am appalled that you could not take our word for it!

[MEG#7]   : He probably wouldn't even have believed we were from Madra if the
            mayor hadn't come!

A. Mayor  : Am I supposed to believe the accusations of a complete stranger?

[MEG#7]   : Is this your position, Mayor?

* - The Alhafran mayor nods.

A. Mayor  : How can I be expected to believe a tidal wave could wash Indra into
            Osenia? Or that a group of men could walk--on foot!--from Madra
            all the way to Alhafra?

M. Elder  : It sounds to me like you had forgotten about us altogether!

A. Mayor  : I'm not sure you remember the last time we met. Do you?

* - Neither the Madran elder or [MEG#7] seem to recall.

M. Mayor  : We met when I was just a child... It must have been more than
            ten years ago now...

A. Mayor  : Twenty years! It's been twenty years since I last saw you.

M. Elder  : Has it really been so long?

A. Mayor  : It's been quite a long time indeed!

[MEG#7]   : I guess we can't blame you for forgetting his face.

A. Mayor  : Don't be silly! I didn't forget his face! His face merely...changed!

Kraden    : Ahem! Forgive my interrupting your interruption, but... Would I be
            correct in assuming that I am speaking to the leaders of Madra and
            Alhafra?

M. Mayor  : You are correct! I am the mayor of Madra.

* - The Madran elder and Alhafran mayor start to speak at the same time.

M. Elder  : And I...
A. Mayor  : I am...

* - Speaking quietly, they work out an order.

A. Mayor  : I am the mayor of Alhafra.

M. Elder  : I am Madra's town elder.

[MEG#7]   : I am a close personal friend of Shin, whose lover was injured by
            the Champa!

Kraden    : I am the scholar Kraden.

* - Kraden turns to Felix.

Kraden    : He is Felix, the leader of our group.

Jenna     : I am Jenna, Felix's sister.

Sheba     : I am called Sheba. I come from the town of Lalivero.

Kraden    : Now, what errand has brought you all here?

* - The Madran and Alhafran mayors start to speak at the same time.

M. Mayor  : We came for Briggs...
A. Mayor  : The mayor of Madra claims--

* - The Alhafran mayor motions for the Madran mayor to continue.

M. Mayor  : We followed Briggs here from Madra. Of course, we have good reason
            to suspect them of being pirates.

* - Briggs and Chaucha seem a tad displeased by the descriptor.

A. Mayor  : Ahem! And I was honestly taken aback to hear a businessman being
            slandered! If they truly are pirates, then why would they go to
            the trouble of buying a ship from us?

M. Elder  : Because the very funds they used to purchase the ship were pillaged
            from our homes!

Briggs    : If the ship was bought with Madran gold, then it belongs to the
            Madrans! What do you say? If we give them the ship, will that fix
            everything?

M. Mayor  : Then where will you go?

Briggs    : I won't run, and I won't hide. ...Actually, I don't feel up for
            much of anything right now.

M. Elder  : Then you probably won't mind being locked up, will you?

Chaucha   : Briggs...

Briggs    : Don't worry, Chaucha! I'll be back! Take care of Eoleo!

* - Note: Eoleo is their child.

    Briggs turns to Felix's group.

Briggs    : Your strange powers surprised me, but even without them, you would
            have overwhelmed us.

* - Briggs and his men approach the mayors and the elder.

M. Mayor  : We'll be taking that boat, then.

Pirate 1  : You're taking our ship!? You're worse than we ever were!

Pirate 2  : Aren't you at least going to pay us for the boat!?

Briggs    : Quiet! All of you!

* - He turns back to the Madran mayor.

Briggs    : Do as you must, but I have one request... You have to let Chaucha
            and Eoleo stay in the boat until it's repaired.

* - The Madran mayor nods.

A. Mayor  : You haven't done Alhafra any harm, Briggs...

M. Elder  : At least keep him locked up until the boat is repaired...

* - The Alhafran mayor nods.

[MEG#7]   : And our prisoner, Piers... Is he one of your men?

Briggs    : I don't know any Piers! Sounds to me like you've made a pretty big
            mistake!

M. Elder  : See! It's just as I said! Piers is innocent! You must return to
            Madra and free him immediately!

[MEG#7]   : ...Me? What, alone?!?

M. Mayor  : Only two of us will remain here. You can return to Madra with
            the others.

[MEG#7]   : Understood! We'll return immediately!

* - He departs.

Guard 1   : Can you come with us? ...Please?

* - Briggs nods. The two guards lead him and his men away.

A. Mayor  : It looks like that wraps this whole mess up... Let us return to my
            mansion for a nice cup of tea...

* - The Alhafran mayor and the Madran elder begin to depart, but the mayor stops
    and turns back.

A. Mayor  : You say your name is Kraden?

* - Kraden nods.

A. Mayor  : Thank you very much for the help with Briggs. If you have time,
            please come see me at my mansion before you go... It's nothing
            special, but I would like to thank you for everything you've done.

* - He and the elder depart.

M. Mayor  : Why do I get the feeling the mayor of Alhafra prefers to deal with
            my father over me?

* - He turns to Felix's group.

M. Mayor  : Thank all of you very much. Due to your efforts, Piers is going to
            be released.

* - He examines the ship.

M. Mayor  : And now, this fine ship belongs to Madra. None of this would have
            come to pass were it not for you. Thank you. Unfortunately, I don't
            have any reward I can offer you here...

Kraden    : Oh, pish posh! We don't need any reward, do we, Felix?

-----------------------------------------------------------
     -(Yes)
M. Mayor  : Ha! Your honesty is refreshing, Felix!



     -(No)
M. Mayor  : That's as [sic] may be, but I still feel quite indebted to you.
-----------------------------------------------------------

M. Mayor  : So, what shall I do? I know... Come to Madra after our boat has been
            fixed and we've sailed home. We are still recovering from the
            effects of the tidal wave, so it won't be much... But we do want to
            give you some kind of reward. Well, shall we be going?

* - He departs.

Chaucha   : I see, so...

* - Felix's group turns to her.

Chaucha   : Oh! N-Nothing. Never mind... I do get to stay on the boat, right?
            At least until it's repaired? Yes. That's where I'll be if you
            need me. ...With Eoleo...

* - She departs.

Sheba     : I feel kind of bad for Chaucha.

Jenna     : What can we do about it? After all, she's the one married to a
            pirate.

Kraden    : So, what should we do now? I suggest that we try to find Piers.
            He could prove enlightening!

Sheba     : That's true... He seems to be a Water Adept. He might be able to
            tell us a little about these lands...

Jenna     : Do you think we should help them fix the boat?

Kraden    : Say, if we help with the boat, maybe they'll give us a ride back to
            Madra! Good idea!

Sheba     : What do you say, Felix?

-----------------------------------------------------------
     -(Yes)
Jenna     : All right! Let's go see what we can do to get this thing
            sailing again!



     -(No)
Jenna     : You're opposed to it? Well, since you seem to have your own ideas,
            let's get going!
-----------------------------------------------------------


#$#$#$#$#$#$#$#$#$#$#$#
$#  Eastern Alhafra  #$
#$#$#$#$#$#$#$#$#$#$#$#

Kraden    : You do plan to help with the mast, right?

Sheba     : Not even Briggs and his pirates could fix that mast. How are we
            supposed to?

Jenna     : They need our help... We at least have to try... Isn't that right,
            Felix?

* - Felix nods.

Kraden    : Well then, we'd better get right to it, hadn't we?





* - By the large stone atop the mast's tip:

Jenna     : I don't know what we're going to do about this rock... I think
            we've done all we can do here... Let's get going...





* - When heading off the ship after that prior comment:

Kraden    : Are you finished here, Felix?

-----------------------------------------------------------
     -(Yes)
Sheba     : Wait, you wanted to do this, and now you're telling me we should
            just give up?

Jenna     : I just don't see how much more help we can be here, Sheba.



     -(No)
Sheba     : Oh, don't be ridiculous! We've already done so much.

Jenna     : I know how you feel, but there's nothing else we can do right now.
-----------------------------------------------------------

Kraden    : So... Maybe we should start searching for another ship then...
            ...Not that I was planning on "borrowing" the Madran's ship!
            Although... I did plan on asking them if we could use it once we
            got back to Madra... But it doesn't look like the ship will be
            leaving anytime soon. So I think maybe we should just forget about
            that and start on our way again, Felix.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Alhafran Cave (prison)  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - Chaucha and Eoleo are visiting Briggs.

Guard     : You here to see Briggs?

Briggs    : Chaucha... It's good to see you. And you, too, Eoleo.

Eoleo     : Goo. Goo goo ga.

Chaucha   : How... is your cell? Is there anything I can do to make this easier
            on you?

Pirate 1  : I'm fine, Chaucha. My only complaint is that the food here is
            terrible.

Chaucha   : What!? Are they forcing you to eat this disgusting gruel?

Guard     : Now, wait a second... First of all, it's not disgusting. It's
            nutritious! And besides... You're IN JAIL! What did you expect,
            gourmet cuisine?

* - Eoleo tries lifting the cell's key from its table by using Psynergy.
    But his power is weak, and thus he is unable to succeed in his endeavor.
    Nevertheless, he continues trying.

    A pirate, who noticed Felix's presence, whispers something in Briggs's ear.

Briggs    : Eoleo!

* - Eoleo stops and looks at Briggs, who shakes his head disapprovingly.
    Eoleo, however, resumes his attempt.

Briggs    : Eoleo!

* - The child stops again.

Eoleo     : Hooo... Ahhh waaah... WAHHH!

Guard     : I don't know why he's crying! You're his mother! Can't you do
            something!?

Chaucha   : There there, Eoleo... What's the matter?

Eoleo     : Waa waa waa!

Chaucha   : Did the mean old guard frighten you?

Eoleo     : Waa waa...

Chaucha   : Don't let him bother you... He's just a big bully! Come on!
            Let's get you home!

Eoleo     : Waa waa...

* - Chaucha turns to the guard.

Chaucha   : We'll be back again later. Will that be all right?

Guard     : Yeah, yeah. That's fine.

* - She turns to Briggs.

Chaucha   : We'll come back soon, dear.

* - She and Eoleo depart.

    Using Mind Read on Briggs:

Briggs    : Felix has strange powers of his own, so we can't let him see what
            Eoleo can do. If he does, he might ruin our only chance to escape...


#$#$#$#$#$#$#$#
$#  Inn, 2F  #$
#$#$#$#$#$#$#$#

Alex      :{S} So, I hear you caught Briggs...

               --------------------------------------------
                    -(Yes)
               Mia, a young girl from my clan, was very kind, much like you
               are... Perhaps you should consider lending a hand to the mayor
               of Madra. He could use it...



                    -(No)
               You have no need to hide such fine exploits from me. Working hard
               for the benefit of others is quite noble. That's what Mia always
               said...
               --------------------------------------------

           {M} Feel free to help whomever you like if it truly makes you happy.
               Perhaps capturing Briggs marks the beginning of your dreams
               coming to fruition.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} We're all going to work together to rebuild the homes that were
               destroyed by the tidal wave. It may have hurt us, but if we put
               our backs into it, we can overcome this hardship.

           {M} It's so nice of everyone to chip in and help rebuild Alhafra.

[002]     :{S} Once things are back to normal, we're all going to build another
               sailboat. If we all work together, we'll have it done in no time!

           {M} Everyone in town is so much happier now that we've started
               rebuilding the town... I hope things stay this nice once all the
               work is done.

[003]     :{S} Everyone is talking about how you captured the pirates in the
               prison. Wow! Taking care of that salty bunch is something else!

           {M} Those pirates have the coolest outfits! Someday, I wanna be a
               pirate, so I can dress up all fancy like that!

[004]     :{S} So, the guys who bought the boat are the pirates who were
               terrorizing Madra?

           {M} You know, pirates who pay for stuff instead of stealing must be
               pretty weird pirates.

[005]     :{S} The mayor is the only one from Madra who stayed in town.
               They said something about freeing an innocent man...

                 * - The elder actually stayed as well.

           {M} I can't believe they left their mayor behind! Those Madrans are
               so coldhearted.


             * - After the Madran mayor departs:

           {S} I hear the mayor of Madra went back through the desert and home
               to Madra...

           {M} He seems like an honest, hardworking young man... nothing at all
               like our mayor.

[006]     :{S} The mayor of Madra apparently seized the boat from the pirates
               and plans to sail it back home. I think he's got quite a wait
               in store before that mast gets fixed.

           {M} If our mayor thinks I'm going to work on a boat for him, he's got
               another think [sic] coming. Madra's mayor can wait here forever
               for all I care.


             * - After the Madran mayor departs:
           {S} It looks like the mayor of Madra went home to fetch some workers
               for the boat...

           {M} I guess our mayor didn't even offer Madra any help at all...
               What a crummy thing to do.

[007]     :{S} No one is allowed beyond this point. Don't even think about it.

           {M} The mayor said no one goes through, and I mean to make sure
               no one goes through!


              * - After having given Large Bread to [017]:

            You're the one who gave my son some food, aren't you? Did you want
            to go see the cave?

            -----------------------------------------------
                 -(Yes)
            I'm only letting you pass because you did good by my son...

              * - He steps aside.

            I'm only letting you by so you can explore a little. Make sure you
            don't lay a hand on any of the mayor's treasure.



                 -(No)
            If you were up for a little spelunking, I'd be glad to let you pass.
            Oh well...
            -----------------------------------------------


           {S} I've heard that the deeper you go into the cave, the more
               dangerous it gets, so be wary.

           {M} Not that it matters. The door to the mayor's treasure room is
               locked, so they're not getting in.

[Weapon]  :{S} What? Briggs was the leader of a crew of pirates? Aw, but he was
               so nice!

           {M} Briggs was  very generous. He bought plenty of weapons.
               Wait a minute... I wonder what he was going to DO with all
               those weapons...

[Armor]   :{S} That group from Madra was incredibly lucky! They didn't do a
               thing, but they get a great boat because someone else caught
               Briggs.

           {M} Getting a boat for nothing seems like a pretty good deal to me...
               If you ignore the fact that that boat isn't going anywhere for
               a while.

[008]     :{S} I can help build houses, too. ...At least for a little while,
               right?

           {M} Helping people out feels really good.

[009]     :{S} I never thought a fine house could be crushed in the blink of
               an eye by plain old water. I guess that's what makes tidal waves
               true natural disasters.

           {M} You know, sitting here fixing houses really makes you think about
               how unsafe the sea is.

[010]     :{S} Once repairs are done here, we have to fix the bridge in the
               northwest of Osenia. I guess Briggs destroyed it. If you're going
               that way, I'd wait until the bridge is fixed.

           {M} I wonder if the crew from Madra went back through Yampi Desert...
               If they weren't in such a rush, they could just wait for the
               bridge to be fixed.

[011]     :{S} They told me they'd help get that mast fixed up. Would someone
               please explain to me why suddenly they all decided to fix houses
               instead?

           {M} It's strange... The quarters down in the belly of that ship
               feel pretty cramped... It seems like there should be a lot more
               space down there somewhere...

[012]     :{S} [012]:  What does a sailor like me know about building houses,
                       anyway?
               [009]:  Hey! You there! Sailor boy! Get back to work!
               [012]:  Hey! Give me a break! I'm on it!

           {M} Working on deck with the cool ocean breeze on your face feels
               great. Working on land doesn't.

[013]     :{S} We've put off fixing the boat for now so we can work on repairing
               the town first. Which is exactly the opposite of what the mayor
               of Alhafra said would happen.

           {M} The fact that Madra took our boat from us can't be sitting well
               with the mayor. That's probably why he put off fixing their mast.

[015]     :{S} I was afraid my house would never get repaired, but everything's
               fine now. With everyone working together, maybe our new houses
               will be a little sturdier.

           {M} You know, since we're rebuilding the house, maybe I'll ask for
               my own room!

[017]     :{S} I'm so hungry I can't even move...

           {M} I wish someone would just bring me some food...



              * - Upon giving the boy "Large Bread":

            Thanks, mister.

              * - <game>: The kid ate the bread.

            Oh, wow, I feel so much better! Look at how much energy I've got
            now! Geez, mister, I don't know how I can repay you... Wait, I've
            got it! Do you like... adventures?

            -----------------------------------------------
                 -(Yes)
            Then you totally have to go check out the caves under the mayor's
            mansion! Go find my dad... He's up along the path near there.
            The entrance is just past him.

              * - His father is [007].



                 -(No)
            Really? Wow... You're so boring. Well, if you change your mind,
            just let me know.

              * - When speaking to him again, he repeats his question.
            -----------------------------------------------



           {S} I'm feeling a lot better now thanks to you, mister. If you get
               any more food, could you bring it to me, too?

           {M} I wonder if I should have shared some with my sister.

                 * - His sister is [016].

[018]     :{S} Once they fix the old folks' home, it'll be our turn to get
               some repairs done. We're all doing our part to get things fixed,
               even if it's just a little cleaning up.

           {M} If we don't get out of this inn soon, I'll die of starvation!
               The sooner Dad gets the house fixed, the sooner I get a good
               meal!


* - Upon approaching the leftmost destroyed house of the bottom level:

[023]     : Why, look at this!

* - She finds some gold coins in a jar.

[022]     : Wow, honey! You found some gold coins!

[024]     : Way to go, Mom! So... How much did you find?

[023]     : Oh! Well, it's not too much... It's only 5 coins.

[024]     : That's great, though! We can use it to buy some food!

[025]     : I'm going to start looking, too!


* - After the above scene has occurred:

[022]     :{S} All my neighbors are going to work together to help rebuild
               my house. A friend in need really is a friend indeed!

           {M} Losing the lottery and being the last house to get fixed takes
               some pretty bad luck. At least no one is complaining about how
               bad our luck is... except me...

[023]     :{S} What a stroke of luck! Right when we really needed it, too!
               There might be more, so let's keep looking!

           {M} I thought the hard part of cleaning up would be fixing the
               houses... But that's a piece of cake next to having to pick up
               all these pots and jars...

[024]     :{S} My dad lost the draw, so our house is going to be the last one
               to get fixed...

           {M} All because of my dad's stupid luck, our house is the very last
               one fixed. Maybe he can make up for it by finding some cash.

[025]     :{S} I wonder if there's any more money hidden around here...
               Oh, and I'll help with the cleaning up, too!

           {M} I really shouldn't be peeking into other people's pots, should I?





   [ Buildings ]
Innkeeper1:{S} As soon as I'm done fixing up the inn, I'm going to give a hand
               in town.

           {M} Why do I have to work so hard? I'm tired, and I'm in terrible
               shape for my age.

Innkeeper2:{S} We're all taking turns helping out with the repairs in town.
               The lady hasn't ever had to work this hard before. I hope she's
               going to be all right.

           {M} I may not look very strong, but I know I can help out. I want to
               lend a hand.

Chef      :{S} Tonight's meal is chock-full of ingredients to restore strength
               and vitality. Manual labor requires a lot of energy, so you have
               to rejuvenate with a good meal!

           {M} I was told to use only the cheapest ingredients, but I actually
               bought only the best. I don't think I'll be telling the master of
               the inn about this.

[014]     :{S} Everyone's working so hard to restore this town to its previous
               splendor! I've been working all day, and I'm beat.

           {M} We heard a loud popping sound when we tried to hoist the mast...
               We thought we'd broken the mast, but it turns out it was just
               my spine...

* - [015] has gone outside.

[016]     :{S} Mom said we're gonna have a bigger house than before. I hope I
               get my own room.

           {M} Oh! If we get a bigger house, we can get all kinds of pets!

* - [017-018] have gone outside.

[019]     :{S} There's still plenty of work to do once all the construction is
               finished... It's going to be a long time before these houses feel
               livable again.

           {M} I wonder what our new houses will look like... I can't wait to
               see them.

[020]     :{S} My son has terrible luck... I think I passed my bad-luck genes
               on to him... At the very least, I hope my grandchildren end up
               with better luck than we had.

           {M} I guess I just don't have any faith in myself... I should go with
               my instincts, but I always change my mind at the last second.

[021]     :{S} The guy next to us is awfully handsome. He's just my type...

                 * - She is referring to Alex.

           {M} Our neighbor is so mellow. He never stresses out. Maybe that's
               why he's so lucky.

* - [022-025] have gone outside.

-----

[026]     :{S} We've all started working together to repair the house! Oooh...
               Not much longer, and then I can kick these folks out of my house!

           {M} Ahh... It's so relieving to see my wife smiling again. I don't
               think there will be any more arguments with our elderly guests...

[027]     :{S} Once my neighbors' house is repaired, my life can finally get
               back to normal.

           {M} It won't be long until our guests go back home... It's a lot of
               work to help a friend in need, but it does feel good to be nice.

[028]     :{S} Once everyone started working to rebuild the town, our hostess
               started being much nicer.

           {M} The lady of this house is so temperamental. She gets angry at the
               smallest things... It was just a little tomato juice. How was I
               supposed to know that was her wedding gown?

[029]     :{S} I wonder what happened that's making the lady of the house
               smile so much...

           {M} The lady of the house is so adorable when she's in a good mood.
               It would be nice if she were always in a good mood...

-----

Healer    :{S} Capturing the dreaded Briggs was a great deed. Allow me to
               thank you on behalf of my townsfolk.

           {M} I think this man might even be able to defeat the horrible
               werewolves...

-----

[Item]    :{S} The Madrans dropped in and stocked up on items. I guess they're
               traveling by way of Yampi, or they wouldn't have needed so many
               supplies.

           {M} The Madrans must have been in quite a hurry... They knew we were
               going to fix the bridge pretty soon.

-----

[030]     :{S} I thought it was weird that someone would pay that much for a
               broken ship... They probably had some secret plan to steal from
               us... That's why they were so quiet!

           {M} Those guys were just trying to win our trust so they could take
               advantage of us!

[031]     :{S} I'm amazed those guys who bought the ship were pirates...
               But then again, they didn't much look like your average run-of-
               the-mill merchants...

           {M} Pirates? Here in Alhafra? That's a scary thoughts. I'm so glad
               they were caught!





   [ Buildings  -  Mayor's residence ]
Guard 1   :{S} Oh, Felix! Go on in! The mayor's been looking forward to meeting
               with you.

           {M} The mayor was really impressed with these guys... He'll probably
               want them to stay in Alhafra... I hope he doesn't try to give
               Felix my job. I hate when he does that.

Guard 2   :{S} Ah! Felix! Welcome, welcome... Listen, sorry about all that
               "not letting you in" business before... Don't take it personally.

           {M} If I'd known Briggs was a pirate, I would have fought him myself.
               I never get to have any fun.

A. Mayor  : Briggs tells me there are huge towns on a continent that lies across
            the Eastern Sea. He tells me that, by trading with one another, all
            of these towns prosper and grow... I've made a decision...If Alhafra
            is to prosper, then we must trade, too! Trade and grow! I'm going to
            build an entire trade fleet and make lots of money! Still... there
            must be other pirates and freebooters still roaming the high seas.
            Felix, Briggs told me you and your friends fought with great
            strength. If you could lend me that strength, we would need not fear
            any pirates. So if you'd just be willing to help us out, our town
            could begin trading... and prospering... What do you say? Do we
            have a deal?

            --------------------------------------------
                 -(Yes)
            Great! Why don't you just stay here in Alhafra until we're ready
            for our first trade run?



                 -(No)
            Ah, such a pity that you don't see the potential of this partner-
            ship... I certainly hope you will reconsider... We stand to make
            a lot of money...
            --------------------------------------------


              * - After the above has been said:

           {S} I am planning a glorious new sailing ship so that we can begin
               trading immediately... I'm certain this will go well, and we will
               both become very, very wealthy indeed.

           {M} This is such a fantastic idea, and I'm the one who thought of
               it...So, naturally, it need only be me alone who profits from it.

Jiya      : I'm sure the mayor has his reasons for halting repairs on the
            sailboat... The mayors feels that Madra should only get back what
            was stolen from them. Nothing more. But now, it seems the Madrans
            are getting the better end of the deal... The mayor thinks it unfair
            that Madra should benefit while Alhafra suffers. That's why he's
            keeping the pirates' money and using it to repair Alhafra, not the
            boat. If Madra wants their boat fixed, then they can just pay us
            to have it fixed.


              * - After the above has been said:

           {S} The mayor won't help fix the boat until he feels he's getting a
               fair payment in exchange. If Madra's mayor wants the boat fixed,
               he's going to have to shell out more cash.

           {M} The mayor hates seeing anyone else make money, so I'm sure he'll
               make this tough on Madra. Heh heh heh... The mayor doesn't play
               fair.

[032]     :{S} What do you think of Alhafra? Have you taken a fancy to it?

               --------------------------------------------
                    -(Yes)
               Then you are welcome to stay and relax for as long as you please.
               I am sure our mayor will be happy to hear it.



                    -(No)
               Then why don't you follow your feet to the south? There are
               plenty of delights for warriors such as you in the middle of
               Osenia.
               --------------------------------------------

           {M} Why do they always tell me to send adventure-seekers to South
               Osenia? All you do is go to the desert and head south. Where's
               the adventure in that?

[033]     :{S} You should go to the watchtower and gaze southward. On a clear
               day you can see the most amazing view of Air's Rock from there.

           {M} There are numerous tales about that rocky peak we call Air's
               Rock. Air's Rock looks so odd that many people think there must
               be something in hiding there.

[034]     :{S} I've been saying Indra wasn't in the right place for some time
               now. Nobody would believe me until the mayor of Madra actually
               walked here!

           {M} I sat and gazed at that continent every day. I ought to know
               where that continent should and shouldn't be, I tell you!

[035]     :{S} Lookee here! Can't you see Air's Rock out there?

               --------------------------------------------
                    -(Yes)
               From here, it just looks like a regular old rock, but from up
               close, it's something else! The first thing you think when you
               see it is "Now that's one serious rock!"



                    -(No)
               Oh... I guess today is a bit cloudier than usual. Air's Rock
               has another name. They call it the Windy Peak. You almost never
               see clouds near it.
               --------------------------------------------

           {M} The longer I sit here gazing at Air's Rock, the more I grow to
               love it. All it takes is one glance, and you're convinced it
               holds some mystery deep within.

[036]     :{S} Our town was rife with pirates until just recently. Your efforts
               have removed a scourge from our town. We truly owe you our
               gratitude.

           {M} Those pirates never did us any harm, but that's because they were
               up to something.

[037]     :{S} The mountains to the east of Alhafra are the Balloo Range.
               They divide Osenia in two. And we call the area on the other side
               of the Balloo Range East Osenia.

           {M} There's no way to cross the Balloo Range from here. I've heard
               western Osenia is nothing compared to the frightful things found
               in the east.

M. Mayor  : Darn that mayor... I thought he'd get that mast fixed up for us
            right away... I'm starting to think the mayor of Alhafra never
            planned on repairing that boat at all! I was a fool to believe he
            would help us...


              * - After the above has been said:

           {S} I'm starting to think the mayor of Alhafra never planned on
               repairing that boat at all! I was a fool to believe he would
               help us...

           {M} If we leave the boat here and go home, the mayor of Alhafra
               keeps the boat AND the money. There must be a way to fix that
               boat without relying on Alhafra's help...

M. Elder  :{S} He's already been paid to fix the boat, but he says that was
               only while it was Briggs's. He probably expects us to pay for
               the repairs a second time... The greedy pig...

           {M} The money Briggs used to pay for that boat was stolen from our
               people... I don't think it's wrong for us to expect the mayor of
               Alhafra to honor his promise.





   [ Alhafran Cave (prison) ]
Guard     :{S} I've been WAY too busy ever since you captured Briggs and his
               pirate crew.

           {M} It's so boring here when there's no one to guard. I'm glad I've
               got some company.

Briggs    :{S} Oh, stopped by for a visit, did you?

               --------------------------------------------
                    -(Yes)
               I wish that I'd met you under different circumstances...If we had
               met out on the open seas, you would have seen a different man.



                    -(No)
               Ah, so you just came here to check up on us? Hah! Well, as you
               can see, we're not causing any trouble!
               --------------------------------------------

           {M} Felix has strange powers of his own, so we can't let him see
               what Eoleo can do. If he does, he might ruin our only chance
               to escape...

Pirate 1  :{S} I hate prison. The food is terrible. My bed is hard and lumpy...
               It's even worse than being a pirate was.

           {M} I'm not staying in this stupid cell forever. I'll get outta here
               one way or another!

Pirate 2  :{S} It sounds like the mayor of Alhafra lost interest in fixing
               that boat. I guess that means it will be a while before the mast
               gets raised again.

           {M} If they don't fix that boat, then it's not going anywhere. I bet
               Alhafra's greedy mayor doesn't like seeing Madra profit from all
               of this.

Pirate 3  :{S} Everything would have been fine if it hadn't been for you
               meddling kids!

           {M} Oh, what's that punk Felix doing again? I wish that trouble-
               maker'd just scram!

Pirate 4  :{S} I saw you staring at Eoleo...But you couldn't have figured out...
               N-No! Of course not! Nobody could see that.

           {M} I hear some people can see Eoleo's power... I want to see for
               myself! How does he do it?





   [ Eastern Alhafra  -  Below the ship's deck ]
* - When first speaking to Eoleo:

Eoleo     : Goo goo ga ga!

* - He uses his power to make a flower vase levitate.

Chaucha   : Eoleo's only just recently started doing that... After that gem
            fell from the sky and hit him. He was overcome by a terrible fever,
            and when he recovered, he had this power.



Chaucha   :{S} Eoleo and I are going to visit Briggs every day.

           {M} If Eoleo gets the hang of it, then maybe Briggs can...

Eoleo     :{S} Goo goo ga ga!

                 * - He uses his power to make a flower vase levitate.

           {M} I'm gonna use my magic to free Papa.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'12] ---          [Osenia]           --- [02'12] #$#
#$#$#                   Air's Rock                    #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#
$#  Outside  #$
#$#$#$#$#$#$#$#

Signpost  : Beware the Wind Stones. The stones magnify the power of the wind.
            Use caution when approaching Air's Rock.


#$#$#$#$#$#$#$#$#$
$#  Final area  #$
#$#$#$#$#$#$#$#$#$

<game>    : Felix checked the tablet. It has strange characters written on it.

            Wielder of Wind's might... Lay your hands upon this stone...
            We bestow upon thee the power to see the truth unclouded...

Sheba     : Do you think I ought to touch it?

* - Felix nods.

<game>    : Sheba touched the tablet.

* - It rises into the air, as does Sheba as the tablet's energy surrounds her.

<game>    : Sheba learned Reveal.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'13] ---          [Osenia]           --- [02'13] #$#
#$#$#                     Garoh                       #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Outside the village  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - At night, as Felix's group makes their way to Garoh...

?????     : Gaaaroooooo! Aow-aow-oooo!!!

Jenna     : What was that!?

?????     : Awoooooo!!!

* - A werewolf comes from the village.

Werewolf  : Awoooooo!!!

* - It observes the reflection of the full moon in a pond.

Werewolf  : Ah-ah-awoooo!!!

Sheba     : Eeek!

* - Alerted of the group's presence, the werewolf runs back to the village.

Kraden    : I don't believe it! Was that a--

Jenna     : A what? Kraden, do you know what that thing was?

Kraden    : Well... Perhaps...

Sheba     : So, what are you waiting for!? Tell us!

Kraden    : I suspect it may have been... a lycanthrope.

Jenna     : A lycanthwhat?

Kraden    : Just think of them as a race of people born with special powers...

Sheba     : Kind of like Adepts, you mean?

Kraden    : Yes, that sounds right. Sheba, you've put it quite well.
            Adepts borrow their abilities from the power of the elements...
            While lycanthropes borrow theirs from the power of beasts...
            This is why they take the forms of animals... They may look
            frightening... But we must try to communicate with them.

            Lycanthropes... Werewolves... A whole village in hiding...

Jenna     : Is it just me... Or does Kraden seem a little TOO happy to have
            found werewolves?

-----------------------------------------------------------
     -(Yes)
Kraden    : What? Me? Happy to find werewolves? You must be joking!



     -(No)
Kraden    : I would love to study them, but still... they do frighten me...
-----------------------------------------------------------

Kraden    : I guess I'm just curious about all the secrets of these new lands...

Jenna     : Any real scholar would be thrilled to explore a new land full of
            mystery, huh?

* - Kraden nods.

Sheba     : So, are there werewolves only on Osenia?

Kraden    : Ummm...

Sheba     : If so, how could you even have known about them, Kraden?

Kraden    : Er... I, uh...

Jenna     : Yeah... That is weird.

Kraden    : All right, so I lied! I'm glad we found werewolves! There!
            Are you happy!? And you know what!? I even want to get a closer look
            if I can! So let's go! Let's find us some werewolves!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

* - Those outside are wearing hooded cloaks.


   [ Outside ]
[001]     :{S} So, uh... you say you saw a werewolf?

               --------------------------------------------
                    -(Yes)
               Don't be ridiculous... There's no such thing as werewolves.



                    -(No)
               Of course not... You should know there's no such thing! Not here!
               --------------------------------------------

           {M} It's grim luck that brings strangers here in the gloom of the
               full moon.

[002]     :{S} Gaaaroooooo! Gah! Whoops... Heh heh hrrr... I was just calling
               my dog... Sounded good, huh?

           {M} Which one of us was it who removed his hood in front of these
               strangers?

[003]     :{S} You there... Strangers should not go about at night... Guests are
               welcome in Garoh, but they'd do well to stay in at night.

           {M} Foreigners only come here en route to Air's Rock... Only a chosen
               few can reach the peak.

[004]     :{S} Don't you love the sight of the full moon?

               --------------------------------------------
                    -(Yes)
               Yes, I agree... But it brings me grief. We here cannot enjoy
               the sight of it directly.



                    -(No)
               Heh hrr hrrr... Don't feel like you must watch your words on my
               account. The full moon's light gives birth to many strange sights
               on nights like this.
               --------------------------------------------

           {M} The night of the full moon is usually so festive... It's boring
               having to wear these hoods when strangers come...

[005]     :{S} Good evening. Forgive me for not taking my hood off... I just...
               don't care much for the full moon's light.

           {M} Such gorgeous moonlight... if only I could take off this hood...





   [ Buildings ]
[Weapon]  :{S} I'm sorry, but on nights of the full moon, we only sell
               claws and fangs. You... probably wouldn't have any use for those,
               would you?

           {M} I should be outside, howling with the pack, not stuck in here!

[Armor]   :{S} Unfortunate that you should come on a night of the full moon,
               sir... Come during the day to see our full range of wares...

           {M} These strangers seem normal enough... Except that they're up late
               for outsiders...

-----

[006]     :{S} Good evening, wanderers! Are you looking for something?

               --------------------------------------------
                    -(Yes)
               Searching for werewolves, eh?

                   --(Yes)
               You don't really believe they exist, do you? If so, you'd best
               keep it to yourself... That is, if you don't want to have folks
               here howling with laughter...

                   --(No)
               Hehrrr... sorry. Just thought I'd ask. We get some crazy folk
               coming through here, and I had to ask....



                    -(No)
               Just... staying up late, eh? Can't say I blame you, on a night
               like this. We here know the glory of night of [sic] the full
               moon.
               --------------------------------------------

           {M} Outsiders could never understand the gift the moon has given us..

[007]     :{S} Our oldest son is always scampering off late at night... Where
               is he?

           {M} That pup of mine just won't listen. He went otu when he
               shouldn't have... He just wanted to see the moonlight, and now
               his father blames me for it!

[008]     :{S} No fair! My brother always gets to go out late!

           {M} What made Master Maha take my brother into the rock? I want to
               see what's in there...

-----

Innkeeper1:{S} A clear night around here always mean fair weather on the
               morrow... You've come all this way, so you might as well go to
               Air's Rock, too...

           {M} It only rains a few times a year there... Air's Rock is in a
               desert, so what else would you expect?

Innkeeper2:{S} Air's Rock can get quite desolate. After all, it's in the middle
               of a desert...

           {M} Most people see nothing of the true Air's Rock. Our current
               guests saw only the wind and the dust...

* - The two guests are sleeping in bed.

[009]     :{S} Zzzz... Zzzz... What a waste... Just a big rock...

           {M} ...Climbed all over that stupid rock, and for what? Nothing!

[010]     :{S} Zzz... Whuzza? Whirlwind? Wind Stone? Zzzzrrrgg...

           {M} That rock was huge. How was I supposed to make it spin?

-----

Healer    :{S} The people here may be different, but they certainly are nice...
               And those abilities of theirs are amazing!

           {M} No matter what it takes, I will save the souls of those poor
               villagers...

-----

[011]     :{S} Garoh exists to protect Air's Rock... In exchange, we gain
               its power ourselves...

           {M} We have other powers than just Whirlwind... I wonder which of us
               will inherit the powers of Master Maha?

[012]     :{S} So you've heard of Whirlwind? Most people haven't... Even in
               Garoh, only a chosen few can use it.

           {M} And different people use Whirlwind different ways. Master Maha's
               mastery of Whirlwind would put anyone to shame.

[013]     :{S} I've heard about the Wind Stone... Using Whirlwind on it makes...
               something happen.

           {M} I wish I knew what would happen... Something weird, I guess.

-----

[Item]    :{S} Did you come here from Alhafra?

               --------------------------------------------
                    -(Yes)
               Really? You must have gone through the cave... You can't go back
               that way, you know... The return trip is longer.



                    -(No)
               Oh, so you must have come by way of Mikasalla. If you're going to
               Air's Rock, take the crossroads west of Alhafra.
               --------------------------------------------

           {M} I never change my stock, unlike the weapons and armor
               shopkeeps... [sic]

-----

[014]     :{S} When our people grow older, they generate strange powers...
               Of course, I'm just a wee pup, in people years...

           {M} I cast Whirlwind on the stone, like I was supposed to...
               So why didn't I gain the power that Maha wields?

[015]     :{S} My mate is close to obtaining the power he's been seeking...

           {M} If he succeeds and carries on Master Maha's traditions, I'll be
               so proud...


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Northeast of town  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - A boulder is located here. The lycanthrope named "Maha" emerges from
    the boulder by casting Reveal to unveil a hidden opening.

Maha      : What!? Outsiders, here?

* - He darts back inside. Reveal's effect wears off.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Cavern beneath the boulder  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - The lycanthrope from outside of the village is present.

Werewolf  : Haowooo!!! Aow-aow-oooo!!!

Kraden    : Look! It's that werewolf!

* - It runs away.

Kraden    : He was right there! Let's go find him, Felix!





* - Upon arriving at what would appear to be a dead end:

Kraden    : Felix, wait... Where could that werewolf have gone? Do you think we
            lost him somewhere?

-----------------------------------------------------------
     -(Yes)
Kraden    : That would be a shame...



     -(No)
Kraden    : I hope we didn't... Or rather, I'd be quite unhappy if we did...
-----------------------------------------------------------

Werewolf  : Grrrr...

Jenna     : What was that?

Sheba     : It sounded like a wolf growling, didn't it?

Kraden    : My hearing is not so very good, but... there was something.
            Perhaps we should search this area more thoroughly...

Maha      : There is no need...

* - Maha and the other lycanthrope emerge from another hidden opening.

Jenna     : Look... He's using Psynergy.

Werewolf  : Garrrrooow...

Maha      : Fear not... This child is harmless.

Sheba     : He does look kind of... small...

Werewolf  : Grrrrrrr...

Kraden    : Tell me, who are you? How did you come to be here?

Maha      : I should like to ask you the same question. Could it be? Do you
            outsiders possess the power to reveal the unseen?

-----------------------------------------------------------
     -(Yes)
Maha      : Of course... I was certain that you must.



     -(No)
Maha      : Impossible... Without Reveal, you could not have entered this cave.
-----------------------------------------------------------

Werewolf  : Grawooo...

Maha      : Yes, you are correct. They must have passed the challenge of
            Air's Rock.

Jenna     : Er... How come that kid doesn't talk, like you?

Maha      : When we become werewolves, speaking the human tongue becomes
            more difficult.

Sheba     : But you can... You must be someone special, then...

Maha      : Hurh hurr hrrr... "Special"? Perhaps. Why don't you just call me
            Maha... So... I assume you also can use Whirlwind... If you learned
            Reveal on Air's Rock, you must also know Reveal.

-----------------------------------------------------------
     -(Yes)
Jenna     : That's right... I think we can tell Maha that we're Adepts.



     -(No)
Jenna     : I don't think we need to hide the fact that we're Adepts from Maha..
-----------------------------------------------------------

Werewolf  : Awooo...

Sheba     : What did he say? I don't understand...

Maha      : He wanted to know what an Adept is... A question I would like
            answered as well.

Kraden    : Adepts tap the power of elemental energies to generate forces like
            Whirlwind...

Maha      : Elementals... You mean the four elements, the power of earth and
            fire, water and wind?

Kraden    : That is correct. These elements together comprise everything in
            our world...

Maha      : Interesting. Very interesting...

Werewolf  : Awooo...

Jenna     : Um... What did he say this time?

Maha      : He asked if there were no longer any need to hide from you...

Sheba     : ...Why did he have to hide in here in the first place?

Werewolf  : Aaah-Ah-Awoooh! Hawawoooh!

Kraden    : No doubt, most would find the sight of a werewolf rather unnerving..

Maha      : You are, sadly, correct. Many consider ours an accursed race.

Jenna     : And if they found you in your werewolf form?

Maha      : ...Once, our people were burned at the stake as abominations...
            They called this "purification."

Kraden    : Horrible...

* - The other werewolf approaches the others.

Sheba     : But... this little one... He won't get excited and try to bite,
            will he?

* - Maha turns to the other werewolf.

Maha      : Child, return to your home.

Werewolf  : Arrooo?

Maha      : Don't worry. We can trust them... Go back home now.

Werewolf  : Aarrrooo?

Maha      : They are Adepts, not unlike us werewolves... They guard an ancient
            secret. We can trust them. They will not betray us to the world.

* - The werewolf nods. He turns to Felix's group...

Werewolf  : Woof.

* - ...and departs.

Maha      : It has grown quite late. Why don't you go to the inn and rest...

Kraden    : But then...

Maha      : I will not leave this place.

Sheba     : You aren't going home?

Maha      : When I learned Reveal, I lost my human form. The wild is my home
            now.

Kraden    : So, Master Maha, you always look this way?

* - He nods.

Jenna     : And the little one?

Maha      : The child changed because he looked directly at the full moon.

Kraden    : So, by tomorrow morning, he will have returned to his human form
            again?

Maha      : Correct. Now, let us retire.


<game>    : Felix and party stayed the night at the inn.

Innkeeper2: You folks didn't sleep much last night... You don't look like you
            got any rest at all.

Innkeeper1: Master Maha told us all about you. Don't worry about the bill.
            It's on us. Farewell, friends.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Cavern beneath the boulder  -  Second visit  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

Maha      : Ah, you came. I've been waiting for you.

Kraden    : Would you mind telling me a little more about werewolves?

Maha      : You want to know the reason we possess the power to transform into
            beasts?

Kraden    : Ah... Well, I, er... Actually, yes.

Maha      : Do you find it strange that we can change our shapes?

Kraden    : Well, ummm... Yes.

Maha      : But surely changing one's shape is not really all that unusual.

Kraden    : What are you getting at?

Maha      : Think about the caterpillar for a moment. When the time is right,
            does it not transform into a beautiful butterfly?

Jenna     : Well, yes. It's only natural...

Maha      : And the pill bug and hedgehog? Do they not change their shapes
            to protect themselves?

Sheba     : I have heard of these creatures, yes...

Maha      : And many amphibians possess the power to change color at will,
            correct?

* - Felix nods.

Maha      : In light of all this, do you mean to tell me you find werewolves
            so abnormal?

Kraden    : Hrmm, well...To be honest, I hadn't thought of it that way before...

Maha      : Perhaps you simply did not give it enough thought.

Kraden    : How insulting! I, sir... am a SCIENTIST!

Maha      : Indeed! A scientist? That IS impressive. I have spent a great deal
            of time thinking about werewolves. For a time, I even felt cursed
            to have been born a werewolf... But after taking a more objective
            look at nature... I realized that weaker species have survived by
            evolving... by transforming. Don't you agree?

* - Everyone nods.

Maha      : Think about it for a moment. Without changing their bodies with
            weapons and armor... Humans would be very weak creatures indeed.
            I believe that evolving into werewolves is just one way for humanity
            to survive...

Kraden    : But that's...

Maha      : Of course, there's no way I can prove this theory. But I felt that
            our ability to use Whirlwind was evidence of this.

Sheba     : Whirlwind? Why?

Maha      : I had thought only the people of Garoh could use Whirlwind. It was a
            gift known only to werewolves, to Garoh's pack...

Kraden    : And that only a chosen few could use Reveal...

Maha      : But now I find that you, too, can use these...What does it all mean?
            Why are you able to use Whirlwind, and what is an Adept?

Kraden    : Master Maha, do you know of a continent called Angara? It lies far
            north of the Eastern Sea.

Maha      : Angara?

Kraden    : In the middle of Angara, there is a peak called Mt. Aleph.

Maha      : Mt. Aleph? ...Then it's true! Our legends say this peak has stood
            since this world began! If Mt. Aleph does exist, then perhaps our
            legends are true!

Kraden    : It does exist...

* - He turns to Felix and Jenna.

Kraden    : These two hail from the village at the base of Mt. Aleph, a village
            called Vale.

Maha      : They come from Mt. Aleph!? Incredible!

Kraden    : And they are both Adepts. And while their powers may vary...
            Everyone from Vale is an Adept to a certain degree.

Maha      : Then, does that not make them like us in Garoh?

Kraden    : In Vale, the myths say that Mt. Aleph itself gave birth to the
            Adepts...

Maha      : That is not what the legends of Garoh tell us...

Kraden    : As people, they are quite gifted... but it goes far beyond that...
            The mystical stones on Mt. Aleph... The Psynergy Stones... They are
            closely linked to the powers of the townsfolk.

Maha      : "Psynergy Stones," you say?

Kraden    : If there were similar stones in Garoh, it might explain your powers
            as well.

Maha      : And what manner of stones are these Psynergy Stones?

Jenna     : You've seen them, Maha! The shining stone at the heart of
            Air's Rock.

Maha      : I've seen the stone you speak of, but...

Kraden    : Air's Rock is quite far from Garoh.

Maha      : I don't see how it could affect the people here.

Sheba     : I wonder... Could it be the wind?

-----------------------------------------------------------
     -(Yes)
Sheba     : You probably figured it out for yourself already, Felix.



     -(No)
Sheba     : I guess I couldn't have expected you to understand, Felix...
-----------------------------------------------------------

Sheba     : There were strong winds blowing within Air's Rock... Those winds
            would carry far...

Kraden    : Carry? Carry what?

Sheba     : Ugh! You're so dense! The power of the Psynergy Stone!

Maha      : How is that possible? How could the stone's power be carried on
            the wind?

Sheba     : Do not belittle the power of the wind! Given time, the wind can
            grind great mountains down to sand! I mean, the wind at Air's Rock
            was strong enough to blow us off the ground! So why couldn't the
            wind carry particles of the stone all the way to Garoh?

* - Kraden looks excited. He and Maha start to speak at the same time.

Maha      : She's right!
Kraden    : She's right!

Maha      : Those particles from the Psynergy Stone must be charged with its
            power!

Kraden    : This explains why your Psynergy is weaker than that of Vale's
            people... You've been exposed to smaller particles.

Maha      : The wind patterns might also affect who among us in Garoh can use
            Whirlwind. Of course, this is all mere conjecture, but it does
            offer us some clues... Thank you, umm...

Sheba     : I'm Sheba. I'm pleased to meet you.

Kraden    : Oh! Haven't we given you our names, Master Maha? I am Kraden.
            This is Jenna... And Felix.

Maha      : You must permit me to thank you for all you've done.

Kraden    : No, no, please... We don't need any thanks...

Maha      : That's too bad... I was going to give you this.

* - A Jupiter Djinni appears.

Jenna     : It's a Djinni!

Maha      : A "Djinni"? Is that what you call them? When he is with you, he adds
            to your power. He is very helpful. I suppose you'll be continuing
            your journey now?

-----------------------------------------------------------
     -(Yes)
Maha      : So you intend to travel by sea? That is a long journey...



     -(No)
Maha      : So, you still can't tell just what sort of journeys await you...
-----------------------------------------------------------

Maha      : In that case, I think you will get more use out of this "Djinni"
            than I will.

* - The Djinni (Ether) joins the group.

Sheba     : Another Djinni! Talk about lucky!

Kraden    : This is a great gift. We are quite thankful.

Maha      : You don't need to thank me. Just take care on your travels.

Jenna     : Good luck with the... werewolf thing, Maha...

* - He nods.

Kraden    : Well, Felix, we must be going now.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Cavern beneath the boulder ]
Maha      :{S} Take care in your travels, Felix.

           {M} I wish that I were free to travel the world, like Felix and
               his friends.





   [ Outside ]
[001]     :{S} I hear tell [sic] from Master Maha that you guys are special,
               too... We don't have to hide our secret from you any longer!

           {M} How could these outsiders have learned Reveal? These guys must be
               pretty unusual.

[002]     :{S} Awoooooh! Heh heh... Sorry about that! I'm so happy I don't have
               to hide that I howled out loud!

           {M} I never thought I'd be so happy to have our secret out in the
               open!

[003]     :{S} Maha said you were the only outsiders we could share our secret
               with... So... does it bother you that we're all werewolves?

               --------------------------------------------
                    -(Yes)
               Yeah, I thought so... That's too bad. I was so happy when Maha
               told us. Now, I'm just really disappointed. Arooo.



                    -(No)
               Wow! You guys really are different from the others! Most people
               run away screaming or even grab their weapons...
               --------------------------------------------

           {M} Maha said these travelers were like us... Does that mean they're
               werewolves, too?

[004]     :{S} I heard there were other werecreatures in Osenia, in a few
               places... ...People who can turn into other things than wolves...

           {M} I would love to meet other werecreatures someday.

[005]     :{S} Last night when you saw me, I was wearing a hood. I guess I won't
               have to do that anymore!

           {M} I thought we'd never be able to talk to outsiders about our
               secret... I feel so free!

* - [016] is the little lycanthrope from the cavern.

[016]     :{S} Hey, it's you guys! Thanks for last night! Oh, yeah...
               That's right... You probably don't recognize me in my human form!
               I was in the cave with Maha! I was that little werewolf!
               I'm the reason you can stay in our village and we don't have to
               wear hoods!

           {M} My dad told me I put the whole village at risk... He was really
               mad... He said the whole thing was just dumb luck... But why
               would luck be dumb?





   [ Buildings ]
[Weapon]  :{S} What do you think? I'll bet these weapon suit you better than
               any fangs would!

           {M} I prefer the tooth and claw myself, but whatever...

[Armor]   :{S} When we change form it's best to be unclothed. But when you're
               human, armor always comes in handy.

           {M} Maha says that when we're wolves, we don't need to wear armor...
               He says our instincts will protect us.

-----

[006]     :{S} Hey! It's you! Thanks for looking out for our son last night!
               But I'm curious... Did you believe in werewolves before you
               came here?

           {M} The younger the werewolf, the less control he has over his wolf
               form... These travelers must have been very brave to follow him.

[007]     :{S} Everyone is amazed that you learned Reveal at Air's Rock!
               If you have some time, could you teach it to our children?

           {M} Oh, thank goodness! Everything worked out, and my husband's
               not mad...

[008]     :{S} My brother should have gotten in trouble, but they barely even
               got mad at him~

           {M} And dad said he was really going to tan his hide this time, too..
               And now everyone's treating him like he did some amazingly good
               deed!

-----

Innkeeper1:{S} If you can pass the tests of Air's Rock, you can do anything!

           {M} I've heard stories about other places like Air's Rock... If they
               can handle Air's Rock, they can probably handle those too.

Innkeeper2:{S} Maha came along and said the nicest things about you all.

           {M} He said if they were werewolves, he'd want them to take his
               place... They must have made quite an impression on Maha for him
               to say that.

* - The two guests are now awake.

[009]     :{S} Those wolves were really noisy last night, too.

           {M} I'm scared of wolves, so I don't go out much at night...

[010]     :{S} Maybe we should stay and try climbing Air's Rock one more time.

           {M} If I used a lever, I could probably make that rock spin...
               But I still don't get what the point of it is...

-----

Healer    :{S} I've heard about you. They say you're special like the people
               in this town.
           {M} Am I the only one here who isn't special!? Please, won't somebody
               answer my wishes and make me special, too?

-----

[011]     :{S} So you're something special? An Adept, or something like that?
               Does that mean that you can turn into a wolf or, something,
               like us?

           {M} Did Maha mean that they can change forms, like we can?

[012]     :{S} You learned Reveal at Air's Rock and lived to tell the tale...
               So that must mean... you can use Whirlwind.

           {M} So these people can use both Reveal and Whirlwind... They must be
               powerful like Master Maha is.

[013]     :{S} I just can't believe that someone outside the village learned
               Reveal...

           {M} Normally, outsiders never get in to see Maha, but these people...
               They can see him whenever they want...

-----

[Item]    :{S} I've heard stories about other mountains like our own Air's
               Rock... Like on this island that lies across the Eastern Sea,
               far from Osenia...

           {M} I heard that one that's across the Eastern Sea is really pretty,
               too. It's got water spilling down the sides in huge torrents.
               Sounds lovely...

-----

[014]     :{S} You... Is it true that you learned Reveal?

               --------------------------------------------
                    -(Yes)
               Hmm... I thought Air's Rock belonged to my people alone...
               But you young outsiders have mastered it so quickly... I might
               as well quit trying.



                    -(No)
               No, I can tell it was you they're talking about... I can smell
               Air's Rock on you... Ah, but you're so very young! And I am so
               very old... I might as well quit trying.
               --------------------------------------------

                 * - 2nd+ time:

               To think I've wasted so much of my life on something you did in a
               single afternoon...

           {M} I thought I could become a leader if I learned Reveal.
               How foolish of me.

[015]     :{S} He's worked so hard... But now, I don't know... He seems so sad.

           {M} So now, even outsiders are learning Reveal... How do we decide
               who will lead Garoh now?


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'14] ---          [Osenia]           --- [02'14] #$#
#$#$#                    Mikasalla                    #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} It's been a long time since we had any visitors in Mikasalla.

           {M} Why would anyone travel all this way just to come to our
               backwater town?

[002]     :{S} I went out to investigate after the earthquake... It looks like a
               whole different land collided into our own...

           {M} Osenia was big already, but now that we're connected to Indra...
               It's just huge!

[003]     :{S} Are you looking for someone?

               --------------------------------------------
                    -(Yes)
               Well, if you're looking for someone... I'd say the best place to
               start would be... somewhere else.



                    -(No)
               Didn't think so... We don't get a lot of strangers coming here.
               --------------------------------------------

           {M} I like this time of year best of all... It's so much nicer and
               more pleasant than the harsh winter...

[004]     :{S} A town called Garoh lies to the east of us... But...its residents
               aren't quite... human...

           {M} The people in Garoh are pretty furry. They look weird--and kinda
               cuddly--but they're nice enough.

[005]     :{S} If you look across the ocean tot he south, you can see Tundaria.

           {M} It's bitter cold in Tundaria... It snows there all year long.

[006]     :{S} If you're going deeper into Osenia, you'd better be ready for
               trouble.

           {M} No way I'd leave town... If I got lost on the roads out there,
               I'd be a monster snack in no time.

[007]     :{S} If you want to go into the heart of Osenia, there are two ways...
               You can approach from the south, or you can come down from the
               north...

           {M} It's weird that you can't go all the way around Osenia from the
               south... I mean, it's a piece of cake if you go around from the
               north...

[008]     :{S} In the heart of Osenia lies a sacred place, Air's Rock...

           {M} Air's Rock has stood there since this world was first formed...
               Nobody knows exactly what that means, though...

Sheep     :{S} Bah! Baaaaaaa!

           {M} Oh, yeah! Mmm! I just loves to eat me some grass! Yum!

Chicken   :{S} Buk buk buk...

           {M} The ground here is so soft! I just want to scratch and dig,
               buhKAWK!





   [ Buildings ]
Innkeeper1:{S} You've come a long way, friends. Stay a while, and rest your
               feet.

           {M} Why are travelers always in such a hurry? Like my mum used to
               say, "Fools rush in..."

Innkeeper2:{S} There aren't any towns between here and Garoh. You should rest
               here and maybe reequip yourselves before heading out.

           {M} There's no reason to go to Garoh unless you were heading to
               Air's Rock...

-----

G. Healer :{S} Have you been to Garoh?

               --------------------------------------------
                    -(Yes)
               They're all werewolves there... They hide away from those who
               fear them. But their cursed forms come with great powers...



                    -(No)
               Do not fear their outward appearance... Many revile them, but
               they are gentle, and they have kind hearts.
               --------------------------------------------

           {M} I wonder if there are werewolves beyond those in Garoh...
               I also wonder if they might not be as gentle as Garoh's folk.

-----

[General] :{S} We only have a small shop here. I used to specialize in items...
               But now, I sell armor and weapons, too.

           {M} I don't know much about weapons and stuff... I hope they don't
               ask me any questions. Maybe they only want items...

-----

[009]     :{S} I heard someone say there's another continent west of Gondowan.
               ...At least, that's what my dad used to tell me, rest his soul...

           {M} It must be nice to get out and see the world... But staying in
               one place is nice, too. Maybe that's why my dad founded this
               village.

[010]     :{S} My father-in-law was a great explorer, long ago, as was my
               husband.

           {M} That boy sure admires his grandpa, but I get really worried
               about him. I'm afraid he'd get hurt if he became an explorer
               like his grandfather.

[011]     :{S} Hey, mister! Are you an explorer?

               --------------------------------------------
                    -(Yes)
               Awesome! Don't tell anyone, but I want to be an explorer too
               someday!



                    -(No)
               My grandpa used to travel all over the whole world!
               --------------------------------------------

           {M} I love exploring out behind the house... It's my secret place!

-----

[012]     :{S} Those who have climbed Air's Rock claim that they can see the
               unseeable...

           {M} What does the unseeable even look like?

[013]     :{S} My husband has tried to climb Air's Rock many times... I wish I
               knew what he saw in that big hunk of rock.

           {M} I can't let him try to climb it again. What if he were injured?


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'15] ---           [Indra]           --- [02'15] #$#
#$#$#                      Madra                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Town entrance  #$
#$#$#$#$#$#$#$#$#$#$#

Guard 2   : Hey! You lot! Hold it right there!

Guard 1   : Hang on, there's no need to stop them. They couldn't be involved in
            this mess...

Kraden    : If you're talking about the pirate incident, I believe we resolved
            that to everyone's satisfaction.

Guard 2   : This has nothing to do with the Champa this time, old man!
            This time, the Kibombo attacked us!

Kraden    : "Old man"?!? Hmph! Wait... Did you say you were attacked again?
            By the Kibombo?

Guard 1   : Do you know about the Kibombo?

-----------------------------------------------------------
     -(Yes)
Guard 1   : You must be pretty worldly, considering that they rarely leave the
            heart of Gondowan.



     -(No)
Guard 1   : Not many people do...They're a barbaric tribe from central Gondowan!
            Watch out for them!
-----------------------------------------------------------

Kraden    : When did all this happen?!

Guard 1   : Not too long ago...

Guard 2   : Right after the mayor left, actually...

Kraden    : Was anything stolen?

Guard 1   : Only a single black orb... Everything else was untouched.

* - The black orb that was being held in the mayor/elder's residence.

Kraden    : A black orb...

Guard 2   : I'm afraid we don't have much more information than that.

Guard 1   : You helped us with the Champa, so, I'll tell you what... Maybe you
            could look around at the mayor's house. It's the only one that was
            robbed.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
Guard 1   :{S} My guess is the Kibombo have long since fled the area. Still,
               considering the way things have been going, we still want to
               have guards at the gates.

           {M} I've been standing for so long, I wish they could give us little
               stools we could sit on.

Guard 2   :{S} First, pirates raid our town, then the Kibombo come storming in..
               Things have been going horribly for Madra lately...

           {M} The way things have been going, I'm so scared I can hardly sleep
               at night... Is there no way to appease the gods? Is our town
               cursed?

[001]     :{S} So... The Kibombo got into Madra from Gondowan, right? Well,
               doesn't that mean that we can cross into Gondowan from Madra,
               too?

           {M} If Gondowan is really that much bigger than Indra, then I should
               go check it out.

[002]     :{S} There are still plenty of things I want to go investigate in
               this cave. And until I do, there's no way I'm going to seal
               the entire thing off.

                 * - He is referring to the Madra Catacombs.

           {M} I wonder who dug those underground passages and why they're
               there...

[003]     :{S} Briggs didn't have nearly as many pirates under him as we thought
               he did. He did an amazing job of flanking the town, considering
               how few men he had.

           {M} Well, if Briggs only has four crew members, then they couldn't
               have outflanked us...They must have had help from someone else...

[004]     :{S} Now that we're sealing off the other end of this hole, maybe we
               won't have any more surprises!

           {M} It was so convenient, being able to sneak out through the cave to
               the other side.

[005]     :{S} I guess that guy we had in prison wasn't one of Briggs's cronies
               after all...

           {M} He told us he was innocent, but we jailed him anyway. Is that
               justice? Is that right?

[Weapon]  :{S} The armorer and I are busy researching the equipment the Kibombo
               left behind. They dropped a lot of strange weapons that might
               reveal more about the attacks...

           {M} The Champa weapons we found before are identical to the Kibombo
               weapons we just found. It can't be a coincidence...

[Armor]   :{S} I knew there was something strange about the pirates attacking us
               like that... I think those weapons we found are going to be the
               key to the mystery...

           {M} The group that attacked from the east used different weapons from
               the group to the west. If they really were from the same crew,
               then why would they use different weapons?

[Item]    :{S} All my injuries have healed up pretty nicely... It made for a
               nice vacation, but now, it's time to get back to work.

           {M} That Shin is always bugging me just to relax and take a break.
               He's a real pain. I like working more than I like sleeping.

[006]     :{S} The Kibombo came in through the broken wall to the west.

           {M} It's strange... It's almost as though the Kibombo knew that the
               wall was broken... But there's no way they could have known...
               unless the pirates told them...

[007]     :{S} I can't believe someone stomped on those pirates... That's
               incredible!

           {M} If they were strong enough to beat Briggs, they must be huge!

[008]     :{S} Gondowan sounds like a frightening place. I don't think I'll ever
               go there.

           {M} In Gondowan, they have evil magic curses they can put on you
               in an instant!

[009]     :{S} Hey, mister! Are you the guy who beat up Briggs?

               --------------------------------------------
                    -(Yes)
               So does that mean you'll go thump the Kibombo, too?



                    -(No)
               You're not? Someone told me it was a young warrior...
               That sounded a bit like you.
               --------------------------------------------

           {M} I heard the guys who captured Briggs were just a bunch of feeble-
               looking kids...

[010]     :{S} I heard that the elder got us a boat in Alhafra... I wonder if
               it's true...

           {M} The mayor is supposed to be coming back with that boat...
               I wonder when that will be...

[011]     :{S} We think the Kibombo came into Indra across the new land
               bridge... But just because they COULD attack Madra doesn't
               mean they had to...

           {M} If it weren't for that tidal wave, none of this awful stuff
               would have happened...

[012]     :{S} Oh, Piers? We released him as soon as we heard. He stopped by
               the mayor's house and then left town.

           {M} Piers was so happy to get out of jail... But after he spoke to
               the mayor's wife, he looked unhappy. I wonder what she told him.

[013]     :{S} That guy Piers wasn't one of Briggs's men after all. I can't
               believe we locked him up without any evidence...

           {M} Piers didn't seem like he was in a very good mood when he left
               town. I guess he was still angry about having been imprisoned
               like that.

* - Prison entrance:

Guard 3   :{S} You shoulda seen my partner in that fight! He was in the mix
               right up until they took him down... Man... That takes courage!

           {M} I can't believe nobody seems impressed that my partner fought the
               Kibombo so bravely. Don't tell me they don't think it takes guts
               to stand up against them, because it does!

Guard 5   :{S} Everyone yelled at me for running away this last time, so next
               time, I'm gonna fight! But the thing is, last time, I took such
               a beating I got lumps on my head. Ouch!

           {M} I didn't have a chance to run away during the fight. The Kibombo
               were everywhere! That's the only reason I stayed to fight them.
               But I'm not about to tell anyone that!





   [ Buildings ]
Innkeeper1:{S} I've heard that Kibombo wield an evil, wicked magic... But...
               why didn't they use any of it when they attacked us?

           {M} There's nothing worse than wicked, evil magic. I don't want to
               see it, much less use it.

Innkeeper2:{S} Things have been busy here... First the pirates, then the
               Kibombo... What a week!

           {M} If it were me, I would have attacked a wealthier town.
               ...If it were me.

Employee  :{S} I hid under my bed on the night of the attack. I was really
               scared!

           {M} After I crawled under the bed, I fell asleep, so I was pretty
               achy the next morning.

[014]     :{S} I watched the entire attack of the Kibombo with my own eyes.
               I'll never forget it... I was paralyzed with fear...

           {M} I had to go to the bathroom in the middle of the night, but
               when I went... I saw all these eyes in the darkness. I got
               so scared... I didn't have to go anymore.

[015]     :{S} If you want to know about the attack, talk to my partner.
               He saw the whole thing.

           {M} The Kibombo attacked in the wee hours of the morning...
               Why weren't they asleep, like all us respectable people?

-----

[016]     :{S} It was sure sneaky of Briggs to destroy the bridge to Osenia
               after they crossed. It made it really hard for the mayor to reach
               Alhafra.

           {M} It sounds like Osenia is a huge place. They took forever to catch
               up with Briggs!

[017]     :{S} So Briggs and his pirates must have gone to Alhafra looking for
               a boat. I'm impressed that they were captured before they could
               escape.

           {M} Now that Briggs has been captured, I have nothing to fear! Yes!
               That means I can head to Osenia for some business!

-----

[Item Sis]:{S} I'm so happy that my sister's all better now.

           {M} I was so scared that my sister wouldn't get better...
               What would I do without her?

-----

[018]     :{S} My husband pursued the Kibombo after the attack, but he had to
               turn back...

           {M} In his youth, my husband was a very fast runner. They called him
               "The Cheetah." I guess he's learned that he can't race against
               old age.

[019]     :{S} The Kibombo apparently used ropes to climb down the cliffs.
               But we can't climb back up the cliffs from this side.

           {M} If I were just a little bit younger, I think I might have been
               able to catch those Kibombo.

-----

[020]     :{S} I can't stop thinking about that ship Piers left by the eastern
               shore.

           {M} I wonder if that ship grounded by the eastern shore is still
               broken. It seems like a well-built ship. It'd be a shame to just
               leave it there.

[021]     :{S} Piers left that boat of his behind when he took off... That thing
               wasn't going anywhere, so I guess he had no choice but to give it
               up.

           {M} Some people in town saw Piers heading toward the Gondowan Cliffs.

-----

Healer    :{S} The Kibombo are a tribe from Gondowan... They're searching for
               some great and evil power. Do not allow yourselves to be
               corrupted by them.

           {M} I hope the power of our faith will prevent the Kibombo from
               attacking us again...

[022]     :{S} If that tidal wave hadn't hit us, the Kibombo never would have
               been able to attack.

           {M} Everyone says them Kimbombo were mostly nekkid... They sound
               so... savage!

[023]     :{S} Them Kibombo possess evil powers. They sure are a weird bunch.

           {M} We're lucky the Kibombo didn't use their evil powers...
               There were enough injuries as it was.

-----

[024]     :{S} I'm glad the Kibombo's attack wasn't too terrible this time,
               but what if they come back?

           {M} What can we do to stop the Kibombo from attacking us again?
               Maybe we have to find a way to separate our continents like
               before the tidal wave...

[025]     :{S} The Kibombo are a very warlike tribe. That last attack was enough
               to warn me to stay away from central Gondowan!

           {M} Our best guess is that the Kibombo come from the central part of
               Gondowan... Why would they turn around so quickly after coming
               all this way?

-----
* - Elder and mayor's residence:

Mayor Wife:{S} All the Kibombo wanted when they attacks us was the black orb
               that sat above the fireplace. We're just lucky no one was hurt.

           {M} When my husband hears that the orb he was keeping was stolen,
               he'll be quite angry...

Elder Dau :{S} My father was holding on to that orb for Piers, and the Kibombo
               stole it... No matter how much he apologizes for losing it,
               it won't make things right.

           {M} I won't ever forget the look on Piers's face when he heard
               his orb was stolen. He was so sad... It was like he'd lost a
               part of himself...

Mayor Son :{S} If my father'd been in town, I wouldn't have been scared when the
               Kibombo attacked.

           {M} Dad always knows what to do... He'd never have let those
               Kibombo barge in here...

Mayor Dau :{S} My father hasn't come home yet, even though Briggs has been
               captured. I'm scared that something happened to him...

           {M} I hope he's just late because he's looking for a good souvenir
               to bring me...

Elder Wife:{S} Piers went to Kibombo to get his orb back. We told him that
               central Gondowan is very dangerous, but he wouldn't listen.

           {M} When Piers left, he said he was going to pursue the Kibombo,
               but I wonder... What if he reached the cliffs and then couldn't
               climb them. [sic] I hope he's not stuck.

-----
* - Prison:

Man 1     :{S} So, that Piers guy wasn't a pirate after all, huh? That still
               doesn't answer where that ice came from... That freaked me out...

           {M} That Piers was a strange fellow. Shin was terrified of him.
               He let him go as soon as we learned he was innocent.

Shin      :{S} Piers wasn't one of the Champa... That's why they let him go.
               You shouldn't just keep an innocent man in prison for no reason.

           {M} There was something really frightening about Piers... I'm glad
               to be rid of him... He went after the Kibombo, but I doubt he'll
               make it back from Gondowan alive.





   [ Madra Catacombs ]
[026]     :{S} Oh, uh... You coming through?

               -----------------------------------------------
                    -(Yes)
               Yeah, uh... We're sealing the hole up right now, so you, uh,
               can't get through this way. If you're trying to get into Madra,
               why don't you head around to the main entrance?



                    -(No)
               Yeah, well, that's good, 'cause we wouldn't let you down here
               anyway... Besides, anyone who's going to Madra can just go
               through the main gates, like normal folk.
               -----------------------------------------------

           {M} We sealed up the hole, but nobody seems to feel any better...
               Maybe we should just fill up the catacombs completely...

[027]     :{S} These caves were my secret hiding place. I wish they weren't
               going to seal it all up.

           {M} I've never seen any monsters around the cave entrance...
               I want to go inside and see if there are any monsters inside,
               but I can't...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'16] ---     [Indra / Gondowan]      --- [02'16] #$#
#$#$#                 Gondowan Cliffs                 #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$
$#  Cave  #$
#$#$#$#$#$#$

* - Prior to Briggs's capture, residents of Kibombo are present.

Man 1     : We've been found!

Man 2     : You wanna fight, punk?

Man 3     : No one said anything about fighting yet! We haven't done anything
            to you!

Man 4     : And if you think we did, then prove it!



Man 1     :{S} I'm, uh, from Kibombo... It's, er... nice to meet you.

           {M} Oh, tense... We're busted! They're on to us, I know it! We never
               should have launched that raid on Madra without the others!

Man 2     :{S} Hey, we're just here to finish what you guys started, OK?
               You guys are the ones who rammed into our continent, and don't
               you forget it!

           {M} My family lost its entire store of food--months' worth, gone
               in a flash! Well, we'll show those foreigners what happens
               when they mess with us!

Man 3     :{S} Hey, we're just out here, uh... camping... Yup. If you want
               good camping, go to Indra. We're just here to, you know,
               see the sights and stuff.

           {M} And once Kibombo warriors swarm over your town, we'll all be
               real good friends...

Man 4     :{S} Our friends from Kibombo are coming soon. When they get here,
               we'll all come say hello.

           {M} It was a good raid, but after all that work, we didn't find a
               thing... I wonder what happened to those people who fled from
               the jail we broke into.


#$#$#$#$#$#$#$#
$#  Outside  #$
#$#$#$#$#$#$#$#

Dog       :{S} Rrruff! Rrruff!

           {M} Dig here, you dig? Rrruff!

* - Using "Scoop" reveals a geyser.

Dog       :{M} I knew it! I knew there was something there, and he dug it up!
               Look at that!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'17] ---         [Gondowan]          --- [02'17] #$#
#$#$#                    Naribwe                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Welcome to Naribwe. It's really hot out... You should relax
               a while.

           {M} I can hardly stand the heat in Naribwe, and I've lived here
               my whole life! I can't imagine what travelers must think of it.

[Item]    :{S} No one can see the future. Absolutely no one. Except for our
               fortune-teller. Just by looking at your items, he can see the
               path you're meant to follow.

           {M} Even if I wanted my fortune told, I don't have any armor or
               weapons to show him. If he were only willing to look at other
               items, I'm sure he'd get more business.

[002]     :{S} It's dangerous out ever since the day the gems fell from the sky.
               After that day, all local creatures suddenly grew more powerful
               and terrifying.

           {M} That was the day the wind blew so hard and the dark clouds came
               from the north. That's when those strange gems fell from above.

[003]     :{S} The Kibombo went on an expedition to the east, but they've
               already returned. Do you know what kind of expedition it was?

               --------------------------------------------
                    -(Yes)
               What? They crossed over to Indra and attacked a town!?
               The Kibombo are a reckless and dangerous people.



                    -(No)
               Oh, you don't? The Kibombo rarely journey far abroad. It's very
               worrisome...
               --------------------------------------------

           {M} Akafubu is almost certainly looking for jewels. I cannot
               understand why a witch doctor needs so many jewels.

[004]     :{S} When I climbed the Kibombo Mountains, I had to find a path the
               Kibombo didn't know about...

           {M} I remember when I found that path above the pass... Not even the
               Kibombo knew about it! I'm not even sure I could find the way to
               the higher pass anymore...

[005]     :{S} You don't plan on going to Kibombo, do you, mister?

               --------------------------------------------
                    -(Yes)
               Well, you'll have to find a path through the Kibombo Mountains to
               get there. The Kibombo warriors keep a close watch on the pass.
               They won't let you through.



                    -(No)
               That's a wise choice. Nothing good would come to you in a place
               like that.
               --------------------------------------------

           {M} To get to Kibombo, you have to cross over the Kibombo Mountains.
               I seem to recall my grandfather telling me about a way past the
               guards.

[006]     :{S} I would not venture far north of here if I were you...

           {M} It if awful to the north of Naribwe... It is hotter, and the
               creatures are fierce... And worst of all, that's where the
               Kibombo are!

[007]     :{S} When Oeia was their witch doctor, the Kibombo were much more
               peaceful. Akafubu took over when Oeia passed on, and he is
               responsible for their warlike ways.

           {M} Kibombo magic was once widely respected. Now, it is merely
               feared. That is the way of things since Oeia appointed Akafubu
               as his successor before dying.

G. Healer :{S} I am but a humble pilgrim, serving the greater good in the
               heart of Gondowan. Travelers should know that even in this
               wild land, aid is not far off.

           {M} Anywhere I can do some good, I will serve without complaint.
               Although... it would be nice if it were a little cooler here.

[008]     :{S} Can you tell me where you have come from?

               --------------------------------------------
                    -(Yes)
               Angara? That is a land far to the north, is it not? I've heard
               that when it is hot here, it is cold in Angara. The world is a
               strange place.



                    -(No)
               Why won't you tell me? What are you trying to hide?
               --------------------------------------------

           {M} The warrior who passed through here earlier said he came from
               an isle in the middle of the sea.

[009]     :{S} On the far side of the river lies a huge mountain we call Magma
               Rock. It is a a sacred place that the gods created long ago.

           {M} Sometimes, you can hear explosions from across the river near
               Magma Rock. I wonder what's going on over there.





   [ Buildings ]
Innkeeper1:{S} Our cooking is famous all across Gondowan. If you find you like
               it, come back soon! We change our menu every season.

           {M} Our spices are our secret. Everyone loves spicy food, even if
               they regret it later. And I'll thump the first person that tries
               to tell me otherwise!

Innkeeper2:{S} If you like adventure, you should head out west across the
               river... Oh, wait... With all the rain we've had lately, the
               river is probably too deep to cross.

           {M} The river is probably very dangerous right now. It's filled
               with monsters when the water are running high.

-----

[Weapon]  :{S} If you are burdened with many concerns, take a weapon to the
               fortune-teller. He can read your future by studying the weapons
               that you carry.

           {M} I can look at any weapon and see the monsters it faced, but I
               cannot read its future.

[Armor]   :{S} You should visit the fortune-teller when you are in our village.
               By looking at the items you possess, he can see what it is that
               troubles you.

           {M} Whenever I get my fortune read, I offer up some armor. I think
               this might be why I find so many rare and valuable artifacts.

-----

[010]     :{S} The fortune-teller lives at the highest house in Naribwe...
               He's the closest thing we have to a mayor.

           {M} The fortune-teller is Naribwe has quite a reputation...
               His predictions are so accurate! He's always done them for
               us alone, so I don't understand how he got so famous.

[011]     :{S} We're a small village, but if we all cooperate, we can get
               almost anything done.

           {M} As long as we listen to the words of the fortune-teller,
               we won't have any worries...

-----

Seer      :{S} If you desire a reading, stand before the table...

           {M} The items that one carries are filled with one's hopes and
               desires. I can sense these desires and I can see answers hidden
               within them.

* - For the seer's readings, refer to section 03'03.

[012]     :{S} By painting our bodies, we bring about good luck. You should
               try it, too.

           {M} Body painting also protects us from the magic of the witch
               doctor, or so I'm told.

[013]     :{S} My father is a fortune-teller, not a witch doctor. There are a
               great many differences between him and Akafubu of Kibombo.

           {M} My father may not be a witch doctor, but he could easily defeat
               Akafubu.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'18] ---         [Gondowan]          --- [02'18] #$#
#$#$#                Kibombo Mountains                #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Up the path, a man coming from the north speaks to a man already here.

Guard 1   : Is the way clear?

Guard 2   : This area is clear! The strange one has not been seen! And there?

Guard 1   : We have not seen the stranger near the village. Do you believe
            he was truly headed toward Kibombo?

Guard 2   : The guards here were only recently knocked unconscious.

Guard 1   : Correct. We were under strict orders to maintain a strict watch
            over the mountain pass.

Guard 2   : No one must be permitted into Kibombo until Akafubu has completed
            his ceremony.

Guard 1   : Then we had better hurry to find the one who attacked our guards.

* - Guard 1 returns to the north.

Guard 2   : Keep a good watch. Do not permit anyone to pass. If anyone
            interrupts Akafubu's ceremony, he will hold you responsible...





* - Upon approaching any of the guards:

Guard A   : Guards! An intruder! Someone is trying to pass! To arms, Kibombo
            warriors! To arms!

* - Several guards come and swarm Felix's group.

Guard B   : Here! The intruder is here!

            Kibombo does not permit visitors! You just follow this road
            right back to where you came from!

Guard A   : Guard! Get him out of here!





* - Upon being spotted by the watchdog:

Watchdog  : Grrrrr! Rrrruff! Rrufff!

Guard     : An intruder! Repel the intruder immediately!

* - From here, it is the same as before when the guards swarm Felix's group.





* - After knocking down a bone that distracts the watchdog:

Watchdog  :{S} Sniff sniff... Lick lick lick!!

           {M} A bone! That's my favruff! Lick lick... It's deruffcious!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'19] ---         [Gondowan]          --- [02'19] #$#
#$#$#                    Kibombo                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - It is night. Torches have been placed outside of every building.
    Most residents have gathered by the north end of the village.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} If the Great Gabomba's mouth doesn't open, Akafubu must not yet
               be a true witch doctor.

           {M} I feel so much excitement... At last, will the Great Gabomba
               recognize Akafubu's strength?

[002]     :{S} Akafubu's ceremony is set to begin soon. I wonder if he'll
               succeed this time.

           {M} It's strange that Akafubu decided to try again tonight.
               What bolstered his confidence?

[003]     :{S} Akafubu was a good man when he was training with Oeia...
               After Oeia died, Akafubu was simply no longer the same.

           {M} Akafubu has not yet attained the magical skill that Oeia
               possessed. I worry for our future if Akafubu's character is
               as weak as his magic.

[004]     :{S} Akafubu blames his failure on the jewel he originally used.
               He claims it was no good. That's why he led a team of soldiers
               to find a new one.

           {M} They attacked some town to get the jewel he needed.
               I hope no one was injured.

[005]     :{S} I'm afraid of what Akafubu will do if he fails the ceremony
               a second time.

           {M} When he fails the ceremony, Akafubu gets so angry... I hope he
               doesn't turn his anger on to me... I'm afraid of his powerful
               magic.

[006]     :{S} Akafubu is attempting the ceremony again tonight. Oeia performed
               the same ceremony with no problems. What's holding Akafubu back?

           {M} Oeia's sudden death brought pressure and responsibility on
               Akafubu, well before his time.

[007]     :{S} When the Gabomba is angered, his eyes glow with rage and fire
               shoots out of his mouth.

           {M} I hope Akafubu hasn't angered the Great Gabomba. I would be sorry
               to see him die like that...

[008]     :{S} Akafubu has tried this before, but he has always failed.
               Tonight is different, though. With this new gem, he may succeed.

           {M} As a child, Akafubu was every bit as horrible. He always cried
               when he had to share his toys. When he was good, he was very,
               very good... but when he was bad, he was AWFUL.

[009]     :{S} During the last ceremony, Akafubu made the jewel float in the
               air... But the mouth of the Great Gabomba did not open.

           {M} The Great Gabomba is supposed to open his mouth of Akafubu
               is worthy.

[010]     :{S} Hey, no pushing! You're not going to get any closer, with all
               these people packed in here.

           {M} There are so many people here! If I want to see the ceremony,
               I'll have to climb the posts!

[011]     :{S} If the Great Gabomba likes the jewel, his mouth will open and
               his tongue will stick out. It sounds weird, but it's a sign
               that the Gabomba accepts the offering.

           {M} If the Great Gabomba actually moves and sticks out his tongue...
               I might just faint!

[012]     :{S} Is making the jewel float with the power of his mind all there is
               to it? I would have thought a ceremony like this would have
               required a little more effort.

           {M} He's failed so many times already... Won't the same thing happen
               again if he tries it another time?

[013]     :{S} I hope the Great Gabomba is satisfied by Akafubu's jewel and
               opens his mouth this time.

           {M} If the Great Gabomba opens his mouth, he will have acknowledged
               Akafubu's power. When the Great Gabomba accepts the jewel,
               the door will open.

[014]     :{S} Akafubu looks really confident tonight. I think he just might
               succeed this time!

           {M} He travels to Madra and returns with a stolen gem, and now he
               expects us to call him a hero?

[015]     :{S} He who is the witch doctor of Kibombo holds the most revered
               office in our whole town.

           {M} If only Oeia had taught his magic to someone else... If he had
               another pupil, this would go more easily on poor Akafubu.
               He would not be alone.

G. Healer :{S} Oh... Oh my... I've heard of ceremonies like these...
               Foreign deities are so frightening...

           {M} I wonder if a man in my position should really be in a place
               like this.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Cliffs above Gabomba Statue  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Only from the cliffs can Felix's group observe the ceremony below.

Akafubu   : At last, the sacred night has come!

* - The jewel from Madra, similar in appearance to Babi's Black Orb, has been
    put into the Gabomba's hands.

Akafubu   : Tonight, Akafubu becomes the Kibombo's new witch doctor! All of you,
            pray in the depths of your hearts for my success!

* - The other observers cheer.

Kraden    : It looks like the initiation ceremony is beginning. I'm not sure
            what will happen, but we'd better hurry, Felix.





* - Piers is also standing atop the cliff.

Piers     : Wh-Who are you?!? What... What are your intentions?

Sheba     : It looks like Piers has already forgotten us, huh?

-----------------------------------------------------------
     -(Yes)
Jenna     : I know! We met Piers when he was in JAIL! And it's not like he had
            lots of visitors, either!



     -(No)
Jenna     : What, is he so obsessed with his black orb that he can't even
            remember us?
-----------------------------------------------------------

Piers     : Wait a second... I know you... You're the travelers who came
            seeking me when I was in jail.

Kraden    : So, you DO remember!

Piers     : What are you doing in this place?

Sheba     : Actually, that's what we wanted to ask you...

Jenna     : We were worried about you, Piers, so we followed you here...

Piers     : And that's what brings you to this dangerous place?

Sheba     : What's that supposed to mean?

Jenna     : We came here to help you, Piers. Why are you being like that
            about it?

Piers     : Tell me something... Exactly when did I ask you for your help?

Akafubu   : SILENCE! I shall now present our jewel to the Great Gabomba!

* - Akafubu uses the Psynergy "Lift" to raise the jewel into the air.

Piers     : !!!

Akafubu   : O Great Gabomba! Please accept this, our humble gift!
            Please, Great Gabomba! Accept this jewel!

* - The Gabomba opens its eyes.

Akafubu   : Look! The Great Gabomba has noticed the light of the jewel!

* - It shuts its eyes again.

Akafubu   : Why, Great Gabomba?

* - He lowers the jewel.

Akafubu   : Your prayers were weak! Open your hearts to the Great Gabomba!
            Sing your praises and dance for the Great Gabomba until your prayers
            reach his ears!

Piers     : Akafubu is no witch doctor! He's an Adept! I may have to confront
            him to get my orb back... I may have to fight. I will do whatever
            it takes, but I will have my black orb back again.

* - He looks about.

Piers     : It's no use. We can't get to Akafubu from here. This won't work,
            either... What are we going to do? We can't get ever there!

Jenna     : Piers is in trouble. Shouldn't we try to help him?

* - Kraden notices two ledges, separated by a gap, as well as a wooden log
    on the ledge farthest from them--which is out of reach by normal means.

Kraden    : Maybe if we could do something about that stump, we could reach the
            backside of Gabomba. We've got to help Piers. Right, Felix?

-----------------------------------------------------------
     -(Yes)
Kraden    : Then hop to it!



     -(No)
Kraden    : What's all this now, Felix? Is it too much to ask that you help
            Piers in his time of need?
-----------------------------------------------------------

* - Before dealing with the log:

Piers     :{S} The orb is right before me, and yet I cannot reach it...

           {M} I am certain I just sensed the power of Psynergy, but that
               can't possibly be...

* - Upon using Move to drop the log into the gap:

Piers     : ?!? That power... Was that Psynergy?

-----------------------------------------------------------
     -(Yes)
Piers     : I knew it!



     -(No)
Piers     : Please, don't try to complicate things by lying... It must have
            been Psynergy...
-----------------------------------------------------------

Piers     : I should have spotted it at once! You're Adepts!

Jenna     : Wait, so does that mean you're--

Piers     : Yes, my name is Piers, and I too am an Adept. To be honest,
            everyone in Lemuria is an Adept, and not just me.

Sheba     : What's Lemuria?

Piers     : Lemuria is an island that lies in the center of the Eastern Sea.

Kraden    : Wait a second... You said Lemuria? I've heard that name before...
            Of course! It was Lord Babi! He often spoke to me of Lemuria.
            He said it was so advanced that we can scarcely begin to imagine
            what it must have been like...

Piers     : You are correct. My home was and is all that you say. Whoever told
            you this knows much of Lemuria.

Jenna     : But wait, if it's so far away in the middle of the ocean, how come
            anyone knows so much about it?

Piers     : It is not easily reached, and we Lemurians seldom leave... I cannot
            imagine how anyone could  have learned anything at all about us.
            Except... Hold on a moment... Babi... I've heard that name somewhere
            before...

Sheba     : Well, yeah... Everyone knows about Lord Babi... He's the ruler of
            Tolbi...

Piers     : I've never heard of Tolbi. Until recently, I had never left my home
            of Lemuria...

Jenna     : Piers, are you just playing games with us?

Piers     : Don't be foolish. What would I gain from lying to you?
            I'm being quite serious.

Kraden    : Piers is not playing games, Jenna. You can trust him.

Piers     : Thank you for believing me, master sage!

Kraden    : Please, call me Kraden, Piers of Lemuria. And I am the one who
            should be thanking you!

            You look puzzled, Felix. You are probably wondering what I'm
            talking about...

-----------------------------------------------------------
     -(Yes)
Kraden    : I thought as much...



     -(No)
Kraden    : Oh, good! Then I probably don't need to tell you...

Jenna     : Wait, just because my brother knows that you're talking about
            doesn't mean we do! Tell us!
-----------------------------------------------------------

Kraden    : If what Babi told me is true, Lemuria is all that remains of a once
            great civilization.

Piers     : Your friend is correct.

Kraden    : In fact, the reason I was sent to Vale was somewhat related to my
            inability to find Lemuria itself...

Sheba     : I don't understand... What was in Vale that had anything to do
            with Lemuria?

Kraden    : Babi believed that, in Lemuria alone, the power of Alchemy remains
            unbound.

* - Piers nods.

Kraden    : Lord Babi had need of Lemuria's Alchemy, but despite our effort,
            we could not find the lost city. Since we could not find Lemuria,
            Lord Babi went me to unlock the secrets of Alchemy myself.

Piers     : Ah, yes! Babi! If I recall correctly, a man named Babi came to
            Lemuria long ago... He stole one of our ships and fled the isle...

Kraden    : Yes! That must indeed be the same Lord Babi who know leads [sic] the
            people of Tolbi.

Jenna     : Now, I'm even more confused. This is making my head hurt... I mean,
            if Babi really stole a ship from your home, why would he be trying
            so hard to find it again?

Kraden    : I can't expect you to understand, my dear. Lord Babi's reasons for
            finding Lemuria are... complex.

Sheba     : But if he already found Lemuria once, why doesn't he just go back
            the same way?

Piers     : Once you have left Lemuria, finding it again is quite difficult,
            even if you know where to look.

Jenna     : Well... why?

Piers     : The waters around Lemuria are wrapped in a perpetual fog...
            It is very difficult to navigate.

Kraden    : I remember Lord Babi once saying something to that effect.

Piers     : Even if one locates Lemuria, getting through the fog itself
            remains quite a challenge.

Sheba     : I don't get it... Why can't you just sail straight through it?

Piers     : The ocean currents around Lemuria are swift and treacherous...
            Only one who can sail a Lemurian ship can complete the journey.

Sheba     : But... Babi stole a Lemurian ship from you, right? That means that
            he can sail it... You said yourself that he used it to flee the
            island!

Kraden    : Unfortunately, Babi was the only one of us who could use the ship.

Piers     : You see, Lemurian ships can only be helmed by Adepts... Which is why
            I have to get my black orb back! I must be able to captain my ship!
            There may be something up ahead on this path. Then let's go...

* - He starts to leave.

Kraden    : Wait a moment, Piers... We want to help you get your orb back.

Piers     : You intend to help me, Kraden?

Kraden    : I am on this quest for  many reasons... one of them being that
            I wish to see Lemuria. If you would allow it, that is... I'd like to
            visit Lemuria myself.

Piers     : If this is something you would do for Babi, then I cannot permit it.

Kraden    : What? Why not?
Piers     : Babi is a thief. He is not well loved in Lemuria.

Kraden    : It is partially on behalf of Babi... ...but there's more to it
            than that! I want to go to Lemuria so that I can see the full power
            of Alchemy!

            I want to aid Piers so that he will take us to Lemuria...
            What do you say, Felix?

-----------------------------------------------------------
     -(Yes)
Kraden    : You'll do it!? Splendid!



     -(No)
Kraden    : Why, Felix? Why? Please, we simply have to!

Jenna     : What's the matter with you, Felix? I don't see why we can't
            help Piers.

Sheba     : Yeah. I'm with Jenna on this one.
-----------------------------------------------------------

Piers     : I appreciate your offer, but...

Jenna     : I understand, Piers... You're not sure if you'll be able to take us
            to Lemuria, is that it?

* - Piers nods.

Sheba     : Can't we talk about this later?

Kraden    : Yes, yes, of course! For now, let's just get that orb back for
            Piers!

<game>    : Piers joined your party.





* - When trying to head back to the village?

Piers     : Now that I know the orb is here, I won't leave this village without
            it! I will go alone if I must!

* - He leaves. When approaching him:

Piers     : You've come to help my get my orb back? Thank you, all of you!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Gabomba Statue  -  Interior  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A hidden ladder can be found that leads into the statue. Within it,
    various mechanical devices are scattered about.

    In the second-highest room, two gears allow for the tongue to be rolled out.
    A miniature statue rests at the back of the room.

    Upon arriving at the highest room, Akafubu shouts from outside.

Akafubu   : Focus your energies!

* - Kraden looks out the Gabomba's eyes.

Kraden    : Everyone! Look over here!

Akafubu   : Let us now present our jewel to the Great Gabomba!

* - Akafubu uses Lift to raise the jewel.

Akafubu   : O Great Gabomba! Please accept this, our humble gift!
            Please, Great Gabomba! Accept this jewel!

* - The Gabomba opens its eyes.

Akafubu   : Look! The Great Gabomba has noticed the light of the jewel!

* - Inside the Gabomba's head, two floating orbs - one red and one blue -
    send out energy across conduits on the floor. However, the energies are
    unable to reach the miniature Gabomba head on the floor due to obstruction.

    The Great Gabomba shuts its eyes again.

Akafubu   : You are still not pleased?

* - He lowers the jewel.

Akafubu   : No! This time, he seemed almost like he might... We must continue!
            Drums! More drums!

Kraden    : Ah! So that's how it works!

Sheba     : He's been failing because the conduit that channels his Psynergy
            is broken.

Jenna     : Should we reconnect the conduit so he can complete the ceremony?

-----------------------------------------------------------
     -(Yes)
Piers     : I won't help them, Felix! They're the ones who stole my orb
            from the Madrans!



     -(No)
Piers     : I agree, Felix! Why should we help this pack of thieves?
-----------------------------------------------------------

Kraden    : Piers, I understand that you're angry at them, but it really is
            in our best interest to help. Think about it, Piers...
            Akafubu stole the orb solely to perform this ceremony...
            So, what do you think he intends to do with the orb?

Piers     : He means to give it to the Great Gabomba... Oh! So...if his ceremony
            succeeds, the orb will be taken into the statue...

Kraden    : And we're INSIDE the statue! If the ceremony succeeds, we can go
            find the orb!

Piers     : I... don't want to help that Akafubu, but...

Sheba     : I don't like the idea of helping him any more than you do, but if we
            can end this without a fight...

Piers     : You're right, Sheba. Let's see if we can't help him finish his
            little ceremony.

Kraden    : It looks like the energy charge is supposed to run over these
            blocks.

* - Some parts of the circuit can be taken out and swapped with others.
    Those are the blocks.

Kraden    : If we can just move these around a little, that might be enough
            to complete the circuit...

* - He notices something.

Kraden    : Ah! There we go!

Sheba     : These panels have arrows on them... What do you think it all means?

Kraden    : Look at the directions they point... I'll bet these will rotate
            the blocks...

Piers     : But how do we set the blocks back in place?

Jenna     : Just Pound them in!

* - The first letter of "Pound" is capitalized as it is the name of a Psynergy.

    When the pillar between the panels is pounded into the floor, the blocks
    rise into the air - at that point, they must be individually pounded back
    into their places after having been rotated by stepping on the arrow panels.

Kraden    : Won't that do the trick? We must watch the path his Psynergy takes
            and move the blocks accordingly.

* - Outside:

Akafubu   : Oh! The magic, the power of the witch doctor fills my body! At the
            count of twenty, I shall present our jewel to the Great Gabomba!
            Make your hearts as one, and dance for the Great Gabomba!

* - At the count of twenty:

Akafubu   : O Great Gabomba! Please accept this, our humble gift!





* - If neither color energy reaches the mini head, the Gabomba shuts its eyes.

Akafubu   : You are still not pleased!

* - He lowers the jewel.

Akafubu   : No! This time, he seemed almost like he might... We must continue!
            Drums! More drums!





* - If the blue energy reaches the head, the Gabomba's eyes flash blue.

Akafubu   : Look! Look! The Great Gabomba has seen our jewel!

* - Its eyes... pop out and are replaced by trembling, mechanical blue dots?
    Strangely enough, that would appear to be the case.

Man 1     : Ah! We have enraged the Great Gabomba!

Man 2     : No! Great catastrophe shall befall the Kibombo!

Akafubu   : Silence! SILENCE! Do not be hasty! The Great Gabomba has not opened
            his eyes in anger! Your prayers... have not appeased him...
            That is all! Pray! You must pray more! Let the Great Gabomba hear
            our desires! Drums! More drums!!!





* - If the red energy reaches the head, the Gabomba's eyes flash red.

Akafubu   : Look! The Great Gabomba has responded to our gift!

* - Fire shoots from the Gabomba's mouth.

Man 1     : Wahhh! The Great Gabomba spews jets of flame!

Man 2     : It is the end of Kibombo! Our village is doomed!

Akafubu   : Silence! SILENCE! Do not be hasty, my people! The Great Gabomba
            is not angered by our ceremony! He is angered by the presence of
            wicked thoughts! Cast away your wicked thoughts! Dance! Dance for
            the Great Gabomba! Drums! More drums!!!





* - If both energies reach the head, the Gabomba's eyes flash white.

Akafubu   : Look! The Great Gabomba has responded to our gift!

* - It extends its tongue, taking the black orb into its mouth, and then
    puts out its tongue again for Akafubu to enter.

Akafubu   : Did you see it, people? At last! The Great Gabomba accepts me!
            I shall answer his call! I shall enter the Great Gabomba!
            Wait for me, my people!

* - He enters.

    Felix's group is standing by the miniature statue on the second-highest
    room.

Piers     : The black orb... Where is it?

Sheba     : I saw it roll in there...

Jenna     : It came in through there and rolled along the groove in the floor...

Kraden    : It vanished into that hole!

Sheba     : It looks pretty deep...

Jenna     : Can you see it? Do you think we can reach it?

Sheba     : Hm... No, I can't even see it.

Piers     : It's no use... Now, I'll never see Lemuria again... I am lost
            forever from my homeland!

Sheba     : Wait, hold on... I can see light on the other side of this hole...

Kraden    : A light? There must be a room on the other side of this statue...

Akafubu   : Who... Who are you!? What are you doing here? Are you Kibombo!?

-----------------------------------------------------------
     -(Yes)
Akafubu   : What? Do you take me for a naive fool!?



     -(No)
Akafubu   : Then what are you doing inside the Great Gabomba!?
-----------------------------------------------------------

Piers     : We've come to reclaim the black orb you stole!

Akafubu   : Do you really believe I would permit you to take it!?

Sheba     : Hey, watch it! You wouldn't even be in here if it weren't for us!

Akafubu   : What is that supposed to mean? Why should I believe you? I am
            Akafubu, the chosen witch doctor of Kibombo!

* - Jenna drags him to the top floor.

Jenna     : Yeah, we know... We saw your magic energy flowing past us. See how
            this channel runs along the floor? Here, look... It runs all the way
            over there! But the thing is, the circuit was broken right there.
            So we completed the circuit so that your magic energy could go where
            it needed to go.

Akafubu   : But... if you truly did this, then why? Why did you help me?

* - The others come up.

Kraden    : We were sort of hoping that we could take the orb if your ceremony
            succeeded...

Akafubu   : Ah, so you have taken the orb? Then begone! You have no further
            business here!

Piers     : But... we didn't get the orb.

Sheba     : It rolled through this groove and right through this hole.

Kraden    : We saw a light through there, so we suspect there must be another
            room behind the wall...

* - They return to the second-highest floor. Akafubu places a red jewel in the
    hands of the miniature statue. It slides away, revealing a passage.

Akafubu   : I might be able to retrieve the orb.

* - Akafubu heads down the passage.

Jenna     : Do you think Akafubu will really return the orb to us?

-----------------------------------------------------------
     -(Yes)
Piers     : Maybe we had him all wrong...



     -(No)
Piers     : I think Jenna is right. It sounds like he's going to return what
            he has stolen.
-----------------------------------------------------------

Sheba     : I thought Akafubu was an evil man, but I guess we were wrong...

Kraden    : You never can tell, Sheba...

            We have little choice but to trust that he will return it. Come on!
            Let's go, Felix!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Akafubu sees the future... That's how he knew to find the jewel
               in Madra.

           {M} I really wonder how accurate Akafubu's farsight [sic] is. If his
               skills were stronger, he should be able to prophesy the outcome
               of this ceremony.

[002]     :{S} They told me I had to stay awake until the ceremony's over.
               Usually, they tell me I have to go to bed early! Make up your
               minds already!

           {M} As long as this ceremony's going on, I get to stay up! Normally,
               I get in trouble for trying to stay up this late.

* - [003] has left.

[004]     :{S} They say the Great Gabomba's great jaw finally opened. I wish
               I could go up front and get a better view.

           {M} They're saying the Great Gabomba opened his mouth, but I'll just
               have to take their word for it. I wish I were closer, so I could
               see it and know for sure.

* - [005] has left.

[006]     :{S} Tonight seems to have been a good night... I was worried,
               since Akafubu kept failing.

           {M} Will the Great Gabomba finally accept Akafubu and make him our
               new witch doctor?

[007]     :{S} Last time Akafubu tried the ceremony, he failed. I saw him crying
               behind the statue after.

           {M} Akafubu's always been a crybaby. Whenever he failed his lessons,
               he cried and cried.

[008]     :{S} What? Don't ask me what Akafubu's doing in there. I was just
               wondering myself.

           {M} It's so far away from the action... From back here, Akafubu looks
               like a deranged mosquito!

[009]     :{S} Akafubu has been inside the Great Gabombo for a while now.
               How long is he going to take?

           {M} What's taking so long? We can't finish the ceremony until Akafubu
               comes back out.

* - [010] has left.

[011]     :{S} I believe in Akafubu. I believe he will surpass Oeia and become
               a great witch doctor.

           {M} Akafubu and Oeia are so different... How can he ever hope to
               replace Oeia? Ah, why did Oeia have to die? What are we to do?

[012]     :{S} Once the ceremony is complete, Kibombo will be like a village
               reborn. Peace will come again.

           {M} Kibombo was so much better when Oeia was our leader. I wish we
               could return to that life once again...

[013]     :{S} I think Akafubu's has [sic] finally succeeded at his ceremony.
               Maybe Kibombo will finally be peaceful once again.

           {M} Akafubu is obsessed! He'll keep trying this until he gets it
               right. Please, oh please, just get it right tonight!!!

[014]     :{S} Whew! Thank goodness those drums have stopped. They were rattling
               my brain!

           {M} Am I going to have to play drums all night? Can't they just...
               dance without them?

[015]     :{S} Oeia's death was so sudden. It's been hard on Akafubu.

           {M} I suspect Akafubu never really wanted to become the Kibombo
               witch doctor. Poor boy.





   [ Gabomba Statue  -  Outside ]
[016]     :{S} Ahh! Something is coming from within the Great Gabomba!
               Are you men, or are you... gods?

           {M} They look like people, but how could they be here now? I cannot
               believe it! Why doesn't my magic amulet have any effect on them?

[017]     :{S} You look human... but perhaps you are the ones who created the
               Great Gabomba, reborn before us!

           {M} If no person other than Akafubu can enter the Great Gabomba...
               Then these people aren't really people at all!

[018]     :{S} Akafubu possesses the power to enter the Great Gabomba! My faith
               is restored!

           {M} I saw Akafubu's power open the jaw of the Great Gabomba. I saw it
               happen, but I still don't believe. it. But... I SAW it happen...

[019]     :{S} We must stand guard and wait until Akafubu's return!

           {M} I hope Akafubu completes the ceremony soon... I'm so sleepy...
               I want to go home.

[020]     :{S} Men or gods, we fear you not! The Kibombo fear nothing!

           {M} What if the Great Gabomba only opened its mouth to lure Akafubu
               in and... crush him like a grape!

[021]     :{S} It seems these beasts want to pass through... Can't you see
               we are in the midst of our ceremony!? None shall pass until
               it is complete!

           {M} Look at these guys. They think they're so hot... I bet they think
               they're gonna get past me... They have no idea how long I can
               stand here, saying the same thing to them, over and over.

[022]     :{S} This isn't a bad way to spend an evening, when you get right
               down to it. I could dance all night and all day tomorrow, too.

           {M} Sure, this is fun, but my feet hurt! I never want to hear an
               irresistible dance beat again!

[023]     :{S} It is proper for a warrior to be a man of few words.
               It is the fearful dog who barks the loudest.

           {M} *Koff! Koff!* All this chanting is making my throat hurt!
               No more singing in the shower for me.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Gabomba Statue  -  Interior  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Past the miniature statue, an elevator leads to a hall on a lower level.
    At the far end, the black orb has been placed in another statue's hands.

Akafubu   : I have followed Oeia's instructions and entered the final chamber!
            He told me that if I reached this chamber, I would become Kibombo's
            witch doctor. But what must I do here to become a witch doctor?
            I do not know...





* - Akafubu:

Akafubu   :{S} Your black orb rests in the hands of the statue before you.
               Go on, take it.

           {M} Oeia... What am I to do now?





* - Upon examining the orb, the statue's eyes glow and the orb rises.

?????     : Oh, young witch doctor... You have succeeded in your task.
            You have found this chamber.

Akafubu   : Wh-Who speaks?

Kraden    : It sounded like it was the statue of the Great Gabomba.

Akafubu   : That's ridiculous...

Gabomba   : Akafubu! Your magic has grown strong! At last, you are worthy
            of the title witch doctor. I give you the feathers and gown that
            are the badges of your office!

* - The items appear on Akafubu.

Gabomba   : Akafubu, from this day forward, you shall be Kibombo's witch doctor.

Akafubu   : I've done it! I've finally earned the right to be witch doctor!
            At last! Yes!

* - He quickly takes off to announce the state of things.

    A chest lowers from above.

Gabomba   : And there is one thing that remains for me to give you...

            Akafubu... You hasty fool... I had something else to give you,
            and in your haste, you left too soon.

            Say, you there...

* - Felix looks around.

Gabomba   : Yes! You! You, looking around there! I have magic for Akafubu,
            magic that he will soon need, ...but he is not ready for it.
            As a result, I have decided that I shall not pass this magic on
            to anyone just yet. Tell this to Akafubu: If he desires this
            new magic, then he must earn it himself!

* - The chest rises out of sight.

Gabomba   : If Akafubu does not refine his magical arts, then he will never
            earn this new power. This power shall not be realized until he
            ceases living only for himself... And instead lives his life to
            benefit others. Tell him so!

Kraden    : I don't suppose you could just... give that magic to us?

Gabomba   : What do you mean?

Kraden    : I'm just asking if maybe we could earn that magic before Akafubu.

Gabomba   : The power can be claimed by another, but only if Akabubu lacks the
            will to earn it himself.

Kraden    : Aha! So we CAN get it!

Gabomba   : Perhaps if he must compete for his power, he will focus and take
            his office seriously. But before you do this thing, you must convey
            to Akafubu all that I have told you.

Kraden    : Oh, of course! We wouldn't dream of cheating him... We will tell him
            all you have told us.

Gabomba   : Follow that path, and you will find a cavern...

* - A tile on the floor disappears, revealing a ladder.

Gabomba   : But now, I shall sleep... until the time comes when I must anoint
            a new witch doctor.

* - The orb drops down into the statue's hands.

Kraden    : Felix... Go get Piers's precious orb.

<game>    : Felix got the Black Crystal.

Kraden    : Felix... Do you have any idea exactly what this "Great Gabomba"
            really is?

-----------------------------------------------------------
     -(Yes)
Kraden    : If you have unraveled that which I cannot, then perhaps you are the
            greater scholar.



     -(No)
Kraden    : You do not understand either? Then I do not feel quite so foolish...
-----------------------------------------------------------

Kraden    : But doesn't this witch doctor magic seem not unlike some kind of
            Psynergy? Wouldn't it be quite fortunate if we were to get our
            hands on that power ourselves?

-----------------------------------------------------------
     -(Yes)
Kraden    : Oh! You didn't need much convincing at all, did you, Felix?



     -(No)
Kraden    : Hrmm... You would feel guilty about taking it, eh, Felix?
-----------------------------------------------------------

Kraden    : I needn't remind you, but... We're going to need every kind of
            Psynergy we can muster to complete this quest... Either way, Felix,
            we are, at the very least, obligated to deliver the Gabomba's
            message. We must fulfill our promise to the Gabomba. Then, maybe we
            can come back inside this Gabomba statue some other time to get it.

* - They depart.


#$#$#$#$#$#$#$#$#$#$#
$#  Akafubu's hut  #$
#$#$#$#$#$#$#$#$#$#$#

<game>    : Felix carried the message of the Gabomba to Akafubu.
            By the time Felix finished his story, dawn had broken.

Kraden    : Right... Well, I guess that's that!

A's Father: You are virtuous men, coming here to deliver this message.
            My son and I thank you.

Akafubu   : What do we have to be thankful of? If they had just stopped me
            from leaving the Great Gabomba, this wouldn't have happened!

A's Father: What!? If you had been more interested in your duty, you would not
            have left so quickly...

Akafubu   : But, Father! These people are trying to steal the magic of our
            people! It should be mine! Mine, I tell you! That power belongs
            to me! I'm going to be the one to get the Great Gabomba's magic!
            You'll see!

A's Father: My son, you have much to learn.

            He may look like a man, but before me, he acts like a child. See how
            he behaves when he gets excited? No matter what I say, he won't
            listen to me right now. I think he has had enough for today...

Kraden    : I see your point. Well! I suppose we should be leaving then.
            After all, our journey has only just begun. We cannot remain idle
            much longer.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

* - These speaker identifications have no relation to those prior.


   [ Outside ]
Guard 1   :{S} You didn't come to Kibombo to get revenge on us for that raid,
               did you?

               --------------------------------------------
                    -(Yes)
               How many of you are there? We've got some pretty fierce warriors,
               you know... You don't really think you can defeat all of us,
               do you?



                    -(No)
               Whew! That's good to hear. We're supposed to protect the village,
               but I feel bad for the raid.
               --------------------------------------------

           {M} No one in Kibombo really wants war with our neighbors. We want
               everyone who shares this land to share peace as well.

Guard 2   :{S} The other warriors are busy hunting right now. The food supply
               for the whole village depends entirely on the animals they catch.

           {M} With all our battles behind us, we warriors spend our time
               refilling the village food supply.

[001]     :{S} Now that the ceremony is over, I feel a touch depressed.
               I wish we could have more big events like that soon.

           {M} Now that the witch doctor ceremony is over, I've decided that...
               it was kind of fun!

[002]     :{S} Oh... I smell something delectable. We'll be eating some good
               meat soon.

           {M} You don't think anyone will notice if a sneak a little nibble
               while I'm cooking, do you?

[003]     :{S} We get to eat normal animals again! They taste so much better
               than those monsters we've had!
           {M} Lately the monsters have been increasing, and the animals are

               becoming more and more scarce. That's why everyone's so excited
               that we get to have nice, normal steaks tonight!

[004]     :{S} Good ol' meat... I love meat. I can't wait until we get some.

           {M} Gulp! The smell of that sauce over the fire is making me so
               hungry... How long until we can eat!?

[005]     :{S} It looks like there are fewer warriors in Kibombo now, huh?

               --------------------------------------------
                    -(Yes)
               All of our warriors were just local farm boys...Now that he's the
               witch doctor, Akafubu let them all return to their farming work.



                    -(No)
               You couldn't tell? I thought you might have been a little more
               observant, but oh well...
               --------------------------------------------

           {M} Covering our warriors in paint makes them scarier, and it makes
               them more intimidating. Most of our warriors aren't that strong,
               so they need every trick they can use.

[006]     :{S} Akafubu has finally completed his ceremony, and things are
               starting to calm down. Maybe now, our warriors can set aside
               their spears and return to their peaceful lives.

           {M} Everyonw was terribly worried about Akafubu's ceremony. We're all
               relived it's over now.

[007]     :{S} The Great Gabomba's mouth will remain open until Akafubu has
               earned the gift of the Gabomba. Maybe I ought to sneak in there
               and get a look around while I have the chance.

           {M} I want to look inside the Great Gabomba at least once.
               You don't suppose just peeking will get me cursed, do you?

[008]     :{S} I couldn't for the life of me figure out how our warriors got to
               Indra without a boat. But I just found out that something has
               pushed Indra into contact with Gondowan!

           {M} Because Kibombo lies hidden deep in the continent, we rarely
               hear news of the Eastern Sea.

[009]     :{S} Now that Akafubu is our new witch doctor, we shall embark on a
               path to peace. The neighboring villages have no reason to fear
               our warriors any longer. This is a signal fire. We use these
               to send messages to neighboring villages. I hope these messages
               set our neighbors' minds at ease.

           {M} I wonder if I can keep going until another village sees our
               signal and comes to meet with us... I don't care which village
               it is, just send a delegation! Fast!





   [ Buildings ]
Innkeeper1:{S} Don't worry about the beds here... We used to have insect
               problems, but not anymore. We used a special bug powder on
               our beds. It's quite harmless to humans, I'll bet.

           {M} The bed makes me itch so badly! It feels like bugs are crawling
               all over me! Whenever I get itchy, I just rub some of that
               bug powder all over myself!

Innkeeper2:{S} I can't remember how long it's been since we've had any guests.
               Tell you what... If you stay at our inn, you can have all the
               freshly grilled steak you want!

           {M} I love Kibombo's BBQ monster steak...with extra-spicy Herb sauce!
               It's a local treat that's fun to eat! ...But it's not nearly
               as fun catching the monsters...

-----

[Weapon]  :{S} The weapons I sell in this shop are ones we do not use in
               Kibombo. You find it strange that I do not sell the weapons
               we make here, don't you?

           {M} Our warriors appear so strong because of the deadly poison on
               their spears. In a war, Kibombo spears would make a powerful
               ally.

[Armor]   :{S} The only defenses we Kibombo need are our shields and our
               war paint. Our warriors think armor is for cowards.

           {M} Because our paint is infused with the witch doctor's magic,
               we're safe from attacks. I would opt for paint in any battle...
               no matter how much iron my enemy wore.

[Item]    :{S} I'm sorry, but the Kibombo spearhead poison is a tribal secret,
               used for hunting only. We can't let outsiders have it, because
               they might try to turn it toward evil uses.

           {M} If I had a coin for every time some stranger came up and asked
               me to sell them poison... If only they'd let me sell it, I could
               make millions!

-----

[010]     :{S} If you are looking for treasure, look west of the river.
               The rocky peaks there are called the belly of the continent.
               Great treasure hides there.

           {M} Sure, our legends speak of much treasure, but no one ever seems
               to have found it.

[011]     :{S} Each year, when the rains stop, our warriors look for treasure
               in the belly of the continent. Maybe the belly is hidden, or the
               treasure is also. I don't know, but they all return empty-handed.

           {M} I wonder what Oeia meant when he said that our magic is deeply
               tied to the belly of the continent...

-----

[012]     :{S} I've heard that if you head west from southern Gondowan, you'll
               see the Eastern Sea. There are two continents in the middle of
               that ocean: Hesperia and Atteka.

           {M} I know I could find more animals and grain on the far side of
               the river. If only I could go... These seasonal monsoon rains
               have swollen the river and made it too dangerous to cross.

[013]     :{S} Are you going to head to western Gondowan?

               --------------------------------------------
                    -(Yes)
               That's unfortunate. The recent rains have swollen the rivers.
               It is too dangerous for us to allow anyone to pass.



                    -(No)
               That's for the best. It is far too dangerous for anyone to be
               going out west. Perhaps a boat would lessen the danger to a
               degree...
               --------------------------------------------

           {M} Crossing the river by canoe is much too dangerous. I'd need a
               ship to get across.

[014]     :{S} You can see Atteka from the bridge in western Gondowan.
               My grandfather told me so. Someday, I'll be a warrior like my
               grandfather, and I'll be able to see it for myself!

           {M} If I'm ever going to be a warrior, I must build more muscle
               and master the art of the spear.

-----

[015]     :{S} We think it is time to inform other villages that Akafubu has
               completed the ceremony. I think they'll be glad to know that we
               no longer pose any threat to them.

           {M} I am a might warrior, trained from birth to be fierce. If you
               are feared, you are powerful! I'm... supposed to start my
               "being nice to people" training on Monday.

[016]     :{S} Many in Gondowan fear the might of Kibombo warriors. But we
               don't want to be feared. Now is the time for Kibombo to change
               its image.

           {M} It won't be easy, convincing them that we've turned over a
               new leaf... but we'll try.

-----

G. Healer :{S} Kibombo's peace is restored now that the ceremony has reached
               its end... Now, the fate of Kibombo's people depends on how
               Akafubu leads them.

           {M} I can't believe that Akafubu would change simply because he
               completed the ceremony.

Akafubu   :{S} I just can't quite grasp the Great Gabomba's magic. Still,
               I'm trying really hard to help everyone, just like the Great
               Gabomba said...

           {M} Dang! Why did I leave that stupid room so quickly?
               Stupid, stupid, stupid Akafubu!

A's Father:{S} My son has been so kind and compassionate since the ceremony.
               He's a changed man. He has focused on bettering himself and
               earning the Great Gabomba's magic.

           {M} After he became a witch doctor, Akafubu had no more reason to
               focus himself... It is good that he now has a new goal.
               He will have to work hard to earn the Great Gabomba's magic.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Gabomba Catacombs  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - After acquiring the "Cyclone" Psynergy, the catacombs--which lie below the
    hidden ladder in the final room of the Gabomba statue--can be traversed.

    At the end, another miniature statue of the Gabomba is present.

Gabomba   : By reaching this place, you have proven your power.

* - A book, the Tomegathericon (which changes one's class) appears in its hands.

Gabomba   : By rights, Akafubu should bear this power... But I shall keep my
            promise and bestow it upon the one to reach this place first!

Kraden    : I am grateful for your promise... But I am worried that we have
            done Akafubu and the Kibombo a great wrong.

Gabomba   : Akafubu has not honed his own powers, and the fault lies with him
            alone... And yet, there is a hint of truth to what you say...

Kraden    : Then what are we to do? Does this mean we won't receive your magic?

Gabomba   : As I have said, I will give the power to you. Your concern is
            misplaced. But I must add some small conditions to our agreement...

Kraden    : Wh-What kind of conditions?

Gabomba   : You must not... mention this to Akafubu. Akafubu was plainly
            ill prepared for this test. He will lose heart if he hears what
            you have done. And yet... the Kibombo have need of this ill-prepared
            leader... If Akafubu ever reaches this place, I shall teach him
            the magic as well. Promise me that you will not tell Akafubu that
            you earned this magic. Can you do this?

Kraden    : Of course!

Gabomba   : And now I shall sleep. Farewell, successor to the witch doctor.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'20] ---         [Gondowan]          --- [02'20] #$#
#$#$#                    Naribwe                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Don't tell me you just came back from Kibombo! You must be really
               brave to have made it there and back again!

           {M} Who would travel to Kibombo right now? It's not very safe right
               now.

[Item]    :{S} Strangers to our town would do well to visit the fortune-teller's
               hut.

           {M} Those who become lost should offer the fortune-teller one of
               their hard-earned items.

[002]     :{S} Some soldiers came through here looking for a guy named Piers.
               They looked unhappy that I'd never heard of him.

           {M} What kind of a name is Piers. [sic] An odd one, certainly.

[003]     :{S} I didn't see any Kibombo soldiers in the mountain pass...
               Where did they go?

           {M} I'm so glad the Kibombo aren't lurking over us in the hills
               anymore... They were here, they were there, they were everywhere!

[004]     :{S} Ouch... Some big brute came through here looking for a woman
               named Menardi. I told him I'd never heard of her, and he shoved
               me to the ground and stormed off!

           {M} What has gone wrong with the world? People have no respect for
               their elders!

[005]     :{S} A man came through a while ago. He said he was going to Kibombo.
               He hasn't come back yet. I think the guards in the mountains
               caught him.

           {M} If the man they were looking for has gone to Kibombo, they're
               better off waiting. Kibombo is a dangerous place for outsiders
               right now.

[006]     :{S} I saw smoke rising from Kibombo... Were they having a bonfire
               or something?

           {M} That smoke's been rising from Kibombo for a while... I doubt
               it's just a fire...

[007]     :{S} The smoke coming from the Kibombo Mountains is coming from a
               signal fire. The signals are hard to read, though. Whoever's
               sending them isn't terribly at it.

           {M} The signals say something has... ended? Or maybe has been chosen?
               It's so hard to figure out... I wish they were a little better
               at smoke signals.

G. Healer :{S} It's strange. As hot as it is here in Gondowan, if you head
               south, it's bitter cold... The land of Tundaria is a frozen
               wasteland that deserves its name.

           {M} The cold of Tundaria stifles virtually all living things.
               Compared to that barren land, Gondowan's heat is comforting.

[008]     :{S} The fortune-teller predicted that the Kibombo will settle down
               for a time... I hope for all of our sakes that he's right.

           {M} The fortune-teller has never been wrong... But I can't imagine
               that the Kibombo would ever really calm down.

[009]     :{S} I mentioned Magma Rock to a traveler the other day, and he was
               very intrigued. I can't be sure, but I think he might have
               headed in that direction.

           {M} I don't think anyone can reach Magma Rock now. The river is
               too deep.





   [ Buildings ]
Innkeeper1:{S} I see so many travelers... How am I supposed to remember who
               Piers is? And why would anyone come all the way to Gondowan to
               find him? What does Isaac want?

           {M} Why would Isaac travel all this way in search of a man he has
               never met? What could it be that drives him to look for this
               Piers?

Innkeeper2:{S} If Piers is traveling in your group, please give him this
               message: Isaac and his companions would like to speak with him.

           {M} He paid me a lot of money to pass this message on, but how
               would he know if I didn't? Ah, I'm too honest for my own good.
               I'll keep passing Isaac's message on to my guests.

-----

[Weapon]  :{S} Whenever I get customers from out of town, I always tell them
               the same thing... "The fortune-teller sees all." Nobody can
               resist trying it at least once.

           {M} When I look at my weapons, I can instantly tell what monsters
               they have fought.

[Armor]   :{S} If you wish to know anything, go to the fortune-teller.
               He's fast, accurate, and affordable.

           {M} I like offering armor to the fortune-teller. It usually gets me
               good results.

-----

[010]     :{S} I guess those warriors learned much about their future from the
               fortune-teller. You should do the same. Bring your items to him,
               just as they did.

           {M} The power of the fortune-teller is great. Anyone who listens to
               his advice benefits greatly.

[011]     :{S} Our fortune-teller has been saying some horrible things lately.
               He's been telling everyone that "our peace shall soon sleep."
               It's not very comforting.

           {M} The fortune-teller said that the power of nature would rekindle
               the advance of civilization. But which is better, an advanced
               civilization, or a peaceful one?

-----

Seer      :{S} If you desire a reading, stand before the table...

           {M} Items placed before me are filled with the desires of those who
               place them there. If I can sense those desires, I can answer
               that which they seek.

* - For the seer's readings, refer to section 03'03.

[012]     :{S} Reading fortunes in people's items takes a lot of energy, so he's
               not always willing to do it. But if you have 20 coins on you,
               he might be a little more willing.

           {M} After Father's been reading all day, he sleeps like a baby.
               A really loud, snoring baby.

[013]     :{S} If trouble resides in your heart, I suggest you speak with my
               father.

           {M} Father should charge more for his readings. People profit from
               what he tells them. Why shouldn't he profit from telling them?


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'21] ---           [Indra]           --- [02'21] #$#
#$#$#                      Madra                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Elder/Mayor's residence  -  Outside  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A woman is standing nearby. She speaks to herself:

Karst     : Where could Menardi have gone? Where are you, my sister?

* - Afterwards:

Karst     :{S} Have you by chance seen a girl named Menardi?

               --------------------------------------------
                    -(Yes)
               You have? And... And you're telling me that my sister is... dead?

                   --(Yes)
               If you continue these lies, I might take it upon myself to
               shut you up. Get out of my sight!

                   --(No)
               If you don't know my sister, then I have nothing to say to you.
               Get out of my sight!



                    -(No)
               If you don't know my sister, then I have nothing to say to you.
               Get out of my sight!
               --------------------------------------------

           {M} Using Psynergy on me? Are you so dense that you don't know when
               to be afraid? I don't have time to play games with you. Now,
               leave me to my thoughts!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Elder/Mayor's residence  -  Inside  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

Mayor     : Felix! You're back!

Elder Dau : And you've brought Piers with you!

Elder     : Oh! Piers! Piers, I must apologize for the trouble we've caused you.
            I'm sorry we lost your jewel...

Piers     : Don't be. Everything worked out for the best.

Mayor Dau : Piers, you said you were going to go to Gondowan. Did you make it?

Piers     : Yes. In fact, we have just returned.

Mayor     : And your jewel...

-----------------------------------------------------------
     -(Yes)
Elder     : You actually got it back from the Kibombo? Incredible...

Piers     : I was able to recover it with the help of Felix and his friends.

Elder Dau : That's wonderful! I'm so relieved! I was worried that you might
            never get it back!



     -(No)
Elder     : You didn't recover it from the Kibombo?

Piers     : That's not true, sir. Felix and his companions helped me recover it.

Elder Dau : Please! Don't startle me like that! I was afraid you might never
            get it back!
-----------------------------------------------------------

Kraden    : That's why we came back... To let you know that we've recovered it.
            Worry no more.





* - If East Indra Shore has not been visited since finishing with Kibombo:

Mayor Son : If you've already recovered your jewel, why don't you stay here
            for a bit longer?

Jenna     : Unfortunately, we can't...

Sheba     : Hey, have you seen the girl out front?

* - Jenna nods. The mayor's son seems confused.

Piers     : We must go... to the island that is my home.

Kraden    : Piers, are you... Are you sure?

* - Piers nods.

Piers     : After what we've been through, I feel I've learned a few things.

Sheba     : Like what!?

Piers     : Like... the fact that you truly are good people. And that you
            have gone to great lengths for no other reason than to help those
            in need. I have come ot realize that I, too, must do something
            to help where I can.

Jenna     : Piers...

Piers     : I have made my decision. And the sooner we depart, the better,
            right, Kraden?

* - Kraden nods.

Piers     : We shall set sail, Felix! To my ship! To the Eastern Sea!

Elder Dau : Do you truly mean to leave so soon, Piers?

Piers     : I may yet again have reason to visit your town, but... yes,
            I must go.

Elder     : You seem quite busy.



* - If East Indra Shore has been visited since finishing with Kibombo:

Mayor     : Ah, so you'll be leaving again, will you?

Elder Dau : Are you sure you must leave so soon, Piers?

Piers     : I may yet again have reason to visit your town, but... yes,
            I must go.

Elder     : You seem to be quite busy.





* - Regardless:

Kraden    : It is their youth that allows them to be so busy.

Jenna     : But we'll be back, I promise. Maybe we'll be able to visit at a more
            leisurely pace...

Mayor Son : I'd like that...

Mayor Dau : So would I!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Elder/Mayor's residence  -  Outside  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - The mayor rushes out of the house.

Mayor     : Felix, wait! I believe I promised you a reward for helping with
            the boat, didn't I?

-----------------------------------------------------------
     -(Yes)
Mayor     : Imagine! You came all this way to put us at ease, and I totally
            forget to give this to you!



     -(No)
Mayor     : Well, you may have forgotten, Felix, but I have not.
-----------------------------------------------------------

Mayor     : Regardless, I told you that I would reward you when the boat was
            fixed... That may take quite a while now, it seems... That being
            the case, I'd like to give you that reward now.

Sheba     : We can't accept it now, though, could we, Jenna?

Jenna     : Madra is still in shambles from the disaster... We couldn't possibly
            accept any gifts...

Mayor     : Nonsense! Misfortune or no, a promise is a promise!

<game>    : Felix got the Cyclone Chip.

Mayor     : I am glad that I was able to give it to you before you left.
            Your travels seem to take you from danger into greater danger.
            Please be careful.

* - The mayor returns inside.

Kraden    : Thank you, Mr. Mayor.

Karst     : ...Felix? You... He just called you Felix, didn't he? Why didn't I
            see it before? You are Felix! Then Menardi should be somewhere
            around here, too... And yet...

Sheba     : You won't see Menardi or Saturos again. Isaac killed them.
            They're probably at the bottom of the sea by now...

Jenna     : Sheba! Quiet!

Karst     : Hmph! I heard that, you wretched little thing! Can it be true?
            Is my sister dead?

-----------------------------------------------------------
     -(Yes)
Karst     : I can't believe it... No one has the power to defeat Saturos and
            my sister... Yet you all avoid my gaze... And that look on your
            faces... It... is true...



     -(No)
Karst     : No? Then where s she!? Show me my sister! What is the mater?
            Is it so very hard? You were traveling with her--bring her to me!
            She would never have left you behind... and yet you are alone...
            So it's true? She's...
-----------------------------------------------------------

Karst     : Who is this Isaac?

* - Everyone acts as though they're unaware.

Karst     : What? You feign ignorance/ Why? Would you protect him from my fury!?
            Never mind. I believe I've heard some rumors of a traveler named
            Isaac lately. Is this Isaac the same one they've been speaking of?
            Is he pursuing you? If that is the case, then this Isaac should
            show up here sooner or later.

Kraden    : How do you know it wasn't Felix who defeated your sister?

Karst     : What do you take me for? I'm a warrior, like my sister...I can gauge
            a man's strength at a single glance. Even if you doubled Felix's
            power, he would still be no match for my sister. And besides,
            I doubt Felix could find it in himself to betray my sister. He knows
            that the lives of those he holds dear would hang in the balance.

            But I must congratulate you on your successes at both the Mercury
            and Venus Lighthouses. Although your success there now prevents us
            from returning the Western Sea. You would have failed, of course,
            had we not researched how to climb those lighthouses...

* - Everyone seems a tad surprised at the remark.

Karst     : Oh, didn't Menardi tell you? Regardless, Isaac won't be getting in
            my way. You will have to find your own way to the Western Sea.
            And if you make the journey, you'll have to light Jupiter on your
            own as well! We have our own work to do, and number one on the list
            is taking care of Isaac! Are we clear on this, Felix?

-----------------------------------------------------------
     -(Yes)
Karst     : Aren't you an obedient boy... If you're worried you can't get it
            done, we could help you a bit.



     -(No)
Karst     : What's the matter? Afraid you can't perform your duties?
            We could help you a bit...
-----------------------------------------------------------

Kraden    : No, thank you. I believe we'll just find Jupiter Lighthouse on
            our own, if it's all the same.

Karst     : I see. Just don't let us down. we're going to find that Isaac...
            I'm going to find this Isaac... And I swear that the last thing
            he sees will be Karst avenging the death of her dear sister!

* - She takes her leave.

Sheba     : Wow. And I thought Saturos and Menardi had issues.

Jenna     : We shouldn't take Karst too lightly...

Piers     : Wait a moment... Karst did say "we," didn't she?

Kraden    : Yes. Saturos and Menardi traveled as a pair. Perhaps she has a
            partner as well.

Sheba     : We ought to warn Isaac that Karst is after him. Maybe we should
            try to find him first.

Jenna     : Believe me, I'd love to see Isaac again, but we just don't have
            time to look for him. Plus...

Kraden    : Even if we did find them, I think there is a good chance we'd
            end up fighting them.

Piers     : Why?

Kraden    : What we are trying to achieve, they are trying to prevent...
            And they will fight to stop us.
Sheba     : But, Jenna... Aren't you and Isaac an item? Couldn't you, you know,
            do something?

Jenna     : A... An item? No! I mean... It's not like that! Not... really...

            ...Stupid Sheba...

Kraden    : Ah! Well! Er, yes. For now, we should press onward to Jupiter
            Lighthouse, like we'd planned.

Jenna     : But... what about Garet and the others?

Sheba     : Don't you mean... Isaac?

Jenna     : Sheba! Be quiet! Sheesh...

Kraden    : *Ahem!* Are you ready to listen yet?

            They were strong enough to defeat Saturos and Menardi. They won't be
            beaten easily. We should continue on ahead, just as Saturos and
            Menardi would have, OK, Jenna?

* - Jenna nods.

Kraden    : Sheba? Piers? Are you ready?

* - They both nod.

Kraden    : Then we should be going, right, Felix?

* - Felix nods.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
Guard 1   :{S} Hey! It's you guys! It's good to see you again! You want to enter
               Madra? Yeah, sure! Go ahead! Feel free!

           {M} How much longer do we have to stand guard here? Seriously,
               there's nothing to guard again! We've already been attacked by
               everyone!

Guard 2   :{S} The mayor finally returned from Alhafra.

           {M} He was gone so long, I was starting to worry that the mayor
               would never come back.

[001]     :{S} We go to all that work getting the ship from Briggs, and now
               we can't get it to work? I guess the mayor's holding a council
               to see if they can figure out what's wrong.

           {M} They've been having so many meetings lately! I guess that boat
               must be in miserable shape!

[002]     :{S} It's not that I don't want to go to Alhafra... But what's the
               point if we can't fix the mast?

           {M} If a building has broken columns, we tear it down... Shouldn't a
               boat with a broken column be torn down as well?

[003]     :{S} The mayor asked me to go to Alhafra with him, but I'm not sure
               I should... If that ship runs on the power of the wind, how
               reliable could it really be?

           {M} Sailors are supposed to use oars to pull the boat through the
               water... So, what's a sailor supposed to to don a boat what's
               powered by wind?

[004]     :{S} I was at the mayor's house, watching them argue about why the
               boat won't move. What's so important about a mast, and what does
               it have to do with sailing?

           {M} These new boats apparently use the power of wind to cross the
               seas... I just don't understand how a big pole in the boat can
               help to capture the wind...

[005]     :{S} I wonder if the legends are true... If there really is a great
               society on a far-off island... Because if they are true, I want
               to see this island.

           {M} What was that island again? Come on, brain... Work with me...
               Lemoria? Lemurland? Lulu?

[Weapon]  :{S} It looks like the Kibombo must have been involved in the raids
               on our town... Kibombo weapons are too distinct... We found a
               bunch of them after the attacks.

           {M} The pirates and the Kibombo must have been working together.
               What an astounding discovery!

[Armor]   :{S} People are saying the Champa and the Kibombo formed an
               alliance... I don't buy it, myself.

           {M} That night, the Champa came from the east, and the Kibombo,
               from the west. That's not an alliance.

[Item]    :{S} My boyfriend, Shin, seems so downtrodden lately... I hope he's
               all right.

           {M} Shin seems terrified of Piers. I wonder what happened between
               them. Still, I guess that explains why he's been so on the edge
               lately.

[006]     :{S} I heard the boat the mayor got is much better than the battered
               raft we used to have! I also heard that the new ship can even
               sail far across the sea!

           {M} Everyone gets the urge to explore, to go out into the wild and
               see new lands... I'd love to see the world. I've love to have
               an adventure of my own!

[007]     :{S} If you have a big enough ship, you can sail anywhere in the
               world! Isn't that amazing?

           {M} How big would a ship that could go anywhere be? Probably bigger
               than a whale!

[008]     :{S} I don't know what will happen when they all head out to sea.
               They know nothing about sailing!

           {M} The people of Madra know our own lands well... but we know little
               of the world beyond. What kind of fool would think himself ready
               to sail into a world he knew nothing about?

[009]     :{S} A group of sharp-looking travelers came through here recently.
               They said they were looking for an island called Lemuria.

           {M} That island that group was asking about sounded familiar for some
               reason... Grandpa used to tell me stories about a treasure island
               when I was young. Was that the place?

[010]     :{S} Is there by any chance a girl named Jenna with you?

               --------------------------------------------
                    -(Yes)
               Ah! Those people must have been looking for you! There were four
               of them, and they looked weatherworn, but they had an amazing
               ship.



                    -(No)
               Oh... Well, if you run across anyone named Jenna, let her know
               Isaac is looking for her. You look like you travel a lot.
               Maybe you'll run across this Jenna somewhere.
               --------------------------------------------

           {M} I wonder why those travelers were in such a hurry... They looked
               so severe... You'd think they carried the fate of the world
               on their shoulders.

[011]     :{S} I don't think the mayor ever got that boat of his fixed,
               either... Got tired of waiting. I guess he's going back out again
               as soon as he finds enough people to fix it himself.

           {M} Why would anyone be happy to have a broken boat?

[012]     :{S} I thought Shin and the others were lying, but after seeing what
               I saw, I'd believe anything. They called it Psynergy and said
               it can change water into ice.

           {M} Madra is always so hot. If there were some way to create ice,
               it would be so... cool.

[013]     :{S} Say, Piers, there was another group of travelers with powers
               similar to your own. What are the odds that we should meet two
               groups with these amazing abilities?

           {M} Is turning water to ice really such a special power?

[028]     :{S} Everyone here in Madra is afraid of the Kibombo now.
               Do they scare you, too?

               --------------------------------------------
                    -(Yes)
               I saw the fear in your eyes the instant I said "Kibombo."
               Don't get worked up, though. We caught sight of a Kibombo
               smoke signal that said they had given up their warlike ways.



                    -(No)
               You must have heard their proclamation... We only just caught
               sight of their smoke signals... They have announced a truce!
               --------------------------------------------

           {M} We're still recovering from the Kibombo raid... It's no small
               wonder people are still afraid...





   [ Buildings ]
Innkeeper1:{S} Are you worried about all the fish that have been washing up dead
               on the shore?

               --------------------------------------------
                    -(Yes)
               No need to worry. Those fish all died farther out in the bay.
               The fish we cook here at the inn are caught fresh from our pier.



                    -(No)
               No?! I suppose you'd be happy if the fish up and vanished, huh?
               They're dying because the ocean temperatures are rising, but
               no one is doing anything about it...
               --------------------------------------------

           {M} I've never seen a single customer get sick fro our fish!
               Not a single one... I've never served rotten old fish in my life!
               I only use the finest, freshest ingredients in my cuisine.

Innkeeper2:{S} Has someone been telling you that we've been serving up the dead
               fish found on the beaches? Outrageous! We go to great pains to
               serve only the finest fresh fish to our customers.

           {M} Someone must have seen me burying the dead fish. I'll bet that's
               where the rumor started.

Employee  :{S} One of our guests kept asking for a weapon that he could use to
               slay a great sea monster...He kept mentioning this trident thing,
               but we couldn't help him.

           {M} It must be a very strange monster if one needs a unique weapon
               to fight it.

[014]     :{S} I guess that a lot of dead fish have been washing ashore all over
               the eastern seacoast. It's kind of sad... Imagine how much money
               we could have made if we'd caught them.

           {M} If I had a boat we could use, now would be a great time to make
               some money. We'd just need to take our nets and scoop up whatever
               we find...

[015]     :{S} I've heard that the rising ocean temperatures mean that a volcano
               is forming under the sea.

           {M} Hm... I wonder if the tidal wave might have been caused by an
               undersea eruption...

-----

[016]     :{S} Since things are finally calming down in Madra, our people are
               ready to get down to business. They seem to have thought up a
               business plan that makes use of Isaac's power.

           {M} The business plan our people have come up with is supposed to
               make us rich. I guess it must be a brilliant plan.

[017]     :{S} There's talk of might travelers who passed by here recently.
               I wish I could have met them. It seems they had powers no one
               has ever seen before. I bet those powers could be profitable.

           {M} What if we just traveled with Isaac to show off his powers...
               We could make loads of cash!

-----

[Item Sis]:{S} I've told my sister not to worry about Shin. He's tough.
               At least... he usually is...

           {M} Shin's normally so kind and gentle. I hope he gets over
               whatever's bothering him.

-----

[018]     :{S} My husband relishes those rare mushrooms growing in the Gondowan
               cliffs. I wish someone would bring some back for him.

           {M} My poor husband's getting old... Those cliffs care him now.
               In his prime, he'd have scrambled up those cliffs in no time
               for a mushroom.

[019]     :{S} How are we to climb the cliffs between here and Gondowan?
               If someone would just drop some ropes down from the top,
               it wouldn't be a problem.

           {M} I'm dying for some of those Gondowan mushrooms, but I can't ever
               reach them.



* - If you offer the Laughing Fungus:

[019]     : Oh, my... Is... Is that...

[018]     : Is that one of his most favorite mushrooms!?

[019]     : No, dear... They look similar, but these aren't quite right.
            Thanks for bringing this by, but it's just not the type of
            mushroom we like...

[018]     : Please... Won't you please try to find the mushrooms my husband
            loves so much?



* - If you offer the Healing Fungus:

[019]     : Oh, my... Is... Is that...

[018]     : Is that one of his most favorite mushrooms!?

[019]     : Did you climb all the way up those cliffs just to get that mushroom
            for us?

[018]     : That's the nicest thing anyone has ever done for me. I have to
            thank you for this!

[019]     : But what could I have that a warrior like you would want?

[018]     : That's a tricky one...

* - They head upstairs and return with a Mars Djinni.

[018]     : I don't know if you want a pet, but this is all we can offer.
            Take care of it!

<game>    : Felix found the Mars Djinni Char!

[019]     : I can't wait for dinner tonight. Batter-fried mushrooms! Mmm!

[018]     : This here's enough of a mushroom that we'll be eating it for days!



* - After having offering the Healing Fungus:

[018]     :{S} This here's enough of a mushroom that we'll be eating it for
               days!

           {M} These mushrooms will make any meal taste amazing!

[019]     :{S} I can't wait for dinner tonight. Batter-fried mushrooms! Mmm!

           {M} The more I think about dinner tonight, the more I drool...

-----

[020]     :{S} One of the sailors, Isaac, was very curious about Piers's ship.
               A little TOO curious. It looked like he had a similar boat,
               almost identical to Piers's.

           {M} We've had a lot of strange visitors ever since Piers showed up.

[021]     :{S} Some sailors came through recently with a ship similar to
               Piers's. I'd never seen one before, and now they're everywhere.
               Are they new?

           {M} Oars, I understand. Hey, I'll even give a sailboat a try...
               But there's no way I'm setting foot on a ship powered by some
               fool magic thingie.

-----

Healer    :{S} I've noticed lately that the temperature of the ocean has been
               slowly rising. It is a bad omen, I say. Be wary if you plan to
               set sail soon.

           {M} I knew the temperatures were rising slowly over time. But now,
               it's plain to see that the temperatures are rising at a
               dramatically higher rate.

[022]     :{S} The ocean's been warming up a lot, and we're seeing lots of
               dead fish washing up on shore. At this rate, there aren't going
               to be any fish left for us to catch for food.

           {M} Our new ship is spectacular, but if we can't find some new
               fishing spots, it does us no good at all. Tidal waves, raids on
               our town, and now the warming ocean waters... What's going on?

[023]     :{S} When the ocean warms, the Eastern Sea beckons... Seek for the
               center, the legends say. These legends are known to nearly every
               sailor. It would be wise for you to remember it, too.

           {M} Seafaring towns know many more legends of the sea... But a few
               of the sailors passing through here have told their share of
               stories of the salty sea.

-----

[024]     :{S} I wonder if the Kibombo have truly set aside their spears and
               returned to peace...

           {M} The salesman that just came back from Gondowan claims the Kibombo
               are peaceful now... But if we relax, we won't be ready for their
               next attack.

[025]     :{S} Our salesman said Kibombo's ceremony is done, and he claims that
               they're peaceful again. I'll be so relieved if what he said
               turns out to be true.

           {M} The continent shift makes it feel like we're sharing backyards
               with the Kibombo... We'd be so happy if we could live in peace
               without having to fear their spears.

-----
* - Elder and mayor's residence:

Elder     :{S} We just have to finish repairs on that boat we left in Alhafra...
               We've had several meetings already, discussing our next course of
               action.

           {M} Why won't the mayor of Alhafra repair our boat? If we could get
               that ship, Madra would embark on a voyage to prosperity...

Mayor     :{S} I know you went to a lot of trouble to get us that boat, but we
               just had to give up on it. We couldn't just sit and wait in
               Alhafra until the thing got fixed.

           {M} All of this could have been avoided if the people of Alhafra's
               offer to repair the boat was genuine. Now, I refuse to let that
               boat fall into the hands of Alhafra and its mayor.

Mayor Wife:{S} I'm so relieved Piers got his jewel back.

           {M} I can't believe it... Despite all my worrying, they got that
               jewel back like it was nothing.

Elder Dau :{S} I can't believe Piers actually went all the way to Kibombo to get
               his jewel back. That's so... dashing!

           {M} I felt a little responsible for Piers losing his jewel. I'm so
               happy he got it back!

Mayor Son :{S} I like you guys a lot. I'm sad that you're leaving.

           {M} I wish they'd tell me all about their adventures!

Mayor Dau :{S} My daddy went to Gondowan, and all I got was nothing.

           {M} I'm so glad Daddy got home safely.

Elder Wife:{S} Gondowan is such an awful, dangerous place... I never imagined
               for a second that Piers would make it back here safely.

           {M} Piers said he was going to Gondowan alone, but now he has some
               friends with him. That's nice. If he'd been all alone, I'm sure
               he would have been eaten by monsters.

-----
* - Prison:

Guard 1   :{S} When Isaac and his party heard about Piers, they seemed shocked.
               They said they were going to follow you to Gondowan.

           {M} So, this Piers fellow must be a friend of Isaac... Why else
               would they go all the way to Gondowan for him?

Guard 2   :{S}   * - He approaches a puddle.

               Uhhhnnn... UHHHNNN!

                 * - He backs up.

               They told me that you make Psynergy by focusing your mind...
               I've been focusing nonstop for days, but do you see any ice? No!


                 * - 2nd+ time:

               How can anyone just create ice by thinking about it? I mean,
               imagine how much power you'd have if you could just think,
               and things happened!

           {M} I knew I should have asked them how to make ice...

Man 1     :{S} Shin's developed a terrible fear of the cold. He's afraid of
               being turned into a block of ice. Tell Piers to cool it with the
               ice routine, OK?

           {M} I understand why Shin's scared of Piers, but I think he might be
               overdoing it.

Shin      :{S} Oh! Piers! After the way we treated you, I thought you'd never
               come to Madra again! I know we were not very nice to you
               before... I hope you can forgive us.

           {M} Even the sound of the name "Piers" sends a chill down my spine.





   [ Madra Catacombs ]
[027]     :{S} It seems no one is really happy that the mayor got this grand,
               new ship. The poor mayor...

           {M} Our mayor's done so little for us up until now... We should
               at least thank him for the boat.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'22] ---           [Indra]           --- [02'22] #$#
#$#$#                 East Indra Shore                #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - If Madra has not yet been revisited:

Piers     : My ship! At long last... I have returned to my ship.

Kraden    : Well, Piers?

Piers     : I'm thrilled... I'm just happy to be back with my ship.

Sheba     : Uh, that's not what Kraden's asking...

Jenna     : You forgot, didn't you, Piers? When we talked in Kibombo?
            Remember what Kraden asked?

Sheba     : He wanted you to take us to your home... To Lemuria.

Jenna     : Remember how we said we'd talk about it later? Well, it's later now,
            Piers.

Piers     : Oh... Is it? I suppose we have to talk about it sooner or later.
            You shall have your answer.

Kraden    : Piers... if you do not wish to take us, you do not have to.
            Just tell me honestly. And if not, well, we'll just have to
            get ourselves a boat and find our own way to Lemuria.

            Right, Felix?

-----------------------------------------------------------
     -(Yes)
Jenna     : What's with the guilt trip? Piers hasn't even given us his answer
            yet!

Sheba     : Kraden! Felix! Stop trying to pressure Piers!



     -(No)
Jenna     : Sheba is right! You guys just let Piers give us his answer!

Sheba     : I agree with Felix. We shouldn't try to pressure Piers, Kraden.
-----------------------------------------------------------

Kraden    : But that's not what I was--

Piers     : Don't worry, Sheba... I've actually been thinking about this
            quite a bit. I just never got the opportunity to mention it before.

Kraden    : Well? Well!? It's not nice to test the patience of an old man.
            Will you take us or not?

Piers     : We will go to Lemuria, Kraden.

Kraden    : I figured it was too much to... What did you just say!?

Piers     : I will take you to Lemuria.

* - Kraden appears shocked.

Jenna     : Kraden? Are you OK?

* - His body seems to shake as he nods.

Piers     : Is he OK!?

Kraden    : Piers! Are you... Are you serious?

Piers     : After what we've been through, it would be wrong to deny you.
            That's what made up my mind.

Sheba     : What's what made up your mind?

Piers     : The fact that you are truly good people. You have gone to great
            trouble to help one whose problems needn't have concerned you...
            Witnessing that kindness... It made me want to help, too.

Jenna     : Piers, you...

Piers     : No, Jenna. Please, don't say a word. I've made up my mind.
            I shall be leaving immediately, but I want you to come, Kraden.
            Let us set sail, Felix! To my ship! And the Eastern Sea!

Kraden    : So at long last I will finally reach Lemuria...

Sheba     : I wonder what kind of advanced civilization we'll find in Lemuria...

Jenna     : I'm actually excited to find out!

* - Piers seems concerned about something.

Jenna     : What's wrong, Piers?

Piers     : It just occurred to me... The mayor of Madra and his wife must be
            worried about me. I'd feel bad if I didn't let them know I was
            all right before leaving Indra. We should go tell them that I've
            retrieved me orb. Then they wouldn't have to worry.

            Is that acceptable, Felix? Can we stop by Madra briefly before
            we leave for Lemuria?

Kraden    : What do you say, Felix? Shall we go see the mayor?

-----------------------------------------------------------
     -(Yes)
Kraden    : I have no objection, so why not? Let's go.



     -(No)
Kraden    : Don't worry about me. I've waited this long. I can wait a little
            longer. Let's go see the mayor!
-----------------------------------------------------------

Kraden    : But we must depart as soon as we're done at the mayor's house,
            Piers.

Piers     : Oh, thank you!





* - If you try to board the ship:

Piers     : Then let's waste no time! We should set out for Madra at once!


#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Ship  -  Main deck  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$

* - After having visited Madra:

Piers     : At last, I'm back on my ship. Finally, I can return to my beloved
            Lemuria. Wait there a moment.

* - He uses the Black Crystal to open a previously-sealed door.

Piers     : To set sail, we must go down to the power chamber belowdecks.
            Let's head down.

* - Inside, the ship has been swarmed with "Aqua Jelly" (squid) monsters.


#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Ship  -  First room  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#

Bookcase  :{O} It looks like there's a captain's logbook in here.
               There's something about an unreported trip to Lemuria in here...
               I guess they were rushed.

Wardrobe  :{O} It's pleasantly cool.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Ship  -  Power chamber  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

Piers     : How did all these monsters get on board? I could swear I locked the
            door when I left... It doesn't matter. Once get this ship moving,
            I'm sure they'll all jump ship. OK, now, I must set the black orb
            into this pedestal.

* - As he does so, the room lights up and the ship moves.
    Everyone heads above deck.

Piers     : Take the tiller, Felix!

* - Felix doesn't quite seem to know what that would be.

Pier      : If you hope to reach Lemuria, you'll have to learn a few things
            about handling a ship. I think we ought to sail the Eastern Sea
            until you get the hang of it.

Sheba     : Kraden, shouldn't we be heading straight for Lemuria?

Kraden    : Well, I suppose if we have to learn to sail, it's better to do it
            sooner than later...

Jenna     : Then I want to go to Lalivero! And Tolbi! Oh! And Vale!
            Can we go to Vale?

Piers     : I'd love to see your hometown, Jenna! Shall we? Let's do it!
            To Vale we go!

-----------------------------------------------------------
     -(Yes)
Kraden    : I don't think that's a good idea.



     -(No)
Kraden    : I'm with Felix. I don't think that would be wise course of action.
-----------------------------------------------------------

Piers     : Come, now! Why not?

Kraden    : Think about the roads we have traveled to get where we are...

Sheba     : I can't... I was never any good at geography.

Kraden    : Then allow me to explain... The coastline of Angara, the continent
            in which Vale lies, is surrounded by rocky cliffs.

Jenna     : Oh... You don't think Piers's boat could land there?

Kraden    : And as for Gondowan, I would guess the people from Lalivero are...
            looking for us.

Sheba     : He's right. Saturos and Menardi went a little wild in Lalivero,
            and you were all with them.

Jenna     : Oh... But Sheba can explain the situation for us. Faran and the
            Laliverans would understand, I'm sure.

Sheba     : And then they'd make me stay in Lalivero! Would you just leave me
            there, Felix?

Jenna     : Oh yeah... Maybe that wouldn't be such a good idea after all...

Kraden    : Then it's decided!

Piers     : What's decided?

Kraden    : The sea is vast... We can go wherever we please! So, let's explore
            a bit, Felix!

Sheba     : That's a great idea! We've already met werewolves and discovered
            new Psynergy.

* - She mentions werewolves even if Garoh was not visited.

Sheba     : I'm sure there's even more out there waiting for us to find it!

Jenna     : Wow! This is going to be great!

Piers     : Hmm... The seas can be quite dangerous. It won't be my fault if
            something happens, Kraden.

Kraden    : To the open sea, Felix!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'23] ---     [Great Eastern Sea]     --- [02'23] #$#
#$#$#                 Apojii Islands                  #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$
$#  Aqua Stone  #$
#$#$#$#$#$#$#$#$#$

* - Upon using Douse on the stone, it shines and a rain quickly starts to fall.
    A current of Psynergetic energy makes its way to Aqua Rock across the sea,
    causing five moai statues to move aside, unblocking a path.

[007]     : What... What just happened? That rock couldn't have heard my
            wishes... That's impossible! It's got to be. Well, OK then...
            Maybe we should try putting some more of our wishes into the rock.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} This is Apojii, the easternmost island in the Eastern Sea!
               Wherever you're from, you've come a long way. You must be here
               to see Gaia Falls!

           {M} Looking over Gaia Falls really makes you feel small and
               insignificant.

[002]     :{S} I don't know what brings you to Apojii, but you'd better not be
               planning anything stupid.

           {M} Apojii has so many nice sights... Gaia Falls to the east, and
               Aqua Rock to the south.

[003]     :{S} Whatever you do, don't sail out to the eastern edge of the sea...
               That's where the world ends. No one knows where the falls go,
               but you won't come back!

           {M} The currents near Apojii run swiftly because we're so near to
               Gaia Falls.

[004]     :{S} On Aqua Island, you can see the guardian moai. Because of the
               moai, no one can climb the craggy mountain.

           {M} Why would anyone build a guardian statue out on Aqua Island?
               What's to guard?

[005]     :{S} Have you any idea what it's like living on the edge of the world?
               One wrong step, and down you go!

           {M} Well, at least Gaia Falls will put an end to a few silly
               arguments. After all, if it's got an edge and you can fall of it,
               the world is clearly FLAT!

[006]     :{S} The huge waterfall at the edge of the world is known as Gaia
               Falls. 

           {M} All of the ocean's water is spilling over Gaia Falls...
               Where does it all go? And more importantly, what happens
               when all the water's gone over the edge?

[007]     :{S} If there's nothing on Aqua Island, then what are those moai
               guarding, anyway?

           {M} Aqua Rock must be the secret hidden on Aqua Island. One day,
               I'll have to scale its peak.

[008]     :{S} Do you think if you fall off of Gaia Falls that you keep on
               falling forever and ever?

           {M} I wonder where I'd be if I fell off Gaia Falls... I'd like to
               know, but I don't want to find out firsthand!

[009]     :{S} When they come of age, all the men of Apojji go to Aqua Island.
               Will I, too?

           {M} Aqua Island is supposed to be dangerous, but that's why I want
               to go!





   [ Buildings ]
Innkeeper1:{S} Wow! You look just like the guy who showed up in the fancy boat.
               He slept for a long time... He must've had a really long trip.

           {M} I'm sure that boat is quite comfortable... But no matter how nice
               your boat is, you can't beat sleeping in a nice, dry bed on land.

Innkeeper2:{S} You guys aren't the warriors who came in that boat, are you?

               --------------------------------------------
                    -(Yes)
               Hmm... A while ago, some others came in a boat much like yours...
               I'm sure back on the mainland that those boats are all very
               popular, aren't they?



                    -(No)
               It's not nice to tease an old lady! If that's not your boat,
               then how did you get here?
               --------------------------------------------

           {M} Those guys on the other boat must have been pretty well off...

-----

[General] :{S} It'd be nice if we could import some items that our visitors
               would like.

           {M} No one ships to Garapas so I wonder if wares are scarce.
               On the other hand, I suppose some wares are unique to Garapas.

-----

[004]     :{S} He's too old to try now, but my husband used to dream of scaling
               Aqua Rock.

           {M} He always wanted to climb to the peak of the mountain on Aqua
               Rock. But he spent all his time studying that Aqua Stone instead.
               I always wondered why.

[005]     :{S} That old Aqua Stone is supposed to be the key to getting onto
               Aqua Island.

           {M} You unlock the Aqua Stone by making it damp, but splashing
               springwater [sic] on it won't work.

-----

G. Healer :{S} This little island must seem quite boring to you sophisticated
               mainlander types. But we have our share of hardships and trials.

           {M} Whenever visitors come out, the islanders start to complain about
               their lives. But they don't realize that they live better here
               than they ever could in Osenia.

[007]     :{S} I'd love to go to the mainland. I want to go somewhere without
               any ocean!

           {M} I wonder what it's like, standing in the middle of a vast ocean
               of grass or sand.

[008]     :{S} I'm sick of living on this boring island paradise!
               Ah! Does thinking that make me a bad person?

           {M} Maybe they'll take me with them if I ask for a job! I can swab a
               mean deck!

-----

[009]     :{S} There's this guy in town who spends his time at the spring,
               staring at the Aqua Stone.

           {M} I just wish he's spend some time at home. I'm fed up with his
               nonsense!

[010]     :{S} Why does my father keep staring at that rock every day?

           {M} I can't ever tell what kind of mood Mom and Dad are in.
               At least they're not fighting.

-----

[011]     :{S} I absolutely refuse to let my son swim in the ocean until he is
               an adult.

           {M} I sink like a rock. It always embarrasses my son to see me try
               to swim. I'm afraid he's no better than I am, but he still wants
               to practice and get better!

[012]     :{S} The currents around Apojii are just too strong to let children
               swim on their own. They're too strong for a lot of the adults,
               too... They can just wash a person away!

           {M} Poor boy...His father sinks like a rock, and I know it's genetic.
               So he's not allowed to swim!

[013]     :{S} Hey, mister! Did you know that all the kids are calling you
               their hero?

           {M} Wow! He swam in the ocean and survived the currents!
               And he's looking at me!

[014]     :{S} I'm not allowed to go into the ocean.

           {M} It's stupid that I'm not allowed to swim just because Dad doesn't
               know how... Someday, I'll show him... I'll show them all!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'24] ---     [Great Eastern Sea]     --- [02'24] #$#
#$#$#                    Aqua Rock                    #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Pedestal before final area  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

<game>    : It's a column with a spot where you can place something.

* - Choosing to place the Aquarius Stone, acquired in Rock, results in
    the water between the two ledges to the north being parted, leading to...


#$#$#$#$#$#$#$#$#$
$#  Final area  #$
#$#$#$#$#$#$#$#$#$

<game>    : Felix checked the tablet. It has strange characters carved on it.

            Wielder of Water's strength... Lay your hands upon this stone.
            If th'art worthy, the power to drain away the standind water shall
            be yours.

Piers     : Water's strength, huh? That sounds like my sort of thing,
            doesn't it?

* - Felix nods.

<game>    : Piers tried to touch the stone slate.

* - It rises into the air, as does Piers as the tablet's energy surrounds him.

<game>    : Piers learned Parch.

* - Water suddenly fills up the space around the ledge on which they stand,
    cutting off access to the rock ladders that led from another ledge,
    into the space, and up to the current ledge.

Piers     : What went wrong? What are we going to do, Felix? Maybe our power
            is being tested.

* - Indeed--the water must be evaporated via Parch.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'25] ---     [Great Eastern Sea]     --- [02'25] #$#
#$#$#                      Izumo                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Northwesternmost building  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A girl sits on the floor, in tears. Hearing Felix's footsteps, she says:

Kushinada : Susa, don't come for me...If I see you, I'll surely lose the courage
            to sacrifice myself for Izumo. If I run, Lady Uzume and all of Izumo
            will suffer greatly... Please... Don't come for me. Lady Uzume has
            foretold the coming of a hero, and I believe her... And so I shall
            remain here, until the coming of the next full moon... and the hero.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Uzume's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

Uzume     : Susa's not here. I believe he went to Mt. Mikage. He believes he
            can save Kushinada, and so he has gone to fight the serpent.
            He truly believes he can defeat the Great Serpent of Mikage.
            It's all for naught, though, as a hero will certainly appear and
            destroy the great serpent. If the serpent defeats Susa, I'll...
            be alone.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} We've had a lot of trouble here in Izumo lately. I don't want to
               scare you, but... you should leave, and fast. Right now.
               Seriously. Run.

           {M} The Great Serpent of Mikage has awakened...What does it all mean?
               That dragon is the guardian of the island, so why is it treating
               us so cruelly?

[002]     :{S} Lady Uzume doesn't want to sacrifice Kushinada. But that's the
               only way to appease the serpent...

           {M} I'm sure that kindhearted Lazy Uzume doesn't want to sacrifice
               anyone.

[003]     :{S} Choosing the next sacrifice by lottery seems such a harsh method.
               I am far too old to understand the ideas of these modern times.
               They seem far too extreme.

           {M} Sacrifices as great as this should not be determined by chance
               alone...

[004]     :{S} The daughters of the family in that home requested that we use
               a lottery to choose the victims.

           {M} Kushinada's always had bad luck at games of chance. I'll bet
               those girls were counting on it.

Okuni     :{S} My name's Okuni. I'm a great dancer... Except I don't feel
               much like dancing these days.

           {M} I'm not going to be sacrificed, but that doesn't mean I'm happy.
               My dear friend Kushinada doesn't deserve this, either...

[005]     :{S} Susa's going to try to kill the serpent and save his beloved
               Kushinada. He's so fearless!

           {M} What if losing Kushinada makes Susa return to his wild ways?
               I hope he fights the serpent... If he loses, at least he won't
               have to bear living without Kushinada.

[006]     :{S} A brave warrior will appear to defeat the serpent by the next
               full moon... It's just a legend, though. No one believes that.
               No one.

           {M} Why won't anybody listen to Lady Uzume? They've always trusted
               her, at least up until now...

[007]     :{S} As a child, Susa was as wild as could be and brought his elder
               sibling, Lady Uzume, much strife. Kushinada is the one who tamed
               his wild ways. Of course, no one wants to see her sacrificed.

           {M} Lady Uzume loves her brother dearly... I'm sure she'd take
               Kushinada's place if she could.

[008]     :{S} See this ring of giant stones? They've been here for ages. No one
               knows who put them here. See how they make this beautiful circle?
               Except for that one, right?

               --------------------------------------------
                    -(Yes)
               Susa moved it... He didn't even use his hands. He surely holds
               the secrets to a great power.



                    -(No)
               You're... not terribly observant, are you?
               --------------------------------------------

           {M} Why does Lady Uzume have me guarding these ruins? What a waste
               of time...


             * - After moving the misplaced stone into its proper place:

           The misaligned stone! It's back in its original position!
           How did this happen!? Hmmm... Either Susa or Kushinada must have
           moved it when I wasn't looking.

             * - The stone was in a position such that it could only be moved
                 via Psynergy.

                 Once all of the stones are in place, a tile moves aside,
                 allowing access to a ladder that leads to Izumo Ruins,
                 where the Ulysses summon tablet is located.


           {S} Can you imagine what it must be like to have the power to move
               stones without touching them? That anyone should possess that
               power is truly amazing.

* - In front of the building where Kushinada is:

Guard 1   :{S} Even if Susa tried to rescue Kushinada, she wouldn't just
               run away with him. I think she still believes that a hero will
               appear and defeat the serpent. That must be it.

           {M} Lady Uzume says that a hero would appear, but I don't know...
               There's no hero coming... If Susa came running past me with
               Kushinada, I wouldn't stop them.

Guard 2   :{S} Yeah, Susa came through here on his way to save Kushinada.
               The jerk knocked me flat and just kept on going... He was
               totally wild...

           {M} You know, I can't stand Susa, but I understand how he feels.
               Kushinada's a really sweet girl.





   [ Buildings ]
Innkeeper1:{S} Of course, I knew the legend of the great serpent... Everyone
               does! But I didn't believe it! Sacrificing a young girl to the
               serpent year after year? It's too cruel to be true!

           {M} Things like this are really going to hurt the inn... get get few
               enough travelers as it is!

Innkeeper2:{S} If I were younger, I might have been the sacrifice... Ahh...
               It's so horrible!

           {M} What does that serpent plan on doing with those young women?
               Surely, it doesn't intend to marry all of them!

-----

[General] :{S} Izumo's leaders have always possessed certain special powers.
               Always. And let me tell you, the combined power of Susa and
               Lazy Uzume is stunning to see.

           {M} The power that Lady Uzume and Susa possess comes from their
               ancestors. It cannot be learned, and it cannot be imitated.

[009]     :{S} One day, Kushinada put on a display of power so great that it
               almost rivaled Susa's! It's such a shame... I really wanted to
               see how strong she might have become.

           {M} It was the day those bright rocks fell from the sky...That's when
               Kushinada gained her powers.

-----

[010]     :{S} What I want to know is, what caused our legendary guardian to
               awaken?

           {M} The serpent is only supposed to awaken if the land is in
               grave danger. I wonder what calamity is going to befall us...

[011]     :{S} The Dragonsbane seems to have put the serpent under... but for
               how long?

           {M} The serpent will drink as much Dragonsbane as it can find,
               right down to the last drop. Nobody knows why they like it
               so much, considering how much it weakens them... It must be
               like catnip to them.

[012]     :{S} A while back, the volcano erupted on the mainland. We saw
               brilliant flashes of light to the west. The great dragon awoke
               shortly afterward. It caused a terrible panic through the island.

           {M} I wonder if all the recent disasters aroused the dragon from his
               slumber on the mountain.

[013]     :{S} I can't find my dagger... I had it earlier... Where did it--
               I wonder if Susa...

           {M} According to legend, that's the only thing that can put the
               serpent back to sleep. As for the dagger... I'll bet Susa's
               planning on using it to save Kushinada.

[014]     :{S} I am old, and I've had enough of this world. Why wouldn't I make
               a good sacrifice for the dragon?

           {M} Our guardian serpent is really just a dragon. Why do dragons
               always want maiden sacrifices?

[015]     :{S} The serpent can't stand sunlight, so it only shows up in the
               village at night. Just as the legend says.

           {M} There's no way to get sunlight into the serpent's cave on
               Mt. Mikage. Just no way...

-----

[016]     :{S} I'm so relieved that I'm not this year's sacrifice, but what
               happens next year?

           {M} I only suggested this lottery idea because I didn't want to be
               sacrificed. It looks like Kushinada really does have bad luck,
               like everyone says...

[017]     :{S} Okuni, Kushinada, and Lady Uzume all drew in the lottery to
               choose the next sacrifice with us... I can't believe we drew
               Kushinada. Is that chance? Fate? I guess you never know...

           {M} Susa's been so sad all the time, ever since Kushinada was
               named the next sacrifice. I never liked the old, wild Susa,
               but he's so different now. Maybe I can be his new girlfriend.

[018]     :{S} If Lady Uzume's name had been drawn in the lottery, would she
               have been the next sacrifice?

           {M} Lady Uzume's been able to focus on governing Izumo lately.
               I think it's because Susa's calmed down.

-----

G. Healer :{S} Why would our guardian spirit demand a sacrifice?
               It's inexcusable! A true guardian would never require
               such a cruel tribute.

           {M} If only I possessed the power to prevent this from happening.
               Please grant me strength...

[019]     :{S} When I get older, I might have to be a sacrifice, too...
               ...What's a sacrifice?

           {M} Nobody wants to be a sacrifice, so a sacrifice must be something
               pretty scary.

[020]     :{S} *Sniff* How could we sacrifice our beloved Kushinada?
               It's not fair!

           {M} I don't want the serpent of Mt. Mikage to eat Kushinada.
               Oh, won't somebody help her?

-----
* - Uzume's residence.

Uzume     :{S} If the serpent defeats Susa, I'll... be alone.

           {M} I pray that our guardian's anger is not aroused and that Susa
               will be protected...

Drummer 1 :{S} The serpent ate all our food and vanished into the darkness.
               It ruined the festival.

           {M} Before the serpent ate all our food, it was a terror to behold...
               But afterwards? He wasn't so bad. No doubt about it, that serpent
               sure knows good food when he eats it.

Drummer 2 :{S} The serpent lives on Mt. Mikage. In our tongue, its original name
               meant "the undying mountain." As long as the serpent lives on its
               peak, I doubt the serpent will ever die, either.

           {M} Legend has it that Mt. Mikage is enshrouded by a mysterious
               power. I wonder if that's the source of the serpent's eternal
               life.

Dancer 1  :{S} There's no point dancing if Okuni's not here...

           {M} Okuni's such a great dancer. It's just so much more fun
               when she's here to dance with us.

Dancer 2  :{S} The serpent attacked the town one night during a festival.
               It didn't leave until it had eaten all of the food we'd prepared
               for our feast...

           {M} The serpent would eat up anything we put in front of it!
               Its hunger knows no bounds.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'26] ---     [Great Eastern Sea]     --- [02'26] #$#
#$#$#                    Gaia Rock                    #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#
$#  Mountaintop  #$
#$#$#$#$#$#$#$#$#$#

Altar     :{O} I'm... sensing something...

* - Using Reveal, the "Dancing Idol" (an animate doll) appears. After taking it:

Altar     :{O} I can't feel anything...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Interior  -  1st room  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

Altar     :{O} It looks like something can be placed here.

* - Putting the Dancing Idol on the altar causes the two dragon head statues
    to move aside, each revealing a pathway.


#$#$#$#$#$#$#$#$
$#  Interior  #$
#$#$#$#$#$#$#$#$

* - Four beams of sunlight are cast through holes in a certain room's floor,
    hitting orbs in the Great Serpent's lair and refracting onto the beast,
    thus weakening it.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Great Serpent's lair  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - Susa is standing by the serpent, which has been drinking Dragonsbane (a type
    of water that dragons seem to quite enjoy, despite the harm it causes them).

Susa      : At last... The serpent has finally had its fill. This is the chance
            I'd hoped for. I will defeat you before the next full moon and
            rescue Kushinada myself!

* - He draws his sword.

Susa      : All right, you so-called guardian! Let's see what you've got!

* - He lunges at it, but it doesn't so much as flinch. Susa tries again,
    but still to no avail.

Susa      : That's weird... It didn't even react...

* - It spits out a fireball at Susa, knocking him to the ground.

Susa      : Feeding the serpent Dragonsbane isn't weakening it enough for me to
            beat it!

* - Before approaching the dragon:

Susa      :{S} I'm done for... That dragon has finished me off...

           {M} Who do they think they are? I'm the only one who can save
               Kushinada.
* - After defeating the Great Serpent:

Kraden    : It looks like the dragon is in bad shape, but it doesn't seem like
            it's close to dying...

Susa      : Even though the serpent's been defeated, I can't rest! Be still,
            serpent, and I will grant you peace.

* - He lunges at the beast; this time, it is too weak to defend, and is felled.

Susa      : With this, Kushinada's life has been spared. You have my sincerest
            thanks.

* - He starts to leave.

Kraden    : Where are you going?

Susa      : To Kushinada, of course.

* - He departs. Felix's group begins to as well, but stop as a tablet rises
    from the sands near the felled dragon.

<game>    : Felix searched the slate. There is an inscription.

            Wielder of Earth's might, Lay [sic] your hands upon this stone.
            I shall grant thee the power to melt into the earth, the power
            of Sand!

Kraden    : Wielder of Earth's might... That'd be you, Felix. Touch it.
            Go on, don't worry!

* - Felix nods.

<game>    : Felix touched the rock.

* - It rises into the air, as does Felix as the tablet's energy surrounds him.

<game>    : Felix learned Sand.


#$#$#$#$#$#$#$#$
$#  Exterior  #$
#$#$#$#$#$#$#$#$

* - Susa is lying on the ground.

Susa      : I'm not dying...I'm just so tired...I'm going to lie down for a bit.



Susa      :{S} If you're going to Izumo, tell my sister that I'm still alive.

           {M} I really got worked over, but as long as Kushinada's safe,
               it was worth it.



* - When leaving, Susa speaks again.

Susa      : You're going to tell Kushinada that you defeated the serpent,
            aren't you?

-----------------------------------------------------------
     -(Yes)
Susa      : Ha ha ha! Of course! That's exactly what happened!



     -(No)
Susa      : Please, you were the ones to defeat it, so you should be honest and
            accept credit.
-----------------------------------------------------------


Susa      :{M} Kushinada's safe... She's safe! Nothing else matters.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'27] ---     [Great Eastern Sea]     --- [02'27] #$#
#$#$#                      Izumo                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Uzume's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - A man has informed Uzume and Kushinada of the recent events.

Uzume     : Warriors appeared from within Mt. Mikage?

Man       : Yes... After the serpent's roar, these warriors appeared.

Uzume     : So, it wasn't Susa who defeated the serpent, but those heroes...

Man       : It might have been...

* - Uzume seems upset over the statement, given Kushinada's presence
    (even though Uzume was the first to suggest it).

Man       : Lady Kushinada, please forgive me...

* - Kushinada turns to Uzume.

Kushinada : I don't care who defeated the serpent... I'm more worried about
            what happened to Susa.

Uzume     : So, Susa never came down from Mt. Mikage?

Man       : He returned to the village after the heroes appeared, and he knew
            the serpent was defeated.

Kushinada : Oh, Susa...

* - Uzume notices Felix's group.

Uzume     : Who are you? This is my home, and I am having a private
            conversation. Leave at once!

* - The man seems concerned about Uzume's reaction.

Kushinada : What is it?

Man       : There can be no doubt... These are the heroes who appeared on
            Mt. Mikage.

Uzume     : Are you the ones who defeated the serpent?

Kushinada : So it was you...

Uzume     : My apologies... You are welcome here.

Kushinada : Who are you?

Kraden    : I'm Kraden, and this is Felix. Behind him is Piers.

Piers     : Pleased to meet you.

Jenna     : I'm Jenna, and this is Sheba.

Kraden    : We're on a quest. Our travels across the Great Eastern Sea
            brought us here.

Kushinada : You were seen coming down from Mt. Mikage. What brought you to
            such a dangerous place?

Sheba     : To complete our quest, we need many types of Psynergy.

Uzume     : Psynergy?

Kushinada : What is Psynergy?

Kraden    : Psynergy is many things... The power to move things with one's mind,
            to heal, to create.

Uzume     : All with one's mind? Tell me, is it something like... this?

* - She demonstrates Move.

Uzume     : Is that the power you're talking about?

* - The group seems quite surprised.

Jenna     : That power? Lady Uzume?

Uzume     : It's not mine alone. Kushinada and Susa possess it as well.

Kushinada : This is the power we possess. I assume you have something like it
            yourselves?

-----------------------------------------------------------
     -(Yes)
Kushinada : So, you call what we do "Psynergy," and you can do it, too?



     -(No)
Kushinada : I thought so. Only those who can wield the power can see it.
            And you did see it, didn't you?

Piers     : Felix, there's no need to hide our abilities from them, is there?

Kushinada : So, you call what we do "Psynergy," and you can do it, too?
-----------------------------------------------------------

Kushinada : If you already have Psynergy, why do you need more of this power?

Susa      : Their powers are different from our own. There seem to be many forms
            of Psynergy.

* - Susa enters the building.

Uzume     : Susa!

Kushinada : Susa... So, you lived after all, Susa...

Susa      : Yes, I've survived, and I've made it home to you both.
            Thanks to them, actually...

Uzume     : Felix, our gratitude to you and your friends grows deeper each
            passing moment.

            Susa, you spoke of different types of power. Tell me, what did
            you mean?

Susa      : I can only describe what I saw, my sister. Ask Felix here about it.

Kraden    : Ah, yes. Psynergy...I have dedicated most of my life to its study...
            The power of Psynergy comes from the four basic forces of earth,
            fire, water, and wind. These energies, the foundations of Alchemy,
            are called "Elementals."

* - The others seem confused.

Kraden    : You don't know Alchemy? The four elements? Why, they're the building
            blocks of all matter on Weyard.

Susa      : All existing matter comes from Alchemy and this Psynergy?

Kraden    : Yes, that's right. Everything you see around you is some combination
            of these elements.

Kushinada : Does this mean that there are as many types of Psynergy as there are
            types of elements?

Kraden    : That's right, Kushinada. You're a smart lass. Mt. Mikage was a place
            of great earth powers. I'd imagine your powers are earth based.

Uzume     : That's right, but how did you know this?

Piers     : Kraden... Mt. Mikage is Gaia Rock, isn't it?

* - Kraden nods.

Uzume     : ...Gaia Rock? Mt. Mikage is the sacred mount of our people!

Sheba     : Yes, but there are many mountains like your Mt. Mikage all across
            the Eastern Sea. Mt. Mikage is a source of earth power, and there-
            fore, it must be Gaia Rock.

Susa      : You have seen other mountains like our Mt. Mikage?

Jenna     : Yes! In fact, it seems that each of these rocks contains a different
            elemental power.

Kushinada : And now, you are questing to gather the power of these elements,
            yes?

* - The group nods.

Uzume     : And you only defeated the Great Serpent of Mikage to accomplish
            this goal?

-----------------------------------------------------------
     -(Yes)
Uzume     : Regardless of your motives, you have saved us all.



     -(No)
Uzume     : You took pity on Kushinada? You are very kind to help Susa, Felix.
-----------------------------------------------------------

Kraden    : You're... not implying that we defeated the serpent, are you?
            It's true that we did fight the creature...But without Susa's power,
            the battle might not have ended so happily.

Susa      : What... What are you--

Piers     : Susa had given the beast a lot of Dragonsbane in order to weaken it.

Sheba     : We could never have beaten the beast if it had not been in a...
            weakened state.

Jenna     : We were victorious only because Susa risked everything to weaken
            the dragon.

Uzume     : Susa, perhaps, after all, you are...

Susa      : No, I didn't...

Sheba     : Don't forget, Susa dealt the finishing blow, didn't he?

-----------------------------------------------------------
     -(Yes)
Susa      : Finishing blow? All I did was stab it with the Cloud Brand.



     -(No)
Susa      : That's right. Piercing it with the Cloud Brand was hardly a
            finishing blow.
-----------------------------------------------------------

Kraden    : I disagree... You weakened the serpent. You dealt the final blow.
            I'd say you were essential. So, Lady Uzume, wouldn't you say that
            Susa deserves the reward for this feat? Even Felix agrees,
            don't you, Felix?

-----------------------------------------------------------
     -(Yes)
Jenna     : I do, too.

Sheba     : We weren't fighting in hopes of getting a reward, were we?

Piers     : We'll be satisfied just learning your Psynergy.



     -(No)
Jenna     : Are you asking for a reward? That's just plain greedy!

Sheba     : We couldn't possibly take any sort of reward.

Piers     : Learning new Psynergy will be reward enough.
-----------------------------------------------------------

Kraden    : As you can see. Now, it's about time for us to leave Izumo Village.
            Yes, indeed! We're on our way to Lemuria.

Kushinada : You're leaving so soon?

Kraden    : We are in a great hurry.

Uzume     : Then you must return to Izumo someday.

Jenna     : I'm sure we'll be back once our mission is completed.

Kushinada : Excellent! I shall accept that as your oath!

Sheba     : ...Oath? Oh, by promising to return, we'll be ensuring that our
            quest will end successfully...

Piers     : I understand... We must vow to return, everyone.

Uzume     : We'll be waiting.





* - Upon exiting the house, Susa runs out.

Susa      : Felix, wait! It troubled me to let you leave like this... I owe you
            much for your help, but I didn't have any way to thank you...
            And then I thought of something. You're a warrior, and warriors
            need weapons. Wouldn't you agree?

            -----------------------------------------------
                 -(Yes)
            This token isn't something I possess. It's a legend, one that might
            be of use to you. Long ago, the Great Serpent of Mikage would sleep
            with its body crossing the river... Where its tail fell, the Cloud
            Brand lay hidden. That's the legend, anyway. The serpent was once
            the sword's protector, but it lost the sword many ages past. Anyway,
            maybe you want to go check out the dragon again... I left something
            there for you... just as a way of saying thank you.

            Well, I've said what I came to say. I'm going back to Kushinada.
            I hope you are successful in your quest.



                 -(No)
            Are you sure about that? I was only hoping to show you my
            appreciation.


              * - Speaking to him again:

            Would you be willing to accept a token of my gratitude?

                --(Yes)
              * - See:  "This token isn't something I possess."

                --(No)
            Are you sure about that? I was only hoping to show you my
            appreciation.
            -----------------------------------------------


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Those screams from Mt. Mikage... They must have come from the
               serpent. That means Susa must have saved Kushinada!

           {M} I had always thought Susa was nothing but a troublemaker,
               but he's proven himself a hero now!

[002]     :{S} Susa has changed so much from the wild youth we once feared.
               He's saved our village.

           {M} It's odd to think that so many in the village once despised
               Susa...

[003]     :{S} Susa has grown so much to fight for his beloved Kushinada so
               gallantly.

           {M} All the girls must be so relieved now that that awful lottery
               has been ended forever.

[004]     :{S} Susa has put the serpent back to rest, but not everyone seems
               happy...

           {M} Everyone's been wondering why the serpent wanted a sacrifice...
               Was he lonely?

Okuni     :{S} We're planning a festival to celebrate the end of the serpent's
               reign of terror! Lady Uzume is paying for the whole thing, so
               bring your dancin' feet!

           {M} This celebration will rival the one that woke the serpent in the
               first place!

[005]     :{S} Kushinada has been spared? I'm thrilled beyond words! She did not
               deserve such a fate...

           {M} Kushinada is such a sweet girl. She should never have been chosen
               in the lottery.

[006]     :{S} Lady Uzume predicted that a great hero would appear to save
               Kushinada. Nobody thought that hero would be Susa!

           {M} So... Susa really was as much of a hero as Lady Uzume claimed...
               How disappointing.

[007]     :{S} I've heard people saying that Susa had the help of other
               heroes... Are you they? [sic]

           {M} What would make anyone want to race up Mt. Mikage and into the
               serpent's lair?

* - [008]'s script is the same as before, until the misaligned stone is moved.

[008]     :{S} But it's a festival! Why do I have to keep guarding the
               stone circle?

           {M} Susa did a momentous thing, battling the serpent. So why do I
               not want to congratulate him?

* - In front of the building where Kushinada had been:

Guard 1   :{S} Did you hear how Susa defeated the serpent and rescued Kushinada?
               How come she doesn't seem any happier now that she's free?

           {M} Kushinada must be upset that Susa defied his sister and risked
               his life for her. She worries about him so much.

Guard 2   :{S} If you're looking for Kushinada, Lady Uzume escorted her to
               the mansion. Now that Susa has defeated the serpent, Kushinada
               is no longer being held as a sacrifice.

           {M} Lady Uzume and Kushinada are as close as sisters. It must be
               nice...

[010]     :{S} We may never know what was responsible for waking the serpent
               from its slumber...

           {M} We need to figure out what woke the serpent...After the festival,
               maybe...

[011]     :{S} The serpent taught us one thing: Celebrate while you can, but
               keep your eyes open!

           {M} That Susa used my dagger to defeat the serpent. He would never
               have won if not for that dagger! And he gets all the credit!

[012]     :{S} Our island is safe at last! It's time for us to celebrate and
               enjoy ourselves again!

           {M} Dancing is good for the soul! Oooog... But too much dancing...
               makes... me... dizzy.

[014]     :{S} Lady Uzume and the others aren't really blood relatives.
               Does that surprise you?

               --------------------------------------------
                    -(Yes)
               Well, they do possess a power no one else has... Maybe that means
               they are siblings after all.



                    -(No)
               I'm just glad that Lady Uzume used her powers for the good of
               us all.
               --------------------------------------------

           {M} As long as we have Lady Uzume, Kushinada, and Susa here,
               Izumo will be safe.

[016]     :{S} Dancing like this is pure bliss.

           {M} A dragon, a hero, a damsel in distress... That's got all the
               makings for a fairy tale...

[017]     :{S} I wonder if there's someone out there who would sacrifice his
               life for me. Will I ever find him?

           {M} All anyone talks about is how Susa risked his life to save
               Kushinada. I'm so jealous...

[018]     :{S} Everyone says that Susa is the one to thank for returning peace
               to our small village.

           {M} Susa said the serpent wasn't all that tough... He makes quite a
               dashing hero!





   [ Buildings ]
Innkeeper1:{S} Briggs, from Champa, hasn't been by selling much fish lately,
               so our menu's suffered.

           {M} If Briggs's ship doesn't come soon, we won't be able to get any
               seafood. Until them, all we'll have to eat is freshwater fish.

Innkeeper2:{S} As Lady Uzume foretold, the serpent was defeated without
               returning to our village.

           {M} I understand now! I had no idea why we were preparing all those
               barrels. If not for those barrels, the serpent just might have
               destroyed all of Izumo Village.

-----

[General] :{S} You must see many wonderful things traveling across the Eastern
               Sea. How I'd love to travel like you and see such wonders.

           {M} I'd love to travel the Great Eastern Sea and get things I can't
               find here on the island.

[009]     :{S} My goods are among the best on the island. I'm sure there are
               things the people on the mainland would love to have.

           {M} This may be a small island, but our craftsmanship is as good as
               anything on the mainland. It may seem impossible now, but one
               day I'll be trading with the shops in all the big cities.

-----

* - [010] to [015] have left, though only four of them appear outside.

-----

* - [016] to [018] have gone outside.

-----

G. Healer :{S} Now that peace has been restored, our island is flourishing once
               more. And I am most pleased that we had no need of any
               sacrifices!

           {M} I thank the powers that be that I was not chosen as a sacrifice.

[019]     :{S} If you're a sacrifice, that means you have to marry the dragon,
               right? I'd hate to think what it must be like, cooking for a
               creature that big.

           {M} That dragon wanted a new wife each and every year! He must really
               like girls.

[020]     :{S} Now that the serpent's been defeated, we don't have to sacrifice
               anyone!

           {M} Maybe now, Kushinada can come out and play. What should we do,
               though?

-----
* - Uzume's residence.

Uzume     :{S} If you have time, won't you enjoy a little of our celebratory
               festival?



                 * - Upon offering the Dancing Idol:

               Ah... Could it be? Is this the dancing doll of Mt. Mikage?

               --------------------------------------------
                    -(Yes)
               You found this at the peak of Mt. Mikage?



                    -(No)
               Don't lie to me. The style, the craftsmanship... You must have
               found this on Mt. Mikage.
               --------------------------------------------

               Again, you have done more for me than I can properly reward you
               for doing...

               I think I may have something that might please you.

                 * - She summons a Mars Djinni.

               This is my pet. It's very dear to me. I am unsure how it works,
               but this fellow seems to magnify our power... Though it saddens
               me to part with it, I would have you take him, as he might help
               you... Felix and his friends have agreed to care for you from
               now on. Please, accept this gift.

                 * - <game>:  Felix found the Mars Djinni Coal!



                 * - After having received Coal:

               With this dancing doll, I can explore Mt. Mikage on my own.
               Take care, Felix.

           {M} And what were you planning to do, once you'd read my mind, hm?

                 * - 2nd+ time:

               Trying again, Felix? What a pest. You can see my mind, but
               you are incapable of peering into my heart.

Kushinada :{S} Someday, Susa and I will have a son, and we will name him Takeru.
               When he goes to sleep at night, I will tell him the story of your
               great deeds and your quest.

           {M} If Felix's descendants are ever in trouble, our Takeru will
               rush to their aid.

Susa      :{S} I'm sure you know the villagers believe I beat the serpent.
               Don't let me take all the glory!

           {M} I'm no hero, but that shouldn't stop anyone from treating me
               like one.

Drummer 1 :{S} Lady Uzume has grown quite fond of this odd creature she found...
               She's taken it as a pet.

           {M} I heard that Lady Uzume's pet sometimesi [sic] disappears into
               thin air... Sound [sic] a little bit like that cat I had when I
               was little.

Drummer 2 :{S} Lady Uzume's new pet affects her powers in weird ways.
               It doesn't do anything to us...

           {M} I don't know what it means that Lady Uzume's pet increases her
               power...But these kids have seen a lot of things I've never seen.
               Maybe they understand...

Dancer 1  :{S} They've been saying that you went into Mt. Mikage, too...
               Is that true?

               --------------------------------------------
                    -(Yes)
               There's a legend about a doll of mysterious power hidden
               somewhere in the mountain. I'm sure Lady Uzume would be very
               pleased if you were to find it for her...



                    -(No)
               Oh... There's an old legend about a dancing doll that has strange
               powers hidden up there. Lady Uzume really wants that doll. Maybe
               Susa will find it and bring it back for her...
               --------------------------------------------

           {M} Why does Lady Uzume want that dancing doll so badly?

Dancer 2  :{S} Supposedly, the doll has the power to move the statues that
               block light inside the mountain.

           {M} I wonder what sort of dance the doll does. I've love to see what
               it looked like someday.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'28] ---           [Angara]          --- [02'28] #$#
#$#$#                      Champa                     #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Oh, I'm so hungry... And there won't be anything to eat until
               Briggs returns.

           {M} Where could Briggs be wasting his time now?

[002]     :{S} How did you find your way here, to the edge of Angara? Champa is
               hidden by mountains. No one ever climbs over to see us, except
               for the monks of the Fuchin Temple.

           {M} Champa is all alone on the eastern edge of Angara. That's why we
               took to the sea. We had to learn to fend for ourselves... That's
               why we are seafaring people today.

[003]     :{S} Eoleo, Briggs's son, has a really strange ability... I'll bet
               if I keep practicing, I'll be able to do it, too, so I'm giving
               it my all.

           {M} If I could pick up things without using my hands, life would be
               so much easier.

[004]     :{S} Once Briggs comes back, I can play with Eoleo again...
               I hope they come back soon.

           {M} Eoleo's so much younger than I am, but I can't stop thinking
               about him... Is that... love?

[005]     :{S} When is Briggs going to return with food for the village?
               We can't wait much longer.

           {M} Briggs promised to bring enough food for the whole village.

[006]     :{S} Champa is impoverished, but soon, we will prosper again.
               All our hopes rest on Briggs returning with a ship filled
               with treasures!

           {M} I bet Briggs has already dug up his treasure and is on his way
               back home.

[007]     :{S} You've the look of a traveler about you... Have you been to
               Ankohl Ruins?

               --------------------------------------------
                    -(Yes)
               Only those who have mastered the powers of the earth can enter
               the ruins.



                    -(No)
               My mistake... These old eyes aren't what they used to be. Anyway,
               the ruins are just a little ways northeast of here. You should go
               see them.
               --------------------------------------------

           {M} I want someone to solve the riddle of Ankohl Ruins before
               I die... It's my one wish!

[008]     :{S} The ruins at Ankohl are all that remains of a great sanctum
               our ancestors built. They must have been quite wealthy to build
               such a massive building.

           {M} They say the chamber at the top of the ruins is decorated in
               the purest gold. Our ancestors must have been wealthy to afford
               such extravagant decor.

[009]     :{S} The cliff caves are a lot quieter with Briggs gone...
               It's a little lonely without him here.

           {M} Why haven't Briggs and his men returned yet? Obaba said not to go
               looking for them, but what if they're in trouble?

[010]     :{S} Our matriarch is the last successor of the Ankohl. She's a master
               of the forge. It was the ancient gift of the Ankohl...
               There's nothing broken that they couldn't fix.

           {M} Obaba's locked herself in her room until her grandson, Briggs,
               returns from sea. She's so worried...She hasn't even been eating.
               I hope she's all right.

[011]     :{S} The Champa sailors aren't... well liked outside of here, are we?

               --------------------------------------------
                    -(Yes)
               Hey, that hurts... You could at least lie to me, just to be
               polite... If you keep spreading rumors like that, you'll have
               a rough time around here.



                    -(No)
               Really? That's nice to hear. But if you do hear anything,
               don't believe a word of it.
               --------------------------------------------

           {M} If Briggs would just bring the treasure he found back to Champa,
               we could all prosper. Then we could put this pirate business
               behind us for good.





   [ Buildings ]
* - First tent on raft:

[012]     :{S} It looked to me like the wave came from the Sea of Time.
               What's in there? What caused it?

           {M} Something must have blown up in the Sea of Time.
               That would explain the tidal wave.

[013]     :{S} The tidal wave was terrible... It...It nearly swallowed me whole!

           {M} The fish are vanishing. I'm sailing farther and farther for
               fewer and fewer fish.

[014]     :{S} Most of the sailors here live in the cliff dwellings, but I
               don't like those caves. They're dank! And what's worse, the
               people living in the harbor really resent the cliff-dwellers.

           {M} You have to be one of the pirates to live in the cliffs...
               I just can't do it...

-----
* - 2nd tent on raft:

[015]     :{S} There's not much space in the cliff caves. That's why we have to
               live out here on the boats.

           {M} These rafts are all we have! There's no place left for us on
               dry land!

[016]     :{S} Everyone in Champa is poor, but the poorest of us all live
               on rafts... I want to live on land.

           {M} If Dad hasn't been opposed to Briggs becoming a pirate, we'd
               still be living on land.

[017]     :{S} My dad went out to fish, but there were no fish to be caught,
               so he had to come back empty-handed.

           {M} Father worries so much about the lack of fish... He used to
               come back with fish jumping out of his nets. Why can't he catch
               fish anymore?

[018]     :{S} When my father heads out to sea, he takes our home with him
               and leaves us cold. But when he comes home with an empty net,
               that leaves us cold AND hungry.

           {M} I hope Dad makes it back before dark... I don't want to have to
               sleep on shore with no shelter.

-----

[General] :{S} I have some lovely artifacts, but it's only because I've been to
               the Ankohl Ruins.

           {M} Our products cost what they cost for a reason: they're all rare
               and valuable treasures from Ankohl. If I risk my life to get
               something nice, of course I'm going to ask a higher price for it!

[019]     :{S} If you go to Ankohl Ruins, you might find some nice artifacts
               for yourself.

           {M} The stuff in the ruins just sits there waiting for someone to
               come along and take it. But if it's broken, I'm the only guy
               in town who can fix it.

-----

[020]     :{S} We've seen a lot of traveling warriors in Champa of late.
               We never used to... I wonder if it's just a coincidence that
               we've seen so many lately...

           {M} More visitors means more money for our village... Maybe we'll
               even get tourists soon!

[021]     :{S} A group of travelers came here looking for a Felix. He seems
               to be a fairly popular guy.

           {M} Now that I think about it, someone else was looking for a Felix,
               too. I'll bet that guy is probably still somewhere in town...

-----

Healer    :{S} Briggs bears the weight of hope for our struggling, impoverished
               village. He must return home soon, before all the villagers
               lose hope and fall into despair.

           {M} I hope Briggs brings something home for us... If not, it might be
               the end of Champa...

-----

[022]     :{S} The ocean has been a lot warmer lately, and the fish population
               is decreasing. It's not natural for the ocean to be so warm.
               What's causing it?

           {M} We Champa rely entirely on the ocean for our survival. It's all
               we've ever known... I wish the Eastern Sea would return to its
               bountiful days of overflowing nets and smooth seas.

[023]     :{S} I've heard rumors of a terrible tidal wave striking the lands
               south of us. I sure hope Briggs and his men weren't engulfed
               by it...

           {M} All the sailors are saying the tidal wave down south was
               unbelievably huge. If Briggs were caught up in it, I don't think
               he could have survived.

-----

Innkeeper1:{S} Listen, if you came to Champa looking for good seafood, you came
               to the wrong place. We haven't had a decent catch in months.
               It's like all the fish are just... gone.

           {M} It's a shame that we can't offer any fish to our customers.
               Ah, how I long for the days when we had fish enough for everyone.

Innkeeper2:{S} We used to do good trade with an island east of us. They bought
               all our surplus fish. We don't have any surplus anymore.
               We don't even have enough for ourselves.

           {M} Watching our catches dwindle with every day... It's a nightmare!
               Where have all the fish gone?





   [ Cave system within cliffs ]
[024]     :{S} The Champa sailors who don't live in the cliffs are no better
               than cowards. The ones living in the caves will protect Briggs
               and Obaba without a second thought.

           {M} If you live up in the cliffs, that means you've proven that
               you can travel far across the seas. If you call yourself a sailor
               without ever going anywhere, you're not worthy of the title.

-----

[025]     :{S} All of our men went to sea with Briggs--even my sweetheart!
               I hope they return soon.

           {M} Briggs is the greatest among all our sailors. As long as he
               is leading our men, they'll make it back to Champa just fine.

-----

[026]     :{S} I bet you're wondering why only sailors and their families get to
               live in the cliff dwellings. Well, from up here on the cliffs,
               families can look out to sea and await the return of their
               sailors.

           {M} Standing here, staring across the sea from these cliffs, makes me
               feel like I'm helping our sailors.

-----

[027]     :{S} Before he left, Briggs ordered me to keep watch in his absence.
               If Obaba is so worried about Briggs, she ought to send someone
               out to look for him.

           {M} Briggs may be our captain, but at least he's not all full of
               himself. I hate people like that.

-----

[028]     :{S} My husband wants our children to be sailors like him, but I
               simply won't have it.

           {M} When I married a sailor, I knew how cruel the sea could be.
               I can't stop my husband from sailing, but I don't want our
               children to follow that path.

[029]     :{S} Mom's had it pretty rough. I hope I meet a sailor with a future,
               so I don't have to work so hard.

           {M} Eoleo is the only boy in town who will amount to anything...
               He will be mine!

[030]     :{S} Someday, I want to be a sailor, like my father before me.
               My mother hates the idea, though. She'd rather have my study
               and become a scholar or something.

           {M} Has Mom forgotten that I am my father's son? If she knew anything
               about me, she'd never ask me to give up the sailor's life.

-----

[031]     :{S} Obaba's not seeing anyone right now. She's concerned about her
               grandson, and she doesn't want to be bothered.

           {M} I've never seen Obaba like this before. She must be really
               worried about Briggs...

-----

[032]     :{S} That pit is Obaba's forge. She uses it when she's working metal
               into weapons and equipment.

           {M} I wonder how deep this forge goes. It's supposed to reach right
               into the mountain's heart. Obaba must be a master of the forge
               if she's the only one who can call up its flames.

-----
* - Upon approaching the door to Obaba's room, she comes out.

Obaba     : Has my grandson returned? Has my Briggs come home?

            -----------------------------------------------
                 -(Yes)
            You lie! If Briggs had truly returned, he would have come to see
            me first!



                 -(No)
            I asked not to be disturbed until my grandson has returned home!
            Now, let me be!
            -----------------------------------------------

* - She returns to her room.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'29] ---           [Osenia]          --- [02'29] #$#
#$#$#                     Alhafra                     #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - The Burst Brooch, which bestows Burst, is found in Tundaria Tower in the
    far south. It can be used to break cracked objects, such as the stone
    atop the ship's mast.


#$#$#$#$#$#$#$#$#$#$#$#
$#  Eastern Alhafra  #$
#$#$#$#$#$#$#$#$#$#$#$#

* - After disposing of the stone, and having begun to disembark:

Man 1     : Hey! That block on the mast has disappeared!

* - Two men are present to the south.

Man 2     : Hey! Now, we can raise the mast and use the sail again!

Man 1     : Hey, mate, let's go tell the mayor the good news!

Man 2     : Yeah, let's do that!

* - They depart.

Eoleo     : Baba babubu!!

Chaucha   : What is it, Eoleo? What are you so excited about?

Eoleo     : Baba babubu!

Chaucha   : It's true! The block that was pinning the mast down is gone!

* - She turns to Felix's group.

Chaucha   : You were the ones who did it, weren't you?

-----------------------------------------------------------
     -(Yes)
Chaucha   : I knew you would do it someday.



     -(No)
Chaucha   : But, of course, I also know that you didn't do it for our benefit.
-----------------------------------------------------------

Chaucha   : Still, Briggs will be pleased when he hears about this.

* - Eoleo looks happy.

Chaucha   : Well then, let's go tell him!

* - They depart. The two men, the Alhafran mayor and Jiya soon arrive.

Mayor     : I still just can't quite believe that the stone block on top of
            the mast has totally vanished.

Man 1     : I'm telling you, Mayor, I saw it with my own eyes!

            ...I mean, I didn't see it! It's gone!

Man 2     : If you don't believe us, you can go see for yourself!

* - They move closer to the mast and observe the absence of all the debris.

Mayor     : Huh? What? Whoa, hey!!! It's gone! That huge block is really gone!

Jiya      : Excellent news, Mayor!

Mayor     : Unfortunately, the mayor of Madra will probably try to take it
            from us now. But that can wait. Who was able to move the block?

* - Neither of the two men are aware. The mayor notices Felix's group.

Mayor     : Felix! Felix, did you do this?

Kraden    : Surprised to see us, Mayor?

Mayor     : Did you do this?

Kraden    : We left Alhafra some time ago, but we just returned and destroyed
            the stone block.

Mayor     : Exploring? What brought you back to Alhafra right now?

Kraden    : Felix had a hunch that we might be needed here.

Jiya      : Mayor, not to interrupt, but shouldn't we begin repairs on your ship
            now?

Mayor     : Yes, yes... You're right, of course.

* - He turns to the other two men.

Mayor     : Gather the townspeople and get them to work on the mast.

Man 1     : Yes, sir! We're on our way!

Man 2     : We shouldn't need too many people to raise the mast!

Mayor     : All right. I'm counting on you.

* - They depart. The mayor turns back to Felix's group.

Mayor     : Destroying that stone must have been quite a challenge.
            Why don't you come back to my manor to get some rest?

-----------------------------------------------------------
     -(Yes)
Kraden    : You're too kind, Mayor. We'd be happy to...



     -(No)
Kraden    : We could use the rest, Felix. We should accept the mayor's offer.
-----------------------------------------------------------


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Mayor's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - The next morning:

Kraden    : Thank you again, Mayor. You keep a fine house.

Mayor     : Don't be silly. You've done us a great deed. It was the least I
            could do.

* - Sheba whispers to Jenna.

Sheba     : Even if he gets the boat fixed, I don't think he's going to hand it
            over to Madra...

Jenna     : I agree... He's being way too nice for me to not be a little
            suspicious of him...

Mayor     : I'm sorry, did you girls have something you'd like to share with us?

* - They shake their heads.

Mayor     : I see!

* - The screen turns gray as everyone continues speaking, yet the player is
    not made aware of their words.

    The mayor says something to Kraden, which seems to puzzle him. Kraden turns
    to the others, perhaps looking for a comment on the mayor's remark.

    Cue awkward silence.

    The mayor appears concerned, but then he smiles, saying something to
    Sheba and Jenna. They appear a tad surprised.

    The mayor nods, and a heart emoticon appears above him. Jenna shakes her
    head, while Sheba appears upset, as does Felix. The mayor seems distressed.

    The screen blanks out, coming back to the scene after some time has passed.

Mayor     : Jiya, how are the repairs coming along? Things seem to be moving
            slowly down there.

Jiya      : Milord, these things take time...

* - A guard runs into the room.

Guard     : Sir, there's a problem!

Mayor     : Calm down, man! You're a soldier! What are you so flustered about!?

Guard     : Briggs destroyed the prison and escaped with his pirates!

Mayor     : What, were you asleep while this was going on?

Guard     : Don't... Don't be silly!

Jiya      : How could Briggs possibly break out of our prison? It's one of
            the strongest in Osenia!

Guard     : I don't know what happened, but before I knew it, they'd smashed a
            hole in the wall!

* - One of the two men who spotted the stone's absence appears.

Man 1     : Mayor! The mast has been raised!

* - No one seems particularly enthused.

Man 1     : Hey, what's up?

* - He notices the guard.

Man 1     : Wait, you're supposed to be guarding the prisoners... What happened?

Mayor     : It appears that Briggs has escaped.

Man 1     : That's no good...

Jiya      : What are you standing around for!? Search the area! Find Briggs
            at once!

Guard     : It... might not be quite that easy...

Man 1     : He is a pirate, after all... A famous one!

Jiya      : Enough of that! Move it!

* - The guard and the man quickly depart.

Mayor     : Regardless, I'm going to go inspect my boat... Oh, and Felix and
            his crew were there, too, weren't they? I treated you like an
            honored guest in my home... Usually, one feels a certain obligation
            to those who do them such a kind service, am I right?

            So, don't just stand there! Return the favor and find my Briggs!

Jiya      : Come on! Hurry up! Let's go! Move it!

Mayor     : Let's go see the boat.

* - The mayor and Jiya take their leave.

Piers     : The mayor of Alhafran certainly does know how to look out for
            his own interest, doesn't he?

Sheba     : That's one way of putting it!

Jenna     : Well, so what do we do? Do we go after Briggs?

-----------------------------------------------------------
     -(Yes)
Sheba     : Don't feel like you have to do them any favors!



     -(No)
Sheba     : That's right! Why should we help the mayor, after the way he
            treated you!
-----------------------------------------------------------

Kraden    : Felix can decide for himself what to do... At the very least,
            I want to go see the sailing ship now that it's fixed.
            Let's just go outside and take a quick look.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

* - These identifications have no relation to those prior.


   [ Outside ]
[001]     :{S} I'm just standing guard, in case Briggs decided to attack the
               mayor's manor.

           {M} I'm supposed to be guarding in case Briggs shows up. But if he
               does, I'll probably just cry.

[002]     :{S} I wonder where Briggs and his crew went... There's no sign of
               them around here...

           {M} Why do I have to look for Briggs? It's not my fault he escaped...

[003]     :{S} The mayor was actually singing and skipping when he went to
               the dock. He seemed so pleased.

           {M} The mayor only had one thing on his mind on his way to the
               dock... Money, and lots of it.

[004]     :{S} I'm sure it's just a coincidence, but whenever you show up,
               trouble happens.

           {M} It's been so busy around here... Pirates, warrior, sailing ships,
               natural disasters. What a week!

[005]     :{S} I heard you made it so we could fix our sailboat! Is there
               anything you CAN'T DO?

           {M} I hate to tell Felix, but even though our mayor seems nice,
               he's really a selfish jerk.

[006]     :{S} Ever since we heard Briggs broke out of jail, we've all been
               a little nervous...

           {M} I'd bet that Briggs fled the city at the first chance.
               I really wonder if he'd still be here.

[007]     :{S} If Briggs is smart, he's probably long gone from Alhafra,
               if you ask me.

           {M} The mayor said I had to look for pirates... Where am I supposed
               to be looking?

[008]     :{S} Our sailboat looks fabulous with its mast repaired! You really
               must go check it out!

           {M} Who cares if the boat is fixed? It's not like we'll be allowed
               on board. The mayor's too selfish.

[009]     :{S} I've been waiting for this day for years! I can't wait to
               set sail across the Eastern Sea.

           {M} I'm probably too old for the mayor to let me on the ship, but
               I can still have my dreams.

[010]     :{S} I don't know why everyone's so excited about fixing the ship.
               We promised it to Madra, didn't we?

           {M} Briggs paid a lot for a broken boat, but now that it's fixed,
               it's practically priceless!

[011]     :{S} With that ship, Alhafra's going to become a big, important
               trading town... We'll all be rich!

           {M} I'm certain the only person to prosper from the boat will be
               that oaf of a mayor.

[012]     :{S} Weird... have you ever had the feeling that someone just
               passed by? Maybe it's just me.

           {M} What if the pirates were nearby... Maybe that was them behind
               the building...

[013]     :{S} The whole town is grateful to you... Without your help,
               we couldn't have fixed the mast!

           {M} Now that the boat is fixed, who gets to keep it? Us? Or the
               Madrans?

[014]     :{S} Huge boats carry more, but we need smaller ships to catch the
               wind. The mayor just doesn't understand this...

           {M} Without smaller ships, how can we catch the fish we need to eat?

[015]     :{S} The secret to harnessing the wind's power is building a small
               ship. Large ones can't do it.

           {M} Smaller ships use their sails to steer a lot, but it must be
               harder when your ship's so big.

[016]     :{S} Once that stone was taken care of, it was really quite easy to
               raise the mast again. 

           {M} Now that all the debris has been cleared away, our harbor looks
               so nice.

[017]     :{S} Oh! It's you! Where have you been? We haven't seen you around
               Alhafra lately...

           {M} Felix must have found himself a boat... Isn't that what brought
               him to Alhafra in the first place?





   [ Mayor's residence ]
[018]     :{S} Everyone in town is talking about how the boat's finally been
               fixed! You should see it!

           {M} I don't know what the big rush is. We can see the boat whenever
               we want. It's ours!


#$#$#$#$#$#$#$#$#$#$#$#
$#  Eastern Alhafra  #$
#$#$#$#$#$#$#$#$#$#$#$#

* - Three men lie on the ground.

Man 1     :{S} Stupid Briggs...

           {M} Briggs said the boat was his... And, to be honest, they had paid
               us for it, but...

Man 2     :{S} Why do these things always happen to me?

           {M} I just came down to see the repaired mast, and they jumped on me
               from out of nowhere.

Man 3     :{S} Oooog... Ow...

           {M} Briggs's pirates... They attacked us and... The ship...
               The ship...

* - At the dock's end, the mayor, Jiya and a fourth man also lie on the ground.

    The ship has begun to move.

Mayor     : Briggs!!! Briggs where are you taking my boat?

Jiya      : He's attempting to steal it! Thief! Thief!

* - Briggs speaks from the ship.

Briggs    : Did you call me a thief? I paid for this boat, fair and square.
            I'm no thief.

Chaucha   : You're the thieves! You tried to take our boat away, after we
            paid you so much for it!

Mayor     : ... ...

Briggs    : You're the one who stole OUR boat!

Kraden    : Ahoy, Briggs!

Briggs    : Uh-oh... It's Felix!

Chaucha   : You're not afraid of them, are you? Look how far away they are...
            There's no way they can catch us now!

Briggs    : You're right... They're stuck on the land, and we've got this boat!

Chaucha   : They can't catch us... What would they do, swim?

Briggs    : Hah! You're right! They can't board us from way over there!

Chaucha   : Wasn't there something you wanted to do the next time you saw Felix?
            Don't tell me you forgot... It's all you ever talked about when you
            were in jail!

Briggs    : Oh yeah... I almost forgot.

Chaucha   : So now's your chance! Do what you swore to do!

* - He faces Felix's direction, sticks out his tongue and holds down the
    bottom half of his right eyelid.

Briggs    : Bleah!

Chaucha   : Is that the best you could come up with?

Briggs    : But, Chaucha, they're an awfully tough bunch...

Chaucha   : See? It's that attitude right there! That's why you'll never amount
            to anything!

Briggs    : You know what? You're right!

            Hey! Felix! You guys take care! And keep Alhafra safe from thieves
            and pirates!

            And politicians, too!

Kraden    : What!?!

Briggs    : I doubt we'll ever meet again, but if we do, remember this!
            Neener neener neener! Neener neener neener!

* - He spins around...

Briggs    : Neener neener bleah!

* - ...and repeats his original taunt.

Chaucha   : That may have been a bit much. If you make him mad, he might
            chase us right back to Champa.

* - They sail out of sight. Back at the docks, the mayor shouts at Jiya and
    the other man by him.

Mayor     : What!!! You let Briggs get away! You and your friends talk a
            good game, but when trouble happens, where are you!?

            Well, isn't this a fine mess! My prize ship, stolen by a bunch of
            filthy pirate scum!

* - He kicks the man.

Mayor     : Get up!

* - He kicks Jiya.
Mayor     : They're gone, and you let them escape! You guys have royally botched
            this one. This ruins everything! You all ought to be ashamed!
            All of you were cowering, while I was the only one to stand up
            to them! All of you!

            I'm going back to my manor!

            And you, Felix. I am extremely disappointed in you. There will be
            no reward for you, Felix! You let that Briggs steal MY ship!
            You're lucky I don't lock you up in his stead!

            Bah! I've had enough of this! Don't just stand there with your
            mouths gaping! Get out of here!

* - The first three men stand up.

Mayor     : We don't have a boat, so there's no reason for anyone to be here at
            the port. Return to town.

* - The mayor, Jiya, and the four men take their leave.

Kraden    : What an awful person. Do you suppose he's always this self-centered?

-----------------------------------------------------------
     -(Yes)
Kraden    : Yes, he's terribly irritating. You're quite right, Felix.



     -(No)
Kraden    : You can stay calm after listening to that windbag? That's quite
            mature of you.
-----------------------------------------------------------

Kraden    : I'll wager Briggs is returning to Champa, personally.
            Well, it doesn't matter. I think I've had enough of this town.
            Shall we be leaving?

-----------------------------------------------------------
     -(Yes)
Kraden    : Great! Let's leave as soon as possible, shall we?



     -(No)
Kraden    : Ah, yes, well... If you still have business to attend to here.
            All right. But the sooner we leave, the better. Lead on, Felix!
-----------------------------------------------------------


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Alhafra lost its ship. Now, we're nothing but a big, boring town
               in the middle of Osenia.

           {M} If only we had that ship, Alhafra could have been a powerful
               trading town... and wealthy, too...

[002]     :{S} Even though we lost the big boat, I'm not particularly upset.
               We'll be just fine if everyone can work together and build a
               fleet of smaller boats.

           {M} I hope trade doesn't make Alhafra get all big. I like how quiet
               things are around here... We should stay a small town, with our
               small little boats.

[003]     :{S} It was great to see everyone in town working to raise the mast.
               Too bad the boat got stolen.

           {M} The mayor seemed so happy to see us working on the boat...
               That's kind of strange. After all, we were only fixing it so we
               could give it to Madra, weren't we?

[004]     :{S} After we did all that work to fix the mast, someone goes and
               steals our boat. We never should have fixed it in the first
               place.

           {M} It was Madra's boat. It should have been Madra's problem...

[005]     :{S} When they find that their boat was stolen, I'm sure Madra's
               not going to be too happy.

           {M} The mayor of Madra seems like a reasonable person. It's too bad
               this had to happen.

[006]     :{S} It's not like the boat could even more when the mast was still
               broken... When you think of it that way, it doesn't feel ike we
               really lost anything at all.

           {M} There's no point in worrying about losing something we never had
               to begin with.

[007]     :{S} Briggs came through here and disappeared into the forest.
               Scared the pants clean off me!

           {M} The poor guard was blindfolded when Briggs escaped, so he didn't
               see a thing. He's smart, that Briggs, covering his escape route
               like that.

[Armor]   :{S} So, Briggs stole Madra's ship right out from under our own
               greedy mayor? Ah, 'tis an ill wind that... that... um...
               Oh, I forget how it goes. But it's bad, trust me.

           {M} I don't know... I never really thought the mayor would give
               that boat to Madra anyway. Our mayor's far too greedy to pass up
               an opportunity like this.

[Weapon]  :{S} Everyone's saying that Briggs probably escaped by tunneling
               through the mayor's manor.

           {M} Supposedly, the cave under the mayor's manor is treacherous.
               You'd have to be pretty tough to make it out of there alive.

[008]     :{S} When is this house going to be finished once and for al!?
               The repairs are taking forever!

           {M} If Mom would stop making all these trifling little requests,
               we'd be done a lot faster...

[009]     :{S} The repairs are coming along pretty slowly, aren't they? Well,
               you wouldn't feel much like working either if your last major
               project was stolen!

           {M} We're all pulling together to fix this house. At least everyone
               is helping with the work.

[010]     :{S} Back before Briggs destroyed the bridge to the west, it was a
               lot easier to trade with Madra.

           {M} First, he steals a ship... then he ruins a very important
               bridge... Briggs is a real jerk.

[011]     :{S} We fixed the mast so we could use that boat. Now, Briggs has
               taken the boat and sailed off to Champa.

           {M} Why worry about Briggs? It's not as though we've got a boat
               to chase him with...

[012]     :{S} If they caught a good breeze, they're probably way off to the
               north of us by now.

           {M} If Briggs hadn't stolen that boat, I'd be out on the open sea
               right now, wind in my hair.

[013]     :{S} It felt so great when the whole town joined together to get
               those boat repairs done.

           {M} I know it's time to forget about that boat and get back to
               work... But I just can't let it go.

[015]     :{S} The mayor's been handing out free food to help us all through
               these difficult times. The way things have been going, though,
               I bet everyone just hoards it all.

           {M} I don't know what will happen if the repairs aren't done before
               winter hits...

[017]     :{S} We have to store what food we get from the mayor and only eat
               a little bit of it at a time.

           {M} I've seen Father trying to do some repairs, but it's too much
               work for him to do on his own.

[018]     :{S} That guy's house isn't fixed, and he won't help out on our house
               until his is done.

           {M} We could use some help with the house, but it looks like we're
               on our own for now.

[022]     :{S} Even if we fix it, the columns and the walls will collapse...
               They always do...

           {M} This is just too much work for one man to get done. I need to
               stop and get some rest, but I promised I'd finish...

[023]     :{S} With everyone's help, we were somehow able to avoid the wind and
               rain at least. You know, after all this, I now understand how
               difficult it is to be a carpenter.

           {M} He's never going to get finished with that terrible attitude
               of his. Until he feels like working, nothing much is going to
               get done around here.

[024]     :{S} There are quite a lot of houses in need of repair. Until the
               others are finished, I'll wait quietly.

           {M} Carrying these things all over has gotten my hands all torn up.
               I feel so... rugged!

[025]     :{S} Mom was happy to hear that the repairs wre coming along nicely.
               The thing is, they're not.

           {M} There's no way Dad can fix this house up all by himself.
               It's a mess!





   [ Buildings ]
Innkeeper1:{S} We're still recovering from the damage the tidal wave caused.
               Once the reconstruction is complete, Alhafra will be the
               perfect town... Indestructible!

           {M} After the tidal wave, it was one complaint after another, but
               things have quieted down. Everyone's been pulling together to
               get this work done, and we've set our differences aside.

Innkeeper2:{S} The mayor used the money he got from Madra to pay for all our
               food. Everything was looking good, until the boat got stolen...
               That sort of killed morale.

           {M} The mayor may have pulled through the tidal wave just fine, but
               his town didn't! How could he even CONSIDER punishing me for
               trying to feed all these unfortunate souls?

Chef      :{S} A bigger boat could haul in more fish, but right now, just about
               anything will do!

           {M} So what if trade brings people here? Things are so bad, we can't
               even offer a decent meal!

[014]     :{S} It seems that Briggs broke out of jail with the help of his wife,
               Chaucha.

           {M} Briggs and his wife were totally planning this jailbreak when she
               saw him there... What was the guard doing? Wasn't watching his
               prisoner? Was he napping?

[016]     :{S} I just want a house where we can all live together without
               fighting!

           {M} I'd really like to have a pet, but I know better. Things are
               too tough right now.

[019]     :{S} Briggs might have had a key, but I think he used a different
               escape route... I mean, walking out the front door of our jail
               would have been really stupid!

           {M} If I had a key, I would have used it. That's for sure. Briggs
               escaped through the caves, though... That pirate's a wily one.

[020]     :{S} Someone said my son and my grandchildren are fixing the house.
               They're so considerate...

           {M} Isn't anyone helping my family with the house? I'm an old man,
               and it'll take them years to finish!

[021]     :{S} So that Alex fellow left already, did he? He's such a rogue...
               Is he running from something?

           {M} He was just my type... Aloof, strong, blue haired... But he was
               a little too aloof. He... He never even said good-bye...

-----

[026]     :{S} Fixing that old guy's house is starting to drive us all crazy.
               I, for one, will be ready for a celebration once it's done.

           {M} Will they ever get out of my house? It's starting to worry me
               a bit...

[027]     :{S} The repairs on our neighbors' house are moving slowly.
               The longer it takes, the longer they live with us!

           {M} I don't have anything to say to them, and I'm tired of being
               the good hostess all the time!

[028]     :{S} My house is damaged more than I thought. Looks like I'm still
               stuck here with my neighbors.

           {M} I don't mind not being at home, but my wife wants her privacy
               back!

[029]     :{S} My husband and I don't get out much, and it's nice to meet the
               neighbors... But we've been here for so long, I don't think
               we'll be going out for quite a while.

           {M} I hated this place at first, but it's grown one me. I feel
               so much more sociable now...

-----

Healer    :{S} I heard you were there when Briggs escaped on the sailing ship.
               A villain like Briggs should never have been allowed to escape.
               It's a terrible thing.

           {M} They were so confident when they caught him before, but they
               were careless and let him escape!

-----

[Item]    :{S} The bridge to the west of us is all fixed now, just so you know.

           {M} People will start traveling again, and they'll need to buy
               equipment... My equipment!

-----

[030]     :{S} Briggs didn't commit any crimes in Alhafra, did he?

           {M} I don't believe for one second that Briggs was a pirate,
               raiding the towns of Indra.

[031]     :{S} I don't want to say this out loud or anything, but... Briggs paid
               for that boat fair and square. He didn't steal it at all.

           {M} Briggs paid for the boat and then left in it. Why is everyone
               treating him like a crook?





   [ Buildings  -  Mayor's residence ]
Guard 1   :{S} You really made a mess of things. Letting Briggs get away?
               What's wrong with you!? The mayor trusted you! You were his
               favorites--but not anymore!

           {M} One thing's for sure... We're not going to be hearing about how
               great Felix is anymore! Now it's my turn to show the mayor what
               I can do!

Guard 2   :{S} The mayor of Alhafra does not wish to meet with you. Please
               step back.

           {M} The mayor was so mad at us for letting Briggs reach the boat.
               How were we to know he was going to steal it?





   [ Alhafran Cave (prison) ]
Guard     :{S} Before I knew it, Chaucha stole the keys to the jail, and Briggs
               and his crew had them. I never looked away! Not once! I never
               let my guard down! How did this happen?

           {M} No matter how many times I go over it, nothing seems right.
               I'm just not convinced... Wait a sec... Did Eoleo have a hand
               in this? He was standing behind me the entire time...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'30] ---           [Angara]          --- [02'30] #$#
#$#$#                      Champa                     #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Briggs and his men have brought several crates of food and gems.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Near entrance to cave system  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - A pirate sees Felix.

Pirate 1  : Whoa! You... You're Felix!

Pirate 2  : What? Really? It's Felix?

Pirate 1  : You're awfully persistent, aren't you?

Pirate 2  : Briggs, get outta here! Felix is here to finish you off!

Briggs    : What was that!? Felix? Here?

            Oh no! It's really him! I've got to get out of here!!!

* - He and the two pirates run into the caves.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
* - [003], [009, [010], and [011] have gathered by the new crates of food.

[001]     :{S} Briggs came back with a giant load of food! I've never been so
               full! It feels great!

           {M} Briggs is so generous! He told me to eat and eat and eat, so
               I did!

[002]     :{S} Let's see them call Champa poor now! Ever since Briggs came back
               with a cargo of gems, we've been filthy stinking rich!

           {M} Gosh... How much are all those jewels worth? More than I can
               figure, I know that.

[003]     :{S} Those bags are full of food for the people of Champa.
               Briggs gave them to us.

           {M} All of our stockhouses [sic] are so full of food that they've
               just left the extra out here...

[004]     :{S} I want to play with Eoleo, but he never comes down to the harbor
               anymore.

           {M} Eoleo said he couldn't play with us anymore, even though he's
               younger than we are...

[005]     :{S} Don't talk to me about food... I feel like I'm gonna be sick.

           {M} Errrrg... I was so full, and I just kept eating. I think I'm
               going to explode now.

[006]     :{S} Hey, you just came to Champa not too long ago, didn't you?

               --------------------------------------------
                    -(Yes)
               You'll be pleased to know that Briggs found ancient pirate
               treasure and bought us all food!



                    -(No)
               Well, you wouldn't know it to look at us now, but Champa was
               quite poor until recently. Now, thanks to Briggs, we're all
               so wealthy, it's disgusting!
               --------------------------------------------

           {M} Things are going to be different around here. Things are going
               to be better. I can't wait.

[007]     :{S} Briggs took a long time to return to us. You want to know why?

               --------------------------------------------
                    -(Yes)
               He was being held by an evil man who stole his money and made him
               a prisoner! They were probably trying to find Briggs's jewels...
               The sea is a rough place.



                    -(No)
               Briggs overcame great danger to return home to us. I admire him.
               I really do.
               --------------------------------------------

           {M} We're lucky Briggs hadn't found the jewels when he was caught.
               That would have been the end of Champa.

[008]     :{S} Briggs looks so reliable, so sure of himself. I've never seen him
               like this before.

           {M} Briggs was always such a brat, but now he's saved the village!
               What a turnaround!

[009]     :{S} Now, nobody has to do anything he or she doesn't want to do!
               We owe Briggs a lot of thanks.

           {M} Nobody really likes to play the role of a pirate. I'm sure
               everyone is glad they don't have to anymore.

[010]     :{S} Obaba is the last possessor of the ancient secrets of Ankohl,
               a long-lost civilization... There's nothing she can't fix,
               no matter how broken it is. She's quite the blacksmith!

                 * - 2nd+ time:

               You'd think Obaba would be glad that Briggs was back.
               She acts like nothing's changed.

           {M} Is Obaba in a good mood now, or what? I noticed the change as
               soon as Briggs returned. If you've got something to ask her,
               now's the time to ask.

[011]     :{S} Briggs fought the odds to bring us jewels and food! He's an
               amazing leader!

           {M} If Champa gets enough money, maybe we can stop with the looting
               and pillaging...





   [ Buildings ]
* - First tent on raft:

[012]     :{S} While I'm grateful for the food, it's somewhat annoying knowing
               that Briggs saved the day.

           {M} I should just sign up with Briggs's crew and stop all my
               complaining. Oh, but my shipmates would never forgive me if I
               bailed on them like that.

[013]     :{S} I hear that Briggs sold the jewels he found for cash and then
               acquired a boat.

           {M} The nerve of that Briggs! He's gone for a bit, and he comes back
               in a bigger boat! I'll bet he only did it to show us up, too!

[014]     :{S} Briggs really saved our hides this time, but I'm not about to
               join his crew! Yeah, maybe I do owe him for this, but I'll find
               a way to pay him back legitimately.

           {M} I refuse to live in the cliffs, and therefore I am against
               Briggs. I have accepted his food, but that is as far as I will
               let myself slip.

-----
* - 2nd tent on raft:

[015]     :{S} We don't need to live off fish anymore, so we don't need any
               fishermen, do we? That does it. I'm not working anymore.
               What would be the point?

           {M} I'd rather spend my time sleeping than passing it chasing fish
               that can't be caught. Why go after food, when Briggs can give it
               to you?

[016]     :{S} It's true! It's true! Briggs did return with the jewels!
               He's really going to have more friends than he did before!

           {M} Briggs is a hero for saving the village. But will Father lose
               his motivation to be productive?

[017]     :{S} When Briggs returned with the jewels, the adult quit working.
               I hope I don't become like them.

           {M} Quitting their jobs makes the adult just like us kids.
               It's getting really weird around here.

[018]     :{S} Father's acting like a child, and it seems he quit his job.
               He plans on lounging around at home...

           {M} If Father sits around the house, he will lose all respectability.
               It's better to fish than to do nothing.

-----

[General] :{S} The jewels Briggs found are truly remarkable. I wonder if there
               are any more like these in that cave.

           {M} Briggs's men said they found amazing weapons and things in the
               cave, too... I wish I'd been there. I would like to have seen
               them...

[019]     :{S} Thanks to Briggs, the Champa can eat again! Unfortunately,
               all that food is going to run out someday. Then, what do we do?

           {M} Now's the time we ought to be working hardest. While we can eat,
               Champa can flourish.

-----

[020]     :{S} I've been wondering about finding a chief for Champa, since we
               don't have one. If so, then Briggs would be the favorite, since
               he's given so much to the village.

           {M} A new image for Champa will reflect the time we live in...
               Any new visitors will like it...

[021]     :{S} We village elders have guided Champa for so many years... Yes,
               times are changing. Perhaps it's time Champa's leadership was
               given to the sailors.

           {M} Observing Briggs recently, the limits of Champa as a village are
               very apparent. From now on, the village will develop through
               trade. I guess that's the era we've come to.

-----

Healer    :{S} Briggs's jewels have turned this poor town into a wealthy place,
               but he brought too many. Now, the hardworking people of Champa
               have learned to be lazy louts.

           {M} All the people in town think they can live without ever having
               to work again. They've quit their jobs, and they rely too heavily
               on Briggs's find.

-----

[022]     :{S} It seems the elders are considering appointing Briggs the
               first-ever chief of Champa.

           {M} Sure, Briggs saved the village. But saving it from despair is not
               the same as governing it...

[023]     :{S} I, for one, think a person who can bring the people of Champa
               together will do us some good.

           {M} Supporting an entire village through fishing from the sea is
               next to impossible. We need new sources of income. Briggs is on
               the right path, finding us all those lovely jewels.

-----

Innkeeper1:{S} We still haven't been able to catch any fish for dinner.
               Not to worry, though. We'll serve up the meat that Briggs
               bought for us!

           {M} Most people here would love a nice fish meal, but having red meat
               is a nice change.

Innkeeper2:{S} It's nice not having to work, but it gets a little boring after
               a while.

           {M} The only way to find your special purpose in life is to work
               hard.





   [ Cave system within cliffs ]
[024]     :{S} What, you want to come in?

               --------------------------------------------
                    -(Yes)
               As if! I'm a nice girl, and I'm not about to let some masher
               come storming into my room!



                    -(No)
               Yeah? So what do you want? You're wasting my time.
               --------------------------------------------

           {M} Tough or not, he's not getting past me without a beating.

-----

* - [025] has left.

Pirate 1  :{S} Why do you have to be so stubborn? Quit following us, you
               big bully!

           {M} Maybe if I pretend he's not there, he'll go away. I don't want to
               fight him... He's got creepy powers!

Pirate 2  :{S} All right, I surrender! I'll go back to Alhafra... but only if
               Briggs is going.

           {M} He's after our ship, isn't he? That no-good thief mayor must have
               sent him.

-----

* - Pirates 3 and 4 are blocking the routes to [026] and [027].

Pirate 3  :{S} I'd rather fight than go back to jail. Bring it on, sissyboy!

           {M} It would be so much easier just to go back to jail. Yeah...
               They can't beat me up if I surrender!

Pirate 4  :{S} You're Felix, aren't you? You've come to bring in Briggs,
               haven't you?

           {M} Briggs said the guy who captured him was some amazingly tough
               thug named Felix. But I don't know... If this really is him,
               he doesn't look like the bad guy Briggs said he was.

-----

* - [028] has left.

[029]     :{S} If you so much as TOUCH me, I'll bite your nose off!

           {M} What's he staring at? Sheesh! This guy's a total lech!

[030]     :{S} Why's everyone so scared of you? You don't look so tough.

           {M} He's not so tough! Why's everyone running away? Just thump him
               good and be done with it.

-----

* - [031] has left.

Pirate 5  :{S} Did you really think you could come storming into Champa,
               Briggs's home, without a fight?

           {M} Why would Briggs run away like a little baby just because
               this guy showed up?

Pirate 6  :{S} Leave the women and the children alone. They've got nothing
               to do with this.

           {M} What are they doing here? Do they mean to captured us?

-----

[032]     :{S} Aw, come on! I'm not doing anything! Leave me alone!

           {M} Briggs is pretty tough. This guy must be a serious monster if
               he beat the captain...


#$#$#$#$#$#$#$#$#$#$#
$#  Obaba's forge  #$
#$#$#$#$#$#$#$#$#$#$#

Briggs    : Hold it right there!

            So, Felix, you've come. Don't assume I'll go so easy on you
            this time!

Obaba     : Is that boy him? The "mighty warrior" you told me about?

Briggs    : I told you he didn't look like much, Grandma... Weren't you even
            listening to me?

Obaba     : All you told me is that his name is Felix and that he is a
            "might warrior." Hmph. He doesn't look like the sort of person
            who's interested in stealing our jewels, though.

Briggs    : But that's not the point, Grandma! If you don't destroy him now,
            he's going to take me far away, and you won't ever see me again!

Obaba     : Oh, now he doesn't look like the kind of boy who would do that...

Briggs    : If he takes me away, poor Eoleo will be so sad! What do you say
            about that, huh?

Obaba     : Oh, that's just not fair. You know I can't deny my great-grandson!
            I don't see why I should be the one to get you out of this mess,
            but I can't bear to see Eoleo sad.

Briggs    : Grandma, please!

Obaba     : Oh, all right.

* - She pulls out some sort of item and turns to Felix's group.

Obaba     : Listen, you have no idea what you're getting into. I think you'd
            better leave.

-----------------------------------------------------------
     -(Yes)
Obaba     : Ah, you've made a good decision. You seem like a reasonable boy.
            Reasonable boys live longer.

* - When returning:

Briggs    : Back for more?

Obaba     : I wouldn't be doing this if it weren't for Eoleo, you know.

            I'm sorry. You look like quite a nice boy, but I just can't allow
            you to take my Briggs away.

* - She repeats her earlier remark.



     -(No)
<see below>
-----------------------------------------------------------

* - After saying no:

Obaba     : Stubborn, are you? Ah, well. If that's the way it's going to be,
            get ready for your medicine!

            Heart of the earth, fury of the forge's flames, grant me power!

* - She tosses the item into the forge. A similarly-colored large salamander,
    called Avimander, bursts forth from the flames and attacks Felix's group.

    After felling Avimander:

Obaba     : My salamander! You... beat my salamander... I thought he was
            unbeatable... How could this be? How did you do that? What...
            What are you?

Briggs    : Grandma, what's going on!? I thought you were going to protect me!

Obaba     : What do you mean, what am I doing? I've done everything I can!

Briggs    : Grandma!!! He's going to take me away! He's a bad guy! You have to
            do SOMETHING!

Obaba     : I'm sorry, Briggs, but you'll have to fight him yourself.

Briggs    : Wha-What!?

Obaba     : You heard me. I'm through pampering you. You have to get out of this
            yourself!

Briggs    : But... Grandma... Look at him! I mean, look what he can do!

Obaba     : I know, dear, but there's nothing I can do to help. You don't want
            him to take you away, do you?

Briggs    : But... what about poor Eoleo?

Obaba     : *Sigh* All right, all right.

Kraden    : Um. Excuse me... There seems to be a small misunderstanding.

Sheba     : Yeah! I don't like standing here listening to a pirate call US
            the bad guys!

Obaba     : Pirate! My Briggs?

Jenna     : He stole a ship from Alhafra and escaped from their jail!
            A ship WE helped fix!

Obaba     : Briggs, is this true?

Briggs    : Aw... But, Grandma, they...

Piers     : We should tell you, we're not here to take Briggs back to Alhafra.

Kraden    : So you've decided you don't want to run errands for the mayor of
            Alhafra?

-----------------------------------------------------------
     -(Yes)
Sheba     : Good. That greedy bag of hot air can do his own dirty work,
            for all I care.



     -(No)
Sheba     : Felix, I know you can't mean that. We didn't come to Champa for that
            bloated gasbag.
-----------------------------------------------------------

Obaba     : Briggs... Piracy? Why?

* - She heads towards him, but he runs around the forge to avoid her.

Briggs    : Grandma, it's not what you think? These guys, they...

Obaba     : Briggs, you just hush up!!! ...It all makes sense now. The gems,
            the food, your absence...

Briggs    : What do you mean? What makes sense?

Obaba     : They're telling the truth! And you, Briggs! You've been lying to me
            this whole time!

Briggs    : You're going to take their word over your own grandson's?

Obaba     : You got that right! I should have known better than to believe you,
            you scoundrel!

Chaucha   : He only did it for Champa!

* - Chaucha enters the room.

Briggs    : Chaucha! You came!

Chaucha   : I heard Felix had shown up looking for you. I was worried...

Obaba     : What do you mean, Briggs did it for Champa? All of that food...
            Stolen goods?

Chaucha   : No, we paid for everything we brought back with us.

Obaba     : But you stole a boat to do it, didn't you?

Briggs    : Grandma, we found those jewels ourselves, and we paid Alhafra well
            for that ship, didn't we?

-----------------------------------------------------------
     -(Yes)
Obaba     : Your story has the ring of truth to it.

Briggs    : Thank you, Felix. Your honesty speaks well of you.



     -(No)
Obaba     : So he's lying again?

Briggs    : Dang it, Felix, I'm not lying!
-----------------------------------------------------------

Chaucha   : We... were pirates, for a short while. Until we found the jewels.
            But if not for our efforts, Champa would have started away long ago.

Obaba     : But that doesn't excuse resorting to piracy!

Briggs    : Hey, it's not like we were doing it for the money! We wanted to
            save Champa!

Chaucha   : Those jewels we found are very valuable. We intend to repay each
            town we... borrowed from. Isn't that true?

* - Briggs pauses.

Chaucha   : What's the matter with you!? You said on the boat that we would
            repay every last town!

Briggs    : Oh yeah... You're right... We really ought to try to make amends
            for what we've done.

Chaucha   : That's the truth, Grandmother. Can you find it in your heart to
            forgive your only grandson?

Obaba     : All right, all right. I'm too old for grudges. But what about Felix?

Chaucha   : What do you say, Felix? Can you forgive my husband?

-----------------------------------------------------------
     -(Yes)
Kraden    : I agree, Felix. If each town is repaid what was stolen,
            I see no reason for complaint.



     -(No)
Kraden    : I don't know, Felix. We didn't come to capture Briggs.
            Why should we care?
-----------------------------------------------------------

Chaucha   : Do you hear that? They forgive you, too. That means you can
            leave Eoleo with nothing to fear.

Briggs    : I... I don't know what to say...

Chaucha   : You know, you look a little strange...

Briggs    : Oh... Oh, really?

Chaucha   : You haven't caught a cold, have you? Do you have a fever?

Briggs    : What are you talking about?

Chaucha   : No, I'm positive... You look flush, too... You'd better lie down
            before it gets worse.

Briggs    : She... worries about me.

Chaucha   : Hurry up and get into bed so you can get some rest!

* - She starts to leave. Briggs pauses.

Chaucha   : Oh, for goodness' sake! You don't want to five them your cold,
            do you? Come on!

* - He quickly follows her out of the room.

Obaba     : So... what brings you to Champa? I mean, you didn't come here to
            catch Briggs, from what I gathered... Ah, well... To be young and
            foolish again. If you ever need to consult with me on any number
            of subjects, you're welcome anytime.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Cave system within cliffs ]
[024]     :{S} I think those guys down in the harbor wanted to come up here
               and join us... All they had to do is ask, but I think they're
               chicken...

           {M} All those sailors who didn't join Briggs said they didn't want to
               be pirates. Now that Briggs's going straight, they want to join
               him. I think they're just cowards.

-----

[025]     :{S} Aren't you the ones who caught Briggs in Alhafra? You don't look
               it, but you're pretty strong.

           {M} That Felix sure comes off high and mighty. I hate those self-
               righteous types.

-----

[026]     :{S} When Briggs set sail, we thought we'd never see him again.
               Now, all of a sudden, he shows up, and with enough food to save
               our town forever!

           {M} I was just gazing out at sea, and then I saw Briggs's ship...
               I got all choked up.

-----

[027]     :{S} Why did you have to go and tell Obaba that we were pirates?
               I'll bet that really upset her.

           {M} I just know she's going to yell at us. The waiting is the
               worst part. Next to the yelling.

-----

[028]     :{S} We have so much food everywhere now! I hope Briggs goes off soon
               to bring us even more jewels and treats!

           {M} Briggs says he's sick and can't go to sea right now. But how
               can he not go? He has to make up for all of his evil deeds...

[029]     :{S} Eoleo still won't come down and play with us. I'm getting really
               cheesed off at him.

           {M} Eoleo is younger than I am, but he acts like he's a lot older.

[030]     :{S} Briggs came down with a cold. I guess that means he won't be
               sailing for a while.

           {M} Briggs's never been sick a day in his life. I wonder how he
               caught a cold now...

-----

* - [031] has left.

-----

[032]     :{S} You guys don't look much like warriors, but you sure are brave
               to fight your way in here.

           {M} Felix must be incredibly strong to get Briggs all worked up
               like that.

-----

Pirate 1  :{S} We're going to wait until Briggs feels better before we go out
               to sea again.

           {M} Suppose we went to get the jewels... How would we gather them,
               with that trap in the way?

Pirate 2  :{S} It's all my fault. If I hadn't messed with that switch, we'd have
               gotten everything.

           {M} At least we got some of the jewels before that stupid switch
               blocked us off.

Pirate 3  :{S} We really want to make amends. We just need Briggs to get better.

           {M} I was as shocked as the next guy that we couldn't reach those
               treasure chests...

Pirate 4  :{S} There were plenty of treasures on that island in the middle of
               the sea. If we get tired of waiting for Briggs, maybe you could
               come with us.

           {M} Briggs is just pretending to be sick because he doesn't want to
               follow up on his promise.

-----

Briggs    :{S} Once I'm over my cold, I'm setting out to get more jewels and
               make amends with Madra and Daila.

           {M} I'm certain that there are even more jewels back in that cave!
               If only I'd had the chance to grab a few more before that trap
               blocked our way!

Chaucha   :{S} I wonder what's wrong with Briggs. He was feeling so healthy
               and happy. He doesn't have a fever, and he's not coughing,
               but he says he's too weak to go out.

           {M} There is absolutely nothing wrong with Briggs. I just know he's
               hiding something from me...

Eoleo     :{S} Babu ba bubabu...

           {M} One of Papa's men touched a trap, and that's why Papa couldn't
               get all the jewels. Papa, I think you should tell Felix about
               that.

-----

Obaba     :{S} I mean it. If there's ever anything you need, just call on me.
               I'm always here.

           {M} Now I've done it. I said I'd help them with anything, but
               I'm only good at fixing broken things...


#$#$#$#$#$#$#$#$#$#$#
$#  Obaba's forge  #$
#$#$#$#$#$#$#$#$#$#$#

* - If one of the trident prongs has been collected, Felix presents it.

    The right prong is located in the Shrine of the Sea God (Indra).
    The center prong is located in Tundaria Tower (Tundaria, far south).
    The left prong is located in Ankohl Ruins (Angara, near Champa).

Obaba     : This looks like a weapon! It looks like part of a trident, but it's
            only one third of the whole thing, it seems... Why... Could it be?
            Is this the legendary trident of Ankohl? I'll hold on to this for
            you. It won't do you any good like this, and I'll keep it safe here.

            You seem unsure... You don't think I'll pull a fast one on you,
            do you?

-----------------------------------------------------------
     -(Yes)
Obaba     : Kids today. So mistrustful.



     -(No)
Obaba     : Ah, that's nice. Don't you worry!
-----------------------------------------------------------

Obaba     : If you bring me the other two pieces, I'll be happy to rebuild it
            for you.


* - Social Script:

Obaba     :{S} The legend says that anyone who holds the whole lance has nothing
               to fear from the sea.

           {M} All of my smithing knowledge and training was solely so that I
               might rebuild the legendary trident. I can't wait to get all
               three pieces and repair the ancient weapon of Ankohl.





* - Second prong:

Obaba     : Ah, have you found the second piece, dear? It's magnificent!
            I'll hold on to this as well. Wouldn't want it getting lost,
            now would we? Only one to go!


* - Social Script:

Obaba     :{S} Yes, there's no doubt about it. Those must truly be fragments of
               the legendary trident.

           {M} Soon, I'll have the chance to test my skills to their fullest
               extent! I can hardly wait!





* - Third prong:

Obaba     : Well done! You found all three pieces of the trident! That means I
            can begin work reforging the ancient trident of Ankohl! At last!

* - She approaches the forge.

Obaba    : We'll just toss all three pieces in here, shall we?

-----------------------------------------------------------
     -(Yes)
Obaba     : Just leave it to me...



     -(No)
Obaba     : There's nothing to be afraid of, dear. Just leave it to me.
-----------------------------------------------------------

Obaba     : Heart of the earth, fury of the forge's flames, grant me power!

* - She drops the prongs into the forge.

Obaba     : That's funny... Nothing happened.

* - Light fills the forge, soon followed by flames.

Obaba     : What's going on?

* - A pillar of fire rises in the center of the circle.

Obaba     : Something's happening! Is that... the legendary trident?

* - The flames fade; the trident floats in their place.

Obaba     : After all these years, the trident is complete again. But what's
            making it float like that? Regardless, the trident has been fixed.
            It belongs to you now, Felix. Use it well.


* - Social Script:

Obaba     :{S} The trident seems to have some amazing power... The legends must
               be true... No matter what you encounter at sea, no monster can
               stand against you with that trident.

           {M} All of my training was for the single purpose of reforging the
               ancient trident.


#$#$#$#$#$#$#$#
$#  Outside  #$
#$#$#$#$#$#$#$#

* - As Felix's group makes their way to depart:

Alex      : I see you've caught up with me again, Felix.

* - He approaches them from the northern area of the village.

Sheba     : Alex!

Piers     : Alex? Who is Alex?

Kraden    : Alex is a Water Adept. We had been traveling together, but he left
            us when we landed on Indra.

Piers     : A Water Adept?

Alex      : Ah, and I see you've made a new friend! You have been busy,
            haven't you?

-----------------------------------------------------------
     -(Yes)
Alex      : And you've found yourself a new Water Adept! Do you mean to
            cast me away, like old trash?



     -(No)
Alex      : Please... It's quite obvious that you decided to replace me with
            a new Water Adept. I expect you thought you'd never see me again!
-----------------------------------------------------------

Jenna     : What do you want with us now, Alex? Or did you forget you were
            the one who abandoned US?

Alex      : My dear Jenna... Have you come to despise me so, after all we've
            been through?

-----------------------------------------------------------
     -(Yes)
Sheba     : That's right, Felix! Why should we care about someone who just left
            us behind like that!?



     -(No)
Sheba     : Duh! You're the one who left us. It's pretty clear who despises whom
            here.
-----------------------------------------------------------

Alex      : My, aren't we a bitter bunch? And I was just trying to help you with
            your little task.

Kraden    : We have no need of your help. We can light the lighthouses without
            you.

Karst     : Oh... Can you really?

* - She approaches.

Sheba     : Karst!

Karst     : That's right, Karst! I'm flattered that you remember!

Jenna     : What is this, Alex? What's going on?

Alex      : Ah, how can I explain this...

Agatio    : What's going on is Alex is demonstrating his remarkable foresight
            once again!

* - A man approaches. Felix's group is obviously confused as to his identity.

Alex      : Oh, have you not have the pleasure of an introduction?

Karst     : He stayed back at the ship when I saw them in Madra.

Agatio    : I am Agatio. Let's se... That guy's Felix, and the girls are Jenna
            and Sheba, which makes him... Kraden. They look like an unreliable
            bunch of ragamuffins.

Alex      : Yes, they are rather useless, aren't they? That's why I finally
            had to abandon them, of course. But now, I believe I may have
            been... hasty in my judgment.

            You are Piers?

Piers     : H-How do you know my name?

Alex      : How soon they forget! We met you before, when you were being...
            detained. Who could forget the amateur Adept changing water into ice
            in that strange little town?

Kraden    : Ah! You saw that! That must be how you knew Piers was a Water Adept.

Alex      : In fact, I was even thinking of borrowing his ship at one point.

Jenna     : You would steal someone's boat? That's so typical, Alex!

Alex      : You wound me, Jenna... I only meant to borrow it.

Sheba     : Whatever you might have meant, that doesn't make it right!

Alex      : And just when I was about to seize the opportunity, you had to
            come back.

Piers     : You mean from Kibombo...

Alex      : I was mere moments too late.

Kraden    : Isn't that a shame.

Alex      : Still, because of that, I did meet Karst and Agatio, so perhaps
            it was my fate...

Jenna     : Can't you just stop talking about yourself for one second, Alex?

Karst     : Enough of your childish gibes! Alex, I want to know what makes
            these punks useful!

Alex      : Because they brought us the orb that Akafubu had taken. That shows
            some resourcefulness.

Agatio    : How so?

Alex      : The Kibombo are quite warlike... or were, at any rate.
            Recovering the orb was most likely not easy.

Karst     : They were just typical villagers, easily frightened with a small
            display of Psynergy...

Alex      : No... They would have used less abrupt methods than those you
            favor...

Agatio    : Oh? What methods would those be?

Kraden    : Alex said it clearly enough. We wouldn't terrorize people into
            doing what we wanted.

Karst     : Enough of this! Stop changing the subject! When are you going to
            light the remaining lighthouses?

Agatio    : Yes! Our patience is beginning to wear thin!

Karst     : If you waste much more of our time, we'll take those Elemental Stars
            and do it ourselves!

Agatio    : If we had a Wind Adept like Sheba and the Elemental Stars,
            we wouldn't need you.

Sheba     : Excuse me?

Alex      : I am, of course, opposed to their line of thinking. My experience
            with Saturos and Menardi suggests that, while they were fierce
            warriors... They are somewhat lacking when it comes to solving the
            mysteries of the lighthouses...

Karst     : You mean to say that they failed to solve the riddles?

Alex      : Miserably...

Agatio    : Are you suggesting they were simply brutes, incapable of logic and
            intelligence? And are you saying the same of us!?

Alex      : I'm afraid so...

Karst     : Alex... Whose side are you on?

Alex      : I am on no one's side. My only concern is to see the lighthouse
            beacons lit once again.

Agatio    : So you mean to leave the task to Felix?

* - Alex nods.

Karst     : Then why have we come all this way looking for Felix?

Alex      : I merely wanted to confirm that he and his companions had not
            forgotten their quest.

Agatio    : Is that truly all?

Alex      : I also wanted to introduce Felix to the two of you.

Jenna     : Why would you want to do that?

Alex      : With Saturos and Menardi gone, you probably felt very little
            pressure to complete your task. I cannot have that.

Sheba     : What do you mean by that!?

Alex      : With Saturos and Menardi gone, I felt another pair might...
            How shall I put this... Provide you with the proper incentive
            to complete your task.

Piers     : Is that some kind of threat?

Alex      : Take it as you wish. I just wanted to provide you with the proper
            encouragement.

Karst     : So, what? You've used us to your satisfaction, and now, our role
            is done?

* - Alex nods.

Agatio    : You only wanted us around to flex a little muscle and scare them
            into action? Fine.

* - He turns to Felix's group.

Agatio    : I suppose we will let you go today...

* - He departs.

Karst     : But we will always be nearby... pushing you to make your way to
            Jupiter Lighthouse swiftly.

* - She departs.

Alex      : I look forward to seeing you soon, Felix, somewhere very near
            Jupiter Lighthouse.

* - Alex begins to leave, but stops as he thinks of something.

Alex      : Kraden, am I right in recalling that you pursue this quest on the
            behalf of Tolbi's ruler, Babi?

Kraden    : This is true. I'm studying Alchemy because Lord Babi has ordered it.
            What about it?

Alex      : Ah, what a pity. It would seem all your studies... have been for
            naught.

Kraden    : What are you getting at, Alex?

Alex      : Only that it seems your Lord Babi has at last succumbed to the
            ravages of time.

* - Kraden pauses.

Kraden    : Lord Babi is dead?

Alex      : Oh, so you didn't know?

Sheba     : Lord Babi? Dead? Could that really be true?

* - Alex nods.

Jenna     : Alex! How would you know such a thing?

Alex      : Do not mistake me! We had no hand in Babi's passing. However,
            the people of Tolbi may be under the impression that our presence
            led to his death.

Piers     : Alex! Cut the melodrama and get to the point for a change!

Alex      : Simply put, I would recommend against traveling to north Gondowan
            for a while. I just thought it might be better if you focused on
            your quest, instead of exploration, for now...

Sheba     : How kind of you.

Alex      : Take it as you will...

            Very well. May we meet again.

* - He takes his leave.

Jenna     : So the only reason Alex came here was to threaten us?

Sheba     : And to bring us news of Babi's death, despite the fact that we
            asked for no such news!

Piers     : Perhaps he had his own reasons for telling Kraden...

Sheba     : What do you mean, Piers?

Piers     : If Kraden undertook this quest on behalf of Babi, then he no longer
            has any need--

Jenna     : Oh. Of course! I hadn't thought of that. Your orders were to find
            Lemuria, right, Kraden?

Sheba     : That's right. But if Babi really has died, you're free to go where
            you will, Kraden.

Kraden    : That's not true, Sheba. Certainly, my original reason for
            researching Alchemy was for Lord Babi...

Piers     : "Was for Lord Babi?" That's the past tense! What are your reasons
            now?

Kraden    : This is no longer solely for research... I do this because of what
            I've learned on this quest.

Jenna     : Your research?

Sheba     : What you learned on this quest?

* - Jenna and Sheba look at each other, both appearing quite perplexed.
    They begin to speak at the same time.

Jenna     : I'm not following you at all!
Sheba     : I don't understand a word of this.

Kraden    : Of course you don't! Felix is the only one I've spoken to about any
            of this...

* - They turn to Felix and, again, happen to speak simultaneously.

Jenna     : What!? You knew!?
Sheba     : That's not fair! Tell us!

-----------------------------------------------------------
     -(Yes)
Kraden    : Please, Felix... Let's not say too much about it just yet.



     -(No)
Kraden    : Felix is right. Now is not the time to tell you about it all...
-----------------------------------------------------------

* - They look upset.

Kraden    : It's... far too complicated.

Jenna     : Well, when WILL you tell us?

Kraden    : I am sure we will tell you once we get to Lemuria.

Sheba     : Do you promise?

Kraden    : I promise...

            Piers? You don't mind waiting?

Piers     : I cannot read minds, like Sheba, but I have a guess at what you're
            thinking...

Kraden    : A guess? What do you mean?

Piers     : You are a great scholar, Kraden, are you not? I believe your theory
            is correct. And to prove it, I want to return to Lemuria as soon as
            possible.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'31] ---        [Sea of Time]        --- [02'31] #$#
#$#$#                     Lemuria                     #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - The trident is used to break the force field surrounding Poseidon,
    who guards the way to Lemuria, and who would otherwise be unbeatable.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  If a current carries the ship out of the sea  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

Sheba     : Hold on to that tiller! Do you want us to get swallowed by the
            waves!?

Jenna     : I know you're worried, Sheba, but he's doing the best he can...

Piers     : That was an incredibly strong whirlpool, but I doubt it could sink
            us or destroy the shio.

Jenna     : See, Sheba? There's nothing to worry about. Even if we hit a
            whirlpool, we should be fine.

Sheba     : But still... Piers, can't you show Felix how to get past the
            whirlpools and into Lemuria?

Piers     : Er, yes, well...

Kraden    : What's wrong, Piers? Lemuria's just beyond these whirlpools,
            isn't it?

Piers     : Yeah, I... think so...

Sheba     : You... "think so"!?

Jenna     : Aren't you... FROM Lemuria? Shouldn't you know exactly where it is?

Piers     : Yes, I'm from Lemuria... I've never had to get back INTO it before!
            And besides, the tidal wave carried me out of Lemuria. I didn't come
            through here.

Kraden    : Oh, I see. So that must mean... You don't actually know which
            direction Lemuria is in, do you?

Piers     : Don't be silly! I mean... I just need to get my bearings.

Kraden    : Hm... That doesn't sound good.

            If Lemuria really is beyond these currents, then we'll need to find
            a way to get through them. And until we do... We won't be getting
            into Lemuria.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Passage to Lemuria proper  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - If you try to head back to Piers's ship:

Kraden    : Lost already, Felix? That's the way to the boat dock! You can't want
            to return already! We've only just gotten to Lemuria. We can't leave
            yet! There's still so much to see!





* - A statue on another ledge must be pushed aside via Move to as to jump onto
    the ledge. Two men observe this.

Man 1     : Why, that was Psynergy, wasn't it?

Man 2     : Are they Adepts?

Man 1     : Who ARE you!?

Man 2     : Are you the ones who defeated Poseidon?

-----------------------------------------------------------
     -(Yes)
Man 2     : That's quite something! Who are you, that you could defeat that
            leviathan?



     -(No)
Man 2     : But clearly, you are here, and the beast is gone...
-----------------------------------------------------------

Man 1     : If you are strong enough to defeat Poseidon, you are too dangerous
            to enter Lemuria.

Man 2     : The king's orders are clear! We cannot grant you entry.

Kraden    : King? Who is your king?

Man 1     : High Highness, King Hydros, of course...

Man 2     : His Majesty has ruled over Lemuria for centuries.

Man 1     : King Hydros has decreed that Lemuria must be kept safe from
            dangerous outsiders.

Piers     : You say that we are dangerous, but do you include me as well?

* - He steps forth.

Man 1 & 2 : Piers!

Man 1     : Did you join them in battle against Poseidon?

* - Piers nods.

Man 2     : Impossible! Everyone knows you possess great courage, but you are
            still a mere Lemurian!

Piers     : Such comments do us all a great disservice! I battled fiercely
            alongside my friends!

* - The two men look at each other, still somewhat unsure of the situation.
    Piers turns to Felix.

Piers     : Leave our landing to me.

* - He turns back to the other two.

Piers     : You have my word that we shall create no problems during our stay.
            Will you not permit us to enter?

Man 1     : Piers, I know you are a man of your word, but the king's orders
            must stand!

Man 2     : You understand that we cannot simply ignore the king's orders,
            don't you, Piers?

Piers     : What is King Hydros doing...

Kraden    : So, you people really take your kings seriously, don't you?

Man 1     : Insolent pup! Do not dishonor the king of Lemuria! We are peaceful,
            but quick to anger!

Kraden    : Pup? I must be twice your age! Who are you calling "pup"?

Man 2     : You wish to see Lemuria, and yet you know so little of us!
            I am far older than you. Show respect!

Kraden    : Pah! Older than me?! Inconceivable!

Piers     : Er... Actually, Kraden, these two are perhaps older than all of you
            combined... Babi must have spoken of this to you. In Lemuria,
            time passes quite slowly.

Kraden    : Ah... Well...I suppose I recall something of that sort or another...
            Maybe... But to imagine for a moment that these two gentlemen are
            older than I am? It's a bit much!

            But perhaps I was rude, and I hope you accept my apology.
            My ignorance misled me.

Man 1     : Well, just so long as we're clear on that.

Man 2     : But if your fighting is as skilled as your wordplay, then perhaps
            you aren't so dangerous to us.

Man 1     : I agree. Perhaps His Majesty will provide an exception in their
            case.

Man 2     : King Hydros might be willing to reverse his order if we confer
            with him, wouldn't he?

Man 1     : We shall speak with him at once!

Man 2     : King Hydros has been seeking news from beyond the Sea of Time.
            He will want to see you.

Man 1     : Wait here.

Kraden    : How long do you think we'll be waiting?

Piers     : Good point. Time means little to most Lemurians. Mere moments to us
            could seem like a lifetime to outsiders.

Man 1     : You seem young to me, and yet you are probably an old man among
            your people... I would imagine that you have probably done enough
            waiting in your lifetime.

Man 2     : King Hydros instructed us to be kind to the elderly at all times.

Man 1     : They seem trustworthy enough... Shall we let them in?

Man 2     : I can see no reason not to. We won't get in trouble, will we?

Piers     : I will be with them! Now, please, let me walk the streets of my home
            once more! I beseech you!

Man 1     : Then we place our trust in each of you. You may enter. But...
            don't do anything rash!

Man 2     : If you cause any trouble, we'll hunt you down and exact swift and
            terrible vengeance.

Man 1     : Do we have your word?

-----------------------------------------------------------
     -(Yes)
Kraden    : Ooo! Ooo! Finally! What could be waiting for me in Lemuria?
            I can't wait another moment!



     -(No)
Kraden    : We've come a long way to see Lemuria. I won't have anything ruin it
            for me now!

* - Alternatively, Kraden will say:

Kraden    : What!? Are you INSANE!? Or maybe you think you're funny?
            Because you're not! Maybe this whole quest is just a game to you,
            but it's not to me! Are you bored!? Do you want to go home!?
            FINE! That's it! Then let's go home!
-----------------------------------------------------------

Piers     : Oh, hush. I'll keep a close eye on them. You have nothing to fear.

Man 2     : Very well, Piers. We place our faith in you, then. Enter freely
            and peaceably.

Man 1     : You must already be aware of this, but you are not permitted to
            enter the palace.

Man 2     : If the king were to find out about this, we'd be in big trouble.

Piers     : Don't worry! I won't let that happen.

* - They two men take their leave.

Kraden    : Is this Hydros really so fearsome?

Piers     : Fearsome isn't the right word... King Hydros has lived longer than
            anyone. He is most wise. While everyone respects him and holds him
            in great reverence... It would be a mistake to call it fear.
            I certainly do not fear him. The king... He...

Kraden    : He what?

Piers     : You will understand once you meet the king yourself. But that does
            not matter now. Let's go! To Lemuria... The city you've all been
            longing to see...


#$#$#$#$#$#$#$#
$#  Outside  #$
#$#$#$#$#$#$#$#

* - Upon walking up the stairs to the third level, Kraden looks about.

Kraden    : Oh! Goodness!

* - He heads to the fourth level, where the palace is located.

Kraden    : Felix! Look over here! This palace is magnificent!



* - If you try to head down from the fourth level:

Kraden    : Where are you going, Felix? Let's take a longer look around!



* - Upon approaching the castle:

Kraden    : This place is remarkable... Truly remarkable...

Guard 1   : Who goes there! I've not seen you in Lemuria before!

Guard 2   : Wait a moment... You must be the travelers who arrived with Piers.
            Is your name Felix, perchance?

Guard 1   : Piers? You mean Piers, the Lost One?

Piers     : Have I earned a title in my absence? Well, worry not!
            Piers is lost no more!

            I seek counsel with King Hydros. Has High Highness been told of
            my return?

Guard 2   : Word was sent, but I do not know if it has reached the king.

Piers     : What do you mean?

Guard 1   : Lord Conservato is meeting with His Highness as we speak.

Piers     : Not Conservato...

Kraden    : What's wrong, Piers? You don't look pleased to hear that name...

Piers     : Kraden... What do you think of what you have seen of Lemuria?

Kraden    : It is a magnificent city! Or do you mean the castle? Both are
            magnificent!

Piers     : And you, Felix? Do you agree?

-----------------------------------------------------------
     -(Yes)
Piers     : Any newcomer to our town would doubtless feel the same at first.



     -(No)
Piers     : Ah! Yes, you marvel not at the present condition, but at the
            greater splendor of its past!
-----------------------------------------------------------

Piers     : In ages past, Lemuria was a far lovelier, more grand, and more
            lively city. High Highness, the kind, tells of days gone by,
            of a more brilliant Lemuria long before my birth. Over the countless
            years, our people have lost vigor, enthusiasm, creativity... Lemuria
            has fallen into slow collapse, a city that has lost its spark...
            Lemuria as you see it is only a shadow of the city of legend.

Kraden    : If only I had the chance to see the city in all its splendor.
            But how does Conservato figure in?

Piers     : King Hydros believes that our decay is related in some way to
            Alchemy.

Kraden    : Alchemy!?

Piers     : King Hydros wants to find a way to stop the ruin of Lemuria.

Guard 1   : If there were anything we could do to help stop it, we would.

Guard 2   : But the senators are unwilling to take action! They're stubborn,
            and they fear any change...

Kraden    : Senate? What is a senate?

Piers     : The senate is the group of elders who determine policy in Lemuria.

Guard 1   : Lord Conservato holds the highest office in the senate.

Guard 2   : The senate usually opposes any new ideas or proposals introduced
            before it...

Piers     : Word of our arrival will never reach the king as long as Conservato
            has his ear.

Guard 1   : And his conversations with the king are incredibly long.

Guard 2   : We have no choice but to wait patiently here.

Piers     : Why don't we spend our time looking around Lemuria until then...


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} I cannot remember the last time we had visitors in Lemuria.
               Not in a great while, certainly.

           {M} More of the same, today and every day. Nothing around here
               ever changes.

[002]     :{S} In Lemuria, we do not grow old. It must seem quite odd to those
               from the outside world.

           {M} I've aged so slowly, I no longer fear death, but at the same
               time, I have no motivation at all.

[003]     :{S} Drinking from this spring restores vigor and vitality!
               Want a sip?

           {M} These turtles have lived in the spring forever... It must be
               the water that does it...

[004]     :{S} Lemuria has no disease, no war... Anyone who saw it would think
               it a paradise. And yet... all who come to our city seek to leave
               soon after arriving. I, too, wish to leave.

           {M} I haven't been surprised in ages. I don't know what I'd do if
               something happened.

[005]     :{S} How old am I again? I quit counting after I turned two hundred,
               and that was long ago.

           {M} King Hydros is far older even than I am... How old is he?

[006]     :{S} Life never changes here in Lemuria. It can get rather dull,
               you'll find.

           {M} Sometimes, I think the buildings fall apart faster than we age.

[007]     :{S} I ought to feel surprised to see outsiders here, but I can't
               remember how to be surprised.

           {M} Long ago, a man named Lunpa drifted to our island. That was quite
               a surprise. Someone else came with him, but he fled so quickly.
               What was his name again?

[008]     :{S} It has been many, many years since a new child was born in
               Lemuria. Lemurians love children, but they only remain children
               for such a short time.

           {M} Everyone spoils me so much... I don't ever want to grow up!
               But in another 20 or 30 years, I will be an adult. Oh well.
               At least it's some kind of change.

[009]     :{S} We are the only children in Lemuria. I often with there were
               other children to play with.

           {M} Are there other children in the lands beyond the Sea of Time?
               Are there other people?

Cat       :{S} Meow... Mrrrfle...

           {M} No one in Lemuria feels any passion for anything. They're lazier
               than a cat in a sunbeam.

Dog       :{S} Woof! ...rrrrrROOF!

           {M} There's so much treasure buried here that you could dig almost
               anywhere and find something... So why doesn't anybody here dig?

Chicken   :{S} Bukbukbuk...

           {M} If it weren't for the people in the castle, the Lemurians would
               probably let themselves starve.

Cow       :{S} Moo.

           {M} Lemurians are so lazy that they make me look like a dynamo.
               And they live so long!





   [ Spring of Lemuria ]
* - Outside:

[010]     :{S} Do you wish to test your luck at the Spring of Lemuria?

               --------------------------------------------
                    -(Yes)
               Go ahead. Test your luck!

                 * - He moves aside. When speaking to him again:

               You look like you're in for a spell of good luck. After all,
               your aura glows brightly about you!



                    -(No)
               Well, then, I'll just take a turn... If you change your mind,
               let me know, and I will give you a chance.
               --------------------------------------------

           {M} No one is luckier than him who believes in his luck and has
               friends who believe in him.

* - Inside:

[011]     :{S} If you face away from the spring, toss in a coin, and land it in
               the target, good fortune will come. You've traveled a long way
               to be here. You should give it a try.

           {M} I'd love to test my luck, but I've used up all my coins.
               Maybe I'll take one out of the spring!

[012]     :{S} I remember an outsider who came to Lemuria and then spent DAYS
               testing his luck at the spring!

           {M} He had such a good time, he said he was going to build a spring
               like this in his hometown.

Signpost 1:{O} The Spring of Lemuria
               Face away and toss in a coin to test your luck.

Signpost 2:{O} The Spring of Lemuria
               Toss in a Lucky Medal to improve your luck.





   [ Residence to the east of Piers's ]
[013]     :{S} I have never been outside of Lemuria. I don't know what the
               rest of the world is like. If there weren't laws prohibiting
               us from leaving, I would be gone in an instant.

           {M} Who knows what wonders lie across the Sea of Time... I'd love to
               know, but... I can't stand places with little culture and no
               advanced civilization.

[014]     :{S} Now that Piers has returned, maybe he'll share his tales of the
               outside world with me.

           {M} The senate passed the law that prohibits us from leaving.
               But Piers was carried out to sea by the tidal wave. He can't be
               blamed for that...





   [ House of the Senate ]
[015]     :{S} Are you the warriors from beyond the Sea of Time who returned
               with Piers?

               --------------------------------------------
                    -(Yes)
               What can you uncivilized louts hope to bring to Lemuria?



                    -(No)
               Only savages and barbarians are wont to tell lies when confronted
               with uncomfortable situations.
               --------------------------------------------

           {M} Was that some form of Psynergy?

               --------------------------------------------
                    -(Yes)
               Ho ho ho! We Lemurians are masters of Psynergy all! Your powers
               are not special here.


                    -(No)
               No? Curious. But it does not matter. Lemurians are masters of
               Psynergy. It is of no import.
               --------------------------------------------


                 * - 2nd+ time:

               What does Hydros think will happen if he sets Alchemy loose
               on the world again!?

[016]     :{S} Come what may, I cannot approve of anything setting Alchemy loose
               on the world.

           {M} All of the members of the senate must remain opposed to breaking
               the seal. As long as we remain united, King Hydros cannot take
               any action to complete his plan.

-----

[017]     :{S} Long ago, the power of Alchemy was abused in ways that might
               bring about the end of the world. Because it was sealed away,
               the king claims, the world has begun to wither and decay.

           {M} Ever since Alchemy was sealed, time itself has seemed frozen.
               In my mind's eye, I do not see anyone who will go along with
               the king's plan.

[018]     :{S} Has Lemuria fallen into decay, I ask you? Nay! Only by casting
               aside Alchemy has the world been saved from itself!

           {M} Certainly, Lemuria has lost some of the splendor that once filled
               its streets. But to think that Alchemy could restore this is
               madness itself!

[019]     :{S} And now, rumors abound of a group of fools who are actually
               attempting to restore Alchemy. It is only because Alchemy was
               sealed away that the world has enjoyed this lasting peace.

           {M} If Alchemy were loosed upon the world, people would fight again
               to control the Stone of Sages. Alchemy must remain sealed away,
               if for no other reason than to avoid this strife.

-----

[020]     :{S} Do you seek to know more about the draughts that provide us with
               such longevity?

               --------------------------------------------
                    -(Yes)
               Once, Lemurians bottled special draughts to leave here and travel
               through Weyard... A man named Babi stole the remainder of our
               precious draughts and fled Lemuria.



                    -(No)
               Then I shall tell you this: So long as we drink of the Lemurian
               Spring, we live long. We no longer leave our home, so we have
               no need to make our draughts of old.
               --------------------------------------------

           {M} Even though we no longer prepare the draught, the water of
               our spring sustains us...





   [ Palace - Outside ]
Guard 1   :{S} The king is holding counsel with Lord Conservato right now.
               It might be a while before you can see him.

           {M} How much longer will Conservato be in there? They've been talking
               for ages now.

Guard 2   :{S} The king will be thrilled to hear his trusted Piers has returned.

           {M} I had heard Piers was back, but I didn't believe it until now...
               You seem much more confident, Piers. Everyone has bene noticing
               it.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Piers's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

P's Uncle :{S} Are you the travelers that came here with Piers?

               --------------------------------------------
                    -(Yes)
               <see below>



                    -(No)
               No? Ah, interesting. I wonder when Piers will come to see me.
               --------------------------------------------

           {M} I was--what is the word?--surprised when I heard Piers had
               returned. I hope that I get to see him soon.

* - After saying "Yes", Piers steps forward from the group:

Piers     : I am sorry it has taken me so long to visit, Uncle.

P's Uncle : Piers! You are alive!

Piers     : Yes, I've managed to survive against a great many trials. 

Kraden    : What a fascinating coincidence! We've stumbled across Pier's uncle's
            house!

P's Uncle : I must thank you all for looking after my nephew.

Piers     : This is Felix and Kraden. They are my friends, and have aided me
            tremendously.

P's Uncle : If my sister could only hear how timid young Piers has become a
            mighty warrior...

Piers     : Where is my mother? We've been so busy since we arrived that I
            haven't had a chance to see her.

* - Piers looks around, noticing items (mostly bottles) strewn about the floor.

Piers     : Now that I think about it, this place is a mess. What happened?
            Mother is always so neat...

            ...No! She hasn't... fallen ill again, has she?

Kraden    : There is still illness in Lemuria?

Piers     : My mother was born with a weak heart...

P's Uncle : Piers... I'm sorry... Your return comes too late... After the tidal
            wave washed you to sea, your mother suddenly fell ill... The shock
            of losing you was too great for her poor heart. She held out hope
            for your safe return until the very end. Perhaps your mother gave
            herself up to ensure your survival... Does that not sound like
            your mother?

Piers     : Where is she now?

P's Uncle : She rests in the cemetery now. Check the headstones...
            You will find her.

* - Piers rushes out of the house.

Kraden    : What should we do, Felix? Should we follow Piers?

-----------------------------------------------------------
     -(Yes)
Kraden    : After all we've been through, the least we can do is offer Piers
            our condolences.



     -(No)
Kraden    : You're right. Piers probably needs some time alone right now.
-----------------------------------------------------------


* - Before leaving:

P's Uncle :{S} I'm so relieved that Piers has returned to me alive. He is the
               last of my relatives. Without him, I would be alone.

           {M} Poor Piers... Being born in Lemuria and gifted with long life...
               Only to lose his father in his youth and his mother now.
               He faces many long years of loneliness.



* - When beginning to leave the house:

P's Uncle : Wait... I ask that you leave Piers to his mourning for now...
            Now he is struggling with the loss of his mother. He needs time.

* - Felix nods.

P's Uncle : You came to Lemuria to learn more of Alchemy, did you not?

            I suspected as much. Piers was right to bring you here. Piers told
            me his secret... The mission he was given by His Highness the king.
            Even had the tidal wave not carried Piers off, he would have left...
            Such was his fate.

            You look confused... Piers told you about this, did he not?

-----------------------------------------------------------
     -(Yes)
P's Uncle : Of course... He must trust you a great deal.



     -(No)
P's Uncle : Curious... I can't understand why he would do that...
-----------------------------------------------------------

P's Uncle : If Lord Conservato had not led the senate to oppose him, he would
            have left sooner. I wonder what news Piers has brought with him.
            Either way, I do know why he has brought you here.

            Felix... Don't tell me that he hasn't at least told you that much!

-----------------------------------------------------------
     -(Yes)
P's Uncle : You say he's told you, but you look rather confused.



     -(No)
P's Uncle : Did Piers tell you nothing before bringing you here to Lemuria?
-----------------------------------------------------------

P's Uncle : Unfortunately, I know little more than that... While Piers confronts
            his sorrow over the loss of his mother, you have some time...

            I shall write you a letter... So that you can see Lunpa...
            Lunpa has locked himself in his tower and rarely comes out,
            but if I send him this, he will see you.

* - He hands the letter to the bird that had been perched on the table by him.

P's Uncle : All I need is a bird to carry it to him in his tower.

* - The bird flies off.

P's Uncle : There. You should be able to see him now.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
* - Cemetery:

Piers     :{S} ...

           {M} Mother... Why have you left me...



   [ Buildings ]
* - Piers's residence:

P's Uncle :{S} Go to Lunpa's tower. He will see you now.

           {M} Lunpa has given the kind tremendous aid on this matter.
               He will have much to tell them.


#$#$#$#$#$#$#$#$#$#$#
$#  Lunpa's tower  #$
#$#$#$#$#$#$#$#$#$#$#

* - Lunpa speaks from the apex as Felix approaches the door on the ground level.

Lunpa     : Are you kids Piers's traveling companions? The door's broken,
            I'm afraid. But I opened up a window just above the door.
            Sorry about this, but you'll have to climb through there.

* - Lash can be used to tie a rope to a stake near the window.

    If Piers took the Lash Pebble with him:

Lunpa     : What's the matter? Can't you climb up? ...Fine. Just a moment.

            You came all this way and then got stuck here? You can't be
            very bright.

* - He puts a rope in place.

Lunpa     : There! Is that better? Now climb up here.



* - Inside, on the lowest floor:

Lunpa     : Honestly, I'm amazed that anyone can travel so far across the world
            in this age.

            Say, Piers isn't with you! Er... why not?

Sheba     : His mother passed away... He's gone to visit her grave.

Lunpa     : Of course... His mother... He loved her dearly. A terrible loss...
            It must be hard on him.

            Well, Piers may not be here, but we still have much to discuss.
            If Piers brought you, you must be working to break the seal on
            Alchemy, right?

-----------------------------------------------------------
     -(Yes)
Lunpa     : Ah, Piers has done quite well in finding you!



     -(No)
Lunpa     : That doesn't make sense... He wouldn't have brought you to Lemuria
            if you weren't helping.
-----------------------------------------------------------

Kraden    : What mission could the good King Hydros have assigned to Piers?

Lunpa     : What? Piers has told you nothing of his mission?

* - Everyone nods.

Lunpa     : ...Really?

* - They nod again.

Lunpa     : So you actually have nothing at all to do with Alchemy!?

Jenna     : Our parents were kidnapped by the Fire Clan, far to the north.
            We are only firing the lighthouse beacons to gain their freedom...

Lunpa     : King Hydros told me that Venus and Mercury have been ignited
            once again. Was that your doing?

* - They nod.

Lunpa     : I'm afraid I know nothing of any northern "Fire Clan."

* - He turns to Kraden.

Lunpa     : But that doesn't explain you, sir. You're clearly not related to
            these two. What are your goals?

Sheba     : Kraden joined us on this quest on behalf of Lord Babi of Tolbi.

Lunpa     : ...Babi? I only know of one man named Babi... But it couldn't...

Kraden    : Master Lunpa, the Babi we speak of is the same man you knew
            long ago.

Lunpa     : Ah! So... he's still out there, living in the outside world?

Kraden    : Well, that might not be the most accurate way of putting it.

Lunpa     : Most... accurate? My, you certainly have an odd way of turning
            a phrase...

Kraden    : He was living, yes... Until recently, that is...

Lunpa     : So, Babi passed away... But only recently, you say?

Kraden    : When he finally ran out of his mystic draughts, his spirit began
            to wane.

Lunpa     : Then... I no longer know anyone in the world outside.

Jenna     : But... Aren't you Lunpa, the Righteous Thief?

Lunpa     : I was called that once, long, long ago. Why do you ask?

Jenna     : I'll bet there's at least one person in the outside world whom you
            still know.

Lunpa     : Who would that be?

Jenna     : There's a town called Lunpa in northern Angara. A man named Donpa
            lives there.

Lunpa     : I settled that village! And Donpa... He is my son...

Kraden    : Now, your grandson, Dodonpa, rules over your village.

Lunpa     : Rules? Rules is an ill-sounding word.

Jenna     : But it's an accurate one, Lunpa. Dodonpa is an evil thief, who has
            caused much trouble in Angara.

Lunpa     : What has become of my son? How could he permit such a thing to
            happen?

Kraden    : Master Lunpa, don't you have any idea how old Donpa is?

* - Lunpa doesn't seem to.

Kraden    : He is as I am. An old man... He may be older even than I.

Sheba     : If this news outrages you, why don't you go and set Dodonpa
            straight?

Lunpa     : If only I could...

* - Jenna turns to Felix.

Jenna     : Is this the only reason we're here? To bring news of the outside
            world?

-----------------------------------------------------------
     -(Yes)
Lunpa     : You are kind, Felix, but there are much more important matters
            at hand.



     -(No)
Lunpa     : Yes, yes... I am sorry we were sidetracked. We have much more
            to discuss...
-----------------------------------------------------------

Kraden    : But before we begin, there is one thing I must say...
            You don't mind, do you, Felix?

-----------------------------------------------------------
     -(Yes)
Kraden    : Clearly, your judgment on this matter is fogged, Felix.
            I must speak.



     -(No)
Kraden    : I knew you'd agree.
-----------------------------------------------------------

Kraden    : I have discussed this with none but Felix, but... I have my own
            reasons for this quest.

Sheba     : What do you mean?

Kraden    : Only that I have my own reasons for wanting to see the beacons lit
            again...

Jenna     : Why are you telling us all of this now?

Kraden    : Because I feel this quest is deeply linked to Lemuria. I thought
            it odd that Lord Babi shoulder order me to research Alchemy.

Sheba     : Hey, wait a minute... Is this what you promised to tell us once we
            reached Lemuria?

Kraden    : Yes, yes... May I continue?

            Long ago, before Alchemy's power was sealed... There were many
            civilizations as advanced and cultivated as Lemuria. At the moment
            that Alchemy was sealed away, most of those civilizations began to
            wane... Until eventually, they vanished. I have formed certain
            theories now, suggesting that this may be related to the seal on
            Alchemy.

Jenna     : Let me get this straight... You felt you couldn't tell us this
            until we were in Lemuria?

* - Kraden nods.

Sheba     : And you only wanted to come to Lemuria to test your theories and see
            if they were true...

* - He nods again.

Jenna     : But even if everything you said IS true, what does it all mean?

Lunpa     : If your theories are correct, the world itself will wane and
            vanish... Won't it, Kraden? Piers never spoke of this to you,
            did he? If you came to this theory on your own, you are indeed
            a wise scholar. We would do well to trust you.

Kraden    : What do you mean?

Lunpa     : King Hydros and I, as well as others in Lemuria, hold the same
            beliefs that you do, Kraden.

Kraden    : You do!?!

* - Lunpa nods.

Lunpa     : Civilizations thrive by building upon the knowledge of the past.
            Knowledge gained in one generation should be taken even further
            by the next. Thus, knowledge and learning continue to grow.
            This is the natural course of civilization.

            But where is the world today? The great civilizations of old have
            all withered and vanished. We are all isolated and alone. You have
            encountered many cultures in your travels. Are any of them capable
            of building the great sanctums and lighthouses you have seen?

            No, they are not... But this is not the only sign of the decay
            you have theorized...

            I think it best that you hear the rest directly from His Majesty,
            King Hydros. Yes, Kraden! We shall go to visit the king!

Kraden    : Ah, but King Hydros is in counsel with Lord Conservato. We might not
            be allowed in.

Lunpa     : Conservato? That fool. He refuses to acknowledge what he can see
            with his own eyes! I will meet with the king and press our evidence
            upon Conservato. Come with me!

* - He runs to the door, having forgotten that it's broken.

Lunpa     : Gah! Stupid door!

* - Energy surrounds him.

Lunpa     : HAHHH-AHH!

* - He rams the door, throwing it open.

Lunpa     : Pah! At last, you are open!

* - He turns to the others.

Lunpa     : To the king's chambers!

* - He takes off.

Sheba     : Lunpa ought to be as old as Lord Babi was, but he has so much
            energy!

Jenna     : He's got a fire in him.

Kraden    : I do wish I could have heard more about Lord Babi, though. But come,
            Felix! To the king's palace we go!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Lunpa's tower ]
Bookcase 1:{O} There's a book called "The Great Adventures of Lunpa."
               ...Written by Lunpa, no less. "When the great flood came,
               we fled our homes by boat. Waves engulfed our ships.
               We came to in a strange land called Lemuria."

Bookcase 2:{O} I found a letter from Babi. On the outside, it reads,
               "To my dear friend Lunpa." Babi wrote, "Forgive me, Lunpa,
               but I must leave the island without you."





   [ Palace - Outside ]
Guard 1   :{S} King Hydros awaits you. You are free to enter.

           {M} They are clearly using Psynergy, which makes them Adepts...
               But are they so important that High Highness must make time
               for them right away?

Guard 2   :{S} High Highness, the king, has instructed that we let you pass.
               You are welcome here.

           {M} What does High Highness have in mind? Piers, his friends,
               and Lunpa are all here.





   [ Palace - Inside ]
[021]     :{S} If you seek the counsel of High Highness, the kind, follow the
               passage to the doors at the end.

           {M} Oh, dear! Using Psynergy in the palace of the good King Hydros!?
               What ill-mannered buffoons!

[022]     :{S} High Highness never leaves a meeting with Conservato in a
               good mood. Good luck.

           {M} High Highness, the king, is most temperamental, which is a rare
               trait in Lemurians. Lord Conservato is calm and collected,
               like a true Lemurian.

[023]     :{S} Conservato and the king were yelling so loudly, that I could
               hear them from out here.

           {M} Lord Conservato only raises his voice when he speaks with the
               king. Their debates frighten me. I can't stand the yelling.

-----

[024]     :{S} King Hydros is the wisest of all the Lemurian kings... But I
               understand why Conservato and his senate oppose the king's plans.

           {M} High Highness is worried that Lemuria will with away. What a
               ridiculous notion!

Bookcase 1:{O} Here's a book called "Alchemy and Ancient Civilization: Part I."
               "Through the use of Alchemy, civilization undergoes great growth
               and improvement.

Bookcase 2:{O} Here's a book called "Alchemy and Ancient Civilization: Part II."
               "Those who master Alchemy shall master the world."

Bookcase 3:{O} Here's a book called "The Great Lemurian People." "The chosen
               master of water will be a native son of Lemuria."

Bookcase 4:{O} Here's a book called "Elemental Lighthouses." It reads,
               "The beacons of the four elemental lighthouses brighten the
               fringes of Weyard."

Bookcase 5:{O} Here's a book called "The History of Lemuria." An excerpt:
               "Only traces of the once-brilliant land of Lemuria remain today."

-----

Wardrobe  :{O} What the--!!! What's with all these bathrobes?!? Where are
               the baths?

-----

[025]     :{S} The senate holds King Hydros in poor regard because he favors
               Lunpa's wisdom over their own.

           {M} I trust the king. If His Majesty is wrong, the fault lies with
               Lunpa, not with him.

-----

[026]     :{S} He is still in chambers with Lord Conservato. Why is he granting
               them entrance?

           {M} Lord Conservato holds the most power in Lemuria after the king.
               I don't think he'll take kindly to the advice of outworlders
               like these.


#$#$#$#$#$#$#$
$#  Palace  #$
#$#$#$#$#$#$#$

* - In the hallway leading to Hydros's chamber:

Guard     : You are Lord Felix, correct?

-----------------------------------------------------------
     -(Yes)
* - The guard steps aside.



     -(No)
Guard     : Then you have no business here! His Majesty is involved in a most
            important meeting right now.
-----------------------------------------------------------

* - Felix's group enters the king's chamber. Piers has also come.

Hydros    : It would seem the warriors of which you spoke have arrived.

Lunpa     : So it would, Your Highness. I shall call them to us immediately.

Hydros    : There is no need, Lunpa. Let us go to them.

Conservato: Hydros! Would you see me dishonored thus? They ought to present
            themselves to us!

Hydros    : I do not go to present myself to them, Conservato. I am merely going
            to where they are. I have something that I wish to show everyone.

Conservato: Regardless of your reasons, sire, I will not go to them!

Hydros    : Do as you will, Conservato. However, WE shall go.

* - Hydros, Lunpa and Piers approach Felix's group at the entrance.

Hydros    : I heard of your arrival. It is quite remarkable that you were able
            to reach Lemuria. Welcome.

Piers     : Allow me to introduce my companions. This is Sheba... Jenna...
            Felix... ...And Kraden.

Lunpa     : Kraden is the one who told me of the outside world's civilizations,
            of their condition...

Hydros    : Ah, Kraden! Lunpa describes you as a remarkable scholar.
            Your research impressed us.

Kraden    : Thank you, Your Highness.

Hydros    : Your theories are correct. Our world is now on a path to
            destruction.

Conservato: And who has decided this? You, Hydros? Some civilizations have
            vanished, surely, but that is the way of the outside world.
            Look around you: Lemuria remains unchanged!

Hydros    : Don't delude yourself. Lemuria has been in slow decline for ages
            now, but that can wait.

            My most trusted scholars have reached this conclusion after
            extensive research. I sent Piers to confirm this for me...

Conservato: So you admit it, Hydros! You violated the directive of the senate!
            You used the tidal wave as your chance to send Piers away, despite
            our commands!

Piers     : You are incorrect. The tidal wave carried me away by chance alone.

Hydros    : Conservato, you must know that the tidal wave was caused by
            Poseidon's return! Only a fool would have chosen to send a man
            to sea if he knew that this would have happened.

Kraden    : What was it that you intended to have Piers confirm?

* - Hydros snaps his fingers, causing the room to darken and a map to appear
    below a sheet of glass on the floor.

Hydros    : This map shows the ancient world, when Lemuria still traded with
            people on the many continents.

* - http://img476.imageshack.us/img476/4582/map1ancientil1.png

    The continents' positions are significantly different in the present.

Conservato: It was a great age... A time when the world shined brightly.

* - A new map appears.

    http://img142.imageshack.us/img142/278/map2lunpalo1.png

Hydros    : And this... is the map Lunpa had with him when he arrived in Lemuria
            150 years ago...

Lunpa     : I used this map to sail around the world. It is quite accurate.

Kraden    : In-Incredible!

Hydros    : You understand, Kraden...

Sheba     : What do you understand?

Kraden    : Well, unless my eyes deceive me, the continents have shrunk since
            the golden age...

Jenna     : That's insane!

Lunpa     : It is not insane! It is true!

Hydros    : Perhaps this will make the point more clearly. Look at these two
            maps side by side.

Kraden    : There's no mistaking it. The continents on Lunpa's map are clearly
            smaller...

Conservato: Lies! Nothing but lies!

* - He approaches the others.

Conservato: What do you hope to gain from foisting these lies upon our people?

Hydros    : You know well that I hope to gain nothing more than the truth,
            Conservato.

Conservato: And who do you expect will believe such nonsense?

Hydros    : If you do not believe the evidence before your eyes, what do you
            believe? Do you believe the Lemurian map to be accurate to this day?

* - Conservato nods.

Hydros    : Tell me, Piers... You were able to investigate this matter,
            were you not?

Piers     : Thanks to Felix and my companions, I was able to travel much of the
            Eastern Sea.

Hydros    : And what did you find?

Piers     : I found, in truth, that Lunpa's map is the more accurate of the two.
            However, the world seems even smaller now than it appears on
            Lunpa's map...

Conservato: What are you saying?

Kraden    : Time itself has stopped... Think of Weyard as a living, breathing
            being, possessing its own life force... The four elements are the
            nourishment needed to sustain this being.

Lunpa     : Kraden... This is exactly what King Hydros himself has said to me!

Hydros    : Ever since Alchemy was sealed away, the world has been cut off from
            its nourishment. It has gone into a state akin to hibernation.

Kraden    : By using less energy, Weyard prolongs its life...

Hydros    : Yet when hibernating, the being has only stopped its own clock...
            not the flow of time around it.

Kraden    : When a bear sleeps through the winter, it needs only wait for spring
            to come...When it awakens, it can nourish its weakened body again...

Piers     : But if spring never comes, the bear will eventually die...

Lunpa     : Weyard is wasting away. Its continents shrinking, because its
            spring has never come.

Conservato: Hydros, how can you make such outrageous claims? The world is not
            alive...

Hydros    : Tell me, Conservato, why do you think Poseidon has returned?

Conservato: Do you have the answer, Hydros?

Hydros    : The elemental lighthouses... Felix and his companions have lit
            the beacons on both Mercury and Venus Lighthouse.

Conservato: What!? Have you any idea what will happen if you set that evil loose
            upon the world again?

-----------------------------------------------------------
     -(Yes)
Conservato: You know that it could bring about the destruction of the world,
            and yet you did it anyway?



     -(No)
Conservato: When the four beacons are fired, Alchemy will be released, and
            our world, destroyed.
-----------------------------------------------------------

Conservato: My lord, you cannot possibly intend for these people to light the
            remaining beacons!?

Hydros    : I do indeed, Conservato, and I also fear the possibility that
            Alchemy will destroy the world. But I cannot stand by, knowing
            as I do that the world will wither and die if we do not act!

Conservato: This is madness, Hydros! Does the threat of Alchemy mean so little
            to you? Would you put the world in even greater danger to satisfy
            your theories!?

            With only two of the beacons lit, I assume you intend to send Piers
            out again?

Piers     : And I will go, Lord Conservato. Felix has need of my power!

Conservato: Then go, Piers... But if you do, say farewell... for you will never
            be able to return. You will be banished from Lemuria forever.
            You know our laws. Are you prepared for the outcome?

            I myself am disgusted by the whole matter. I take my leave of you,
            Hydros.

* - Conservato heads into the hallway.

Conservato: But I warn you... I will NOT permit you to go through with this
            madness!

* - He departs.

Kraden    : What will you do, Your Highness?

Hydros    : I knew this outcome was inevitable. But I could not sit silent while
            our world drifted down the path of its destruction.

            I want you to light the remaining beacons before you return.

Sheba     : That's what we intend to do, but we cannot leave the Eastern Sea...

* - Reasons:

    * A large stone blocks the way in Gondowan Cliffs (Indra/Gondowan).
    * Stone spires jut up from the water in the spaces between Indra/Osenia and
      Osenia/Tundaria.
    * Gondowan and Angara are connected by land.
    * Stones and bridges obstruct the rivers of Gondowan.
    * None of Angara's rivers can be entered.

Hydros    : I have already heard of this problem from Piers...

* - Lunpa produces a treasure chest, which contains the "Grindstone."

Lunpa     : This is something I found by accident in some ruins back in my days
            as a thief.

Hydros    : I'm not sure what is it, but it seems to contain some powerful
            Psynergy.

Piers     : Seems to? You are not certain?

Hydros    : It is a Psynergy that we Lemurians are unable to use.

            I understand you travel with many different kinds of Adepts,
            do you not, Felix?

Kraden    : If we include Piers in our numbers, we have one Adept for each of
            the four elements.

Hydros    : Then at least one of you should be able to use the Psynergy that
            this contains.

Lunpa     : King Hydros believes the item can only be used by one who wields
            Psynergy of the earth.

Hydros    : If I am not mistaken, it is a powerful Psynergy we call Grind.
            If you master this Psynergy, the reefs that block your way shall
            pose no trouble anymore...

Lunpa     : With Grind, you should be able to create a path by which you can
            sail into the Western Sea.

Hydros    : Go, brave Adepts! By your hands, may the remaining lighthouses
            burn bright once more!

Lunpa     : That Psynergy is quite powerful. It can only be trusted to a very
            few people. That His Highness has given it to you should illustrate
            how great his expectations are. I have no doubt that your journey
            will be fraught with ever-increasing danger... But we are counting
            on you, Felix.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ House of the Senate ]
* - Upon approaching the door:

<game>    : The door is locked... It sounds as if there's a raucous caucus
            going on inside...





   [ Palace - Outside ]
Guard 1   :{S} I've never seen Lord Conservato so angry before...

           {M} I'm sure the senate has something to say about this.
               What's going on around here?

Guard 2   :{S} Lord Conservato has ordered us to prevent you from leaving the
               island... But I cannot see why he would do something like that.

           {M} How could Lord Conservato expect someone like me to believe that
               King Hydros... Would order Piers to destroy the world?





   [ Palace - Inside ]
[021]     :{S} Both Lord Conservato and the king want peace for us, so why
               must they fight all the time?

           {M} The king's leadership is too progressive... It's as though he
               invites opposition. Of course he doesn't get along with the
               senate. It's their duty to protect the laws of old!

[022]     :{S} Maybe once you have left, the king and Conservato will come to
               an accord.

           {M} Whenever outsiders arrive in Lemuria, it means trouble.
               Piers has done nothing but stir up trouble by bringing them here.

[023]     :{S} Today, His Highness and Lord Conservato were arguing more loudly
               than ever before!

           {M} What will happen to us? Will Lord Conservato be able to stop the
               king's plans?

-----

[024]     :{S} If Hydros plans to unleash Alchemy upon the world again, then I
               am against it.

           {M} As long as I can live in peace, I am happy. I suppose that is a
               sign of growing old...

-----

[025]     :{S} If you and Lunpa were all to leave Lemuria, I think we'd have
               peace and quiet here again.

           {M} I know why Lemuria ended all its dealings with the outside
               world... Lemurians want peace. We desire no change.

-----

[026]     :{S} Lord Conservato seemed very angry. Maybe that's why he called for
               a senate meeting.

           {M} The senate's reports usually tend to influence the popular
               opinion in Lemuria. I'll bet that is a constant annoyance to
               the king...

Guard     :{S} I think I overheard something I shouldn't have... I'll forget
               everything.

           {M} The actions of King Hydros are treasonous. They betray the will
               of his people.

Hydros    :{S} Do not listen to Conservato. We cannot let the world wither and
               die. Go, brave Adepts! By your hands, may the remaining
               lighthouses burn bright once more!

           {M} My people may not desire change, but I cannot let that stop me.
               I do this not for myself, but for all those yet to be born
               throughout Weyard.

Lunpa     :{S} You must sail to the Western Sea. Do not worry about Lemuria.
               Ignite the elemental beacons. Conservato lacks the conviction
               to discuss these matters with the people of Lemuria.

           {M} His Majesty has come to this decision on his own, without the
               counsel of his advisors. This is why I must remain by his side
               and support his decision.

-----
* - Hydros's bedroom:

Bookcase 6:{O} Here's a book called "The Diary of Hydros." "Piers is most
               definitely still alive. I pray for his safe return."


#$#$#$#$#$#$
$#  Dock  #$
#$#$#$#$#$#$

* - Upon setting off:

Sheba     : Umm... Piers?

Piers     : Yes, Sheba? What is it?

Sheba     : There's something I've been meaning to ask you... Something I have
            to ask you...

Piers     : Ask me, Sheba.

Sheba     : You and I look roughly the same age, but how old are you, really?

Piers     : Is that your question, Sheba? It's not important!

Jenna     : It is to me. If you are much older than us, then I'm afraid we've
            not shown you the proper respect.

Kraden    : She's got a point.

Piers     : Don't worry about such things. Please, treat me as you have
            all along.

Kraden    : No, that won't do. You have to tell us.

Piers     : What!? Come now! This is silly!

Sheba     : No, Piers! Tell me!

Piers     : You're afraid you haven't shown me the proper respect, and yet
            you make demands of me?

Jenna     : Come on, Piers... You can tell us. How old are you really?

Piers     : This has nothing to do with respect! You just want to know how old
            I am, don't you!

Sheba     : Hee hee!

Jenna     : Heh heh!

Kraden    : Oh ho ho ho!!!

Piers     : I knew it! Come on, Felix! Can't you get them off my back?

Felix     : ... ...

Piers     : You're in this too, aren't you, Felix? I've had it with your
            conspiracies! I will not tell you!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'32] ---          [Osenia]           --- [02'32] #$#
#$#$#                     Yallam                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Yallam doesn't get many visitors. Hasn't for a long time. I'd
               love to know a little about what's going on in the outside world.

           {M} Yepp was the one who visited the lands beyond eastern Osenia.
               Since he died, we've had no news from the outside world at all.

[002]     :{S} Our master boatsman, Yepp, died. Now, all we have to remember him
               are the songs he wrote.

           {M} Singing with Yepp and all the children in the village helped us
               remember the songs. It's funny how we all memorized every one of
               Yepp's songs.

[003]     :{S} If Yepp were alive today, our village would be thriving.
               He brought us lots of work.

           {M} Those pearls Yepp brought back from the sea were the most
               marvelous things I've ever seen. If he were still with us,
               Yallam wouldn't be in this terrible fix.

[004]     :{S} Yepp was the one who taught me how to handle a boat. That was
               right before he died... He'd promised to teach me how to dive
               for pearls... Poor Yepp. I really miss him.

           {M} I've searched the seas from north to south, and I just can't find
               those pearls... I wonder if the pearls from his secret place are
               all gone...

[005]     :{S} Yepp told me the only thing he could teach me was how to sail and
               how to sing.

           {M} Yepp always sang such wonderful children's songs whenever he
               played with them.

[006]     :{S} There used to be a lot of pearl divers here in Yallam. I used to
               do some diving myself! Yup... They were all younger than me, but
               I still gave 'em a good run for the money.

           {M} Yepp was amazing. He could cut clean through the Sea of Time with
               utter ease. He read those waves like no other sailor on Weyard.
               He was a true man of the sea.

[007]     :{S} Yepp found this huge bed of pearls and sold them in another town.
               Then, he bought all kinds of things we needed in Yallam.

           {M} Yepp never told any of us where he found his bed of pearls,
               but... I suspect it's somewhere near the center of the Eastern
               Sea. He knew that area pretty well.

-----
* - Place where the children play:

[008]     :{S}   * - Refer to "Yepp's songs", below this social script section.

           {M} Yepps's songs are a lot of fun, because he made this game that
               goes along with them...

[009]     :{S} Yepp wrote all of his children's songs while he was out here
               in his own private space.

           {M} The story is that all these objects around here were brought here
               by Yepp long, long ago. If you look around, you'll see that
               everything was arranged in accordance with his songs...

[010]     :{S} Running around in circles here while singing one of Yepp's songs
               is pretty tough.

           {M} There's a lot of stuff to remember for each song. It's tough to
               play without making any mistakes.

[011]     :{S} There's a game that goes along with the song, but it's tough.
               I want to play something else.

           {M} I once heard that children's songs and stories have hidden
               meanings. I wonder if Yepp has hidden anything in his songs...





   [ Buildings ]
Innkeeper1:{S} It's a bit strange trying to run an inn in a city that never
               gets tourists, isn't it? Well, sometimes, the locals like to
               stay here. It's like a little vacation for them, I guess.

           {M} Yallam was always such a poor town. We had to work hard just
               to break even.

Innkeeper2:{S} Taopo Swamp has dried up, and now it's inaccessible.
               What's worse, with no water, we can no longer get any more
               delicious Yallam mountain fish.

           {M} There weren't a lot of mountain fish after the swamp dried up.
               We probably won't catch many.

-----

G. Healer :{S} Even out in these far-off shores, people need the services and
               hope I bring. I am grateful merely to have the chance to bring
               them some small relief.

           {M} Once, this was a thriving village. Now, I look around, and I
               only see abject poverty and despair.

-----

[012]     :{S} Yepp had three different songs he used to sing. Each song was
               about a different situation.

           {M} The songs are supposed to mean something, but none of the other
               kids knows what...

[013]     :{S} Do you like children's songs?

               --------------------------------------------
                    -(Yes)
               Hmmm... Well, I don't care for them so much, myself. I mean,
               the lyrics make no sense! ...And that stupid dance we have to do
               when we sing!!



                    -(No)
               Yeah, you're totally right. I just hate those songs. One of these
               days, I'll write one, and it'll be so much better than this!
               --------------------------------------------

           {M} I wonder why Yepp wanted the children to learn those songs he
               used to sing...

-----

[014]     :{S} It's been really dry the past few months. Even Taopo Swamp
               has dried up.

           {M} When Taopo Swamp dries up, we're in for some serious drought
               problems this year.

[015]     :{S} We're supposed to be right in the middle of the rainy season,
               but I don't see any rain...

           {M} I can't stand this drought! How long is the weather going to
               be like this?

-----

[016]     :{S} Sunshine has started complaining that he can't work lately.
               He blames it on the lack of rain.

           {M} What kind of person only wants to work when it's raining?
               I know Sunshine likes to enjoy his days off, but he needs to
               find a better excuse not to work.

[017]     :{S} Our blacksmith, Sunshine, makes the kinds of items you can't find
               anywhere else. You wouldn't know it to look at him... or talk
               to him... but he's an amazing worker...

           {M} Sunshine's a little eccentric. He disappears into Taopo Swamp
               for days at a time...

-----

[Item]    :{S} If you're looking for Taopo Swamp, head west around the northern
               mountain range. Sunshine sometimes goes up there by himself on
               long trips. It's a dangerous place.

           {M} What does Sunshine want in Taopo Swamp? There's nothing up there
               but bugs and some odd mountain fish.

-----

[Weapon]  :{S} If the blacksmith isn't willing to work, then how am I supposed
               to get fine weapons to sell?

           {M} If Sunshine set his mind to it, he could make a lot of money!
               What a waste of talent...

[Armor]   :{S} If you want plain old, boring armor, have a look around.
               If you're looking for some of Sunshine's armor, you'll have to
               come back later.

           {M} I shouldn't tell him how boring all this stuff is. I wish
               Sunshine would get back to work!

-----

Sunshine  :{S}   * - Without anything forgeable:

               Ah, so you're looking for a really unique item, eh?

               --------------------------------------------
                    -(Yes)
               Hey, if it ain't a'rainin', I ain't a'workin'! Come back when
               it's raining!



                    -(No)
               Listen up... It's a bright, sunshiny day, and I'm not working
               till it rains. But I'm not just slacking because it's a nice day.
               I only work in the rain!
               --------------------------------------------

           {M} If it's not raining, I can't get into Taopo Swamp. And if I can't
               get to Taopo, then I can't get the stuff I need to work, so
               there's no point!

S's Wife  :{S}   * - Before speaking to Sunshine:

               This? This is the blacksmith Sunshine's smithy, the best forge
               in Weyard! But Sunshine's not taking any jobs right now.


                 * - After speaking to Sunshine:

               Man, Sunshine would be rich if he worked more. What a waste...

           {M} Sunshine's a pretty stubborn guy. If he says he isn't going to
               work, then he's not gonna work.

S's Son   :{S} Dad's not doing any work right now, but I'm making some basic
               things for the villagers. Maybe someday, I'll be able to smith
               unique weapons, like my dad. That's why I keep practicing!

           {M} Everyone thinks Dad is stubborn, but he's not... He's a true
               artist, and so what if he gets a little temperamental from
               time to time?


#$#$#$#$#$#$#$#$#$#$
$#  Yepp's songs  #$
#$#$#$#$#$#$#$#$#$#$

[008]     : Do you want to hear one of the songs Yepp wrote?

-----------------------------------------------------------
     -(Yes)
[008]     : Here, let me show you!

* - He and the other children line up. They do as the song says.

    Twins  =  Two stones
    Swirl  =  Small stones
    Star   =  Tree stump with marking
    Moon   =  Tree stump with marking
    Sun    =  Sun-shaped arrangement of stones

[008]     : If you want to go to the stars,
            if you want to go to the stars.

            Go north past the twins,
            passing two swirls, run
            deasil twice 'round the trunk.

            Haste without waste, and head to
            the east, past three to the north.

            There, run 'round thrice and wait
            for the waves. When they stop,
            run north and go to the stars.

            If you race full of folly and
            take the wrong way, you'll
            find yourself a watery grave.

            Do you wanna hear the second children's song Yepp wrote?


    --(Yes)
[008]     : If you want to go to the moon,
            if you want to go to the moon.

            Face west from the stars and
            run straight past three swirls,
            then circle 'round twice.

            Haste without waste, and head to
            the south, then one swirl west.

            There, run 'round thrice and wait
            for the waves. When they stop,
            run south and go for the moon.

            If you race full of folly and
            take the wrong way, you'll
            find yourself a watery grave.

            OK, so, now do you want to hear the third children's song?


   ---(Yes)
[008]     : If you want to go to the sun,
            if you want to go to the sun.

            Face south from the moon
            and run straight through two
            swirls, then circle 'round twice.

            Haste without waste, and head to
            the west, then six to the north.

            There, run 'round thrice and wait
            for the waves. When they stop,
            run north and go for the sun.

            If you race full of folly and
            take the wrong way, you'll
            find yourself a watery grave.

            That's it. That's all the games we have for the songs...
            If you want to play some more, just give me a holler.


   ---(No)
[008]     : Well, that's just fine then. Give me a holler if you ever do.


    --(No)
[008]     : Well, that's just fine then. Give me a holler if you ever do.



     -(No)
[008]     : This is where all the kids in Yallam come to play...
            Nobody complains when we play around out here...
-----------------------------------------------------------


* - The songs act as instructions for navigating the Sea of Time.

    Stumps  =  Stones that stop currents when a ship sails around them
    Twins   =  Stones that mark what is initially the only viable entrance
    Swirl   =  Whirlpool
    Star    =  Stone shaped like a star
    Moon    =  Stone shaped like a crescent moon
    Sun     =  Poseidon


#$#$#$#$#$#$#$#
$#  Forging  #$
#$#$#$#$#$#$#$#

* - If you have something forgeable:

Sunshine  : You want me to make you a little something special?

            -----------------------------------------------
                 -(Yes)
            Well, look at that! You went to get some raw materials for me,
            didn't you? Right when I saw those materials, I had to work!
            Which item needs my special attention?



              * - If you select something that cannot be forged:

            No, that's no good. It just has no soul...



              * - If you select something processed:

            It's OK if I work with your <item>?

                --(Yes)
            Well, all right! I'm going to make you something great!

                --(No)
            Hm... That's not right...



              * - If you select something rusted:

            You want it to shine, don't you?

                --(Yes)
            A little elbow grease, and it'll make something great!

                --(No)
            Well, hm... I wonder which one...



              * - If you cancel the selection:

            Aren't you the ones mucking about earlier?





                 -(No)
            Hm... Maybe I made a mistake. It's hard to tell... If you want
            good work, I'll need good materials.
            -----------------------------------------------



* - After providing something forgeable:

Sunshine  :{S} I can't wait to see what I'm going to wind up making with this...
               It's funny, but I never know until I actually start working!

           {M} It's been a long time since I've been able to work. I'm so
               excited! What should I make?

S's Wife  :{S} It takes our Sunshine a long time to finish the items he works
               on. Maybe you could just... wait a little while before coming to
               pick it up...

           {M} What happened to Sunshine? He's so happy, and he just talks about
               work all the time!

S's Son   :{S} It's so weird, but something really inspired my father to work!
               He's beaming with joy!

           {M} Now that my dad's working again, I have to watch his every move
               to see what I can learn from him.



* - After leaving Yallam and returning:

Sunshine  :{S} My wife has the item I made you. She can give it to you.

           {M} If it's not raining, I can't get into Taopo Swamp. And if I can't
               get to Taopo, then I can't get the stuff I need to work, so
               there's no point!

S's Wife  :{S} Here's the item you wanted. Now, about the payment...
               We only take cash. Is that all right with you?

               --------------------------------------------
                    -(Yes)
               OK, here you go!



                    -(No)
               Hey, we're not a charity! If you can't pay for it, you don't
               get it!
               --------------------------------------------

           {M} Sunshine's a pretty stubborn guy. If he says he isn't going to
               work, then he's not gonna work.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'33] ---     [Great Eastern Sea]     --- [02'33] #$#
#$#$#                      Isles                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                 _======================_
                 \_  E Tundaria Islet  _/
                  ======================

#$#$#$#$#$#$#
$#  Event  #$
#$#$#$#$#$#$#

* - Two penguins are present, one on each side of a river.

Pengus    :{S} Pen pen!

           {M} My darling Pengulina hurt her leg on the far shore and can't
               swim back. Somebody, please... Help her!

* - A log can be rolled into the water. On the other shore:

Pengulina :{S} Pen pen pehnnn!

           {M} Ohh... My leg... I can't get back to my dearest Pengus...

* - After helping her across the log, using Mind Read:

Pengus    : Thank you so much for saving my sweet Pengulina. Allow me to
            give you this in return for your help.

<game>    : Felix got a Pretty Stone.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Pengus    :{S} Pen pen.

           {M} I'm so happy my lovely little Pengulina is all right.

Pengulina :{S} Pen pen.

           {M} I'm so glad to be back on this side again, with my precious
               Pengus.

G. Healer :{S} I am here to tend to any travelers who come to this place.

           {M} May these travelers' journey end in peace and safety...

Man       :{S} My mom says there's this strange tower on the northern cape
               of Tundaria.

           {M} Who in Weyard would have built a tower in the middle of that
               frozen nowhere?

Old Man   :{S} Used to be, you could sail to the other side of Gondowan by
               skirting the coast of Tundaria. Now, the whole area's got these
               rocky spires... You just can't work a boat around 'em.

           {M} Tundaria is the southernmost continent in Weyard. I hear that
               if you head eat far enough... There's an incredibly waterfall
               at the edge of the Eastern Sea. It sounds like hokum to me.

Old Woman :{S} You must be cold, dressed in those thin clothes... Come warm
               yourselves by the fire...

           {M} Around here, it doesn't matter what season it is... It's always
               the cold season. I can't even go outside without first covering
               myself in fur.


___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                 _=====================_
                 \_  SE Angara Islet  _/
                  =====================

#$#$#$#$#$#$#
$#  Event  #$
#$#$#$#$#$#$#

* - Without Pretty Stone:

Bird      :{S} Chirp chirp!

           {M} I love feeling fancy! I want a really fancy accessory to make me
               feel extra fancy!



* - With Pretty Stone:

Bird      : Oh my! That stone you have! It's divine! Simply divine!
            I must have it! MUST! I'll give you my very fancy neckerchief
            for that fancy stone of yours!

<game>    : Felix traded his stone for the very fancy neckerchief.
            Felix got a Red Cloth.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Bird      :{S} Chirp chirp!

           {M} What do you think? Don't I look fancy! I sure feel fancy!
               And that's all that matters! But I think this looks fabulous
               on me! I love fancy accessories!



* - When initially speaking to Man 1:

Man 1     : We like this island. A lot... That's why we're here... Because we
            like it. We aren't looking for Treasure Isle! Nope!

Man 2     : What are you saying? Idiot!

            Don't listen to that guy. He didn't say anything about Treasure
            Isle. Nothing at all.

Man 1     : Look, we're busy... We can't talk now... Catch us some other time...



* - Afterwards:

Man 1     :{S} Look, we're busy... We can't talk now... Catch us some other
               time...

           {M} If we're supposed to be partners in this crazy treasure hunt,
               why am I the one doing all the cooking?

Man 2     :{S} The Eastern Sea is huge, even if you don't add the Sea of Time,
               which I guess you've got to do. You don't look like much of a
               sailor. You're not a treasure hunter, are you? Because you won't
               find any in the waters around here, let me tell you!

           {M} Sure, there are legends about how there's treasure hidden north
               of the Sea of Time. But have WE found any? I just hope it's not
               on the seafloor! What would we do then?


___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                  _====================_
                  \_  N Osenia Islet  _/
                   ====================

#$#$#$#$#$#$#
$#  Event  #$
#$#$#$#$#$#$#

* - Without Red Cloth:

Cow       :{S} Moo! Moo!

           {M} I've been feeling so low lately... I long to feel the utter joy
               of... something. I just don't know what.



* - With Red Cloth:

Cow       : Oh! That red neckerchief is quite nice indeed. That would lift my
            spirits. This really brightens my moooood!

<game>    : Felix tied the neckerchief to the tree.

Cow       : Are you giving that lovely thing to moooooi?

            --------------------------------------------
                 -(Yes)
            That's so kind of you! I should repay you! Have some milk!
              * - <game>: Felix got some Milk.



                 -(No)
            I'm sorry to hear that. Come see me if you don't want it anymore.
            --------------------------------------------


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Cow       :{S} Moo! Moo!

           {M} Yup. A nice, red neckerchief will never steer you wrong!

Young Man :{S} I just want to know what's on the other side of that sea of
               fog... No one has ever crossed through it, but one day, I just
               know I'll do it!

           {M} Dad and Grandpa haven't been able to cross the Sea of Time.
               They're so old now... I will be the one to make their dreams
               come true.

Man       :{S} The Sea of Time... A massive bank of fog that lies over the
               sea... All sailors fear it, and rightly so! I don't know if I'll
               ever make it through, but I'm certain my son will do it someday.

           {M} I remember once, an entire fleet of ships entered the Sea of
               Time. They vanished into the mists. Every last one of the vessels
               was destroyed by the currents.

Woman     :{S} Sailors tell of terrible currents and vortexes that can tear a
               boat to shreds in the Sea of Time.

           {M} Once, long ago, my husband entered the Sea of Time without being
               destroyed. The whirlpools spun him around and he got so dizzy
               he couldn't stand. I wonder if he remembers.

Old Man   :{S} When you enter the sea of fog... enter the currents from the
               direction of the red rocks. Then, your ship won't be destroyed.
               But that's all I know. And it might not even be right!

           {M} I didn't really discover the secret of the red rocks... It was
               Yepp, the great explorer from Yallam, who t old me. I should
               fess up.

Old Woman :{S} Ours is a sad lineage... Three generations of sons have sworn
               their lives to trying to pass through the sea of fog.

           {M} And just what will happen once they get through the sea of fog?
               I wish they would just give up.


___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                 _======================_
                 \_  West Indra Islet  _/
                  ======================

#$#$#$#$#$#$#
$#  Event  #$
#$#$#$#$#$#$#

* - Without Milk:

Dog       :{S} Arff! Arff!

           {M} The water here is so salty! I wish someone would bring me
               something tasty to drink.



* - With Milk:

Dog       : Sniff! Sniff! I smell fresh milk! Hah hah hah! Are you going to
            give me that milk? Are you? Huh? Huh!? I'll trade you this for it!
            I caught it myself!

<game>    : Felix traded his milk for the dog's turtle!
            Felix got a Li'l Turtle.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Dog       :{S} Arff! Arff!

           {M} I don't like to waste. I'll just take little tiny laps.

Man       :{S} Ever since the tidal wave moved Indra, we haven't been able to go
               to Gondowan's western shores.

           {M} The waterways north of Tundaria would have been the perfect place
               to teach my sons to sail...

Woman     :{S} Did you know Indra moved? It was quite a shock to all of us
               here... We haven't been able to use the waterways to the south
               ever since.

           {M} I'm so grateful our little island wasn't damaged in the tidal
               wave... It was a miracle.

Child 1   :{S} My pop's the best sailor in all the Eastern Sea! That's why
               he can go anywhere, even in that tiny boat of his!

           {M} I can't wait until Dad teaches me how to sail...

Child 2   :{S} You're lucky, mister. You get to ride your boat out on the open
               sea all you want... My dad'll be done with his boat soon, and
               together, we'll be able to sail anywhere we want...

           {M} I can't wait until the day I can sail far away with Dad and
               Kirt...


___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                _=======================_
                \_  Sea of Time Islet  _/
                 =======================

#$#$#$#$#$#$#
$#  Event  #$
#$#$#$#$#$#$#

* - Without Li'l Turtle:

Turtle    :{S} ...

           {M} I'm so very... very lonely. I could sure use a friend.



* - With Li'l Turtle:

Turtle    : I'm so very sad and lonely. I wish I had a friend to call my own...
            Hey! You've got an itty-bitty turtle tot, don't you? Why don't you
            set that li'l guy free with me?

-----------------------------------------------------------
     -(Yes)
Turtle    : At long last, I have a friend! Lonesome George I am no more!
            I'm so happy! I don't have much to offer you in return, but I can
            show you... my secret spot. Hop on my back!

* - Felix does so.

Turtle    : And we're off!

* - He takes him to an even smaller islet to the south, surrounded by rocks
    (which is why you can't just sail there). The Islet Cave can be found here.

Turtle    : Well, here we are. When you want to go back to the island,
            just let me know.

* - Returning:

Turtle    :{S} Yup!

           {M} You all set to go back to the island?

               --------------------------------------------
                    -(Yes)
               Then back we go!
                 * - They return:
               Here we are! If you want to go to my secret spot again,
               just let me know.



                    -(No)
               Take your time! I don't like to rush...
               --------------------------------------------



     -(No)
Turtle    : No? Oh... Then lonely I shall stay. But if you change your mind,
            you know where to find me.

* - Speaking to the turtle again:

Turtle    : Oh! You're really going to let me take care of your li'l turtle?

* - Both options result in the same outcome as before.
-----------------------------------------------------------


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Turtle    :{S} Yup!

           {M} Want to go to my secret spot again?

               --------------------------------------------
                    -(Yes)
                 * - Same as saying yes before.



                    -(No)
               Anytime you want me to take you to my secret spot, just say
               the word.
               --------------------------------------------

Old Man 1 :{S} You used to be able to dive into the ocean and find all sorts of
               treasure in the reefs. I liked to think all that stuff was a
               gift from the deep... A gift for me!

           {M} I remember how we used to dredge up treasure by looking for
               shadows in the reefs...

Old Man 2 :{S} The temperature of the ocean has been rising. The waters are
               hottest at the Sea of Time. I sure hope Poseidon hasn't surfaced
               again! He was once a king, but now, he's a monster!

           {M} Long ago, Poseidon ruled over all the oceans as the one true king
               of the sea. Legends say the only way to defeat him is to stab him
               with a trident...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'34] ---     [Great Western Sea]     --- [02'34] #$#
#$#$#                      Isles                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

By using Grind on a stone in Gondowan Cliffs, one can pass into the Western Sea.


___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                 _=====================_
                 \_  SW Atteka Islet  _/
                  =====================

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Man 1     :{S} The sea west of here spills over a massive waterfall.
               You'll really start to appreciate the grandeur of nature
               if you see that, I can tell you.

           {M} My buddy thinks I'm nuts to risk my life for a look at the falls.
               Actually, I just want to get my hands on some treasure I saw
               on the way there.

Man 2     :{S} There's nothing to the west of here. AND it's really dangerous.
               You shouldn't go that way.

           {M} The currents are so strong near the falls that any boat caught
               in it is doomed.


___________________________________________________________
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
===========================================================
                   _=================_
                   \_  Kalt Island  _/
                    =================

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Old Man   :{S} If you want to cross the glaciers of the Northern Sea, you'll
               need magma balls... They come from volcanoes, but the best place
               to get them is Magma Rock, to the south.

           {M} The people of Logo have a legendary weapon called a cannon that
               fires magma balls. That's supposed to be how they crossed the
               frozen wastes, but it sounds like a tall tale.

Old Woman :{S} A long time ago, we used to trade with a village named Prox to
               the north of us. But the sea freezes in winter, and over time,
               it just became impossible to get there.

           {M} The Northern Sea is thick with icebergs in the winter. They can
               sink a boat in an instant!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'35] ---         [Hesperia]          --- [02'35] #$#
#$#$#               Hesperia Settlement               #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Man       :{S} You must be very brave to come all the way here by boat.

           {M} For a continent as desolate as this one, there sure have been
               a lot of boats here lately.

Woman     :{S} There's a place called Shaman Village in the middle of the
               continent. Supposedly, one of the rivers leads to it.
               I have no idea which one, though.

           {M} I think there's a cave at the end of the river. That's the way
               into Shaman Village. I wonder if I should tell them what the
               legends say... Nah, they look like a smart group.

Boy       :{S} The people of Shaman Village are very wary of strangers.
               Be careful if you ever meet them.

           {M} Long ago, Shaman was ravaged by outsiders. It was terrible.
               From that day on, they simply have not trusted strangers
               in their village.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'36] ---         [Hesperia]          --- [02'36] #$#
#$#$#                 Shaman Village                  #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

* - No one here will speak to Felix's group.


   [ Outside ]
[001]     :{M} Hm. Outsiders... I don't like the looks of them. I'm just going
               to wait until they leave.

[002]     :{M} Ugh... Foreigners. I'm not going to waste my time even TALKING
               to them!

[003]     :{M} Our ancestors learned that we can trust no one but the people of
               Contigo, our longtime friends!

[004]     :{M} Until the chief says otherwise, nobody will talk to these
               outsiders. It's the law.

[005]     :{M} Who invited these foreigners into our town?

[006]     :{M} Shut your doors tight when outsiders are in sight. If we want to
               protect ourselves, our culture, we have to keep outsiders OUT.

[007]     :{M} These foreigners look trustworthy, but I know better... They may
               seem nice, but all outsiders are wicked!

-----

[008]     :{M} Our ancestors learned a harsh lesson... Shamans never lie, but
               outsiders are never honest.

* - There's a sign on a barricade:

Sign      :{O} Trial Road
               None may enter without permission from Moapa.

-----

* - The seer has retreated into his tepee.





   [ Buildings ]
Innkeeper1:{M} I don't much like strangers, but if they're willing to pay,
               I'm willing to let them stay.

                 * - When you try to speak to him, he holds up a card that says:
                     "Put 80 coins on the counter, and you can stay."

Innkeeper2:{M} Moapa ordered us to let them stay. I don't know why, though.
               It's not like we lock the doors.

-----

* - Two tepees in the front of town are closed, as is a building to the east.

-----

G. Healer :{S} Nothing personal, but nobody in town will talk to you.
               It may seem weird, but it's a law among the Shaman tribe.
           {M} They'll need to find Moapa if they want to talk to one of
               the locals.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Moapa's residence  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - Upon approaching the front door, Moapa and two men walk out of the building.

Moapa     : This is my house. If you're looking for Moapa, here I am.
            Back up. Give me some room.

* - Felix's group does so (they actually were quite close).

Moapa     : Who has we here? Strangers in Shaman Village? What is your purpose
            in coming here?

Man 2     : Shaman Village does not appreciate intruders.

Man 1     : You're not welcome here, outlander. Leave now, and never come back.

Moapa     : If there's something you want to say, hurry up and say it.
            I'll listen, but nor for long!



* - When speaking to them, the menu appears, thus letting you present an item.

Moapa     :{S} What's wrong? Nothing to say? Then what are you standing around
               for? Get out of town!

                 * - Upon presenting any item other than the Shaman's Rod:

               If you're offering charity, I won't have it... Or do you want to
               show me something?

           {M} They don't look like they've come from Contigo... There's no
               reason for us to be nice.

Man 1     :{S} If there's something you want to say, say it to Moapa, not to us.
               We don't want to hear it.

                 * - Upon presenting an item:

               Yes, yes. That's very nice. Did you want to sell it? Because I
               don't have any money.

           {M} If it hadn't been for Moapa, I'd have been glad to fling these
               outlanders into the cold.

Man 2     :{S} If you anger Moapa, you'll be in for a little taste of his
               awesome and terrible power.

                 * - Upon presenting an item:

               What makes you think I would be interested in this? Show it to
               Moapa if you must, but I don't need it.

           {M} Maybe they're looking for treasure. They ought to be looking in
               Contigo, not here. The temple near Contigo is filled with
               treasure beyond belief.



* - Upon presenting the Shaman's Rod to Moapa:

Moapa     : That's the Shaman's Rod!

Man 2     : We thought it was lost forever... It once belonged to the great
            Hoabna.

Man 1     : Hoabna's staff was a gift from his great friend in Contigo, Yegelos.
            When Yegelos gave it to him, Hoabna accepted a great
            responsibility...

Moapa     : We vowed to care for the sacred treasure of Contigo, the Hover
            Jade... When the Shaman's Rod returns to us, we are charged to
            give the bearer the Hover Jade.

            Have you outlanders come to claim the Hover Jade?

Kraden    : I suppose we have, yes.

* - He examines them.

Moapa     : That's a shame. We'll never give the Hover Jade to you!

Kraden    : But... we brought you the Shaman's Rod... What's stopping you from
            giving us the Jade?

Moapa     : Hoabna handed the Hover Jade down from generation to generation
            for our care. We are to return it to the descendants of Yegelos.
            And you are clearly not from Contigo.

Sheba     : That's preposterous! We returned your rod! We've come so far
            already!

Jenna     : What difference does it make if we're from Contigo or not!?

Piers     : Make no mistake about it. We are the intended recipients of the
            stone of Yegelos.

Kraden    : Is there some way we can get our hands on the Hover Jade?

Moapa     : No. You ask the impossible.

Man 2     : What about... the test? Would that be a bad idea, Moapa?

* - Moapa appears confused.

Man 2     : You know, Trial Road? Only Yegelos could walk that path.

* - Still, he seems puzzled.

Man 1     : The way of the vanishing sand!

* - Moapa smiles.

Moapa     : Yes, if you outlanders intend to claim the Hover Jade, you must
            fetch it and bring it here! If you people have the courage,
            follow me!

* - He and the two men head off to Trial Road.

Sheba     : If you'd told us there was a test to begin with, we'd have been out
            of your hair by now.

Jenna     : What kind of test is this?

Kraden    : I understand that you're a little concerned, but unless you try it,
            you'll never know! Give it your best, Felix!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Buildings ]
* - Moapa's residence:

M's Wife  :{M} Moapa left the door open, and strangers got in... Ah, but they're
               gone already...

M's Son   :{M} The outlanders look like warriors, but they're nothing next to
               my father. He's the leader of Shaman Village, but he's also
               just so trong! He never loses!

M's Dau   :{M} Those are the first foreigners I've ever seen... They don't look
               so different from us.


#$#$#$#$#$#$#$#$#$
$#  Trial Road  #$
#$#$#$#$#$#$#$#$#$

* - A massive block of sand has piled up between two cliffs.
    A Wind Stone (see: Air's Rock) is present.

Moapa     :{S} To inherit the stone of Yegelos, you must cause this sand to
               disappear. If you can manage that feat, then the blood of Contigo
               runs through your veins.

           {M} I know the truth. These outlanders stole the rod from Contigo.
               No matter. Their misdeeds will be revealed to all when they
               fail the Trial Road.

Man 1     :{S} When Yegelos and Hoabna waged their might battles here, the sand
               suddenly vanished.

           {M} They stand no chance of making the sand vanish. They will give up
               and go home.

Man 2     :{S} Just ahead lies Trial Road, where Hoabna and Yegeloes fought
               their greatest battles. Only superior ones such as they could
               have followed the road to its end.

           {M} If they lack the power of Contigo or the power of Shaman Village,
               they will fail.





* - Upon choosing to use Whirlwind on the Wind Stone:

Jenna     : You can do it, Sheba!

Sheba     : Leave it to me, Jenna. This will be a breeze.

* - The stone magnifies her power, summoning an enormous cyclone that removes
    the sand in mere moments.

Moapa     : I don't believe it. They did it! The sand vanished!

Man 2     : The legends... They were all true!

Man 1     : She's the one! She must have come from Contigo!

Moapa     : Her? She's the one that did it? But she's... just a girl!

Sheba     : Well, you wanted the sand to vanish, so...

Piers     : Can we have the Hover Jade now?

Moapa     : Nope, you still can't have it.

Jenna     : What? Why not?

Moapa     : This was just a test to see if you earned the right to take the test
            to earn the stone.

Kraden    : So, there's more that they have to do before you'll give them
            the stone?

Moapa     : You will have to reach the end of Trial Road.

Man 2     : The girls, too? Surely you can't make them...

Man 1     : I thought that only the chosen hero could travel the road...

Sheba     : What, are you saying I can't be the chosen hero?

Moapa     : The heroes have always been men, ever since the time of Hoabna.
            It is the way.

Sheba     : I don't like your attitude, mister! I can be ever bit as heroic
            as some guy!

Man 2     : That may be true, but you must respect our customs.

Man 1     : It's the same in Contigo, you know. If you don't like it,
            take it up with Yegelos.

* - Moapa and the two men start to leave.

Kraden    : Hold it, hold it... Moapa, what were you just saying about Trial
            Road? If we reach the end of Trial Road, won't our names join
            the ranks of your heroes?

Jenna     : Kraden's right... It shouldn't matter if a girl does it...
            All that matters is that we finish!

Piers     : If you give us the chance, we will prove it to you.

Sheba     : Unless you're afraid that a girl like me might become your town's
            newest hero.

Man 2     : Have they earned the right? Shall we let them onto Trial Road?

Man 1     : I don't like the way these outsiders were talking to me.

Man 2     : I think they need to learn exactly what it takes to be a hero
            around here!

Man 1     : Yeah, if these guys are so stubborn, let's give them a shot!
            They'll probably give up!

Jenna     : You said it yourselves. We're too stubborn to quit.

Sheba     : Yeah. If you want us "outlanders" to leave, you'd better give us
            a chance to walk Trial Road!

* - Moapa looks at the two men, who both nod.

Moapa     : Trial Road is a difficult one... When you reach the top, a terrible
            battle awaits you. It's difficult enough for me. I expect you will
            find it quite impossible. Still interested?

-----------------------------------------------------------
     -(Yes)
Moapa     : You seem confident, but it is your ignorance speaking.



     -(No)
Moapa     : So... You are not as sure of yourselves as you first seemed.
            But I will permit this. Follow me, and I shall explain.
-----------------------------------------------------------





* - Moapa and the two men head down the path past where the sand had been.
    Felix's group follows them. They come to the location of the trial cave
    and its two entrances.

Moapa     : Listen carefully to me. This cave provides you with an opportunity
            to practice your skills. Legends say that Yegelos and Hoabna once
            fought here. These columns commemorate this. They raced one another
            to the summit... And there, they fought with all their might on the
            peak of the mountain. In honor of their great battle, the leaders of
            Shaman created this trial.

            The rules are simple. The room is filled with traps and snares.
            Use the power of Contigo to avoid them. This road has four doors.
            To open them, you will need to place items in these chests.

Felix     : Why?

Moapa     : The door is triggered only when the treasure chests are filled to
            the correct weight. Try putting heavier items, like weapons and
            tools, into the chests, or the doors won't open. If you reach the
            door after your opponents do, you will be at a serious disadvantage.
            You see, it will take twice the weight to open the doors. Stand on
            the switch, and the number of chests you need to fill will open.
            If you are last to each of the four doors, you will lose eight items
            to the chests!

            If Trial Road proves too much for you, press this button. This ends
            the battle, though. A true hero would not surrender so easily.
            In order to reach the battle at the summit, you cannot fail on
            Trial Road.

            Do you understand?

-----------------------------------------------------------
     -(Yes)
Moapa     : Then you understand the treacherous path of Trial Road.
            Will you continue?



    --(Yes)
Moapa     : You have heard the rules, and you wish to continue.
            You have been warned. Choose the road of your liking.
            It matters not to us.



    --(No)
Moapa     : You have chosen wisely, and for your wisdom, you must leave
            Shaman Village.

* - If you return:

Moapa     : Do you want to challenge me on Trial Road?

   ---(Yes)
Moapa     : Do you need to hear Moapa's explanation again?

  ----(Yes)
Moapa     : Thick-witted outsiders.

* - He repeats everything from "The rules are simple".

  ----(No)
Moapa     : Choose the road of your liking. It matters not to us.

   ---(No)
Moapa     : You have chosen wisely, and for your wisdom, you must leave
            Shaman Village.





     -(No)
Moapa     : Would you like me to explain it to you again?

    --(Yes)
Moapa     : Do all outlanders share your thickwittedness?

* - He repeats everything from "The rules are simple".

    --(No)
Moapa     : Then you understand the treacherous path of Trial Road.
            Will you continue?

* - This is the same as when it results from the initial "Yes."
-----------------------------------------------------------





* - After accepting the trial, but before choosing a path:

Moapa     :{S} Choose the road of your liking. It matters not to us.

           {M} I cannot lose. I will not lose. It is my responsibility as head
               of the Shaman tribe.

Man 1     :{S} Do you need to hear Moapa's explanation again?

               --------------------------------------------
                    -(Yes)
               Moapa:  Thick-witted outsiders.

                 * - Moapa repeats everything from "The rules are simple".



                    -(No)
               As long as you remain in our village, my people are not free to
               do as they will. If you are not going to take the challenge of
               Trial Road, you must leave Shaman Village.
               --------------------------------------------

           {M} You don't seem like bad people, for outlanders, but we cannot
               give you the jade. Only the hero with the bloof of Yegelos,
               the hero of Contigo, can claim the gem.

Man 2     :{S} Do you need to hear Moapa's explanation again?

               --------------------------------------------
                    -(Yes)
               Moapa:  Thick-witted outsiders.

                 * - Moapa repeats everything from "The rules are simple."



                    -(No)
               Then you must leave Shaman Village and forget about the Hover
               Jade.
               --------------------------------------------

           {M} You're doomed. Moapa is the greatest warrior in all of Hesperia.





* - If you try to leave the area:

Moapa     : Have you decided to give up this foolishness once and for all?

-----------------------------------------------------------
     -(Yes)
Moapa     : You have chosen wisely, and for your wisdom, you must leave
            Shaman Village.

* - Refer to "If you return:" in the choice sequence following the explanation.



     -(No)
Moapa     : Choose the road of your liking. It matters not to us.
-----------------------------------------------------------





* - Upon selecting a path:

Moapa     : If you have chosen, then we shall take the other path.
            On the count of three, the challenge begins!





* - If you forfeit, everyone goes back outside:

Moapa     : It would be wise of you to quit. Even if you reach the top,
            you cannot beat me. You should do well to leave Shaman Village
            at once.

* - Refer to "If you return:" in the choice sequence following the explanation.





* - Upon reaching the summit, if you came before the others:

Moapa     : You were quite swift! You may prove a challenge yet! However,
            just because you're fast doesn't mean you're strong. Challenge
            or no, I will win. Let the battle begin!

* - Upon reaching the summit, if you came after the others:

Moapa     : You may have been slow, but you made it through Trial Road
            to the mountain's peak! Well then... The time is nigh for us
            to decide who is stronger! Let the battle begin!



* - Regardless, after defeating Moapa and the two men:

Moapa     : All right, all right. You've proven your strength, and you are
            heroes indeed. As we promised, you will receive the Hover Jade,
            and we will take the Shaman's Rod.

<game>    : Felix got the Hover Jade.

Moapa     : After many years, the vow that Hoabna made to Yegelos has at last
            been fulfilled!

            I'm tired now. I'll be back in the Shaman Village resting.

* - Kraden looks at the others in Felix's group.

Kraden    : I'm sure you must be exhausted as well. Let's go back to the village
            and rest.

* - They automatically go to the inn and stay the night.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} So, you rose to the challenge of Triad Road? Moapa was quite
               impressed with you!

           {M} Moapa is quite honorable to sing their praises. This is what
               makes him a leader.

[002]     :{S} Heroes cannot be evil. And now, we have learned that heroes
               can be foreigners, too.

           {M} We are too cautious around strangers. The world should not be
               such an unfriendly place.

[003]     :{S} Everyone in town is talking about how you have fulfilled Hoabna's
               promise.

           {M} I hope that we remain close friends with the Contigo after this.

[004]     :{S} The people of Shaman Village are normally quiet, valiant, and
               noble. You defeated Moapa, and we must respect the bravery you
               demonstrated in fighting him.

           {M} It's tough to imagine this bunch beating Moapa, but I'm not
               thinking about it.

[005]     :{S} You defeated Moapa, and that is ample proof of your skill as
               warriors. I think you will find that the people of Shaman Village
               treat you quite differently now.

           {M} Someday, a child in Shaman will grow to be stronger even than
               Moapa. Then, the Shaman tribe will rise up again and rclaim
               what it once lost to Contigo.

[006]     :{S} Some people among the Shaman tribe possess a special power...
               The story goes that those with this power are the chosen few.

           {M} People living on the outskirts of Shaman Village have different
               powers from us. Why would that be?

[007]     :{S} After your battle, did you check on the other side of the
               mountain?

               --------------------------------------------
                    -(Yes)
               Did you see the spring? There's supposed to be a spring that
               only Hoabna could find.



                    -(No)
               If you have the same powers Hoabna had, you might be able to
               get there... Nobody with the powers of the Shaman tribe alone
               can reach the hidden spring.
               --------------------------------------------

           {M} If I had the power to break down walls of sand, I'd climb to the
               other side of the mountain.

-----

[008]     :{S} Your battle with Moapa was just like the legendary battle between
               Hoabna and Yegelos! I would love to have watched, to see a new
               legend in the making...

           {M} I never thought I'd live to see the day Hoabna's promise was
               fulfilled. Of course, I never thought anyone with Contigo blood
               could defeat a Shaman hero.

-----

* - As you pass by:

Seer      : Hoolabaloo!

* - After that:

Seer      :{S} So, you'd like to hear your fortune, would you?

               --------------------------------------------
                    -(Yes)
               Well, you caught me in a good mood... I'll do it! Hoolabaloo!
               Ballabahoo! Hoolabaloola! I can see it clearly... Your life is
               thick with danger... Ooo... Wow, that was a strong one...
               Listen, don't go south. Bad stuff down there. Wow. Oh, it's
               terrible! Awful beyond words! No more, no more!

                 * - Afterwards:

               You should absolutely not go south. Do you hear me? I'm serious
               about this...



                 * - After a certain major event in Atteka (to the south),
                     his prediction changes.

               Wallamafoo! Ballabahoo! Whazupwichoo! I can see it clearly...
               Your life is thick with danger... Ooo... Wow, that was a strong
               one... North by northeast is... bad. Bad stuff up there. Wow.
               Oh, it's terrible! Awful beyond words! No more, no more!

                 * - Afterwards:

               Listen, I want you to promise me you'll NEVER go north by
               northeast. You got that?



                    -(No)
               That's probably good. The things I see are not for everyone
               to hear.
               --------------------------------------------

           {M} That's weird... Everything is cloudy... The ether is grey and
               full of mists... The world is undergoing some sort of change,
               it seems.





   [ Buildings ]
Innkeeper1:{S} You've traveled to lots of different lands, haven't you?

               --------------------------------------------
                    -(Yes)
               That explains it... The only reason you won is because of your
               travels... Your strange, exotic weapons are what won the day,
               not your skill.



                    -(No)
               I could have sworn that fancy boat was yours... If you can afford
               such a nice boat, you can probably afford nice weapons, too.
               --------------------------------------------

           {M} Moapa has been miserable since his defeat. If only I could have
               taken his place up there.

Innkeeper2:{S} We're very fond of Moapa here. He's a great leader. If anyone
               in town says something mean to you, please forgive them.

           {M} It drives me nuts how worked up everyone gets about Moapa
               around here.

Chef      :{S} Around here, people like a nice hot steak and some potatoes and
               beans... You foreigners might be used to strange, exotic food,
               but we like our meals simple.

           {M} Those fancy foreign chefs use all sorts of spices to hide the
               flavor of their food. As far as I'm  concerned, there are only
               two spices: salt and pepper.

[009]     :{S} I've been locked up inside all day! I'm so glad to get outside
               and stretch!

           {M} All of the older people in town are really upset that Moapa
               lost... It doesn't matter to us kids. I think they're too hung up
               on tradition.

[010]     :{S} Ah... I've been inside for so long... I think I'll have a little
               picnic! But what should I eat...

           {M} I'm starving! I can't wait until dinner! I love my meat and
               potatoes! And BEANS!!! It must be the spices the chef uses...
               Lots of salt, and lots of pepper!

-----

[Item]    :{S} Everyone is depressed that Moapa lost his big fight. They should
               be glad the hero came!

           {M} My husband is getting neurotic, worrying about whether his
               weapons caused the loss.

[011]     :{S} I was stunned to hear that Moapa lost his battle... His weapons
               all came from my own warehouse, so I feel a little responsible.

           {M} Although it's not right to blame his loss on the weapons he used.
               I couldn't afford it if that rumor started going around.

-----

[012]     :{S} The battles between Shaman and Contigo were terrible, and few
               warriors ever survived. Eventually, our towns chose Hoabna and
               Yegelos to fight as our champions.

           {M} Grandma and Grandpa have been in a terrible mood since they
               heard Moapa lost. They're probably tired of being asked about
               the ancient war between Atteka and Hesperia.

[013]     :{S} I've always wondered why the final battle between Hoabna and
               Yegelos took place here. I think Yegelos was really brave for
               traveling here all the way from Contigo.

           {M} Everyone always comes to ask Grandma and Grandpa about the
               old battles of legend. It's all anyone ever talks to them about
               anymore. I'll bet they're tired of it.

[014]     :{S} For years, the people of Hesperia fought against the people of
               Atteka... Our own Shaman Village was caught up in this war,
               as were the people of Contigo.

           {M} I had thought that, after Yegelos, Contigo remained without a
               new hero. Now, suddenly, a hero shows up who is mightier even
               than Moapa. It's beyond belief!

[015]     :{S} In those dark times, Contigo and Shaman fought repeatedly
               to protect our lands. We fought to no avail, until we decided
               to let Hoabna and Yegelos fight for the outcome.

           {M} The stories always said that the heroes of Contigo were inferior
               to our own. Now, I'm not so sure... It sounded like a fair match,
               and yet Shaman's hero lost.

-----

[016]     :{S} I can finally open the door and air the place out. I can't
               believe Moapa was on the mountain fighting while I was stuck
               in here.

           {M} I thought it was quiet out here. I've been locked inside all day,
               so I couldn't check... It was all because they were fighting
               Moapa up on Trial Road...

[017]     :{S} If I'd known that there was going to be a challenge on Trial
               Road... I wouldn't have locked up. I'd have been right up there,
               watching the fight!

           {M} Nobody got to watch the challenge at Trial Road. It was just
               too far from town. What a stupid law, that makes us hide away
               and miss all the battles!

-----

G. Healer :{S} You beat Moapa? Incredible! ...Not that I ever doubted you!

           {M} The older folks of Shaman are quite upset that Moapa was beaten.
               I'm afraid this might lead to renewed fighting between Shaman
               and Contigo.

[018]     :{S} Don't be too pleased with yourself for beating Moapa. One of
               these days, we'll come storming into Contigo, and we'll show you
               what's what!

           {M} Moapa must have been hungry after climbing the mountain...
               That's the only way those lousy Contigo nobodies could have
               beaten him.

[019]     :{S} Oh, please... Let a true warrior be born in Shaman. Let us forget
               this disgrace!

           {M} I can't forgive the fact that Contigo's heroes beat our leader,
               Moapa... I hope a new hero is born in Shaman, one who can crush
               those Contigo barbarians.

-----
* - Outside of Moapa's residence:

Man 1     :{S} I don't think the other villagers will ever forgive us for losing
               to you on Trial Road. If they had any idea how strong you are,
               they wouldn't be complaining.

           {M} That wasn't a fair fight... I was all worn out from the climb...
               How could I fight? How did Hoabna manage to fight after climbing
               a mountain like that!?

Man 2     :{S} Your attacks showed skill and speed, but if we meet in battle
               again, I won't lose.

           {M} Just climbing to the top of Trial Road is excruciating.
               It must have been hard for Yegelos and Hoabna, too.


* - Inside:

Moapa     :{S} You have defeated me, and yet I still don't know your names...
               Would you tell me?

               --------------------------------------------
                    -(Yes)
               Felix, Jenna, Sheba, and Piers. I shall remember those names.
               We do not forget the names of heroes who can defeat me in
               fair combat.



                    -(No)
               A warrior who does not share his name is a humble warrior indeed.
               --------------------------------------------


                 * - After he learns their names:

               Felix, the hero of Contigo! I shall never forget you, the
               only one that defeated me!

           {M} If a warrior beats you, you must learn his name... Not many
               people have beaten me, and they deserve my respect.


                 * - After he learns their names:

               Felix, Jenna, Sheba, and Piers... I won't forget those names...
               Someday, their names will be engraved on the columns leading to
               Trial Road.

M's Wife  :{S} Moapa said that he doesn't even know the names of the heroes
               who beat him... He feels bad for not having asked. Maybe you
               should go tell him your names.

           {M} I would feel bad not knowing the name of a warrior who defeated
               me, I guess...

M's Son   :{S} In a formal battle, it is both customary and honorable to give
               your name. It's not too late for you... Please go tell my father
               your names.

           {M} What a shame... My own father, losing to some ignorant foreigner
               with bad manners.

M's Dau   :{S} Why does it matter if you know the name of someone who beat you
               or not?

           {M} It's so old-fashioned to have to give your name to an opponent
               before a battle.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'37] ---          [Atteka]           --- [02'37] #$#
#$#$#                  Atteka Inlet                   #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A large artificial wing has been brought here.

[001]     :{S} We've made these wings and carried them here just to fulfill
               a great prophecy.

           {M} We first heard the prophecy three years ago... The wings have
               come a long way since then.

[002]     :{S} We must be prepared to attach these wings to the sacred vessel.
               It is said that we will know the time has come when Mt. Jupiter
               is in flames.

           {M} These wings are so heavy that they would sink an ordinary ship.
               I wonder what kind of ship the sacred vessel is.

[003]     :{S} We brought these wings from Contigo, and now we're guarding them.
               If they were damaged or broken, the prophecy might never be
               fulfilled.

           {M} I doubt anyone could hurt these sturdy wings, but we must guard
               them just the same.

[004]     :{S} I wonder if these giant wings will really make it fly...
               I'd like to see that.

           {M} It's kind of hard to imagine what these wings would look like
               actually flapping.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'38] ---          [Atteka]           --- [02'38] #$#
#$#$#                    Contigo                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A giant crater lies to the east of the village.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Do you know anything about a legend about these people who could
               control the wind and air?

               --------------------------------------------
                    -(Yes)
               Well, the legend says that these giants from Anemos built Contigo
               with their wind powers.



                    -(No)
               That was the Anemos tribe. They even had the power to fly through
               the air! The people of Contigo inherited some of their power,
               and now, we rule over Atteka.
               --------------------------------------------

           {M} The Anemos blood in our veins often brings about strange
               miracles.

[002]     :{S} If you want to get a look at the Anemos geoglyphs, you ought to
               go to the ruins...

           {M} The Anemos geoglyphs are the most amazing carvings I've ever
               seen...

[003]     :{S} Our people have labored for some time to build the Wings of
               the Anemos.

           {M} We built the Wings of Anemos out of materials we found in the
               ruins of Anemos Sanctum.

[004]     :{S} The beacon within Jupiter Lighthouse will soon be lit. I know
               this because of a strange premonition I had three years ago.

           {M} Surely, someone will come soon to light the beacon atop the
               lighthouse.

[005]     :{S} I guess the people of Contigo lost the power they inherited from
               the Anemos tribe.

           {M} The power of the wind is not all that we've lost. We have lost
               much of our culture, as well as the technology to rebuild the
               ruins.

[006]     :{S} When the power of Anemos is lost, a group will come to light the
               beacon against darkness. We had thought it was nothing but
               legend, but it is all coming true.

           {M} I think Jupiter Lighthouse will be lit soon. I don't know when,
               but it will happen soon.

[007]     :{S} The Anemos geoglyphs show a boat with wings sprouting from its
               hull... The story goes that these wings could make the boat
               float in the air...

           {M} It's hard to believe, but the Anemos really did have the power
               to make ships fly.

[008]     :{S} The people of Anemos possessed power over the wind. They could
               also see into the future.

           {M} There were two siblings born in Contigo. The older held great
               power. Both are gone now... The younger was only a baby when he
               left the village. I don't know how strong he became.





   [ Buildings ]
[009]     :{S} The siblings who inherited the powers of the Anemos aren't in
               Contigo anymore. The younger brother was just a baby when the
               merchant known as Hammet took him away.

           {M} The families of children who inherited those powers lived lives
               of constant suffering. Eventually, they left Contigo to make
               their fortunes elsewhere.

[010]     :{S} I'm sure the younger brother, Ivan, must be grown up by now...
               Is he still with Hammet?

           {M} Ivan's mother left him in the care of a kindly merchant.
               She died shortly afterward. I think she died of sorrow at
               sending Ivan away. She wanted a better life for him.

[011]     :{S} My father doesn't approve of the way I look up to Yegelos.

           {M} I wish I could have inherited the power of the Anemos.
               Then I could be a hero.

-----

[Item]    :{S} The villagers are working their hardest to complete the wings
               and fulfill the prophecy.

           {M} Oh, how I want to see the sunlight shining off these wings
               up in the sky!

[012]     :{S} Long ago, the people of Hesperia attacked Atteka. Our fore-
               fathers were not afraid. With the help of the great hero Yegelos,
               we drove them off, and they haven't invaded since.

           {M} For a long time now, Contigo has been without a hero.
               This depresses our youth, I think.

[013]     :{S} A long time ago, the tribes of Shaman and Contigo were at
               constant war. Throughout their many battles, the warriors
               Yegelos and Hoabna formed a friendship.

           {M} Everybody thinks the people of Contigo are strong, but we just
               hate to fight. It's strange, because Yegelos loved to fight,
               and Hoabna was the stronger of the two.

-----

Innkeeper1:{S} We've had so many people coming to Contigo lately that we're
               full, and I'm beat!

           {M} It's good to have this much business, but what happens to us
               when the wings are done?

Innkeeper2:{S} All the work on the wings means that our inn is always full!
               It's a good time for us!

           {M} Once the wings are finished, all these guests will leave.
               Until then, I'll work my hardest.

Chef      :{S} If I don't make dinner now, it won't be ready in time for all our
               guests to eat!

           {M} I must be the greatest chef in the world! Look at all this food
               I've been making! I'm amazing!

Employee  :{S} Gotta make all the beds before everyone returns from Anemos
               Sanctum... Then, I've gotta get started setting things up for
               dinner before they come down to eat!

           {M} I've got so much to do that I don't even have time to eat!
               I'm starving!!!

[014]     :{S} The prophecies of the Anemos tell that someday soon, a true
               miracle will occur...

           {M} The Wings of Anemos are nearly complete... I think I'll take
               tomorrow off.

[015]     :{S} Did you just arrive in Contigo? Are you connected to the
               prophecy, or are you here to help build the wings?

           {M} I worked myself half to death yesterday. I feel miserable,
               but I'll do it again tomorrow.

[016]     :{S} I'm afraid I'm too old to help in the construction of the wings,
               but I so want to see them fly...

           {M} I threw my back out helping with the wings. I can't touch my
               toes. I can barely tough my knees.

[017]     :{S} When is the miracle of the Anemos gonna hurry up and happen?
               I can't wait forever!

           {M} I want to see the boat when it sails through the air on our
               wings. But even more, I want to see the hero or prophecy...
               Will he be a real looker, like Yegelos?

-----

G. Healer :{S} The real miracle will be if these wings actually make a boat fly.
               However, I remain open-minded. I hope we can see this miracle
               of Anemos soon!

           {M} If I see the Wings of Anemos make a boat fly through the air,
               I too shall be a believer.

-----

[018]     :{S} Soon, the siblings with the power of the Anemos will return
               and fulfill the legend.

           {M} I just know Ivan became big and manly, just like Yegelos.
               I know he'll return...

[019]     :{S} The power of the Anemos is all but gone in Contigo. However,
               it sometimes happens that a newborn suddenly shows power over
               the wind.

           {M} A terrible misfortune fell on the family of the siblings...
               It's a terrible story.

[020]     :{S} I don't have any powers like the Anemos did, but my sister, Ahri,
               is different.

           {M} Whenever my sister furrows her brow like that, strange things
               happen around here.

Ahri      :{S} <game>:  The baby's forehead is furrowed, like it's thinking.

                 * - A small gust of wind is summoned.

               Ahri  :  Babu bawaba bibaw.
               [018] :  It sure is drafty in this shabby old house.
               [019] :  When the Wings of Anemos are complete, let's fix
                        the house!

           {M} Bawaba... It's hot... I want cool wind, babu baba.





   [ Anemos Sanctum  -  Exterior ]
* - An artificial wing like the one from Atteka Inlet is being constructed
    atop a drawing of a winged ship.

[021]     :{S} The wings will be finished shortly. Where is the ship they're
               going to be attached to?

           {M} What do we do if we made these wings, and then no boat shows up
               for us to put them on?

[022]     :{S} Which part goes where? Does this metal feather connect to that
               wooden post? It's like a puzzle, and it's getting rather
               complicated.

           {M} There are too many parts! I think I'm going insane from all these
               stupid parts!

[023]     :{S} You've gotta watch out, 'cause you don't want to break
               anything... It's delicate work!

           {M} When I start getting irritated, I just go nuts. I think I should
               avoid getting irritated.

[024]     :{S} Just a few more touches, and the wings are done. All we have left
               is to assemble them!

           {M} How long have we been working on these stupid wings? When I see
               that boat soaring through the skies, I think I'll cry.

[025]     :{S} The wings are almost done. We just need to get them to the bay
               and await the ship.

           {M} I've been really busy lately, but now that the second wing is
               almost done, I can rest.

[026]     :{S} I've come a long way to see the flying boat. I hope the
               prophecies are right.

           {M} The guys carrying the other wing haven't come back, and we're
               almost ready to send this one!



* - Closer to the sanctum:

Sign 01   :{O} Felix examined the sign. The characters from the wall are
               translated there. Some them [sic] are gates, and some them [sic]
               are roads. Search with your heart to find the truest path.

[027]     :{S} That sign has a translation of the characters on the wall.
               If you're interested in studying the sanctum, you should give it
               a read.

           {M} I don't know if anyone in Contigo cares about what I'm doing
               here. But I know that devoted pilgrims will appreciate having
               this translation.

[028]     :{S} I want to get a good look at the inside of the sanctum, but
               I can't get this door to open. I'm hoping that deciphering these
               characters on the wall might give me the clue I need.

           {M} Wouldn't it be terrible if I got the door open and there was
               nothing on the other side?

[029]     :{S} Have you taken a good look at the Anemos geoglyph?

               --------------------------------------------
                    -(Yes)
               You can't see all of it right now, because the wings are covering
               up the picture...



                    -(No)
               Oh, that's really too bad. The picture of the flying boat looks
               so cool.
               --------------------------------------------

           {M} I can't even imagine how cool it would be to see a boat like the
               one in the geoglyph. But it's so big! I doubt there's a boat
               that big anywhere!

[030]     :{S} The merchant Hammet took the gold in this room with him when he
               left Contigo. He vowed to use the money to raise Ivan properly
               and give him a good life.

           {M} Someone told me that Hammet went to a town called Kalay and
               did quite well for himself.





   [ Game: Lucky Wheels ]
Owner 1   :{S}   * - With Game Tickets:

               Step right up and try your hand at lucky wheels! You have <#>
               game tickets, Felix. Would you like to use these tickets?

               --------------------------------------------
                    -(Yes)
               Step right up and enjoy yourself.


                 * - Win something:
               Congratulations! You won [PRIZE]! Here you go. Come again!


                 * - Don't win anything, with no tickets left:
               Too bad... Come back after you get some tickets.


                 * - Don't win anything, with some tickets left:
               Too bad... Would you like to use your tickets to keep playing?
                   --(Yes)
               Step right up and enjoy yourself.
                   --(No)
               Come again!



                    -(No)
               The rules are listed on the sign. Take a look, take a look.
               --------------------------------------------


                 * - Without Game Tickets:

               Step right up and try your hand at lucky wheels! You gotta have
               game tickets to play.

           {M} Hmm... I wonder if these kids will take all the best items...

Sign 02   :{O} Turn the slot and get a prize! The lottery slots are over here.

Sign 03   :{O} Lucky Wheels Rules
               Pull the lever and try to line up matching icons to win big.
               You have only 5 chances to pull the lever. Press the star to
               keep a wheel from spinning and match other wheels.
               You get 1 line for 1 game ticket, 3 lines for 2 tickets,
               5 lines for 3 tickets, and 7 lines for 4 tickets.
               Use all your tickets on Lucky wheels!

Sign 04   :{O} Lucky Wheels Prizes
               Prizes are determined by which icons you match.
               Shirts win undershirts, Rings win rings, Boots win boots,
               Stars and Heart win items, and Moons can win you anything.





   [ Game: Super Lucky Dice ]
Owner 2   :{S} Welcome, welcome, step right up! Care for a round of
               Super Lucky Dice?

               --------------------------------------------
                    -(Yes)
               OK, then, let 'em roll!
                 * - If you win more coins than you lose:
               Ya won <#> coins! Talk about lucky!
                 * - If you lose more coins that you win:
               Ya lost <#> coins. Better luck next time.



                    -(No)
               Oh really? That's a shame!
               --------------------------------------------

           {M} When they lose, they call me a cheater. When they win, they call
               it skill. Really, it's all just luck.

Owner 3   :{S} If you want to learn about the rules to Super Lucky Dice,
               just check out the sign.

           {M} It's not a tough game, not if you play enough. You just sorta
               learn as you play...

[031]     :{S} So, tell me, pal... have you ever played Superdice before?

               --------------------------------------------
                    -(Yes)
               Yeah, but you've never won, have you? I can see it in your face.



                    -(No)
               Now, this here's a simple game, but it's my favorite dice game.
               --------------------------------------------

           {M} This kid's got unlucky written all over his face. One unlucky
               person can spoil it for everyone... I hope he doesn't ruin
               my lucky streak.

[032]     :{S} I almost always get at least one pair, but then I lose everything
               on the hi-lo game!

           {M} I can win, I can win, I can win! Whoa! ...I'm going to lose...

[033]     :{S} If you lose the hi-lo game, you don't win anything... It's tough
               to know when to quit!

           {M} It's tough to know when to keep playing and when to cut your
               losses.

Sign 05   :{O} Drop some cash and double up! The hi-lo dice are over here!

Sign 06   :{O} Super Lucky Dice     The Rules of the Game.
               Throw all four dice onto the table in a single toss. If two
               of the dice match, it's a push, and you win your money back.
               If three of the dice match, you win back twice the bet you
               placed. If you get two pairs of matching dice, you win three
               times the bet you placed. If all four dice match, it's a
               perfect toss! You win eight times your bet!

               If you get one pair, two pair, three of a kind, or a perfect
               four, you can play the hi-lo game! You have to guess whether
               the next roll of the dice will be more or less than your current
               total. If you win the hi-lo game, you double your winnings!
               You can do this up to five times.





   [ Game: Lucky Dice ]
Owner 4   :{S} Hey, buddy, wanna try yer luck at the dice? It's 550 coins
               to play.

               --------------------------------------------
                    -(Yes)
               OK! Then take the dice.
                 * - If you win more coins than you lose:
               Ya won <#> coins! Talk about lucky!
                 * - If you lose more coins that you win:
               Ya lost <#> coins. Better luck next time.



                    -(No)
               No? Oh, well. Who's next?
               --------------------------------------------

           {M} Winning or losing is pure luck. I ain't cheatin' nobody.

Owner 5   :{S} Read the sign if ya don't know the rules.

           {M} The rules for Lucky Dice ain't all that hard. Ya can even
               learn 'em while ya play.

Sign 07   :{O} You never know what the dice will do next! Come and give our
               dice a toss!

Sign 08   :{O} Lucky Dice
               Throw the dice on the table and try to get the same numbers.
               Prizes are based on the number rolled and where each die lands.
               The more numbers that match, the more you win.

Sign 09   :{O} Lucky Dice

               If two numbers match on either the dice or the table...
               it's called a pair, and you don't win or lose anything.
               Two pair doubles your money. Triple matches triple your money.
               Four of a kind is perfect, and you win five times your bet.
               Plus, if your dice come up perfect on the Perfect Bonus spot
               on the table, you win an even bigger bonus!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'39] ---          [Atteka]           --- [02'39] #$#
#$#$#               Jupiter Lighthouse                #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Room with elevated platform in front of heptagon with hole  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

?????     : Holder of the star... Show the power of Anemos!

* - As Hover is unleashed atop the platform, Psynergetic energy swarms the
    heptagon and light bursts forth from the hole in its center. This activates
    the areas that allow for Hover to be utilized.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Exterior  -  Southeast of Cyclone stone that led to red door  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - On a high ledge of the tower:

Mia       : Ahhhh!!!
Garet     : Mia!

* - They are not in view.

Garet     : Oof!
Mia       : Noooo!!!

Ivan      : Garet!
Isaac     : Mia!



Kraden    : Is that... It's Isaac and the others!

Piers     : Isaac? Isn't he a friend of yours, Felix?

-----------------------------------------------------------
     -(Yes)
Kraden    : They both come from Vale, and regardless of what Isaac believes,
            they must be allies now!



     -(No)
Kraden    : Don't be that way! You two have much in common, even if you are
            at odds right now...
-----------------------------------------------------------

Jenna     : But Isaac and the others came all this way just to try and stop us!

Sheba     : But didn't you hear that? It sounded like a cry for help...
            What if they're in trouble?

* - They rush ahead and look up. Above them, Mia and Garet have fallen from the
    small inverted drawbridge (two parts that hang down when a button is
    pressed). Garet has taken hold of a small ledge, which Mia sits on.

Isaac     : Hang on, Mia! Don't worry, Garet! Everything will be fine!

Mia       : Don't worry about me... I'm fine, but Garet...

            Garet, you're only using one arm to hang on... What's the matter?

Garet     : I don't know... I think I hurt my arm when I fell...
            It's totally numb! I can't move it!

Mia       : You shouldn't have tried to cave me when I fell into that hole...

Garet     : Oh, Mia, don't blame yourself... I wasn't going to leave you
            down there!

* - Mia tries to pull Garet onto the ledge.

Mia      : It's no use! I can't pull you up, Garet! I'm not strong enough!
           Isaac, please! You've got to save Garet!

Isaac    : This doesn't look good... We have to save Garet, and fast!

Agatio   : No, I'm afraid you won't be doing that.

* - Agatio and Karst appear.

Ivan      : Who are you!?

Karst     : Me? Why, I'm Karst.

Agatio    : And I'm Agatio.

Isaac     : If you're not here to help my friend, then get out of my way,
            so I can do it myself!

Karst     : Your friends will have to take care of themselves. You have a
            little debt to repay.

Ivan      : Debt? What are you talking about? We've never even seen you before!

Agatio    : Regardless, you have done Karst here a great wrong, and you're
            beginning to be a hindrance to us.

Isaac     : Wait a second... You two look familiar somehow... Do you know
            Saturos and Menardi?

Karst     : So, you're not such a fool after all, Isaac! You are right.
            We are of the same clan. The Fire Clan, from the frozen land of
            Prox, far to the north!

Ivan      : Prox? Never heard of it.

Agatio    : That doesn't surprise me. Our town hangs on the brink of extinction.
            And the seal placed on Alchemy is responsible!

Isaac     : What are you saying? That doesn't make any sense.

Karst     : It matters not! For soon, Prox will recover its lost power...

Agatio    : We shall bring Prox back from the edge, and then all the people
            of Weyard will kneel before us!

Ivan      : You think we'd let you, after hearing all that nonsense?

Karst     : See! You're a hindrance!

Isaac     : And Felix was trying to help you?

Agatio    : Actually... we don't know what Felix's objectives are.

Karst     : And we don't care, so long as he lights the beacon on Jupiter
            Lighthouse.

Ivan      : Then get out of our way! We're here to stop Felix!

            Move, or we'll have to move you ourselves!

Agatio    : Did you hear that, Karst? They actually want to fight?

Karst     : You mean to tell us that you would leave your friend... hanging?

Isaac     : So this was all part of your plan?

Ivan      : Cowards! Stop playing dirty and fight fair!

Agatio    : If you really are the brats who killed Saturos and Menardi, then
            you've earned some new foes!

Karst     : But answer me this: would you still cry foul if you were fighting us
            four on two?

Ivan      : That's why you were waiting up here? To set a trap and make Mia and
            Garet fall?

Agatio    : We didn't plan on snaring both of them, though... That WAS a
            pleasant surprise!

Isaac     : So that's the deal, is it? You came up here to fight us?

Karst     : Oh, did you figure that out all on your own? Impressive!
            I'm quite fond of intelligent boys...

Ivan      : I hope you don't think we're afraid of a fair fight, two on two...

Agatio    : A fair fight?

Karst     : I'm sorry if I misled you, but we have a third... A Water Adept...
            Alex!

* - Karst looks back from where she and Agatio came.

Karst     : Alex? ...Where is he?

Agatio    : What's wrong, Karst?

Karst     : It's Alex! He's gone!

Agatio    : What!?

Isaac     : Alex!
Ivan      : Alex?

Karst     : Did anyone see where he went?

Agatio    : Forget about him! Honestly, I was planning to do the same to him
            that I'm about to do to them! My only regret is that I won't be
            able to wipe that sneering smile off his face.

Karst     : Well, take out all of your aggressions on these brats...
            You'll feel better!

* - They commence combat.

Kraden    : Felix! Agatio and Karst are attacking Isaac and the others!

Sheba     : Do you think Isaac and Ivan can handle them without Mia and Garet's
            help?

Piers     : I'm disgusted that Karst would set a trap for them.
            It's dishonorable!

Jenna     : What if Garet loses his grip while they're still fighting?

Kraden    : There's still time! We have to help Isaac!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  On the way to Isaac's group  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

Alex      : Ah, Felix... I've been waiting for you. Have you come here to light
            the beacon?

-----------------------------------------------------------
     -(Yes)
Alex      : And you're sure that's ALL you're going to do?



     -(No)
Alex      : Hmph. They consider you their enemy, and yet you pity them.
-----------------------------------------------------------

Alex      : I saw you watching when Isaac's friends fell into Karst's trap.
            I know you, Felix. I know that if you leave Isaac behind,
            you'll regret it. You're not like me. You can't simply discard
            someone who is no longer of use to you. Well, you'd better hurry
            if you still hope to save them.

<game>    : Everyone recovered fully.

Alex      : There you go! Consider it a gift. You can still make it. Go on...



* - Before continuing:

Alex      :{S} It is time you followed your true feelings. Go on.
               Save your friends.

           {M} Even now, I want to run to Mia, to give her my aid...
               It seems I am weak as well... I suppose I have no choice
               but to part ways with Agatio and Karst.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Near the small inverted drawbridge  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

Ivan      : Isaac... I'm sorry... I can't take it any more... [sic]

* - He collapses.

Isaac     : Keep it together, Ivan!

Agatio    : Ha! You're a fool! Never let concern distract you in battle!

* - Agatio casts Rising Dragon, downing Isaac.

Karst     : We did it, Agatio!

Agatio    : It was close, but we did it.

Karst     : Heh... He's no warrior. His concern for his friend gave us the
            opportunity to strike!

Agatio    : What's this? He's still alive!? Even after that blow?

Karst     : It would be a shame if you and I ever had to regret letting
            him live...

Kraden    : Isaac! Watch out!

            He's still alive! If we're going to act, Felix, we have to act now!

Sheba     : They're going to kill Isaac!

Jenna     : No, they aren't! I'm not about to let that happen!

Piers     : None of us are, Jenna!

Agatio    : Felix? What's going on?

Karst     : Be grateful! We just did you a favor!

* - Agatio looks about.

Agatio    : I understand that when Venus was lit, the ground shook so fiercely
            that the very earth split. Curious that it hasn't here!

Karst     : You haven't lit the beacon yet, have you? And after all we've done
            to help you!

Kraden    : We're going to light to beacon right now...

Agatio    : If that's true, then you'd better go do it!

Sheba     : But we're not leaving Isaac behind.

Karst     : Oh, great... Are you going to betray us now?

-----------------------------------------------------------
     -(Yes)
Karst     : Typical. And you're going to try to stop us from finishing them off,
            aren't you?



     -(No)
Karst     : Don't lie... We can see it in your eyes. We can see what you truly
            mean to do.
-----------------------------------------------------------

Piers     : If you're only here to clear the way for us to light the beacon,
            then your work is done.

Agatio    : Isaac has proven to be a greater foe than we'd imagined.
            We can't let him live.

Karst     : Consider how powerful these two were without the aid of a Water
            Adept. We have to finish them.

Jenna     : If you want them, you're going to have to face us first!

Kraden    : You're both quite badly injured... You're in no shape to fight
            all four of them. I think it would be best if you left now.

Karst     : We haven't much choice...

Agatio    : Karst, no!

Karst     : Agatio, if we fight Felix now... we'll be destroyed.

Agatio    : Isaac killed your sister! Where is your anger!?

Karst     : I am filled with rage, but not so much as to be blinded by it.

Agatio    : What, then? Do we give up? Fine! But this is not the end.

Karst     : Do with Isaac as you will.

Agatio    : But swear this oath to us: if we leave now, you will light the
            beacon's fire.

-----------------------------------------------------------
     -(Yes)
Agatio    : I don't care if you want to help Garet or not! The lighthouse
            comes first!



     -(No)
Agatio    : We do not have time to wait for you to save Garet!
-----------------------------------------------------------

Kraden    : Go, Felix. I will tend to Garet.

Karst     : And be sure to bring with you the Mars Star that Isaac carries
            on him.

Kraden    : How did you know about the Mars Star?

Agatio    : Did you think this was about nothing more than revenge?
            Alex told us about it!

Karst     : Take the Mars Star, or we'll be forced to make you!

* - Piers approaches Karst.

Agatio    : Do not force our hand on this!

Isaac     : Go on, Felix. Take it. I don't know why you're doing this, but
            I trust you... Take the Mars Star.
<game>    : Felix took the Mars Star.

Karst     : That's better, Felix. We'll be waiting for you on the aerie.

* - She and Agatio depart. Felix goes to follow them.

Piers     : Felix, wait... We cannot trust them. Take me with you...

Sheba     : Good thinking. If something happens up there, you'll be safer
            with Piers.

Jenna     : We'll be fine. Take Piers with you...

Kraden    : Listen to the others... Safety in numbers, as they say...



* - Before leaving:

Jenna     :{S} Isaac! I don't know how you survived that attack, but I'm so glad
               you did... We're going to help you... We're going to heal you...

Sheba     :{S} Ivan... You've been injured. Don't worry about the others.
               Let's take care of those wounds.

Kraden    :{S} We have to help Garet. He can't hold out for much longer.

Isaac     :{S} F, Felix... No! Why are you helping them?

Ivan      :{S} Don't worry about us... Help Garet and Mia first.


#$#$#$#$#$#$#
$#  Aerie  #$
#$#$#$#$#$#$#

Karst     : You're late, Felix!

Agatio    : Now light the beacon!



* - Their Mind Read script can only be obtained via hacking.

Karst     :{S} Once you've lit the beacon, we might even forgive you for saving
               Isaac back there.

           {M} Once Jupiter is lit, we'll have no need for you. Just watch...

Agatio    :{S} Once Jupiter is lit, only Mars remains! Now, light the beacon!

           {M} Do even think [sic] about resisting us... We have our own ideas
               about that. Once the beacon is lit, your usefulness will have
               run out for good.



* - Upon approaching the beacon:

<game>    : There seems to be a wide hole for the Elemental Star.
            Cast the Jupiter Star in?

* - Felix does so. A pillar of light bursts forth.

Piers     : I've heard tales of this... But I had no idea it would be so
            spectacular.

* - A blue/purple sphere of Psynergetic energy forms above the hole.

Piers     : We have ignited the beacon... The third lighthouse is lit...
            Now let us go...

Karst     : I don't think so...

Agatio    : You see, you've betrayed us once already...

Karst     : We simply can't trust you anymore...

Agatio    : And now that Jupiter Lighthouse is lit, I'm afraid we have little
            use for traitors.

Karst     : Poor dear... You look puzzled. Would you like to know why we don't
            need you?

-----------------------------------------------------------
     -(Yes)
Karst     : I'd be happy to tell you. Mars Lighthouse is in Prox.



     -(No)
Karst     : Figured it out, have you? Yes, Mars Lighthouse is in Prox.
-----------------------------------------------------------

* - While Felix and Piers are distracted by this new information, Karst dashes
    at Felix and swipes the Mars Star.

Piers     : What are you doing!?

<game>    : They stole the Mars Star!

Karst     : Your job is done now.

Piers     : We're not done yet...

Agatio    : We've got the Mars Star! We don't need you anymore!

Karst     : You know what that means, of course, don't you?

-----------------------------------------------------------
     -(Yes)
Karst     : Exactly! That means it's time to die, Felix!



     -(No)
Karst     : No? Well, how can I put this? It's time to die!
-----------------------------------------------------------

Piers     : But what will happen to Felix's parents?

Agatio    : We keep our promises! Once all four lighthouses have been lit,
            we shall release them!

Karst     : We would never do anything as terrible as breaking our word...
            as you have done so casually.

Agatio    : But if you're dead... Who will come to take them home from Prox?

Karst     : I guess they'll just have to spend their remaining years in the
            frozen wastelands of the north!

Agatio    : Don't worry! They'll be fine! Now prepare for the end!

* - They engage Felix and Piers in combat.





* - After two turns pass:

Jenna     : Felix! I thought you were taking too long, so I came to check
            on you. What's going on?

Piers     : They say they don't need us anymore...

Karst     : Agatio! Felix's sister isn't supposed to be here...

Agatio    : What do you want me to do? We can't just leave now! We have to
            finish them!

Jenna     : Don't worry, Felix! I'm here to help!





* - After two turns pass:

Sheba     : Jenna! I got the feeling something was wrong, so I rushed up here.
            Just in the nick of time, it looks like!

Jenna     : Thank you, Sheba! I'm not looking forward to fighting, but I'm
            glad you're here.

Karst     : Another one? Agatio, we're rapidly being outnumbered!

Agatio    : It's too late to flee now! We have to keep fighting!

Sheba     : Isaac and the others are safe! Now let's take care of these two
            rats!





* - If the battle was won:

    Agatio and Karst have collapsed onto the ground.

Piers     : We did it... We beat them...

Jenna     : Barely...

Sheba     : What should we do with them?

Agatio    : Finish us!

Karst     : But think: what happens to your parents if neither we nor Saturos
            and Menardi return?

Jenna     : Are you saying our people will kill our parents if you don't return
            to Prox? I doubt that!

Agatio    : Well then, I suppose you'd better finish us off, like you said.

Karst     : What's the matter? Are you going to do it or not?

-----------------------------------------------------------
     -(Yes)
Alex      : No, Felix! Don't!



     -(No)
Alex      : You've made the better choice, Felix.
-----------------------------------------------------------

Jenna     : When did you get here, Alex?

Alex      : If Karst is not bluffing... If you kill them, all your efforts will
            have been for naught. Do you understand, Felix? If that happens,
            Isaac will suffer the same fate you do...

* - Alex uses his Psynergy to heal Agatio and Karst.

Sheba     : Alex! What are you doing!?

Alex      : I have revived them.

Jenna     : Why!? Are you going to make us fight them again?

Alex      : Don't worry, Jenna. Look at them... They can barely walk right now.

Piers     : Still, that doesn't give you the right to...

Alex      : If you're not going to finish them off, you'll just be leaving
            them here, won't you?

Agatio    : You're not going to help us defeat these brats?

Karst     : You better not be expecting a big thank-you for this, Alex!

Alex      : Of course not, Karst. I would never ask for your gratitude.

* - Kraden speaks from off-screen.

Kraden    : What's keeping Felix and the others?

Alex      : We should be going before Isaac and the others arrive.

Sheba     : If they're coming up, how do you plan on avoiding them on your
            way down?

Alex      : Do not worry about us... We'll just take the elevator. Now that
            the lighthouse has been lit, it should be fully operational again.

* - Alex, Agatio and Karst head to the western elevator. By that time,
    Kraden and Isaac's group have arrived at Felix's group's location.

Kraden    : Oh! You're looking better!

Isaac     : Felix, Jenna...

Jenna     : Isaac... Garet...

Garet     : Man! They got away! What a bunch of jerks!





* - If the battle was lost:

    Felix's group collapses onto the ground.

Karst     : Isaac wasn't the only surprise. They were all far more powerful
            than I'd expected.

Agatio    : Don't worry, Karst! We'll win in the end...

* - Felix twitches.

Karst     : This one moved... I can't believe they're still alive! The pests!

Agatio    : If we stay here much longer, Isaac and the others will come!
            We should leave!

Karst     : I know... But treason deserves death! We must finish them!

Alex      : There's no time for petty grudges!

* - Alex stands at the bottom of the stairs nearest the beacon.

Agatio    : Alex! You...

Alex      : You no longer consider me a friend? I do not care.

Karst     : It goes beyond that, Alex! You've betrayed us, and treason deserves
            death!

Alex      : Yes, I heard you the first time. But shouldn't you heal yourselves
            before making foolish threats? After fighting both Isaac and Felix,
            you're in no condition to fight me. And if Isaac and the others
            come, what chance will you have?

* - Kraden speaks from out of view.

Kraden    : What's keeping Felix and the others?

Alex      : There's no time to talk!

Karst     : Then what should we do?

Alex      : We take the elevator! With the beacon lit, it should be fully
            opterational once more.

Agatio    : We have no choice. Let's go.

Alex      : Good! You're listening to reason! Now follow me!

* - Alex, Agatio and Karst head to the western elevator. By that time,
    Kraden and Isaac's group have arrived at Felix's group's location.

Kraden    : Felix! Jenna!

Isaac     : What's happened?

Kraden    : It seems they fought with Agatio and Karst...

Ivan      : I had a really bad feeling after Sheba left. I hate it when
            I'm right...

Mia       : Your power of prediction must be even stronger than you'd thought,
            Ivan...

* - Isaac notices that the western elevator has descended.

Isaac     : Blast! They must have taken the elevator to escape!

Garet     : How could they have done that to Jenna? Those monsters!

Ivan      : Felix tried to help us... They must have attacked him because he
            betrayed them.

Mia       : So, does that mean Felix isn't really our enemy?

* - Felix twitches again.

Kraden    : Felix! You're alive!

Isaac     : Mia, he needs healing, quickly! There's still time!

Garet     : Don't let 'em die! Felix still has a lot of questions to answer
            before he's in the clear!

Kraden    : If you save Felix, we'll tell you everything...

* - Mia heals everyone.





* - Regardless of the battle's outcome:

Isaac     : All right, Felix! We want to know what's going on!

Kraden    : It's all quite complicated, Isaac. There are a number of

* - Slight pause.

Kraden    : extenuating circumstances.

Garet     : What are you talking about, Kraden?

Ivan      : Look, I don't think any of us are in any shape for another fight
            right now.

Isaac     : What do you mean, Ivan?

Ivan      : I'm just saying we should get ourselves back to Contigo and
            sort things out there.

Kraden    : That's a sound plan, Ivan... I fully agree.

* - Everyone else seems in agreement.

-----------------------------------------------------------
     -(Yes)
Isaac     : You're right. We can't fight right now. Let's head back to Contigo.
            What do you say, Felix? Can we talk there?

            We'll be waiting for you... So don't think you can sneak off again!



     -(No)
Jenna     : He's right, Felix. It's time we explained ourselves to them.
            We should go to Contigo.

            We'll be there, Isaac. I promise. I hope you can still trust us.

Isaac     : I never stopped trusting you, Jenna. I'll be waiting for you
            in Contigo.

* - Isaac turns to Felix.

Isaac     : We'll be expecting you. Don't think you can sneak out of this!
            You owe us an explanation!
-----------------------------------------------------------

* - Isaac's group departs via the eastern elevator. Felix's group takes the
    western elevator once it returns.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'40] ---          [Atteka]           --- [02'40] #$#
#$#$#                    Contigo                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - If you try to go to Atteka Inlet:

Jenna     : You're not planning on running away from Isaac again, are you?
            We can't run anymore, Felix. I promised him that we wouldn't.
            Besides, they want to talk, not fight... They're waiting for us.
            Let's go to Contigo.

* - 2nd+ time:

Jenna     : We shouldn't run from Isaac anymore, Felix.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Are you looking for Isaac? He and his colleagues are in the house
               at the top of the hill. Are you the people they've been waiting
               for?

           {M} They look like they're in for some trouble. Oh well...
               I ain't a'gonna help 'em.

[002]     :{S} The crater behind the village is supposed to be where the city
               of the Anemos was. The legend says that, one day, it just
               lifted off the ground and flew away!

           {M} Cities flying up in to the sky? I don't buy that for a second!

* - [003] has left.

[004]     :{S} Everyone's left town for the time being. They're transporting
               the wings... Actually, they might even have finished putting them
               onto the ship by now.

           {M} The prophecies are all coming true... We're living in some
               strange times, it seems.

[005]     :{S} Is that your boat? It looks exactly like the one in the
               geoglyphs.

           {M} It's just like the legends said... The ship in the geoglyphs
               has finally come to Contigo.

[006]     :{S} The legends tell us that a great calamity brought an end to
               the Anemos... It had something to do with the light from the
               lighthouses being extinguished.

           {M} The ancient city of the Anemos was located right near the ruins.
               That crater nearby is where the city once was.

* - [007] has left.

[008]     :{S} Jupiter Lighthouse has been lit, for the first time in years...
               Did you feel that earthquake? If that's what happens when the
               lighthouses shine, I wish that it had stayed dark!

           {M} What does it mean, when ancient legends are turning out to be
               true? I just want the world to go back to the way it was before.





   [ Buildings ]
* - All buildings except the inn and Great Healer's shrine are locked.

-----

Innkeeper1:{S} You have to hurry! I think the ship from the geoglyphs is going
               to take off soon!

           {M} Once all our customers leave, I'm free to go. So hurry up
               already!

Innkeeper2:{S} First, the lighthouse is lit, and now, we're going to see a
               flying boat! It's like a festival!

           {M} I can't believe it... All of the hopes of the people of Atteka
               have come true here, in Contigo! It's like a miracle, a dream
               come true! This calls for a festival!

Chef      :{S} They've finished putting the wings on the boat, but I don't see
               what the big deal is. It's just a flying boat, for crying
               out loud!

           {M} It was kind of impressive watching the procession carrying
               those wings, though...

Employee  :{S} The boss said it was all right for us to go to the inlet once
               all the customers leave. So hurry up and leave, so we can go
               watch the boat!

           {M} All these years, I thought it was just a children's story,
               but now it's all coming true...

* - The others are still here, but their script is unchanged.

-----

G. Healer :{S} A flying ship... Surely, it must be a miracle. I'll have to
               study this closely.

           {M} Perhaps if I see a miracle with my own eyes, my faith will be
               restored once more...





   [ Anemos Sanctum  -  Exterior ]
* - Everyone has left.


#$#$#$#$#$#$#$#$#$#$#$#
$#  House atop hill  #$
#$#$#$#$#$#$#$#$#$#$#$#

Isaac     : I'm glad you kept your promise, Felix.

Garet     : All right, let's hear what he has to say for himself!

Jenna     : What can we say, Isaac? Has Felix ever harmed you? Have we ever
            fought against you?

Sheba     : Felix's been avoiding you, but he never had any intention of
            fighting you or anything...

Mia       : And he definitely helped us out back at Jupiter Lighthouse.

Ivan      : Isaac's been worrying about Jenna nonstop since this nightmare
            began! How could she run away from him like that?

Piers     : She was afraid that if we met, we would be forced to fight...
            She didn't want that.

Isaac     : I know that, now... But it doesn't explain why you're doing this...

Kraden    : Felix betrayed his hometown, Vale... That's why he hasn't been
            able to face Isaac. Felix had hoped to play the villain alone,
            without getting Jenna or me involved...

Garet     : He betrayed Vale? Kraden, what are you talking about?

Kraden    : He conspired to steal the Elemental Stars and fire the beacons of
            the four lighthouses.

Mia       : That's what Saturos and Menardi were trying to do...

Ivan      : Why were you helping them?

Jenna     : Our parents' lives were at stake! We had to help!

Garet     : Parents? But... your parents died three years ago, in that storm...

Kraden    : That night, Saturos and his men had raided Sol Sanctum... The storm
            was their doing.

Jenna     : Garet, you saw two strangers that night--Saturos and Menardi.
            They were the only survivors of Saturos's raiding party.

Kraden    : They had failed to solve the mystery of Sol Sanctum. In doing so,
            they triggered the storm.

Jenna     : Everyone thought that you were killed by that boulder, Felix.
            I can't tell you how glad I was to find you were alive!

Kraden    : In fact, nobody was killed by the boulder that day!

Isaac     : So that means...

Ivan      : Wait a minute, Kraden... Did you just say that NOBODY was killed
            by that boulder?

Mia       : But what about Isaac's dad? And Jenna and Felix's parents?
            I thought they'd died that day!

Isaac     : I'm not so sure now...

Kraden    : Yes! If Felix survived, Kyle and the others may have as well...

Mia       : Why didn't you tell us? We could have worked together to save
            your parents, couldn't we?

-----------------------------------------------------------
     -(Yes)
Ivan      : Except that we had only just begun our journey, and we simply
            weren't strong enough.



     -(No)
Ivan      : He's right. They were too powerful then... It would have been
            impossible.
-----------------------------------------------------------

Kraden    : There's more to it than that. He had another reason to light the
            lighthouse beacons. Unless the lighthouse beacons are all lit,
            Weyard will eventually be destroyed.

Isaac     : Destroyed? But... how? Why?

Piers     : King Hydros, ruler of Lemuria, says that our world is steadily
            shrinking.

Sheba     : Elemental energy drives the growth of civilization. Without it,
            we and our world will wither.

Mia       : All that because the lighthouses aren't illuminated?

Kraden    : According to my research, that seems to be the case.

Garet     : But... once the lighthouses are all lit, you said the world would
            end anyway!

Kraden    : That... might be true, too... But if we do nothing, the world will
            definitely end.

Isaac     : Wait for the end of the world to come or wind up accidentally
            triggering it ourselves... What a choice...

Kraden    : Nothing is certain. There is no way to prevent the world from
            reaching its natural end. However, we can fight to save the world
            from withering away due to the actions of men.

Garet     : And, Felix, you knew this? You were helping them because you knew
            what was happening?

-----------------------------------------------------------
     -(Yes)
Garet     : You're a lot smarter than I remember you being...



     -(No)
Garet     : You just figured it out along the way, huh? That's still pretty
            darned smart.
-----------------------------------------------------------

Isaac     : Why did you wait so long to tell me? I would have helped you...

Kraden    : You wouldn't have done it before, Isaac... It would have meant
            violating the sacred teachings of Vale.

Hamma     : Now that we know all of this, shouldn't we be going?

* - Hamma of Lama Temple on Angara enters the building.

Mia       : Hamma!

Hamma     : Hello again...

Kraden    : Hamma! You... know Isaac? And his companions, too?

Isaac     : We met at the temple on the edge of the Lamakan Desert...
Hamma     : I'm Hamma, descendant of the Anemos.

* - Everyone appears surprised at her statement.

Hamma     : I was born in Contigo, and I inherited the power of the Anemos.

Garet     : Hey... We just got into Contigo, and we found out this is where
            Ivan was born!

Mia       : Yeah... We also learned that he's got a sister!

Sheba     : Sister... You don't mean...

Hamma     : That would be me, yes.

* - Ivan approaches Hamma.

Hamma     : Not now, Ivan... This isn't the time. Three lighthouses have been
            lit... The elements have been thrown out of balance. Jupiter is
            growing stronger, and the north grows colder with every passing
            moment. You must hurry to Mars Lighthouse. Ignite its beacon,
            before all of Weyard freezes...

Jenna     : Mars Lighthouse? Agatio has the Mars Star. He's on his way to
            light it now!

* - Hamma uses her Psynergy to examine the future.

Hamma     : I doubt they will be able to light the Mars beacon...

Piers     : Why's that?

Hamma     : There is a powerful force that does not want to see Mars rekindled.
            You will fail as well... unless you pool your strengths together
            and fight as one.

Kraden    : This is bad. We have to go... now!

Hamma     : I had hoped that you would feel that way... I've prepared a gift
            for you, to aid you on your way to Mars Lighthouse. I must leave
            you now, but we will meet at the inlet.

* - Hamma departs.

Jenna     : I'm sorry we left Venus Lighthouse without seeing you...
            I'm sorry for making you worry... Maybe when this is all over,
            we can all go on a trip together.

Sheba     : Hey, Jenna, you sure seem calm, considering that we're racing to
            meet our enemies...

Mia       : I'm just relieved that we've sorted our differences...

Piers     : Me too, Mia... We could not have stood divided against a common foe.

Garet     : Yeah, I guess I'm a little happy that we're not going to have to
            beat Felix up.

Isaac     : Listen, this is Felix's quest now... We're just doing what we can
            to help out...

* - Jenna turns to Felix.

Jenna     : Aren't you happy?

-----------------------------------------------------------
     -(Yes)
Kraden    : Everything's finally come together...This is how it was meant to be,
            Felix.



     -(No)
Kraden    : Don't worry about the future, Felix... Enjoy this brief moment's
            happiness.
-----------------------------------------------------------

Kraden    : But Hamma's waiting for us. Let's go to our ship!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'41] ---          [Atteka]           --- [02'41] #$#
#$#$#                  Atteka Inlet                   #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

* - If you try to leave to the east, two men stop you.

Man 1     : Where do you think you're going?

Man 2     : We worked really hard on that ship of yours!

Man 1     : I want to see our handiwork take flight. Don't you, buddy?

Man 2     : I want to! Boy, do I want to!

Man 1     : So hurry up! We want to see the boat fly!

Man 2     : Thanks, buddy!





[001]     :{S} Everyone's waiting down by the beach. They all want to see
               the boat fly with their own eyes.

           {M} Hamma is the new leader of Contigo. She bears the powers of
               the Anemos, after all. But I still think she shouldn't be
               ordering us to help fix up your boat.

Healer 1  :{S} When people work together, even a little spiritual power can
               work great wonders. We sent everyone back to the village so that
               their hopes would not impair your flight.

           {M} We can't get too close to the boat, or it might not fly...
               We've just go to have everyone watch from afar.

Man 1     :{S} The villagers are all waiting to see the ship fly. So how's about
               getting on with the flying!?

           {M} It's amazing to think that my hard work is going to help make
               that boat fly.

Man 2     :{S} Hamma wouldn't let us get any close, so we're waiting here to
               watch the ship leave.

           {M} Hamma says that our own hopes and dreams might prevent the boat
               from flying. It's as though, by wanting it too much, we'll
               actually prevent it from happening.

* - Four healers are by Hamma.

Healer 2  :{S} It's almost time... Time to watch a legend become reality!

           {M} The day has finally come that the ship will fly on the Wings
               of Anemos...

Healer 3  :{S} If everyone will just obey Hamma's request, the ship will
               surely fly.

           {M} The Anemos were powerful, sure, but can their power really make a
               great ship fly? No... No, I must not doubt... I must have faith
               that it will fly. It is meant to be.

Healer 4  :{S} Once you remove the stone anchors weighing the ship down,
               it should fly...

           {M} I hear that the warriors brought the Hover Jade back with them...
               Now, that's something that I'd really like to see.

Healer 5  :{S} When the winged ship of Anemos flies once again, the whole land
               shall be made free... That's what the legend says, anyway...
               But what land needs freeing? We seem free enough...

           {M} These warriors will know what to do... They'll know how to
               save the land...


#$#$#$#$#$#$#$#$#$#
$#  By the ship  #$
#$#$#$#$#$#$#$#$#$#

Hamma     : I've been waiting for you, Felix. Take a look at your ship.
            Now that you have been given wings, all obstacles in your path
            will vanish forever... However, it is not the wings alone that
            grant your ship the power of flight. Psynergy if the force that
            powers the Wings of Anemos. If the ship is to fly, you will need
            to focus the power of your minds... You have visited Shaman Village
            recently, have you not? Now is the time ot make use of the powers
            you acquired there.

            Now... Use the power of Hover to raise your ship! At first, you may
            not want to move your ship too high or too far... It will be
            difficult at first, but that is to be expected... After all, this is
            your first flight. But your quest should not demand much more of
            you... Now, be confident and set sail!

            All of Contigo is watching... Show them your power, and make your
            vessel fly!



* - Before doing so:

Hamma     :{S} Use your Psynergy to raise your ship and fly over reefs.

           {M} Travel safely, Ivan... The world depends on you.



* - After setting off and flying over a reef:

Ivan      : We did it! The ship took off without a hitch!

Garet     : Yeah, but... shouldn't it be flying a little higher than this?

Mia       : Hamma told us that we wouldn't be able to fly very high until we
            were more familiar with Hover.

Isaac     : Let's see how far we can take this thing!

Jenna     : Sheba, what's wrong? You don't look happy...

Sheba     : Do you remember on Idejima, when I told you I had my own reasons for
            joining your quest?

Kraden    : You were so secretive! Are you going to tell us now?

Sheba     : ... ...

Jenna     : You've gone quiet again... It's OK... You don't have to tell us
            if you're not ready yet.

Sheba     : I thought that if I went to Jupiter Lighthouse, I would learn
            who I was...

Isaac     : I remember the people of Lalivero talking about how Sheba fell from
            the sky...

Sheba     : All my life, I've been looking for the answer... Where was I born,
            and why was I abandoned?

Piers     : You knew Felix was going to Jupiter Lighthouse eventually, and so
            you went along with him.

Mia       : But you didn't find any answers, did you, Sheba?

Ivan      : I'm sorry, Sheba... I was so excited to find Contigo that I didn't
            consider your feelings.

Garet     : What? Why is everyone so down all of a sudden?

Sheba     : ... ...

Garet     : Faran raised Sheba like his own daughter. He's cared for her
            ever since he first found her!

Sheba     : Yes, that's true, but...

Garet     : But you can never be his real daughter, is that it?

Jenna     : Garet! You don't have to be so blunt about it!

Mia       : No, he's right... I'd want to know my real parents, no matter
            how caring Faran might have been.

Garet     : You think so? If it were me, I doubt it'd bother me at all...

Kraden    : Sheba, you may not know this, but you and I are very similar...

Sheba     : What do you mean?

Kraden    : Well, it's not exactly the same situation, but... I was born in a
            poor village. My memories are hazy, but I still remember it. I was
            only four when Babi took me under his wing. You see, even though
            I was young, I was quite intelligent. Babi had heard about me...

Isaac     : And Babi took you to Tolbi to further your education, to raise you
            as a scholar...

Kraden    : I was separated from my parents so early in life... I've never known
            the comforts of a true home.

Sheba     : Faran has always been like a father to me... I must have been
            very lucky.

Kraden    : I should say so.

Sheba     : Thank you, Kraden... I feel better now...

Kraden    : I'm glad I could help.

            Well, we should be going... Let's hurry on, Felix!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

[001]     :{S} I wonder what's on the other side of the ocean... I should be
               happy where I am, but... Whenever I think about that flying ship,
               I want to leave home, to explore the world!

           {M} I wish I could travel to the end of the sea on that beautiful
               flying ship.

[002]     :{S} I've been watching the skies, hoping I could catch anther glimpse
               of the flying ship.

           {M} Whenever I look at the sky, I think about that flying ship,
               and I want to travel the world.

[003]     :{S} All of our myths and legends have taught us that the sea is a
               dangerous, fearsome power. But on the day the ship left, the sea
               was so calm and romantic looking...

           {M} Everyone in Contigo used to be afraid of the ocean. But now,
               everyone who saw the ship take off sees the sea filled with
               wonder and romance.

[004]     :{S} You're going north? I hear it's always winter in the lands to
               the north, so bundle up!

           {M} I've decided to become... an adventurer! One day, When Ivan and
               his companions return, I will join them on their amazing ship!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'42] ---          [Atteka]           --- [02'42] #$#
#$#$#                    Contigo                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#
$#  House atop hill  #$
#$#$#$#$#$#$#$#$#$#$#$#

Hamma     : Ah, you've returned! What brings you to my new home?

Ivan      : Hamma... You're my sister... Why didn't you tell me sooner?
            Why didn't you tell me when we first met?

Hamma     : You play an important role in all of this. If I'd told you,
            you would have come here too soon.

* - Ivan looks around.

Ivan      : This place is so familiar... I feel like I've lived here my
            whole life.

Hamma     : Look at me, Ivan. You're too sentimental. You would have given up
            your quest to find your true home, and we would all now be lost.

Ivan      : What are you saying, sister?

Hamma     : No, not sister... Do not think of me as your sister until you have
            fulfilled your destiny.

Ivan      : W-Why?

Hamma     : Our world is falling into ruin...

Isaac     : What? Hamma, what do you mean? What's happening?

Kraden    : Look, I don't want to interrupt your reunion or anything, but...
            I couldn't help overhearing you say something about the world
            falling apart. What's up?

Hamma     : Our world requires a delicate balance of elemental forces.
            That balance has been disturbed. Without that balance, one element
            might be lost beneath the others, straining Weyard.

Kraden    : You're talking about Mars Lighthouse, right?

* - Hamma nods.

Ivan      : Isn't Agatio taking care of Mars Lighthouse? Everything should be
            fine soon.

Hamma     : Agatio will not light Mars Lighthouse.

Isaac     : You don't think he can do it?

Hamma     : No. A great power stands ready to oppose them. They lack the power
            to resist that force, and they will fall before it.

Isaac     : But what will happen if Mars Lighthouse isn't lit quickly enough?

Hamma     : Our world will be plunged into ice.

Ivan      : But what would make that happen?

Hamma     : Even I do not know the answer to that question.

* - Kraden thinks for a moment.

Kraden    : Ah... Yes, given the way that the elements interact. I see...

Isaac     : Kraden, you understand?

Kraden    : Well, I'm only guessing... But I think it's a good guess.

Ivan      : Quit fooling around and tell me!

Kraden    : The earth is nurturing and warm. Many creatures are reared in this
            warmth, you see?

-----------------------------------------------------------
     -(Yes)
Ivan      : I follow you...



     -(No)
Ivan      : It's OK, Felix... I don't really get it either, but let's see where
            he's taking this...
-----------------------------------------------------------

Kraden    : Now, think about the ocean. It is a cold place, is it not?

-----------------------------------------------------------
     -(Yes)
Isaac     : Yeah, it is awfully cold...


     -(No)
Isaac     : I don't know what point he's trying to make, but I have to agree
            that the ocean's cold...
-----------------------------------------------------------

Kraden    : Both lighthouses were lit, and a balance was reached. But with only
            the lighthouse of wind lit, the balance has been disturbed.

Ivan      : I get it... Wind cools things down, but it can't heat them up...

Kraden    : When you burn your hand on something hot, you blow on it to cool it
            off, don't you?

Isaac     : Right, yeah... I've always done that without thinking about it,
            but it makes sense, huh?

Hamma     : When Mercury Lighthouse was lit, this didn't happen, though.
            I wonder why...

Kraden    : Water cannot cool things as swiftly as wind, perhaps. Or maybe
            the combined power of water and wind is cooling things down even
            faster...

Isaac     : If what Hamma's saying is true, we'd better get moving again, Felix.

Ivan      : I got too worked up about seeing my sister... Sorry.

Hamma     : It's all right. I'm happy that you cared so much...

Kraden    : All right, Felix! Let's head to Mars Lighthouse!


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} I got stuck doing chores at home, and I had to miss watching the
               ship take off.

           {M} I didn't get to see the ship take off, but I'm not really all
               that disappointed. I heard that it wasn't that impressive anyway.

[002]     :{S} I've seen a lot of weird things lately... Maybe I ought to
               listen to those legends.

           {M} Wait... The city of Anemos flew up into the sky? All right,
               that's just stupid!

[003]     :{S} It wasn't what I expected, but seeing the ship take off was
               still amazing.

           {M} All of those legends did nothing but build up people's
               expectations. I'm just glad to know that the ship flew at all...

[004]     :{S} Everyone's been going on about how amazing it was to watch the
               ship fly... I wish I could have been there to see it. I guess it
               was pretty moving.

           {M} Some people were talking about how the ship wasn't really that
               impressive. Why would they say that? A ship actually flew
               through the air!

[005]     :{S} It must be so exciting to travel around the world in a flying
               ship.

           {M} I couldn't fly in the air, that's for sure. I get motion sickness
               just walking around.

[006]     :{S} If a ship can rise up from the sea, why can't a city rise up
               from the ground?

           {M} The city of the Anemos rose up into the sky and became what we
               now call the Moon.

[007]     :{S} I saw the ship fly! Now I want to see what it looks like from
               on board!

           {M} The ship looked like it had a few problems trying to get off
               the ground. I guess it was because the crew had never made a
               ship fly before.

[008]     :{S} Hamma was telling us that the world is a dangerous place.
               I wonder what she meant. I think she's concerned about the
               elemental balance...

           {M} I heard that the world could freeze over soon... I hope Ivan
               does what he needs to.





   [ Buildings ]
[009]     :{S} I guess the lighthouse was lit because Ivan and Hamma finally
               returned to Contigo.

           {M} Hamma will stay with us, but Ivan is leaving again. The power
               of Anemos must be a terribly responsibility for such a young boy.

[010]     :{S} Ivan doesn't remember his mother, because he was taken away at
               such an early age. But I saw her eyes the day he went away.
               Tears welled up, and she couldn't stop crying.

           {M} I wonder how Ivan feels now that he knows what happened to his
               mother. Hamma seems so closed up... I wonder if she'll talk to
               him about it...

[011]     :{S} From the look on Ivan's face, whatever happened at the lighthouse
               must have been bad.

           {M} Someday, I'm gonna fight Ivan, and then I'll be the legendary
               hero of Contigo!

-----

[Item]    :{S} It's always such a letdown when you finish off a major task
               like fulfilling an ancient prophecy.

           {M} Now that the wings are done, everyone who came to help out
               has left the village...

[012]     :{S} Brrr... Brrr... It's been really cold since the lighthouse beacon
               was lit!

           {M} Jupiter Lighthouse has been called the beacon of wind... Is that
               why it's so windy and cold?

[013]     :{S} Winter just ended, but it keeps getting colder. What's going on?

           {M} Hamma says that if Ivan fails, it will continue to get colder
               and colder.

-----

Innkeeper1:{S} All of our work and all of our celebration are finally at an end.
               I think Contigo is going to go back to being a very quiet place.

           {M} It's going to be a little slow for a while, but I can't really
               complain, now, can I? After all, I saw the lighthouse shining
               again, and I actually saw a flying ship!

Innkeeper2:{S} The inn has become so lonely now that everyone's gone home.
               We should have an annual festival in Contigo to commemorate
               this day!

           {M} The inn is bound to be slow for a little while, but business will
               pick up again. Everyone who witnessed the events of the past few
               days will want to come back.

Chef      :{S} Now's my chance to experiment with some exciting new dishes!
               What should I make first...

           {M} Seeing that ship take flight was the most moving thing I've
               ever seen... I think I'll have to preserve it for future
               generations... in cake form!

Employee  :{S} Gosh... We were so busy, and now we're totally empty.
               I don't know what to do!

           {M} What are we going to do? All the excitement is over, and I'm
               going to be bored! I was starting to like all the attention
               I was getting!

* - [014] through [017] have left.

-----

G. Healer :{S} It was a miracle that made all of the legends of the Anemos
               come true... I'm not entirely sure, but I think my faith has
               been restored!

           {M} It was a shock to see such a huge ship float. It made me realize
               how small we all truly are.

-----

[018]     :{S} The lighthouse has been lit, and we've made a ship fly...
               Our legends are coming to life!

           {M} Ivan has the power of prophecy, and I'll bet he didn't
               see this coming!

[019]     :{S} It's up to the people of Contigo to live up to our own legends.

           {M} Now that I think about it, this very day will probably become
               a legend, too!

[020]     :{S} Mom and Dad have been walking around in a daze since the ship
               took off.

           {M} It's time to fix those drafts now that the wings are done!

Ahri      :{S} <game>:  The baby's forehead is furrowed, like it's thinking.

                 * - A small gust of wind is summoned.

               Ahri  :  Goo go. Gaa gaa... Waaa!
               [018] :  Drafts! I hate drafts! This stupid house is always cold!
               [019] :  Now that we've finished the wings, we should fix
                        the house.

           {M} Goo... It's getting colder... Gagoo... I want a blanket...

-----

Hamma     :{S} No matter what happens, you must light the beacon on Mars
               Lighthouse! I hope for your safe return.

           {M} My heart is with you always, Ivan. Never forget that.





   [ Anemos Sanctum  -  Exterior ]
[021]     :{S} I can't believe that a ship just like the one in the geoglyph
               actually exists. And I think everyone's proud to have helped
               to make the legends come true!

           {M} That flying ship looked so fake... It didn't look anything like
               I'd imagined it would. Nobody else was complaining, but they
               don't pay attention to the details, like I do.

* - [022] through [026] have left.



* - Closer to the sanctum:

[027]     :{S} I'm convinced there's something hidden in the Sanctum.
               I just know it says something about it on the wall.

           {M} All right, so we've followed the instructions on the wall,
               and we STILL can't get in!

[028]     :{S} All the amazing things we've seen and done, all the legends
               that have come true... And I still can't get into the secret
               chambers of Anemos Sanctum!!!

           {M} If you tap on the floor or walls, you can hear a hallow sort
               of sound. I'm convinced that there's nothing on the other side!

[029]     :{S} Look closely at the geoglyph. Study it, examine its details...
               The more you stare at it, the more you recognize the greatness
               of the Anemos.

           {M} We all came together and worked to make the legends come true...
               It's really inspiring... Actually, it gives me goosebumps...
               [sic] Brrrr.

[030]     :{S} He's an odd boy, but I'm glad that Ivan has returned to Contigo
               at last...

           {M} Ivan was supposed to be a great, manly hero... I guess not all
               the legends came true...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'43] ---     [Gondowan & Angara]     --- [02'43] #$#
#$#$#                Gondowan Settlment               #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

Man       :{S} Don't tell me, you're here to solve the riddle of the rock!
                 * - He's referring to Magma Rock.

               --------------------------------------------
                    -(Yes)
               I don't want to scare you but, I think you should reconsider.
               Even the warriors who survive to make it back do so by the
               skin of their teeth.



                    -(No)
               Just passing through? Here's some advice for you: Steer clear of
               the mountain. I don't know what kind of treasure's up there,
               but it's not worth your life.
               --------------------------------------------

           {M} The mountain is called Magma Rock, and it's cursed... No one's
               supposed to go up there.

Woman     :{S} I hear Kibombo has finally chosen a new witch doctor.
               Maybe now, they'll calm down and not be so aggressive...

           {M} We're lucky the river floods over every season. That's what
               keeps the Kibombo away. We were fine this year, though.
               They still hadn't chosen a new witch doctor, so they stayed put.

Boy       :{S} There was a giant explosion on the rock the other night...
               I couldn't get back to sleep at all.

           {M} The explosions within Magma Rock are called magma balls. They're
               formed natural near the mouth of the volcano. Scary, huh?


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'44] ---          [Gondowan]         --- [02'44] #$#
#$#$#                    Magma Rock                   #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$
$#  Final area  #$
#$#$#$#$#$#$#$#$#$

<game>    : Felix checked the tablet... There's something etched on it.

            Wielder off Flame's [sic] strength, Lay [sic] your hands upon
            this stone... If th'art worthy, I will grant thee the power to
            Blaze [sic] with fire.

Jenna     : Flame's strength? Hey, that must mean it's finally my turn!

* - Felix nods.

<game>    : Jenna received the fire Psynergy Blaze.

* - It rises into the air, as does Jenna as the tablet's energy surrounds her.

<game>    : Jenna learned Blaze.


#$#$#$#$#$#$#$#$#$#$#$#
$#  An earlier room  #$
#$#$#$#$#$#$#$#$#$#$#$#

* - Felix's group can now reach a stone spewed out from the lava.

<game>    : There's something burning like an ember within the stone.
            Do you want to retrieve it?

* - Upon selecting "Yes":

<game>    : Felix got a Magma Ball.

* - The stone freezes.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'45] ---           [Angara]          --- [02'45] #$#
#$#$#                       Loho                      #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Welcome to Loho! We've been excavating all sorts of ores to get
               the metals inside! The metal used to make the ancient ruins might
               have come from these very rocks!

           {M} We only settled here a short while ago, and we found all those
               ruins here... We named our settlement Loho, but I've been
               wondering what it used to be called...

[002]     :{S} We have a lot of important excavations going on, but we're also
               doing some mining.

           {M} Everyone in Loho sure loves digging. It's not all mining...
               We're interested in history, too.

[003]     :{S} Once we can get through the wall, there will be enough work for
               everyone in town!

           {M} If you live in Loho and you don't dig, you're not one of us...
               You don't belong.

[004]     :{S} If you want to be a miner, you have to know the earth...
               You have to know where to dig.

           {M} Real experts can find the best spots to dig in a single glance.

[005]     :{S} I haven't found anything worth the trouble of digging up.
               It's time to find another spot.

           {M} I think I'm starting to lose my touch... None of my digs
               has [sic] produced anything at all.

[006]     :{S} This is the spot. A good hole here, and you'll dig up some
               fantastic ore...

           {M} Once you've been mining for a while, it's like the ground says
               to you, "Hey! Hey, you! Dig here!"

[007]     :{S} That wall seems indestructible! We've been trying to dig through
               it for a while now. We're pretty sure there are some valuable
               metals and minerals on the other side.

           {M} If we can't get through that wall, we'll never know what's on the
               other side...

[008]     :{S} Some of the miners found an ancient cannon when they were
               digging a while back. If you want to see it, it's over by
               the wall near the ruins.

           {M} All we need is a way to use the cannon to knock down the wall...
               That would be great. Then, we could get rid of the cannon
               altogether. We don't have any use for weapons here.

* - By the cannon and the wall blocking the ruins:

[009]     :{S} Did you want this cannon?

               --------------------------------------------
                    -(Yes)
               Well, if you can figure out a way to break down this wall,
               it's all yours.



                    -(No)
               All we really want to do is break down that wall right there...
               If we can find someone to do that, we'll give 'im the cannon.
               --------------------------------------------

           {M} All right, we figured out that you need to put a steel ball
               in there, but what do you do then? You stick a ball in there
               just fine, but I don't think it'll be coming out on its own...

[010]     :{S} We brought the cannon up here to break down the old wall, but
               we don't have any ammunition...

           {M} Cannons are so heavy! Why did we bring it up here if we're not
               going to use it?

[011]     :{S} You can put metal balls in the barrel, but what makes them
               come out again? It looks a little like an old ballista, but
               the way it works is totally different.

           {M} What idiot said that we'd be able to destroy that wall if we
               dragged the cannon up here?





   [ Buildings ]
* - One counter is designated to the inn, while the other is for the
    weapon/armor/item shop. Both are operated by [012].

[012]     :{S} Commerce really took off when we started this mining colony in
               Loho. You just have to know how to make the most out of what's
               around you...

           {M} Whenever someone strikes gold, we get a rush of visitors, and
               business just takes off.

Sign      :{O} It reads "People staying at the inn can check in at the counter.
               [sic]

-----

Healer    :{S} If you're only here for the cannon, you can forget about it.

           {M} If the cannon is truly as powerful as the people say, we can't
               just give it away.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  By the cannon and the wall  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

<game>    : It looks like it's empty.

* - Felix inserts the Magma Ball and fires the cannon. It obliterates the wall.

[011]     : Is everyone all right?

[009]     : Did you hear that? That sound was incredible!

* - [010] looks at Felix.

[010]     : What do you think you're doing, making all that noise?

* - [011] looks behind himself, at the wall.

[011]     : Hey, look at that!

* - [009] and [010] look at [011].

[011]     : What are you looking at? It wasn't me! It was the wall!
            Look at the wall!

* - They do so.

[009]     : The wall... It's gone!

[010]     : Well, it's mostly gone, yeah... You can get through to the other
            side now!

* - [011] turns to Felix again.

[011]     : How did you manage to break down the wall?

[009]     : Ah, never mind... What's important here is that we can dig on the
            other side of the wall now!

[010]     : Yeah, who cares how it happened? We can dig again!

[011]     : Well, you did what we asked, so the cannon's all yours!

[010]     : Hmmm... It's gonna be tough carrying that thing around...

[011]     : Those guys are new in town, aren't they? Do you think they came from
            Atteka or Hesperia?

[009]     : I don't know, but I can tell you they came by boat...

* - [010] enters a nearby building and heads to the roof.

[010]     : Yeah, I saw one anchored off the beach!

[011]     : That boat's yours, isn't it?

-----------------------------------------------------------
     -(Yes)
[011]     : Well, why don't you let us get that cannon onto your boat for you,
            hm?



     -(No)
[011]     : Look, the only way to get here is by boat, and I see a boat
            right there! Don't tell me it's not yours!

            I don't know why I'm offering, but why don't you let us put it
            aboard your boat for you?
-----------------------------------------------------------

* - The three men carry it to the ship. Upon exiting Loho:

[009]     : You don't have anything to worry about. We got the cannon onto
            your ship with no problems.

[010]     : Now, we're going to start excavating the ground north of the wall
            you knocked a hole in.

* - They return to Loho.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Was that you that fired the cannon earlier? If you know how to
               use the cannon, you'll be able to sail in the Northern Sea.

           {M} That cannon can shatter any of the ice floes that keep the ships
               from trying to sail north.

[002]     :{S} That cannon sure gives off a serious bang! Everyone in Loho
               was totally shocked!

           {M} That cannon was really loud... Imagine if you were standing
               right next to it!

[003]     :{S} I've gotta go stake myself a claim on the other side of the wall!
               We've found some valuable metals out here; think what we'll find
               inside!

           {M} I just need to stick to this one spot. Eventually, I'll dig up
               something valuable!

[004]     :{S} You probably only want the cannon so that you can force other
               people to obey your will.

           {M} These guys must be really busy, sailing around all over the world
               like that.

[005]     :{S} I think we've dug up all that there is out here. I'm going to
               find myself a new spot inside the wall.

           {M} Even at my age, I just love the feel of digging into the earth.
               Still, when you're not digging up anything good, you start to
               feel a little frustrated.

[006]     :{S} Ah, so you have a quest to fulfill, do you? I guess that means
               you're leaving soon. When I was your age, I used to love the life
               of danger and adventure.

           {M} When they get wherever they're going, they'll tell the world that
               Loho's got the best metal!

[007]     :{S} When we found that cannon at the dig, I thought it was just
               useless junk. If you know how to use it, it can be a pretty
               potent tool!

           {M} I don't think we should have given the cannon away. We should
               have sold it to Tolbi.

[008]     :  * - Before being informed that the cannon was attached:

           {S} I saw some of the village men carrying the cannon out of town...

           {M} I don't know where they were taking it, but I'm glad the cannon's
               gone... I think they just wanted to make some room for us to
               begin mining again.


             * - After being informed that the cannon was attached:

           {S} Now that the wall's been breached, we can get on with the mining!
               Good work!

           {M} We don't have anything to worry about, now that we can start
               mining in the ruins...

* - Past the destroyed wall:

[009]     :{S} Ha ha ha! I've got this giddy feeling, like I'm going to dig up
               a mountain of money! Whenever I get this feeling, I always dig
               out a fortune!

           {M} It doesn't matter how old you get... Nothing beats the feeling
               of digging a new mine.

[010]     :{S} I keep digging up little, tiny gems and metals... But when I get
               enough, I'll be rich! After all, when you pile up enough dirt,
               you eventually make a mighty mountain!

           {M} I've hit the mother lode! I keep on digging, and I keep
               getting more and more!

[011]     :{S} Thanks for opening up the wall... There are some great places to
               dig out here!

           {M} I only just started digging, and I'm already wealthy beyond my
               wildest dreams!





   [ Buildings ]
[012]     :{S} I hear you took our cannon in exchange for knocking down that
               ancient wall. I'll be sorry to see it go... That cannon was going
               to make Loho famous.

           {M} Now, we don't have a symbol anymore... We just have a town full
               of holes.

-----

Healer    :{S} You've acquired a splendid cannon. Just be sure that you use it
               wisely.

           {M} It worries me to no end, thinking of the evils one could do
               with that cannon.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'46] ---     [Great Western Sea]     --- [02'46] #$#
#$#$#                 Northern Reaches                #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Without the cannon  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$

Jenna     : Kraden, come look at this... There's a huge ice wall blocking our
            path...

Kraden    : Hm... If we can't do something about that wall, we're not going
            any farther, Felix.


#$#$#$#$#$#$#$#$#$#$#$#
$#  With the cannon  #$
#$#$#$#$#$#$#$#$#$#$#$#

Jenna     : Kraden, come look at this... There's a huge ice wall blocking our
            path...

Kraden    : Nothing to worry about, Jenna. We'll just have to use that cannon
            we got in Loho!

Sheba     : That's right! If the cannon can blast away a stone wall, think what
            it'll do to ice!

Kraden    : Felix, take us between those two blocks of ice for shelter when you
            fire the cannon.

* - He does so.

Piers     : We should be safe if we fire from this distance.

Kraden    : OK, here we go! Felix, aim right at the ice wall and fire when
            ready!

-----------------------------------------------------------
     -(Yes)
Kraden    : Fire the Magma Ball!

* - They do so, demolishing the ice wall.

Jenna     : Great! We did it! We can keep going now!

Kraden    : All right, let's head for the Northern Seas.

Sheba     : Let's go!



     -(No)
Kraden    : What? You're not ready yet? Take your time and get into position
            then... But as soon as you're ready, fire!
-----------------------------------------------------------


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'47] ---     [Northern Reaches]      --- [02'47] #$#
#$#$#                      Prox                       #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - A heavy snowstorm has befallen the village and the surrounding region.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  North end of Prox  -  By house  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - A man comes out of the building and speaks to a woman.

Man       : They're not here...

Woman     : Strange... We looked all over the village, and we can't find
            any trace of them at all...

Man       : Everyone says they've practically vanished without a trace...
            It's so strange.

Woman     : You don't think they...

Man       : They wouldn't have done to the lighthouse...

Woman     : Yeah, you're probably right.

Man       : Puelle's going to be upset that we didn't follow his order to
            free them, though.

Woman     : He was clear about it, too... "When Felix returns to Prox,
            set his parents free."





* - Social Script:

Man       :{S} Puelle ordered me to set your parents free. That's why I'm here
               now... The only thing is, no one else is here... I don't know
               where your parents went!

           {M} Puelle wanted to set Felix's parents free before Prox was
               destroyed... But if we can't find them, how can we set them free?

Woman     :{S} Felix took the trouble of coming back for his parents, and now
               they're just gone?

           {M} I can't think of anywhere else Felix's parents might have gone!


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  North end of Prox  -  By exit  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Puelle (Prox's chieftain), the elder and three men and woman have gathered.

Puelle    : We can't wait for Agatio and his men any longer... If we wait
            much longer, this wind and snow will make it impossible to reach
            the lighthouse. I'm going to the lighthouse... Will any of you
            come with me?

Man 1     : Puelle, I can't let you go on your own...

Man 2     : If something were to happen to you, who would lead our village?

Woman  1  : Please, you must let us go in your stead.

Puelle    : How can you expect to accomplish what Agatio and Karst could not?

Woman 2   : They may have been more powerful than any of us, but we can't just
            stand by!

Man 3     : They're not coming back, just like Saturos...You have to let us try.

Elder     : I can't. I can't allow it.

Puelle    : Listen to your elder... He speaks wisely.

Elder     : I'm speaking to you too, Puelle. If Agatio and Karst cannot do
            the task, how can you, a single man, hope to do it?

Puelle    : What are you saying? If we stand around debating, our town is
            doomed for certain!

Elder     : We can't risk sacrificing any more lives.

Puelle    : So, we must sit here and wait for a miracle to come.





* - Social Script:

Man 1     :{S} Is that you, Felix? When did you return to Prox? You should take
               your parents back to Vale, so they can at least die in their
               hometown.

           {M} If the lighthouse isn't lit soon, Prox is doomed... I need to get
               out of here!

Man 2     :{S} If we were better Adepts, we could try to enter the lighthouse
               ourselves...

           {M} Neither our elder nor Puelle will tell us what's going on at the
               lighthouse... We are we training so much? A lighthouse shouldn't
               pose that much danger...

Man 3     :{S} I feel so helpless... Agatio has not returned, and the light-
               house beacon remains unlit.

           {M} Puelle is stronger than any of us, and there is nothing he can do
               to save us... But if we don't take some kind of action, Prox will
               be destroyed for sure...

Woman 1   :{S} All we can do now is wait for Agatio and his men to return...
               But no honest soldier can sit idly by while others do all of
               the work.

           {M} If they didn't light the beacon, and they didn't return home,
               Agatio's team must have failed.

Woman 2   :{S} Our Psynergy feels weak... I can sense it inside me. The water,
               earth, and wind lighthouses have been lit, and fire alone
               remains dark.

           {M} If only my fire Psynergy weren't so weak now, I might be able
               to help...

Woman 3   :{S} Puelle promised that he would return our hostages to Vale.
               If you don't believe me, ask him yourself.

           {M} Puelle never intended to take hostages. He wanted the people of
               Vale to be returned safely. Saturos insisted that we hold on to
               them for our safety, but Puelle disagreed.





* - Upon approaching the elder and Puelle:

Elder     : You... Felix, it's you...

Puelle    : I'd heard that you had returned to us... You look so much stronger
            than when you left.

Elder     : It seems he has brought some allies with him.

Kraden    : Yes... I am Kraden.

Isaac     : My name is Isaac.

Elder     : Isaac... Isn't that...

Puelle    : That is the name of the one Agatio said had killed Saturos and
            Menardi.

Kradem    : Isaac, stop that...

            You are correct, but Isaac had reasons for fighting them.
            Saturos and Menardi had invaded Vale, stolen its sacred treasure,
            triggered a volcano... You cannot blame Isaac for pursuing them
            and fighting to regain what they had stolen.

Isaac     : We only wanted to stop them... We didn't think they'd fight us to
            the death. They flung themselves into the opening of Venus Light-
            house's beacon...

Man 1     : Did... Saturos and Menardi put up a good fight?

Woman 1   : I'll bet you thought you didn't stand a chance against them, huh?
            You were probably really tense the whole time...

Woman 2   : Saturos and Menardi had a job to do... That was all.

Man 3     : If I'd been in your shoes, I'd have done the same thing...
            I can't blame you.

Woman 3   : And in the end, you were stronger than they were... You should be
            proud of that.

Elder     : I am sad that they lost their lives in their quest, but there was
            no avoiding it.

Puelle    : What has happened cannot be undone. We should cooperate to find
            a way to save Weyard.

Kraden    : We understand that Agatio and Karst have made for Mars Lighthouse
            and not returned.

Elder     : Then all that remains for us is to wait until Gaia Falls carries us
            all to our doom.

Isaac     : It seems that Mars Lighthouse is as dangerous as all the rest.

Puelle    : We have only a few soldiers remaining, and none who can make the
            climb to the aerie.

Kraden    : Only Saturos and perhaps Agatio were strong enough to reach the
            top...

Elder     : And none of them can help us now.

Isaac     : You think we can do it?

-----------------------------------------------------------
     -(Yes)
Isaac     : I agree, Felix...



     -(No)
Isaac     : Felix, what are you thinking?
-----------------------------------------------------------

Kraden    : We've climbed three lighthouses already... What's one more?
            Let's go to Mars Lighthouse!

Puelle    : They've proven themselves strong enough! I say we trust in Felix
            to do this!

Elder     : This is an unexpected turn of events, but yes, I think you can
            light the lighthouse.

Kraden    : Off to Mars Lighthouse! Let's go, Felix! Come on, Isaac!

Puelle    : There is one thing that I don't want you to forget. In order to
            light the beacon at Mars Lighthouse, you will need to have the
            Mars Star.

Elder     : Ah! And Agatio and Karst have the Mars Star now!

Puelle    : You must find Agatio and Karst, and you must take the Mars Star
            from them.

Elder     : Thanks for your help. The future of Weyard rests in your hands.





* - Social Script:

Elder     :{S} Felix, you are the only hope left to us now. Good luck.

           {M} If they were strong enough to defeat Saturos and Menardi,
               perhaps they can do the job...

Puelle    :{S} You must find Karst, get the Mars Star, and light the lighthouse.

           {M} If this doesn't work, we're all finished... Prox, Weyard, even
               Vale... All will be lost...

* - The others' script has not changed.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

   [ Outside ]
[001]     :{S} Felix! Welcome back to Prox! It looks like only Mars Lighthouse
               still needs lighting... Agatio didn't think you'd be coming back
               here, so I'm a little surprised to see you...

           {M} Agatio and Karst told me that Felix ran away because their quest
               was too dangerous.

[002]     :{S} Once the final lighthouse is lit, the winds should weaken.
               They keep getting stronger, though!

           {M} If this weather continues much longer, we'll all be buried under
               snow in no time.

[003]     :{S} Agatio and Karst left for Mars Lighthouse a little while ago...

           {M} Agatio and Karst are the strongest fighters in Prox... That's why
               we sent them. But I'm worried... They've been gone for a while
               now, and the lighthouse still remains dark.

[004]     :{S} Felix, you're back? And you learned how to use Psynergy?
               I can sense the power inside of you... It's strong!

           {M} If Felix could become an Adept so quickly, so can I!

[005]     :{S} I'm glad you made it back safely... The ice is making it very
               difficult for anyone to sail here.

           {M} Ever since Agatio returned form Jupiter Lighthouse, the winds
               have been stronger than ever...

[006]     :{S} I've been keeping a close eye on the northern skies... Once I see
               a bright flash in the distance, I'll know the last beacon has
               been lit.

           {M} Everything is supposed to return to normal once Mars Lighthouse
               is lit again.

[007]     :{S} We're used to the cold up here in Prox, but lately, it seems to
               be getting worse.

           {M} It gets cold around here, but this is the first time I've ever
               seen snow pile up on the river. What if Agatio doesn't reach
               Mars Lighthouse in time?

[008]     :{S} Have you seen Saturos or Menardi? People have been saying that
               they were killed...

           {M} I can't believe anyone could have beaten Saturos and Menardi...





   [ Buildings ]
Innkeeper1:{S} Felix, your parents have gone away... They were very worried
               about you.

           {M} Felix's parents were worried about him when they heard Saturos
               was dead.

Innkeeper2:{S} Your mother knows that you're strong and healthy, so I'm sure
               she's very relieved...

           {M} Felix's parents were so worried about him that they were
               wasting away...

-----

[009]     :{S} The rift at Mars Lighthouse gets wider every day. If we don't
               find a way to stop it, I think it's going to devour Prox
               entirely!

           {M} I thought Prox would be here forever, but now, it looks like
               it might be destroyed!

[010]     :{S} Our chieftain told me that the rift is growing larger by the day,
               just like Gaia Falls is. We'd better light the Mars beacon soon,
               or Prox is finished...

           {M} Nobody believed that the rift would go as far south as Prox...
               They all thought Puelle was being melodramatic... But no one
               thinks that anymore...

[011]     :{S} Not too long ago, I climbed the mountains to the north to look
               at the rift. It was huge!

           {M} The northern rift has gotten so big that I couldn't see the
               other side...

-----

[012]     :{S} We sent emissaries to Vale to tell them that Weyard was dying.
               But they wouldn't listen to us... If only they had listened
               to us...

           {M} At least the journey wasn't for nothing. We learned that Sol
               Sanctum held a hidden secret.

[013]     :{S} Vale's elders were stubborn... They refused to listen to us,
               and they drove us out by force. We had gone in peace, hoping to
               convince them of the plight our world faces...

           {M} Three years ago, we sent our finest to Sol Sanctum. All but two
               were killed in a trap. The people of Vale couldn't possibly
               understand how dire our need was...

-----

[014]     :{S} The people Saturos rescued from the storm in Vale should be
               waiting in their room. Once Mars Lighthouse has been lit,
               they'll be free to return home.

           {M} Mars is the last lighthouse that needs to be rekindled.
               Once that's been taken care of, the people of Vale will be
               set free.

[015]     :{S} Puelle, our chieftain, grew worried about Agatio and Karst.
               He's gone to the northern edge of town to wait for them.

           {M} Now that Saturos and his team are gone, Agatio is the last of our
               warriors. If something happens to them, our final hope is lost.

[016]     :{S} Don't forget, Felix, your mother and father are staying in the
               north end of Prox.

           {M} Saturos used Felix's parents to force Felix to follow him on
               his mission. We've fallen on hard times when we need to coerce
               people to join our cause.

-----

G. Healer :{S} I hear Agatio and Karst have gone to Mars Lighthouse...
               What if their actions only cause more turmoil? How can we
               be sure they're right?

           {M} These catastrophes are the result of the lighthouse beacons
               being rekindled. This snow, this wind, it all started after
               Jupiter Lighthouse was lit.

-----

[Item]    :{S} You go away for a little while, and you come back a strong and
               mighty warrior! I'm so proud of you!

           {M} Felix looks so confident, so bold...You can see it in his eyes...

[017]     :{S} When you left Prox, you were so young that you could barely
               lift a sword! Now, look at you! You could handle any weapon
               with ease!

           {M} What has he gone through that he's become so strong in such a
               short time?

-----

[018]     :{S} If Mars Lighthouse's fires are not rekindled, Prox will be
               destroyed, but that's not all... Eventually, Gaia Falls will
               continue to erode, finally devouring all of Weyard.

           {M} I think it's too late for us already... But if they light the
               fires, we'll be ready for them.

[019]     :{S} No one thought about our needs when they extinguished the great
               lighthouses... Now, because of them, our great land is dying,
               crumbling away at the edges...

           {M} To think that we all once had the power to control nature...
               What fools we were.

[020]     :{S} Prox originally flourished because concerned Adepts lit the fires
               of the Mars Lighthouse. Now, we, the people of the northern
               flame, have been forgotten by the outside world.

           {M} When the lighthouses were all extinguished, every great
               civilization fades away...

-----
* - Igloo:

[021]     :{S} Those poor children. They don't understand what's about to
               happen to us... I just want them to be happy in the short time
               left to us.

           {M} I can't bring myself to tell them what's going to happen to us...
               Oh, please, save us...

[022]     :{S} The wind is so cold and bitter that we decided to hide out
               inside our igloo...

           {M} Mama and Papa have been acting really strange lately...
               They seem so sad. Whenever I ask them what's wrong, they tell me
               to go outside and play some more.

[023]     :{S} My parents told me that it would do me some good to get some
               fresh air, but I'm freezing!

           {M} I always catch a cold when I'm outside in weather like this...
               Does Mom want me to get sick?

[024]     :{S} Felix, you like igloos, right?

               --------------------------------------------
                    -(Yes)
               You WOULD say that... You come from somewhere warm and sunny!
               We didn't have anything to play with, so we just decided to
               make this thing...



                    -(No)
               Well, if you don't like cold things, you're in the wrong place!
               We just built this so that we'd have something to do to keep us
               warm...
               --------------------------------------------

           {M} I hate igloos, but at least it's protecting us from the wind...


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'48] ---     [Northern Reaches]      --- [02'48] #$#
#$#$#                Mars Lighthouse                  #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Room with Flame Dragons  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Felix's group eventually encounters two Flame Dragons frozen in ice.
    After breaking the ice and felling the beasts, they revert to their
    original forms: Agatio and Karst.

Agatio    : Why... Why am I lying here? Wait, I think I remember...
            We were going to light the beacon...

Karst     : But the lighthouse was frozen. We wandered lost inside, trying to
            find the aerie... We must hurry... If we delay, Prox is destroyed.

Agatio    : It's no use... I'm absolutely drained... I can't even stand.

Karst     : And the cold... Why am I so cold? We of the Fire Clan are meant
            to be immune to the cold...

Agatio    : I feel the cold too, Karst... I... I'm afraid we're going to die
            up here...

Karst     : I can feel it now... The long, dark sleep creeping into my soul...

Agatio    : Wait... I think I remember... The eye... It told us that we lack
            the will to go any farther...

Karst     : The eye... I remember now... I felt its gaze pierce me to the core,
            then all went black...

Agatio    : That's right... And I remember fighting against Felix...

Karst     : I do, too... Was it a dream? An illusion?

* - Agatio notices Felix's presence.

Agatio    : Felix? Is that you?

-----------------------------------------------------------
     -(Yes)
Agatio    : Amazing... Then our luck hasn't entirely run out yet...



     -(No)
Agatio    : How can you play games with us like this? Regardless, it's amazing
            that you're here... It means our luck hasn't entirely run out yet...
-----------------------------------------------------------

Agatio    : Felix, you must complete our quest... Please... You have to light
            the beacon...

Karst     : We can't even stand... We're in no condition to go on.
            Light the beacon for us... Please.

Agatio    : You'll need the Mars Star. Go on... Take it.

Karst     : Please hurry... If I can just see the light of the beacon, I'll know
            that I haven't died in vain.

Agatio    : We're counting on you...




Agatio    :{S} It's too late for us now... Hurry, light the beacon.

           {M} I'm so tired... A fog is rising before my eyes... No!
               Can't die until the beacon... is lit...

Karst     :{S} Your hands... so warm... People have such warm hands... I had
               forgotten...

           {M} I'm so cold, colder than I ever thought possible... All because
               Mars Lighthouse remains unlit... I have to stay alive...
               long enough to see its light...



* - After taking the Mars Star, the northern dragon statue speaks.

Dragon    : You who holds the star, open your heart and listen...
            If you wish to reach the heavens, give your star to me.

* - Placing the Mars Star in the dragon's mouth causes the entire lighthouse
    to become warmer, and some rooms to partially fill with lava.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Room of four spirits  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - The spirits (fish, human, bird and dragon) are drawn on the walls.

Dragon    : If you do not hold the star, you shall not ascend to the heavens...
            Begone!

* - There are inscriptions next to the drawings:

Fish      : Fish... With cold courage, they ruled the water.
Human     : Mankind... With the power of wisdom, the ruled the earth.
Bird      : Bird... On the wings of truth, they ruled the winds.
Dragon    : Dragons... Burning with might, they ruled the fires.



* - After acquiring the Mars Star:

Dragon    : You who holds the star, open your heart and listen...
            If you wish to scale the heavens, set the four spirits aflame!

* - As the drawings of the spirits are approached, doors appear, each leading
    to a tower.

    Atop the towers are torches on which Blaze must be used to blow fire onto
    the spirit drawings at those locations. This causes the claw-shaped torches
    in front of the dragon statue to become lit. With all of them set ablaze,
    the dragon statue speaks again.

Dragon    : You have proven your worth! The heavens await you!

* - A circle appears on the ground. Using Teleport on it leads to the aerie.


#$#$#$#$#$#$#
$#  Aerie  #$
#$#$#$#$#$#$#

?????     : Betrayers, you have arrived!

Garet     : Who said that!?

Mia       : The wind's too strong! I can't see anything!

Sheba     : I heard it too, but I don't see anyone else up here!

Piers     : Felix! Quick! Cast the Mars Star in before anything has a chance to
            stop us!

* - Felix approaches the beacon, but a force pushed him back.

?????     : So, you are still intent on lighting the beacon of Mars Lighthouse?

Isaac     : Who said that!?

?????     : Have you forgotten me so soon, Isaac? And you, Garet?

Ivan      : It seems to know you, Isaac... Do you have any idea what it is?

* - Isaac and Garet shake their heads.

?????     : Then search your heart, boy!

Kraden    : That voice...

* - The Wise One, a floating stone with a single eye, appears.

Garet     : It's... the Wise One!

Kraden    : Isaac, since when are you on a first-name basis with the Wise One?

Jenna     : It must have been... Isaac, what happened in Sol Sanctum after we
            were kidnapped?

Isaac     : When Saturos and Menardi stole the Elemental Stars, they also
            triggered a volcanic eruption. The Wise One prevented Mt. Aleph
            from erupting so that Garet and I could escape.

Ivan      : But... wait, Mt. Aleph DID erupt! There was a huge explosion!
            We saw it all the way in Vault!

Garet     : But it would have erupted with us still inside... There was no way
            we could have escaped in time.

Isaac     : The Wise One held off the eruption until we could escape...
            He even halted the lava flow.

Mia       : I can't believe it... Nobody has enough power to do that...

Garet     : I know it sounds weird, but I was there, and it happened, so you'll
            just have to believe us!

Piers     : If it can do all that, this Wise One seems more like a god than
            an Adept!

Wise One  : I did not just save you. I also tasked you with recovering the four
            Elemental Stars. Why have you disobeyed my command? Why have you
            come to light the beacon?

Jenna     : Because Prox will be destroyed if we don't! We can't let that
            happen...

Wise One  : Prox? They have brought this disaster upon themselves.

Sheba     : Are you saying we should just abandon them to die? What did they do
            to deserve that!?

Wise one  : The people of Prox have committed an unforgivable sin.
            They must pay the price.

Isaac     : For lighting the lighthouses? Is that their sin? Does that warrant
            total destruction?

Mia       : If we don't light the beacon, Gaia Falls will eventually erode away
            all of Weyard!

Piers     : We have fought for so long to save all the people of our world,
            and now you would stop us?

Sheba     : Gaia Falls is growing. It's consuming more and more with each
            passing day!

Jenna     : How can you just allow the world to crumble into nothingness?

Sheba     : The seal needs to be broken! The world will be destroyed if
            it's not!

Wise One  : You have learned far too much.

Kraden    : Wise One! You can't continue to protect the lighthouses!
            You know what's happening! It is your duty to protect all of Weyard!
            If Weyard is destroyed, you will have failed us all!

Jenna     : Why won't you answer us, Wise One?

Wise One  : If Alchemy is unleashed, mankind may well destroy all of Weyard
            itself.

Kraden    : But we can combine our strengths, ensure that Alchemy not be used
            for evil...

Wise One  : It is inevitable. In time, one man will seek to rule over all.
            It is human nature, inescapable.

            And it shall come sooner than any of you think.

Kraden    : Why do you say that?

Wise One  : The Water Adept who climbs toward the peak of Mt. Aleph even as
            we speak... Is he not a friend of yours? Alex is his name.
            Surely, you have not forgotten him?

Jenna     : Alex!? What would he be doing on Mt. Aleph?

Wise One  : He understand far more than you do. He knos that when the four
            beacons have been lit... Their light will gather at Sol Sanctum.

Kraden    : But what would he gain from being there?

Wise One  : When the final beam of light reaches the peak of Mt. Aleph,
            the Golden Sun shall rise.

Kraden    : The Golden Sun!? What is that? And what would Alex want with it?

Wise One  : When the four beams merge into one, they form a golden light,
            bathing Mt. Aleph's peak.

Ivan      : Is... Is that Alchemy? I mean, pure Alchemy made real, at the heart
            of its power?

Kraden    : And it's that light that gives shape to the Stone of Sages?

Wise One  : This has been Alex's one true desire from the very start.

Piers     : Alex planned all of this? Then he must have been after this power
            all along!

Garet     : We've been duped! He used us all! Oh, you'd better believe he's not
            getting away with this!

Mia       : Alex... How could he do this? He's... He's one of my own people!
            I feel sick... disgusted...

Isaac     : None of that matters right now. We still have to light the beacon.
            We don't have any choice. If we don't do it now, Prox will be
            destroyed! Felix... We have to, right?

-----------------------------------------------------------
     -(Yes)
Sheba     : You bet we do! The Wise One will have to deal with Alex on his own.



     -(No)
Sheba     : Felix! We don't have any choice! The Wise One will have to deal with
            Alex himself.
-----------------------------------------------------------

Wise One  : I cannot interfere in the actions of mankind.

Jenna     : If you can't interfere, then how about getting out of our way
            so we can light the beacon, huh?

Ivan      : Ooo... Good one, Jenna!

Garet     : I don't like doing exactly what Alex wants, but it's looking like
            we've got no choice...

Isaac     : Don't worry, Felix! Just throw the Mars Star into the beacon's well!
            Now!

-----------------------------------------------------------
     -(Yes)
<no script>



     -(No)
Garet     : The Wise One himself said he's not allowed to interfere!
            You're all clear!
-----------------------------------------------------------

* - Felix approaches, but the Wise One begins to use Psynergy.

Piers     : Wise One! Didn't you just say that you aren't allowed to interfere
            with our actions?

Wise One  : That is correct. I cannot stop you.

            But... what if some miracle were to occur, one that prevented you
            from igniting the beacon?

Piers     : Miracle? What are you talking about? What kind of miracle?

Wise One  : If you can defeat a miracle, only then can you ignite the
            beacon's flame.

Kraden    : The Wise One is up to something! Be wary, everyone! We don't know
            what he's capable of!

* - The three-headed "Doom Dragon" flies onto the aerie. Its right and middle
    heads are yellow, while its left is red.

Sheba     : A three-headed dragon? THAT'S your miracle?

Piers     : So you would have us fight for our future? Fine, then fight
            we shall!

Garet     : What's he thinking? We already beat a two-headed dragon.
            How much tougher can this one be?

Mia       : I don't care how many heads it has. Nothing's going to stop us now!

Ivan      : Let's do it! For Prox! For the future of Weyard!

* - Everyone gets into position.

Kraden    : Wait a second... Wasn't that two-headed dragon actually...
            So that means this three-headed dragon must be...

            Felix! NO! You mustn't fight that dragon! It's--

Garet     : Too late, Kraden! We can't get away from it now!

Kraden    : Felix, don't! Stop!!!

* - During the battle with Doom Dragon, its heads are severed. Upon cutting off
    the third head, all three revert to those from whom they were created.
    The individuals are alive, albeit barely so.

Ivan      : ...Who are they?

Kraden    : That's what I was trying to warn you about! It wasn't just the
            dragon you killed...

Garet     : I remember you warning us, but it was too late for us to stop...

Mia       : Kraden, what do you know? Why were you trying to stop us from
            fighting the dragon?

Kraden    : It was the Wise One's final trap...

Ivan      : Trap? What do you mean?

Kraden    : The Wise One knew he couldn't stop you, so he played a cruel,
            wretched trick on you instead.

Isaac     : Kraden, I don't understand... What are you trying to tell us?

Jenna     : Sheba, let's see who those people are while they try to sort
            this out.

Kraden    : No, Jenna! Don't look! You mustn't look! It will only bring you
            pain...

Sheba     : What are you talking about, Kraden? They can't hurt us anymore...
            We'll just--

* - Jenna realizes who they are, appearing startled.

Sheba     : What's the matter, Jenna?

Jenna     : It... can't be... How? How...

Kyle      : Nnn... Uhnnn...

* - Isaac seems quite surprised.

Mia       : What is it, Isaac?

Kyle      : Uhhh... unnnn...

Garet     : Isaac! I... I know that guy! That's your dad!

Sheba     : Then... does that mean... the other two are...

J's Father: Hhnnnng...

J's Mother: Hhhnnn...

Jenna     : Mom... Dad...

Piers     : I'll heal Jenna's parents! Quickly, Mia! Tend to Isaac's father!

Kraden    : If only... If only I'd realized it sooner...

* - Some time passes. Piers and Mia cease using their Psynergy.

Sheba     : What's the matter, Piers? Why did you stop? Jenna's parents
            need you...

Ivan      : Don't give up, Mia. You can't! You have to save them...

Mia       : It's no use, Ivan... I'm tapped...

Piers     : I am, too... And even if I weren't, it's just too late...

Jenna     : What are you saying!? They're not... They can't be...

Piers     : That's not what I'm saying, Jenna... I...

Jenna     : I finally found them... I was going to be with them again...
            For the first time in years...

Sheba     : Jenna...

Jenna     : Please... It can't be... Mom... Wake up! It's me... It's Jenna!
            ...Don't leave me...

Kraden    : Jenna, you must prepare yourself for what comes next...
            Being transformed into a dragon, fighting in that form...
            This requires tremendous power.

Jenna     : What are you saying, Kraden?

Kraden    : In fighting you, your parents were forced to use every last ounce
            of their energy.

Jenna     : They don't have the strength to...

Kraden    : Even if they had won the battle, they would not have survived.
            You cannot blame yourself...

* - Garet looks into the distance, addressing the out-of-sight Wise One.

Garet     : You monster!!! Why did you do this? Why did you make us fight
            Jenna's parents?

Sheba     : You're no god! You're no protector! You're evil!

Piers     : You don't understand the pain you have caused, Wise One. You have
            no idea the damage done to a child who learns she has destroyed
            her own parents.

Isaac     : That's enough... I knew what I was doing the moment I raised
            my sword. We defied the Wise One in order to save the world.
            Our parents would understand. Don't you think so, Felix?

-----------------------------------------------------------
     -(Yes)
Jenna     : You're right. It hurts, but it's true. We didn't do this for
            ourselves. We did it for all of Weyard.



     -(No)
Jenna     : I agree with my brother... But it does no one any good if we
            don't complete our task.
-----------------------------------------------------------

Garet     : We still have a chance to save Prox.

Sheba     : Perhaps we can't save your parents, but we can save countless
            others.

Ivan      : Kyle and the others saved them, too... They sacrificed their lives
            so that we could go on.

Piers     : I never imagined that my actions would help to save the world...

Mia       : Even though lighting the beacon may create wars and strife,
            I regret none of this.

Kraden    : There's little time left, Felix... Use the mars Star and light
            the beacon.





* - Before casting the Mars Star into the beacon:

Isaac     :{S} Our quest is almost over. I... don't know how I'm going to
               tell Mom about this... But sorrow can wait. We've got to light
               the beacon.

Garet     :{S} I wish I could console you somehow... It must be tough...
               I just wish I'd have one last chance to have some of Felix's
               mother's cookies.

Ivan      :{S} Felix, I understand your loss... But remember, you and Jenna
               still have each other.

Mia       :{S} If Alex set this all in motion, then he's responsible for this,
               and I'll never forgive him.

Jenna     :{S} I thought I'd get to see my parents again... I thought I'd get to
               hold them again... But instead, we were forced to destroy them...

Sheba     :{S} I don't know my parents... They might be alive, somewhere
               out there... But I share your pain.

Piers     :{S} I'm sorry things has to end up like this, Jenna.

Kraden    :{S} Both Kyle and your parents were very dear to me. My sorrow
               joins yours, friends. We must light the beacon, if for no other
               reason than to provide them with a proper funeral.

Kyle      :{S} *Koff! Koff!* Felix... You made it back... alive... Please, I ask
               one last thing... Tell Dora... to live her life to the fullest...
               for me...

J's Father:{S} Unnnn... Felix? ...Jenna? I am so happy...to have one last chance
               to see you again... in the end...

J's Mother:{S} Uhhhhnnn... Felix... I... can't se you, but I sense that you're
               nearby... Please... Take care of Jenna for us...



* - If you try to leave:

Kraden    : Do not let your sadness overwhelm you, Felix! Go! Once the
            beacon been ignited, you can mourn as much as you need.
            I will protect you.





* - Upon casting the Mars Star into the beacon, a pillar of light bursts forth,
    breaking the entire lighthouse into quarter pieces.

    A sphere of Psynergetic energy rises.

Mia       : The beacon is lit!

Ivan      : And to think, I joined this quest hoping to prevent exactly this
            from happening...

Sheba     : And I began this quest as a prisoner, taken against my will.

Piers     : And if that tidal wave hadn't sent me far off course, I wouldn't
            even be here now.

Garet     : How many lives have been taken and changed forever just to light
            this beacon?

Jenna     : Mom... Dad... Weyard is safe now.

* - Someone's voice can be heard via telepathy.

????? 1    : You're right! I hear voices, too!

????? 2    : I told you... I told you I could hear them!

Isaac      : Who said that? Where are you?!

????? 1    : We're in Imil! We're at the base of Mercury Lighthouse!

Mia        : You... You can't be!

* - The scene switches to that lighthouse, where Megan and Justin--apprentices
    of Mia--are present, standing within a beam of light.

Justin    : Hey! I know that voice! It's Mia, I just know it! Mia!!!

Mia       : It's you!

Megan     : Of course it's us! We can hear you, Mia! You're all right!
            I'm so happy!

Old Woman : Who are those two kids talking to?

Old Man   : I don't know. They've been standing here telling everyone to
            leave the lighthouse. ...Weird couple of kids if you ask me!

Mia       : How is it that we can hear you?

Justin    : I don't know, but he told us we'd be able to talk to you if we
            came here now.

Mia       : He? Who's "he"?

Justin    : I don't know... We were sleeping, and he came to us in a dream...
            He said, "Go to the lighthouse!"

Mia       : The lighthouse? Why?

Justin    : He said that we have to deliver a message... He was too busy
            to do it himself...

Mia       : What message?

Megan     : We have to warn everyone to stay clear of the lighthouses!

Mia       : What's going to happen?

Justin    : I don't know, but he told us to warn people away from Mt. Aleph
            as well!

Garet     : But who is "he"!? You still haven't told us!!!

Megan     : You're a meanie! I don't tell meanies anything!

Mia       : Don't pay any attention to him... It's me, Mia... Can you tell me
            who spoke to you?

Justin    : I told you, I don't know, but he looked like a big rock...
            with a big, rocky eye!

Sheba     : The... The Wise one!

* - The scene switches back to Mars Lighthouse, where the building's pieces
    have come back together.

Sheba     : What could he be doing?

Kraden    : Of course! I understand... The Wise One said that when all four
            lighthouses have been lit, the Golden Sun will shine... When that
            happens, Mt. Aleph and the lighthouses will probably become
            quite dangerous...

Piers     : So, the Wise One is warning people in dreams, telling them to
            seek refuge?

* - Kraden nods.

Garet     : Why would he do that!? You saw what he did to us... He can't be
            up to anything good...

* - Hamma contacts them telepathically.

Hamma     : Have you not learned? One's actions do not always reveal one's
            true intentions.

Ivan      : Hamma... Sister...

Isaac     : Master Hamma! Did you receive a message, too?

Hamma     : Yes. I was called to Jupiter Lighthouse in a dream. You have
            completed your quest, but I see it comes with great loss...
            Your suffering has been almost unbearable.

Jenna     : Master Hamma... My parents...

Hamma     : I know, Jenna, and I am sorry. But do not give up hope for them
            just yet...

Jenna     : What do you mean, Master Hamma?

Hamma     : Appearances can be an illusion... The Wise One has a caring heart.

Garet     : He forced us to fight Isaac's and Jenna's parents! What's so
            "caring" about that!?

Hamma     : If the Wise One were truly evil, he would not be warning me of
            danger in my dreams.

Garet     : Well, I... I guess not... But then, what's he up to?

Hamma     : We do not have time to discuss it right now.

Kraden    : She's right. If the Wise One said it's not safe to be near the
            lighthouses, then I think we should listen.

Hamma     : I am heading for safety, too. All of you must get away from the
            lighthouse now.

Kraden    : Hurry, everyone! Let's go!

Jenna     : What about our parents?

Isaac     : We can't leave them behind...

Piers     : I understand how you feel, but we won't make it if we have to
            take them with us!

Ivan      : Make the decision, Felix! Should we take them with us?
* - Regardless of Felix's reply, another beam of light rises from the beacon.

Garet     : It's too dangerous... The Golden Sun is forming!

Piers     : A ray of light is emanating from the beacon... From the Mars Star.

Sheba     : What will happen?

Kraden    : The power of Alchemy will be unleashed upon the world!

Mia       : We must take Isaac's father and Jenna's parents and flee!

* - The sphere begins to overflow with energy.

    Garet moves a bit.

Garet     : Stop it! Let go of my wrist!

Isaac     : Garet, get a grip! No one's touching you!

Garet     : I'm serious! I...

Mia       : The beacon!

Piers     : Jenna... We have to move your parents!

Jenna     : Mom! Dad!

Ivan      : What's happening?

Kraden    : There's no time for questions! Just carry them! Carry them and go!

* - The beacon's light fills the screen, obscuring all sight.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'49] ---     [Northern Reaches]      --- [02'49] #$#
#$#$#                      Prox                       #$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - The snowstorm has ceased.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Northernmost house on bottom level  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

Elder     : Thank you, Felix! And you, too, Isaac and Kraden. By igniting Mars
            Lighthouse, you stopped Gaia Falls from devouring our town.

Isaac     : We're just glad to have helped save Weyard...

Puelle    : You've been through many trials, more than any of us can ever
            know...

Kraden    : We had no idea what to expect when we lit the final beacon...

Woman     : When we saw the flash of the beacon, we had no idea what you
            suffered to light it...

Isaac     : I thought we were done for... There was no way we could escape with
            our parents' bodies.

Kraden    : Well, at least, not if we hadn't pulled together and overcome
            our sorrows...

Man       : That light was brilliant!

Kraden    : You know, I shall always regret that I didn't get to look upon the
            beacon's light from afar...

Elder     : I understand your regret... As a scholar of Alchemy, you would have
            been most impressed.

Isaac     : I saw the beams of blue, red, and purple streaming out toward the
            southeast...

Woman     : That's the direction in which Vale lies, is it not? Was the light
            headed to your hometown?

Isaac     : Indeed it was. The Wise One said the beams were going to merge
            into one above Mt. Aleph.

Elder     : The orb of golden light we saw... That was shining directly over
            Vale?

Kraden    : Yes. That was the Golden Sun forming over Mt. Aleph.

Puelle    : If I remember the tales correctly... The Golden Sun is the blast of
            light emitted at the very moment the Stone of Sages forms...

Kraden    : Such legends exist even here? I wish that I'd known that sooner!

Elder     : I fear for Vale, to think that all this energy is being released
            right over your hometown.

Isaac     : We're all worried about that. We're hoping we can return to Vale
            as quickly as possible.

Puelle    : Oh... Is there nothing we can do to convince you to stay?

Elder     : We had hoped you might stay in Prox a while, but that sounds
            unlikely...

Isaac     : Don't worry... We plan on returning as soon as things quiet down,
            don't we?

-----------------------------------------------------------
     -(Yes)
Elder     : Our village will not soon forget that you saved us from the edge
            of destruction. Do visit us again.



     -(No)
Elder     : You have just completed a long and difficult journey. Perhaps when
            you are older, you will look back on your youth, and you will
            remember us fondly...
-----------------------------------------------------------

Kraden    : When that time comes, I may no longer be in this world.

Puelle    : Don't say such things... I'm sure a long life awaits you.

* - Kraden nods.

Kraden    : Well, I suppose we should be departing for Vale soon.

Isaac     : You're right, Kraden... If we don't you-know-who might start
            causing trouble...

Elder     : At least some of your cares have been remedied... You must be glad
            to know we've brought all three back from the brink of death.

Puelle    : I would not have thought it possible had I not seen it.

Kraden    : Even I do not fully understand it...But their [sic] can be no doubt.
            The fire Psynergy released by the beacon rekindled their spirits.
            I hadn't expected so much Psynergy to be released by the light-
            house's beam... I have no real explanation, other than that their
            life force had not been fully extinguished. It was a miracle, but
            the fire Psynergy seems to have recharged them somehow.

Elder     : And had your parents not been Adepts, the wave of Psynergy would
            have passed them by.

* - Jenna shouts from outside.

Jenna     : Isaac! What's taking you two so long? Don't keep me waiting!

Kraden    : Uh-oh! It's Jenna... We're late, and she looks rather displeased
            with us.

Isaac     : Should I let her know we're leaving now?

-----------------------------------------------------------
     -(Yes)
Isaac     : I'm sorry! We're almost done. Can you wait for us at the village
            gates with the others?

Jenna     : I'm serious! If I have to wait much longer, you're not going to
            be happy!



     -(No)
Isaac     : I'm sorry, Jenna! It sounds like things are going to take just a
            little bit longer...

Jenna     : Well, I'm not going to wait much longer! If you don't come soon,
            we're all leaving without you!
-----------------------------------------------------------

Man       : I'll wait outside with them.

* - He takes his leave.

Isaac     : I don't think they want to wait anymore, Felix. We're all set to
            head home...

Kraden    : They have no patience whatsoever. Ah, well... I suppose it is time
            to leave.

Puelle    : May your journey home be safe and uneventful...

Elder     : We shall never forget what you have done for Prox.


#$#$#$#$#$#$#$#$#$#$#
$#  Social Script  #$
#$#$#$#$#$#$#$#$#$#$#

* - Under normal conditions, minds cannot be read, as Sheba and Ivan are absent.
    However, Mind Read script can be obtained via hacking.



   [ Outside ]
[001]     :{S} Thank you for lighting the fires of the lighthouse beacon, Felix.
               You saved us all.

           {M} Felix has proven himself as the strong warrior Prox has ever
               known!

[002]     :{S} Will you be going back to Vale now that your quest is over,
               Felix? Don't forget us!

           {M} I bet Felix and his friends live in a nice, warm place...
               I wish I could go with them.

[003]     :{S} It's too bad about Agatio and Karst... They weren't bad people...
               A little obsessed, yeah, but it's still sad that they're gone.

           {M} I heard that Karst and Agatio were defeated by a monstrous
               dragon... Felix beat the dragon, though... I don't know whether
               I'm impressed or scared of him.

[004]     :{S} You did an amazing job... You accomplished what Agatio and Karst
               could not...

           {M} When Felix left town, he of [sic] a fighter... He wasn't much
               of anything, really... When did he become mightier than the
               mightiest of Prox's warriors?

[005]     :{S} I don't remember the last time I saw the sky this bright and
               clear.

           {M} The blizzard's finally over... That was the worst patch of
               weather we've ever had!

[006]     :{S} I was so moved when I saw that light shining from the north.
               We all owe you our lives.

           {M} I was the first person in town to see the lighthouse! I was so
               happy, I had to tell everyone! I felt like a little boy again,
               running giddily through town, shouting and waving!

[007]     :{S} Winter in Prox can be bitter cold, but I think things will feel
               more mild after this.

           {M} Now that our weather is returning to normal, maybe everyone will
               move back here.

[008]     :{S} The lighthouses have all been lit... Does that mean we're going
               to fall back into war and chaos?

           {M} They had no choice... They had to light the four elemental
               lighthouses... Even though it might mean a rise in war and
               violence, it had to be done.

* - The three children from the igloo have come outside to play.

[022]     :{S} I miss running around outside. It's been so cold, I can't even
               work up a good sweat.

           {M} That blizzard was unreal, but it's gone now, and the weather's
               beautiful.

[023]     :{S} If I'm going to be a great warrior, like Felix, I'm gonna have to
               train hard.

           {M} You get more exercise running in the snow, because it's a lot
               harder to do.

[024]     :{S} Weeee! What fun! Now that it's stopped snowing, we can go outside
               and play.

           {M} Now that the lighthouse is lit, we don't have to play in that
               stupid igloo anymore.





   [ Buildings ]
Innkeeper1:{S} We had no idea there would be such a terrible earthquake when the
               beacon was lit. My wife tumbled right into my arms... It was like
               we were teenagers all over again!

           {M} We'll never be able to thank Felix and the warriors of Vale
               enough. I hope they're all happy to be home with their families
               in Vale again.

Innkeeper2:{S} After that earthquake, I feel like I aged a couple of years
               in just a few minutes!

           {M} When the earthquake hit, Felix and his friends were high up on
               the lighthouse. If that had been me up there, I think my heart
               would have stopped from fear!

-----

[009]     :{S} I think the rift to the north started receding when the
               lighthouse was lit...

           {M} I was afraid the falls were going to gobble me up! I'm glad
               that's over now...

[010]     :{S} I wonder if that hole up  north has stopped growing...
               What if it starts again?

           {M} What do we do if the falls start expanding again and Felix isn't
               here? Oh, great... That's going to keep me up all night worrying.

[011]     :{S} The lighthouse was so beautiful when the beacon was lit...
               It made a beautiful band of light!

           {M} All the lights joined up together and shot off to the southeast.
               It looked like they all formed into a big, golden ball or
               something.

-----

[012]     :{S} Felix, take some advice from an old man... You would do well
               not to tell anyone that you were the ones to light the beacons...

           {M} If they found out Felix used the treasures of Sol Sanctum to
               light the beacons... That fool of a mayor would no doubt punish
               them for what they did to save us.

[013]     :{S} Isaac and his friends left Vale having sworn to return with the
               Elemental Stars. When they return, they'll have to tell everyone
               what happened. I hope they won't be punished...

           {M} The mayor and the elders in Vale are so out of touch. When they
               see Felix and his friends return without the stones, they'll
               punish them.

-----

Elder     :{S} Your body has absorbed a great deal of raw elemental energy.
               Please be careful.

           {M} The power to revive the dead... It's an awesome and terrifying
               power indeed... Eternal life could soon be in the hands of
               Alchemists everywhere... What a thought!

Puelle    :{S} I have much to do, so I won't be able to see you off, but I wish
               you safe journey.

           {M} We may have underestimated the power of the Psynergy he
               unleashed... We'll have to study it more closely once we've
               seen Felix on his way.

[014]     :{S} Felix, I always thought of you as my very own grandson when you
               were here... Now that you're leaving, I can't describe the sorrow
               that fills this old man's heart.

           {M} Who knew that the poor, injured boy they brought back from Vale
               would be the one to save Prox? I'm happy that he'll finally be
               able to return home, but I'll miss him so...

[015]     :{S} There's no telling what could happen now... If you absorbed
               energy, maybe Jenna did, too... Which means you'd better not
               make her angry, or you'll really get it!

           {M} We've lost so many soldiers, and now Felix is leaving...
               It's going to be quiet in Prox.

[016]     :{S} Think of your old grandma's cooking every now and then when
               you're back home in Vale.

           {M} I'm so sad... Felix doesn't even have time to enjoy this last
               meal I made him...

-----

G. Healer :{S} Now that the lighthouse has been lit, I fear for what will
               happen to Weyard.

           {M} The lighthouses are going to restore the power of Alchemy to
               the land... But Alchemy is too terrible a power to set free...

-----

[Item]    :{S} Your foster grandmother knew that you would return. She always
               said you were reliable.

           {M} It's too bad Felix can't stick around.. He'd make the perfect
               son-in-law.

[017]     :{S} Thank you so much, Felix! If you hadn't returned to us,
               we wouldn't be here right now!

           {M} I never imagined that little Felix would become stronger
               even than Agatio and Karst.

-----

[018]     :{S} The people of Prox won't forget what you've done for them...
               You can return home to Vale with great pride, but you'll always
               be welcome here.

           {M} Felix and his allies saved us from certain destruction.
               It's a shame the rest of the world doesn't know how much they've
               done for us all.

[019]     :{S} I guess the four lighthouses were the seal that blocked the power
               of Alchemy. So not only did Felix save Prox, he's also brought
               about a new golden age!

           {M} Now that Alchemy is free, it's like Weyard is waking up! How will
               the world change?

[020]     :{S} I've been told that lighting the four beacons has set Alchemy
               free on the world. Now that we all can use Alchemy again,
               civilization is going to make great strides!

           {M} Alchemy has been freed. We must begin researching it in earnest
               here in Prox.

-----
* - Igloo:

[021]     :{S} I can hear the sound of children playing far off in the
               distance... That sound means that everything's back to normal
               and our worries are past.

           {M} It's been so long since children's voices rang through our
               streets. I hope these children remain ignorant of how much danger
               we were all in...

* - [022], [023], and [024] have gone outside to play.





   [ North end of Prox ]
Man 1     :{S} Sorry, Felix, but this road is blocked off right now.

           {M} The road to the lighthouse is in terrible shape after the
               earthquake... I've got no clue how Felix and the others
               made it back to town on that road.

Man 2     :{S} If you're worried about the lighthouse beacon, don't...
               It's still lit.

           {M} The elders were saying that the lighthouse is tough to put out
               once it's lit.

Man 3     :{S} I just don't think I'm cut out to be a soldier. I should have
               taken up knitting instead.

           {M} On the other hand, now that Alchemy is free, maybe I should
               study Alchemy...

Woman 1   :{S} Felix taught me a lot about how to be a serious soldier...
               I've been going easy on myself, but no more! I'm going to train
               harder every day!

           {M} Maybe if I train hard enough, I'll be as strong as Menardi and
               Karst were...

Woman 2   :{S} Well, you look like you're all set for the return trip to Vale.
               Travel well, Felix.

           {M} When Felix left Prox, I didn't think much of him, but now,
               he's totally hot!

Woman 3   :{S} Even just standing outside the lighthouse, I can feel the energy
               coming from within...

           {M} If the light of the beacon keeps shining, the power of Alchemy
               will never end... Even if Prox is attacked, the bright flames
               of our strength will burn on.


#$#$#$#$#$#$#$#$#$#$#$#$
$#  Village entrance  #$
#$#$#$#$#$#$#$#$#$#$#$#$

Jenna     : What took you so long? Mom and Dad are tired of waiting for you...

J's Mother: That's not true, Felix. You take as long as you need to say farewell
            to the people of Prox.

J's Father: Don't worry about us, Felix... Puelle and the others took good care
            of us.

Jenna     : Don't tell him that! We'll be stuck here forever!

Sheba     : You look like you're feeling back to your old self, Jenna!

Piers     : You were weeping such mournful tears after the battle...

Jenna     : What!? As if! You can't prove anything!

Mia       : Go easy on her. You have to remember, she thought that both of her
            parents had died.

J's Mother: Oh, were you crying, Jenna?

Jenna     : No! I said... I said I wasn't!

Garet     : Now you've got me thinking about my family... I didn't think I'd
            miss them this much...

Ivan      : I only hope that they're all safe back in Vale...

Isaac     : I just want to be home again... I want to see how my mother
            is doing...

Kyle      : Don't worry, Son. I'm sure Dora's doing fine. She's a strong woman.
            And she wouldn't let anything happen until you came home.

Kraden    : Sorry to keep you all waiting. At last, the time has come for us
            to return to Vale... As soon as we leave Prox, we'll head toward
            Angara, and from there, to Vale...

J's Mother: I can't wait to see this winged ship of yours! Is sounds so
            incredible!

J's Father: I remember so little of our trip to Prox... This is really my first
            voyage on a ship.

Kyle      : I've heard that the wind and waves make the boat rock... I hope I
            don't get sick...

Kraden    : This ancient ship of ours actually flies above the ocean...
            It's quite a cozy ride.

Isaac     : It looks like we've got an exciting last trip ahead of us,
            doesn't it?

-----------------------------------------------------------
     -(Yes)
Isaac     : Wow... Setting out like this takes me back to our own quest's
            start... It was so long ago.



     -(No)
Isaac     : I'm still worried about my mother, but I'll try to put it aside
            and enjoy the trip.
-----------------------------------------------------------

Jenna     : If you keep talking like this, we'll never go anywhere! Let's go,
            Felix!

* - Most everyone heads off, but Isaac and Felix lag behind. Kraden, Garet and
    Jenna stop as well.

Kraden    : What's the matter, boys? Are you reluctant to depart?

-----------------------------------------------------------
     -(Yes)
Kraden    : It's hard to believe that our quest is almost at its end.
            I know how you feel.



     -(No)
Kraden    : After all that we've been through, you can't possibly be nervous
            about this small trip!
-----------------------------------------------------------

Isaac     : I just hope that Vale came out of this in as good a condition as
            Prox did...

Kraden    : We won't know until we get there.

Garet     : I can't stop thinking about how my parents are doing...

Kraden    : Were the both of them in Vale?

* - Jenna nods.

Jenna     : Can't you make a guess, Kraden? Will Vale still be standing when
            we arrive!

Kraden    : Not even I can know that...

Garet     : I can see it in your eyes, Kraden! You think something's happened,
            don't you?

Kraden    : It's a possibility... One that cannot be ignored...

Isaac     : If it's not there, then what's the point in even going back?

Kraden    : Is that really how you feel, Isaac? What about you, Felix?

-----------------------------------------------------------
     -(Yes)
Kraden    : Have you already forgotten all that we discussed? You ought to
            refresh your memory!



     -(No)
Kraden    : You remember, don't you, Felix? Think about it for a moment, Isaac.
-----------------------------------------------------------

Garet     : What do you mean?

Kraden    : Our conversation with Hamma after we ignited the beacon...

Jenna     : Don't you remember us talking to the children from Imil at the
            base of Mercury Lighthouse?

Isaac     : When they were warning people away from the lighthouses?

Kraden    : Yes. The Wise One instructed everyone to seek refuge.

Garet     : Yeah, so what about it?

Kraden    : You still don't see, Garet? Even if Vale was destroyed, I'd expect
            that the villagers have all escaped to safety.

Jenna     : I guess that's true... They might still be all right.

Garet     : That's true... So whatever happens, my family's alive!

Isaac     : I'd forgotten about that... Thanks, Kraden.

Jenna     : Garet, can you make sure everyone else knows that?

* - Jenna and Garet head south to the others.

Kraden    : OK, let's go. The both of you! We have to catch up to everyone.

Isaac     : Kraden... Why did the Wise One change our parents into a dragon?
            Why did he make us fight them? I mean, we almost killed them...
            He tried to make us kill our own parents. Why?

Kraden    : Do you think that he intended for them to die from the start?

-----------------------------------------------------------
     -(Yes)
Kraden    : I cannot speak for him, but I think he kenw that they would be
            revived by the beacon's light.



     -(No)
Kraden    : Ah... You don't understand why he put you through all this if he
            knew they'd survive...
-----------------------------------------------------------

Kraden    : We cannot hope to fathom the motives of a being as all-powerful
            as the Wise One...

Isaac     : You don't know either, Kraden?

Kraden    : I can only hazard a guess... The Wise One... wanted to test you.

Isaac     : What do you mean, test us?

Kraden    : I cannot tell you more... It is up to you to find the answer.

            Will we use Alchemy to wage war, to raise armies? Or will we use it
            to grow wise, to rise above our petty feuds and perform great deeds?

            You were willing to sacrifice everything for your quest.
            I'd say you've risen to this challenge.

* - He looks in the direction where the others departed.

Kraden    : Oops! Is everyone else that far ahead of us? We'd better hurry and
            catch up to the others before they leave us behind! After all, I'm
            not terribly interested in trying to walk all the way back to Vale.
            If you feel the same, then we'd better be hurrying.

            Isaac! Felix! We're off!

* - The credits roll. During them:


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [02'50] ---          Epilogue           --- [02'50] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#
$#  [Angara]  Mt. Aleph  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - Back when the beacon had just been lit, Alex was climbing the mountain.

Alex      : The Golden Sun... The very quintessence of Alchemy's power!
            It's beginning! Wait for me! Please, wait! Wait until I reach
            the summit of Mt. Aleph!  

* - Mars, Mercury, Venus and Jupiter send their energy to Mt. Aleph,
    forming the Golden Sun. At the summit, Alex stands in the sphere's light.
    The mountain glows, brimming with Psynergy.

Alex      : At last! I have it! Eternal life... and limitless power! At last,
            the power of nature is mine to control as I will! Rise, storms!
            Rise up and unleash your might upon Vale and the foothills of
            Mt. Aleph!

* - Nothing happens.

Alex      : That's odd... I should have limitless power... So why can't I
            call up a simple storm?

* - The Wise One appears before Alex.

Alex      : Wh-Who are you?

Wise One  : I am called the Wise One...

Alex      : The Wise One? Vale's protector?

Wise One  : You wish to have limitless power?

Alex      : Wish to? I just got it!

Wise One  : No. Your power is nearly limitless, but it has boundaries.

Alex      : Nearly limitless? You speak in riddles. Can't you see?
            The power is mine!

Wise One  : Yes. You also have nearly endless life. And your Psynergy is...
            somewhat stronger.

Alex      : If you are trying to anger me, have a little taste of exactly
            how much power I have attained!

* - He uses his Psynergy, pushing the Wise One back.

Alex      : Look at me! My body is brimming with power!

* - The Wise One uses its own Psynergy to throw Alex down, and then to
    suspend him in midair.

Alex      : How!? What's going on? I should be all-powerful! How can you
            defeat me?!?

* - The Wise One slams Alex down.

Wise One  : You are not all-powerful, Alex. Your power has its limits,
            as does your life.

Alex      : This cannot be! Who is responsible for this treachery?
            Who has robbed me of my dream?

Wise One  : I, the Wise One, imbued the Mars Star with some of the power of the
            forming Golden Sun. It rests even now in the hands of young Isaac.

Alex      : Why?

* - The mountain begins to shake violently.

Wise One  : The heavens and earth are changing, Alex! You must flee now!

Alex      : Wha-What!?

Wise One  : Mt. Aleph will soon be drawn into the heart of the earth!
            You must flee or join it forever!

Alex      : Flee?! I can't flee! I can't even move!

Wise One  : Ah, yes. You now see the limits of your power. If you are swallowed
            by the earth, you may not survive. If you survive, perhaps we shall
            meet again someday...

* - The Wise One disappears as the mountain begins to sink into the earth.


#$#$#$#$#$#$#$#$#$#$#$
$#  [Angara]  Vale  #$
#$#$#$#$#$#$#$#$#$#$#$

* - At a hill near the village:

Jenna     : Finally! We've reached Vale.

Garet     : ... ...

Sheba     : What's the matter, Garet? You're finally home again.
            Aren't you happy?

Ivan      : Garet's just worried about what's happened to everyone in Vale.

Mia       : So it's just over that last hill?

Piers     : I can't wait to see what your hometown looks like.

Kraden    : It's beautiful... I'm sure you will like it, Piers.

J's Father: I'm... just going to close my eyes. Someone tell me if it's
            all right to open them.

J's Mother: Me too... Would someone else see how things are?

Isaac     : I'll go. Come with me, Felix.

Kyle      : How's it look, Isaac?

Isaac     : I'm almost there...

            It... It can't be...

Jenna     : What is it, Isaac? ...Felix? Say something!

Felix     : I'm sorry, Jenna, but... Vale... Mt. Aleph... They're gone!

Garet     : What!?

* - Vale has been pulled under the ground with Mt. Aleph, which only stands
    partially above the ground.

J's Father: This... This is terrible.

J's Mother: Is that Mt. Aleph?

Isaac     : Mom...

Kyle      : Dora...

Garet     : Mom... Dad...

Jenna     : Isaac... Garet... What can I do? What can I say to comfort you?

            They're here somewhere... They have to be here...

Piers     : What can we do? How can we help them now?

Kraden    : I don't know... Call out to them... Such a tragedy...

Felix     : I'll call them...

            Isaac... Garet... I understand what you're feeling. I've felt it,
            too. But standing here won't bring them back. Let's go back to
            Vault. We can rest there and think...

Isaac     : ... ...

Kyle      : ... ...

Garet     : Your family's safe, Felix. You don't have anything to worry about
            anymore... But what am I supposed to do? ...I'm all alone now.

Sheba     : Aw... Poor baby...

Jenna     : Sheba, what's gotten into you? How could you say that to Garet?

Mia       : Tee hee! I wonder...

Garet     : Sheba, Mia!? You think this is funny!? I've lost everyone!
            My whole family!

????? 1   : Garet! Don't be so sad!

Isaac     : ???

????? 2   : I'd thought you might be a little more confident after all your
            adventures!

Isaac     : !

????? 3   : Ha ha! I got to see my brother crying!

Garet     : !!!

* - Garet's family approaches.

G's Father: So, you made it back, Garet... I knew it would take more than this
            to beat you, Son.

G's Mother: Welcome home, Garet...

G'sGrandpa: You look surprised to see us, Garet.

Kyle      : How did you survive?

G's Mother: The Wise One warned us of danger. He guided us here to safety.

G'sGrandma: Everything was destroyed... Our homes, our town...

Kraden    : But the Wise One saved you all?

Garet     : I'm... I'm not alone!

Kraden    : If you all made it out, did Dora as well?

* - Dora steps forward.

Kyle      : Dora...

Isaac     : ...Mom...

Dora      : Welcome home, Kyle... Isaac...

Kyle      : You survived!!!

Dora      : So did you...



The End


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$                                       $#$#$#$#$#$#$#$#$#$#
#$#$#   [03'00]   ---               Addenda               ---   [03'00]   #$#$#
#$#$#$#$#$#$#$#$#$#$                                       $#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [03'01] ---       Djinn & Summons       --- [03'01] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#$#
$#  Djinn abilities  #$
#$#$#$#$#$#$#$#$#$#$#$#

   [ Venus ]
* - Golden Sun:

Flint     : Strike a blow that can cleave stone.
Granite   : Create a mighty earthen barrier.
Quartz    : Revive a downed ally.
Vine      : Tangle foes to drop Ability.
Sap       : Attack a foe and steal HP.
Ground    : Use gravity to hold a foe.
Bane      : Attack with nature's venom.

* - Golden Sun: The Lost Age:

Echo      : Attack with a double strike.
Iron      : Bolster the party's Defense.
Steel     : Siphon a foe's HP with a kiss.
Mud       : Slow a foe with sticky mud.
Flower    : Refresh allies and restore HP.
Meld      : Launch a powerful team strike.
Petra     : Turn a foe to stone.
Salt      : Restore allies' status to normal.
Geode     : Strike with a clod of earth.
Mold      : Strike a foe.
Crystal   : Restore HP to all allies.



   [ Mars ]
* - Golden Sun:

Forge     : Boost party Attack with flame's fury.
Fever     : Wrap a foe in feverish delusion.
Corona    : Boost party Defense with a heat aura.
Scorch    : Stun a foe with a blast attack.
Ember     : Restore party PP with passion's flames.
Flash     : Block damage to party with a firewall.
Torch     : Penetrate defense with a melting blast.

* - Golden Sun: The Lost Age:

Cannon    : Strike with the power of Mars.
Spark     : Revive an ally with cheers of support.
Kindle    : Increase all allies' attack.
Char      : Paralyze foes with a strong blow.
Coal      : Rally your allies to boost Ability.
Reflux    : Counter an enemy's attack.
Core      : Strike through an enemy's Defense.
Tinder    : Revive a downed ally.
Shine     : Dazzle does and strike decisively.
Fury      : Call worth wandering souls to attack.
Fugue     : Fatigue your foes to drop their PP.



   [ Jupiter ]
* - Golden Sun:

Gust       : Attack with mighty wind gusts.
Breeze     : Boost party Resistance.
Zephyr     : Boost party Agility with swift wind.
Smog       : Veil a foe's vision in smoke.
Kite       : Attack twice next round.
Squall     : Paralyze a foe with a storm.
Luff       : Seal a foe's Psynergy.

* - Golden Sun: The Lost Age:

Breath    : Restore HP quickly.
Blitz     : Numb a foe with a lightning strike.
Ether     : Focus will to restore HP.
Waft      : Calm a foe with soothing scents.
Haze      : Hide away to avoid damage.
Wheeze    : Poison a foe as you strike.
Aroma     : Restore everyone's PP.
Whorl     : Take a deep breath, and strike!
Gasp      : Call the Grim Reaper on your foes.
Lull      ; Negotiate a temporary cease-fire.
Gale      : Blast enemies with a wind strike.



   [ Mercury ]
* - Golden Sun:

Fizz       : Restore HP with calming water.
Sleet      : Drench a foe to drop its Attack.
Mist       : Lull a foe into deep sleep.
Spritz     : Restore party HP with soothing mist.
Hail       : Freeze a foe to drop its Defense.
Tonic      : Heal all party ailments.
Dew        : Revive a downed ally.

* - Golden Sun: The Lost Age:

Fog       : Blind an enemy with fog.
Sour      : Reduce a foe's resistance.
Spring    : restore HP with healing herbs.
Shade     : Create a watery shield.
Chill     : Strike to reduce a foe's defense.
Steam     : Increase all allies' Elemental strength.
Rime      : Seal a foe's Psynergy.
Gel       : Weaken a foe's Attack.
Eddy      : Speed up Djinn recovery time.
Balm      : Revive all downed allies.
Serac     : Strike a chilling finishing blow.


#$#$#$#$#$#$#$#
$#  Summons  #$
#$#$#$#$#$#$#$#

   [ Venus ]
01:  Venus     -  The elemental power of earth.
02:  Ramses    -  Guardian of an immortal pharaoh.
03:  Cybele    -  The great mother of the earth.
04:  Judgment  -  The might of the apocalypse.



   [ Mars ]
01:  Mars      -  The elemental power of fire.
02:  Kirin     -  A mystical beast cloaked in flame.
03:  Tiamat    -  The queen of all dragons.
04:  Meteor    -  A meteorite from deep space.



   [ Jupiter ]
01:  Jupiter   -  The elemental power of wind.
02:  Atalanta  -  The heavenly huntress.
03:  Procne    -  A goddess in bird form.
04:  Thor      -  The mighty god of thunder.



   [ Mercury ]
01:  Mercury   -  The elemental power of water.
02:  Nereid    -  Princess of the sea spirits.
03:  Neptune   -  An incarnation of the sea king.
04:  Boreas    -  The god of the north wind.



   [ Summon Tablets ]
01:  Zagan        -  Earth's might enflamed.
02:  Megaera      -  The goddess of vengeance.
03:  Flora        -  The wind rider, goddess of flowers.
04:  Moloch       -  The sacred ice monster.
05:  Ulysses      -  An [sic] legendary wandering mage.
06:  Haures       -  A beast that sunders darkness.
07:  Eclipse      -  A dragon whose wings span the skies.
08:  Coatlicue    -  A goddess bearing the water of life.
09:  Daedalus     -  Master craftsman of ancient times.
10:  Azul         -  An awakened dragon from the deep.
11:  Catastrophe  -  The embodiment of destruction.
12:  Charon       -  The boatsman of the river Styx.
13:  Iris         -  Goddess of rainbows, guide of souls.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [03'02] ---   Transfer-prompted Events  --- [03'02] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - If certain requirements were met in Golden Sun, then special events
    will occur in The Lost Age.


#$#$#$#$#$#$#
$#  Madra  #$
#$#$#$#$#$#$#

* - If Isaac's group learned of the thieves' escape from Vault, then
    when exiting Madra after having acquired the Cyclone Chip:

Thief Head: Hey! Wait a minute!

* - The three thieves approach Felix's group.

Kraden    : Who are you?

Thief Head: You were talking about Isaac, weren't you?

Thief 2   : Don't play dumb... We all heard you.

Kraden    : Yes, we know Isaac. What about him?

Thief 3   : Well, why don't you tell us where we can find him?

Kraden    : Why should we tell you anything?

Theif 3   : Isaac took good care of us when we were in Vault, and we'd like to
            thank him...

Kraden    : Ah, yes... Well... I'm afraid we don't know where you can find
            Isaac right now.

Thief Head: Oh, is that so? Well, I guess we'll just have to give you the reward
            we'd planned for him.

Kraden    : You've got a grudge against Isaac, and you're going to take it out
            on us?

Thief 3   : Oh yeah, you could call it a grudge,,, A serious grudge.

Thief Head: But don't worry... We're just going to give you a little sample
            of what we've planned for him.

* - The thieves engage Felix's group in combat. After the fight:

Thief Head: We lost again...

Thief 2   : So, boss... You, uh... You think maybe it was a mistake going after
            these guys?

Thief 3   : This means we're going to jail again, doesn't it?

Thief Head: Aw... Why do we have to go back to jail. I hate it there...
              * Typo

Thief 2   : It's not like we really hurt anyone... After all, we lost!

Thief Head: Yeah... And it's not like we stole anything... this time...

Thief 3   : We're not gonna have to go to jail, are we?

Kraden    : You're thieves!

* - They nod.

Kraden    : If we asked around, we could probably find a dozen reason to have
            you locked up!

Thief Head: Are you guys, like, wandering sheriffs or something?

-----------------------------------------------------------
     -(Yes)
Thief Head: Because we could be really useful to you if you are.
            We know all sorts of criminal elements...



     -(No)
Thief Head: And even if you're not, we could be really useful to you...
            Anything's better than jail!
-----------------------------------------------------------

Kraden    : You can't honestly believe we would let you join us!

Thief 2   : Hey, come on! We haven't done anything wrong, really!
            Not yet, anyway...

Thief 3   : Yeah! We didn't have enough time to do anything bad before we ran
            into you guys!

Thief Head: Yeah, so give us a break!

* - He throws the Golden Boots at Felix's group.

Thief Head: So, uh... Bye! See you later!

* - They flee. Kraden turns to Felix.

Kraden    : Will you promise to stop following Isaac and trying to get revenge
            on him?


#$#$#$#$#$#$#$
$#  Champa  #$
#$#$#$#$#$#$#$

* - If Isaac's group assisted in Hsu's rescue, then
    upon arriving for the first time:

Feizhi    : Isaac!

* - Feizhi runs up to Felix.

Feizhi    : Isaac, is it you? Do my eyes deceive me?

-----------------------------------------------------------
     -(Yes)
Feizhi    : Oh. I must have been mistaken.



     -(No)
Feizhi    : No, you are not Isaac, are you?
-----------------------------------------------------------

Kraden    : Young lady, are you looking for someone by the name of Isaac?

Feizhi    : Yes, old man! I am looking for one called Isaac!

* - She looks around.

Feizhi    : Where is Isaac?

Kraden    : I'm sorry... Isaac isn't with us...

Feizhi    : Well then, where can I find Isaac?

Kraden    : Why do you want to find him so badly?

Feizhi    : Me? I am Feizhi... Isaac helped me once. He helped Ulmuch.
            Ulmuch was trapped, but Isaac saved him. He is a brave man,
            isn't he?

Kraden    : I suppose... But why are you looking for him? Do you

* - Slight pause.

Kraden    : like him? Is that it?

Feizhi    : You're a mean old man. It is not polite to tease me.

Kraden    : That's what it is! You like Isaac!

Feizhi    : No! I am so embarrassed!

Kraden    : Don't worry, Feizhi... We'll tell Isaac how you feel!

Feizhi    : I... Really? Then... will you give him this when you tell him?

* - She takes out the Golden Ring.

Kraden    : What is it?

Feizhi    : Isaac is on a dangerous journey. I am worried about him, so I made
            him a good luck charm.

Kraden    : Ah, a good luck charm... I see.

Feizhi    : I am going home now, old man. Thank you for doing this favor for me.

* - She departs.


#$#$#$#$#$#$#$#
$#  Alhafra  #$
#$#$#$#$#$#$#$#

* - If Deadbeard was defeated on Crossbone Isle, then
    on the second floor of the inn, after the ship's mast is fixed:

Pirate 1  : Legends said that Crossbone Isle could be found in the middle of the
            Karagol Sea.

Pirate 2  : Ah... Crossbone Isle... Wait, did you say "could"? Is it not there
            anymore or something?

Pirate 1  : Well, it's still there, but there's no point in going. Someone named
            Isaac picked it clean.

Pirate 2  : What, he took all the treasure?

Pirate 1  : Yeah. And apparently, he even defeated the ancient ghost pirate
            protecting it...

Pirate 2  : What about the stories that if you beat the ghost pirate, you would
            become the leader of all pirates?

Pirate 1  : Well, you see, that means that Isaac is our leader now.

Pirate 2  : Wow... just like that? I'll bet he's pretty tough.

Pirate 1  : No doubt. But you know, he must be a reliable guy, too...

Pirate 2  : You think?

Pirate 1  : You'd have to be to beat that ghost. That's why we're looking for
            him now, remember?

Pirate 2  : If he's looking for a pirate crew, he can count me in!

* - They depart.


#$#$#$#$#$#$#$#$#$#$
$#  Atteka Inlet  #$
#$#$#$#$#$#$#$#$#$#$

* - If Hammet was saved from the village of Lunpa, then
    when boarding your ship after the Wings of Anemos have been affixed to it:

Man       : Hey, wait! Master Hammet requested that I deliver this to Isaac,
            and I totally forgot about it!

Hamma     : Well, you'd better hurry.

Man       : I'm supposed to deliver this to Isaac... It's not too late, is it?

* - He sets down a chest, which contains an Orihalcon (a forgeable ore).

Hamma     : On my way here, I stopped in Kalay briefly to speak with Master
            Hammet. He was quite upset that you hadn't returned to visit him so
            that he could thank you. So he requested that I take this with me to
            Atteka. It is a gift of thanks from Master Hammet. Take it, please.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Colosso finalists  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - If Isaac won Colosso, then
    all of that year's finalists (save for Buford) can be encountered.



* - At Madra's inn, before the Kibombo attack:

Morgan    :{S} We're heading to Tolbi. We hear there's a tournament there
               called Colosso. I'm Morgan, and this here's Dekka. We're gonna
               compete and we're gonna win!

           {M} The gladiator who takes the prize in Colosso earns quite a
               reputation as a warrior... Mercenaries get a lot more jobs when
               they've got a good reputation.

Dekka     :{S} Hey, if you see a gladiator named Isaac, give him a message
               for me... If he's thinking about going to Colosso this year,
               he doesn't stand a chance of winning!

           {M} We fought in Colosso last year, but we lost to a weaselly little
               kid named Isaac. We're after revenge, so we've been out on a
               risky journey to increase our fighting strength.



* - At Mikasalla's inn, at any time until speaking to this finalist or
    until joining with Isaac's group:

Galahad   :{S} Forgive my manners... No, please... Do not fear me. I am the
               warrior, Galahad. I am looking for someone, and I need your
               help... Do you know of a knight called Isaac?

               --------------------------------------------
                    -(Yes)
               You do? I must warn Sir Isaac that he is in danger most
               grievous... Even now, Satrage, Navampa, and Azart are looking
               for him... They wish to avenge the loss he gave them at Colosso.



                    -(No)
               A pity... The one I seek won a battle at Colosso, in Tolbi.
               He won... and too easily, perhaps. Now, his opponents are eager
               for revenge.
               --------------------------------------------


                 * - 2nd+ time:

               Isaac's enemies are gathering now, to destroy him and erase
               their shame.

           {M} I fear what might happen if the three find Isaac before I can
               warn him...



* - Shaman Village Cave, after Isaac's group joins with Felix:

?????     : I found Isaac!

* - Navampa, Azart and Satrage rush into the area.

Navampa   : We've been looking for you, Isaac!

Kraden    : Who are you guys?

Satrage   : The name's Satrage. You took me out in the last round at Colosso.

Azart     : And I'm Azart!

Navampa   : And don't forget Navampa!

Isaac     : Oh. It's you guys.

Satrage   : Is that any way to say hello to some old friends?

Isaac     : What's your problem?

Azart     : We want to talk to you about your fighting style at Colosso.

Navampa   : Yeah. And we think you shouldn't have won, Isaac. We think you
            didn't fight fair.

Kraden    : It sounds like you resent the fact that Isaac beat you...

* - They shake their heads.

Navampa   : We've just been thinking about it, and there's no way that Isaac
            should have won!

Isaac     : Right. So you think I cheated just because I used my Psynergy
            abilities in Colosso?

Azart     : I don't know how you did it. I'm just sayin' I think you cheated
            is all...

Kraden    : Ah, but Psynergy is a warrior's skill, every bit as much as your
            sword arts. It isn't cheating.

Navampa   : You're not listening, are you, old man? The fight was fixed,
            and we're here to pay you back!

* - The three gladiators engage the group in combat. After the fight:

Azart     : These guys were phenomenal!

Satrage   : Which one of you didn't think they won Colosso fair and square?

Azart     : It wasn't me! I think both you and Navampa were saying something
            like that.

Isaac     : So. You don't still think our victory at Colosso was fixed, do you?

Navampa   : No way, Isaac! We've seen the error of our ways!

Satrage   : We promise we won't badmouth you or call you a fraud ever again.
            Will you forgive us?

-----------------------------------------------------------
     -(Yes)
Satrage   : You're not such a bad kid after all!



     -(No)
Satrage   : Don't be that way! We've learned our lesson! Forgive us!

* - He repeats the same plea every time you say no.
-----------------------------------------------------------

* - After saying yes:

Navampa   : You came out here looking for treasure, didn't you?

* - He sets down a Golden Shirt.

Navampa   : Here, this was in the chest we found.

Azart     : You were nice enough to forgive us, so we think you should have it.

Navampa   : Right, well... I guess we'll be leaving now.

Satrage   : By the time the next Colosso rolls around, we ought to be strong
            enough to win for sure!

Azart     : Maybe we'll see you there.

* - They depart.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [03'03] ---    Naribwe Fortuneteller    --- [03'03] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

I am a teller of fortunes. Would you have a reading?

-----------------------------------------------------------
     -(Yes)
It's 20 coins to hear what your future holds. Will you pay?


    --(No)
Then stand back.


    --(Yes)
* - Insufficient funds:

Many want things they cannot afford. If you do not have the money, you will have
no reading.

* - Sufficient funds:

Very well. Show me one of your items.

* - The selected item is placed on the table.

Are you prepared?


   ---(Yes)
I shall begin my reading...


   [ Weapons ]
I see... Beyond the weapon you set down lies a terrible foe. Many enemies await
you, far beyond the mountains. If you move to strike them... you will meet with
great disaster.

* - After Kibombo:

I see... Beyond the weapon you set down lies a terrible foe. In a misty sea,
a mighty foe... A fearsome battle awaits you. Gather the pieces of the weapon
to defeat him, or drown in defeat yourself.

* - After defeating Poseidon:

I see... Beyond the weapon you set down lies a terrible foe. None in the eastern
world can stand against the power you possess.





   [ Armor ]
I see... From the garb you have placed before me, I sense the presence of
the one you await. To the southeast... in the plains of the southern continent
in the Eastern Sea... The one you seek awaits.

* - After Jupiter Lighthouse:

I see... In the item you have placed before me, I can see nothing of
the future...





   [ Items that bestow Psynergy when equipped ]
I see... I feel a shining power glowing beyond the item before me. A distant
isle lies far to the northeast... Sail there. High atop a rocky peak, a power
awaits you.

* - After learning Sand at Gaia Rock:

I see...  I feel a shining power glowing beyond the item before me. The eastern
lands hold litle for you now. You will not remain here long... I see you
opening a channel between the continents and sailing the Western Sea!





   [ Trident ]
* - Any prong:

I see... The object you have placed before me wields a mighty power over a
terrible foe.

* - He continues. What he says depends upon which prongs have been acquired
    (there's an expected order; if the last two prongs are found before
    the intended first, then only the first's location is revealed)

    Before finding the right prong:

Near the beach where you washed ashore lie ancient ruins. Seek them out.

* - After finding the right prong:

In the northern reaches of the Eastern Sea lies moss-covered, overgrown ruins.
You should explore them.

* - After finding the left prong:

In the distant south lies an icy cape. Above the rocky shore stands a tower.
Climb it.

* - After acquiring all three prongs:

I see... The object you have placed before me wields a mighty power over a
terrible foe. You have the weapon you need in many fragments... Bring them to
the people at the eastern edge of the northern continent.



* - Reforged Trident:

I see... That object you have placed before me... It is a fearsome weapon to a
particular beast. If you wield this weapon, you can defeat the legendary beast!

* - After defeating Poseidon:

I see... That object you have placed before me... It is a fearsome weapon to a
particular beast. But there are no more beasts for you to fear in this part of
the world.





   [ Other items (e.g., Herb) ]
I see... Beyond the item before me, I see a path for you to follow. I see you
inside a sacred icon. By listening to the voices, you will earn a precious item.

* - After Kibombo:

I see... Beyond the item before me, I see a path for you to follow. You must
forge a weapon to defeat a mortal enemy. Seek out the pieces!

* - After acquiring the three Trident prongs, but before having them reforged:

I see... Beyond the item before me, I see a path for you to follow. You will
raise a mighty column and gain assistance where it is least expected.

* - After the ship is Alhafra is repaired:

I see... Beyond the item before me, I see a path for you to follow. You will
gain trmendous help from a village on the eastern reaches of the northern lands.
Seek them out.

* - After acquiring the Trident:

I see... Beyond the item before me, I see a path for you to follow. You have
the weapon you need to defeat the sea beast. Go to the sea of mists and
face your foe!

* - After Lemuria:

I see... Beyond the item before me, I see a path for you to follow. The object
that you seek lies somewhere in the west. Why do you linger in the eastern
world? If your work is done, the west beckons you.





   ---(No)
Shall I give you another reading for a different item?

* - If "Yes," the player is prompted to select another possession. If "no":

Then away with you.
-----------------------------------------------------------


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [03'04] ---       Optional Bosses       --- [03'04] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

#$#$#$#$#$#$#$#$#$#$#
$#  Treasure Isle  #$
#$#$#$#$#$#$#$#$#$#$#

* - In the final room, Felix's group encounters the Star Magician.

Magician  : I am the guardian of water. If you would claim my power, you must
            prove your worth.

* - Star Magician guards the summon tablet for Azul.


#$#$#$#$#$#$#$#$#$
$#  Islet Cave  #$
#$#$#$#$#$#$#$#$#$

* - In the final room, Felix's group encounters a knight.

Sentinel  : I am the guardian of wind. If you would claim my power, you must
            prove your worth.

* - Sentinel guards the summon tablet for Catastrophe.


#$#$#$#$#$#$#$#$#$#$#$#$#
$#  Yampi Desert Cave  #$
#$#$#$#$#$#$#$#$#$#$#$#$#

* - In the final room, Felix's group encounters a demon.

Valukar   : I am the guardian of fire. If you want my power, prove yourself
            in my crucible of flame.

* - Valukar guards the summon tablet for Daedalus.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$
$#  Anemos Inner Sanctum  #$
#$#$#$#$#$#$#$#$#$#$#$#$#$#$

* - There is a circle in Contigo on which one can use Teleport, thus gaining
    access to the interior of Anemos Sanctum.

    The first room contains four circles associated with an element, each being
    enclosed by eighteen smaller circles. As Felix stands atop a larger circle,
    the Djinn of its element give power to those around it. If every circle is
    activated, then a door opens.

    Upon approaching a summon tablet in the second room, which sits upon a
    drawing of a skeleton:

?????     : We inherited the power of the land to create a great darkness.
            If you crave this power, attack this slate!

* - The tablet allows one to summon Charon.

    In the final room, Felix's group encounters a headless suit of armor.

Dullahan  : I am the shadow, the keeper of light. If you want the sun's power,
            show me your own.

* - Dullahan guards the summon tablet for Iris.


#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$# [03'05] ---          Link Lobby         --- [03'05] #$#
#$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#

* - (This section contains spoilers for 02'40)

    Only {S} script is available.


    Before any linked battles in a given session:

    {1}  =  Felix is active, character is active
    {2}  =  Felix is active, character is inactive
    {3}  =  Felix is inactive

    After winning a linked battle:

    {4}  =  Character is active
    {5}  =  Character is inactive

    After losing a linked battle:

    {6}  =  Character is active
    {7}  =  Character is inactive

Jenna     :{1} Hey, I'll do my best if you do yours!

           {2} OK, I'll be waiting right here. Do your best, and hurry back.

           {3} Wait, I say I'll fight, and then you back out of it?
               What's that all about?


           {4} You know, you would never have won without me.

           {5} Sure, you won, but...it would have been a lot easier if I'd
               been there, huh?


           {6} Wow. That was a serious beating... What happened to us?

           {7} Of course, you're going to lose if you have such an awful
               attitude about it!

Sheba     :{1} You don't even want to try? I'll show you my power.

           {2} Don't you want me with you anymore, Felix?

           {3} Good luck, Felix! If you want me, you know where to find me.


           {4} Yeah... That didn't offer a lot of challenge.

           {5} Oh, you won? Yeah, that's great. But you still left me behind!


           {6} I was doing my very best. I certainly hope you were, too.

           {7} If you'd taken me with you, none of this would ever have
               happened. Don't you forget it.

Piers     :{1} All right, Felix, we'll do it together!

           {2} Are you trying to tell me something, Felix?

           {3} So it's just me. Is that all right? I'm a little nervous.


           {4} I gave it my best effort, as you could see.

           {5} That was a stunning battle. I was on the edge of my seat.


           {6} Maybe it would have been better if I just hadn't come...

           {7} You should have asked for my help. From the look of things,
               you could have used it.

Isaac     :{1} It's our turn. Let's go, Felix.

           {2} OK, we're set, Felix. But remember, you're calling the shots,
               all right?. [sic]

           {3} I'll fight enough for both of us...


           {4} Everybody deserves a little credit for this victory!

           {5} Everybody did great! I didn't worry at all about you!


           {6} Don't blame yourself... It was just a bad strategy.

           {7} You win some, you lose some. That's the nature of competition.

Garet     :{1} Hey, Felix, I'm all set to show you what I've got.

           {2} What? I have to take a beak? Why do I have to do that?

           {3} If you don't want to fight, that's fine. We'll do better
               without you, no problem.


           {4} You can count on me, through thick and thin!

           {5} You won? Without me? Wow... Way to make a guy feel unneeded
               there.


           {6} Pull yourself together! We'll do it next time.

           {7} What? You lost? That's what you get for leaving me out!

Ivan      :{1} If you want me to fight, I'll do it, but don't expect anything
               amazing from me.

           {2} There's something really sad about being told to stay behind.

           {3} Huh? No way! Please fill in for me!


           {4} If I seemed nervous, it was only because I wasn't sure you were
               prepared for this.

           {5} You really stayed cool in the heat of battle. Good work!


           {6} You should have picked someone else. It's all my fault that
               we lost.

           {7} It's not a problem, Felix. You'll do better next time.

Mia       :{1} I'll do the best I can!

           {2} That's fine, I could use some rest anyway.

           {3} I'll do the best I can.


           {4} I'm glad we won... But don't you feel at all bad for your
               opponents?

           {5} The most important thing is that nobody got hurt.
               Except your opponents.


           {6} I didn't help out very much, did I? I'm sorry...

           {7} I know I wasn't out there with you, but...I still blame myself.



[001]     : Welcome to Battle Arena, where the elite meet to battle one another!
            Test your skills in Linked Battles and Monster Battles! Speak to the
            girl at the counter if you're looking for a fight!

[002]     :   * - Monster battle:

            You do not have an opponent. Would you like to battle a monster?

            -----------------------------------------------
                 -(Yes)
            When you finish your preparations, please step into the circle!

            Good luck!


              * - Upon winning a battle:

            Not bad! Would you like to fight the next monster?

                --(Yes)
            Good luck!

                --(No)
              * - The session ends.


            You won <#> battle<s>. You broke the record!

            You won <#> battle<s>. Please speak to me when you wish to
            battle again.

            You won 0 battle. I told you our monsters were tough!
            Please try again.



                 -(No)
            Please wait until an opponent arrives, then.
            -----------------------------------------------



              * - Linked battle:

            Please speak to me when you want to fight in a battle.

            Would you like to apply?

            -----------------------------------------------
                 -(Yes)
            You have asked for a battle. We will call your name if your opponent
            accepts. Please wait.

            When you finish your preparations, please step into the circle!



                 -(No)
            Please speak to me when you want to fight in a battle.
            -----------------------------------------------


            Your opponent has asked for a battle. Do you accept?

            -----------------------------------------------
                 -(Yes)
            When you finish your preparations, please step into the circle!



                 -(No)
            Please speak to me when you want to fight in a battle.
            -----------------------------------------------


              * - After both of the players have agreed to battle:

            If you want to participate, please step into the circle!

[003]     : I will tell you your total wins when you finish the linked finals.

              * - After a record has been set:

            You've won <#> Linked Battle<s>. Keep up the good work!

[004]     : I can't wait to see how many Monster Battles you win. I'll be
            counting your victories!

              * - After a record has been set:

            You've won <#> consecutive Monster Battle<s>. Keep up the good work!

* - [005] is quivering.

[005]     : I don't have the guts to fight in the battle arena. I'll just be
            sitting here, if that's OK.

[006]     : Should I enter or not? I'm so stressed about this...

[007]     : I like my men macho. You...don't work out much, do you?

[008]     : You look a little scrawny, but guys like you are often surprisingly
            strong... Fighting a guy with a build like that would really wear
            me out! Whew!

              * - Subsequently:

            I'll be rooting for you! Do your best!

[009]     : In the linked finals, you can't delay after your opponent selects
            a move. If you don't choose your command within 15 seconds,
            you automatically defend.

[010]     : Up to three allies can fight in the linked finals... So all of you
            can fight!

              * - After Piers joins Felix:

            Up to three allies can fight in the linked finals. There are four
            in your party, so the rightmost ally will have to pass.

              * - After Isaac's group joins Felix:

            Up to three allies can join you in a Link Mode battle. Your party
            has eight allies total, so only the three allies on the left of
            the list can fight.



              * - He alternates between saying one of the above and:

            You can change the order of your party in the status screen.
            But you knew that, right?

[011]     : Sometimes, your class changes when you unleash a Djinni. You need to
            watch that, because it can get you into some real trouble if you're
            not careful.

[012]     : You could use Psynergy, Djinn, even summons and items! There are
            a lot of battle strategies...


                                End of Document
Restore Page

