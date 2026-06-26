Entropia Companion - AI Development Guide

---

# 🚨 READ THIS FIRST

This file is the operating manual for any AI assistant working on this repository.

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

Do not create duplicate systems.

Do not remove features unless explicitly requested.

Every coding session should leave the project in a better state than it was before.

---

# User Workflow Rules

The project owner prefers:

* One step at a time.
* Short, direct instructions.
* No long explanations unless requested.
* Full file replacements when code changes are needed.
* Beginner-friendly comments in code when helpful.
* No unnecessary redesigns.
* No guessing when requirements are unclear.

If a step-by-step setup is being done, give **one step only**, then wait for confirmation.

---

# Project Vision

The goal is to build the ultimate desktop companion application for **Entropia Universe**.

The application should help the player answer questions such as:

* What should I use next?
* Which weapon is best for my current skills?
* Which armor is most economical?
* What creatures should I hunt?
* What skills do I still need?
* How far am I from using this weapon properly?
* How much will my next upgrade cost?
* Which setup gives the best efficiency?
* What is the cheapest or smartest progression path?

The application should become a complete planning, tracking and analysis tool.

---

# Core Purpose

The application must allow the player to make better Entropia Universe decisions using:

* avatar skills
* weapon data
* armor data
* amplifier data
* healing tool data
* creature data
* costs
* efficiency
* skill requirements
* progression goals

The main long-term feature is:

> Given my current skills and resources, what should I use next?

---

# Long-Term Goals

The application should eventually support:

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
* Skill gap calculator
* Upgrade planner
* Hunting planner
* Mining planner
* Crafting planner
* Weapon recommendations
* Armor recommendations
* Creature recommendations
* Setup recommendations
* Complete equipment statistics
* Future modular expansion

---

# Required Equipment Statistics

The system must eventually support detailed item and equipment stats, including but not limited to:

* ammo burn
* damage
* attacks per minute
* damage per second
* damage per PEC
* efficiency
* durability
* range
* reload
* SIB
* profession requirements
* hit ability
* critical hit ability
* maxed/unmaxed status
* skill requirements
* enhancer slots
* amplifier compatibility
* decay
* total cost per shot
* total cost per kill
* effective damage
* markup impact

---

# Skill Planning Requirements

The system must eventually be able to answer:

* Can I use this weapon effectively?
* Is this weapon maxed for me?
* What skills/professions do I still need?
* How far off am I from using it properly?
* What should I skill next?
* What is the next efficient weapon for me?
* Which weapon gives the best value for my current skills?
* Which setup is too advanced for me?
* Which setup is wasting PED?

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

Never hard-code data that belongs in the database.

Prefer clear service modules over large all-in-one files.

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

Prefer full file replacements when giving code to the project owner.

---

# Workflow Before Implementing Features

Before implementing a feature:

1. Understand the current implementation.
2. Check whether a similar system already exists.
3. Extend existing systems before creating new ones.
4. Check whether database changes are needed.
5. Explain major architectural changes before implementing them.

---

# Workflow After Implementing Features

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

# Database Rules

SQLite is the local database unless the project owner decides otherwise.

Do not commit local `.db` files.

Database schema changes must be documented in `DATABASE.md`.

Database access should be centralized.

Avoid scattering raw SQL throughout the project.

Use clear table names and field names.

Design tables for future expansion.

---

# API Rules

Entropia Nexus synchronization is a long-term goal.

API code should be isolated from UI code.

API response handling should be clean and testable.

Do not hard-code API secrets.

Do not commit tokens, passwords or `.env` files.

If API data is stored locally, document where and how.

---

# Recommendation Engine Rules

The recommendation system should be built carefully.

It should consider:

* player skills
* maxed/unmaxed status
* weapon efficiency
* cost per shot
* damage output
* markup
* amplifier compatibility
* creature choice
* survivability
* long-term progression

Do not build this as one giant function.

Use small calculation modules that can be tested and improved.

---

# Decision Making

When multiple solutions exist, prefer the one that:

* is easier to understand
* is easier to maintain
* scales better
* avoids future rewrites
* minimizes technical debt
* keeps data, logic and UI separated

Do not optimize prematurely.

Build for the future without over-engineering.

---

# Communication

When suggesting major changes, explain:

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

Never commit local database files unless explicitly requested.

Keep `.gitignore` up to date.

---

# Project Success

The project is successful if it helps the player make better decisions inside Entropia Universe.

Every new feature should move the project closer to that goal.

Quality is more important than speed.

Maintainability is more important than cleverness.

The project should remain understandable years from now by a developer seeing it for the first time.
