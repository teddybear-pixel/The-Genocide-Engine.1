# Configuration

## What is configuration?

Configuration stores settings that control how the program operates.

Code = what the system does.

Configuration = how the system is set up to operate.

## Why do we need it?

Instead of putting changeable settings throughout the code, we keep them in a central place.

## Examples

- Environment settings
- Data paths
- Logging level
- Simulation settings
- Random seed
- Feature settings

## Key Concept

Configuration allows us to change how the system operates without changing the underlying system logic.

## THE GENOCIDE ENGINE

The configuration system will become more important as the engine grows and more settings are introduced.

# Logging

## What is logging?

Logging records information about what the program is doing while it runs.

Code = what the system does.

Logging = a record of what the system is doing.

## Why do we need it?

As THE GENOCIDE ENGINE grows, many different components will be running and changing state.

Logging helps us understand what happened while the program was running.

## Examples

- Program started
- Configuration loaded
- World state initialized
- Something unexpected happened
- An error occurred
- A system component completed an operation

## Key Concept

Logging allows us to observe and troubleshoot the program while it runs without relying only on `print()` statements.

## THE GENOCIDE ENGINE

Logging will become more important as the engine grows and more components interact with each other.

# Typed Data Models

## What are typed data models?

Typed data models define what kind of information the program expects and how that information is organized.

Code = what the system does.

Data model = what information the system works with.

## Why do we need them?

THE GENOCIDE ENGINE will work with many different types of entities and information.

Data models give that information a consistent structure.

## Examples

- Person
- Family
- Community
- Population
- Region
- Organization
- Event
- Location
- Resource

## Key Concept

Typed data models give the system a clear and predictable structure for representing information.

## THE GENOCIDE ENGINE

Typed data models will eventually form the foundation of the World State Core and allow the system to represent entities and their changing state.

# Reproducible Test Data

## What is reproducible test data?

Reproducible test data is fixed, known data that can be used repeatedly during development and testing.

Code = what the system does.

Test data = the known information we use to test the system.

## Why do we need it?

Using the same test data allows us to run tests repeatedly and know that the results should be consistent.

## Examples

- Sample entities
- Sample populations
- Sample events
- Sample locations
- Sample world states

## Key Concept

Reproducible test data makes testing consistent and helps us know whether changes to the code actually work.

## THE GENOCIDE ENGINE

Reproducible test data will allow us to test the engine using known scenarios before working with more complex or real-world data.

# Basic CLI / API Interface

## What is a CLI?

A CLI (Command-Line Interface) allows us to interact with the program through the terminal.

Code = what the system does.

CLI = how we can interact with the system from the terminal.

## Why do we need it?

A CLI gives us a simple way to start the program, provide commands or settings, and eventually run different parts of the engine.

## Examples

- Start the engine
- Check the version
- Run a simulation
- Load a dataset
- Run a test scenario

## What is an API?

An API (Application Programming Interface) allows different software components to communicate with each other.

We are only establishing the basic interface foundation during Phase 0.

## Key Concept

A CLI gives humans a way to interact with the system.

An API gives software a way to interact with the system.

## THE GENOCIDE ENGINE

The interface will eventually provide ways to start, control, inspect, and interact with different parts of the engine.