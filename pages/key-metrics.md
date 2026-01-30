---
layout: new-section
sectionImage: 'https://centralesupelec.venture.fr/wp-content/uploads/2023/06/cropped-Logo-CentraleSupelecVenture-VBk.png'
---


# 🔢 Les nombres que tout développeur back-end devrait connaître

Chiffres utiles pour conception, SLOs et dimensionnement.

---

## Latence et Percentiles

- Objectif SLO courant: **P95 < 200ms**, **P99 < 500ms** pour endpoints critiques.
- P50 (médiane) utile pour debug mais P95/P99 plus pertinents pour UX.

## Disponibilité & Erreurs

- Objectif disponibilité: **99.9% (trois 9)** = ~43.8 minutes d'indisponibilité/an.
- 99.99% (quatre 9) = ~52.6 minutes/an? (correction: 52.56 minutes/année pour 99.9) — vérifiez selon période.
- Taux d'erreur acceptable: **<0.1%** pour endpoints critiques.

## Cache & Capacité

- Cache hit ratio cible: **> 90%** pour caches d'objets; **> 70%** acceptable selon coût.
- Taille moyenne payload HTTP: **~1-10 KB** (API JSON); optimisez si >> 100 KB.

## Throughput & Dimensionnement

- RPS par cœur CPU (approx): **~500-2000 req/s** dépendant du framework et complexité.
- Règle pratique: dimensionner pour la charge P95 et ajouter 25-50% de marge.

## Connexions DB & Pools

- Pool DB: typedef: **min 10, max 100** selon application; ne pas dépasser nombre de connexions que la BD peut gérer.
- Recommandation: mesurer latence DB et adapter pool en conséquence.

## Timeouts & Retries

- Timeout HTTP interne: **500ms - 2s** selon call; pour appels réseaux lointains augmenter.
- Retry: **exponential backoff** avec jitter; max 3 tentatives pour opérations idempotentes.

## Sécurité & Auth

- Token expiration: Access tokens **~15min - 1h**, refresh tokens plus longs (jours).
- Password hashing: cible **< 1s** par hash pour bonne UX; augmentez selon infra.

## Coût approximatif

- Règle: stateless + JWT réduit coût infra; persistance/sessions augmente charges DB.
- Estimation: 10k RPS stateless peut nécessiter **~2-5 serveurs** selon CPU/RAM.

---

## Où mesurer

- Mesurez P95/P99, erreurs, saturation CPU, GC pauses et latence GC pour Java.
- Gardez dashboards: latency (p50/p95/p99), error rate, saturation, throughput, queue lengths.

---

## Conseils rapides

- Prioriser P99 pour endpoints critiques (paiement, login).  
- Documenter SLOs et procédures d'alerte.  
- Revoir les nombres trimestriellement.

**Sources & lectures**: SRE literature (Google SRE book), TechEmpower, cloud provider docs.
