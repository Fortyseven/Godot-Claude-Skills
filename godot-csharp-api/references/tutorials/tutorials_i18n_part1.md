# Godot 4 C# Tutorials — I18N (Part 1)

> 4 tutorials. C#-specific code examples.

## Internationalizing games

### Introduction

While indie or niche games usually do not need localization, games targeting a more massive market often require localization. Godot offers many tools to make this process more straightforward, so this tutorial is more like a collection of tips and tricks.

Localization is usually done by specific studios hired for the job. Despite the huge amount of software and file formats available for this, the most common way to do localization to this day is still with spreadsheets. The process of creating the spreadsheets and importing them is already covered in the [Importing translations](tutorials_assets_pipeline.md) tutorial. If you haven't read the Importing translations page before, we recommend you give it a read before reading this page.

> **Note:** We will be using the official demo as an example; you can [download it from the Asset Library](https://godotengine.org/asset-library/asset/2776).

### Configuring the imported translation

Translations can get updated and re-imported when they change, but they still have to be added to the project. This is done in Project > Project Settings > Localization > Translations:

The above dialog is used to add or remove translations project-wide.

### Localizing resources

It is also possible to instruct Godot to use alternate versions of assets (resources) depending on the current language. This can be used for localized images such as in-game billboards or localized voices.

The Remaps tab can be used for this:

Select the resource to be remapped then add some alternatives for each locale.

> **Note:** The resource remapping system isn't supported for DynamicFonts. To use different fonts depending on the language's script, use the DynamicFont fallback system instead, which lets you define as many fallback fonts as you want. The upside of the DynamicFont fallback system is that it works regardless of the current language, making it ideal for things like multiplayer chat where the text language may not match the client's language.

### Automatically setting a language

It is recommended to default to the user's preferred language which can be obtained via [OS.get_locale_language()](../godot_csharp_misc.md). If your game is not available in that language, it will fall back to the [Fallback](../godot_csharp_misc.md) in Project > Project Settings > General > Internationalization > Locale, or to `en` if empty. Nevertheless, letting players change the language in game is recommended for various reasons (e.g. translation quality or player preference).

### Locale vs. language

A locale is commonly a combination of a language with a region or country, but can also contain information like a script or a variant.

Examples:

- `en`: English language
- `en_GB`: English in Great Britain / British English
- `en_US`: English in the USA / American English
- `en_DE`: English in Germany

Indie games generally only need to care about language, but read on for more information.

Why locales exist can be illustrated through the USA and Great Britain. Both speak the same language (English), yet differ in many aspects:

- Spelling: e.g. gray (USA), grey (GB)
- Use of words: e.g. eggplant (USA), aubergine (GB)
- Units or currencies: e.g. feet/inches (USA), metres/cm (GB)

It can get more complex however. Imagine you offer different content in Europe and in China (e.g. in an MMO). You will need to translate each of those content variations into many languages and store and load them accordingly.

### Converting keys to text

Some controls, such as [Button](../godot_csharp_ui_controls.md) and [Label](../godot_csharp_ui_controls.md), will automatically fetch a translation if their text matches a translation key. For example, if a label's text is `MAIN_SCREEN_GREETING1` and that key exists in the current translation, then the text will automatically be translated.

This automatic translation behavior may be undesirable in certain cases. For instance, when using a Label to display a player's name, you most likely don't want the player's name to be translated if it matches a translation key. To disable automatic translation on a specific node, set the Auto Translate > Mode to `Disabled` in the inspector.

In code, the [Object.tr()](../godot_csharp_core.md) function can be used. This will just look up the text in the translations and convert it if found:

```csharp
level.Text = Tr("LEVEL_5_NAME");
status.Text = Tr($"GAME_STATUS_{statusIndex}");
```

> **Note:** If no text is displayed after changing the language, try to use a different font. The default project font only supports a subset of the Latin-1 character set, which cannot be used to display languages like Russian or Chinese. A good resource for multilingual fonts is [Noto Fonts](https://www.google.com/get/noto/). Make sure to download the correct variation if you're using a less common language. Once you've downloaded the font, load the TTF file into a DynamicFont resource and use it as a custom font of your Control node. For better reusability, associate a new a Theme resource to your root Control node and define the DynamicFont as the Default Font in the theme.

#### Placeholders

To feature placeholders in your translated strings, use [GDScript format strings](tutorials_scripting.md) or the equivalent feature in C#. This lets translators move the location of the placeholder in the string freely, which allows translations to sound more natural. Named placeholders with the `String.format()` function should be used whenever possible, as they also allow translators to choose the _order_ in which placeholders appear:

#### Translation contexts

If you're using plain English as source strings (rather than message codes `LIKE_THIS`), you may run into ambiguities when you have to translate the same English string to different strings in certain target languages. You can optionally specify a _translation context_ to resolve this ambiguity and allow target languages to use different strings, even though the source string is identical:

```csharp
// "Close", as in an action (to close something).
GetNode<Button>("Button").Text = Tr("Close", "Actions");

// "Close", as in a distance (opposite of "far").
GetNode<Label>("Distance").Text = Tr("Close", "Distance");
```

#### Pluralization

Most languages require different strings depending on whether an object is in singular or plural form. However, hardcoding the "is plural" condition depending on whether there is more than 1 object is not valid in all languages.

Some languages have more than two plural forms, and the rules on the number of objects required for each plural form vary. Godot offers support for _pluralization_ so that the target locales can handle this automatically.

Pluralization is meant to be used with positive (or zero) integer numbers only. Negative and floating-point values usually represent physical entities for which singular and plural don't clearly apply.

```csharp
int numApples = 5;
GetNode<Label>("Label").Text = string.Format(TrN("There is {0} apple", "There are {0} apples", numApples), numApples);
```

This can be combined with a context if needed:

```csharp
int numJobs = 1;
GetNode<Label>("Label").Text = string.Format(TrN("{0} job", "{0} jobs", numJobs, "Task Manager"), numJobs);
```

### Making controls resizable

The same text in different languages can vary greatly in length. For this, make sure to read the tutorial on [Size and anchors](tutorials_ui.md), as dynamically adjusting control sizes may help. [Container](../godot_csharp_ui_controls.md) can be useful, as well as the text wrapping options available in [Label](../godot_csharp_ui_controls.md).

To check whether your UI can accommodate translations with longer strings than the original, you can enable pseudolocalization in the advanced Project Settings. This will replace all your localizable strings with longer versions of themselves, while also replacing some characters in the original strings with accented versions (while still being readable). Placeholders are kept as-is, so that they keep working when pseudolocalization is enabled.

For example, the string `Hello world, this is %s!` becomes `[Ĥéłłô ŵôŕłd́, ŧh̀íš íš %s!]` when pseudolocalization is enabled.

While looking strange at first, pseudolocalization has several benefits:

- It lets you spot non-localizable strings quickly, so you can go over them and make them localizable (if it makes sense to do so).
- It lets you check UI elements that can't fit long strings. Many languages will feature much longer translations than the source text, so it's important to ensure your UI can accommodate longer-than-usual strings.
- It lets you check whether your font contains all the characters required to support various languages. However, since the goal of pseudolocalization is to keep the original strings readable, it's not an effective test for checking whether a font can support CJK or right-to-left languages.

The project settings allow you to tune pseudolocalization behavior, so that you can disable parts of it if desired.

### TranslationServer

Godot has a server handling low-level translation management called the [TranslationServer](../godot_csharp_misc.md). Translations can be added or removed during runtime; the current language can also be changed at runtime.

### Bidirectional text and UI mirroring

Arabic and Hebrew are written from right to left (except for the numbers and Latin words mixed in), and the user interface for these languages should be mirrored as well. In some languages the shape of a glyph changes depending on the surrounding characters.

Support for bidirectional writing systems and UI mirroring is transparent, you don't usually need to change anything or have any knowledge of the specific writing system.

For RTL languages, Godot will automatically do the following changes to the UI:

- Mirrors left/right anchors and margins.
- Swaps left and right text alignment.
- Mirrors horizontal order of the child controls in the containers, and items in Tree/ItemList controls.
- Uses mirrored order of the internal control elements (e.g., OptionButton dropdown button, CheckBox/CheckButton alignment, List column order, TreeItem icons and connecting line alignment). In some cases, mirrored controls use separate theme styles.
- Coordinate system is **not** mirrored.
- Non-UI nodes (sprites, etc.) are **not** affected.

It is possible to override text and control layout direction by using the following control properties:

- `text_direction`, sets the base text direction. When set to "auto", the direction depends on the first strong directional character in the text according to the Unicode Bidirectional Algorithm.
- `language`, overrides the current project locale.
- The `structured_text_bidi_override` property and `_structured_text_parser` callback, enable special handling for structured text.
- `layout_direction`, overrides control mirroring.

> **See also:** You can see how right-to-left typesetting works in action using the [BiDI and Font Features demo project](https://github.com/godotengine/godot-demo-projects/tree/master/gui/bidi_and_font_features).

### Adding break iterator data to exported project

Some languages are written without spaces. In those languages, word and line breaking require more than rules over character sequences. Godot includes ICU rule and dictionary-based break iterator data, but this data is not included in exported projects by default.

To include it, go to Project > Project Settings > General > Internationalization > Locale and enable Include Text Server Data, then export the project. Break iterator data is about 4 MB in size.

### Structured text BiDi override

Unicode BiDi algorithm is designed to work with natural text and it's incapable of handling text with the higher level order, like file names, URIs, email addresses, regular expressions or source code.

For example, the path for this shown directory structure will be displayed incorrectly (top "LineEdit" control). "File" type structured text override splits text into segments, then BiDi algorithm is applied to each of them individually to correctly display directory names in any language and preserve correct order of the folders (bottom "LineEdit" control).

Custom callbacks provide a way to override BiDi for the other types of structured text.

### Localizing numbers

Controls specifically designed for number input or output (e.g. ProgressBar, SpinBox) will use localized numbering system automatically, for the other control [TextServer.format_number(string, language)](../godot_csharp_misc.md) can be used to convert Western Arabic numbers (0..9) to the localized numbering system and [TextServer.parse_number(string, language)](../godot_csharp_misc.md) to convert it back.

### Localizing icons and images

Icons with left and right pointing arrows which may need to be reversed for Arabic and Hebrew locales, in case they indicate movement or direction (e.g. back/forward buttons). Otherwise, they can remain the same.

### Testing translations

You may want to test a project's translation before releasing it. Godot provides three ways to do this.

Under Project > Project Settings > General > Internationalization > Locale (with advanced settings enabled) is a Test property. Set this property to the locale code of the language you want to test. Godot will run the project with that locale when the project is run (either from the editor or when exported).

Keep in mind that since this is a project setting, it will show up in version control when it is set to a non-empty value. Therefore, it should be set back to an empty value before committing changes to version control.

Second, from within the editor go to the top bar and click on View on the top bar, then go down to Preview Translation and select the language you want to preview.

All text in scenes in the editor should now be displayed using the selected language.

Translations can also be tested when [running Godot from the command line](tutorials_editor.md). For example, to test a game in French, the following argument can be supplied:

```shell
godot --language fr
```

### Translating the project name

The project name becomes the app name when exporting to different operating systems and platforms. To specify the project name in more than one language go to Project > Project Settings > General > Application > Config. From here click on the Localizable String (Size 0) button, then the Add Translation button. It will take you to a page where you can choose the language (and country if needed) for your project name translation. After doing that you can now type in the localized name.

If you are unsure about the language code to use, refer to the list of locale codes.

---

## Locale codes

Locale code has the following format: `language_Script_COUNTRY_VARIANT`, where:

- `language` - 2 or 3-letter language code, in lower case.
- `Script` - optional, 4-letter script code, in title case.
- `COUNTRY` - optional, 2-letter country code, in upper case.
- `VARIANT` - optional, language variant, region and, sort order. A variant can have any number of underscored keywords.

### List of supported language codes

| Language code | Name                        |
| ------------- | --------------------------- |
| aa            | Afar                        |
| ab            | Abkhazian                   |
| ace           | Achinese                    |
| ach           | Acoli                       |
| ada           | Adangme                     |
| ady           | Adyghe                      |
| ae            | Avestan                     |
| aeb           | Tunisian Arabic             |
| af            | Afrikaans                   |
| afh           | Afrihili                    |
| agq           | Aghem                       |
| ain           | Ainu                        |
| agr           | Aguaruna                    |
| ak            | Akan                        |
| akk           | Akkadian                    |
| akz           | Alabama                     |
| ale           | Aleut                       |
| aln           | Gheg Albanian               |
| alt           | Southern Altai              |
| am            | Amharic                     |
| an            | Aragonese                   |
| ang           | Old English                 |
| anp           | Angika                      |
| ar            | Arabic                      |
| arc           | Aramaic                     |
| arn           | Mapudungun                  |
| aro           | Araona                      |
| arp           | Arapaho                     |
| arq           | Algerian Arabic             |
| ars           | Najdi Arabic                |
| arw           | Arawak                      |
| ary           | Moroccan Arabic             |
| arz           | Egyptian Arabic             |
| as            | Assamese                    |
| asa           | Asu                         |
| ase           | American Sign Language      |
| ast           | Asturian                    |
| av            | Avaric                      |
| avk           | Kotava                      |
| awa           | Awadhi                      |
| ayc           | Southern Aymara             |
| ay            | Aymara                      |
| az            | Azerbaijani                 |
| ba            | Bashkir                     |
| bal           | Baluchi                     |
| ban           | Balinese                    |
| bar           | Bavarian                    |
| bas           | Bassa                       |
| bax           | Bamun                       |
| bbc           | Batak Toba                  |
| bbj           | Ghomala                     |
| be            | Belarusian                  |
| bej           | Beja                        |
| bem           | Bemba                       |
| ber           | Berber                      |
| bew           | Betawi                      |
| bez           | Bena                        |
| bfd           | Bafut                       |
| bfq           | Badaga                      |
| bg            | Bulgarian                   |
| bhb           | Bhili                       |
| bgn           | Western Balochi             |
| bho           | Bhojpuri                    |
| bi            | Bislama                     |
| bik           | Bikol                       |
| bin           | Bini                        |
| bjn           | Banjar                      |
| bkm           | Kom                         |
| bla           | Siksika                     |
| bm            | Bambara                     |
| bn            | Bengali                     |
| bo            | Tibetan                     |
| bpy           | Bishnupriya                 |
| bqi           | Bakhtiari                   |
| br            | Breton                      |
| brh           | Brahui                      |
| brx           | Bodo                        |
| bs            | Bosnian                     |
| bss           | Akoose                      |
| bua           | Buriat                      |
| bug           | Buginese                    |
| bum           | Bulu                        |
| byn           | Bilin                       |
| byv           | Medumba                     |
| ca            | Catalan                     |
| cad           | Caddo                       |
| car           | Carib                       |
| cay           | Cayuga                      |
| cch           | Atsam                       |
| ccp           | Chakma                      |
| ce            | Chechen                     |
| ceb           | Cebuano                     |
| cgg           | Chiga                       |
| ch            | Chamorro                    |
| chb           | Chibcha                     |
| chg           | Chagatai                    |
| chk           | Chuukese                    |
| chm           | Mari                        |
| chn           | Chinook Jargon              |
| cho           | Choctaw                     |
| chp           | Chipewyan                   |
| chr           | Cherokee                    |
| chy           | Cheyenne                    |
| cic           | Chickasaw                   |
| ckb           | Central Kurdish             |
| csb           | Kashubian                   |
| cmn           | Mandarin Chinese            |
| co            | Corsican                    |
| cop           | Coptic                      |
| cps           | Capiznon                    |
| cr            | Cree                        |
| crh           | Crimean Tatar               |
| crs           | Seselwa Creole French       |
| cs            | Czech                       |
| cu            | Church Slavic               |
| cv            | Chuvash                     |
| cy            | Welsh                       |
| da            | Danish                      |
| dak           | Dakota                      |
| dar           | Dargwa                      |
| dav           | Taita                       |
| de            | German                      |
| del           | Delaware                    |
| den           | Slave                       |
| dgr           | Dogrib                      |
| din           | Dinka                       |
| dje           | Zarma                       |
| doi           | Dogri                       |
| dsb           | Lower Sorbian               |
| dtp           | Central Dusun               |
| dua           | Duala                       |
| dum           | Middle Dutch                |
| dv            | Dhivehi                     |
| dyo           | Jola-Fonyi                  |
| dyu           | Dyula                       |
| dz            | Dzongkha                    |
| dzg           | Dazaga                      |
| ebu           | Embu                        |
| ee            | Ewe                         |
| efi           | Efik                        |
| egl           | Emilian                     |
| egy           | Ancient Egyptian            |
| eka           | Ekajuk                      |
| el            | Greek                       |
| elx           | Elamite                     |
| en            | English                     |
| enm           | Middle English              |
| eo            | Esperanto                   |
| es            | Spanish                     |
| esu           | Central Yupik               |
| et            | Estonian                    |
| eu            | Basque                      |
| ewo           | Ewondo                      |
| ext           | Extremaduran                |
| fa            | Persian                     |
| fan           | Fang                        |
| fat           | Fanti                       |
| ff            | Fulah                       |
| fi            | Finnish                     |
| fil           | Filipino                    |
| fit           | Tornedalen Finnish          |
| fj            | Fijian                      |
| fo            | Faroese                     |
| fon           | Fon                         |
| fr            | French                      |
| frc           | Cajun French                |
| frm           | Middle French               |
| fro           | Old French                  |
| frp           | Arpitan                     |
| frr           | Northern Frisian            |
| frs           | Eastern Frisian             |
| fur           | Friulian                    |
| fy            | Western Frisian             |
| ga            | Irish                       |
| gaa           | Ga                          |
| gag           | Gagauz                      |
| gan           | Gan Chinese                 |
| gay           | Gayo                        |
| gba           | Gbaya                       |
| gbz           | Zoroastrian Dari            |
| gd            | Scottish Gaelic             |
| gez           | Geez                        |
| gil           | Gilbertese                  |
| gl            | Galician                    |
| glk           | Gilaki                      |
| gmh           | Middle High German          |
| gn            | Guarani                     |
| goh           | Old High German             |
| gom           | Goan Konkani                |
| gon           | Gondi                       |
| gor           | Gorontalo                   |
| got           | Gothic                      |
| grb           | Grebo                       |
| grc           | Ancient Greek               |
| gsw           | Swiss German                |
| gu            | Gujarati                    |
| guc           | Wayuu                       |
| gur           | Frafra                      |
| guz           | Gusii                       |
| gv            | Manx                        |
| gwi           | Gwichʼin                    |
| ha            | Hausa                       |
| hai           | Haida                       |
| hak           | Hakka Chinese               |
| haw           | Hawaiian                    |
| he, iw        | Hebrew                      |
| hi            | Hindi                       |
| hif           | Fiji Hindi                  |
| hil           | Hiligaynon                  |
| hit           | Hittite                     |
| hmn           | Hmong                       |
| ho            | Hiri Motu                   |
| hne           | Chhattisgarhi               |
| hr            | Croatian                    |
| hsb           | Upper Sorbian               |
| hsn           | Xiang Chinese               |
| ht            | Haitian                     |
| hu            | Hungarian                   |
| hup           | Hupa                        |
| hus           | Huastec                     |
| hy            | Armenian                    |
| hz            | Herero                      |
| ia            | Interlingua                 |
| iba           | Iban                        |
| ibb           | Ibibio                      |
| id, in        | Indonesian                  |
| ie            | Interlingue                 |
| ig            | Igbo                        |
| ii            | Sichuan Yi                  |
| ik            | Inupiaq                     |
| ilo           | Iloko                       |
| inh           | Ingush                      |
| io            | Ido                         |
| is            | Icelandic                   |
| it            | Italian                     |
| iu            | Inuktitut                   |
| izh           | Ingrian                     |
| ja            | Japanese                    |
| jam           | Jamaican Creole English     |
| jbo           | Lojban                      |
| jgo           | Ngomba                      |
| jmc           | Machame                     |
| jpr           | Judeo-Persian               |
| jrb           | Judeo-Arabic                |
| jut           | Jutish                      |
| jv            | Javanese                    |
| ka            | Georgian                    |
| kaa           | Kara-Kalpak                 |
| kab           | Kabyle                      |
| kac           | Kachin                      |
| kaj           | Jju                         |
| kam           | Kamba                       |
| kaw           | Kawi                        |
| kbd           | Kabardian                   |
| kbl           | Kanembu                     |
| kcg           | Tyap                        |
| kde           | Makonde                     |
| kea           | Kabuverdianu                |
| ken           | Kenyang                     |
| kfo           | Koro                        |
| kg            | Kongo                       |
| kgp           | Kaingang                    |
| kha           | Khasi                       |
| kho           | Khotanese                   |
| khq           | Koyra Chiini                |
| khw           | Khowar                      |
| ki            | Kikuyu                      |
| kiu           | Kirmanjki                   |
| kj            | Kuanyama                    |
| kk            | Kazakh                      |
| kkj           | Kako                        |
| kl            | Kalaallisut                 |
| kln           | Kalenjin                    |
| km            | Central Khmer               |
| kmb           | Kimbundu                    |
| kn            | Kannada                     |
| ko            | Korean                      |
| koi           | Komi-Permyak                |
| kok           | Konkani                     |
| kos           | Kosraean                    |
| kpe           | Kpelle                      |
| kr            | Kanuri                      |
| krc           | Karachay-Balkar             |
| kri           | Krio                        |
| krj           | Kinaray-a                   |
| krl           | Karelian                    |
| kru           | Kurukh                      |
| ks            | Kashmiri                    |
| ksb           | Shambala                    |
| ksf           | Bafia                       |
| ksh           | Colognian                   |
| ku            | Kurdish                     |
| kum           | Kumyk                       |
| kut           | Kutenai                     |
| kv            | Komi                        |
| kw            | Cornish                     |
| ky            | Kirghiz                     |
| lag           | Langi                       |
| la            | Latin                       |
| lad           | Ladino                      |
| lah           | Lahnda                      |
| lam           | Lamba                       |
| lb            | Luxembourgish               |
| lez           | Lezghian                    |
| lfn           | Lingua Franca Nova          |
| lg            | Ganda                       |
| li            | Limburgan                   |
| lij           | Ligurian                    |
| liv           | Livonian                    |
| lkt           | Lakota                      |
| lmo           | Lombard                     |
| ln            | Lingala                     |
| lo            | Lao                         |
| lol           | Mongo                       |
| lou           | Louisiana Creole            |
| loz           | Lozi                        |
| lrc           | Northern Luri               |
| lt            | Lithuanian                  |
| ltg           | Latgalian                   |
| lu            | Luba-Katanga                |
| lua           | Luba-Lulua                  |
| lui           | Luiseno                     |
| lun           | Lunda                       |
| luo           | Luo                         |
| lus           | Mizo                        |
| luy           | Luyia                       |
| lv            | Latvian                     |
| lzh           | Literary Chinese            |
| lzz           | Laz                         |
| mad           | Madurese                    |
| maf           | Mafa                        |
| mag           | Magahi                      |
| mai           | Maithili                    |
| mak           | Makasar                     |
| man           | Mandingo                    |
| mas           | Masai                       |
| mde           | Maba                        |
| mdf           | Moksha                      |
| mdr           | Mandar                      |
| men           | Mende                       |
| mer           | Meru                        |
| mfe           | Morisyen                    |
| mg            | Malagasy                    |
| mga           | Middle Irish                |
| mgh           | Makhuwa-Meetto              |
| mgo           | Metaʼ                       |
| mh            | Marshallese                 |
| mhr           | Eastern Mari                |
| mi            | Māori                       |
| mic           | Mi'kmaq                     |
| min           | Minangkabau                 |
| miq           | Mískito                     |
| mjw           | Karbi                       |
| mk            | Macedonian                  |
| ml            | Malayalam                   |
| mn            | Mongolian                   |
| mnc           | Manchu                      |
| mni           | Manipuri                    |
| mnw           | Mon                         |
| mos           | Mossi                       |
| moh           | Mohawk                      |
| mr            | Marathi                     |
| mrj           | Western Mari                |
| ms            | Malay                       |
| mt            | Maltese                     |
| mua           | Mundang                     |
| mus           | Muscogee                    |
| mwl           | Mirandese                   |
| mwr           | Marwari                     |
| mwv           | Mentawai                    |
| my            | Burmese                     |
| mye           | Myene                       |
| myv           | Erzya                       |
| mzn           | Mazanderani                 |
| na            | Nauru                       |
| nah           | Nahuatl                     |
| nan           | Min Nan Chinese             |
| nap           | Neapolitan                  |
| naq           | Nama                        |
| nb, no        | Norwegian Bokmål            |
| nd            | North Ndebele               |
| nds           | Low German                  |
| ne            | Nepali                      |
| new           | Newari                      |
| nhn           | Central Nahuatl             |
| ng            | Ndonga                      |
| nia           | Nias                        |
| niu           | Niuean                      |
| njo           | Ao Naga                     |
| nl            | Dutch                       |
| nmg           | Kwasio                      |
| nn            | Norwegian Nynorsk           |
| nnh           | Ngiemboon                   |
| nog           | Nogai                       |
| non           | Old Norse                   |
| nov           | Novial                      |
| nqo           | N'ko                        |
| nr            | South Ndebele               |
| nso           | Pedi                        |
| nus           | Nuer                        |
| nv            | Navajo                      |
| nwc           | Classical Newari            |
| ny            | Nyanja                      |
| nym           | Nyamwezi                    |
| nyn           | Nyankole                    |
| nyo           | Nyoro                       |
| nzi           | Nzima                       |
| oc            | Occitan                     |
| oj            | Ojibwa                      |
| om            | Oromo                       |
| or            | Odia                        |
| os            | Ossetic                     |
| osa           | Osage                       |
| ota           | Ottoman Turkish             |
| pa            | Panjabi                     |
| pag           | Pangasinan                  |
| pal           | Pahlavi                     |
| pam           | Pampanga                    |
| pap           | Papiamento                  |
| pau           | Palauan                     |
| pcd           | Picard                      |
| pcm           | Nigerian Pidgin             |
| pdc           | Pennsylvania German         |
| pdt           | Plautdietsch                |
| peo           | Old Persian                 |
| pfl           | Palatine German             |
| phn           | Phoenician                  |
| pi            | Pali                        |
| pl            | Polish                      |
| pms           | Piedmontese                 |
| pnt           | Pontic                      |
| pon           | Pohnpeian                   |
| pr            | Pirate                      |
| prg           | Prussian                    |
| pro           | Old Provençal               |
| prs           | Dari                        |
| ps            | Pushto                      |
| pt            | Portuguese                  |
| qu            | Quechua                     |
| quc           | K'iche                      |
| qug           | Chimborazo Highland Quichua |
| quy           | Ayacucho Quechua            |
| quz           | Cusco Quechua               |
| raj           | Rajasthani                  |
| rap           | Rapanui                     |
| rar           | Rarotongan                  |
| rgn           | Romagnol                    |
| rif           | Riffian                     |
| rm            | Romansh                     |
| rn            | Rundi                       |
| ro            | Romanian                    |
| rof           | Rombo                       |
| rom           | Romany                      |
| rtm           | Rotuman                     |
| ru            | Russian                     |
| rue           | Rusyn                       |
| rug           | Roviana                     |
| rup           | Aromanian                   |
| rw            | Kinyarwanda                 |
| rwk           | Rwa                         |
| sa            | Sanskrit                    |
| sad           | Sandawe                     |
| sah           | Sakha                       |
| sam           | Samaritan Aramaic           |
| saq           | Samburu                     |
| sas           | Sasak                       |
| sat           | Santali                     |
| saz           | Saurashtra                  |
| sba           | Ngambay                     |
| sbp           | Sangu                       |
| sc            | Sardinian                   |
| scn           | Sicilian                    |
| sco           | Scots                       |
| sd            | Sindhi                      |
| sdc           | Sassarese Sardinian         |
| sdh           | Southern Kurdish            |
| se            | Northern Sami               |
| see           | Seneca                      |
| seh           | Sena                        |
| sei           | Seri                        |
| sel           | Selkup                      |
| ses           | Koyraboro Senni             |
| sg            | Sango                       |
| sga           | Old Irish                   |
| sgs           | Samogitian                  |
| sh            | Serbo-Croatian              |
| shi           | Tachelhit                   |
| shn           | Shan                        |
| shs           | Shuswap                     |
| shu           | Chadian Arabic              |
| si            | Sinhala                     |
| sid           | Sidamo                      |
| sk            | Slovak                      |
| sl            | Slovenian                   |
| sli           | Lower Silesian              |
| sly           | Selayar                     |
| sm            | Samoan                      |
| sma           | Southern Sami               |
| smj           | Lule Sami                   |
| smn           | Inari Sami                  |
| sms           | Skolt Sami                  |
| sn            | Shona                       |
| snk           | Soninke                     |
| so            | Somali                      |
| sog           | Sogdien                     |
| son           | Songhai                     |
| sq            | Albanian                    |
| sr            | Serbian                     |
| srn           | Sranan Tongo                |
| srr           | Serer                       |
| ss            | Swati                       |
| ssy           | Saho                        |
| st            | Southern Sotho              |
| stq           | Saterland Frisian           |
| su            | Sundanese                   |
| suk           | Sukuma                      |
| sus           | Susu                        |
| sux           | Sumerian                    |
| sv            | Swedish                     |
| sw            | Swahili                     |
| swb           | Comorian                    |
| swc           | Congo Swahili               |
| syc           | Classical Syriac            |
| syr           | Syriac                      |
| szl           | Silesian                    |
| ta            | Tamil                       |
| tcy           | Tulu                        |
| te            | Telugu                      |
| tem           | Timne                       |
| teo           | Teso                        |
| ter           | Tereno                      |
| tet           | Tetum                       |
| tg            | Tajik                       |
| th            | Thai                        |
| the           | Chitwania Tharu             |
| ti            | Tigrinya                    |
| tig           | Tigre                       |
| tiv           | Tiv                         |
| tk            | Turkmen                     |
| tkl           | Tokelau                     |
| tkr           | Tsakhur                     |
| tl            | Tagalog                     |
| tlh           | Klingon                     |
| tli           | Tlingit                     |
| tly           | Talysh                      |
| tmh           | Tamashek                    |
| tn            | Tswana                      |
| to            | Tongan                      |
| tog           | Nyasa Tonga                 |
| tpi           | Tok Pisin                   |
| tr            | Turkish                     |
| tru           | Turoyo                      |
| trv           | Taroko                      |
| ts            | Tsonga                      |
| tsd           | Tsakonian                   |
| tsi           | Tsimshian                   |
| tt            | Tatar                       |
| ttt           | Muslim Tat                  |
| tum           | Tumbuka                     |
| tvl           | Tuvalu                      |
| tw            | Twi                         |
| twq           | Tasawaq                     |
| ty            | Tahitian                    |
| tyv           | Tuvinian                    |
| tzm           | Central Atlas Tamazight     |
| udm           | Udmurt                      |
| ug            | Uyghur                      |
| uga           | Ugaritic                    |
| uk            | Ukrainian                   |
| umb           | Umbundu                     |
| unm           | Unami                       |
| ur            | Urdu                        |
| uz            | Uzbek                       |
| vai           | Vai                         |
| ve            | Venda                       |
| vec           | Venetian                    |
| vep           | Veps                        |
| vi            | Vietnamese                  |
| vls           | West Flemish                |
| vmf           | Main-Franconian             |
| vo            | Volapük                     |
| vot           | Votic                       |
| vro           | Võro                        |
| vun           | Vunjo                       |
| wa            | Walloon                     |
| wae           | Walser                      |
| wal           | Wolaytta                    |
| war           | Waray                       |
| was           | Washo                       |
| wbp           | Warlpiri                    |
| wo            | Wolof                       |
| wuu           | Wu Chinese                  |
| xal           | Kalmyk                      |
| xh            | Xhosa                       |
| xmf           | Mingrelian                  |
| xog           | Soga                        |
| yao           | Yao                         |
| yap           | Yapese                      |
| yav           | Yangben                     |
| ybb           | Yemba                       |
| yi            | Yiddish                     |
| yo            | Yoruba                      |
| yrl           | Nheengatu                   |
| yue           | Yue Chinese                 |
| yuw           | Papua New Guinea            |
| za            | Zhuang                      |
| zap           | Zapotec                     |
| zbl           | Blissymbols                 |
| zea           | Zeelandic                   |
| zen           | Zenaga                      |
| zgh           | Standard Moroccan Tamazight |
| zh            | Chinese                     |
| zu            | Zulu                        |
| zun           | Zuni                        |
| zza           | Zaza                        |

### List of supported script codes

| Script code | Name                        |
| ----------- | --------------------------- |
| Adlm        | Adlam                       |
| Afak        | Afaka                       |
| Aghb        | Caucasian Albanian          |
| Ahom        | Ahom                        |
| Arab        | Arabic                      |
| Armi        | Imperial Aramaic            |
| Armn        | Armenian                    |
| Avst        | Avestan                     |
| Bali        | Balinese                    |
| Bamu        | Bamum                       |
| Bass        | Bassa Vah                   |
| Batk        | Batak                       |
| Beng        | Bengali                     |
| Bhks        | Bhaiksuki                   |
| Blis        | Blissymbols                 |
| Bopo        | Bopomofo                    |
| Brah        | Brahmi                      |
| Brai        | Braille                     |
| Bugi        | Buginese                    |
| Buhd        | Buhid                       |
| Cakm        | Chakma                      |
| Cans        | Unified Canadian Aboriginal |
| Cari        | Carian                      |
| Cham        | Cham                        |
| Cher        | Cherokee                    |
| Chrs        | Chorasmian                  |
| Cirt        | Cirth                       |
| Copt        | Coptic                      |
| Cpmn        | Cypro-Minoan                |
| Cprt        | Cypriot                     |
| Cyrl        | Cyrillic                    |
| Deva        | Devanagari                  |
| Diak        | Dives Akuru                 |
| Dogr        | Dogra                       |
| Dsrt        | Deseret                     |
| Dupl        | Duployan                    |
| Egyd        | Egyptian demotic            |
| Egyh        | Egyptian hieratic           |
| Egyp        | Egyptian hieroglyphs        |
| Elba        | Elbasan                     |
| Elym        | Elymaic                     |
| Ethi        | Ethiopic                    |
| Geok        | Khutsuri                    |
| Geor        | Georgian                    |
| Glag        | Glagolitic                  |
| Gong        | Gunjala Gondi               |
| Gonm        | Masaram Gondi               |
| Goth        | Gothic                      |
| Gran        | Grantha                     |
| Grek        | Greek                       |
| Gujr        | Gujarati                    |
| Guru        | Gurmukhi                    |
| Hang        | Hangul                      |
| Hani        | Han                         |
| Hano        | Hanunoo                     |
| Hans        | Simplified                  |
| Hant        | Traditional                 |
| Hatr        | Hatran                      |
| Hebr        | Hebrew                      |
| Hira        | Hiragana                    |
| Hluw        | Anatolian Hieroglyphs       |
| Hmng        | Pahawh Hmong                |
| Hmnp        | Nyiakeng Puachue Hmong      |
| Hung        | Old Hungarian               |
| Inds        | Indus                       |
| Ital        | Old Italic                  |
| Java        | Javanese                    |
| Jurc        | Jurchen                     |
| Kali        | Kayah Li                    |
| Kana        | Katakana                    |
| Khar        | Kharoshthi                  |
| Khmr        | Khmer                       |
| Khoj        | Khojki                      |
| Kitl        | Khitan large script         |
| Kits        | Khitan small script         |
| Knda        | Kannada                     |
| Kpel        | Kpelle                      |
| Kthi        | Kaithi                      |
| Lana        | Tai Tham                    |
| Laoo        | Lao                         |
| Latn        | Latin                       |
| Leke        | Leke                        |
| Lepc        | Lepcha                      |
| Limb        | Limbu                       |
| Lina        | Linear A                    |
| Linb        | Linear B                    |
| Lisu        | Lisu                        |
| Loma        | Loma                        |
| Lyci        | Lycian                      |
| Lydi        | Lydian                      |
| Mahj        | Mahajani                    |
| Maka        | Makasar                     |
| Mand        | Mandaic                     |
| Mani        | Manichaean                  |
| Marc        | Marchen                     |
| Maya        | Mayan Hieroglyphs           |
| Medf        | Medefaidrin                 |
| Mend        | Mende Kikakui               |
| Merc        | Meroitic Cursive            |
| Mero        | Meroitic Hieroglyphs        |
| Mlym        | Malayalam                   |
| Modi        | Modi                        |
| Mong        | Mongolian                   |
| Moon        | Moon                        |
| Mroo        | Mro                         |
| Mtei        | Meitei Mayek                |
| Mult        | Multani                     |
| Mymr        | Myanmar (Burmese)           |
| Nand        | Nandinagari                 |
| Narb        | Old North Arabian           |
| Nbat        | Nabataean                   |
| Newa        | Newa                        |
| Nkdb        | Naxi Dongba                 |
| Nkgb        | Nakhi Geba                  |
| Nkoo        | N'ko                        |
| Nshu        | Nüshu                       |
| Ogam        | Ogham                       |
| Olck        | Ol Chiki                    |
| Orkh        | Old Turkic                  |
| Orya        | Oriya                       |
| Osge        | Osage                       |
| Osma        | Osmanya                     |
| Ougr        | Old Uyghur                  |
| Palm        | Palmyrene                   |
| Pauc        | Pau Cin Hau                 |
| Pcun        | Proto-Cuneiform             |
| Pelm        | Proto-Elamite               |
| Perm        | Old Permic                  |
| Phag        | Phags-pa                    |
| Phli        | Inscriptional Pahlavi       |
| Phlp        | Psalter Pahlavi             |
| Phlv        | Book Pahlavi                |
| Phnx        | Phoenician                  |
| Piqd        | Klingon                     |
| Plrd        | Miao                        |
| Prti        | Inscriptional Parthian      |
| Psin        | Proto-Sinaitic              |
| Ranj        | Ranjana                     |
| Rjng        | Rejang                      |
| Rohg        | Hanifi Rohingya             |
| Roro        | Rongorongo                  |
| Runr        | Runic                       |
| Samr        | Samaritan                   |
| Sara        | Sarati                      |
| Sarb        | Old South Arabian           |
| Saur        | Saurashtra                  |
| Sgnw        | SignWriting                 |
| Shaw        | Shavian                     |
| Shrd        | Sharada                     |
| Shui        | Shuishu                     |
| Sidd        | Siddham                     |
| Sind        | Khudawadi                   |
| Sinh        | Sinhala                     |
| Sogd        | Sogdian                     |
| Sogo        | Old Sogdian                 |
| Sora        | Sora Sompeng                |
| Soyo        | Soyombo                     |
| Sund        | Sundanese                   |
| Sylo        | Syloti Nagri                |
| Syrc        | Syriac                      |
| Tagb        | Tagbanwa                    |
| Takr        | Takri                       |
| Tale        | Tai Le                      |
| Talu        | New Tai Lue                 |
| Taml        | Tamil                       |
| Tang        | Tangut                      |
| Tavt        | Tai Viet                    |
| Telu        | Telugu                      |
| Teng        | Tengwar                     |
| Tfng        | Tifinagh                    |
| Tglg        | Tagalog                     |
| Thaa        | Thaana                      |
| Thai        | Thai                        |
| Tibt        | Tibetan                     |
| Tirh        | Tirhuta                     |
| Tnsa        | Tangsa                      |
| Toto        | Toto                        |
| Ugar        | Ugaritic                    |
| Vaii        | Vai                         |
| Visp        | Visible Speech              |
| Vith        | Vithkuqi                    |
| Wara        | Warang Citi                 |
| Wcho        | Wancho                      |
| Wole        | Woleai                      |
| Xpeo        | Old Persian                 |
| Xsux        | Cuneiform                   |
| Yezi        | Yezidi                      |
| Yiii        | Yi                          |
| Zanb        | Zanabazar Square            |

### List of supported country codes

| Country code | Name                                       |
| ------------ | ------------------------------------------ |
| AC           | Ascension Island                           |
| AD           | Andorra                                    |
| AE           | United Arab Emirates                       |
| AF           | Afghanistan                                |
| AG           | Antigua and Barbuda                        |
| AI           | Anguilla                                   |
| AL           | Albania                                    |
| AM           | Armenia                                    |
| AN           | Netherlands Antilles                       |
| AO           | Angola                                     |
| AQ           | Antarctica                                 |
| AR           | Argentina                                  |
| AS           | American Samoa                             |
| AT           | Austria                                    |
| AU           | Australia                                  |
| AW           | Aruba                                      |
| AX           | Åland Islands                              |
| AZ           | Azerbaijan                                 |
| BA           | Bosnia and Herzegovina                     |
| BB           | Barbados                                   |
| BD           | Bangladesh                                 |
| BE           | Belgium                                    |
| BF           | Burkina Faso                               |
| BG           | Bulgaria                                   |
| BH           | Bahrain                                    |
| BI           | Burundi                                    |
| BJ           | Benin                                      |
| BL           | St. Barthélemy                             |
| BM           | Bermuda                                    |
| BN           | Brunei                                     |
| BO           | Bolivia                                    |
| BQ           | Caribbean Netherlands                      |
| BR           | Brazil                                     |
| BS           | Bahamas                                    |
| BT           | Bhutan                                     |
| BV           | Bouvet Island                              |
| BW           | Botswana                                   |
| BY           | Belarus                                    |
| BZ           | Belize                                     |
| CA           | Canada                                     |
| CC           | Cocos (Keeling) Islands                    |
| CD           | Congo - Kinshasa                           |
| CF           | Central African Republic                   |
| CG           | Congo - Brazzaville                        |
| CH           | Switzerland                                |
| CI           | Côte d'Ivoire                              |
| CK           | Cook Islands                               |
| CL           | Chile                                      |
| CM           | Cameroon                                   |
| CN           | China                                      |
| CO           | Colombia                                   |
| CP           | Clipperton Island                          |
| CR           | Costa Rica                                 |
| CQ           | Island of Sark                             |
| CU           | Cuba                                       |
| CV           | Cabo Verde                                 |
| CW           | Curaçao                                    |
| CX           | Christmas Island                           |
| CY           | Cyprus                                     |
| CZ           | Czechia                                    |
| DE           | Germany                                    |
| DG           | Diego Garcia                               |
| DJ           | Djibouti                                   |
| DK           | Denmark                                    |
| DM           | Dominica                                   |
| DO           | Dominican Republic                         |
| DZ           | Algeria                                    |
| EA           | Ceuta and Melilla                          |
| EC           | Ecuador                                    |
| EE           | Estonia                                    |
| EG           | Egypt                                      |
| EH           | Western Sahara                             |
| ER           | Eritrea                                    |
| ES           | Spain                                      |
| ET           | Ethiopia                                   |
| EU           | European Union                             |
| EZ           | Eurozone                                   |
| FI           | Finland                                    |
| FJ           | Fiji                                       |
| FK           | Falkland Islands                           |
| FM           | Micronesia                                 |
| FO           | Faroe Islands                              |
| FR           | France                                     |
| FX           | France, Metropolitan                       |
| GA           | Gabon                                      |
| GB, UK       | United Kingdom                             |
| GD           | Grenada                                    |
| GE           | Georgia                                    |
| GF           | French Guiana                              |
| GG           | Guernsey                                   |
| GH           | Ghana                                      |
| GI           | Gibraltar                                  |
| GL           | Greenland                                  |
| GM           | Gambia                                     |
| GN           | Guinea                                     |
| GP           | Guadeloupe                                 |
| GQ           | Equatorial Guinea                          |
| GR           | Greece                                     |
| GS           | South Georgia and South Sandwich Islands   |
| GT           | Guatemala                                  |
| GU           | Guam                                       |
| GW           | Guinea-Bissau                              |
| GY           | Guyana                                     |
| HK           | Hong Kong                                  |
| HM           | Heard Island and McDonald Islands          |
| HN           | Honduras                                   |
| HR           | Croatia                                    |
| HT           | Haiti                                      |
| HU           | Hungary                                    |
| IC           | Canary Islands                             |
| ID           | Indonesia                                  |
| IE           | Ireland                                    |
| IL           | Israel                                     |
| IM           | Isle of Man                                |
| IN           | India                                      |
| IO           | British Indian Ocean Territory             |
| IQ           | Iraq                                       |
| IR           | Iran                                       |
| IS           | Iceland                                    |
| IT           | Italy                                      |
| JE           | Jersey                                     |
| JM           | Jamaica                                    |
| JO           | Jordan                                     |
| JP           | Japan                                      |
| KE           | Kenya                                      |
| KG           | Kyrgyzstan                                 |
| KH           | Cambodia                                   |
| KI           | Kiribati                                   |
| KM           | Comoros                                    |
| KN           | St. Kitts and Nevis                        |
| KP           | North Korea                                |
| KR           | South Korea                                |
| KW           | Kuwait                                     |
| KY           | Cayman Islands                             |
| KZ           | Kazakhstan                                 |
| LA           | Laos                                       |
| LB           | Lebanon                                    |
| LC           | St. Lucia                                  |
| LI           | Liechtenstein                              |
| LK           | Sri Lanka                                  |
| LR           | Liberia                                    |
| LS           | Lesotho                                    |
| LT           | Lithuania                                  |
| LU           | Luxembourg                                 |
| LV           | Latvia                                     |
| LY           | Libya                                      |
| MA           | Morocco                                    |
| MC           | Monaco                                     |
| MD           | Moldova                                    |
| ME           | Montenegro                                 |
| MF           | St. Martin                                 |
| MG           | Madagascar                                 |
| MH           | Marshall Islands                           |
| MK           | North Macedonia                            |
| ML           | Mali                                       |
| MM, BU       | Myanmar                                    |
| MN           | Mongolia                                   |
| MO           | Macao                                      |
| MP           | Northern Mariana Islands                   |
| MQ           | Martinique                                 |
| MR           | Mauritania                                 |
| MS           | Montserrat                                 |
| MT           | Malta                                      |
| MU           | Mauritius                                  |
| MV           | Maldives                                   |
| MW           | Malawi                                     |
| MX           | Mexico                                     |
| MY           | Malaysia                                   |
| MZ           | Mozambique                                 |
| NA           | Namibia                                    |
| NC           | New Caledonia                              |
| NE           | Niger                                      |
| NF           | Norfolk Island                             |
| NG           | Nigeria                                    |
| NI           | Nicaragua                                  |
| NL           | Netherlands                                |
| NO           | Norway                                     |
| NP           | Nepal                                      |
| NR           | Nauru                                      |
| NU           | Niue                                       |
| NZ           | New Zealand                                |
| OM           | Oman                                       |
| PA           | Panama                                     |
| PE           | Peru                                       |
| PF           | French Polynesia                           |
| PG           | Papua New Guinea                           |
| PH           | Philippines                                |
| PK           | Pakistan                                   |
| PL           | Poland                                     |
| PM           | St. Pierre and Miquelon                    |
| PN           | Pitcairn Islands                           |
| PR           | Puerto Rico                                |
| PS           | Palestine                                  |
| PT           | Portugal                                   |
| PW           | Palau                                      |
| PY           | Paraguay                                   |
| QA           | Qatar                                      |
| RE           | Réunion                                    |
| RO           | Romania                                    |
| RS           | Serbia                                     |
| RU           | Russia                                     |
| RW           | Rwanda                                     |
| SA           | Saudi Arabia                               |
| SB           | Solomon Islands                            |
| SC           | Seychelles                                 |
| SD           | Sudan                                      |
| SE           | Sweden                                     |
| SG           | Singapore                                  |
| SH           | St. Helena, Ascension and Tristan da Cunha |
| SI           | Slovenia                                   |
| SJ           | Svalbard and Jan Mayen                     |
| SK           | Slovakia                                   |
| SL           | Sierra Leone                               |
| SM           | San Marino                                 |
| SN           | Senegal                                    |
| SO           | Somalia                                    |
| SR           | Suriname                                   |
| SS           | South Sudan                                |
| ST           | Sao Tome and Principe                      |
| SV           | El Salvador                                |
| SX           | Sint Maarten                               |
| SY           | Syria                                      |
| SZ           | Eswatini                                   |
| TA           | Tristan da Cunha                           |
| TC           | Turks and Caicos Islands                   |
| TD           | Chad                                       |
| TF           | French Southern Territories                |
| TG           | Togo                                       |
| TH           | Thailand                                   |
| TJ           | Tajikistan                                 |
| TK           | Tokelau                                    |
| TL, TP       | Timor-Leste                                |
| TM           | Turkmenistan                               |
| TN           | Tunisia                                    |
| TO           | Tonga                                      |
| TR           | Turkey                                     |
| TT           | Trinidad and Tobago                        |
| TV           | Tuvalu                                     |
| TW           | Taiwan                                     |
| TZ           | Tanzania                                   |
| UA           | Ukraine                                    |
| UG           | Uganda                                     |
| UM           | U.S. Outlying Islands                      |
| US           | United States of America                   |
| UY           | Uruguay                                    |
| UZ           | Uzbekistan                                 |
| VA           | Holy See                                   |
| VC           | St. Vincent and the Grenadines             |
| VE           | Venezuela                                  |
| VG           | British Virgin Islands                     |
| VI           | U.S. Virgin Islands                        |
| VN           | Viet Nam                                   |
| VU           | Vanuatu                                    |
| WF           | Wallis and Futuna                          |
| WS           | Samoa                                      |
| XK, KV       | Kosovo                                     |
| YE           | Yemen                                      |
| YT           | Mayotte                                    |
| ZA           | South Africa                               |
| ZM           | Zambia                                     |
| ZW           | Zimbabwe                                   |

---

## Localization using gettext (PO files)

In addition to importing translations in CSV format, Godot also supports loading translation files written in the GNU gettext format (text-based `.po` and compiled `.mo`).

> **Note:** For an introduction to gettext, check out [A Quick Gettext Tutorial](https://www.labri.fr/perso/fleury/posts/programming/a-quick-gettext-tutorial.html). It's written with C projects in mind, but much of the advice also applies to Godot (with the exception of `xgettext`). For the complete documentation, see [GNU Gettext](https://www.gnu.org/software/gettext/manual/gettext.html).

### Advantages

- gettext is a standard format, which can be edited using any text editor or GUI editors such as [Poedit](https://poedit.net/). This can be significant as it provides a lot of tools for translators, such as marking outdated strings, finding strings that haven't been translated, etc.
- gettext is supported by translation platforms such as [Transifex](https://www.transifex.com/) and [Weblate](https://weblate.org/), which makes it easier for people to collaborate to localization.
- Compared to CSV, gettext files work better with version control systems like Git, as each locale has its own messages file.
- Multiline strings are more convenient to edit in gettext PO files compared to CSV files.

### Disadvantages

- gettext PO files have a more complex format than CSV and can be harder to grasp for people new to software localization.
- People who maintain localization files will have to install gettext tools on their system. However, as Godot supports using text-based message files (`.po`), translators can test their work without having to install gettext tools.
- gettext PO files usually use English as the base language. Translators will use this base language to translate to other languages. You could still user other languages as the base language, but this is not common.

### Installing gettext tools

The command line gettext tools are required to perform maintenance operations, such as updating message files. Therefore, it's strongly recommended to install them.

- **Windows:** Download an installer from [this page](https://mlocati.github.io/articles/gettext-iconv-windows.html). Any architecture and binary type (shared or static) works; if in doubt, choose the 64-bit static installer.
- **macOS:** Install gettext either using [Homebrew](https://brew.sh/) with the `brew install gettext` command, or using [MacPorts](https://www.macports.org/) with the `sudo port install gettext` command.
- **Linux:** On most distributions, install the `gettext` package from your distribution's package manager.

For a GUI tool you can get Poedit from its [Official website](https://poedit.net/). The basic version is open source and available under the MIT license.

### Creating the PO template

#### Automatic generation using the editor

The editor can generate a PO template automatically from specified scene and GDScript files. This POT generation also supports translation contexts and pluralization if used in a script, with the optional second argument of `tr()` and the `tr_n()` method.

Open Project > Project Settings > Localization > Template Generation, then use the Add… button to specify the path to your project's scenes and scripts that contain localizable strings:

After adding at least one scene or script, click Generate in the top-right corner, then specify the path to the output file with a `pot` file extension. This file can be placed anywhere in the project directory, but it's recommended to keep it in a subdirectory such as `locale`, as each locale will be defined in its own file.

See **below** for how to add comments for translators or exclude some strings from being added to the PO template for GDScript files.

You can then move over to **creating a messages file from a PO template**.

> **Note:** Remember to regenerate the PO template after making any changes to localizable strings, or after adding new scenes or scripts. Otherwise, newly added strings will not be localizable and translators won't be able to update translations for outdated strings.

#### Manual creation

If the automatic generation approach doesn't work out for your needs, you can create a PO template by hand in a text editor. This file can be placed anywhere in the project directory, but it's recommended to keep it in a subdirectory, as each locale will be defined in its own file.

Create a directory named `locale` in the project directory. In this directory, save a file named `messages.pot` with the following content:

Messages in gettext are made of `msgid` and `msgstr` pairs. `msgid` is the source string (usually in English), `msgstr` will be the translated string.

> **Warning:** The `msgstr` value in PO template files (`.pot`) should **always** be empty. Localization will be done in the generated `.po` files instead.

### Creating a messages file from a PO template

The `msginit` command is used to turn a PO template into a messages file. For instance, to create a French localization file, use the following command while in the `locale` directory:

```shell
msginit --no-translator --input=messages.pot --locale=fr
```

The command above will create a file named `fr.po` in the same directory as the PO template.

Alternatively, you can do that graphically using Poedit, or by uploading the POT file to your web platform of choice.

### Loading a messages file in Godot

To register a messages file as a translation in a project, open the Project Settings, then go to Localization > Translations, click Add… then choose the `.po` or `.mo` file in the file dialog. The locale will be inferred from the `"Language: <code>\n"` property in the messages file.

> **Note:** See Internationalizing games for more information on importing and testing translations in Godot.

### Updating message files to follow the PO template

After updating the PO template, you will have to update message files so that they contain new strings, while removing strings that are no longer present in the PO template. This can be done automatically using the `msgmerge` tool:

```shell
# The order matters: specify the message file *then* the PO template!
msgmerge --update --backup=none fr.po messages.pot
```

If you want to keep a backup of the original message file (which would be saved as `fr.po~` in this example), remove the `--backup=none` argument.

> **Note:** After running `msgmerge`, strings which were modified in the source language will have a "fuzzy" comment added before them in the `.po` file. This comment denotes that the translation should be updated to match the new source string, as the translation will most likely be inaccurate until it's updated. Strings with "fuzzy" comments will **not** be read by Godot until the translation is updated and the "fuzzy" comment is removed.

### Checking the validity of a PO file or template

It is possible to check whether a gettext file's syntax is valid.

If you open with Poeditor, it will display the appropriate warnings if there's some syntax errors. You can also verify by running the gettext command below:

```shell
msgfmt fr.po --check
```

If there are syntax errors or warnings, they will be displayed in the console. Otherwise, `msgfmt` won't output anything.

### Using binary MO files (useful for large projects only)

For large projects with several thousands of strings to translate or more, it can be worth it to use binary (compiled) MO message files instead of text-based PO files. Binary MO files are smaller and faster to read than the equivalent PO files.

You can generate an MO file with the command below:

```shell
msgfmt fr.po --no-hash -o fr.mo
```

If the PO file is valid, this command will create an `fr.mo` file besides the PO file. This MO file can then be loaded in Godot as described above.

The original PO file should be kept in version control so you can update your translation in the future. In case you lose the original PO file and wish to decompile an MO file into a text-based PO file, you can do so with:

```shell
msgunfmt fr.mo > fr.po
```

The decompiled file will not include comments or fuzzy strings, as these are never compiled in the MO file in the first place.

### Extracting localizable strings from GDScript files

The built-in [editor plugin](https://github.com/godotengine/godot/blob/master/modules/gdscript/editor/gdscript_translation_parser_plugin.h) recognizes a variety of patterns in source code to extract localizable strings from GDScript files, including but not limited to the following:

- `tr()`, `tr_n()`, `atr()`, and `atr_n()` calls;
- assigning properties `text`, `placeholder_text`, and `tooltip_text`;
- `add_tab()`, `add_item()`, `set_tab_title()`, and other calls;
- `FileDialog` filters like `"*.png ; PNG Images"`.

> **Note:** The argument or right operand must be a constant string, otherwise the plugin will not be able to evaluate the expression and will ignore it.

If the plugin extracts unnecessary strings, you can ignore them with the `NO_TRANSLATE` comment. You can also provide additional information for translators using the `TRANSLATORS:` comment. These comments must be placed either on the same line as the recognized pattern or precede it.

### Using context

The `context` parameter can be used to differentiate the situation where a translation is used, or to differentiate polysemic words (words with multiple meanings).

For example:

In a gettext PO file, a string with a context can be defined as follows:

### Updating PO files

Some time or later, you'll add new content to our game, and there will be new strings that need to be translated. When this happens, you'll need to update the existing PO files to include the new strings.

First, generate a new POT file containing all the existing strings plus the newly added strings. After that, merge the existing PO files with the new POT file. There are two ways to do this:

- Use a gettext editor, and it should have an option to update a PO file from a POT file.
- Use the gettext `msgmerge` tool:

```shell
# The order matters: specify the message file *then* the PO template!
msgmerge --update --backup=none fr.po messages.pot
```

If you want to keep a backup of the original message file (which would be saved as `fr.po~` in this example), remove the `--backup=none` argument.

### POT generation custom plugin

If you have any extra file format to deal with, you could write a custom plugin to parse and and extract the strings from the custom file. This custom plugin will extract the strings and write into the POT file when you hit **Generate POT**. To learn more about how to create the translation parser plugin, see [EditorTranslationParserPlugin](../godot_csharp_editor.md).

---

## Localization using spreadsheets

Spreadsheets are one of the most common formats for localizing games. In Godot, spreadsheets are supported through the CSV format. This guide explains how to work with CSVs.

The CSV files **must** be saved with UTF-8 encoding without a [byte order mark](https://en.wikipedia.org/wiki/Byte_order_mark).

> **Warning:** By default, Microsoft Excel will always save CSV files with ANSI encoding rather than UTF-8. There is no built-in way to do this, but there are workarounds as described [here](https://stackoverflow.com/questions/4221176/excel-to-csv-with-utf8-encoding). We recommend using [LibreOffice](https://www.libreoffice.org/) or Google Sheets instead.

### Formatting

CSV files must be formatted as follows:

| keys | <lang1> | <lang2> | <langN> |
| ---- | ------- | ------- | ------- |
| KEY1 | string  | string  | string  |
| KEY2 | string  | string  | string  |
| KEYN | string  | string  | string  |

The "lang" tags must represent a language, which must be one of the valid locales supported by the engine, or they must start with an underscore (`_`), which means the related column is served as comment and won't be imported. The `KEY` tags must be unique and represent a string universally. By convention, these are usually in uppercase to differentiate them from other strings. These keys will be replaced at runtime by the matching translated string. Note that the case is important: `KEY1` and `Key1` will be different keys. The top-left cell is ignored and can be left empty or having any content. Here's an example:

| keys  | en                    | es                     | ja                           |
| ----- | --------------------- | ---------------------- | ---------------------------- |
| GREET | Hello, friend!        | Hola, amigo!           | こんにちは                   |
| ASK   | How are you?          | Cómo está?             | 元気ですか                   |
| BYE   | Goodbye               | Adiós                  | さようなら                   |
| QUOTE | "Hello" said the man. | "Hola" dijo el hombre. | 「こんにちは」男は言いました |

The same example is shown below as a comma-separated plain text file, which should be the result of editing the above in a spreadsheet. When editing the plain text version, be sure to enclose with double quotes any message that contains commas, line breaks or double quotes, so that commas are not parsed as delimiters, line breaks don't create new entries and double quotes are not parsed as enclosing characters. Be sure to escape any double quotes a message may contain by preceding them with another double quote. Alternatively, you can select another delimiter than comma in the import options.

```none
keys,en,es,ja
GREET,"Hello, friend!","Hola, amigo!",こんにちは
ASK,How are you?,Cómo está?,元気ですか
BYE,Goodbye,Adiós,さようなら
QUOTE,"""Hello"" said the man.","""Hola"" dijo el hombre.",「こんにちは」男は言いました
```

#### Specifying plural forms

Since Godot 4.6, it is possible to specify plural forms in CSV files.

This is done by adding a column named `?plural` anywhere in the table (except on the first column, which is reserved for translation keys). By convention, it's recommended to place it on the second column. Note that in the example below, the key column is the one that contains English localization.

```none
en,?plural,fr,ru,ja,zh
?pluralrule,,nplurals=2; plural=(n >= 2);,,
There is %d apple,There are %d apples,Il y a %d pomme,Есть %d яблоко,リンゴが%d個あります,那里有%d个苹果
,,Il y a %d pommes,Есть %d яблока,,
,,,Есть %d яблок,,
```

> **Note:** Automatic Control translation is not supported when using plural forms. You must translate the string manually using [tr_n()](../godot_csharp_misc.md).

#### Specifying translation contexts

Since Godot 4.6, it is possible to specify translation contexts in CSV files. This can be used to disambiguate identical source strings that have different meanings. While this is generally not needed when using translation keys `LIKE_THIS`, it's useful when using plain English text as translation keys.

This is done by adding a column named `?context` column anywhere in the table (except on the first column, which is reserved for translation keys). By convention, it's recommended to place it on the second column, or after `?plural` if it's also used. Note that in the example below, the key column is the one that contains English localization.

```none
en,?context,fr,ru,ja,zh
Letter,Alphabet,Lettre,Буква,字母,字母
Letter,Message,Courrier,Письмо,手紙,信件
```

> **Note:** Automatic Control translation is not supported when using context. You must translate the string manually using [tr()](../godot_csharp_misc.md) or [tr_n()](../godot_csharp_misc.md).

### CSV importer

Godot will treat CSV files as translations by default. It will import them and generate one or more compressed translation resource files next to it.

Importing will also add the translation to the list of translations to load when the game runs, specified in project.godot (or the project settings). Godot allows loading and removing translations at runtime as well.

Select the `.csv` file and access the Import dock to define import options. You can toggle the compression of the imported translations, and select the delimiter to use when parsing the CSV file.

Be sure to click Reimport after any change to these options.

### Loading the CSV file as a translation

Once a CSV file is imported, it is **not** automatically registered as a translation source for the project. Remember to follow the steps described in Configuring the imported translation so that the translation is actually used when running the project.

---
