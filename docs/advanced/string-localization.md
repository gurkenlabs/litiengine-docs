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

// With formatted parameters (e.g. welcome=Welcome, {0}!)
String welcome = Resources.strings().get("welcome", playerName);
```

## Setting Locale

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

## Fallback Behavior

If a key is missing in the current locale, the engine falls back to the default `strings.properties` file.

## Best Practices

1. **Use consistent key naming**: `category.subcategory.item`
2. **Keep default file complete**: All keys should exist in `strings.properties`
3. **Don't concatenate strings**: Avoid `"Hello " + name` (word order varies by language)

## See Also

- [Resource Management](../resource-management/README.md) - Loading resources
- [User Interface](../user-interface/README.md) - Building UIs
