# DCS Platform Basics

Load this file when the user asks for conceptual guidance, onboarding training, or the basic meaning of DCS-related platform objects.

## Choose The Right Change Model

- Light extension
  - For simple customization of standard products
  - Can be used directly in production
  - Best for simple field, layout, visibility, lock, or required-flag adjustments
- Custom extension
  - For more complex extensions to standard products
  - Should follow the normal test-to-production deployment flow
- Custom development
  - For new apps or deeper custom solutions
  - Also follows the full test-to-production deployment flow

Do not route light-extension changes into the DCS patch flow unless the user has a very specific documented reason.

## Environment Choices

- Lightweight dev environment
  - Good for learning, personal use, or teams smaller than about 5 people
  - Runs on Windows or Mac
  - Lower resource cost
- Container environment
  - Better for larger teams, UAT, or production-like setups
  - Higher resource requirement
  - Requires stronger ops support

## CosmicStudio

- CosmicStudio is the one-stop developer tool for installing and managing development environments.
- It is not for production deployment.
- It can install 金蝶AI星空 development environments and centralize dev resources.

## Core Platform Objects

- Cloud
  - A business domain or solution domain, such as finance or procurement
- App
  - A solution unit under a cloud
- Page
  - A concrete UI object under an app
- Metadata
  - The design-time description of those objects

## Cloud And App Management

- Cloud management covers cloud creation, modification, delete, and git or SVN sync.
- App management covers:
  - self-built apps
  - original apps
  - third-party apps
  - menu management
  - business objects
  - page management
  - import or export
  - extension or inheritance

## Designer Anatomy

The page designer is organized around:

- design views
- function buttons such as save and preview
- control toolbox
- design canvas
- property panel

Important ideas:

- Prefer business fields when they fit. Use generic controls only when needed.
- XML view exposes the generated page metadata.
- Preview is the fastest way to verify the design before packaging.

## Form And List Basics

- Bill pages automatically create:
  - form
  - list
  - mobile form
  - mobile list
- Bills are good for flow data and prebuilt save or query behavior.
- Lists map fields from the form entity and are configured inside the list design view.

## Plugin Development Basics

- Use the IDEA helper for Gradle project initialization.
- Use the dev server to download platform dependencies and support local debug.
- Run `DebugApplication.java` for local debug after the helper project is ready.

## Educational Walkthrough Pattern

When the user asks to learn DCS, teach in this order:

1. light extension versus custom extension versus custom development
2. cloud, app, and page model
3. designer basics
4. project creation and repo creation
5. metadata push and build
6. quality and publish
