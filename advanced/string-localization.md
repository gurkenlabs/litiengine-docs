---
meta.description: "Learn how to implement string localization in LITIENGINE for multi-language game support."
meta.keywords: "LITIENGINE, localization, i18n, translation, language, strings, Java"
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
Button startButton = new Button(Resources.strings().get("menu.start"));
```

## Setting Locale

```java
// Set locale before loading resources
Locale.setDefault(Locale.GERMAN);

// Or configure in code
Resources.strings().setLocale(Locale.FRENCH);
```

## Fallback Behavior

If a key is missing in the current locale, the engine falls back to the default `strings.properties` file.

## Best Practices

1. **Use consistent key naming**: `category.subcategory.item`
2. **Keep default file complete**: All keys should exist in `strings.properties`
3. **Don't concatenate strings**: Avoid `"Hello " + name` (word order varies by language)

## See Also

- [Resource Management](/docs/resource-management/README/) - Loading resources
- [User Interface](/docs/user-interface/README/) - Building UIs
