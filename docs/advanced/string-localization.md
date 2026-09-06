---
title: String Localization
icon: lucide/languages
description: Learn how to implement string localization in LITIENGINE for multi-language
  game support.
keywords: [LITIENGINE, localization, i18n, translation, language, strings, Java]
tags: [localization, i18n, translations, languages, strings]
---
# String Localization

LITIENGINE provides built-in support for string localization, allowing you to create multi-language games.

## How Localization Works

1. Create properties files for each language (`strings_en.properties`, `strings_de.properties`)
2. Access strings via `Resources.strings().get("key")`
3. Engine selects appropriate file based on locale

## Creating Language Files

### Default Language (strings.properties)

```properties
game.title=My Game
menu.start=Start Game
menu.settings=Settings
menu.quit=Quit
enemy.goblin=Goblin
item.sword=Iron Sword
```

### German (strings_de.properties)

```properties
game.title=Mein Spiel
menu.start=Spiel starten
menu.settings=Einstellungen
menu.quit=Beenden
enemy.goblin=Goblin
item.sword=Eisenschwert
```

## Loading Strings

```java
// Get localized string
String title = Resources.strings().get("game.title");
String startText = Resources.strings().get("menu.start");

// Use in UI
Button startButton = new Button(50, 50, 180, 40);
startButton.setText(Resources.strings().get("menu.start"));

// With formatted parameters (e.g. welcome=Welcome, {0}! You have {1} gold.)
String welcome = Resources.strings().get("welcome", playerName, goldAmount);
```

### UTF-8 Character Encoding

By default, Java `.properties` resource bundles use `ISO-8859-1`. To support full UTF-8 characters (e.g. Japanese, Cyrillic, special symbols), configure string encoding during initialization:

```java
import java.nio.charset.StandardCharsets;

Resources.strings().setEncoding(StandardCharsets.UTF_8);
```

### Modular String Bundles

For large projects, organize strings into dedicated bundles (e.g. `dialogue.properties`, `items.properties`, `quests.properties`):

```java
// Fetch from a specific bundle (e.g. dialogue_de.properties)
String npcLine = Resources.strings().getFrom("dialogue", "elder.greeting");
String questObjective = Resources.strings().getFrom("quests", "main.step1", targetName);
```

## Setting Locale & Runtime Language Switching

Configure the game locale via client configuration or JVM defaults:

```java
// Set language and country via configuration
Game.config().client().setLanguage("de");
Game.config().client().setCountry("DE");

// Or configure in config.properties:
// cl_language=de
// cl_country=DE

// Or set default JVM locale before Game.init()
Locale.setDefault(Locale.GERMAN);
```

### Dynamic Language Switching at Runtime

Because `Resources.strings()` evaluates `Game.config().client().getLocale()` dynamically, switching languages at runtime takes effect immediately for subsequent calls. You can refresh active UI screens in response to an options menu change:

```java
public void switchLanguage(String languageCode, String countryCode) {
  Game.config().client().setLanguage(languageCode);
  Game.config().client().setCountry(countryCode);

  // Refresh active screen components with the newly selected locale
  if (Game.screens().current() != null) {
    Game.screens().current().getComponents().forEach(c -> {
      // Re-apply localized text to buttons, labels, and dialogs
    });
  }
}
```

## Fallback Behavior

If a key is missing in the current locale (e.g. `strings_de.properties`), the engine automatically falls back to the default `strings.properties` resource bundle.

## Best Practices

1. **Use consistent hierarchical keys**: `category.subcategory.item` (e.g. `ui.menu.btn_play`, `item.weapon.iron_sword`).
2. **Keep the default bundle complete**: All keys should exist in `strings.properties` as the universal fallback.
3. **Never concatenate localized strings**: Avoid `"Hello " + name + ", you scored " + score`. Different languages use different word orders; always use `MessageFormat` tokens `{0}`, `{1}`.
4. **Use UTF-8**: Enable `Resources.strings().setEncoding(StandardCharsets.UTF_8)` when supporting non-Latin alphabets.

## See Also

- [Resource Management](../resource-management/README.md) - Loading resources into `.litidata`
- [User Interface](../user-interface/README.md) - Building GUI components and menus
- [Configuration](../configuration/README.md) - Engine and client configuration settings
