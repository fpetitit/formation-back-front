---
layout: new-section
sectionImage: 'https://centralesupelec.venture.fr/wp-content/uploads/2023/06/cropped-Logo-CentraleSupelecVenture-VBk.png'
---

# Microservices

---

## Microservices: Introduction

Architectures distribuées basées sur des services indépendants.

```mermaid
graph LR
                            Client["Client<br/>(Web/Mobile)"]
                            Gateway["API Gateway"]
                            
                            ServiceContract["Service Contrats<br/>(Port 3001)"]
                            ServiceClaim["Service Sinistres<br/>(Port 3002)"]
                            ServiceCustomer["Service Clients<br/>(Port 3003)"]
                            ServiceNotif["Service Notifications<br/>(Port 3004)"]
                            
                            DBContract["Base Contrats"]
                            DBClaim["Base Sinistres"]
                            DBCustomer["Base Clients"]
                            
                            Client -->|HTTP| Gateway
                            Gateway -->|Route| ServiceContract
                            Gateway -->|Route| ServiceClaim
                            Gateway -->|Route| ServiceCustomer
                            
                            ServiceContract --> DBContract
                            ServiceClaim --> DBClaim
                            ServiceCustomer --> DBCustomer
                            
                            ServiceContract -.->|Event| ServiceNotif
                            ServiceClaim -.->|Event| ServiceNotif
                            
                            style Client fill:#e8f4ff
                            style Gateway fill:#fff9e8
                            style ServiceContract fill:#ffe8f4
                            style ServiceClaim fill:#e8ffe8
                            style ServiceCustomer fill:#f4e8ff
                            style ServiceNotif fill:#ffebe8
```

---

## Caractéristiques des Microservices

### Propriétés clés:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>

#### 🎯 Autonomie

- Services indépendants
- Déploiement indépendant
- BD dédiée
- Équipes autonomes

#### 📡 Communication

- API REST / gRPC
- Message brokers (Kafka)
- Events asynchrones
- Découverte de services

</div>
<div>

#### 🔄 Résilience

- Circuit breaker
- Timeout
- Retry policy
- Health checks

#### 📊 Observabilité

- Logging distribué
- Tracing
- Monitoring
- Alerting

</div>
</div>

---

## API Gateway et Service Discovery

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>

### API Gateway (point d'entrée unique):

- Routage: Diriger requêtes aux services corrects
- Authentification: JWT validation
- Rate limiting: Protection DOS
- Caching: Réduire latence
- Load balancing: Distribuer charge

</div>
<div>

```mermaid
graph TB
                            Client["Client"]
                            Gateway["API Gateway<br/>(Kong, AWS API Gateway)"]
                            
                            Eureka["Service Discovery<br/>(Eureka, Consul)"]
                            
                            Serv1["Service 1<br/>Port 3001"]
                            Serv2["Service 2<br/>Port 3002"]
                            Serv3["Service 3<br/>Port 3003"]
                            
                            Client -->|Request| Gateway
                            Gateway -->|Query services| Eureka
                            Eureka -->|Retourne addresses| Gateway
                            Gateway -->|Route| Serv1
                            Gateway -->|Route| Serv2
                            Gateway -->|Route| Serv3
                            
                            Serv1 -->|Register| Eureka
                            Serv2 -->|Register| Eureka
                            Serv3 -->|Register| Eureka
                            
                            style Client fill:#e8f4ff
                            style Gateway fill:#fff9e8
                            style Eureka fill:#ffe8f4
                            style Serv1 fill:#e8ffe8
                            style Serv2 fill:#e8ffe8
                            style Serv3 fill:#e8ffe8
```
</div>
</div>

---

## Communication inter-services

### Approches de communication:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>

#### 🔵 Synchrone (REST/gRPC)

```plaintext
Service A
   ↓ (HTTP/gRPC)
Service B
   ↓ (attend réponse)
Service C
   ↓
Réponse retourne

Avantages:
✅ Cohérence immédiate
✅ Facile à déboguer

Inconvénients:
❌ Couplage fort
❌ Service lent = tout lent
```

</div>
<div>

#### 🟣 Asynchrone (Events)

```plaintext
Service A
   ↓ (Publie event)
Kafka/RabbitMQ
   ↓ (Message broker)
Service B (reçoit)
Service C (reçoit)

Avantages:
✅ Découplage complet
✅ Haute disponibilité
✅ Scalabilité

Inconvénients:
❌ Eventual consistency
❌ Plus complexe
```
</div>
</div>

---

## Saga Pattern: Transactions distribuées

#### Deux approches:

Maintenir la cohérence des données sur plusieurs services

- Choreography: Services écoutent les events et réagissent (loose coupling)
- Orchestration: Service central coordonne les étapes (plus simple mais couplage)

```mermaid
graph LR
                            User["Client crée contrat"]
                            
                            Saga1["Saga Step 1<br/>Service Contrats:<br/>Créer contrat"]
                            Saga2["Saga Step 2<br/>Service Client:<br/>Vérifier client"]
                            Saga3["Saga Step 3<br/>Service Paiement:<br/>Débiter prime"]
                            Saga4["Saga Step 4<br/>Service Notif:<br/>Envoyer email"]
                            
                            Success["✅ Contrat créé"]
                            Rollback["❌ Rollback si erreur"]
                            
                            User -->|Initiate| Saga1
                            Saga1 -->|OK| Saga2
                            Saga2 -->|OK| Saga3
                            Saga3 -->|OK| Saga4
                            Saga4 -->|OK| Success
                            
                            Saga2 -->|ERREUR| Rollback
                            Rollback -->|Undo Saga1| Saga1
                            
                            style User fill:#e8f4ff
                            style Success fill:#e8ffe8
                            style Rollback fill:#ffe8f4
```

---

# 🏗️ Microservices: Choreography vs Orchestration

---

## Définitions et Comparaison

### Choreography

```mermaid
graph LR
    A["Service A"] -->|Événement| B["Broker"]
    B -->|Événement| C["Service B"]
    B -->|Événement| D["Service C"]
    C -->|Événement| B
    D -->|Événement| B

    style A fill:#e8f4ff
    style B fill:#ffe8f4
    style C fill:#fff9e8
    style D fill:#e8ffe8
```

### Orchestration

```mermaid
graph TD
    A["Orchestrateur"] --> B["Service A"]
    A --> C["Service B"]
    A --> D["Service C"]
    B --> A
    C --> A
    D --> A

    style A fill:#ffd700
    style B fill:#e8f4ff
    style C fill:#fff9e8
    style D fill:#e8ffe8
```

---

## Critères de Choix

| Critère | Choreography | Orchestration |
|---|---|---|
| **Couplage** | ✅ Faible | ❌ Fort |
| **Complexité** | ⚠️ Élevée | ✅ Modérée |
| **Flexibilité** | ✅ Élevée | ⚠️ Limitée |
| **Visibilité** | ❌ Difficile | ✅ Claire |
| **Maintenance** | ❌ Complexe | ✅ Simple |

### Outils Populaires

- **Choreography**: Kafka, RabbitMQ, AWS EventBridge
- **Orchestration**: Zeebe, Cadence, AWS Step Functions

---

## Implémentation Pratique


<div style="display: grid; grid-template-columns: .5fr 1fr; gap: 30px; margin-top: 0px;">

### Choreography avec Kafka

```mermaid
sequenceDiagram
    participant Client
    participant ServiceA
    participant Kafka
    participant ServiceB

    Client->>ServiceA: Requête initiale
    ServiceA->>Kafka: Publie événement
    Kafka->>ServiceB: Consomme événement
    ServiceB->>Kafka: Publie résultat
    Kafka->>ServiceA: Consomme résultat
    ServiceA->>Client: Réponse finale
```
</div>

---

<div style="display: grid; grid-template-columns: .5fr 1fr; gap: 30px; margin-top: 0px;">

### Orchestration avec Zeebe

```mermaid
sequenceDiagram
    participant Client
    participant Orchestrateur
    participant ServiceA
    participant ServiceB

    Client->>Orchestrateur: Requête
    Orchestrateur->>ServiceA: Appel
    ServiceA->>Orchestrateur: Réponse
    Orchestrateur->>ServiceB: Appel
    ServiceB->>Orchestrateur: Réponse
    Orchestrateur->>Client: Résultat final
```
</div>