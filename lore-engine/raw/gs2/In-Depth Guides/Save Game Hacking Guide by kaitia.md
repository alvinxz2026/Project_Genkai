---
source_id: kaitia-savehack
author: kaitia
url: https://gamefaqs.gamespot.com/gba/561356-golden-sun-the-lost-age/faqs/30811
type: data-table
covers: [items, djinn, summons, psynergy, classes, characters, ids]
quality: default
summary: 存档 hex 地址（角色属性/元素强度/状态/psynergy/djinn/summon/item/arena 等）。非叙述提取源；价值在于做 canonical id/master-data 与校验。
gs1_counterpart:
notes: 这个和Mr_UnOrigino的那个一样，我觉得这个可以用来给我们的数据提供identifier。后面是不是可以做个master data之类的东西出来？你Note一下，先不用通读，后面我单独用一轮来处理这些。
---

# Save Game Hacking Guide by kaitia

## TABLE OF CONTENTS

- A. INTRODUCTION
    - A1. Update Log
    - A2. About Golden Sun and this Guide
    - A3. Frequently Asked Questions
    - A4. Save Game Hacking
    - A5. Golden Sun Hacking and Saving <<VERY IMPORTANT>>
- B. HEX ADDRESSES
    - B1. Checksums 
    - B2. Character Stats
        - B2a. Organized by Character
        - B2b. Organized by Stat
    - B3. Elemental Strength
    - B4. Status
    - B5. Psynergy
    - B6. Djinn
    - B7. Summons
    - B8. Items
    - B9. Party
    - BA. Story Reset Codes
    - BB. Chest Reset Codes
    - BC. Save Locations
        - BCa. File Select Location
    - BD. Miscellaneous
        - BDa. File Select Name 
        - BDb. Coins
        - BDc. Game Settings
        - BDd. Arena Battles
- C. CONCLUSION
    - C1. Credits and Thanks
    - C2. Contact Information
    - C3. Legal Information and Allowed Sites
    - C4. Still to Come


---

END OF TABLE OF CONTENTS

---

~*=================================*~
 +                                 +
 +  GOLDEN SUN: THE LOST AGE       +
 +  SAVE GAME HACKING GUIDE        +
 +  Version 0.71 (3/24/05)         +
 +                                 +
 +  By kaitia                      +
 +  DDragon962@aol.com             +
 +                                 +
~*=================================*~

I cannot stress this enough: Always make a backup of your old save file!


=====================================================================


  **************************
~*== PART A. Introduction ==*~
  **************************

 ******************
== A1. Update Log ==
 ******************

03/24/05 (0.71) - Holy lack of update. Read the last section of the guide for 
some other stuff, yay.
 * Location values are under way to be decoded
 - Chest Reset Codes added
 - Revised some of the tutorial and FAQ

12/04/04 (0.69) - Aight, here's what's in store for today:
 - Arena Monster Battle modifier
 * Psynergy finally figured out! And it's about 100% complete! Yay!

10/31/04 (0.56) - Today's Halloween, heh. I've done a little bit of errata in 
various sections; nothing really important about that. This time, I've got 
some Elemental Strength modifiers for you to feast your eyes on. Hooray!

10/23/04 (0.52) - Yes, it's been three months since I've updated this guide. 
Sorry for being lazy and whatnot, but I've made up for it by discovering how 
to reset the entire plot of Golden Sun 2! Yay. Check out the Story Reset Code 
for all the juicy details. I also did a little bit of revamping to the table 
of contents structure.

07/24/04 (0.47) - Edited the checksum section a tidy little bit, so check out 
what's changed. Also, there's a new and probably completed section for Game 
Settings, which is a fun little piece. 

07/17/04 (0.45) - Guess what! I found the checksum! It's so cool! Anyways, 
I've still got a couple of loose ends in Party to wrap up. Some people have 
emailed me about exactly how to rip your game onto the computer, so I've 
updated the FAQs for that.

07/10/04 (0.26) - A small update; I just wanted to wrap up Statuses.
 - Statuses section completed
 - Added a new allowed site: Gaming Vortex.

07/04/04 (0.25) - Happy July 4th everyone! I hope you're all enjoying your 
fireworks, cause you're gonna want to celebrate after I tell you what's this 
update!
 - Base Stats completed
 - Character Levels completed
 * Character Stats section finished. Isn't that a lovely thing?
 - Statuses section started
 - Contact Information slightly altered
 - Updated File Select Name with a little bit of new info
I forgot to mention that last time; I changed the address display system from 
something like XEF2 to 3EF2. It's just a whole lot simpler to read, see?

07/01/04 (0.19) - I did a TON of stuff, both updated and new. So much new 
stuff, that I need to list them all out.
 - Names section completed
 - Current Luck completed
 * New section: File Select Name
 - Classes started and completed 
 - Party section about 75% done
 * Summons section started and finished
 - Gave Status its own section, and did about 10% of it
 - Some FAQs for your questioning pleasures have been added.
I also started fiddling around with other things, but not enough to warrant 
writing about it. See "Still to Come" for them. There are also a couple of 
smaller updates here and there.

06/18/04 (0.09) - Initial Release at GameFAQs. Yeah, it's a new guide.


 ***************************************
== A2. About Golden Sun and this Guide ==
 ***************************************

Golden Sun is a very wonderful RPG made by Camelot for the GameBoy Advance. 
Combining a simple yet intuitive RPG engine with puzzle-based dungeons, it 
became a huge hit for RPG fans (although many people also detest this game).

Anyways, the Story of Golden Sun is divided into two parts: Golden Sun, 
starring Isaac, Mia, Ivan, and Garet; and Golden Sun: The Lost Age, starring 
Felix, Jenna, Sheba, and Piers. This save game hacking guide covers The Lost 
Age, and The Lost Age ONLY. Don't try using hex addresses from this guide in 
the original Golden Sun, as I guarantee you that there will be quite some 
unpleasantries with your results...

In addition, this guide is to be only used with the US or (U) version of the 
game. Games from other regions use similar formats, but they will not give 
you the same results (trust me, I've tried).

So why did I write this guide? Fame and glory? A great contribution to 
society? Something like that. Basically, I liked the results of save 
game/state hacking with other games, so I decided to get my hands a little 
dirty. I hope you enjoy this guide.


 **********************************
== A3. Frequently Asked Questions ==
 **********************************

Q. How am I supposed to get a copy of Golden Sun: The Lost Age onto my 
computer?

A. Well, the two most popular methods are either to rip the ROM image 
directly from your GBA cart, or to download the ROM image off the internet. 
The former method is not recommended due to possibly high costs, while the 
latter method is also not recommended because it's rather illegal. There are 
vendors on the internet which sell cables to do the ripping; I'm not gonna 
list them. For your save file to appear on the computer, if you already have 
a ROM on the computer, the simplest way is to take a Gameshark, use the 
Snapshot feature to get your save into a .sps file, then import it onto your 
computer and VisualBoy Advance.

Q. Where can I download the ROM for Golden Sun: The Lost Age?

A. Get the hell out. Not only have I FORGOTTEN where to find the ROM, it's 
totally illegal to download these things. If you really want to download the 
ROM, just run it through Google and your fears may be assuaged.

Q. I'm doing everything you tell me to do and my changes aren't working!

A. Well, the two most probable reasons as to why it isn't working is: you 
messed up the checksum, or you're changing the wrong addresses. For the first 
reason, make sure you've selected the correct range of addresses to be 
checked and that you've properly reversed the values as documented further in 
this guide. As for the second reason, remember that just because I'm listing 
addresses using 3xxx doesn't mean that those are the addresses you're trying 
to find! Depending on your game, your values could be in the realm of 6xxx or 
even Cxxx! So, make sure you're hacking the right library.


 *************************
== A4. Save Game Hacking ==
 *************************

What's this? You've never heard of save game hacking before? Well, allow me 
to attempt to explain the basics of it to you. If you are rather familiar 
with the concept of save game hacking (not save STATE hacking, mind you. If 
you are only familiar with save state hacking, read the section about 
checksums), then you can probably skip ahead to Section A5, which pertains 
specifically to Golden Sun 2's save scheme.

On your little GBA cart, there's the game itself, and some RAM memory which 
holds all the game data from your saves. Save game hacking deals with the 
direct manipulation of those game saves. And by direct, I mean actually going 
into the save file and editing the pure machine code of the save.

So how does one go about mucking inside a GBA save file? Well, you'll need a 
hex editor; preferably, one which can calculate hash/checksums. I personally 
like using WinHex the best, but most people will recommend using Hex Workshop. 
These programs are available via shareware, and you can get them at 
www.download.com.

Start up the hex editor, and open up your .sav file of Golden Sun: The Lost 
Age. You'll be greeted with a sort of matrix of numbers: A long string of 
numbers and letters on the left, and sometimes a two-digit representation at 
the top. Usually, at the left you'll have a table of various letters and 
symbols.

First off, let me explain the hexadecimal system to you. Every computer in 
the world is built off a series of switches. They can either be off or on, 
which leads to a two-number binary system. We count everything in like using 
the decimal system, which utilizes TEN numbers. It's quite unfortunate that 
these two systems are difficult to convert from one to another.
Enter the hexadecimal system. It uses sixteen digits, 0-9, then A-F. Since 
sixteen is a power of 2, hex and binary can be easily swapped. That's what 
the hex editor does. It gives the hexadecimal version of any file on your 
computer, and allows you to edit it directly.

You see how the hex numbers are grouped by two? Each group of two is a byte 
of data. It's important for you to realize this.

Of course, it'd be immensely difficult to index all of this mass of hex. 
Enter the address, also known as the offset. At the left, you'll have a 
column of hex number like this:

00000000
00000010
00000020
00000030
00000040

and continues on...

00003AD0
00003AE0
00003AF0
00003B00

And so on, all the way to the very last spit of data. If your left column 
doesn't increment by 10 like this, I advise you to resize the window until it 
does. It just becomes so much easier to index this way.

Each row contains the addresses of that series of numbers. Like this:

00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

Remember, hex is a base sixteen numbering system, so after 0F (which is 15 in 
decimal, by the way), the next number is 10.

Each address contains the byte stored there, which is the mass of hex numbers 
you see in the general center of the screen. For example:

          00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

00000000  34 B3 03 12 00 00 00 00 00 2E DA 0F 2A A5 EA B0
00000010  2A 92 00 27 7E 8B 00 00 00 00 32 2E 02 84 61 40
00000020  FF E3 CA 09 FF FF FF FF A2 8B 3F 3C D0 00 2E 3A

String of bytes often contain long string of nothing, 00, or the maximum 
amount, FF, which is 255 (16 * 16 - 1).

So, how does one go about storing data in these hex addresses? Let's use 
addresses 13 from above, 27. Just for example, let's say that Felix's level 
is stored at this address. 27(hex) = 39 (dec). So in this particular save, 
Felix's level has been saved as 39. Let's say you want to increase his level 
to say, 75, which is 4B in hex. So, at address 13, change the 27 into a 4B by 
just typing over it. MAKE SURE YOU HAVE THE CURSOR SET TO OVERWRITE MODE. If 
you just insert the number 4B into that slot, guess what? You've just shifted 
all the addresses after by a byte. And that will seriously screw up your data.
So stay safe, folks, and ALWAYS BACK UP YOUR DATA. Anyways, like I said 
before, the maximum amount you can write into a byte is FF, or 255. So you 
can hack Felix's level all the way up to 255! Sweet.

But what about values which will likely go over 255, like you HP? Well, the 
obvious thing to do would be to write it to more than one byte. So, let's say 
you want Felix's attack to be 874. That makes it 36A in hex. But if you look, 
there are only three digits, and you need four to make two bytes! Just parse 
extra zeroes to the left side. So now you have 036A. When writing numbers 
over a byte in length, the game will use the self-proclaimed "reverse byte" 
method. What it will do is split your address into bytes, then write them 
backwards into the file. So it's like this for your attack: 03 6A -> 6A 03. 
And for larger values like 83E27B: 83 E2 7B -> 7B E2 83.

In a perfect world, you'd just edit the data you want, save the file, load up 
your game, and POOF! All your changes have been made without breaking a sweat. 
Unfortunately, it's not a perfect world (or the world of save state hacking, 
for that matter ^_^), and the game uses the dreaded checksum to deter hackers 
like you and I. A checksum is essentially the sum of all the bytes in a 
specific section of data. The game usually writes the checksum at its own 
specific address(es). When the game loads, it checks to see if the sum of the 
bytes is equal to the number written in the checksum. If it is, then good, 
your file loads and all your hard work is paid off. But if it isn't, then the 
game essentially refuses to recognize the data even exists, and you'll be 
greeted with an empty save slot.

Let's say our smatch of data above has a checksum which is stored at 
000000030, and includes all the numbers from 13 to 2A. Add up each individual 
byte, and you get the number AD4. Again, use our parsing and reversing method 
to change it into D4 0A, and write the checksum at 000000030.

          00 01
000000030 D4 0A

Luckily for you, you don't need to add up all those numbers by hand if you 
have WinHex or Hex Workshop. They include a built-in feature which allows you 
to compute the checksum of a selected piece of data. Just muck around until 
you find "Calculate hash/checksum" or something to that extent. Which type of 
checksum you want to use depends on what type of the checksum the game has 
used. 

Well, there you go. That's everything I know about save game hacking.


 *************************************
== A5. Golden Sun Hacking and Saving ==@@@@VERY IMPORTANT!!!!@@@@
 *************************************

Golden Sun: The Lost Age uses some tricks to make life better for the gamer 
but worse for the hacker. First off, each save file uses at least three 
checksums, and to make matters worse, they're located right in the middle of 
your data as opposed to at the start or end of it.

Second of all, there are five so-called "libraries" where a save game can be 
possibly stored. You probably might ask, "But wait, Mr. Kaitia, aren't there 
only three save files in Golden Sun: The Lost Age?" and I'll reply, "Yes 
little grasshopper, there ARE just three save files." Basically, whenever you 
save your game, your data is saved into two of these libraries at a time. 
This is useful because if you interrupt the save process by doing something 
like running out of batteries at that time (which I unfortunately had happen 
to me twice), your data is likely to be safe because your data was backed up 
at another library. Each library fits nicely into a 3000 byte block and 
begins with the word "CAMELOT".

But which libraries correspond to which save file? To tell you the sad truth, 
I DON'T KNOW YET. Sorry. You'll have to manually use a hex value search to 
find which libraries contain your data.

For now, I'll be using the 3000 save library when listing the addresses. Just 
add or subtract 3000 to get the values for the other libraries. Not only are 
3000, 4000, and 5000 nice easy numbers to remember, but the first save file 
likes to have one of its libraries located here.

Note that while you can alter certain pieces of data without breaking the 
checksum, the game may give you a (Data is corrupted) error at your file 
select. Your data SHOULD still load perfectly fine unless you messed with 
things you shouldn't have.

Also, this game frequently stores backup pieces of data. So if you want to 
search for values, keep that in mind. You may find duplicates of the data 
you're searching for, but not all of those addresses may be correct.

And as a general rule of thumb when hacking, ALWAYS keep backups of your data. 
I can not stress this enough. Remember to back up your files!

Okay! Let's start up this guide.


=====================================================================


  ***************************
~*== PART B. Hex Addresses ==*~
  ***************************

 *****************
== B1. Checksums ==
 *****************

Checksum          -> 3008 to 3009
Range of checksum -> 3010 to 5FFF

That's a nice, easy 16-bit checksum there. For WinHex users, you can easily 
highlight the checksum range by going to the Edit menu, then go to Define 
Block. Put 3010 in the top box and 5FFF in the bottom one. Make sure you have 
your hex editor calculate the 16-bit checksum for the selected data. Not 32-
bit, not MD5, not CRC32. Remember to take the resulting dword and use the 
reverse byte method on it.


 ***********************
== B2. Character Stats ==
 ***********************

Let me explain how section G works. First, I'll just give you straight the 
addresses for most of the stats of the characters. It'll be straight up, no-
hassle information. But you probably want more detail, so the second section 
lists the offsets by statistic, so that I may better explain each part. If 
you don't understand what to do in a certain part, chances are it'll be 
better explained in the second section. You may also notice that many of the 
statistics follow one right after the other.

 *****************************
~ B2a. Organized by Character ~
 *****************************

 ********************
= FELIX, Earth Adept =
 ********************

Name              -> 3A60 to 3A6E
Level             -> 3A6F
Experience        -> 3B84 to 3B86

Current HP        -> 3A98 to 3A99
Base HP           -> 3A70 to 3A71
Max HP            -> 3A94 to 3A95

Current PP        -> 3A9A to 3A9B
Base PP           -> 3A72 to 3A73
Max PP            -> 3A96 to 3A97
                     
Current Attack    -> 3A9C to 3A9D
Base Attack       -> 3A78 to 3A79

Current Defense   -> 3A9E to 3A9F
Base Defense      -> 3A7A to 3A7B

Current Agility   -> 3AA0 to 3AA1
Base Agility      -> 3A7C to 3A7D

Current Luck      -> 3AA2
Base Luck         -> 3A7E

Class             -> 3B89


 *******************
= JENNA, Fire Adept =
 *******************

Name              -> 3BAC to 3BBA
Level             -> 3BBB
Experience        -> 3CD0 to 3CD2

Current HP        -> 3BE4 to 3BE5
Base HP           -> 3BBC to 3BBD
Max HP            -> 3BE0 to 3BE1  

Current PP        -> 3BE6 to 3BE7
Base PP           -> 3BBE to 3BBF
Max PP            -> 3BE2 to 3BE3

Current Attack    -> 3BE8 to 3BE9
Base Attack       -> 3BC4 to 3BC5

Current Defense   -> 3BEA to 3BEB
Base Defense      -> 3BC6 to 3BC7

Current Agility   -> 3BEC to 3BED
Base Agility      -> 3BC8 to 3BC9

Current Luck      -> 3BEE
Base Luck         -> 3BCA

Class             -> 3CD5


 *******************
= SHEBA, Wind Adept =
 *******************

Name              -> 3CF8 to 3D06
Level             -> 3D07
Experience        -> 3E1C to 3E1E

Current HP        -> 3D30 to 3D31
Base HP           -> 3D08 to 3D09
Max HP            -> 3D2C to 3D2D  

Current PP        -> 3D32 to 3D33
Base PP           -> 3D0A to 3D0B
Max PP            -> 3D2E to 3D2F

Current Attack    -> 3D34 to 3D35
Base Attack       -> 3D10 to 3D11 

Current Defense   -> 3D36 to 3D37
Base Defense      -> 3D12 to 3D13

Current Agility   -> 3D38 to 3D39
Base Agility      -> 3D14 to 3D15

Current Luck      -> 3D3A
Base Luck         -> 3D16

Class             -> 3E21


 ********************
= PIERS, Water Adept =
 ********************

Name              -> 3E44 to 3E52
Level             -> 3E53
Experience        -> 3F68 to 3F6A

Current HP        -> 3E7C to 3E7D
Base HP           -> 3E54 to 3E55
Max HP            -> 3E78 to 3E79  

Current PP        -> 3E7E to 3E7F
Base PP           -> 3E56 to 3E57
Max PP            -> 3E7A to 3E7B

Current Attack    -> 3E80 to 3E81
Base Attack       -> 3E5C to 3E5D

Current Defense   -> 3E82 to 3E83
Base Defense      -> 3E5E to 3E5F

Current Agility   -> 3E84 to 3E85
Base Agility      -> 3E60 to 3E61

Current Luck      -> 3E86
Base Luck         -> 3E62

Class             -> 3F6D

---

 ********************
= ISAAC, Earth Adept =
 ********************

Name              -> 3530 to 353E
Level             -> 353F
Experience        -> 3654 to 3656

Current HP        -> 3568 to 3569
Base HP           -> 3540 to 3541
Max HP            -> 3564 to 3565  

Current PP        -> 356A to 356B
Base PP           -> 3542 to 3543
Max PP            -> 3566 to 3567

Current Attack    -> 356C to 356D
Base Attack       -> 3548 to 3549

Current Defense   -> 356E to 356F
Base Defense      -> 354A to 354B

Current Agility   -> 3570 to 3571
Base Agility      -> 354C to 354D

Current Luck      -> 3572
Base Luck         -> 354E

Class             -> 3659


 *******************
= GARET, Fire Adept =
 *******************

Name              -> 367C to 368A
Level             -> 368B
Experience        -> 37A0 to 37A2

Current HP        -> 36B4 to 36B5
Base HP           -> 368C to 368D
Max HP            -> 36B0 to 36B1  

Current PP        -> 36B6 to 36B7
Base PP           -> 368E to 368F
Max PP            -> 36B2 to 36B3

Current Attack    -> 36B8 to 36B9
Base Attack       -> 3694 to 3695

Current Defense   -> 36BA to 36BB
Base Defense      -> 3696 to 3697

Current Agility   -> 36BC to 36BD
Base Agility      -> 3698 to 3699

Current Luck      -> 36BE
Base Luck         -> 369A

Class             -> 37A5


 ******************
= IVAN, Wind Adept =
 ******************

Name              -> 37C8 to 37D6
Level             -> 37D7
Experience        -> 38EC to 38EE

Current HP        -> 3800 to 3801
Base HP           -> 37D8 to 37D9
Max HP            -> 37FC to 37FD  

Current PP        -> 3802 to 3803
Base PP           -> 37DA to 37DB
Max PP            -> 37FE to 37FF

Current Attack    -> 3804 to 3805
Base Attack       -> 37E0 to 37E1

Current Defense   -> 3806 to 3807
Base Defense      -> 37E2 to 37E3

Current Agility   -> 3808 to 3809
Base Agility      -> 37E4 to 37E5

Current Luck      -> 380A
Base Luck         -> 37E6

Class             -> 38F1


 ******************
= MIA, Water Adept =
 ******************

Name              -> 3914 to 3922
Level             -> 3923
Experience        -> 3A38 to 3A3A

Current HP        -> 394C to 394D
Base HP           -> 3924 to 2925
Max HP            -> 3948 to 3949  

Current PP        -> 394E to 394F
Base PP           -> 3926 to 3927
Max PP            -> 394A to 394B

Current Attack    -> 3950 to 3951
Base Attack       -> 392C to 392D

Current Defense   -> 3952 to 3953
Base Defense      -> 392E to 392F

Current Agility   -> 3954 to 3955
Base Agility      -> 3930 to 3931

Current Luck      -> 3956
Base Luck         -> 3932

Class             -> 3A3D



 ************************
~ B2b. Organized by Stat ~
 ************************

 ******
= NAME =
 ******

Obviously, this is what you're supposed to name your party members at the 
beginning of the game. You can now edit the names to your own accord. Just 
like the Gameshark codes, you can have a maximum of fourteen letters in your 
name without any glitches instead of the mere five the game allows you to 
have. Note that all of the letters may not display correctly at all times. 

Anyways, the producers have done us a great favor by making the hex digits 
align with most of the standard ASCII character set. So just open up your 
text table on your hex editor; then type away there. Note that most Extended 
ASCII characters won't look the same on the hex editor as they do on the game. 
For example, entering 80 as your value yields the "symbol" of the A button.

Entering 00 as an address' value acts as a "stop" byte, which is known in the 
programming world as null termination. The character's name will always end 
at the 00 value, regardless of what you put after the 00. If you wish to 
enter a space in the name, use the value 20, also known as 032 in ASCII. 

In addition, there are TWO sets of addresses which correspond to Felix's name. 
I only included the set that you probably want. The other set is explained in 
the "File Select Name" section.

|Felix|           -> 3A60 to 3A6E
|Jenna|           -> 3BAC to 3BBA
|Sheba|           -> 3CF8 to 3D06
|Piers|           -> 3E44 to 3E52

|Isaac|           -> 3530 to 353E
|Garet|           -> 367C to 367A
|Ivan |           -> 37C8 to 37D6
| Mia |           -> 3914 to 3922


 *******
= LEVEL =
 *******

Your character level increases when you gain a certain amount of experience 
points. At every level up, you get an increase in stats, so normally, the 
higher the level, the better. But since we can hack into all the stats, Level 
has become useless. Level is stored in just a single byte.

|Felix|           -> 3A6F
|Jenna|           -> 3BBB
|Sheba|           -> 3D07
|Piers|           -> 3E53

|Isaac|           -> 353F
|Garet|           -> 368B
|Ivan |           -> 37D7
| Mia |           -> 3923


 ************
= EXP POINTS =
 ************

How useless is this? The only reason I'd see for you hacking into experience 
points is for bragging rights. Either that or you'd like a quick level up, 
but your "EXP points left" may use a different address. That doesn't seem to 
be the case, so don't worry about it.

|Felix|           -> 3B84 to 3B86
|Jenna|           -> 3CD0 to 3CD2
|Sheba|           -> 3E1C to 3E1E
|Piers|           -> 3F68 to 3F6A

|Isaac|           -> 3654 to 3656
|Garet|           -> 37A0 to 37A2
|Ivan |           -> 38EC to 38EE
| Mia |           -> 3A38 to 3A3A


 ************
= HIT POINTS =
 ************ 

Mmm, delicious hit points. With this, you can really jack up your life 
expectancy. Laugh as the pitiful enemies chop off just 1% of your HP with 
their strongest attack! Ha ha ha! Anyways, there are three fields for Hit 
Point: Current, Base, and Max. Current is your current HP, obviously; Base HP 
sets your base HP for use in class calculations and such; while Max HP sets 
your current maximum hit points. Take note that you can change your max HP 
and keep it like that for a while, but when you do something which invokes 
the Base HP calculation, you'll lose your change unless you changed Base HP 
as well. In short, it's rather useless to change Current HP; change the Base 
HP instead. Hit Points are stored over two bytes.

|Felix|
Current HP        -> 3A98 to 3A99
Base HP           -> 3A70 to 3A71
Max HP            -> 3A94 to 3A95

|Jenna|
Current HP        -> 3BE4 to 3BE5
Base HP           -> 3BBC to 3BBD
Max HP            -> 3BE0 to 3BE1

|Sheba|
Current HP        -> 3D30 to 3D31
Base HP           -> 3D08 to 3D09
Max HP            -> 3D2C to 3D2D

|Piers|
Current HP        -> 3E7C to 3E7D
Base HP           -> 3E54 to 3E55
Max HP            -> 3E78 to 3E79  


|Isaac|
Current HP        -> 3568 to 3569
Base HP           -> 3540 to 3541
Max HP            -> 3564 to 3565  

|Garet|
Current HP        -> 36B4 to 36B5
Base HP           -> 368C to 368D
Max HP            -> 36B0 to 36B1  

|Ivan |
Current HP        -> 3800 to 3801
Base HP           -> 37D8 to 37D9
Max HP            -> 37FC to 37FD

| Mia |
Current HP        -> 394C to 394D
Base HP           -> 3924 to 3925
Max HP            -> 3948 to 3949  


 *****************
= PSYNERGY POINTS =
 *****************

Psynergy points work much like HP, except they are used to determine how many 
more spells you can cast. Just like before, there are three fields, Current, 
Base, and Max PP, and you need to invoke the Base PP to make any noticeable 
differences.

|Felix|
Current PP        -> 3A9A to 3A9B
Base PP           -> 3A72 to 3A73
Max PP            -> 3A96 to 3A97

|Jenna|
Current PP        -> 3BE6 to 3BE7
Base PP           -> 3BBE to 3BBF
Max PP            -> 3BE2 to 3BE3

|Sheba|
Current PP        -> 3D32 to 3D33
Base PP           -> 3D0A to 3D0B
Max PP            -> 3D2E to 3D2F

|Piers|
Current PP        -> 3E7E to 3E7F
Base PP           -> 3E56 to 3E57
Max PP            -> 3E7A to 3E7B


|Isaac|
Current PP        -> 356A to 356B
Base PP           -> 3542 to 3543
Max PP            -> 3566 to 3567

|Garet|
Current PP        -> 36B6 to 36B7
Base PP           -> 368E to 368F
Max PP            -> 36B2 to 36B3

|Ivan |
Current PP        -> 3802 to 3803
Base PP           -> 37DA to 37DB
Max PP            -> 37FE to 37FF

| Mia |
Current PP        -> 394E to 394F
Base PP           -> 3926 to 3927
Max PP            -> 394A to 394B


 **************
= STATIC STATS =
 **************

Yeah, static stats. These are the stats Attack, Defense, Agility, and Luck. 
They um... do stuff in battle. Attack determines how much damage you do to 
the enemy, Defense determines how much damage the enemy does to you, Agility 
determines the order that you move in battle, and Luck does a lot of things. 
Having high stats are good, yes they are. They're similar to HP and PP, 
except there's no "current" stat for each of them. All of the stats are 
stored over two bytes except for luck, which just has one. For consistency 
purposes, the byte after Current and Base Luck is always 01.

|Felix|
Current Attack    -> 3A9C to 3A9D
Base Attack       -> 3A78 to 3A79

Current Defense   -> 3A9E to 3A9F
Base Defense      -> 3A7A to 3A7B

Current Agility   -> 3AA0 to 3AA1
Base Agility      -> 3A7C to 3A7D

Current Luck      -> 3AA2
Base Luck         -> 3A7E

|Jenna|
Current Attack    -> 3BE8 to 3BE9
Base Attack       -> 3BC4 to 3BC5

Current Defense   -> 3BEA to 3BEB
Base Defense      -> 3BC6 to 3BC7

Current Agility   -> 3BEC to 3BED
Base Agility      -> 3BC8 to 3BC9

Current Luck      -> 3BEE
Base Luck         -> 3BCA

|Sheba|
Current Attack    -> 3D34 to 3D35
Base Attack       -> 3D10 to 3D11

Current Defense   -> 3D36 to 3D37
Base Defense      -> 3D12 to 3D13

Current Agility   -> 3D38 to 3D39
Base Agility      -> 3D14 to 3D15

Current Luck      -> 3D3A
Base Luck         -> 3D16

|Piers|
Current Attack    -> 3E80 to 3E81
Base Attack       -> 3E5C to 3E5D

Current Defense   -> 3E82 to 3E83
Base Defense      -> 3E5E to 3E5F

Current Agility   -> 3E84 to 3E85
Base Agility      -> 3E60 to 3E61

Current Luck      -> 3E86
Base Luck         -> 3E62


|Isaac|
Current Attack    -> 356C to 356D
Base Attack       -> 3548 to 3549

Current Defense   -> 356E to 356F
Base Defense      -> 354A to 354B

Current Agility   -> 3570 to 3571
Base Agility      -> 354C to 354D

Current Luck      -> 3572
Base Luck         -> 354E

|Garet|
Current Attack    -> 36B8 to 36B9
Base Attack       -> 3694 to 3695

Current Defense   -> 36BA to 36BB
Base Defense      -> 3696 to 3697

Current Agility   -> 36BC to 36BD
Base Agility      -> 3698 to 3699

Current Luck      -> 36BE
Base Luck         -> 369A

|Ivan |
Current Attack    -> 3804 to 3805
Base Attack       -> 37E0 to 37E1

Current Defense   -> 3806 to 3807
Base Defense      -> 37E2 to 37E3

Current Agility   -> 3808 to 3809
Base Agility      -> 37E4 to 37E5

Current Luck      -> 380A
Base Luck         -> 37E6

| Mia |
Current Attack    -> 3950 to 3951
Base Attack       -> 392C to 392D

Current Defense   -> 3952 to 3953
Base Defense      -> 392E to 392F

Current Agility   -> 3954 to 3955
Base Agility      -> 3930 to 3931

Current Luck      -> 3956
Base Luck         -> 3932


 *******
= CLASS =
 *******

There are many classes in the game, and they're controlled by the Djinn or 
items you have equipped at the time. Different classes grant you different 
stat boosts and psynergy, so it's important to alter your classes depending 
on your strategy. Classes are stored in just one byte, and the value you 
enter in the address determines the class that you have, regardless of Djinn 
and items. Similar to static stats, the class is followed by the consistency 
value of 02.

|Felix|           -> 3B89
|Jenna|           -> 3CD5
|Sheba|           -> 3E21
|Piers|           -> 3F6D

|Isaac|           -> 3659
|Garet|           -> 37A5
|Ivan |           -> 38E1
| Mia |           -> 3A3D

For the class values, assume that any value not listed results in a "?" class. 
Duplicate classes are listed with the element most commonly associated with 
them.

Class values:

00 - NPC
01 - Squire
02 - Knight
03 - Gallant
04 - Lord
05 - Slayer

0A - Guard
0B - Soldier
0C - Warrior
0D - Champion
0E - Hero

14 - Wind Seer
15 - Magician
16 - Mage
17 - Magister
18 - Sorcerer

1E - Water Seer
1F - Scribe
20 - Cleric
21 - Paragon
22 - Angel

28 - Swordsman (Earth)
29 - Defender (Earth)
2A - Cavalier (Earth)
2B - Guardian
2C - Protector (Earth)

32 - Swordsman (Water)
33 - Defender (Water)
34 - Cavalier (Water)
35 - Luminier
36 - Radiant

3C - Dragoon
3D - Templar
3E - Paladin

46 - Apprentice
47 - Illusionist (Earth)
48 - Enchanter (Earth)
49 - Conjurer (Earth)
4A - War Adept (Earth)

50 - Page
51 - Illusionist (Fire)
52 - Enchanter (Fire)
53 - Conjurer (Fire)
54 - War Adept (Fire)

5A - Ninja
5B - Disciple
5C - Master

64 - Seer (Water)
65 - Diviner (Water)
66 - Shaman (Water)
67 - Druid (Water)
68 - Oracle (Water)

6E - Seer (Wind)
6F - Diviner (Wind)
70 - Shaman (Wind)
71 - Druid (Wind)
72 - Oracle (Wind)

78 - Medium
79 - Conjurer (Water/Wind)
7A - Dark Mage

82 - Pilgrim (Water)
83 - Wanderer (Water)
84 - Ascetic (Water)
85 - Water Monk
86 - Guru

8C - Pilgrim (Fire)
8D - Wanderer (Fire)
8E - Ascetic (Fire)
8F - Fire Monk
90 - Protector (Fire)

96 - Ranger
97 - Bard
98 - Warlock

A0 - Brute
A1 - Ruffian
A2 - Savage
A3 - Barbarian
A4 - Berserker
A5 - Chaos Lord

AA - Samurai
AB - Ronin

B4 - Hermit
B5 - Elder
B6 - Scholar
B7 - Savant
B8 - Sage
B9 - Wizard

BE - White Mage
BF - Pure Mage

C8 - Flame User
C9 - Witch
CA - Hex
CB - Fire Master
CC - Justice

D2 - Mariner
D3 - Privateer
D4 - Commander
D5 - Captain
D6 - Admiral

DC - Pierrot
DD - Harlequin
DE - Punchinello
DF - Acrobat

E6 - Tamer
E7 - Trainer
E8 - Beastkeeper
E9 - Beast Lord

F0 - Dark Mage
F1 - Crypt Lord
F2 - Necrolyte
F3 - Necromage

Glitch classes:

F5 - Enemy
F6 - Waiting for opponent's input.
F7 - Mystery Man
F8 - Mystery Woman
F9 - Isaac appeared!
FA - Isaac appeared!
FB - Felix's party attacks first!
FC - Felix's party was caught by surprise!
FD - Isaac attacks!
FE - NPC
FF - Isaac is defending!

Obviously, if you named Isaac or Felix something different, those changes 
will be reflected in the last couple of classes.


 **************************
== B3. Elemental Strength ==
 **************************

Elemental Strength applies to your elemental level, power, and resistance to 
elemental attacks. Usually, this strength is determined by the amount of 
Djinn you equip to a character. But now, that is no more. I'd include this in 
the stats section, but it's a bit lengthy, so I put it here.

Notice how each of the various addresses increase by values of 2. In between, 
the value of the address will USUALLY be 00. You probably want to keep it 
that way, because increasing that value will decrease your resulting 
elemental strength. I'm still experimenting with these addresses, so keep a 
lookout.

Base Elemental Stats:

|Felix|
Earth Power       -> 3A84
Earth Resist      -> 3A86
Water Power       -> 3A88
Water Resist      -> 3A8A
Fire Power        -> 3A8C
Fire Resist       -> 3A8E
Wind Power        -> 3A90
Wind Resist       -> 3A92

|Jenna|
Earth Power       -> 3BD0
Earth Resist      -> 3BD2
Water Power       -> 3BD4
Water Resist      -> 3BD6
Fire Power        -> 3BD8
Fire Resist       -> 3BDA
Wind Power        -> 3BDC
Wind Resist       -> 3BDE

|Sheba|
Earth Power       -> 3D1C
Earth Resist      -> 3D1E
Water Power       -> 3D20
Water Resist      -> 3D22
Fire Power        -> 3D24
Fire Resist       -> 3D26
Wind Power        -> 3D28
Wind Resist       -> 3D2A

|Piers|
Earth Power       -> 3E68
Earth Resist      -> 3E6A
Water Power       -> 3E6C
Water Resist      -> 3E6E
Fire Power        -> 3E70
Fire Resist       -> 3E72
Wind Power        -> 3E74
Wind Resist       -> 3E76

|Isaac|
Earth Power       -> 3554
Earth Resist      -> 3556
Water Power       -> 3558
Water Resist      -> 355A
Fire Power        -> 355C
Fire Resist       -> 355E
Wind Power        -> 3560
Wind Resist       -> 3562

|Garet|
Earth Power       -> 36A0
Earth Resist      -> 36A2
Water Power       -> 36A4
Water Resist      -> 36A6
Fire Power        -> 36A8
Fire Resist       -> 36AA
Wind Power        -> 36AC
Wind Resist       -> 36AE

|Ivan |
Earth Power       -> 37EC
Earth Resist      -> 37EE
Water Power       -> 38F0
Water Resist      -> 38F2
Fire Power        -> 38F4
Fire Resist       -> 38F6
Wind Power        -> 38F8
Wind Resist       -> 38FA

| Mia |
Earth Power       -> 3938
Earth Resist      -> 393A
Water Power       -> 393C
Water Resist      -> 393E
Fire Power        -> 3940
Fire Resist       -> 3942
Wind Power        -> 3944
Wind Resist       -> 3946


Current Elemental Stats:

|Felix|
Earth Power       -> 3AA8
Water Power       -> 3AAA
Fire Power        -> 3AAC
Wind Power        -> 3AAE
Water Resist      -> 3AB0
Earth Resist      -> 3AB2
Fire Resist       -> 3AB4
Wind Resist       -> 3AB6

|Jenna|
Earth Power       -> 3BF4
Water Power       -> 3BF6
Fire Power        -> 3BF8
Wind Power        -> 3BFA
Water Resist      -> 3BFC
Earth Resist      -> 3BFE
Fire Resist       -> 3C00
Wind Resist       -> 3C02

|Sheba|
Earth Power       -> 3D40
Water Power       -> 3D42
Fire Power        -> 3D44
Wind Power        -> 3D46
Water Resist      -> 3D48
Earth Resist      -> 3D4A
Fire Resist       -> 3D4C
Wind Resist       -> 3D4E

|Piers|
Earth Power       -> 3E8C
Water Power       -> 3E8E
Fire Power        -> 3E90
Wind Power        -> 3E92
Water Resist      -> 3E94
Earth Resist      -> 3E96
Fire Resist       -> 3E98
Wind Resist       -> 3E9A

|Isaac|
Earth Power       -> 3578
Earth Resist      -> 357A
Water Power       -> 357C
Water Resist      -> 357E
Fire Power        -> 3580
Fire Resist       -> 3582
Wind Power        -> 3584
Wind Resist       -> 3586

|Garet|
Earth Power       -> 36C4
Earth Resist      -> 36C6
Water Power       -> 36C8
Water Resist      -> 36CA
Fire Power        -> 36CC
Fire Resist       -> 36CE
Wind Power        -> 36D0
Wind Resist       -> 36D2

|Ivan |
Earth Power       -> 3810
Earth Resist      -> 3812
Water Power       -> 3814
Water Resist      -> 3816
Fire Power        -> 3818
Fire Resist       -> 381A
Wind Power        -> 381C
Wind Resist       -> 381E

| Mia |
Earth Power       -> 395C
Earth Resist      -> 395E
Water Power       -> 3960
Water Resist      -> 3962
Fire Power        -> 3964
Fire Resist       -> 3966
Wind Power        -> 3968
Wind Resist       -> 396A


 **************
== B4. Status ==
 **************

Statuses applicable outside of battle include Poison, Venom, Curse, Haunt, 
and Down. There are no others, all the other statuses only carry on during 
battles.

Statuses are used in a bit of a strange way. Excepting Poison and Downed, 
which I'll explain later, the value for each address determines whether or 
not you are afflicted with that status. If the value is 00, then you will not 
have that affliction. If the value is anything higher than 00 (also known as 
ANY value besides 00), you will have that affliction.

Poison works in the same way, with one notable exception: having 01 as the 
value results in just a regular poison, while anything above 01 results in 
the character having Venom. And Downed obviously only exists when your 
character has 0 HP.

|Felix|
Curse             -> 3B90
Poison            -> 3B91
Haunt             -> 3BA0

|Jenna|
Curse             -> 3CDC
Poison            -> 3CDD
Haunt             -> 3CEC

|Sheba|
Curse             -> 3EB8
Poison            -> 3EB9
Haunt             -> 3EC8

|Piers|
Curse             -> 3F74
Poison            -> 3F75
Haunt             -> 3F84


|Isaac|
Curse             -> 3660
Poison            -> 3661
Haunt             -> 3760

|Garet| 
Curse             -> 37AC
Poison            -> 37AD 
Haunt             -> 37BC

|Ivan |
Curse             -> 38F8
Poison            -> 38F9
Haunt             -> 3908

| Mia |
Curse             -> 3A44
Poison            -> 3A45
Haunt             -> 3A54


 ****************
== B5. Psynergy ==
 ****************

These are the "magic" attacks that you can use during battle. Each Psynergy 
spell is stored over four bytes, and has two important characteristics: the 
first byte is the spell's value itself, and the second byte is what "type" of 
spell it is. So, let's take for example, Isaac's first psynergy slot, which 
is located from 3588 to 358B.

Offset | 00 01 02 03 04 05 06 07  08 09 0A 0B ...
003580 | 4C 00 5D 00 2B 00 37 00  C6 80 00 00 ...
              Psy value "Odyssey" ^^ ^^
                                     ^^ Psy type "Class bounded"

There are three types of psynergy in this game: 80 signifies psynergy bounded 
by the character's class; like Ply and Quake Sphere. 40 represents psynergy 
bounded to items; like Halt, Teleport, and Cloak. 00 marks psynergy not 
bounded by anything; like Mind Read, Sand, and Retreat. If you'd like to keep 
your psynergy intact through class changes, assign the ones you want to keep 
types of 00.

But there's more! If you add other numbers to the Psy type, you can access 
entire other sets of psynergy! In fact, modifying the second part of the type 
will sometimes actually cut into Golden Sun's script!

After changing the first psynergy value, repeat the process ad infinitum for 
the next groups of psynergy, and so on. You can store a maximum of 32 
psynergy without the game glitching up on you, which is indicated in the 
following addresses. 

Character Psynergy Slots:

Felix Psynergy    -> 3AB8 to 3B37
Jenna Psynergy    -> 3C04 to 3C83
Sheba Psynergy    -> 3D50 to 3DCF
Piers Psynergy    -> 3E9C to 3F1B
Isaac Psynergy    -> 3588 to 3607
Garet Psynergy    -> 36D4 to 3753
Ivan Psynergy     -> 3820 to 389F
Mia Psynergy      -> 396C to 39EB

Here are the values and type modifiers for all the psynergy. Note that 
glitched values have been skipped, and natural breaks in psynergy are 
indicated as a space. Stuff in parenthesis is personal notes. Also note that 
the game tends to like to sort the psynergy by type, so you may want to be 
wary of that.

Psynergy +00 modifier:

00 - [blank] (for "spaces" in psynergy)
01 - Attack
02 - Defend
03 - Quake
04 - Earthquake
05 - Quake Sphere
06 - Spire
07 - Clay Spire
08 - Stone Spire
09 - Gaia
0A - Mother Gaia
0B - Grand Gaia
0C - Growth
0D - Mad Growth
0E - Wild Growth
0F - Thorn
10 - Briar
11 - Nettle

18 - Frost
19 - Tundra
1A - Glacier
1B - Ice
1C - Ice Horn
1D - Ice Missile
1E - Prism
1F - Hail Prism
20 - Douse
21 - Freeze Prism
22 - Drench
23 - Deluge
24 - Froth
25 - Froth Sphere
26 - Froth Spiral
27 - Cool
28 - Supercool
29 - Megacool

2D - Flare
2E - Flare Wall
2F - Flare Storm
30 - Fire
31 - Fireball
32 - Inferno
33 - Volcano
34 - Eruption
35 - Pyroclasm
36 - Blast (attack psy)
37 - Mad Blast
38 - Fiery Blast
39 - Blast
3A - Nova
3B - Supernova
3C - Fume
3D - Serpent Fume
3E - Dragon Fume
3F - Beam
40 - Cycle Beam
41 - Searing Beam

42 - Bolt
43 - Flash Bolt
44 - Blue Bolt
45 - Ray
46 - Storm Ray
47 - Destruct Ray
48 - Plasma
49 - Shine Plasma
4A - Spark Plasma
4B - Slash
4C - Wind Slash
4D - Sonic Slash
4E - Whirlwind
4F - Tornado
50 - Tempest

57 - Aura
58 - Healing Aura
59 - Cool Aura
5A - Cure
5B - Cure Well
5C - Potent Cure
5D - Ply
5E - Ply Well
5F - Pure Ply
60 - Wish
61 - Wish Well
62 - Pure Wish
63 - Cure Poison
64 - Restore
65 - Revive

66 - Impact
67 - High Impact
68 - Dull
69 - Blunt
6A - Guard
6B - Protect
6C - Impair
6D - Debilitate
6E - Ward
6F - Resist
70 - Weaken
71 - Enfeeble

72 - Taint
73 - Poison
74 - Delude
75 - Confuse
76 - Charm
77 - Paralyze
78 - Sleep
79 - Bind
7A - Haunt
7B - Curse
7C - Condemn
7D - Drain
7E - Psy Drain
7F - Break
80 - Regenerate
81 - Reflect

82 - Lash
83 - Pound
84 - Tremor
85 - Scoop
86 - Cyclone
87 - Parch
88 - Sand
89 - Move

8D - Mind Read
9E - Force
9F - Lift
90 - Reveal
91 - Halt
92 - Cloak
93 - Carry
94 - Catch
95 - Retreat
96 - Avoid
97 - Burst
98 - Grind
99 - Hover
9A - Blaze
9B - Ma???? (likely Magnet)
9C - Teleport
9D - A?? (maybe Air)

A0 - Dragon Cloud
A1 - Demon Night
A2 - Helm Splitter
A3 - Quick Strike
A4 - Rockfall
A5 - Rockslide
A6 - Avalanche
A7 - Lava Shower
A8 - Molten Bath
A9 - Magma Storm
AA - Demon Spear
AB - Angel Spear
AC - Guardian
AD - Protector
AE - Magic Shell
AF - Magic Shield
B0 - Death Plunge
B1 - Shruiken
B2 - Annihilation
B3 - Punji
B4 - Punji Trap
B5 - Punji Strike
B6 - Fire Bomb
B7 - Cluster Bomb
B8 - Carpet Bomb
B9 - Gale
BA - Typhoon
BB - Hurricane
BC - Thunderclap
BD - Thunderbolt
BE - Thunderhead
BF - Mist

C0 - Ragnarok
C1 - Cutting Edge
C2 - Heat Wave
C3 - Astral Blast
C4 - Planet Diver
C5 - Diamond Dust
C6 - Odyssey
C7 - Liquifier
C8 - Plume Edge
C9 - Thunder Mine
CA - Planetary
CB - Diamond Berg
CC - Death Leap
CD - Epicenter
CE - Thorny Grave
CF - Skull Splitter

From here on, psynergy is replaced by weapon unleashes and minor items which 
have a casting cost of 0 PP.

D2 - Terra Strike
D3 - Poison Cloud
D4 - Poison Death
D5 - Mortal Danger
D6 - Bad Omen
D7 - Life Nourish
D8 - Aqua Sock
D9 - Blizzard
DA - Frost Bite
DB - Drown
DC - Life Leech
DD - Psy Leech
DE - Broil
DF - Meltdown
E0 - Heat Mirage 
E1 - Barrage
E2 - Demonfire
E3 - Acid Bath
E4 - Vorpal Slash
E5 - Stun Voltage
E6 - Blinding Smog
E7 - Murk
E8 - Cyclone Slash
E9 - Psyphon Seal
EA - Rapid Smash
EB - Sonic Smash
EC - Asura
ED - Titan Blade
EE - Shining Star

F6 - Herb
F7 - Nut
F8 - Vial
F9 - Potion
FA - Soothing Water
FB - Psy Crystal

Psynergy +01 modifier:

00 - Antidote
01 - Elixir
02 - Water of Life
03 - Mist Potion
04 - Power Bread
05 - Cookie
06 - Apple
07 - Hard Nut
08 - Mint
09 - Lucky Pepper

0B - Smoke Bomb
0C - Sleep Bomb
0D - Adept Ring
0E - Corn

Djinn effects start here:

2A - Aurora Field
2B - Djinn Counter
2C - Flint
2D - Granite
2E - Quartz
2F - Vine
30 - Sap
31 - Ground
32 - Bane
33 - Echo
34 - Iron
35 - Steel
36 - Mud
37 - Flower
38 - Meld
39 - Petra
3A - Salt
3B - Geode
3C - Mold
3D - Crystal
3E - Earth18 (dummy)
3F - Earth19 (dummy)
40 - Fizz
41 - Sleet
42 - Mist
43 - Spritz
44 - Hail
45 - Tonic
46 - Dew
47 - Fog
48 - Sour
49 - Spring
4A - Shade
4B - Chill
4C - Steam
4D - Rime
4E - Gel
4F - Eddy
50 - Balm
51 - Serac
52 - Water18 (dummy)
53 - Water19 (dummy)
54 - Forge
55 - Fever
56 - Corona
57 - Scorch
58 - Ember
59 - Flash
5A - Torch
5B - Cannon
5C - Spark
5D - Kindle
5E - Char
5F - Coal
60 - Reflux
61 - Core
62 - Tinder
63 - Shine
64 - Fury
65 - Fugue
66 - Fire18 (dummy)
67 - Fire19 (dummy)
68 - Gust
69 - Breeze
6A - Zephyr
6B - Smog
6C - Kite
6D - Squall
6E - Luff
6F - Breath
70 - Blitz
71 - Ether
72 - Waft
73 - Haze
74 - Wheeze
75 - Aroma
76 - Whorl
77 - Gasp
78 - Lull
79 - Gale
7A - Wind18
7B - Wind19

Summoned spirits begin here:

7C - Venus
7D - Ramses
7E - Cybele
7F - Judgment
80 - Zagan
81 - Haures
82 - Charon

84 - Mercury
85 - Nereid
86 - Neptune
87 - Boreas
88 - Moloch
89 - Coatlicue
8A - Azul

8C - Mars
8D - Kirin
8E - Tiamat
8F - Meteor
90 - Megaera
91 - Ulysses
92 - Daedalus (Master craftsman of ancient times)
93 - Daedalus (Second strike)
94 - Iris

96 - Jupiter
97 - Atalanta
98 - Procne
99 - Thor
9A - Flora
9B - Eclipse
9C - Catastrophe

Monster attacks begin now:

A4 - Fire Breath
A5 - Fire Breath
A6 - Fire Breath
A7 - Water Breath
A8 - Water Breath
A9 - Water Breath
AA - Ice Breath
AB - Ice Breath
AC - Ice Breath
AD - Dark Breath
AE - Dark Breath
AF - Acid Breath
B0 - Acid Breath
B1 - Storm Breath
B2 - Storm Breath
B3 - Sonic Wave
B4 - Sonic Wave
B5 - Shriek
B6 - Banshee Howl
B7 - Crazy Voice
B8 - War Cry
B9 - Wicked Howl
BA - Wing Beat
BB - Wing Flutter
BC - Wing Stroke
BD - Evil Blessing
BE - Deadly Gas

C2 - Rumble
C3 - Bone Chiller
C4 - Slice
C5 - Bone Charge
C6 - Mystic Flame
C7 - Numbing Sting
C8 - Brute Force
C9 - Sticky Goo
CA - Cannibal Fang
CB - Bear Claw
CC - Poisonous Bite
CD - Flying Attack
CE - Undead Sword
CF - Ransack
D0 - Sticky Poison
D1 - Poison Fang
D2 - Electric Bite
D3 - Poison Tail
D4 - Onslaught
D5 - Vampiric Fang
D6 - Bacteria Rush
D7 - Swift Strike
D8 - Rotten Blood
D9 - Forcible Arm
DA - Double Fang
DB - Mortal Blow
DC - Freebite Rush
DD - Twin Beaks
DE - Rabid Fang
DF - Acid Bite
E0 - Dynamite
E1 - Headbutt
E2 - Poison Ink
E3 - Truncheon Fist
E4 - Counterstrike
E5 - Mad Dash
E6 - Soothing Star
E7 - Spider Web
E8 - Heartrender
E9 - Mad Spatter
EA - Spasm
EB - Sleep Star
EC - Decompose
ED - Haunting
EE - Worms
EF - Berserk
F0 - Lucid Prophecy
F1 - Recovery
F2 - Flee
F3 - Contain
F4 - Threaten
F5 - Tremble
F6 - Fortify
F7 - Speed Surge
F8 - Ally Search
F9 - Sidestep
FA - Total Defense
FB - Stand Ready
FC - Battle Cry
FD - Can't Use (dummy)
FE - Poison Beat
FF - Spinning Beat

Psynergy +02 modifier:

00 - Heat Flash
01 - Death Scythe
02 - Outer Space
03 - Dragon Driver
04 - Drain Fang
05 - Severe Blow
06 - Thrash

Golden Sun 2 weapon unleashes start happening now:

08 - Stone Justice
09 - Sarcophagus
0A - Evil Eye
0B - Vein Tap
0C - Heavy Divide
0D - Hammersphere
0E - Mother Earth
0F - Wyrd Curse (removed from US version?)
10 - Heartbreak
11 - Vengeance
12 - Acheron's Grief
13 - Megiddo

17 - Hurricane
18 - Dreamtide
19 - Stun Cloud
1A - Searing Fog
1B - Ice Crush
1C - Flash Force
1D - Sargasso
1E - Lethe Albion
1F - Reverse Star
20 - Rising Dragon

25 - Power Drive
26 - Boost Hack
27 - Heat Smash
28 - Fire Dance
29 - Blaze Rush
2A - Flare Burst
2B - Shred
2C - Crucible Fire
2D - Scorpionfish
2E - Purgatory
2F - Soul Shatter
30 - Radiant Fire
31 - Life Shear

35 - Moon Air
36 - Flash Edge
37 - Aging Gas
38 - Mad Zephyr
39 - Lunar Slash
3A - Nirvana
3B - High Vitals
3C - Stun Bolt
3D - Trident (item use)
3E - Light Surge
3F - Raiden's Wrath
40 - Void Beam
41 - Supernova
42 - Apocalypse
43 - Legend

Item class psynergies start now:

48 - Sabre Dance
49 - Backstab
4A - Fire Breath
4B - Juggle
4C - Heat Juggle
4D - Fiery Juggle
4E - Flame Card
4F - Thunder Card
50 - Bramble Card
51 - Frost Card
52 - Baffle Card
53 - Sword Card
54 - Sleep Card
55 - Death Card

57 - Whiplash
58 - Wild Wolf
59 - Emu
5A - Roc
5B - Salamander
5C - Orc
5D - Harpy
5E - Grand Golem
5F - Cerebus
60 - Wyvern
61 - Pixie
62 - Dinox
63 - Gryphon
64 - Living Armor
65 - Chimera
66 - Blue Dragon
67 - Faery
68 - Elder Wood
69 - Lich
6A - Troll
6B - Minotaur
6C - Ghost Soldier
6D - Macetail
6E - Fire Dragon
6F - Weird Nymph
70 - Succubus
71 - Estre Wood
72 - Manticore
73 - Phoenix

75 - Call Zombie
76 - Call Demon
77 - Call Dullahan
78 - Raging Heat
79 - Fiery Abyss
7A - Dire Inferno
7B - Poison Flow
7C - Fire Puppet

GS2 Monster attacks start here:

80 - Sand Breath
81 - Desert Gasp
82 - Black Ice
83 - Toxic Breath
84 - Typhoon Blow
85 - Blast Breath
86 - Gravel Blow
87 - Darksol Gasp
88 - Flame Breath
89 - Aqua Breath
8A - Fire Breath
8B - Chill Breath

94 - Flash Punch
95 - Formic Acid
96 - Claw Attack
97 - Beat Dance
98 - Twin Shear
99 - Paralytail
9A - Echo Cut
9B - Clarion Cry
9C - Triple Chomp
9D - Raging Flood
9E - Rising Venom
9F - Slaver
A0 - Mighty Press
A1 - Star Mine
A2 - Heat Stun
A3 - Ocean Fist
A4 - Watery Grave
A5 - Counter-rush
A6 - Counter
A7 - Bosca Hit
A8 - Strong Hit
A9 - Rolling Flame
AA - Rising Dragon
AB - Meteor Blow
AC - Cage
AD - Stun Muscle
AE - Djinnfest
AF - Heat Kiss
B0 - Fatal Fang
B1 - Angle Spike
B2 - Quick Slash
B3 - Doublestep
B4 - Maneater
B5 - Claw Slash
B6 - Mega Slash
B7 - Vanish Claw
B8 - Crusher Grip
B9 - Ur Flash
BA - Power Bite
BB - Terrible Bite
BC - Poison Sting
BD - Kill Sting
BE - Beast Needle
BF - Poison Sting
C0 - Stun Sting
C1 - Mucous Gel
C2 - Poison Gel
C3 - Hydro Slash
C4 - Regen Dance
C5 - Fire Dance
C6 - Power Crush
C7 - Sack
C8 - Vital Moon
C9 - Human Hunt
CA - Demon Eye
CB - Stun Jip
CC - Pike Assault
CD - Formina Sage
CE - True Collide
CF - Armor Crush
D0 - Djinn Blast
D1 - Djinn Storm
D2 - Earth Force
D3 - Guard Aura
D4 - Cruel Ruin
D5 - Mystic Call
D6 - Mine Ball
D7 - Angry Mine
D8 - Djinn Stun
D9 - Crucible
DA - Element Swap
DB - Earnest Ply
DC - Psy Boost
DD - Pressure
DE - ? (dummy field psynergy with "NPC" description and cost of 32 PP)


 *************
== B6. Djinn ==
 *************

Djinn are little elemental creatures that you find in your travels. They can 
do things in battle, and determine your class. There are 72 Djinn total in 
the game, 28 of which can be brought over from the original Golden Sun. Djinn 
hacking happens to be wildly complicated, so I'm not gonna bother with it 
right now. Maybe later. Do take note, however, that it is possible to exceed 
the nine-Djinn-per-character default set in the game. Whoo.


 ***************
== B7. Summons ==
 ***************

Naturally, following the section on Djinn is the section about summoning. By 
putting your Djinn on Standby mode, you can summon spirits to do much damage 
during battle. The compulsory summons are automatically added to your list 
when you get enough Djinn to use them, but they only are one-element summons 
and you can only use at most four Djinn to summon them. But throughout 
Weyward, special Combo Summon Tablets can be found. They allow you to summon 
stronger spirits using multiple elements of Djinn.

There are two addresses storing your combination summons, 325E and 325F. Each 
summon is given a value of a power of two. When you receive that particular 
summon, that value is added to one of the addresses. This ensures that every 
possible combination of summons has a unique total value. To use the list, 
add the listed summon's value to the address indicated.

325E's values:

Zagan             -> +01
Megaera           -> +02
Flora             -> +04
Moloch            -> +08
Ulysses           -> +10
Haures            -> +20
Eclipse           -> +40
Coatlicue         -> +80

325F's values:

Daedalus          -> +01
Azul              -> +02
Catastrophe       -> +04
Charon            -> +08
Iris              -> +10 


 *************
== B8. Items ==
 *************

You can't have any RPG without having items to carry, right? Unfotunately, 
the method for storing the items you have is WEIRD. Unpredictable byte shifts, 
strange changes in values... it's proven to be too difficult for me to decode 
at the moment. Well, gotta start somewhere, right? Each character can carry 
up to 30 items, and for the quantitative items, you can have up to 30 each of 
those.


 *************
== B9. Party ==
 *************

Throughout your quest, you gain characters to add to your party, for a total 
of eight. The first four slots are in the front party when entering battles, 
while the last four and in the back party which may be switched to the front 
at the beginning of your turn. Setting the same value to more than one slot 
gives you two of that character, obviously. If the front row happens to have 
two of the same value, that character will appear only once but you will be 
able to move multiple times. Using values other then ones listed will result 
in your game freezing and emitting a high-pitched noise when the game tries 
to access character data. So don't use the other values.

Note that the exact amount of people in your party is stored somewhere else; 
I'm still trying to figure out exactly where.

Slot 1            -> 3468
Slot 2            -> 3469
Slot 3            -> 346A
Slot 4            -> 346B
Slot 5            -> 346C
Slot 6            -> 346D
Slot 7            -> 346E
Slot 8            -> 346F

Party values:

00 - Isaac
01 - Garet
02 - Ivan
03 - Mia
04 - Felix
05 - Jenna
06 - Sheba
07 - Piers


 *************************
== BA. Story Reset Codes ==
 *************************

Luckily for us, the good people at Camelot have decided to make the method in 
which all the plot elements of Golden Sun: The Lost Age are stored into 
memory exactly the same as how the summons are stored into memory! So, that 
means that every single item that changes the plot somehow is assigned either 
a value of 01, 02, 04, 08, 10, 20, 40, or 80; and the sum of those values 
allows the game to load your file with the same progress as before. Until 
now...

Story Reset Codes -> 3150 to 31A4

Basically, to completely wipe out your story-related progress in the game, 
just set all the values in that address range to 00, and to completely finish 
your save file, set all of them to FF. However, note that a 100% game does 
not have all values set to FF, as some things in the game have multiple 
states, and the "complete" state discludes all previous ones. So, once again, 
YOU MUST KEEP A BACKUP OF YOUR SAVE FILE else you may experience some 
glitchiness. At the very least, write down what your old values were, ok?

I won't be listing which values correspond to which pieces of game progress 
because there are roughly 750 of such values. I will, however, keep a general 
list of what things are and are not affected by these values.

Affected parameters:
 - Plot events
 - Town and world map layout
 - Djinn found
 - Dungeon layouts
 - If your ship has wings (or, alternatively, whether you even have a ship)
 - Hidden item existence
 - Enemy Mimic existence
 - Boss fights

Unaffected parameters:
 - World map music (might be dependent on your party size instead)
 - Opened/closed chest 
 - Party members, Djinn, items, etc.
 - Combo summon tablet existence

That's all I can think of for now.


 *************************
== BB. Chest Reset Codes ==
 *************************

It's pretty much the same schnitzel as the Story Reset Codes, except these 
addresses exclusively modify whether or not a chest has been plundered.

Chest Reset Codes -> 343E to 3446


 **********************
== BC. Save Locations ==
 **********************

Here you will find various addresses pertaining to the location in which you 
are in the story.

 ***************************
~ BCa. File Select Location ~
 ***************************

Holy useless information... this address just controls what location is 
displayed on the file select screen, nothing more. Realistic locations range 
value-wise from 00 to 55. Beyond that, you will find strange "debug" locales 
for a little while, which will then eventually phase into nonsensical words 
grabbed out of the ROM.

F. Select Locale  -> 3010


 *********************
== BD. Miscellaneous ==
 *********************

This section covers things which don't quite fit into the other categories.

 ***********************
~ BDa. File Select Name ~
 ***********************

There is a second set of addresses used for the name that gets displayed on 
the File Select Screen; which should be the character whose map sprite is 
displayed. The name should always be 'Felix' during the entire game except 
for the beginning, where it should be 'Jenna' or the equivalent of those two. 
Note that this name string is twelve letters long as opposed to the fifteen 
for character names.

File Select Name  -> 3010 to 301B


 ************
~ BDb. Coins ~
 ************

The currency in this game is simply Coins. You can carry a maximum of 999,999 
coins, but with the help of the hex editor, you can get up to 16,777,214. 
It's too bad hacking your coins above the limit doesn't do squat. Whenever 
your Coin amount is over the limit and you gain or lose coins, it resets to 
999,999. Sad, isn't it? At least you can brag to your friends about it. Coins 
are stored over three bytes in multiple addresses.

Coins A           -> 3024 to 3026
Coins B           -> 3260 to 3262


 ********************
~ BDc. Game Settings ~
 ********************

Game settings can be accessed via the pause screen. They change window 
settings, message and speech settings, and Auto-Sleep. I'm not going to list 
the possibilities for all the values; there are too many and you can just as 
easily change them via the actual game interface rather than hacking into it. 
Still, it's worth experimenting with the various values. Try using FF for 
Window Colour and Brightness for a unique experience. :D

Window Colour     -> 3475
Window Brightness -> 3476

Message Speed     -> 347C

Message Speed values are 00 for Slow, 01 for Normal, and 02 for Fast. Using 
anything above results in glitch speeds (usually EXTREMELY slow).

Speech            -> 347A
Auto-Sleep        -> 349A

Speech and Auto-Sleep values are 00 for Off and 01 for On, obviously. 
Anything above results in glitches, but it seems that even values make them 
Off, while odd ones make them On.


 ********************
~ BDd. Arena Battles ~
 ********************

These addresses store your record battles in the Battle Arena, accessible 
from the main menu.

Monster Battles   -> 3158 to 3159


=====================================================================


  ************************
~*== PART C. Conclusion ==*~
  ************************

 **************************
== C1. Credits and Thanks ==
 **************************

Thanks for the people at Golden Sun Anonymous for somewhat directly 
influencing me to create this guide. Sniff... too bad the main site has 
somewhat died over the past few months.

And you, for taking your time to read this guide.


 ***************************
== C2. Contact Information ==
 ***************************

If you ever have questions, comments, or corrections about my guide, please 
feel free to contact me.

You can reach me via email or AIM at DDragon962 (at) aol (dot) com. Just 
unscramble that into a real e-mail address. Don't try looking for me on the 
GameFAQs Boards, because I don't go there much. Sorry.

Anyways, you'd better put something like "Save Game Hack" or something to 
that extent in the subject so that I don't delete your mail because of spam.


 *************************
== C3. Legal Information ==
 *************************

This guide may not be reproduced under any circumstances except for personal, 
private use. It may not be placed on any web site or otherwise distributed 
publicly without advance written permission. Use of this guide on any other 
web site or as a part of any public display is strictly prohibited, and a 
violation of copyright.

All trademarks and copyrights contained in this document are owned by their 
respective trademark and copyright holders.

Copyright 2004-2005 Oliver Chen.

Sites allowed to use this guide:
GameFAQs            (http://www.gamefaqs.com)
Gaming Vortex       (http://www.gaming-vortex.com)

 *********************
== C4. Still to Come ==
 *********************

Dead. Yep, that's a rather close word to describe myself right now. I've 
decided to stop looking for the Djinn and Item addresses because you can just 
as easily use a Codebreaker to edit those values. So, I'm now focusing purely 
on stuff that you either can't do with a CB or is just really really hard to 
do with one.

Namely, location. The location values are SO secret, they seem to have their 
own checksum and stuff ^_^ Haha, walk around on Mt. Aleph and other places... 
Well, until next time (if there ever will be a next time)...
Restore Page

