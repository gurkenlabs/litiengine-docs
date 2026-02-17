---
meta.description: "Overview of GuiComponents in LITIENGINE - buttons, labels, sliders, checkboxes, and other UI elements for game interfaces."
meta.keywords: "LITIENGINE, GUI, component, button, label, slider, menu, Java"
---

# GuiComponents: An Overview

LITIENGINE provides a comprehensive GUI framework for creating menus, HUDs, and in-game interfaces. All GUI components extend `GuiComponent`, which provides positioning, rendering, and input handling.

## Component Hierarchy

```
GuiComponent (abstract)
  ├── Button
  ├── CheckBox
  ├── ImageComponent
  ├── Label
  ├── ListField
  ├── Menu
  ├── Slider
  ├── SpeechBubble
  ├── TextFieldComponent
  └── DropdownListField
```

## Common Properties

All GuiComponents share these base properties:

```java
component.setX(100);
component.setY(50);
component.setWidth(200);
component.setHeight(40);

component.setVisible(true);
component.setEnabled(true);
component.setSuspended(false);

component.setText("Hello");
component.setForeground(Color.WHITE);
component.setBackground(Color.DARK_GRAY);
```

## Core Components

### Label

Display static or dynamic text:

```java
Label label = new Label("Score: 0");
label.setFont(Resources.fonts().get("gamefont.ttf", 24f));
label.setForeground(Color.WHITE);
```

### Button

Clickable button with text or image:

```java
Button button = new Button("Start Game");
button.onClicked(e -> {
  Game.screens().display("GAME");
});
```

### CheckBox

Toggleable checkbox:

```java
CheckBox checkbox = new CheckBox("Enable Sound", true);
checkbox.onChecked(e -> {
  Game.audio().setSoundVolume(e.isChecked() ? 1.0f : 0.0f);
});
```

### Slider

Draggable value selector:

```java
Slider slider = new Slider(0, 100, 1);
slider.setValue(50);
slider.onChange(e -> {
  int volume = (int) slider.getCurrentValue();
  Game.audio().setMusicVolume(volume / 100f);
});
```

### TextFieldComponent

Text input field:

```java
TextFieldComponent textField = new TextFieldComponent();
textField.setText("Enter name...");
textField.onTextChanged(e -> {
  playerName = textField.getText();
});
```

### ListField

Scrollable list of items:

```java
ListField<String> list = new ListField<>(Arrays.asList("Option 1", "Option 2", "Option 3"));
list.onChange(e -> {
  String selected = list.getSelectedObject();
});
```

### DropdownListField

Dropdown selection:

```java
DropdownListField<String> dropdown = new DropdownListField<>(options);
dropdown.onChange(e -> {
  String selected = dropdown.getSelectedObject();
});
```

## Component Events

All components support common events:

```java
// Mouse events
component.onClicked(e -> { /* clicked */ });
component.onMousePressed(e -> { /* mouse down */ });
component.onMouseReleased(e -> { /* mouse up */ });
component.onMouseMoved(e -> { /* mouse moved */ });
component.onHovered(e -> { /* mouse entered */ });
component.onLeave(e -> { /* mouse left */ });

// Focus events
component.onFocused(e -> { /* gained focus */ });
component.onFocusLost(e -> { /* lost focus */ });
```

## Adding Components to Screens

```java
public class MenuScreen extends Screen {
  
  @Override
  protected void initializeComponents() {
    Button startButton = new Button("Start");
    startButton.setX(100);
    startButton.setY(100);
    startButton.onClicked(e -> startGame());
    
    this.getComponents().add(startButton);
  }
}
```

## Component Appearance

### Fonts

```java
component.setFont(Resources.fonts().get("font.ttf", 24f));
component.setTextAlignment(TextAlignment.CENTER);
```

### Colors

```java
component.setForeground(Color.WHITE);
component.setBackground(new Color(0, 0, 0, 180)); // Semi-transparent
component.setBorderColor(Color.GRAY);
component.setBorderThickness(2);
```

### Images

```java
ImageComponent image = new ImageComponent();
image.setImage(Resources.images().get("background.png"));
```

## Layout

### Manual Positioning

```java
component.setX(100);
component.setY(50);
component.setWidth(200);
component.setHeight(40);
```

### Anchor Points

```java
component.setAnchor(Location.CENTER);
component.setMarginTop(10);
component.setMarginLeft(20);
```

## Visibility and State

```java
// Show/hide
component.setVisible(false);

// Enable/disable interaction
component.setEnabled(false);

// Suspend updates (for performance)
component.setSuspended(true);
```

## Creating Custom Components

Extend `GuiComponent` for custom UI elements:

```java
public class HealthBar extends GuiComponent {
  
  private int currentHealth;
  private int maxHealth;
  
  public HealthBar(int x, int y, int width, int height) {
    super(x, y, width, height);
    this.maxHealth = 100;
    this.currentHealth = 100;
  }
  
  @Override
  public void render(Graphics2D g) {
    super.render(g);
    
    // Draw background
    g.setColor(Color.DARK_GRAY);
    g.fillRect(getX(), getY(), getWidth(), getHeight());
    
    // Draw health
    g.setColor(Color.RED);
    float healthPercent = (float) currentHealth / maxHealth;
    g.fillRect(getX(), getY(), (int)(getWidth() * healthPercent), getHeight());
  }
  
  public void setHealth(int health) {
    this.currentHealth = Math.max(0, Math.min(maxHealth, health));
  }
}
```

## See Also

- [Creating Menus](/docs/user-interface/creating-menus/) - Building complete menus
- [Screens](/docs/game-api/screens/) - Screen management
