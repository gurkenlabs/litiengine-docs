---
meta.description: "Network communication was removed from LITIENGINE in version 0.5.1-beta."
meta.keywords: "LITIENGINE, network, multiplayer, removed"
---

# Network Communication

> **Note:** Network communication was removed from LITIENGINE in version 0.5.1-beta.

As the engine's networking code had been unmaintained, untested, and had security concerns, the networking package was removed from LITIENGINE.

## Alternatives

For multiplayer functionality, consider these alternatives:

- Implement custom networking using Java's `java.net` package
- Use third-party networking libraries like Netty or Kryonet
- Design your game architecture to communicate with a dedicated server

## Historical Reference

If you're interested in the historical implementation, you can find the removed networking code in older versions of the engine on [GitHub](https://github.com/gurkenlabs/litiengine).

## See Also

- [Release notes v0.5.1-beta](/docs/CHANGELOG/) - Removal announcement
