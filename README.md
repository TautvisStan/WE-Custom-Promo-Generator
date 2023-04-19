# Wrestling Empire Custom Promo Generator
## Usage
### Automatic installation
After the mod manager installs the tool, click `Browse profile folder`, go to `GeeEm-PromoGenerator-1.0.0/plugins/Assets/` and launch `WECustomPromoGenerator.exe`. Follow the instructions on the screen. When you are done making pages click `Create .promo file` and the tool should make a new .promo file. It *should* appear in game the next time you launch it.
### Manual installation
Download the zip and extract it. Go to `/plugins/Assets/` and launch `WECustomPromoGenerator.exe`. Follow the instructions on the screen. When you are done making pages click `Create .promo file` and the tool should make a new .promo file. Put that file in your `<Game directory>\BepInEx\plugins\Assets` folder and it should appear in game the next time you launch it.
### Instructions
- `Please enter the promo title:` - the title of the custom promo. The tool will also use this as the file name.
- `Please enter the promo description: (You can use '[P1]' and '[P2]' to name wrestlers)` - the promo description. [P1] and [P2] will be replaced with the names of the characters.
- `How many speakers are there? Min 0, max 3, not counting the ref or team partners:` - how many main wrestler speakers are there.
- `Is the wrestler 1 team partner included in the promo?` - adds wrestler 1 team partner to the promo. There should be at least 1 main wrestler to work correctly.
- `Is the wrestler 2 team partner included in the promo?` - adds wrestler 2 team partner to the promo. There should be at least 2 main wrestlers to work correctly.
- `Is the ref included in the promo?` - adds ref to the promo.
- `Next step` - will move to promo page generation.
- `Create new page` - creates new promo page:
     - `Enter the first line of the speaker:` / `Enter the second line of the speaker:` - each promo page can have up to 2 lines. For quotes, use `\"`. `$name#` will be replaced with the name of the character with the corresponding id. `@him/his/etc.#` will be replaced with the pronoun of the character with the corresponding id, e.g. `@his1 friend` -> `his friend` or `her friend` depending on wrestler #1's gender. Supported pronouns are `He, he, His, his, Male, male, Man, man, Guy, guy, Boy, boy`.
     - `Enter the speaker id:` / `Enter the receiver id:` - use the provided character ids.
     - `Enter the taunt number (0 for none):` - list of taunts can be found here: https://github.com/IngoHHacks/WECCL/blob/main/TauntAnims.md
     - `Is the speaker happy (H) or angry (A)? (enter 0 for none):` - enter `H` to make the character happy, `A` to make them angry, `0` for none.
- `Create .promo file` - will generate the .promo file. Click this once you are done making the custom promo.
### Manual .promo editing
.promo files can be opened and edited in notepad. For more information about how to edit them manually read the [WECCL documentation](https://thunderstore.io/c/wrestling-empire/p/IngoH/WECCL/).