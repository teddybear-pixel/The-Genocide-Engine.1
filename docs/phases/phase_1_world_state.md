# Phase 1 - World State Core 

# Phase 1 — World State Core

## Goal

Create the foundational representation of the world that THE GENOCIDE ENGINE models.

The system must be able to represent entities, their state, and changes to that state over time.

## Phase 1 Principles

- The world is represented as data.
- Entities have state.
- State can change.
- Changes happen over time.
- World state should be testable.
- Keep the first version simple.
- Do not build risk, causality, simulation, intervention, or prevention systems yet.

## Core Concepts

### Entities

The world can contain different types of entities.

Examples:

- Person
- Family
- Community
- Population
- Region
- Organization
- Institution
- Infrastructure
- Resource
- Event
- Location

### State

Entities have properties that describe their current condition.

Example:

Population:

- Size
- Displacement
- Food access
- Water access
- Healthcare access
- Security
- Child vulnerability

The exact properties will evolve as development continues.

The important concept is:

Entities have state.

State can change.

### World State

The World State represents the condition of the modeled world at a particular point in time.

WorldState(t0)

The state can change when something happens.

WorldState(t0)
      ↓
    Event
      ↓
WorldState(t1)

Eventually:

WorldState(t0)
      ↓
    Event
      ↓
WorldState(t1)
      ↓
    Event
      ↓
WorldState(t2)
      ↓
    Event
      ↓
WorldState(t3)

## Phase 1 Components

### Entity Representation

Represent the different entities that can exist within the modeled world.

### Entity State

Represent the properties and conditions associated with entities.

### World State

Represent the overall state of the modeled world.

### Events

Represent things that happen and can cause changes to the world.

### State Changes

Represent how an entity or the wider world changes after an event.

### Time

Represent when world states and events occur.

## Phase 1 Development Order

1. Entity representation
2. Entity state
3. World state
4. Events
5. State changes
6. Time
7. Testing the complete state-change process

## Phase 1 Completion Criteria

### 1. Entities can be represented

- [ ] Define what an entity is in the system.
- [ ] Create the basic entity data model.
- [ ] Give entities unique identifiers.
- [ ] Add basic identifying information.
- [ ] Create initial entity types.
- [ ] Write tests proving entities can be created and stored.

### 2. Entity state can be represented

- [ ] Define what "state" means for an entity.
- [ ] Determine which properties belong to entity state.
- [ ] Add state to the entity representation.
- [ ] Support different values and data types.
- [ ] Test that entity state can be created and accessed.
- [ ] Test that entity state can change.

### 3. A World State can be represented

- [ ] Define what the World State contains.
- [ ] Create a World State model.
- [ ] Allow entities to exist within the World State.
- [ ] Give the World State a point in time.
- [ ] Test that a World State can be created.
- [ ] Test that entities can exist inside it.

### 4. Events can be represented

- [ ] Define what an event is.
- [ ] Determine the information an event needs.
- [ ] Create an Event model.
- [ ] Give events a time.
- [ ] Identify which entities an event affects.
- [ ] Test that events can be created and represented.

### 5. Events can produce state changes

- [ ] Define how an event affects entity state.
- [ ] Connect events to the entities they affect.
- [ ] Implement the process of applying an event.
- [ ] Produce an updated state after an event.
- [ ] Test that the expected state change occurs.

### 6. Changes can occur over time

- [ ] Define how time is represented.
- [ ] Establish an initial world state.
- [ ] Apply events in chronological order.
- [ ] Produce new world states as changes occur.
- [ ] Test multiple state changes over time.
- [ ] Verify that earlier states remain understandable and traceable.

### 7. World State changes can be tested

- [ ] Create reproducible test scenarios.
- [ ] Create an initial World State.
- [ ] Apply known events.
- [ ] Check the resulting World State.
- [ ] Test multiple entities and changes.
- [ ] Test expected and unexpected situations.
- [ ] Ensure tests are repeatable.

### 8. Phase 1 documentation is complete

- [ ] Document the World State Core.
- [ ] Document entity concepts.
- [ ] Document entity state.
- [ ] Document events.
- [ ] Document state changes.
- [ ] Document time.
- [ ] Document important design decisions.
- [ ] Update the Phase 1 roadmap as development progresses.
- [ ] Record what was learned during implementation.

## Result

The computer can represent a world and how that world changes over time.