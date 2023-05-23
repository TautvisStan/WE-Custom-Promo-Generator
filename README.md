# Wrestling Empire Custom Promo Generator
## Usage
### Automatic Installation
Note: It is recommended to move the created .promo files out of the mod directory otherwise mod manager will delete them when the mod gets updated.
After the mod manager installs the tool, click `Browse profile folder`, go to `\BepInEx\plugins\GeeEm-PromoGenerator\Assets` and launch `WECustomPromoGenerator.exe`. Follow the instructions on the screen. When you are done making pages click `Create .promo file` and the tool should make a new .promo file. It should appear in game the next time you launch it.
### Manual Installation
Download the zip and extract it. Go to `\plugins\Assets\` and launch `WECustomPromoGenerator.exe`. Follow the instructions on the screen. When you are done making pages click `Create .promo file` and the tool should make a new .promo file. Put that file in your `\BepInEx\plugins\Assets` folder and it should appear in game the next time you launch it.
### Instructions
General example: https://imgur.com/a/0aIh4XM
Advanced features example: 
- `Please enter the promo title:` - the title of the custom promo. The tool will also use this as the file name.
- `Please enter the promo description: (You can use '[P1]' and '[P2]' to name wrestlers)` - the promo description. [P1] and [P2] will be replaced with the names of the characters.
- `How many speakers are there? Min 0, max 3, not counting the ref or team partners:` - how many main wrestler speakers are there. 
- `Is the wrestler 1 team partner included in the promo?` - adds wrestler 1 team partner to the promo. There should be at least 1 main wrestler to work correctly. Team format must be set in the match rules.
- `Is the wrestler 2 team partner included in the promo?` - adds wrestler 2 team partner to the promo. There should be at least 2 main wrestlers to work correctly. Team format must be set in the match rules.
- `Is the ref included in the promo?` - adds ref to the promo.
- `Update id list` - will display the wrestler ids you can use. Make sure to always update and check the ids after you make changes to previous fields.
- `Create new page` - creates new promo page:
     - `Enter the first line of the speaker:` / `Enter the second line of the speaker:` - each promo page can have up to 2 lines. For quotes, use `\"`. In order to use wrestler names use `$name#` and replace `#` with the corresponding wrestler id, e.g. if you type `I am $name1` and assign Whack Ax as the first wrestler in the game, he will say `I am Whack Ax`. `$promotion#` can be used the same way, using `I'm from promotion $promotion1` will be replaced by `I'm from promotion Wrestling Revolution` (wrestler 1's promotion). `$$belt(#1)_(#2)`, `$$champ(#1)_(#2)` are a bit more advanced, `(#1)` is the number of a wrestler (promotion), `(#2)` is the number of a title. Example: if someone from Wrestling Revolution is set as the first wrestler `The $$belt1_2 champion is $$champ1_2` will be replaced by `The Inter champion is Acrite`. However, if the first wrestler is from All American Wrestling, it will be replaced by `The United States champion is Perfect Sean`. Note: tag team champion and their partner are 4th and 5th champions (`$$champ1_4` and `$$champ1_5` will call out first wrestler's promotion's tag team champions). `@him/his/etc.#` will be replaced with the pronoun of the character with the corresponding id, e.g. `@his1 friend` -> `his friend` or `her friend` depending on wrestler #1's gender. Supported pronouns are `He, he, His, his, Him, him, Male, male, Man, man, Guy, guy, Boy, boy`.
     - `Enter the speaker id:` / `Enter the receiver id:` - use the provided character ids.
     - `Enter the taunt name or number (0 for none):` - list of taunts can be found here: https://github.com/IngoHHacks/WECCL/blob/main/TauntAnims.md
     - `Is the speaker happy (H) or angry (A)? (enter 0 for none):` - enter `H` to make the character happy, `A` to make them angry, `0` for none.
	 - `Add new feature` - Adds a new advanced promo feature to the promo:
	 	 - `Enter the promo feature` - List and examples of available promo commands can be found here: https://github.com/IngoHHacks/WECCL/tree/main#custom-promos Note: It's enough to use alignment/relationship commands once per promo in any page.
	 	 - `Delete this feature` - you can delete the command if you don't need it.
	 - `Delete this page` - you can delete the page if you don't need it.
- `Create .promo file` - will generate the .promo file. Click this once you are done making the custom promo.
### Manual .promo Editing
.promo files can be opened and edited in notepad. For more information about how to edit them manually read the [WECCL documentation](https://thunderstore.io/c/wrestling-empire/p/IngoH/WECCL/).
## Tips
Tipping can be done here: https://ko-fi.com/gamingmasterlt
## Special Thanks
IngoH for creating WECCL and letting this come to life.