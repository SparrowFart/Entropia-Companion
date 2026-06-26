---

# ChatGPT Workflow

When assisting with this project:

1. Read `AI_INSTRUCTIONS.md` first.
2. Read `PROJECT_STATE.md`.
3. Read `DECISIONS.md`.
4. Read `ROADMAP.md`.
5. Read `FEATURES.md`.
6. Read `DATABASE.md`.
7. Read `CHANGELOG.md`.

Before making significant code changes:

* Understand the existing implementation.
* Reuse existing systems where possible.
* Avoid duplicate functionality.
* Explain architectural changes before implementing them.

When a coding session ends:

* Suggest updates to the documentation if needed.
* Ensure the project remains internally consistent.

The goal is to leave the repository in a better state after every session.


# Entropia Companion - AI Development Guide

## Project Vision

The goal of this project is to build the best desktop companion available for Entropia Universe.

The application should eventually become a complete planning and analysis tool that allows a player to understand exactly where they are, where they are going, and what equipment or skills they should work towards next.

The application must be modular, fast, easy to maintain and designed to continue growing for years.

---

# Primary Objectives

The application will eventually support:

* Entropia Nexus synchronization
* Avatar skill tracking
* Weapon database
* Armor database
* Amplifier database
* Healing tool database
* Creature database
* Mining database
* Crafting database
* Mission tracking
* Codex tracking
* Economy tracking
* Equipment comparison
* Skill requirement calculator
* Upgrade planner
* Hunting cost calculator
* Mining planner
* Crafting planner
* Loot analysis
* Profit/Loss tracking
* Best weapon recommendations
* Best armor recommendations
* "What should I use next?" planning

The architecture must always support future expansion.

---

# Development Philosophy

Always improve the project.

Never rewrite working systems unless requested.

Never introduce unnecessary complexity.

Choose readable code over clever code.

Keep functions focused on a single responsibility.

Build reusable modules whenever possible.

Think long-term.

---

# Before Writing Code

Always read:

1. PROJECT_STATE.md
2. ROADMAP.md
3. DECISIONS.md
4. DATABASE.md
5. FEATURES.md
6. CHANGELOG.md

Understand the current architecture before making changes.

---

# Documentation Rules

Whenever functionality changes:

* Update PROJECT_STATE.md
* Update FEATURES.md
* Update CHANGELOG.md

Whenever priorities change:

* Update ROADMAP.md

Whenever architecture changes:

* Update DECISIONS.md

Whenever database changes:

* Update DATABASE.md

Documentation is part of the project.

---

# Architecture Rules

Avoid tightly coupled code.

Keep modules independent.

Avoid circular imports.

Avoid global variables unless absolutely necessary.

Database access should remain centralized.

Business logic should not be mixed with UI code.

UI should display information.

Logic should calculate information.

Database should store information.

---

# Coding Standards

Use descriptive names.

Keep functions short.

Keep files organized.

Avoid duplicated logic.

Comment non-obvious code.

Prefer maintainability over micro-optimizations.

Follow existing naming conventions.

---

# Git Workflow

After completing work:

1. Update documentation.
2. Test the application.
3. Commit changes.
4. Push to GitHub.

Commit messages should clearly describe the work completed.

---

# Decision Making

When multiple approaches exist:

Prefer the solution that:

* scales better
* is easier to maintain
* is easier to understand
* avoids technical debt

Do not choose shortcuts that make future development harder.

---

# Long-Term Goal

Create the definitive companion application for Entropia Universe.

Every feature should move the project closer to that goal.
