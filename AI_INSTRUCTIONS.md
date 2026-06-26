# Entropia Companion - AI Development Guide

---

# 🚨 READ THIS FIRST

Before writing **any** code:

1. Read this file completely.
2. Read `PROJECT_STATE.md`.
3. Read `DECISIONS.md`.
4. Read `ROADMAP.md`.
5. Read `FEATURES.md`.
6. Read `DATABASE.md`.
7. Read `CHANGELOG.md`.

Do **not** assume anything about the project.

Understand the existing architecture before making changes.

Reuse existing systems whenever possible.

Do not redesign working systems unless explicitly requested.

Every coding session should leave the project in a better state than it was before.

---

# Project Vision

The goal of this project is to build the ultimate desktop companion application for **Entropia Universe**.

The application should help a player answer questions such as:

* What should I use next?
* Which weapon is best for my current skills?
* Which armor is most economical?
* What creatures should I hunt?
* What skills do I still need?
* How much will my next upgrade cost?
* Which setup gives me the best efficiency?

The application should become a complete planning and analysis tool.

---

# Long-Term Goals

The application will eventually support:

* Entropia Nexus synchronization
* Avatar synchronization
* Skill tracking
* Skill history
* Weapon database
* Armor database
* Amplifier database
* Healing tool database
* Creature database
* Mining database
* Crafting database
* Mission tracking
* Codex tracking
* Loot tracking
* Profit/Loss tracking
* Economy analysis
* Equipment comparison
* Skill requirement calculator
* Upgrade planner
* Hunting planner
* Mining planner
* Crafting planner
* "What should I use next?" recommendations
* Complete equipment statistics
* Future expansion through modular architecture

---

# Development Principles

Always think long-term.

Choose maintainability over shortcuts.

Readable code is better than clever code.

Keep the project modular.

Avoid technical debt whenever possible.

Avoid unnecessary complexity.

Every feature should be designed so additional features can be added later without requiring a rewrite.

---

# Architecture Rules

Keep responsibilities separated.

UI displays information.

Business logic performs calculations.

Database stores information.

API layer communicates with external services.

Avoid tightly coupled code.

Avoid circular imports.

Keep modules independent.

Database access should remain centralized.

Never mix UI code with business logic.

---

# Coding Standards

Use descriptive names.

Write self-explanatory code.

Comment complex logic.

Keep functions focused on one responsibility.

Avoid duplicated code.

Reuse existing utilities whenever possible.

Follow the project's existing naming conventions.

Never introduce breaking changes without explanation.

---

# Workflow

Before implementing a feature:

1. Understand the current implementation.
2. Check whether a similar system already exists.
3. Extend existing systems before creating new ones.
4. Explain major architectural changes before implementing them.

After implementing a feature:

1. Test it.
2. Verify existing functionality still works.
3. Update documentation.
4. Commit changes.
5. Push to GitHub.

---

# Documentation Rules

Documentation is part of the project.

Whenever functionality changes:

* Update `PROJECT_STATE.md`
* Update `FEATURES.md`
* Update `CHANGELOG.md`

Whenever priorities change:

* Update `ROADMAP.md`

Whenever architecture changes:

* Update `DECISIONS.md`

Whenever the database changes:

* Update `DATABASE.md`

If new documentation is required, create it.

Never allow documentation to become outdated.

---

# Decision Making

When multiple solutions exist, prefer the one that:

* is easier to understand
* is easier to maintain
* scales better
* avoids future rewrites
* minimizes technical debt

Do not optimize prematurely.

Build for the future without over-engineering.

---

# Communication

When suggesting major changes:

Explain:

* why the change is needed
* advantages
* disadvantages
* possible alternatives

Do not silently redesign existing systems.

If requirements are unclear, ask before making assumptions.

---

# Git Workflow

Use meaningful commit messages.

Keep commits focused on a single logical change.

Never commit temporary files.

Never commit virtual environments.

Never commit secrets, passwords or API keys.

Keep `.gitignore` up to date.

---

# Project Success

The project is successful if it helps a player make better decisions inside Entropia Universe.

Every new feature should move the project closer to that goal.

Quality is more important than speed.

Maintainability is more important than cleverness.

The project should remain understandable years from now by a developer seeing it for the first time.
